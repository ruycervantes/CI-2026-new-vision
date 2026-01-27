# Daniel 1:1 Summary - P&G Integration & WorkOS
**Date:** January 21, 2026
**Participants:** Ruy (PM/CTO), Daniel (Dev - Infrastructure)
**Type:** 1:1 Catch-up

---

## Executive Summary

Ruy and Daniel discussed four key areas: Daniel's upcoming paternity leave (baby due ~Feb 16), P&G SSO integration clarification, Thinkific auto-provisioning needs, and future WorkOS authentication strategy. The call clarified that P&G's Ping Federate SSO requires no middleware changes for group filtering (they control access), but Thinkific user provisioning will need automation. A broader strategic direction emerged around using WorkOS to own the authentication layer and potentially an "orchestrator" middleware for user provisioning across platforms.

---

## 1. Daniel's Paternity Leave Planning
**Status:** Baby due Feb 16 (may change at tomorrow's doctor visit)
**What was discussed:**
- Daniel's baby is expected around Feb 16, though the official 40-week date is March 4
- Tomorrow's gynecologist appointment may adjust the timeline
- Ruy asked Daniel to prepare a simple handoff plan so Mike and Shamil know what they need to know
- All server access is already shared via OnePassword (Stoic Boetus root user)
- P&G solution documentation is the main gap - needs to be documented before leave

**Decisions made:**
- Daniel will send team notification about expected dates (after Friday's doctor update)
- Daniel will document the P&G solution architecture

**Action items:**
- Daniel: Document P&G solution (where in AWS, which scripts, etc.)
- Daniel: Send team notification about paternity leave dates (Friday after doctor visit)
- Daniel: Check if any access/knowledge gaps exist beyond P&G

---

## 2. Contract Renewal
**Status:** Pending (Ruy's task)
**What was discussed:**
- Ruy acknowledged he owes Daniel the contract renewal
- Has been slipping but is on his list
- Will continue same terms

**Action items:**
- Ruy: Complete Daniel's contract extension

---

## 3. P&G SSO Integration Response
**Status:** Needs response to Gabriel today
**What was discussed:**
- Gabriel from P&G asked for time estimate on user synchronization/filtering
- Daniel analyzed Gabriel's diagram and Mojica's payload samples
- P&G uses Ping Federate with group-based access control on their end
- Key insight: **P&G controls group membership externally** - only authorized users will reach Stoic's middleware
- No group information is included in the Ping payload (likely intentional for security)
- Therefore, **no middleware changes needed** for user filtering - P&G handles it

**Technical details:**
- P&G manages access like Microsoft 365 ("Daniel can have Word but not Excel")
- Only users with Stoic permission in their AD group will authenticate
- Gabriel's concern may be about preventing unauthorized license costs
- For double-validation, P&G would need to send group data (which they don't)

**Decisions made:**
- Split response: Daniel handles Ping/middleware part, Ruy handles Thinkific/business part
- Response to Gabriel: Middleware requires no changes for group-based filtering
- Program doesn't start until May anyway - low urgency

**Action items:**
- Daniel: Reply to Gabriel with technical explanation of Ping/middleware (no work needed)
- Ruy: Reply (on Daniel's email) about Thinkific provisioning and business context

---

## 4. Thinkific User Provisioning
**Status:** Needs automation for P&G (but not urgent)
**What was discussed:**
- Current process: Nelson manually uploads users via CSV/Excel, assigns courses and groups
- P&G flow will be different: users authenticate and need automatic Thinkific account creation + course assignment
- This IS something that needs development
- Could be done in middleware (Daniel has admin API key) or via Nelson's automation
- However, P&G program is hybrid (digital + in-person), so they'll need to send Excel anyway for the in-person component
- May not need full SCIM provisioning if Excel upload continues

**Decisions made:**
- Clarify with Gabriel if auto-provisioning is actually needed given hybrid program structure
- Not urgent for now - can be developed later if needed

**Action items:**
- Ruy: Ask Gabriel in response if auto-provisioning is truly needed (given hybrid format)

---

## 5. WorkOS / SSO Strategy Discussion
**Status:** Strategic planning (longer term)
**What was discussed:**
- Ruy shared that multiple enterprise prospects are asking about SSO and HRIS integration
- Questions include: "Does this integrate with my Teams? My HR system? My data?"
- Discussed two layers of integration:
  1. **Authentication/SSO** - own the auth layer (WorkOS can help)
  2. **HRIS integration** - Workday, SuccessFactors, BambooHR, etc. (deeper integration)

**WorkOS benefits:**
- Can handle SSO from any IdP (Ping, Okta, Azure AD, etc.)
- Directory sync / SCIM provisioning built-in
- Stoic would own the auth layer instead of relying on each platform

**Orchestrator concept:**
- Need middleware that says "this user has X role, provision them in Y systems"
- WorkOS handles client-facing auth, orchestrator handles internal provisioning
- Required because even with WorkOS, each destination (Thinkific, Conscious Insights, dashboard) needs provisioning logic

**HRIS layer:**
- Workday and SuccessFactors are the big two
- Could pull user profiles, team structures, required skills
- Enables personalized prompts based on user's actual role/context
- But this is "phase 2 or 3" - auth layer comes first

**Real-world motivation:**
- Lost Sigma Alimentos because they're building internal Copilot chatbot + waiting for SAP SuccessFactors chatbot
- Need to be able to say "we integrate faster than they build internally"

**Decisions made:**
- Daniel to think about WorkOS POC scope and effort estimate
- Need a sandbox environment to test integrations properly

**Action items:**
- Daniel: Read Ruy's document on SSO/integration strategy (to be sent)
- Daniel: Think through POC scope and estimate for WorkOS integration
- Daniel: Request Microsoft 365/Teams sandbox environment (via email to Ruy → Mario)

---

## 6. Microsoft Teams Sandbox Environment
**Status:** Blocker for both Teams integration and WorkOS POC
**What was discussed:**
- Microsoft no longer provides developer sandboxes easily
- Mike is also blocked by this for Teams integration work
- Options explored:
  1. Stoic Enterprises - has Microsoft accounts but unclear if full admin access or subgroup of Accelent
  2. Boetus - could purchase 3-4 licenses (~$50-80/month)
- If Stoic Enterprises is a separate instance with full admin → use it
- If it's a subgroup of Accelent → politics/approvals involved
- Escalation path: Mario (via well-written request)

**Decisions made:**
- Daniel to write a request for sandbox/test environment
- Ruy will escalate to Mario or just buy Boetus licenses if needed

**Action items:**
- Daniel: Write email requesting Microsoft sandbox (what's needed, why)
- Ruy: Escalate to Mario or purchase Boetus licenses

---

## 7. Teams Tab App / OAuth Proof of Concept
**Status:** Completed POC, needs validation in different instance
**What was discussed:**
- Daniel built a Conscious Insights Tab App for Teams with OAuth
- Currently works in one instance
- Needs to validate it works in other Microsoft instances
- Also useful for documenting the real sysadmin installation process

**Action items:**
- Daniel: Validate Teams Tab App in another Microsoft instance (once sandbox available)
- Daniel: Document the sysadmin installation process

---

## Key Decisions Made

| Decision | Details |
|----------|---------|
| P&G middleware needs no changes | Group filtering handled by Ping Federate on P&G side |
| Split response to Gabriel | Daniel: technical (Ping), Ruy: business (Thinkific) |
| Thinkific auto-provisioning not urgent | May not be needed given hybrid program format |
| WorkOS POC worth exploring | Daniel to read strategy doc and estimate effort |
| Need Microsoft sandbox | Either Stoic Enterprises or buy Boetus licenses |

---

## Blockers Identified

| Blocker | Owner | Resolution |
|---------|-------|------------|
| No Microsoft sandbox for testing | Daniel/Mike | Request via Mario or buy Boetus licenses |
| Daniel's paternity leave (mid-Feb) | Team | Document P&G solution, ensure handoff |
| Unclear if Stoic Enterprises has admin access | Ruy | Check with Mario |

---

## Next Steps

1. **Daniel** - Reply to Gabriel with Ping/middleware technical explanation (today)
2. **Ruy** - Reply on Daniel's email with Thinkific/business context (today)
3. **Daniel** - Document P&G solution before leave (this week)
4. **Daniel** - Send team notification about paternity leave dates (Friday)
5. **Daniel** - Write sandbox request email for Mario
6. **Daniel** - Read WorkOS strategy document when Ruy sends it
7. **Ruy** - Send WorkOS/SSO integration strategy document to Daniel
8. **Ruy** - Complete Daniel's contract extension
