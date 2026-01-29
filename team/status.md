# Team Status & Development

> **Current Sprint:** Sprint 3, 2026 (starts Thu Jan 30)
> **Last updated:** January 28, 2026

---

## Shamil

**Location:** Barcelona, Spain (7-8 hrs ahead of Ruy)

### Sprint 3 Status
| Item | Status |
|------|--------|
| Daily Companion Cyclic Flow | Assigned — exploring system Wed-Thu, check-in Fri evening |
| Thinking Partner sidebar | Demoed — needs progressive display + commitment highlighting |

### Next Milestone
- **Fri Jan 31:** Propose technical approach for Cyclic Flow (30-min check-in)
- Then: implement in Sprint 3 (~1 sprint scope)

---

## Mike

**Location:** Barcelona, Spain

### Sprint 3 Status
| Item | Status |
|------|--------|
| MS Teams Notifications | In progress — local dev env working, approaching production deployment |
| VLAN Assessment Admin | Done — production-ready (demoed Jan 28) |
| Language selector removal | Assigned — single language per user for normal users |

### Next Milestone
- MS Teams Notifications shipped (Q1 foundation)
- Production deployment needs: Azure instance setup, manifest updates, Axialent Teams admin access
- Will need Daniel support for deployment (last 15 days of Q1)

---

## Daniel

**Location:** Guadalajara, Mexico (same TZ as Ruy)

### Sprint 3 Status
| Item | Status |
|------|--------|
| Installation Script Automation | In progress (resolving port tracking, pip vs UV decided) |
| WorkOS SSO POC (Boetus) | Assigned — after installation script |
| Profile/Prompt Creation | Not started |
| Testing Automation | Not started |

### Next Milestone
- Installation script completed
- WorkOS POC with Boetus (SSO + provisioning test)
- Support Mike on Teams production deployment (last 15 days of Q1)

**Note:** Baby due Feb 5 (~1 week); taking ~1 month government leave, available for CI work

---

## Leo

**Location:** Barcelona, Spain

### Sprint 3 Status
| Item | Status |
|------|--------|
| Voice vs Bidirectional validation | Pending — customer conversations |

### Next Milestone
- Voice vs Bidirectional decision (Q1)

---

## Ruy

**Location:** Guadalajara, Mexico

### Sprint 3 Status
| Item | Status |
|------|--------|
| Daily Companion Cyclic Flow FRD | Done — handed to Shamil |
| AI Coach design (shared foundation for LD + HPT) | In progress — design doc started (`thinking/ai-coach-design-considerations.md`) |
| Platform vision restructuring | In progress — processing calls, restructuring `core/` docs (see `thinking/call-processing-plan-28jan2026.md`) |
| Thinking Partner feature | To do (Ruy builds this) |

### Next Milestone
- Process remaining calls → restructure core docs (Step 3-5 of call processing plan)
- Fri check-in with Shamil on Cyclic Flow

**Note:** Ruy is a bottleneck for specs — Shamil had 2 idle days between sprints waiting for feature descriptions. Need to build a spec pipeline.

---

## Nelson

**Location:** Barcelona, Spain

### Sprint 3 Status
| Item | Status |
|------|--------|
| Impact/visibility design | In progress — designing what to show clients with current product |
| HPT blended journey spec | In progress — reviewing Ruy's Horacio/Richie materials, iterating on narrative |
| Thierry coordination | To do — schedule product vision review |

### Next Milestone
- Impact visibility design completed
- Review with Thierry for commercial lens validation

---

## Oseas

**Location:** Barcelona, Spain

### Sprint 3 Status
- Strategic oversight
- Behavior Adoption Tracking input (Q2 planning with Ruy)
- Mandated Thierry + Fernando Fascioli as commercial reviewers for all product direction (board decision)
- Confirmed AI Coach as shared foundation for LD + HPT (Jan 28)

---

## Notes

- Sprint Demo completed Jan 28 — Daniel absent
- Sprint planning Thursday Jan 30
- Sprint retro skipped Jan 27 — needs reschedule (include Shamil)

---

## Blockers

| Blocker | Owner | Resolution |
|---------|-------|------------|
| Axialent Teams admin access | Ruy | Request from Mario when deployment ready |
| WorkOS single-URL limitation | Daniel | Build routing middleware as part of POC |
| CICD not set up | Team | Needed for proper release freezing |

---

## Key Decisions

**Jan 28 Sprint Demo:**
- Progressive sidebar display — show fields as they're filled, not all upfront
- Single language per user — remove selector for normal users; set at provisioning

**Jan 28 Product Strategy (Oseas, Nelson, Mike, Ruy):**
- AI Coach is the shared technology foundation — serves both LD and HPT
- Impact/visibility must advance in lockstep with coaching quality ("Si tengo 10 de coaching y 2 de reporte, no lo vendo")
- Thierry + Fernando Fascioli review all product direction (board mandate)
- HPT-specific design waits for Dolo (Q2+); focus on common foundation now
- Nelson owns impact/visibility design
- Don't over-distinguish HPT vs LD at technology level — "todos son la misma chingadera" (Oseas)

**Jan 27 Enterprise Meeting:**
- pip in production — UV shared cache = security risk; use isolated venvs
- WorkOS POC with Boetus — internal playground for SSO testing
- Docker optional — keep as option for client-hosted deployments
- Google exploration informal — Daniel can look into it, not sprint commitment

---

## Team Profiles (Reference)

### Shamil
**Development Goals:** Learn to refine PRDs with technical detail before implementing. Do feature-driven development independently. Understand the full Daily Companion flow end-to-end.

**Skills:** Knows Postgres, can navigate the data model. Ready to take on features with less hand-holding.

### Mike
**Role:** Dev lead, owns Teams integration. Created Claude Code repo docs for the team.

**Skills:** Technical architecture ownership, MS Teams integration expertise. Local Microsoft dev environment working well.

### Daniel
**Role:** Owns infrastructure and deployment. Working on Sprint Automation (OKR #4).

**Skills:** Holds critical knowledge: WorkOS architecture, P&G SSO, CloudPanel config. Goal: remove Mike/Ruy as bottlenecks for client onboarding.

### Leo
**Role:** Sales lead, validates features with customers. Pipeline and demo approval.

**Goals:** Own PMF validation. Customer feedback → product decisions.

### Ruy
**Focus:** Methodology, roadmap, Coach design. Horacio/Dolo coordination. Unblock Shamil, guide his development.

### Nelson
**Role:** Product/operations lead for Axialent digital. Owns impact/visibility design and HPT blended journey spec. Increasingly technical — learning Claude Code and Cursor. May build chatbot wizard independently.

**Skills:** Understands Axialent's data landscape, commercial context, and client needs. Bridge between consulting team and product team.

### Oseas
**Role:** CEO, strategic alignment, board communication. Thinks commercially and in metaphors — anchor product conversations in what's sellable and visible.

### Thierry + Fernando Fascioli (External)
**Role:** Board-designated commercial reviewers. Must be included in product direction decisions. Thierry has strong commercial vision (anchored Vitro project to CFO-validated EBITDA impact). Fascioli is external board advisor.
