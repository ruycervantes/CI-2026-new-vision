# CLAUDE.md

Instructions for Claude Code when working in this repository.

## Project Context

This is the **command center** for Conscious Insights v2 evolution. Ruy is acting as PM + CTO with a 3-month runway to prove product-market fit.

**Key constraint:** Limited time, small team. Prioritize ruthlessly.

## How to Help

### When Updating Vision Document (`conscious-insights-v2-english.md`)
- Check `action-items-ruy-jan2026.md` for documented gaps
- Main gaps: goal-based flow, goals dashboard, multi-session methodology
- Keep the document structure intact - it's been reviewed by Oseas
- Spanish quotes can stay as-is (team is bilingual)

### When Writing Sprint Stories or Tasks
- Reference Q1 priorities in `README.md`
- Owners: Mike (Teams), Shamil (Thinking Partner), Daniel (infra), Leo (testing/PMF)
- Keep stories concrete and actionable
- Include acceptance criteria

### When Doing Research (Competitors, HCI)
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

| Document | Purpose | Update Frequency |
|----------|---------|------------------|
| `README.md` | Command center overview | Weekly |
| `conscious-insights-v2-english.md` | Core vision | As gaps are filled |
| `action-items-ruy-jan2026.md` | Master task list | After every session |
| `meeting-notes-*.md` | Meeting records | Per meeting |
| `handwritten-notes-transcription.md` | Personal reflections | Reference only |

## Technical (Slides)

The pitch slides are a static HTML/CSS/JS site:

- **Run locally:** Open `index.html` in browser
- **Deploy:** Push to master → Netlify auto-deploys
- **Diagrams:** Generated with Gemini (prompts in `diagram-prompts.md`)

### Brand Colors
- Yellow: #FFD500
- Red: #C9332B
- Gray: #E6E6E6

## Key Terminology

- **Thinking Partner** - AI coaching mode (reflection, perspective, gap awareness)
- **Accountability Partner** - Microhabits mode (daily practice, follow-ups)
- **The Gap** - Distance between "who I am" and "who I want to be"
- **PMF** - Product-Market Fit
- **Applied Learning** - Learning through practice, not just content

## Team Context

- **Ruy** - PM + CTO, decision maker, writes vision/methodology
- **Mike** - Dev lead, Barcelona-based, owns Teams integration
- **Shamil** - Dev, works on Thinking Partner features
- **Daniel** - Dev, infrastructure and deployment
- **Leo** - Sales, owns PMF validation and demo approval
- **Horacio** - Coach SME, needed for methodology validation
- **Oseas** - CEO, strategic alignment, board communication

## What NOT to Do

- Don't add time estimates to plans
- Don't create new markdown files unless asked
- Don't restructure the vision document without asking
- Don't guess at technical architecture - ask Mike
