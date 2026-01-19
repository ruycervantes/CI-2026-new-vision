---
name: weekly-plan
description: Weekly planning triage - consolidate action-items + Todoist, triage to 15-20 tasks, identify top 3 outcomes. Use on Mondays or when starting a new week.
---

# Weekly Plan Skill

Consolidate all task sources, triage to a realistic week, sync to Todoist, and define top 3 outcomes.

**Part of Ruy's personal productivity system** (along with `/review-action-items`).

**Different from `/planning-review`:** Weekly-plan is personal task triage. Planning-review is for sprint planning with the dev team (deliverables, right-sizing, sprint files).

## When to Use

- Monday mornings (start of week)
- Sunday evening (prep for week)
- When `@this-week` feels overwhelming
- When action-items file and Todoist are out of sync
- User says "plan my week", "triage this week", "what's my week look like"

---

## The Process

### 1. Gather Sources (automatic)

Read and pull from all task sources:

```
ACTION-ITEMS FILE
├── Read: action-items-ruy-jan2026.md
├── Extract: "This Week Focus" section
└── Extract: Any items marked for this week

TODOIST
├── Query: labels:this-week
├── Query: due dates within 7 days (catch mislabeled)
├── Query: labels:next-week (promotion candidates)
└── Use todoist-org skill for label conventions
```

### 2. Consolidate (automatic)

Create unified view:

```markdown
| Task | Source | Priority | Labels | Notes |
|------|--------|----------|--------|-------|
| ... | action-items | - | - | Not in Todoist |
| ... | Todoist | P1 | this-week | |
| ... | both | P2 | next-week | Mislabeled - due today |
```

Flag issues:
- Tasks in action-items but not Todoist
- Tasks with wrong labels (e.g., @next-week but due this week)
- Duplicate tasks across sources

### 3. Triage (interactive)

Go through each category and ask questions:

**Categories (in order):**
1. Urgent/deadlines - real deadlines this week?
2. High priority - truly needed this week?
3. Medium priority - realistic given capacity?
4. Research/documents - what's achievable?
5. Admin/personal - what can wait?

**Questions to ask:**
- "When is the real deadline for X?"
- "Is X truly needed this week or nice-to-have?"
- "Does X have a hard deadline or is it self-imposed?"

**Decisions:**
- ✅ Keep in `@this-week`
- → Move to `@next-week`
- → Move to `@someday`
- → Move to `@this-month`
- ✅ Done - remove from list

**Target: 15-20 tasks max in `@this-week`**

Show running count as triage progresses.

### 4. Top 3 Outcomes (interactive)

After triage, ask:

> "What are your top 3 outcomes for this week? (Not tasks - results you want to achieve)"

Options:
- User types them directly
- Help pick from the triaged tasks (suggest outcome-level framing)
- Skip for now

**Outcome framing:** Transform tasks into results
- Tasks: "Dolo interview prep + Leo PMF discussion"
- Outcome: "PMF direction clarified"

### 5. Sync (after confirmation)

**Update Todoist:**
- Update labels on existing tasks
- Add new tasks from action-items
- Respect system rules (from todoist-org skill):
  - No due dates except real deadlines
  - Apply energy labels where clear (@deep-work, @quick-win)
  - Always include time label

**Add Week Outcomes:**
- Create uncompletable header task: "🎯 Week Outcomes (dates)"
- Include 3 outcomes in description
- Label: @this-week, P1

**Update action-items file:**
- Add "Week Outcomes" section under "This Week Focus"

### 6. Output Summary

End with clear summary:

```markdown
## Weekly Planning Complete

**3 Outcomes:**
1. {Outcome 1}
2. {Outcome 2}
3. {Outcome 3}

**@this-week: {N} tasks** (target: 15-20)

**Moved out:**
- {Task} → @next-week
- {Task} → @someday

**Added:**
- {N} new tasks synced from action-items
```

---

## Key Principles

From `todoist-org` skill:

1. **Dates are for appointments, not aspirations** - Only set due dates for real deadlines
2. **Labels are for possibilities, not obligations** - Pull based on energy, don't push based on guilt
3. **3 important + 3 quick = full day** - Don't overload
4. **@this-week is curated** - Max 15-20 tasks, not a dumping ground

From this skill:

5. **Outcomes over tasks** - Define what success looks like, not just what to do
6. **Consolidate before triage** - See everything in one place first
7. **Interactive triage** - Ask questions, don't assume urgency
8. **Sync both directions** - Todoist ↔ action-items file stay aligned

---

## Integration with Other Skills

### Personal Productivity System
- **`/review-action-items`** - Process new items into action-items file (after meetings/notes)
- **`/weekly-plan`** - Weekly triage (Monday mornings)
- **`/todoist-org`** - Reference for label system and conventions

### Work (Sprints)
- **`/planning-review`** - Sprint planning with dev team (bi-weekly)
- **`/sprint-stories`** - Create stories for team members

**Typical flow:**
```
PERSONAL (ongoing)
/review-action-items (after meetings/notes)
    ↓
/weekly-plan (Monday)
    ↓
Daily selection from @this-week (each morning)

WORK (bi-weekly)
/planning-review (start of sprint)
    ↓
/sprint-stories (before sprint planning meeting)
```

---

## Start

Begin by reading the action-items file and querying Todoist, then show the consolidated view.
