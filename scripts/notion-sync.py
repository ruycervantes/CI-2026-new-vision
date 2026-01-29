#!/usr/bin/env python3
"""Sync markdown files to Notion pages under a parent page."""

import argparse
import os
import re
import sys
import time

import mistune
import requests
import yaml

NOTION_API = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"
CHUNK_SIZE = 100  # Notion API limit for appending blocks

NETLIFY_BASE = "https://stoic-2026.netlify.app"
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/ruycervantes/CI-2026-new-vision/master"

# Maps relative .md paths (from repo root) to Notion page URLs — populated at runtime
NOTION_PAGE_URLS = {}  # e.g. {"core/vision.md": "https://www.notion.so/<page_id>"}


def load_config(path="scripts/notion-sync-config.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)


def notion_headers(api_key):
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_VERSION,
    }


# --- Image and link URL resolution ---

def resolve_image_url(img_path, source_file):
    """Convert a relative image path to an absolute URL."""
    # Resolve relative to the source markdown file's directory
    source_dir = os.path.dirname(source_file)
    resolved = os.path.normpath(os.path.join(source_dir, img_path))

    # If it's under site/, use Netlify (site/ is the publish dir, so strip "site/")
    if resolved.startswith("site/"):
        return f"{NETLIFY_BASE}/{resolved[5:]}"

    # Everything else: use GitHub raw
    return f"{GITHUB_RAW_BASE}/{resolved}"


def resolve_link_url(href, source_file):
    """Convert a relative .md link to a Notion page URL if available, else absolute URL."""
    if href.startswith(('http://', 'https://')):
        return href

    # Resolve to repo-root-relative path
    source_dir = os.path.dirname(source_file)
    resolved = os.path.normpath(os.path.join(source_dir, href))

    # Check if this file is in our Notion page map
    if resolved in NOTION_PAGE_URLS:
        return NOTION_PAGE_URLS[resolved]

    # Not a synced page — return None (render as plain text)
    return None


# --- Rich text parsing ---

def parse_inline(text, source_file=""):
    """Convert markdown inline formatting to Notion rich_text objects."""
    if not text:
        return []

    # Strip image syntax from inline text (images handled separately in md_to_blocks)
    text = re.sub(r'!\[([^\]]*)\]\([^)]+\)', r'\1', text)

    segments = []
    # Pattern handles: bold+italic, bold, italic, inline code, links
    pattern = re.compile(
        r'(\*\*\*(.+?)\*\*\*)'       # bold+italic
        r'|(\*\*(.+?)\*\*)'           # bold
        r'|(\*(.+?)\*)'               # italic
        r'|(`(.+?)`)'                 # inline code
        r'|(\[([^\]]+)\]\(([^)]+)\))' # link
    )

    last = 0
    for m in pattern.finditer(text):
        # plain text before match
        if m.start() > last:
            segments.append(rich_text(text[last:m.start()]))

        if m.group(2):  # bold+italic
            segments.append(rich_text(m.group(2), bold=True, italic=True))
        elif m.group(4):  # bold
            segments.append(rich_text(m.group(4), bold=True))
        elif m.group(6):  # italic
            segments.append(rich_text(m.group(6), italic=True))
        elif m.group(8):  # code
            segments.append(rich_text(m.group(8), code=True))
        elif m.group(10):  # link
            href = m.group(11)
            resolved = resolve_link_url(href, source_file)
            if resolved:
                segments.append(rich_text(m.group(10), link=resolved))
            else:
                segments.append(rich_text(m.group(10)))

        last = m.end()

    if last < len(text):
        segments.append(rich_text(text[last:]))

    return segments if segments else [rich_text(text)]


def rich_text(content, bold=False, italic=False, code=False, link=None):
    """Create a Notion rich_text object."""
    # Notion limit: 2000 chars per rich_text
    content = content[:2000]
    rt = {
        "type": "text",
        "text": {"content": content},
        "annotations": {
            "bold": bold,
            "italic": italic,
            "code": code,
        },
    }
    if link:
        rt["text"]["link"] = {"url": link}
    return rt


# --- Markdown to Notion blocks ---

def md_to_blocks(md_text, source_file=""):
    """Convert markdown text to Notion block objects."""
    blocks = []
    lines = md_text.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]

        # Image line: ![alt](path)
        img_match = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)\s*$', line)
        if img_match:
            alt_text = img_match.group(1)
            img_path = img_match.group(2)
            url = resolve_image_url(img_path, source_file)
            blocks.append({
                "object": "block",
                "type": "image",
                "image": {
                    "type": "external",
                    "external": {"url": url},
                    "caption": [{"type": "text", "text": {"content": alt_text}}] if alt_text else [],
                }
            })
            i += 1
            continue

        # Code block
        if line.startswith('```'):
            lang = line[3:].strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing ```
            code_content = '\n'.join(code_lines)
            # Notion limit: 2000 chars per rich_text in code block
            if len(code_content) > 2000:
                # Split into multiple code blocks
                for chunk_start in range(0, len(code_content), 2000):
                    chunk = code_content[chunk_start:chunk_start + 2000]
                    blocks.append({
                        "object": "block",
                        "type": "code",
                        "code": {
                            "rich_text": [{"type": "text", "text": {"content": chunk}}],
                            "language": lang or "plain text",
                        }
                    })
            else:
                blocks.append({
                    "object": "block",
                    "type": "code",
                    "code": {
                        "rich_text": [{"type": "text", "text": {"content": code_content}}],
                        "language": lang or "plain text",
                    }
                })
            continue

        # Table
        if '|' in line and i + 1 < len(lines) and re.match(r'\s*\|[\s\-:|]+\|\s*$', lines[i + 1]):
            table_rows = []
            # Header row
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            table_rows.append(cells)
            i += 1  # skip header
            i += 1  # skip separator
            while i < len(lines) and '|' in lines[i] and lines[i].strip().startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                table_rows.append(cells)
                i += 1
            # Build table block
            width = max(len(r) for r in table_rows)
            children = []
            for row in table_rows:
                # Pad row to width
                padded = row + [''] * (width - len(row))
                children.append({
                    "type": "table_row",
                    "table_row": {
                        "cells": [parse_inline(cell, source_file) for cell in padded]
                    }
                })
            blocks.append({
                "object": "block",
                "type": "table",
                "table": {
                    "table_width": width,
                    "has_column_header": True,
                    "has_row_header": False,
                    "children": children,
                }
            })
            continue

        # Divider
        if re.match(r'^---+\s*$', line):
            blocks.append({"object": "block", "type": "divider", "divider": {}})
            i += 1
            continue

        # Headings
        if line.startswith('### '):
            blocks.append(heading_block(3, line[4:], source_file))
            i += 1
            continue
        if line.startswith('## '):
            blocks.append(heading_block(2, line[3:], source_file))
            i += 1
            continue
        if line.startswith('# '):
            blocks.append(heading_block(1, line[2:], source_file))
            i += 1
            continue

        # Blockquote
        if line.startswith('> '):
            blocks.append({
                "object": "block",
                "type": "quote",
                "quote": {"rich_text": parse_inline(line[2:], source_file)}
            })
            i += 1
            continue

        # Bulleted list
        if re.match(r'^[\-\*]\s', line):
            blocks.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {"rich_text": parse_inline(line.lstrip('-* '), source_file)}
            })
            i += 1
            continue

        # Indented bullet (2-4 spaces)
        if re.match(r'^  [\-\*]\s', line):
            blocks.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {"rich_text": parse_inline(line.strip().lstrip('-* '), source_file)}
            })
            i += 1
            continue

        # Numbered list
        if re.match(r'^\d+\.\s', line):
            text = re.sub(r'^\d+\.\s', '', line)
            blocks.append({
                "object": "block",
                "type": "numbered_list_item",
                "numbered_list_item": {"rich_text": parse_inline(text, source_file)}
            })
            i += 1
            continue

        # Empty line → skip
        if not line.strip():
            i += 1
            continue

        # Paragraph (default)
        blocks.append({
            "object": "block",
            "type": "paragraph",
            "paragraph": {"rich_text": parse_inline(line, source_file)}
        })
        i += 1

    return blocks


def heading_block(level, text, source_file=""):
    key = f"heading_{level}"
    return {
        "object": "block",
        "type": key,
        key: {"rich_text": parse_inline(text.strip(), source_file)},
    }


# --- Notion API operations ---

def search_page(title, parent_id, headers):
    """Search for existing page by title under parent."""
    resp = requests.post(f"{NOTION_API}/search", headers=headers, json={
        "query": title,
        "filter": {"property": "object", "value": "page"},
    })
    resp.raise_for_status()
    for page in resp.json().get("results", []):
        # Check title matches and parent matches
        props = page.get("properties", {})
        title_prop = props.get("title", {}).get("title", [])
        page_title = "".join(t.get("plain_text", "") for t in title_prop)
        parent = page.get("parent", {})
        parent_page = parent.get("page_id", "").replace("-", "")
        if page_title == title and parent_page == parent_id.replace("-", ""):
            return page["id"]
    return None


def delete_all_children(page_id, headers):
    """Delete all blocks from a page."""
    resp = requests.get(f"{NOTION_API}/blocks/{page_id}/children?page_size=100", headers=headers)
    resp.raise_for_status()
    for block in resp.json().get("results", []):
        requests.delete(f"{NOTION_API}/blocks/{block['id']}", headers=headers)
    # Handle pagination
    while resp.json().get("has_more"):
        cursor = resp.json()["next_cursor"]
        resp = requests.get(
            f"{NOTION_API}/blocks/{page_id}/children?page_size=100&start_cursor={cursor}",
            headers=headers,
        )
        resp.raise_for_status()
        for block in resp.json().get("results", []):
            requests.delete(f"{NOTION_API}/blocks/{block['id']}", headers=headers)


def create_page(title, parent_id, headers):
    """Create a new page under parent."""
    resp = requests.post(f"{NOTION_API}/pages", headers=headers, json={
        "parent": {"page_id": parent_id},
        "properties": {
            "title": [{"text": {"content": title}}],
        },
    })
    resp.raise_for_status()
    return resp.json()["id"]


def append_blocks(page_id, blocks, headers):
    """Append blocks in chunks of CHUNK_SIZE."""
    for i in range(0, len(blocks), CHUNK_SIZE):
        chunk = blocks[i:i + CHUNK_SIZE]
        resp = requests.patch(
            f"{NOTION_API}/blocks/{page_id}/children",
            headers=headers,
            json={"children": chunk},
        )
        if resp.status_code == 429:
            retry_after = int(resp.headers.get("Retry-After", 1))
            print(f"  Rate limited, waiting {retry_after}s...")
            time.sleep(retry_after)
            resp = requests.patch(
                f"{NOTION_API}/blocks/{page_id}/children",
                headers=headers,
                json={"children": chunk},
            )
        if resp.status_code >= 400:
            print(f"  Error appending chunk {i//CHUNK_SIZE + 1}: {resp.status_code}")
            print(f"  {resp.json().get('message', resp.text[:200])}")
            # Try blocks one by one to find the bad one
            for j, block in enumerate(chunk):
                r = requests.patch(
                    f"{NOTION_API}/blocks/{page_id}/children",
                    headers=headers,
                    json={"children": [block]},
                )
                if r.status_code >= 400:
                    print(f"  Bad block {i+j}: {block.get('type')} — {r.json().get('message', '')[:120]}")
                if r.status_code == 429:
                    time.sleep(int(r.headers.get("Retry-After", 1)))


def sync_file(file_path, title, parent_id, headers, dry_run=False):
    """Sync a single markdown file to Notion."""
    full_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), file_path)
    if not os.path.exists(full_path):
        print(f"  SKIP: {file_path} not found")
        return False

    with open(full_path) as f:
        md_text = f.read()

    blocks = md_to_blocks(md_text, source_file=file_path)
    print(f"  {file_path} → \"{title}\" ({len(blocks)} blocks)")

    if dry_run:
        return True

    # Find or create page
    page_id = search_page(title, parent_id, headers)
    if page_id:
        print(f"  Updating existing page {page_id}")
        delete_all_children(page_id, headers)
    else:
        page_id = create_page(title, parent_id, headers)
        print(f"  Created new page {page_id}")

    # Update cross-link map with this page's ID
    NOTION_PAGE_URLS[file_path] = f"https://www.notion.so/{page_id.replace('-', '')}"

    append_blocks(page_id, blocks, headers)
    print(f"  Done ({len(blocks)} blocks synced)")
    return True


def main():
    parser = argparse.ArgumentParser(description="Sync markdown files to Notion")
    parser.add_argument("--file", help="Sync only this file (path relative to repo root)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without making API calls")
    parser.add_argument("--config", default="scripts/notion-sync-config.yaml", help="Config file path")
    args = parser.parse_args()

    config = load_config(args.config)
    api_key = os.environ.get(config["notion_api_key_env"])
    if not api_key and not args.dry_run:
        print(f"Error: Set {config['notion_api_key_env']} environment variable")
        sys.exit(1)

    headers = notion_headers(api_key) if api_key else {}
    parent_id = config["parent_page_id"]
    pages = config["pages"]

    if args.file:
        pages = [p for p in pages if p["file"] == args.file]
        if not pages:
            print(f"Error: {args.file} not found in config")
            sys.exit(1)

    if args.dry_run:
        print("DRY RUN — no changes will be made\n")

    # Build cross-link map: find or create all pages first
    if not args.dry_run:
        print("Building cross-link map...")
        all_pages = config["pages"]
        for p in all_pages:
            page_id = search_page(p["title"], parent_id, headers)
            if page_id:
                notion_url = f"https://www.notion.so/{page_id.replace('-', '')}"
                NOTION_PAGE_URLS[p["file"]] = notion_url
        print(f"  Found {len(NOTION_PAGE_URLS)} existing pages for cross-linking\n")

    print(f"Syncing {len(pages)} file(s) to Notion parent {parent_id}\n")

    synced = 0
    for page in pages:
        ok = sync_file(page["file"], page["title"], parent_id, headers, dry_run=args.dry_run)
        if ok:
            synced += 1

    print(f"\n{'Would sync' if args.dry_run else 'Synced'} {synced}/{len(pages)} files")


if __name__ == "__main__":
    main()
