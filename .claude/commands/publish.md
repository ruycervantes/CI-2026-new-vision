---
name: publish
description: Publish shareable docs to the stoicenteprises/knowledgebase2026 GitHub repo. Use after editing core docs, research, or chatbot designs.
---

# /publish - Publish knowledge base to GitHub

Syncs shareable folders from this repo to the `stoicenteprises/knowledgebase2026` GitHub repo using `scripts/publish.sh`.

## Instructions

### Step 1: Run the publish script

If user provides a commit message:
```bash
./scripts/publish.sh "$ARGUMENTS"
```

If no argument:
```bash
./scripts/publish.sh
```

### Step 2: Check results

- Verify the script completed without errors
- Report number of files changed
- Confirm push to GitHub succeeded

### Step 3: Report

Show:
- Commit message used
- Files changed (from git output)
- Link: https://github.com/stoicenteprises/knowledgebase2026

## What gets published

| Folder | Contents |
|--------|----------|
| `core/` | Vision, roadmap, alignment, MVP offer, pitch |
| `team-effectiveness/` | HPT research, methodology, synthesis |
| `research/` | Coaching methodology, AI Coach design, interviews |
| `enterprise/` | Integration strategy |
| `site/` | Netlify site and diagrams |
| `chatbot-design/` | Chatbot design process and examples |
| `netlify.toml` | Netlify config |
| `README-public.md` | Becomes `README.md` in the published repo |

## What stays private

`calls/`, `sprints/`, `team/`, `thinking/`, `handwritten/`, action items, OKRs, sprint files, `.claude/`, archive.

## Adding a new folder to publish

1. Add the folder name to the `FOLDERS` array in `scripts/publish.sh`
2. Update the "What gets published" table above
3. Update `README-public.md` with a section for the new folder
4. Run `/publish` to sync

## Parameters

- `/publish` — publish with default message ("Publish updates from command center")
- `/publish Update vision and roadmap` — publish with custom commit message
