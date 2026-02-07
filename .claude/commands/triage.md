---
name: triage
description: Triage action items — clean up, reorganize, and prepare for next period. Works end-of-month (creates new file) or mid-month (cleans in place). Checks Todoist for duplicates before proposing changes.
---

# Triage Action Items

Clean up, reorganize, and prioritize an action items file. Adapts to timing: end-of-month creates a new month file, mid-month cleans the current file in place.

## Arguments
- `$ARGUMENTS` — Optional: path to action items file, or "monthly" to force end-of-month mode

## Step 1: Determine Mode

Check today's date:
- **If last 3 days of month OR first 2 days of next month OR user said "monthly":** Monthly triage mode — will create a new month file and archive the old one.
- **Otherwise:** Mid-month cleanup mode — edits the current file in place.

Report the mode to the user.

## Step 2: Load Sources

1. **Read the action items file.** If no path given, look for `action-items-ruy-{current-month}{year}.md` in the repo root. If not found, ask.
2. **Read OKRs:** `okrs-q1-2026.md` — this is the north star for prioritization.
3. **Read Oseas 1-on-1 log:** `team/oseas-1on1-log.md` — for pending items and recent decisions.
4. **Check Todoist @this-week and @next-week** — fetch current tasks to identify duplicates and already-tracked items.

Report: "Found X sections with Y total tasks in file. Z items in Todoist @this-week, W in @next-week."

## Step 3: Cross-Reference

Compare the action items file against Todoist. For each item in the file, check if it already exists in Todoist. Build three lists:

1. **In both** — duplicates. Note if labels/priority differ.
2. **In file only** — not yet in Todoist. These need to be triaged.
3. **In Todoist only** — not in the file. May be orphaned or independently created.

Present the cross-reference summary to the user.

## Step 4: Section-by-Section Triage

Walk through the action items file section by section. For each section:

1. List all items with a brief status read (done? stale? still relevant? blocked?)
2. For each item, propose one of:
   - **Keep** — carry forward, still relevant
   - **Complete** — done. Move to "Completed This Week" section with date.
   - **Kill** — obsolete or overtaken by events (not done — just no longer relevant)
   - **Move to Todoist personal** — personal items that don't belong in this file
   - **Reframe** — the item needs rewording (absorbed into something else, scope changed)
   - **Move to backlog/someday** — important but not this month

3. Use AskUserQuestion for decisions that need user input. Batch related items where possible (e.g., "these 3 quick wins — any done?").

### For reference sections:
- Ask: archive all, keep key reflections, or keep specific quotes?
- Default recommendation: keep key reflections and strategic context that guides decisions. Archive meeting-specific details.

### For blocked items:
- Check each blocker: resolved? changed? new owner?
- Update the table.

## Step 5: Check for Missing Items

Ask the user:
> "Any recent calls, meetings, or decisions that generated action items not yet captured? Tell me and I'll add them."

If yes, capture them interactively.

## Step 6: Build the Output

### Monthly mode:
Create `action-items-ruy-{month}{year}.md` with this structure:

```markdown
# Action Items - Ruy ({Month} {Year})

Triaged from {previous month} file + [sources].
**Created:** {date}

---

## This Week Focus ({date range})

### {OKR-aligned cluster 1} (e.g., "AI Coach — OKR #1")
- [ ] items...

### {OKR-aligned cluster 2}
- [ ] items...

### Quick wins
- [ ] items...

### Process
- [ ] items...

### Calls to process
- [ ] items...

---

## {Month} Priorities

### {Cluster by area}
- [ ] items...

---

## Completed This Week

Items completed during the week. Reviewed during weekly triage, then archived.
Supports the "Two Lenses" model: what you delivered + what you made easier.

| Date | Item | Impact (what it enabled) |
|------|------|--------------------------|

---

## Blocked Items

| Item | Blocked By | Next Step |
|------|------------|-----------|

---

## Someday / Backlog
- [ ] items...

---

## Key Reflections & Context *(reference, not tasks)*
(carried from previous month, trimmed)
```

### Mid-month mode:
Edit the current file in place — move completed items to Completed section, remove killed items, reframe changed items, reorganize sections.

## Step 7: Update Related Docs

Check if triage decisions affect:
- `okrs-q1-2026.md` — scope changes, new owner assignments
- `core/alignment.md` — role changes, new decisions
- `team/oseas-1on1-log.md` — pending items resolved or added
- `team/status.md` — blocker changes

Propose updates. Ask before editing.

## Step 8: Todoist Sync Prep

Generate a summary of items that need Todoist action:

```
## Todoist Sync Needed

### New items to create:
- "Task name" → project: X, label: @this-week, priority: P2

### Items to complete:
- "Task name" (id: xxx) — done or obsolete

### Items to update:
- "Task name" (id: xxx) — move from @this-week to @next-week

### Personal items to move:
- "Task name" → Todoist personal project
```

Do NOT push to Todoist. Present the list and let the user decide when to sync.

## Step 9: Summary

Report:
- Files modified
- Tasks kept / completed (moved to Completed section) / killed / reframed / moved
- New items added
- Cross-references updated
- Todoist sync items pending

## Principles

- **Conservative by default** — always ask before making changes
- **OKR-aligned** — group tasks by which OKR they serve
- **Preserve the user's voice** — don't rewrite task descriptions unless asked
- **Single source of truth** — each item lives in one place. Flag duplicates.
- **Done = captured** — completed items move to "Completed This Week" section with date + impact. Progress needs to be visible, not erased. Archived during weekly triage.
- **Personal items → Todoist** — this file is for Stoic work + key personal commitments only
- **Reference ≠ tasks** — mark reference sections clearly, keep them trimmed
