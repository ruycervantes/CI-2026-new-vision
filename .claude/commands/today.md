---
name: today
description: Daily work review - fetch today's Todoist tasks, organize by priority, recommend focus. Use at start of day or when planning.
---

# /today - Daily Work Review

Reference the `todoist-org` skill for label meanings and principles.

## Workflow

### 1. Fetch Today's Tasks
Use Todoist MCP `find-tasks-by-date` with `startDate: today`

### 2. Present by Priority

```
## Today ([date]) - [count] tasks

**P1 - Must Do:**
- [ ] Task (`@deep-work`)
- [ ] Task

**P2:**
- [ ] Task (`@quick-win`)

**P3:**
- [ ] Task

**P4 (recurring/admin):**
- [ ] Task
```

Show relevant labels inline: `@deep-work`, `@quick-win`, `@waiting`, `@Doing`

### 3. Focus Recommendation

Apply the **3 important + 3 quick = full day** principle:

- Count P1s - if more than 3-4, suggest moving some to tomorrow
- Identify `@deep-work` items - suggest picking ONE for morning focus
- Note `@quick-win` items for gaps between meetings
- Flag conflicts (multiple deep-work competing for same day)

Example:
```
**Focus:** 3 P1s is manageable. Start with [deep-work item] in the morning.
[Quick-win item] can fill gaps between meetings.
```

### 4. Check for Issues (optional)
- Duplicate tasks
- Overloaded day (too many P1s)
- P1 items missing from action-items file

### 5. Triage Mode (Interactive)

After presenting the day, ask:
> "Any updates? (voice dump: what's done, what to move, what to add)"

**Parse user input for these patterns:**

| Pattern | Action |
|---------|--------|
| "X is done" / "X done" / "already did X" | Complete task X |
| "move X to tomorrow" / "X for tomorrow" | Update due date to tomorrow |
| "move X to [day]" | Update due date to specified day |
| "add [task]" / "I need to [task]" | Add new task for today |
| "add [task] for tomorrow" | Add new task for tomorrow |
| "[task] is P1/urgent" | Update priority |
| "[task] is deep work" | Add @deep-work label |

**Execution flow:**
1. Parse all updates from user input
2. Show parsed actions for confirmation:
   ```
   Understood:
   - Complete: "Meditar"
   - Move to tomorrow: "Review Dolo interview"
   - Add for today: "Talk to Daniel" (P1)
   Proceed? (y/n)
   ```
3. Execute in Todoist (complete-tasks, update-tasks, add-tasks)
4. If any P1/P2 work tasks changed → offer to sync action-items file
5. Show cleaned-up day summary

**Sync to action-items:**
- Only sync work-related tasks (Product Strategy, Testing, Management projects)
- Update "Today" section in action-items-ruy-jan2026.md
- Mark completed items with [x]

## When User Says
- "show me today"
- "what's on for today"
- "daily review"
- "/today"
