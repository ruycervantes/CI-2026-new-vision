# Stoic Platform — Command Center

## What This Is

Strategic planning hub for the Stoic platform (formerly Conscious Insights). Contains platform vision, product specs, roadmap, and action items.

**Timeline:** 3 months to prove product-market fit.

---

## Strategic Positioning

**We help humans have better conversations** — with themselves, with others, as teams, as organizations — through AI that increases consciousness.

**Two design spaces, one shared foundation:**
- **Leadership Development (LD):** Individual behavior change — closing the gap between who you say you want to be and who you show up as
- **Team Effectiveness (HPT):** Team conversations — agreements, commitments, facilitation, evolving together
- **Shared:** AI Coach with multi-session memory, enterprise integration, visibility as design constraint

---

## Core Documents

| Document | Purpose |
|----------|---------|
| [`core/vision.md`](core/vision.md) | **Platform vision** — why we exist, two design spaces, strategic filter |
| [`core/vision-behavior-change.md`](core/vision-behavior-change.md) | **LD product spec** — behavior change methodology, goal hierarchy, One Coach Relationship |
| [`core/roadmap.md`](core/roadmap.md) | **Engineering roadmap** — shared foundation (Q1) + feature candidates by path |
| [`core/alignment.md`](core/alignment.md) | **Leadership alignment** — decisions, validation plan, roles |
| [`core/MVP-offer-hpt.md`](core/MVP-offer-hpt.md) | **HPT near-term MVP** — 90-day hybrid cycle for market validation |
| [`research/coaching/ai-coach-design-considerations.md`](research/coaching/ai-coach-design-considerations.md) | **AI Coach architecture** — memory, implementation paradigms, design questions |
| [`research/coaching/minimum-ai-coaching-for-te.md`](research/coaching/minimum-ai-coaching-for-te.md) | **AI Coach ↔ HPT bridge** — minimum coaching needed for team effectiveness to work |

## Other Folders

| Path | Contents |
|------|----------|
| `team-effectiveness/` | HPT research and synthesis (methodology, synthesis-v2, design rationale) |
| `enterprise/` | SSO, identity (WorkOS), HRMS integration strategy |
| `research/coaching/` | Coaching methodology research — AI Coach architecture, knowledge framework, minimum coaching for TE, interview data |
| `calls/` | Call transcripts and processed summaries |
| `team/` | Sprint status per person, team profiles, process log |
| `thinking/` | Working documents, exploratory notes |
| `sprints/` | Team sprint stories + `backlog.md` (committed work not yet in a sprint) |
| `site/` | Netlify site (HTML pages + diagrams) |
| `archive/` | Previous vision drafts, old meeting notes, diagram prompts |

---

## Team

| Person | Role |
|--------|------|
| **Ruy** | PM + CTO — vision, methodology, Coach design, roadmap |
| **Oseas** | CEO — strategic alignment, board communication, lockstep validation |
| **Nelson** | HPT market validation, impact/visibility design, Thierry coordination |
| **Mike** | Dev lead — Teams integration, technical architecture (Barcelona) |
| **Shamil** | Dev — Coach features, check-in loop |
| **Daniel** | Dev — Infrastructure, deployment automation |
| **Leo** | Sales — PMF validation, customer conversations, demo approval |
| **Horacio** | Coach SME — methodology validation |

---

## Q1 2026 Priorities

### Building (Shared Foundation)
| Feature | Owner | Status |
|---------|-------|--------|
| MS Teams Notifications | Mike | In progress |
| Check-in Loop | Shamil | Ready to build |
| Coach Multi-Session | Shamil + Ruy | Needs Horacio |
| Installation Script + WorkOS POC | Daniel | In progress / Q1 |
| Voice OR Bidirectional Chatbot | TBD | Validate with Leo |

### Validating
- **LD market:** Leo running customer conversations
- **HPT market:** Nelson with current product + visual prototypes
- **Methodology:** Ruy + Horacio

---

## Ruy's Productivity System

Two layers: **capture** (this repo) and **execution** (Todoist).

```
Calls/meetings/notes → action items file → triage → Todoist @this-week → daily execution
```

**Upstream (this repo):**
- `action-items-ruy-{month}{year}.md` — monthly action items file. Items land here from calls, meetings, `/process-call`, `/handwritten`, thinking sessions. Triaged end-of-sprint or when heavy.
- `okrs-q1-2026.md` — north star for what matters. Used during triage to prioritize.
- `team/oseas-1on1-log.md` — running log of Oseas conversations, pending items for next meeting.

**Downstream (Todoist):**
- Labels: @this-week, @next-week, @this-month, @someday + energy tags (@deep-work, @quick-win, @energy-low)
- Daily: pick 3 important + 3 quick wins from @this-week
- Weekly (Monday): `/weekly-plan` to triage and set top 3 outcomes

**Rituals:**
| When | What | Command |
|------|------|---------|
| Daily | Review Todoist, pick focus | `/today` |
| Monday | Weekly planning, consolidate + triage | `/weekly-plan` |
| Thursday (post-sprint-planning) | Triage action items, cross-ref Todoist | `/triage` |
| When file feels heavy | Same as above | `/triage` |

## Working Files

| Path | Purpose |
|------|---------|
| [`okrs-q1-2026.md`](okrs-q1-2026.md) | **Ruy's Q1 OKRs** — AI Coach, PMF validation, execution |
| `action-items-ruy-feb2026.md` | Current month action items (upstream source of truth) |
| `team/process-log.md` | Living process decisions — reviewed at each sprint retro |
| `team/oseas-1on1-log.md` | Oseas 1-on-1 running log |
| `sprint-*-2026-*.md` | Ruy's sprint focus |
| `handwritten/` | Drop zone for handwritten note photos |

---

## Quick Links

- **Vision site:** [Netlify deployment](https://ci-2026-vision.netlify.app) (or open `site/index.html`)
- **Run locally:** Open `site/index.html` in browser
- **Deploy:** Push to master → Netlify auto-deploys
