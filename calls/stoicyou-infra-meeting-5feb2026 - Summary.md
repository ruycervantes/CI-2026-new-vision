# StoicYou.com Infrastructure & Email Meeting Summary
**Date:** February 5, 2026
**Participants:** Ruy (PM/CTO, Stoic), Mario (IT liaison, TecnoBrain), Jorge (TecnoBrain, replacing Javier), Oriana (TecnoBrain, covering for Javier)
**Absent:** Jonathan (Stoic, referenced extensively), Nelson Granja (referenced), Daniel Alvarado (referenced), Javier (TecnoBrain, on vacation)

---

## Executive Summary

Infrastructure meeting to resolve long-standing email and domain issues across Stoic's two domains (stoicyou.com and stoicenterprises.com), and to request a new isolated Microsoft test environment for Teams integration development. The email issues — particularly info@stoicyou.com — have been unresolved since January 14 and are blocking business operations.

---

## 1. StoicYou.com Email Issues (URGENT)
**Status:** Broken since mid-January. Jonathan has been requesting email setup (info@stoicyou.com, contact group) for 3+ weeks with no resolution.
**What was discussed:**
- Emails configured to resolve via Microsoft 365, but accounts were created in SiteGround hosting — mismatch causes delivery failure
- DNS (managed by Daniel via Vultr) points email MX records to Microsoft, but mailboxes live in SiteGround
- Sam (India-based contractor working with Jonathan) attempted to create mailboxes in SiteGround but they don't work because DNS routes to Microsoft
- Jorge confirmed: "contact" is a group supposed to deliver to 4 people — nothing arrives because of the hosting/DNS mismatch
- info@stoicyou.com is also non-functional

**Decisions made:**
- Ruy proposed moving stoicyou.com email to Microsoft 365 instead of SiteGround to resolve the mismatch cleanly
- If only 2 mailboxes needed (contact, info), migration is simple
- If more mailboxes exist, need cost/complexity analysis first

**Action items:**
- Jorge to clarify with Jonathan the full list of email accounts needed
- Resolve info@stoicyou.com and contact group as top priority
- Ruy to send recap email with all requests documented

---

## 2. StoicYou.com DNS & Hosting Architecture
**Status:** Fragmented ownership causing confusion
**What was discussed:**
- **DNS:** Managed via Vultr by Daniel Alvarado (and Mike as backup). Changes can be made in hours.
- **Web hosting:** SiteGround, managed by Sam (Jonathan's contact in India)
- **Email:** Currently split — some attempts in SiteGround, MX records pointing to Microsoft
- DNS and hosting are separate systems, which TecnoBrain didn't fully understand

**Key clarification by Ruy:**
- DNS is just a routing table: subdomain → service (Microsoft, SiteGround, Vultr, etc.)
- Daniel/Mike can update DNS quickly when needed
- The web hosting (SiteGround) and DNS (Vultr) are independent systems

---

## 3. StoicEnterprises.com → StoicYou.com Migration (IMPORTANT, NOT URGENT)
**Status:** Needed but deferred — two domains running in parallel creates confusion
**What was discussed:**
- StoicEnterprises.com has ~4 active Microsoft 365 licenses
- Known active mailboxes: help@stoicenterprises.com (Nelson Granja manages, tied to Thinkific), ruy@stoicenterprises.com (not in use)
- help@stoicenterprises.com cannot be removed until Nelson transitions it
- Goal: eventually consolidate everything under stoicyou.com

**Decisions made:**
- Step 1: Get inventory of all active StoicEnterprises accounts (Oriana to provide)
- Step 2: Coordinate with Nelson on help@ transition plan
- Migration is Phase 2 — not urgent but important

**Action items:**
- Oriana to share full list of StoicEnterprises email accounts
- Ruy/Mario to coordinate with Nelson Granja on help@ transition
- Create migration plan once inventory is complete

---

## 4. StraussComps.com Issue (NOT OURS)
**Status:** Clarified as not a Stoic domain — Jonathan needs to explain
**What was discussed:**
- Jorge raised a blocked mailbox at joel@strausscomps.com
- Neither Ruy nor Mario recognize this domain
- Ruy identified it as possibly a PR agency (Strategic Communications for Tech Innovation)
- Mario confirmed Benjamin has no knowledge of it either

**Decision:** Ask Jonathan to clarify what StraussComps.com is and what he needs

---

## 5. New Microsoft Test Environment for Teams Integration (SEPARATE REQUEST)
**Status:** New request — needs pricing and setup
**What was discussed:**
- Dev team needs isolated Microsoft 365 environment for Teams app integration testing
- Current approach (using Axialent's environment with limited access) is too slow — tickets pile up, can't move fast
- Test domain: **boetus.com** (existing Stoic test domain)
- Need: 2 basic licenses, test accounts (test1@boetus.com, test2@boetus.com)
- Developers (Daniel, Mike) need full admin access
- Must be a **completely separate tenant** — security isolation from production (Ruy cited risk of test misconfigurations exposing production)
- Microsoft removed sandbox environments; local dev tools are insufficient for Teams integration testing

**Decisions made:**
- Create new tenant under Stoic, registered in Spain (same as Axialent Global)
- Jorge to research pricing: ~$12.50/mo annual vs ~$15/mo monthly (M365 Business Standard)
- TecnoBrain admin access via .onmicrosoft.com internal account (no extra license needed)
- Validate with Agustin Carrizo which entity/card to use for billing
- Likely charged to Stoic (development expense, Spain address)

**Action items:**
- Jorge to provide pricing comparison (monthly vs annual)
- Ruy to send detailed email request
- Validate billing entity with Agustin Carrizo
- TecnoBrain to set up new tenant once approved

---

## 6. Communication & Process Issues
**Status:** Systemic problem surfaced
**What was discussed:**
- Gabriel left TecnoBrain ~2 months ago; Javier replaced him but is on vacation
- Knowledge transfer gaps between Gabriel → Javier → Jorge
- Jonathan's email requests languishing since January 14 — communication not flowing
- Multiple parties managing different pieces (DNS: Daniel, hosting: Sam, Microsoft: TecnoBrain) without clear ownership map
- Ruy acknowledged being "part of the problem" in not executing the domain transition

---

## 7. Legal/Compliance Thread (Briefly Mentioned)
**Status:** Paused but needs revival
**What was discussed:**
- P&G compliance/security questionnaire just arrived — Ruy already prepared it (similar to Telus)
- Needs TecnoBrain to confirm general data, policies, etc.
- Separate from the domain/email issues
- Lawyers (Montier) engagement on EU AI Act policies was left incomplete
- Ruy had sent something to them but never followed up; they never responded

---

## Key Decisions Made

| Decision | Details |
|----------|---------|
| Move stoicyou.com email to Microsoft 365 | Cleaner than fixing SiteGround/DNS mismatch |
| New tenant for test environment | Completely isolated from production for security |
| Test domain: boetus.com | Existing Stoic test domain |
| StraussComps.com is not ours | Jonathan to clarify |
| StoicEnterprises → StoicYou migration is Phase 2 | Inventory first, then plan |

---

## Blockers Identified

| Blocker | Owner | Resolution |
|---------|-------|------------|
| info@stoicyou.com broken since Jan 14 | Jorge/TecnoBrain | Clarify full email list with Jonathan, then set up in Microsoft |
| Javier (primary IT knowledge) on vacation | TecnoBrain | Jorge + Oriana covering; Javier back in ~2 weeks |
| Gabriel left TecnoBrain — knowledge gaps | Mario | Jorge/Oriana ramping up |
| Nelson must be involved in help@ transition | Ruy/Mario | Coordinate separately |
| Agustin Carrizo approval for test env billing | Mario | Pending pricing info from Jorge |

---

## Next Steps

1. **Ruy** sends recap email to all parties with structured requests
2. **Jorge** clarifies full email account list with Jonathan
3. **Jorge** provides Microsoft 365 pricing for test environment
4. **Oriana** shares inventory of StoicEnterprises email accounts
5. **Mario** validates test environment billing with Agustin Carrizo
6. **Ruy** shares P&G compliance questionnaire with Mario for TecnoBrain input
7. Resolution of info@stoicyou.com and contact group as top priority
