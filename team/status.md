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
| Coach Multi-Session design | Blocked — needs Horacio meeting |
| Thinking Partner feature | To do (Ruy builds this) |

### Next Milestone
- Horacio meeting → unblock Coach Multi-Session
- Fri check-in with Shamil on Cyclic Flow

---

## Oseas

**Location:** Barcelona, Spain

### Sprint 3 Status
- Strategic oversight
- Behavior Adoption Tracking input (Q2 planning with Ruy)

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

### Oseas
**Role:** CEO, strategic alignment, board communication.
