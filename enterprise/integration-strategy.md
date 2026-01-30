# Enterprise Integration Strategy

*Last updated: January 29, 2026*
*Origin: Discussion doc (Jan 21) → decisions made in Enterprise Connections call (Jan 27)*

**Status:** Q1 2026 plan decided. Teams integration first (Mike, parallel), WorkOS SSO/provisioning POC with Boetus (Daniel). HRMS integration deferred to Phase 2.

---

## The Strategic Risk: We Lose Deals to Inferior But Integrated Solutions

**Key insight from Oseas (to validate):** Enterprise clients will choose *inferior* products that integrate with their systems over *superior* products that create data silos.

This is rational from their perspective:

- **IT/Security:** Every new silo = new risk, new compliance burden, new system to manage
- **HR/Admin:** "I already manage users in Workday. Now I manage them somewhere else too?"
- **Sponsors:** "How do I prove ROI if the data is trapped in your system?"

### We already lost a deal because of this: Sigma Alimentos

They chose not to go with ConsciousInsights because:

1. They were already building a chatbot inside **MS Teams using Microsoft's Copilot Agent framework** — simpler than us, but integrated into where they work
2. They wanted integration with the **Workday agent** — personalized development suggestions based on their Workday data (role, performance, career path)

Sigma chose a simpler solution that lived inside their existing ecosystem (Teams + Workday) over our more sophisticated coaching platform that would be "another app" and "another silo."

**The implication:** Integration isn't a feature request — it's table stakes for enterprise deals. If we can't say "we integrate with your identity, your HRMS, and your collaboration tools," we lose to inferior products that can.

---

## Why Clients Need "Integration"

**The core objection we hear:** "Users won't go to another app and will forget to use it."

But when we dig deeper (P&G example below), "integration" means specific things:

| They say | They actually need | Why |
| --- | --- | --- |
| "Integrate with our HRMS" | SSO + automated provisioning | Security policy — no manual user management |
| "Integrate with our HRMS" | Read HR data for personalization | Better coaching with context |
| "Integrate with our HRMS" | Write completion data back | Visibility for HR/sponsors |
| "Integrate with our LMS" | Embed chatbot, SSO from their system | Users don't leave their platform |
| "Integrate with Teams/Slack" | Notifications + presence in flow of work | Adoption — users forget standalone apps |

**Key insight:** Most "integration" requests are about **identity/access** (SSO, provisioning) and **presence in flow of work** (notifications, embeds). HR data sync is valuable but not the urgent blocker.

---

## P&G: What Actually Happened

Real example of what enterprise integration looks like.

### What P&G required:

| Requirement | Why | Status |
| --- | --- | --- |
| SSO via PingFederate | Security policy — P&G credentials only | ✅ Done — Daniel built custom middleware |
| OIDC claim mapping | Ping uses non-standard claims (`mail` not `email`) | ✅ Done — middleware translates |
| Access control via itAccess Group | Only approved users can access | ✅ P&G configures on their side |
| Auto user creation | Compliance — no manual Excel for users | ✅ Works — SSO auto-creates in Thinkific |
| Auto course enrollment | Users need correct cohort/courses | ❌ **Gap — currently manual Excel** |

### What we need to do NOW (urgent):

**Problem:** Users are auto-created via SSO, but course enrollment is still manual (Nelson uploads Excel).

**Solution:** Automate course assignment for first-time SSO users in Thinkific.

**Effort:** 6-8 hours (Daniel's estimate) — via Thinkific config or API.

**Action:** Daniel to implement. Test with Gabriel/Dor.

### What we learned:

1. Daniel had to build **custom SSO middleware** because Ping has non-standard OIDC claims
2. This is **client-specific work** that will repeat with every new enterprise IdP
3. We don't own identity — Thinkific does — so we're constrained by their limitations

---

## The Problem: We Don't Own Identity

**Current architecture:**

```
Enterprise IdP (Ping, Okta, etc.)
    ↓ custom middleware PER CLIENT
Thinkific (owns identity)
    ↓ iframe
ConsciousInsights chatbot

```

**What this means:**

- Every new client with a different IdP = custom middleware work
- Provisioning/enrollment tied to Thinkific's capabilities
- Adding channels (Teams, other LMS) = rethink auth each time
- We can't say "we integrate with Workday/Okta/etc." — we integrate with Thinkific, then hack around each client's IdP

---

## Strategic Decision: ConsciousInsights Owns Identity (Decided)

**Target architecture:**

```
Enterprise IdP (Ping, Okta, Azure AD, Workday, etc.)
    ↓ SSO + SCIM via WorkOS (one integration)
ConsciousInsights (owns identity)
    ↓ OAuth
    ├── CI Web App
    ├── Thinkific (OAuth connection already exists)
    ├── Teams Tab App
    └── Future LMS embeds

```

**What this unlocks:**

| Benefit | Why it matters |
| --- | --- |
| One integration via WorkOS | No more custom middleware per client |
| We control provisioning | User data, cohorts, journeys are ours to manage |
| Thinkific becomes a channel | Easier to swap, add other LMS, or go standalone |
| All future channels use same auth | Teams, Slack, LMS embeds — all OAuth to CI |
| We can actually say "we integrate" | WorkOS supports Workday, Okta, Azure AD, Ping, etc. |

**Note:** WorkOS can also integrate at a basic level with HRMS systems for directory sync — this could be a stepping stone before deeper HR data integration.

### Q1 POC Plan: WorkOS with Boetus (Decided Jan 27)

**Owner:** Daniel
**Playground:** Boetus.com (team's own Microsoft tenant — can experiment freely)

**POC scope:**
1. Configure WorkOS to handle Boetus.com authentication
2. Route users to either Thinkific or Conscious Insights based on role
3. Test provisioning flow

**Phase 2 (if POC succeeds):** Implement for Axialent internal use (staging), then real clients (production).

**Key technical notes from discussion:**
- WorkOS does NOT replace our Postgres user database — it handles the IdP translation layer
- Single URL limitation: need routing middleware to direct users to correct instance (pg.stoic, axialent.stoic, etc.)
- P&G went direct (custom middleware) because "all we needed was translation" — WorkOS remains the scalable path for multi-client

### Google Workspace (Exploratory, Not Committed)

Mercado Libre (potential client) uses only Google. Daniel has a paid Google Workspace account and can explore informally. First step would be SSO with Google Workspace before Google Meet integration. Not a sprint commitment — depends on whether Google-only clients materialize.

---

## HRMS Integration: Phased Approach

Beyond identity, there's value in deeper HRMS integration. But it's not all-or-nothing:

### Phase 1: SSO + Provisioning (URGENT — via WorkOS)

What it solves:

- Users authenticate with corporate credentials
- Users auto-provisioned/deprovisioned (no Excel)
- Basic org structure (who reports to whom)

This is the **urgent** piece. WorkOS handles this.

### Phase 2: Read HR Data for Context (FUTURE — via Merge.dev, n8n, or Personio POC)

**Near-term candidate:** Axialent uses Personio (smaller company HRMS). Could do an internal POC next quarter to build the "context pulling" abstraction layer using our own system before generalizing to client HRMS.

**HR data that could improve coaching:**

| Data | How it helps |
| --- | --- |
| Tenure | Coach new hire vs. 10-year veteran differently |
| Role/level | Tailor content for IC vs. manager vs. executive |
| Recent promotion | Surface "new manager" content automatically |
| Department/team | Context for team dynamics, cross-functional challenges |
| Performance review data | Personalized development focus areas |
| High-potential flags | Different coaching for succession candidates |
| Competency assessments | Target skill gaps |

**Key question:** Much of this could be collected in onboarding flows. The real value of HRMS reads is *not asking users things HR already knows*.

**Tool options:**

- **Merge.dev** — Unified API for 50+ HRMS (Workday, SuccessFactors, BambooHR, etc.). One integration, many systems. Has EU data residency (Stockholm).
- **n8n** — Workflow automation. Could build client-specific bridges faster. More flexible but less standardized.
- **Custom API work** — Direct integration with specific HRMS. Most control, most work per client.

Merge.dev and n8n aren't mutually exclusive — Merge.dev handles the *what* (unified HR data model), n8n could handle the *when/how* (orchestration, triggers).

### Phase 3: Write Back to HRMS (FUTURE — unclear value)

Potentially write back:

- Learning journey completion
- Coaching engagement metrics
- Assessment results
- Skill development progress

**Open questions:**

- Do HR teams actually want this in their HRMS, or just a dashboard they can access?
- What data does Stoic generate that's worth pushing back?
- Writing back is complex — often the real need is "give my HR team visibility" which could be a reporting portal rather than true integration.

---

## Other Integration Priorities

| Integration | What it does | Depends on |
| --- | --- | --- |
| Teams notifications | Reminders, nudges in flow of work | Mike's current work — no blocker |
| Teams tab app | Full CI experience in Teams | POC exists (Daniel). Needs: WorkOS for auth to work across clients |
| LMS embed (any client) | Chatbot in their LMS via iframe + SSO | WorkOS — then any LMS that supports OAuth |
| HR data reads | Context for personalization | Phase 2 — Merge.dev or n8n |

**Teams integration sequence:**

1. Notifications via chat (Mike, in progress) — creates the "pull" mechanism
2. Tab app (after notifications) — gives users somewhere to land; POC exists on Axialent
3. Bidirectional chat (future) — quick coaching interactions without leaving chat

---

## EU Data Residency

**Validated:** Aleatica (cautious client) was OK with EU hosting + SCCs + DPA.

| Layer | Solution | EU Residency |
| --- | --- | --- |
| SSO/Directory | WorkOS | Has EU option |
| HR Data (future) | Merge.dev | Stockholm EU environment |
| ConsciousInsights | Our infra | ✅ EU PostgreSQL |

**Note:** There's a distinction between where data is stored vs. legal jurisdiction (US companies subject to CLOUD Act even with EU hosting). For most clients, EU hosting + SCCs + DPA is sufficient. Most stringent clients (government, healthcare) may require EU-headquartered vendors.

---

## What We Still Need to Learn

**From sales/clients:**

- Which specific HRMS systems matter to which clients?
- What does "integration" actually mean to each client? (Need to probe deeper)
- Is there real demand for HR data personalization, or is provisioning enough?
- Do they want completion data written back, or just a dashboard?

**Validated so far:**

- Clients use Workday, SuccessFactors, Ping
- SSO + provisioning are **security requirements**, not convenience
- LMS integration = chatbot only (not our content) based on what we've heard

---

## Decisions Made (Jan 27, 2026)

| Decision | Details |
|----------|---------|
| CI owns identity via WorkOS | Committed. POC with Boetus first, then Axialent, then clients |
| Teams integration parallel track | Mike owns. Approaching production deployment |
| pip in production, UV for dev only | UV shared cache = security risk; isolated venvs per instance in prod |
| Docker optional for deployment | Keep as option for client-hosted; not required |
| Google Workspace exploration | Informal — Daniel can look into it, not a sprint commitment |
| Dashboard login deferred | No auth on admin panel yet; evaluate when needed |
| HRMS write (Phase 3) deferred | Wait for client demand |
| LMS embedding deferred | Per-platform work, no generic solution; wait for demand |

---

## Open Action Items

| Action | Owner | Status |
| --- | --- | --- |
| P&G course auto-enrollment fix | Daniel | 🔴 Urgent — unblocks P&G |
| Finish installation script (parameterized) | Daniel | 🟡 In progress |
| WorkOS SSO POC with Boetus | Daniel | 🟡 Q1 — after installation script |
| Teams production deployment | Mike | 🟡 Needs Azure setup + Axialent admin access (request from Mario) |
| Explore Merge.dev / n8n for HR data reads | Team | 🟢 Future — after identity solved |
| Probe deeper on "integration" per client opportunity | Sales/Oseas | 🟡 Ongoing |