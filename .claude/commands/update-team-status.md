# /update-team-status - Update team status from conversation or docs

Extract team status updates from the current conversation or a document and update `team/status.md`.

## File Structure

The file has two main parts:
1. **Sprint Status (top)** — Current work, changes frequently
2. **Team Profiles (bottom)** — Reference info, changes rarely

```
# Team Status & Development
> Current Sprint: Sprint X
> Last updated: Date

## [Person] (one per team member)
  - Location
  - Sprint X Status (table)
  - Next Milestone

## Notes (sprint-level notes)
## Blockers (table)
## Key Decisions (by date)

## Team Profiles (Reference)
  - Roles, skills, development goals (static)
```

## Instructions

### Step 1: Read Current State

Read `team/status.md` to understand:
- Current sprint number and dates
- Each person's current status and milestones
- Existing blockers and decisions

### Step 2: Extract Updates from Context

Look at the conversation or document for:
- **Status changes** — done, in progress, blocked, assigned
- **New assignments** — who's taking on what
- **Completed items** — what's now done
- **New blockers** — what's waiting on what
- **Key decisions** — significant choices made
- **Milestone updates** — new dates or deliverables

### Step 3: Identify Cleanup Opportunities

While extracting, also note:
- **Stale items** — dates that have passed, items marked "tomorrow" or "next week"
- **Completed work** — items that should be marked done or removed
- **Redundant info** — same thing stated multiple ways
- **Resolved blockers** — blockers that are no longer blocking

### Step 4: Propose Changes (Ask First)

**Before writing anything**, present:

```
## Proposed Updates

**[Person]:**
- Add: [new status item]
- Update: [existing item] → [new status]
- Remove: [stale item] (reason)

**Blockers:**
- Add: [new blocker]
- Remove: [resolved blocker]

**Key Decisions ([date]):**
- Add: [decision]

**Cleanup:**
- [Person]: Remove "[stale item]" — date passed
- Notes: Remove "[outdated note]"
```

Use AskUserQuestion to confirm. Options: "Apply all", "Apply with changes", "Skip".

### Step 5: Apply Updates

When updating:

**For Sprint Status tables:**
- Add new items at the end of the table
- Update status text for existing items (don't duplicate rows)
- Remove items only if explicitly completed or stale

**For Next Milestone:**
- Replace with new milestone if more current
- Keep existing if still valid

**For Blockers table:**
- Add new blockers
- Remove resolved blockers (don't just mark "resolved")

**For Key Decisions:**
- Add new date section if decisions from a new meeting
- Don't duplicate existing decisions

**For Team Profiles:**
- Only update if role/skills fundamentally changed
- This section is reference, not sprint tracking

### Step 6: Show Summary

After updating:
```
Updated team/status.md:

Added:
- [Person]: [item]

Updated:
- [Person]: [item] status

Removed:
- [Person]: [stale item]

Last updated: [date]
```

## Cleanup Rules

| Situation | Action |
|-----------|--------|
| Item marked "tomorrow" and date passed | Remove or update date |
| Item marked "done" | Keep in current sprint, remove next sprint |
| Blocker resolved | Remove from table |
| Decision older than 2 sprints | Move to archive or remove |
| Duplicate status rows | Keep most recent, remove duplicate |
| Notes about past events | Update tense or remove if no longer relevant |

## Parameters

- `/update-team-status` — Extract from current conversation
- `/update-team-status <file>` — Extract from a specific file

## Tips

- Focus on the **2 most important changes per person** when proposing
- Don't propose changes to Team Profiles unless something fundamental changed
- When in doubt about removal, ask the user
- Prefer updating existing items over adding new rows for the same work
