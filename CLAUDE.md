# CLAUDE.md

Instructions for Claude Code when working in this repository.

## Project Context

This is the **command center** for Conscious Insights v2 evolution. Ruy is acting as PM + CTO with a 3-month runway to prove product-market fit (PMF).

**Key constraint:** Limited time, small team. Prioritize ruthlessly.

## Team

- **Ruy** - PM + CTO, decision maker, writes vision/methodology
- **Mike** - Dev lead, Barcelona-based, owns Teams integration
- **Shamil** - Dev, works on Coach features
- **Daniel** - Dev, infrastructure and deployment
- **Leo** - Sales, owns PMF validation and demo approval
- **Horacio** - Coach SME, needed for methodology validation
- **Oseas** - CEO, strategic alignment, board communication

## Document Map

### Core Documents (`core/`)

Individual coaching product vision and roadmap. Spanish quotes can stay as-is (team is bilingual).

| Document | Purpose |
|----------|---------|
| `vision.md` | Methodology, user journey, architecture. Key sections: Goal Hierarchy, Change Process, Coach/Daily Companion modes, Juan's Journey |
| `roadmap.md` | Q1/Q2/H2 features, dependencies, team assignments |
| `alignment.md` | Leadership sign-off, validation activities, commitments |

Previous versions in `archive/vision-versions/`.

### Team Effectiveness (`team-effectiveness/`)

Separate product track for team-level coaching and development.

| Path | Purpose |
|------|---------|
| `vision.md` | Product vision, MVP approach, intervention matrix |
| `research/` | Analysis and synthesis (methodology.md, synthesis-v1.md, synthesis-v2.md) |
| `sources/` | HPT Katzenbach docs, team survey instruments, historical survey data |

Related call transcripts in `calls/team-effectiveness/`.

### Enterprise (`enterprise/`)

Cross-cutting infrastructure (SSO, identity via WorkOS, HRMS integration) that applies to both individual and team products.

| Document | Purpose |
|----------|---------|
| `integration-strategy.md` | SSO, identity, HRMS integration strategy, P&G case study |

### Research (`research/`)

Ethnographic design research for individual coaching product. Team effectiveness research lives in `team-effectiveness/`.

| Path | Purpose |
|------|---------|
| `sources/application-coaching/` | Primary methodology docs (AC Handbook, CB Workbook, Magic Cards, coaching cases) |
| `interviews/` | Raw interview transcripts, organized by informant (e.g., `horacio-jan2026/`) |
| `analysis/` | Case studies, intervention analysis, observations |
| `coaching-knowledge-framework.md` | Master synthesis - three-layer framework consolidating all research |

**When doing competitive/HCI research:** Answer the key question "Are we differentiated or 80/20 replaceable?" and connect findings to product decisions.

### Calls (`calls/`)

Call transcripts and processed summaries. Use `/process-call` to process new transcripts.

| Folder | Contents |
|--------|----------|
| `team-effectiveness/` | Team effectiveness interviews (Dolo, etc.) |
| `application-coaching/` | Coaching methodology calls (Richi, Horacio) |
| `strategy/` | Strategic discussions (Oseas 1-1s) |
| `operations/` | Dev/ops calls (Daniel, Shamil, Leo) |

**When reviewing meeting notes:** Extract action items, capture key decisions and who made them, note blocking items.

### Thinking (`thinking/`)

Working documents, brain dumps, exploratory notes. Not finalized analysis.

### Working Files (root)

| Path | Purpose |
|------|---------|
| `README.md` | Command center overview |
| `site/` | Netlify site (index.html, vision.html, roadmap.html, diagrams/) |
| `sprint-*-2026-*.md` | Ruy's sprint focus |
| `action-items-ruy-{month}.md` | Master task list / backlog |
| `sprints/` | Team sprint stories (use `/sprint-stories` to create) |
| `handwritten/` | Drop zone for handwritten note photos (use `/handwritten` to process) |

**When writing sprint stories:** Reference Q1 priorities in README.md. Owners: Mike (Teams), Shamil (Coach features), Daniel (infra), Leo (testing/PMF). Keep stories concrete with acceptance criteria.

### Archive (reference only)

Previous vision drafts, meeting summaries, diagram prompts, old diagrams, transcribed handwritten notes.

## Technical

- **Run locally:** Open `site/index.html` in browser
- **Deploy:** Push to master → Netlify auto-deploys

## Key Terminology

### Individual Coaching
- **Coach** - Deep conversation mode (goal-setting, processing setbacks, evolving the plan)
- **Daily Companion** - Daily practice mode (reminders, check-ins, progress tracking)
- **Goal Hierarchy** - Destination Goal → Management Goal → Tracking Goal
- **The Gap** - Distance between "who I am" and "who I want to be"
- **GPS Dashboard** - Visual showing progress toward Destination Goal
- **If-Then Habit** - Implementation Intention format ("If X, then Y")
- **Adjust Stage** - When users struggle, help them reinterpret and adapt (not just track failure)
- **Applied Learning** - Learning through practice, not just content

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

### Work (Sprints & Calls)
| Command | Description |
|---------|-------------|
| `/process-call` | Deep analysis of call transcripts - creates summary, strategic analysis, and extracts action items |
| `/planning-review` | **Sprint planning** - right-size deliverables, create sprint files for dev team |
| `/sprint-stories` | **Team sprint stories** - create stories for Mike, Shamil, Daniel, Leo |

## What NOT to Do

- Don't add time estimates to plans
- Don't create new markdown files unless asked
- Don't restructure the vision document without asking
- Don't guess at technical architecture - ask Mike
