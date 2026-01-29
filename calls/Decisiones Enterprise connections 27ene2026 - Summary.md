# Enterprise Connections Technical Planning - Summary
**Date:** January 27, 2026
**Participants:** Ruy (PM/CTO), Daniel (Infrastructure), Mike (Dev Lead)
**Context:** Urgent planning session - skipped sprint retro to address enterprise integration decisions discussed via email

---

## Executive Summary

Team aligned on Q1 enterprise integration strategy: (1) continue Teams integration (Mike), (2) complete installation script automation (Daniel), and (3) create WorkOS SSO/provisioning POC using Boetus as playground (Daniel). Decided to use pip over UV in production for security isolation. Dashboard login deferred but flagged as future need.

---

## 1. Enterprise Integration Requirements Breakdown

**What "integration" means to clients (unpacked):**

| Need | What It Really Means | Priority |
|------|---------------------|----------|
| SSO | No new passwords, just click and work | Phase 0 |
| Provisioning | Manage who has access from their HR system, not Excel | Phase 0 |
| Messaging (Teams/Slack) | Adoption - tools in the workflow, not another app | Parallel |
| HRMS Read | Pull context: role, location, performance reviews, competencies | Phase 2 |
| HRMS Write | Write completion data, assessment results back | Phase 3 (unclear value) |
| LMS Embed | Embed chatbots inside their LMS (like Thinkific) | Per-platform, no generic |

**Key insight:** The phrase "we want integration" is vague - clients mean different things. Team broke it down into distinct phases.

---

## 2. Phased Integration Strategy

**Agreed architecture:**

```
Phase 0: SSO + Provisioning (WorkOS)
  └─ User signs in via their IdP → WorkOS validates → Our app provisions

Phase 1 (parallel): Teams Integration
  └─ Alerts + bidirectional chat (already in development)

Phase 2: HRMS Read
  └─ Pull context for personalization (role, competencies, etc.)

Phase 3: HRMS Write
  └─ Push completion/assessment data back (value unclear)
```

---

## 3. WorkOS Architecture Discussion

**How WorkOS fits:**
- Acts as authentication middleware between client IdP (Ping, Okta, Microsoft, Google) and our apps
- Does NOT replace our user database - Postgres stays
- Handles the translation layer between different IdPs
- Single URL limitation: need middleware to route users to correct instance (pg.stoic, axialent.stoic, etc.)

**P&G Exception (Daniel's explanation):**
- Could have used WorkOS but would have needed custom middleware anyway for translation
- Decided to go direct since "all we need is translation"
- WorkOS remains optional layer we can add when needed

**Dashboard login gap:**
- Admin dashboard has no login currently
- Decision deferred: evaluate if WorkOS makes sense or use simpler approach

---

## 4. Q1 POC Plan - WorkOS with Boetus

**Decision:** Create POC using Boetus.com (their own Microsoft tenant)

**POC scope:**
1. Configure WorkOS to handle Boetus.com authentication
2. Route users to either Thinkific or Conscious Insights based on role
3. Test provisioning flow

**Potential Phase 2:**
- If POC goes well, implement for Axialent internal use
- Axialent would be "staging" environment, real clients = "production"

**Why Boetus:**
- They own the Microsoft tenant
- Can experiment freely
- Daniel has bandwidth (government job leave = ~1 month available)

---

## 5. Google Workspace Integration (Exploratory)

**Context:** Mercado Libre (potential client) uses only Google

**Discussion:**
- Daniel has paid Google Workspace account, could explore
- First step would be SSO with Google Workspace (before Google Meet integration)
- Google Meet assumed to be less complex than Teams (unverified)
- NOT committing to build this quarter, but worth exploring

**Decision:** Daniel can explore informally, not a sprint commitment

---

## 6. Installation Script Status (Daniel)

**Current work:**
- CloudPanel instance creation partially solved
- Resolving port tracking (will use text file in system directory)
- pip vs UV decision (see below)

**pip vs UV Decision:**
- **Issue:** UV uses aggressive caching with shared repository across all sites
- **Risk:** If a malicious package update happens, all instances get infected simultaneously
- **Decision:** Keep UV for local development, use pip in production (isolated virtual envs per instance)
- **Alternative discussed:** Freeze library versions on release (but CICD not set up for this yet)

---

## 7. Admin Panel Architecture Discussion

**Current state:**
- Admin runs in Docker (docker-compose up)
- Chainlit runs as system service
- No unified start/stop script
- Admin not integrated into installation script

**Options discussed:**
1. Separate scripts for admin vs main app (admin doesn't need to run always)
2. Docker as optional deployment method
3. Single script that handles both with parameters

**Decision:** Docker should be OPTION, not requirement
- Local dev: pip/UV directly (easier)
- Production or client-hosted: Docker available

**Future admin capabilities discussed:**
- Wizard for creating new chatbot profiles/prompts
- HRMS field mapping configuration
- User management (current)
- Assessment visibility (current)

---

## 8. Teams Integration Status (Mike)

**Current state:**
- Local Microsoft development environment working well
- Approaching production deployment phase

**Upcoming needs:**
- Azure instance setup for production
- Manifest updates for new features
- Admin access request to Axialent Teams (potential blocker)
- Daniel support for deployment (estimated: last 15 days of Q1)

**Clarification from Daniel:**
- Azure mainly for app manifest management
- Bot Framework may incur some costs
- Teams integration = install app + configure manifest endpoints
- Existing Axialent Teams app just needs manifest update

---

## 9. Axialent HRMS (Personio)

**Discovery:** Axialent uses Personio (smaller company HRMS)

**Suggestion (Daniel):**
- Next quarter, do POC on Personio integration
- Create the "context pulling" layer using internal system
- Build the abstraction that can work with other HRMS later

---

## 10. HRMS Integration Research

**WorkOS capabilities (needs verification):**
- Claims integration with Bamboo HR, Workday
- "Directory Sync" - automatic user/group provisioning
- Unclear: how deep is the data access?

**Other options mentioned:**
- Merge.dev - API aggregator for multiple HRMS
- Mike's finding: WorkOS "pipes" for custom data flows

**Decision:** Research after SSO POC works

---

## 11. Daniel's Capacity and Commitments

**Personal context:**
- Baby due February 5 (~1 week)
- Government job: taking ~1 month leave
- Available to focus on CI work during that period

**Commitments:**
1. Finish installation script (ongoing)
2. WorkOS SSO POC with Boetus

**Condition:** No firefighting (e.g., P&G emergencies)

**Mike will need Daniel support:** Last 15 days of Q1 for Teams production deployment

---

## Key Decisions Made

| Decision | Details |
|----------|---------|
| pip in production | UV shared cache = security risk; use isolated venvs |
| WorkOS POC with Boetus | Internal playground for SSO testing |
| Docker optional | Keep as option for client-hosted deployments |
| Admin separate from main app | Can stop container when not needed |
| Google exploration informal | Daniel can look into it, not sprint commitment |

---

## Blockers Identified

| Blocker | Owner | Resolution |
|---------|-------|------------|
| Axialent Teams admin access | Ruy | Request from Mario when deployment ready |
| WorkOS single-URL limitation | Daniel | Build routing middleware as part of POC |
| CICD not set up | Team | Needed for proper release freezing |

---

## Next Steps

1. **Daniel:** Continue installation script, then WorkOS POC
2. **Mike:** Continue Teams development, flag when ready for production deployment
3. **Ruy + Mike:** Separate discussion needed on remaining sprint topics
4. **Team:** Sprint retrospective rescheduled (include Shamil)
