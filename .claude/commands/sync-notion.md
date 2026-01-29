---
name: sync-notion
description: Sync markdown docs to Notion pages. Converts headings, tables, images, and cross-doc links. Use after editing core docs to update Notion.
---

# /sync-notion - Sync markdown docs to Notion

Syncs core markdown documents to Notion pages under "Vision, Roadmap and Docs 2026" (`2f7073cafffb8038bcf7f4335612b1e2`).

## Instructions

### Step 1: Determine scope

- If user specifies a file (e.g., `/sync-notion core/vision.md`), sync only that file
- If no argument, sync all 6 configured files

### Step 2: Run the sync

```bash
export $(cat .env | xargs) && python3 scripts/notion-sync.py
```

For a single file:
```bash
export $(cat .env | xargs) && python3 scripts/notion-sync.py --file $ARGUMENTS
```

### Step 3: Check results

- Verify all files synced (no errors)
- If images fail with 404: the image files need to be committed and pushed to git
  - `site/` images deploy to Netlify (`stoic-2026.netlify.app`)
  - Other images use GitHub raw URLs (`raw.githubusercontent.com/ruycervantes/CI-2026-new-vision/master/`)
  - Both require `git push` to work

### Step 4: Handle image issues

If images are missing from Notion:

1. Check if the image files are tracked:
   ```bash
   git status site/diagrams/ paper-images/ archive/diagrams/
   ```
2. If untracked, add and push:
   ```bash
   git add [image files]
   git commit -m "Add image assets for Notion sync"
   git push
   ```
3. Re-run the sync

### Step 5: Report

Show:
- Number of files synced
- Any errors or bad blocks
- Whether images are expected to render (files pushed to git?)

## Synced files

| File | Notion title |
|------|-------------|
| `team-effectiveness/research/synthesis-v2.md` | TE — Synthesis v2 |
| `team-effectiveness/research/methodology.md` | TE — Methodology |
| `core/alignment.md` | Leadership Alignment |
| `core/vision.md` | Platform Vision |
| `core/roadmap.md` | Engineering Roadmap |
| `core/MVP-offer-hpt.md` | Team Performance MVP |

## Adding new docs

1. Add entry to `scripts/notion-sync-config.yaml`
2. Run `/sync-notion`
3. Update the table above and in `CLAUDE.md`

## Technical details

- **Script:** `scripts/notion-sync.py`
- **Config:** `scripts/notion-sync-config.yaml`
- **API key:** `NOTION_API_KEY` in `.env` (never commit)
- **Parent page must be shared** with the Notion integration
- **Notion API limit:** 100 blocks per append — script chunks automatically
- **Cross-doc links:** Relative `.md` links between synced pages resolve to Notion URLs. Others render as plain text.
- **Inline formatting:** Bold, italic, inline code, and external links are preserved
- **Block types:** Headings, bullets, numbered lists, quotes, tables, code blocks, dividers, images

## Parameters

- `/sync-notion` — sync all 6 files
- `/sync-notion core/vision.md` — sync one file
- `/sync-notion --dry-run` — preview without API calls
