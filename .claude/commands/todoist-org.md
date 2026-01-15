---
name: todoist-org
description: Ruy's Todoist organization system with label-based weekly planning. Use when creating tasks, planning weeks, reviewing priorities, or any Todoist operations. Triggers on mentions of Todoist, task planning, weekly reviews, or "what should I work on".
---

# Todoist Organization System

## Label System (Stable)

### Time-Based Labels (for weekly planning)
- `@this-week` - Current week focus (max 15-20 tasks)
- `@next-week` - Coming up soon
- `@this-month` - Within current month
- `@someday` - Important but not time-bound

### Energy/Context Labels
- `@quick-win` - Under 15 minutes
- `@deep-work` - Needs 1+ hours focused time
- `@energy-low` - Can do when tired
- `@waiting` - Blocked by others
- `@followup` - Needs follow-up action

### Status Labels
- `@to-review` - New tasks needing review
- `@Doing` - Currently in progress
- `@urgent` - True emergencies only
- `@recurrent` - Recurring items

## Core Principles

1. **Dates are for appointments, not aspirations** - Only set due dates for real deadlines
2. **Labels are for possibilities, not obligations** - Pull based on energy, don't push based on guilt
3. **3 important + 3 quick = full day** - Don't overload
4. **Planning prevents paralysis** - Weekly and daily planning rituals matter
5. **@this-week is curated** - Max 15-20 tasks, not a dumping ground

## Task Creation Pattern

When creating tasks:
1. Apply time label (@this-week, @next-week, @this-month, or @someday)
2. Apply energy label (@quick-win, @deep-work, or @energy-low) when clear
3. Set priority (P1-P4) based on importance
4. Add @waiting if blocked, @followup if needs follow-up
5. **Avoid due dates** unless it's a real deadline (meeting, external commitment)

Example good task:
```
"Review P&G proposal" @this-week @deep-work P1
```

Example bad task:
```
"Review P&G proposal" due:tomorrow  ← Don't use dates as motivation
```

## Planning Workflows

### Weekly Planning (Monday)
- Review @this-week → move incomplete to @next-week if needed
- Promote from @next-week → @this-week
- Check @waiting for follow-ups needed
- Identify top 3 outcomes for the week

### Daily Selection
- From @this-week: Pick MAX 3 important tasks
- From @quick-win: Pick 2-3 small tasks
- Match energy level to @deep-work or @energy-low
- That's it. Don't add more.

## When Using Todoist MCP

- Search tasks with `@this-week` label for current priorities
- When creating: always include at least one time label
- Prefer labels over due dates for planning
- Project structure uses emoji prefixes for visual scanning
