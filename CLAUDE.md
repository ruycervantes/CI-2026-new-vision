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

### When Doing Ethnographic Research (`research/`)
- Raw transcripts go in `research/interviews/{informant-date}/`
- Analysis outputs go in `research/analysis/`
- Update `research/coaching-knowledge-framework.md` with new findings
- Sources (methodology docs) live in `research/sources/`

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

| Document | Purpose | Update Frequency |
|----------|---------|------------------|
| `core/vision.md` | Methodology, user journey, architecture | As needed |
| `core/roadmap.md` | Q1/Q2/H2 features, dependencies, team assignments | Each quarter |
| `core/alignment.md` | Leadership sign-off, validation activities | Per alignment meeting |

### Research (`research/`)

Ethnographic design research to inform AI coaching product.

| Folder | Purpose | Contents |
|--------|---------|----------|
| `research/sources/` | Primary methodology docs | Application Coaching, CB Handbook, CB Workbook |
| `research/interviews/` | Raw interview transcripts | Organized by informant (e.g., `horacio-jan2026/`) |
| `research/analysis/` | Analysis outputs | Case studies, intervention analysis, observations |
| `research/coaching-knowledge-framework.md` | Master synthesis | Three-layer framework consolidating all research |

### Working Files (root)

| Document | Purpose | Update Frequency |
|----------|---------|------------------|
| `README.md` | Command center overview | Weekly |
| `site/` | Netlify site (index.html, vision.html, roadmap.html, diagrams/) | When vision changes |
| `sprint-*-2026-*.md` | Ruy's sprint focus (e.g., `sprint-2-2026-foundation.md`) | During sprint |
| `action-items-ruy-jan2026.md` | Master task list / backlog | After every session |
| `sprints/` | Team sprint stories (use `/sprint-stories` to create) | Before sprint planning |
| `handwritten/` | Drop zone for handwritten note photos | As needed (use `/handwritten` to process) |
| `calls/` | Operational call transcripts and summaries | After calls (use `/process-call` to process) |

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

- **Coach** - Deep conversation mode (goal-setting, processing setbacks, evolving the plan)
- **Daily Companion** - Daily practice mode (reminders, check-ins, progress tracking)
- **Goal Hierarchy** - Destination Goal → Management Goal → Tracking Goal
- **The Gap** - Distance between "who I am" and "who I want to be"
- **GPS Dashboard** - Visual showing progress toward Destination Goal
- **If-Then Habit** - Implementation Intention format ("If X, then Y")
- **Adjust Stage** - When users struggle, help them reinterpret and adapt (not just track failure)
- **PMF** - Product-Market Fit
- **Applied Learning** - Learning through practice, not just content

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
