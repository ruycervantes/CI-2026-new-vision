#!/bin/bash
# Publishes shareable folders to the stoic-knowledge-base repo.
# Usage: ./scripts/publish.sh [commit message]
#
# Copies: core/, team-effectiveness/, research/, enterprise/, site/, chatbot-design/, netlify.toml
# Target: ../stoic-knowledge-base (sibling directory)
#
# To pull Nelson's contributions back:
#   cd ../stoic-knowledge-base && git pull
#   rsync -av --delete ../stoic-knowledge-base/core/ ./core/
#   (repeat for other folders as needed)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SOURCE_DIR="$(dirname "$SCRIPT_DIR")"
TARGET_DIR="$(dirname "$SOURCE_DIR")/stoic-knowledge-base"

FOLDERS=(core team-effectiveness research enterprise site chatbot-design)
FILES=(netlify.toml README-public.md)

# --- Init target repo if needed ---
if [ ! -d "$TARGET_DIR" ]; then
  echo "Creating $TARGET_DIR..."
  mkdir -p "$TARGET_DIR"
  git -C "$TARGET_DIR" init
  echo ">> Created new repo at $TARGET_DIR"
  echo ">> You'll need to add a remote: cd $TARGET_DIR && git remote add origin <url>"
fi

# --- Sync folders ---
for folder in "${FOLDERS[@]}"; do
  if [ -d "$SOURCE_DIR/$folder" ]; then
    rsync -av --delete \
      --exclude='__pycache__' \
      --exclude='.DS_Store' \
      "$SOURCE_DIR/$folder/" "$TARGET_DIR/$folder/"
  fi
done

# --- Sync individual files ---
for file in "${FILES[@]}"; do
  src="$SOURCE_DIR/$file"
  # README-public.md becomes README.md in target
  if [ "$file" = "README-public.md" ]; then
    [ -f "$src" ] && cp "$src" "$TARGET_DIR/README.md"
  else
    [ -f "$src" ] && cp "$src" "$TARGET_DIR/$file"
  fi
done

# --- Commit and push ---
cd "$TARGET_DIR"
git add -A

if git diff --cached --quiet; then
  echo "No changes to publish."
  exit 0
fi

MSG="${1:-Publish updates from command center}"
git commit -m "$MSG"

if git remote get-url origin &>/dev/null; then
  git push
  echo ">> Published and pushed."
else
  echo ">> Committed locally. Add a remote to push:"
  echo "   cd $TARGET_DIR && git remote add origin <url> && git push -u origin main"
fi
