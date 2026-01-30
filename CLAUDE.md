# CLAUDE.md

Instructions for Claude Code when working in this repository.

## Project Context

This is the **command center** for Conscious Insights / Stoic platform evolution. Ruy is acting as PM + CTO with a 3-month runway to prove product-market fit (PMF).

**Key constraint:** Limited time, small team. Prioritize ruthlessly.

## Team

- **Ruy** - PM + CTO, decision maker, writes vision/methodology
- **Mike** - Dev lead, Barcelona-based, owns Teams integration
- **Shamil** - Dev, works on Coach features
- **Daniel** - Dev, infrastructure and deployment
- **Leo** - Sales, owns PMF validation and demo approval
- **Horacio** - Coach SME, needed for methodology validation
- **Oseas** - CEO, **PMF owner**, strategic alignment, board communication

## Ruy's Personal Productivity Workflow

### System Overview

Ruy uses a two-layer system:
1. **Action items file** (`action-items-ruy-{month}{year}.md`) — capture + context + triage workspace. This is upstream. Items land here from calls, meetings, thinking sessions, handwritten notes.
2. **Todoist** — daily/weekly execution. Downstream. Items get pulled here after triage with proper labels (@this-week, @next-week, @deep-work, etc.).

**Flow:**
```
Calls/meetings/notes → action items file → triage → Todoist → daily execution
```

### Cadences

**Daily:**
- Use `/today` to review Todoist @this-week, pick 3 important + 3 quick wins.

**Weekly (Monday):**
- Use `/weekly-plan` to consolidate action items + Todoist, triage to 15-20 tasks, identify top 3 outcomes.
- Review @this-week → move incomplete to @next-week if needed.
- Promote from @next-week → @this-week.

**End of sprint (Thursday, after planning) or when file feels heavy:**
- Use `/triage` to clean up the action items file.
- Cross-reference against Todoist for duplicates.
- Kill done/stale items, reframe changed items, create next month's file if end of month.

### Key Files

| File | Role |
|------|------|
| `action-items-ruy-{month}{year}.md` | Current month's action items (upstream source of truth) |
| `okrs-q1-2026.md` | OKRs — north star for prioritization |
| `team/oseas-1on1-log.md` | Running log of Oseas conversations + pending items |
| `team/status.md` | Sprint status per person, blockers, key decisions |
| `team/process-log.md` | Living process decisions, reviewed at each retro |
| `sprints/sprint-stories-jan2026.md` | Current sprint stories with acceptance criteria |

### Todoist Label System

See `.claude/commands/todoist-org.md` for full details. Key labels:
- **Time:** @this-week, @next-week, @this-month, @someday
- **Energy:** @deep-work, @quick-win, @energy-low
- **Status:** @Doing, @waiting, @followup, @urgent

**Principle:** Dates are for appointments, not aspirations. Labels are for possibilities, not obligations.

### When Skills Capture Action Items

`/process-call`, `/review-action-items`, and `/handwritten` should add items to the action items file with enough context to triage later. They do NOT push to Todoist — that happens during triage or weekly planning.

## Sprint Process (Team)

Post-planning steps are documented in `team/process-log.md` under Cadences.

**Weekly cadence:**
- **Monday:** Sprint prep — review `team/process-log.md`, prep retro data (estimates vs actuals)
- **Wednesday:** Retro + demo (shipping checklist: dev → staging → demo → team tests → ship)
- **Thursday:** Sprint planning → post-planning process above

**Key files:**
- `team/process-log.md` — living process decisions, reviewed at each retro
- `team/status.md` — sprint status per person, blockers, key decisions
- `sprints/sprint-stories-jan2026.md` — current sprint stories with acceptance criteria

---

## Document Map

### Core Documents (`core/`)

Platform vision, product specs, and roadmap. Spanish quotes can stay as-is (team is bilingual).

| Document | Purpose |
|----------|---------|
| `vision.md` | Platform vision — why we exist, two design spaces, strategic filter |
| `vision-behavior-change.md` | LD product spec — behavior change methodology, goal hierarchy, Coach + Daily Companion |
| `roadmap.md` | Engineering roadmap — shared foundation (Q1) + feature candidates by path |
| `alignment.md` | Leadership sign-off, validation activities, commitments |
| `MVP-offer-hpt.md` | HPT near-term MVP — 90-day hybrid cycle for market validation |
| `pitch.md` | Pitch deck content |

Previous versions in `archive/vision-versions/`.

### Team Effectiveness (`team-effectiveness/`)

Separate product track for team-level coaching and development.

| Path | Purpose |
|------|---------|
| `research/` | Analysis and synthesis (methodology.md, synthesis-v2.md) |
| `design-rationale.md` | Design rationale and decisions |
| `ai-coaching-dependency.md` | AI coaching dependency for TE |

Related call transcripts in `calls/team-effectiveness/`.

### Enterprise (`enterprise/`)

Cross-cutting infrastructure (SSO, identity via WorkOS, HRMS integration) that applies to both individual and team products.

| Document | Purpose |
|----------|---------|
| `integration-strategy.md` | SSO, identity, HRMS integration strategy, P&G case study |

### Coaching Research (`research/coaching/`)

Coaching methodology research — the source material for AI Coach design. Application coaching praxis, interview data, and analysis.

| Path | Purpose |
|------|---------|
| `sources/` | Primary methodology docs (AC Handbook, CB Workbook, Magic Cards, coaching cases) |
| `interviews/` | Raw interview transcripts, organized by informant (e.g., `horacio-jan2026/`) |
| `analysis/` | Case studies, intervention analysis, observations |
| `coaching-knowledge-framework.md` | Master synthesis - three-layer framework consolidating all research |
| `ai-coach-design-considerations.md` | AI Coach architecture — memory, implementation paradigms, design questions |
| `minimum-ai-coaching-for-te.md` | How AI Coach connects to Team Effectiveness — minimum coaching needed for HPT to work |

### Chatbot Design (`chatbot-design/`)

Process, instructions, and examples for designing custom chatbots on the platform. See `chatbot-design/README.md`.

### Calls (`calls/`)

Call transcripts and processed summaries. Use `/process-call` to process new transcripts.

| Folder | Contents |
|--------|----------|
| `team-effectiveness/` | Team effectiveness interviews (Dolo, etc.) |
| `application-coaching/` | Coaching methodology calls (Richi, Horacio) |
| `strategy/` | Strategic discussions (Oseas 1-1s) |
| `operations/` | Dev/ops calls (Daniel, Shamil, Leo) |

### Team (`team/`)

| Document | Purpose |
|----------|---------|
| `status.md` | Sprint status per person, blockers, key decisions, team profiles. Use `/update-team-status` to update. |

### Thinking (`thinking/`)

Working documents, brain dumps, exploratory notes. Not finalized analysis.

### Working Files (root)

| Path | Purpose |
|------|---------|
| `README.md` | Command center overview |
| `site/` | Netlify site (index.html, vision.html, roadmap.html, diagrams/) |
| `sprint-*-2026-*.md` | Ruy's sprint focus |
| `okrs-q1-2026.md` | Ruy's Q1 OKRs — AI Coach, PMF validation, execution |
| `action-items-ruy-{month}.md` | Master task list / backlog |
| `sprints/` | Team sprint stories (use `/sprint-stories` to create) + `backlog.md` (committed work not yet in a sprint) |
| `handwritten/` | Drop zone for handwritten note photos (use `/handwritten` to process) |

### Archive (reference only)

Previous vision drafts, meeting summaries, diagram prompts, old diagrams, transcribed handwritten notes.

### Behavioral Guidelines

- **Competitive/HCI research:** Answer "Are we differentiated or 80/20 replaceable?" and connect findings to product decisions.
- **Meeting notes:** Extract action items, capture key decisions and who made them, note blocking items.
- **Sprint stories:** Reference Q1 priorities in README.md. Owners: Mike (Teams), Shamil (Coach features), Daniel (infra), Leo (testing/PMF). Keep stories concrete with acceptance criteria.

## Technical

- **Run locally:** Open `site/index.html` in browser
- **Deploy:** Push to master → Netlify auto-deploys

## Key Terminology

### Individual Coaching
- **Coach** - Deep conversation mode (goal-setting, processing setbacks, evolving the plan)
- **Daily Companion** - Daily practice mode (reminders, check-ins, progress tracking)
- **Goal Hierarchy** - Destination Goal → Management Goal → Tracking Goal
- **The Gap** - Distance between "who I am" and "who I want to be"
- **If-Then Habit** - Implementation Intention format ("If X, then Y")
- **Adjust Stage** - When users struggle, help them reinterpret and adapt (not just track failure)

### Team Effectiveness
- **HPT** - High Performing Teams (Katzenbach framework + Axialent experience)
- **4 Quadrants** - Team assessment dimensions from Axialent Team Effectiveness Assessment
- **Intervention Matrix** - Personal/Team/System × Before/During/After framework for interventions
- **CB Assessment** - Conscious Business individual assessment (maps to team gaps)

## Available Commands

### Personal Productivity (Ruy)
| Command | Description |
|---------|-------------|
| `/think` | Thinking partner for working through ideas - brainstorming, exploring concepts, developing plans through conversation. Captures incrementally to `thinking/` folder. |
| `/today` | Daily work review - fetch today's Todoist tasks, organize by priority, recommend focus. Use at start of day or when planning. |
| `/weekly-plan` | Weekly planning triage - consolidate action-items + Todoist, triage to 15-20 tasks, identify top 3 outcomes. Use on Mondays or when starting a new week. |
| `/handwritten` | Transcribe handwritten notes from `handwritten/` folder and propose additions to action items |
| `/review-action-items` | Process new items into action-items file |
| `/triage` | Triage action items — clean up, reorganize, prepare for next period. End-of-sprint or when file feels heavy. |

### Work (Sprints & Calls)
| Command | Description |
|---------|-------------|
| `/process-call` | Deep analysis of call transcripts - creates summary, strategic analysis, and extracts action items |
| `/planning-review` | **Sprint planning** - right-size deliverables, create sprint files for dev team |
| `/sprint-stories` | **Team sprint stories** - create stories for Mike, Shamil, Daniel, Leo |
| `/sync-notion` | **Notion sync** - push markdown docs to Notion pages (images, cross-links, tables) |
| `/publish` | **Knowledge base publish** - sync shareable docs to `stoicenteprises/knowledgebase2026` GitHub repo |

## Notion Sync

Syncs 6 core markdown docs to Notion pages under **"Vision, Roadmap and Docs 2026"** (page ID: `2f7073cafffb8038bcf7f4335612b1e2`).

**Sync command:**
```bash
export $(cat .env | xargs) && python3 scripts/notion-sync.py
```

**Sync one file:** `python3 scripts/notion-sync.py --file core/alignment.md`

**Config:** `scripts/notion-sync-config.yaml` — maps files to Notion page titles. To add a new doc, add an entry there and run sync.

**Synced files:**
| File | Notion title |
|------|-------------|
| `team-effectiveness/research/synthesis-v2.md` | TE — Synthesis v2 |
| `team-effectiveness/research/methodology.md` | TE — Methodology |
| `core/alignment.md` | Leadership Alignment |
| `core/vision.md` | Platform Vision |
| `core/roadmap.md` | Engineering Roadmap |
| `core/MVP-offer-hpt.md` | Team Performance MVP |

**Images:** Files under `site/` use Netlify URLs (`stoic-2026.netlify.app`). Other images use GitHub raw URLs. Images must be committed and pushed to git before they render in Notion.

**Cross-doc links:** Relative `.md` links between the 6 synced pages resolve to Notion page URLs. Links to non-synced files render as plain text.

**API key:** `NOTION_API_KEY` in `.env` (not committed). The parent page must be shared with the Notion integration.

## What NOT to Do

- Don't add time estimates to plans
- Don't create new markdown files unless asked
- Don't restructure the vision document without asking
- Don't guess at technical architecture - ask Mike
