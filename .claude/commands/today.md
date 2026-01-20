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

## When User Says
- "show me today"
- "what's on for today"
- "daily review"
- "/today"
