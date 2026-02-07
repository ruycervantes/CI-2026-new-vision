# Sprint Methodology Fix: Stoic Engineering

**Goal:** Create visibility into velocity, enable data-driven conversations, and make priorities explicit.

**Timeline:** 
- **This sprint (Sprint 1):** Fix methodology using Asana, prepare Linear migration
- **Next sprint (Sprint 2):** Move engineering to Linear
- **Sprints 3-5:** Iterate and collect velocity data

---

## The Problems

### Ruy is the glue

The system doesn't show the picture — Ruy holds it in his head and reconstructs it for others. Sprint planning takes 2-3 hours per week because there's no pre-organized backlog of estimated, ready work. Leonardo and Oseas can't self-serve "what's the status of X" or "what shipped last month" without asking Ruy.

### No estimation discipline

Estimates happen through quick conversations ("how long do you think?") rather than structured team discussion. There's no record of what was estimated vs. what actually happened, so there's no way to:
- Predict capacity accurately
- Identify who consistently over/underestimates
- Have data-driven conversations about delivery

When things don't ship, it's usually because estimates were too optimistic or scope wasn't clear — but there's no data to prove which.

### Priorities aren't documented

The priorities are clear in Ruy's head but not written down in a way others can reference. The Notion page has a rough ordered list, but it's not explicit enough to guide sprint decisions or align stakeholders on what matters most.

### Asana structure fights the workflow

Two separate projects (Development and Testing) fragment the sprint view — you can't see all work competing for the same capacity. The flat task structure doesn't support epic → story → task hierarchy, making it hard to:
- See how tasks roll up to larger initiatives
- Track progress on multi-sprint efforts
- Transform roadmap items into sprint work

Sprint labels are inconsistent (Sprint 19, Sprint 6, Sprint 1-2026). The Done column has 95 items accumulating as a graveyard. The "Design/Spec in-progress" column conflates two different phases.

Even at Asana's Advanced tier ($25/user/month), there's no native sprint backlog, velocity metrics, or burndown charts. You pay more for portfolio views while still building sprint workarounds manually.

### Notion became a dumping ground

Specs from Q1 2025 sit next to Aug 2025 features with no clear distinction between "current," "planned," and "archived." FRDs, backlogs, program plans, and strategy docs are all in one flat list. There's no lifecycle status showing which specs are Draft → Approved → Building → Shipped.

### Shamil's delivery is unpredictable

Some sprints he estimates well and delivers; others drag across multiple sprints. Without estimate/actual data, there's no mechanism to:
- Catch optimistic estimates before the sprint starts
- Hold him accountable to commitments
- Have a concrete conversation about the pattern

The feeling exists but the facts don't.

### Refinement doesn't produce ready work

Sprint planning becomes prioritization + estimation + decomposition all at once — that's why it's slow and still doesn't work. Specs go from "big idea" to "let's start" without the middle layer of sprint-sized, estimated tasks.

---

## Part 1: This Sprint — Methodology First (Still in Asana)

The tool is changing next sprint, but the methodology starts now. Use this sprint to:

1. Establish the discipline of estimates and actuals
2. Write down the priorities
3. Prepare the Linear workspace

### Minimal Asana Adjustments

Don't overinvest in Asana setup — we're migrating in 2 weeks. Just add enough structure to practice the new methodology:

**Add two custom fields to your current project:**

| Field | Type | Purpose |
|-------|------|---------|
| **Estimate** | Number (days) | Capture expected effort at planning |
| **Actual** | Number (days) | Fill in when task completes |

That's it. Don't restructure the board, don't create new views, don't merge projects. We're leaving soon.

**Use these fields this sprint:**
- Thursday planning: Every task gets an estimate
- Wednesday demo: Every completed task gets an actual
- Wednesday retro: Review the gaps

This gives you one sprint of estimate/actual data before Linear, and the discipline carries over.

### Team Process Decisions (Jan 15, 2026 Sprint Planning)

| Decision | Details |
|----------|---------|
| **Story Points** | Adopted IBM sizing table (1,2,3,5,8,13) |
| **Environment Naming** | development → testing → demo → production |
| **Tool Migration** | Evaluate Linear/GitHub this sprint, decide in office hours |
| **Demo Notice** | 3+ days before client demos |
| **Daily Standups** | Via Teams messages, using Asana form |

### Testing & Shipping Process (Jan 15, 2026)

*Source: `calls/Sprint Planning 15 jan 2026 - Summary.md` Section 8*

**Environments:**
```
Development → Testing → Demo → Production
              (testing.stoicq.com)  (demo.stoicq.com)
```

- testing.stoicq.com = QA environment (was "staging")
- demo.stoicq.com = client demos (almost production quality)

**Flow:**
1. Mike marks "Review" → deployed to testing.stoicq.com
2. Leo tests in testing environment
3. Leo approves → promoted to Demo
4. Demo used for client demonstrations

**Rules:**
- 3+ days notice before client demos (for QA tour)
- Leo owns testing → demo approval

**Technical debt:**
- GitHub branch still called "staging" → Mike to rename to "testing"
- Use Claude Code to compare files between branches

**Client lifecycle (undefined):**
- No visibility into which instances are active
- Need process to archive/deactivate unused instances
- Critical: Nelson leaving, Octavio joining - document before handoff

**Open questions:**
- Who notifies Data, Nelson, Axialent when features ship?
- Can deployment script enforce 3-day demo notice? (e.g., require Leo PR approval)

---

## Part 2: The Priorities Page (Do This Week)

This is tool-agnostic and essential. Create in Notion: **"Q1 2026 Engineering Priorities"**

### Template:

```markdown
# Q1 2026 Engineering Priorities

Last updated: [date]

## The Stack Rank

These are our priorities in order. When in doubt, higher beats lower.

### 1. [Priority Name]
**What:** One sentence description
**Why:** Business reason (revenue, client, risk)
**Key deliverables:** 
- Deliverable 1
- Deliverable 2

### 2. [Priority Name]
**What:** ...
**Why:** ...
**Key deliverables:** ...

### 3. [Priority Name]
...

---

## What We're NOT Doing This Quarter

- Thing we're saying no to (and why)
- Thing that can wait

---

## Open Questions

- Decision we need to make
- Dependency we're waiting on
```

### Example for your current situation:

```markdown
### 1. P&G Go-Live Readiness
**What:** Everything needed for P&G production deployment
**Why:** Flagship enterprise client, proof of enterprise viability
**Key deliverables:**
- SSO integration complete
- GDPR compliance verified
- Admin panel for their team

### 2. Thinking Partner v2 Stability
**What:** Port to v2 architecture, fix conversation loop issues
**Why:** Core product quality, affects all clients
**Key deliverables:**
- Migration complete
- QA framework catching regressions

### 3. MS Teams Integration (MVP)
**What:** Basic chatbot presence in Teams
**Why:** Enterprise clients expect it, TELUS specifically asking
**Key deliverables:**
- Bot responds in Teams
- Notifications working
```

---

## Part 3: Prepare Linear Migration (This Sprint)

### Week 1: Setup and Structure

**Create the Linear workspace:**
1. Sign up at linear.app (free tier is fine for setup)
2. Create workspace: "Stoic Engineering" or "ConsciousInsights"
3. Invite Mike and Shamil as members

**Set up the team structure:**

In Linear, the hierarchy is: **Workspace → Teams → Projects → Issues → Sub-issues**

Create one team to start:
- **Team:** ConsciousInsights (or "CI Engineering")

**Create Projects for your current epics/initiatives:**
- MS Teams Integration
- Thinking Partner v2
- Admin Panel
- GDPR Compliance
- Voice Input
- Infrastructure / DevOps

Projects in Linear = Epics. They group related issues and show progress.

**Configure Cycles:**
- Go to Team Settings → Cycles
- Enable Cycles
- Set duration: 2 weeks
- Set start day: Thursday (matches your current cadence)
- Create 2-3 upcoming cycles

**Set up labels:**
- `bug` — Bug fixes
- `feature` — New functionality
- `tech-debt` — Refactoring, cleanup
- `spike` — Research, investigation

**Configure estimate scale:**
- Go to Team Settings → Issue features → Estimates
- Choose: Linear scale (1, 2, 3, 5, 8) or Hours/Days
- Recommendation: Use days if you're not used to story points

### Week 2: Migration and Dry Run

**Export from Asana:**
- Linear has an Asana importer: Settings → Import → Asana
- Or selectively create issues manually for active work only (cleaner)

**Recommendation: Don't import everything.**

Only migrate:
- Current sprint tasks (in progress)
- Backlog items that are refined and ready
- Active bugs

Leave the cruft behind. This is a fresh start.

**Map your Asana structure to Linear:**

| Asana | Linear |
|-------|--------|
| Development + Testing projects | Single Team |
| Tasks | Issues |
| Subtasks | Sub-issues |
| Sections (Backlog, In Progress, etc.) | Status (automatic) |
| Sprint custom field | Cycles |
| Type custom field | Labels |
| Estimate custom field | Estimate (built-in) |

**Create the key views:**

Linear views to set up:
- **My Issues** — Built-in, shows assigned work
- **Current Cycle** — Filter by active cycle
- **Backlog** — Built-in view for un-cycled issues
- **Roadmap** — Built-in, shows projects over time (share with Leonardo)

**Add Leonardo as a viewer:**
- Invite with Guest role so he can see the roadmap
- Or share roadmap view as a public link

### End of This Sprint: Ready to Go

By the Thursday sprint planning of next sprint, you should have:
- [ ] Linear workspace configured
- [ ] Team, Projects, Cycles set up
- [ ] Active backlog migrated
- [ ] Mike and Shamil have accounts and have explored
- [ ] Leonardo has visibility (viewer access or roadmap link)

---

## Part 4: Next Sprint — First Full Cycle in Linear

### Thursday: Sprint Planning in Linear

**Before the meeting:**
- Backlog should have refined, estimated issues
- Cycle for next 2 weeks should exist

**During planning:**

1. Open the Backlog view
2. Review priorities: "This sprint we're focused on X and Y"
3. Drag issues into the current Cycle
4. Each issue should already have:
   - Estimate (from refinement)
   - Project (epic it belongs to)
   - Assignee
5. Stop when capacity is reached (~6-7 days of estimates per person)
6. Ask: "Can you commit to this?" — adjust if no

**Linear makes this faster** because:
- Cycles are first-class, not a custom field
- Dragging into a cycle is one action
- The view auto-filters to show cycle contents

### Wednesday: Refinement in Linear

**Goal:** Take specs from Notion, break into issues, estimate.

**In Linear:**
1. Open the relevant Project (e.g., "MS Teams Integration")
2. Create issues for upcoming work
3. Add to Backlog (not to a Cycle yet)
4. Estimate together with the assignee
5. Link to Notion spec in the issue description

**Issues should be:**
- ≤3 days of work
- Estimated by the person doing them
- Linked to a spec if non-trivial

### Wednesday: Sprint Demo in Linear

**During demo:**
1. Open the current Cycle view, filter by Status = Done
2. Walk through completed issues
3. For each: quick demo or description
4. Record Estimate vs. Actual (add "Actual" as a custom field if needed)

### Wednesday: Retrospective

**Add this standing question:**
> "Look at Estimate vs Actual for this cycle. What was off and why?"

Categories of "why":
- Scope was unclear → refinement problem
- Unexpected complexity → estimation skill
- Interruptions → sprint protection problem
- External dependency → planning problem

Track which category comes up most. That's your systemic issue.

---

## Part 5: Ceremony Cadence Summary

| Day | Ceremony | Duration | Tool |
|-----|----------|----------|------|
| Wednesday | Sprint Demo | 30 min | Linear: Cycle view → Done |
| Wednesday | Retrospective | 20 min | Review estimates vs actuals |
| Wednesday | Refinement | 30-45 min | Linear: Create issues from Notion specs |
| Thursday | Sprint Planning | 30 min | Linear: Backlog → Cycle |

---

## Part 6: Tracking Velocity (Sprints 2-5)

### If using Linear Business ($16/user):

Linear Insights gives you:
- Cycle velocity (issues completed, estimates completed)
- Scope change tracking (what was added mid-cycle)
- Team workload distribution

No spreadsheets needed — it's in the UI.

### If using Linear Basic ($10/user):

Track manually in a spreadsheet:

| Cycle | Person | Issue | Estimate | Actual | Ratio |
|-------|--------|-------|----------|--------|-------|
| C1-2026 | Mike | Auth flow | 2 | 2.5 | 1.25 |
| C1-2026 | Mike | API endpoint | 1 | 1 | 1.0 |
| C1-2026 | Shamil | DB migration | 3 | 6 | 2.0 |

Add a custom field "Actual" (number) to capture this per issue.

### Metrics to track:

- **Ratio per person:** Actual ÷ Estimate (target: 1.0-1.3)
- **Cycle completion %:** Issues done ÷ Issues committed
- **Points/days completed per cycle:** Total estimates done (this is velocity)

After 4 cycles, you'll have enough data to:
- Predict capacity accurately
- Have concrete conversations about estimation accuracy
- Show Leonardo "we ship X points per cycle"

---

## Part 7: Implementation Checklist

### This Sprint (Sprint 1 — still in Asana)

**Methodology:**
- [ ] Add Estimate/Actual fields to Asana project
- [ ] Estimate all tasks at Thursday planning
- [ ] Fill in actuals at Wednesday demo
- [ ] Run retro with estimate/actual review

**Priorities:**
- [ ] Write Q1 2026 Priorities page in Notion
- [ ] Share with Oseas and Leonardo

**Linear Prep:**
- [ ] Get Leonardo's approval for Linear trial
- [ ] Create Linear workspace
- [ ] Configure team, projects, cycles, labels
- [ ] Invite Mike and Shamil
- [ ] Migrate active backlog
- [ ] Give Leonardo viewer access

### Next Sprint (Sprint 2 — first cycle in Linear)

- [ ] Run full sprint in Linear
- [ ] Thursday planning: Drag backlog → cycle
- [ ] Wednesday refinement: Create issues from specs
- [ ] Wednesday demo: Review completed issues
- [ ] Wednesday retro: Review estimates vs. actuals
- [ ] Track velocity (Insights or spreadsheet)

### Sprints 3-5

- [ ] Continue tracking velocity
- [ ] Review: Are estimates getting more accurate?
- [ ] Review: Is cycle completion % improving?
- [ ] Decide: Stay on Linear Basic or upgrade to Business?
- [ ] Have data-driven conversation with Shamil if needed

---

## Appendix A: The Shamil Conversation

Once you have 2-3 cycles of data in Linear, you can have a specific conversation:

**Frame:** "I want to look at our estimation accuracy across the team to improve our planning."

**Data:** Show the estimate/actual ratios for everyone (including Mike, including yourself if applicable).

**Question:** "I'm seeing your tasks are coming in at 2x the estimate on average. What's happening? Is it scope creep, unclear specs, unexpected complexity, or something else?"

**Outcomes:**
- If scope creep: "Let's agree to flag when scope grows mid-task"
- If unclear specs: "Let's spend more time in refinement on your tasks"
- If complexity: "Let's 2x your estimates going forward until the ratio normalizes"
- If other: Address the root cause

This is a process conversation, not a performance conversation — until the pattern persists after adjustments.

---

## Appendix B: What Stays in Asana

Linear is for engineering execution. Asana remains for:

- Cross-functional projects (marketing, sales, ops)
- Company-wide initiatives
- Client project tracking
- Leonardo's operational visibility across all departments

**The bridge between tools:**

High-level milestones can live in Asana for company visibility:
- "MS Teams Integration — Q1 target"
- "P&G Go-Live — February"

The actual engineering work lives in Linear. Ruy updates Asana milestones weekly (5 minutes) or links to Linear's public roadmap view.

---

## Appendix C: Linear vs Asana Cost Comparison

For 3 engineering users:

| Tool | Tier | Monthly | Annual |
|------|------|---------|--------|
| Asana Advanced | Required for portfolios | $75 | $900 |
| Linear Basic | Sufficient for sprints | $30 | $360 |
| Linear Business | Adds Insights analytics | $48 | $576 |

**Linear Basic saves $540/year** compared to Asana Advanced, with better sprint features.

Start with Linear Basic. Upgrade to Business after 2-3 cycles if you want built-in velocity charts instead of spreadsheets.
