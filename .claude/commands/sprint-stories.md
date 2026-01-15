# Sprint Stories (Team Sprint Planning)

Skill for creating sprint stories for the dev team (Mike, Shamil, Daniel, Leo).

**This is team sprint planning, NOT Ruy's personal work.** For Ruy's own deliverables, use `/planning-review`.

## When to Use

- Before Thursday sprint planning meeting
- When breaking down roadmap items into sprint work
- When preparing stories for the team

---

## Input Sources

Work can come from:
- **Roadmap** - Q1 features from `roadmap-q1-2026-draft.md`
- **Bug list** - From Mike
- **Tech debt** - Infrastructure, refactoring needs
- **Urgent requests** - Client issues, blockers
- **Call with Mike** - Prep call can be input (use `/process-call` if recorded)

---

## Prep Options

Two ways to prepare stories:

**Option A: Draft then discuss**
1. Ruy drafts stories from roadmap/backlog
2. Review with Mike
3. Adjust based on his input
4. Bring to sprint planning

**Option B: Call with Mike first**
1. Call with Mike to identify priorities
2. Draft stories together or after
3. Bring to sprint planning

Either works - depends on context.

---

## Estimation

Points can be added:
- **Before planning** - If Ruy and Mike agree on estimate during prep
- **During planning** - Team estimates together (more common)

Use `**Points:** TBD` in draft if estimating during planning.

---

## File Location

**Folder:** `sprints/`

**Naming:** `sprint-stories-{month}{year}.md`

**Example:** `sprints/sprint-stories-jan2026.md`

(Ruy's personal sprint files stay in root: `sprint-2-2026-foundation.md`)

---

## Team Members & Roles

| Person | Role | Typical Work |
|--------|------|--------------|
| **Mike** | Dev lead | Teams integration, architecture, deploys |
| **Shamil** | Dev | Coach features, Thinking Partner |
| **Daniel** | Dev | Infrastructure, deployment scripts |
| **Leo** | Testing/PMF | Testing → demo approval, validation |

---

## Sprint Cadence

| Day | Activity |
|-----|----------|
| **Wednesday** | Demo (show completed work) |
| **Wednesday** | Retro (review estimates vs actuals) |
| **Wednesday** | Refinement (break down upcoming work) |
| **Thursday** | Sprint Planning (commit to sprint scope) |

---

## Story Points (IBM Scale)

| Points | Meaning |
|--------|---------|
| 1 | Trivial - few hours |
| 2 | Small - half day |
| 3 | Medium - 1 day |
| 5 | Large - 2-3 days |
| 8 | Very large - almost full sprint |
| 13 | Too big - needs breakdown |

**Rule:** If estimate > 5 points, break it down into smaller stories.

---

## Environments

```
Development → Testing → Demo → Production
              (testing.stoicq.com)  (demo.stoicq.com)
```

- **Development** - Active dev work
- **Testing** - QA environment (Leo tests here)
- **Demo** - Client demos (almost production quality)
- **Production** - Live clients

---

## Story Template

```markdown
### {Person}: {Feature/Task Name}

{Brief description - what and why}

**Points:** {1/2/3/5/8}

**Requirements:**
- {Requirement 1}
- {Requirement 2}

**Acceptance Criteria:**
- [ ] {Testable criterion}
- [ ] {Testable criterion}
- [ ] {Testable criterion}

**Dependencies:** {What blocks this / what this blocks}

**Notes:** {Any context, links to specs, etc.}
```

---

## Sprint Stories File Template

**Location:** `sprints/sprint-stories-{month}{year}.md`

```markdown
# Sprint Stories - {Month} {Year}

Sprint Planning: {Day}, {Date}

---

## Dev Team

### Shamil: {Story Title}
{Description}

**Points:** {N}

**Acceptance Criteria:**
- [ ] {Criterion}

---

### Daniel: {Story Title}
{Description}

**Points:** {N}

**Acceptance Criteria:**
- [ ] {Criterion}

---

### Leo: {Story Title}
{Description}

**Points:** {N}

**Acceptance Criteria:**
- [ ] {Criterion}

---

## Mike

### Mike: {Story Title}
{Description}

**Points:** {N}

**Acceptance Criteria:**
- [ ] {Criterion}

**Blocks:** {What this unblocks}

---
```

---

## Process

### Before Sprint Planning (Wednesday Refinement)

1. **Identify work** - What needs to happen this sprint? (from roadmap, bugs, tech debt)
2. **Break down** - Stories should be ≤5 points each
3. **Write acceptance criteria** - Testable, specific
4. **Note dependencies** - What blocks what?
5. **Assign owners** - Who does each story?

### During Sprint Planning (Thursday)

1. Review stories together
2. Team estimates (use planning poker or quick consensus)
3. Check capacity (~6-7 days per person per sprint)
4. Commit to sprint scope
5. Note what's NOT in sprint (backlog)

### During Sprint

- Stories tracked in Asana (moving to Linear)
- Daily standups via Teams
- Mike can assign urgent items outside sprint if needed

### End of Sprint (Wednesday Demo)

1. Demo completed work
2. Record actuals vs estimates
3. Incomplete work → next sprint or backlog
4. Retro: what went well, what didn't

---

## Writing Good Acceptance Criteria

**Bad:**
- [ ] Works correctly
- [ ] User can use feature

**Good:**
- [ ] User sees goal extracted from conversation in UI
- [ ] Data persists after page refresh
- [ ] Script creates environment accessible at {client}.stoicq.com within 5 minutes

**Pattern:** `{Actor} {action} {observable result}`

---

## Dependencies Format

When a story blocks or is blocked:

```markdown
**Blocks:** Leo's Testing → Demo Approval Process
```

```markdown
**Dependency:** Mike deploys Leadership Growth Partner from dev to staging first.
```

---

## Start

To create sprint stories:
1. Ask what work needs to happen this sprint
2. Break down by team member
3. Write stories using template above
4. Add to sprint stories file

Or provide a roadmap item / feature and I'll help break it into stories.
