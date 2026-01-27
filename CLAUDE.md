# CLAUDE.md

Instructions for Claude Code when working in this repository.

## Project Context

This is the **command center** for Conscious Insights v2 evolution. Ruy is acting as PM + CTO with a 3-month runway to prove product-market fit.

**Key constraint:** Limited time, small team. Prioritize ruthlessly.

## How to Help

### When Updating Core Documents (`core/`)
- **vision.md** - Methodology, user journey, system design. Key sections: Goal Hierarchy, Change Process, Coach/Daily Companion modes, Juan's Journey
- **roadmap.md** - Q1/Q2/H2 features, dependencies, team assignments
- **alignment.md** - Leadership sign-off, validation activities, commitments
- Previous versions in `archive/vision-versions/`
- Spanish quotes can stay as-is (team is bilingual)

### When Writing Sprint Stories or Tasks
- Reference Q1 priorities in `README.md`
- Owners: Mike (Teams), Shamil (Coach features), Daniel (infra), Leo (testing/PMF)
- Keep stories concrete and actionable
- Include acceptance criteria

### When Working on Team Effectiveness (`team-effectiveness/`)
- Vision and planning docs live in `team-effectiveness/vision.md`
- Research synthesis in `team-effectiveness/research/`
- HPT sources (Katzenbach, surveys) in `team-effectiveness/sources/`
- Related call transcripts in `calls/team-effectiveness/`
- This is a separate product track from individual coaching

### When Working on Enterprise Integration (`enterprise/`)
- Strategy docs in `enterprise/integration-strategy.md`
- Cross-cutting concerns: SSO, identity (WorkOS), HRMS integration
- Applies to both individual and team products

### When Doing Ethnographic Research (`research/`)
- Raw transcripts go in `research/interviews/{informant-date}/`
- Analysis outputs go in `research/analysis/`
- Update `research/coaching-knowledge-framework.md` with new findings
- Application coaching sources in `research/sources/application-coaching/`

### When Doing Competitive/HCI Research
- Summarize findings in markdown
- Answer the key question: "Are we differentiated or 80/20 replaceable?"
- Connect findings to product decisions

### When Creating Roadmap/Planning Documents
- Start from the 3-4 Q1 features agreed with Mike
- Include dependencies between features
- No time estimates - just sequence and dependencies

### When Reviewing Meeting Notes
- Extract action items to `action-items-ruy-jan2026.md`
- Capture key decisions and who made them
- Note blocking items and what unblocks them

## Document Map

**Keep README.md in sync** - when updating the document map here, also update README.md (and vice versa).

### Core Documents (`core/`)

Individual coaching product vision and roadmap.

| Document | Purpose | Update Frequency |
|----------|---------|------------------|
| `core/vision.md` | Methodology, user journey, architecture | As needed |
| `core/roadmap.md` | Q1/Q2/H2 features, dependencies, team assignments | Each quarter |
| `core/alignment.md` | Leadership sign-off, validation activities | Per alignment meeting |

### Team Effectiveness (`team-effectiveness/`)

Separate product track for team-level coaching and development.

| Document | Purpose |
|----------|---------|
| `team-effectiveness/vision.md` | Team effectiveness product vision, MVP approach, intervention matrix |
| `team-effectiveness/research/` | Analysis and synthesis (methodology.md, synthesis-v1.md, synthesis-v2.md) |
| `team-effectiveness/sources/` | HPT Katzenbach docs, team survey instruments, historical survey data |

### Enterprise (`enterprise/`)

Cross-cutting infrastructure that applies to any product (individual or team).

| Document | Purpose |
|----------|---------|
| `enterprise/integration-strategy.md` | SSO, identity (WorkOS), HRMS integration strategy, P&G case study |

### Research (`research/`)

Ethnographic design research for individual coaching product (team effectiveness research lives in `team-effectiveness/`).

| Folder | Purpose | Contents |
|--------|---------|----------|
| `research/sources/application-coaching/` | Primary methodology docs | AC Handbook, CB Workbook, Magic Cards, coaching cases |
| `research/interviews/` | Raw interview transcripts | Organized by informant (e.g., `horacio-jan2026/`) |
| `research/analysis/` | Analysis outputs | Case studies, intervention analysis, observations |
| `research/coaching-knowledge-framework.md` | Master synthesis | Three-layer framework consolidating all research |

### Calls (`calls/`)

Call transcripts and processed summaries, organized by topic.

| Folder | Contents |
|--------|----------|
| `calls/team-effectiveness/` | Team effectiveness interviews (Dolo, etc.) |
| `calls/application-coaching/` | Coaching methodology calls (Richi, Horacio) |
| `calls/strategy/` | Strategic discussions (Oseas 1-1s) |
| `calls/operations/` | Dev/ops calls (Daniel, Shamil, Leo) |

Use `/process-call` to process new transcripts.

### Thinking (`thinking/`)

Working documents, brain dumps, exploratory notes. Not finalized analysis.

| Document | Purpose |
|----------|---------|
| `thinking/where-to-pick-up-work.md` | Current state of team effectiveness + behavior change integration |
| `thinking/strategic-brain-dump.md` | Planning notes, operational commitments |

### Working Files (root)

| Document | Purpose | Update Frequency |
|----------|---------|------------------|
| `README.md` | Command center overview | Weekly |
| `site/` | Netlify site (index.html, vision.html, roadmap.html, diagrams/) | When vision changes |
| `sprint-*-2026-*.md` | Ruy's sprint focus (e.g., `sprint-2-2026-foundation.md`) | During sprint |
| `action-items-ruy-jan2026.md` | Master task list / backlog | After every session |
| `sprints/` | Team sprint stories (use `/sprint-stories` to create) | Before sprint planning |
| `handwritten/` | Drop zone for handwritten note photos | As needed (use `/handwritten` to process) |

### Archive (reference only)

| Folder | Contents |
|--------|----------|
| `archive/vision-versions/` | Previous vision drafts |
| `archive/meeting-notes/` | Meeting summaries and transcripts |
| `archive/diagram-prompts/` | Prompts used to generate diagrams |
| `archive/diagrams/` | Old diagram versions |
| `archive/handwritten-notes/` | Transcribed personal notes |
| `archive/unused-diagram-variants/` | Alternate diagram versions |
| `archive/index-slides-old.html` | Old pitch slides |

## Technical

The vision document is a static HTML/CSS site:

- **Run locally:** Open `site/index.html` in browser
- **Deploy:** Push to master → Netlify auto-deploys
- **Diagrams:** Generated with Gemini (prompts in `archive/diagram-prompts/`)
- **Old slides:** Archived at `archive/index-slides-old.html`

### Brand Colors
- Yellow: #FFD500
- Red: #C9332B
- Gray: #E6E6E6

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

### General
- **PMF** - Product-Market Fit

## Team Context

- **Ruy** - PM + CTO, decision maker, writes vision/methodology
- **Mike** - Dev lead, Barcelona-based, owns Teams integration
- **Shamil** - Dev, works on Coach features
- **Daniel** - Dev, infrastructure and deployment
- **Leo** - Sales, owns PMF validation and demo approval
- **Horacio** - Coach SME, needed for methodology validation
- **Oseas** - CEO, strategic alignment, board communication

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
