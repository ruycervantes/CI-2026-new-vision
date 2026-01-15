# Sprint Planning Call Summary
**Date:** January 15, 2026
**Participants:** Ruy (PM/CTO), Mike (Dev Lead), Daniel (Infra), Leo (Sales/Testing)
**Absent:** Shamil (Coach features)

---

## Executive Summary

Sprint planning focused on three main areas: (1) infrastructure automation for client deployments, (2) Microsoft Teams integration as the Q1 priority, and (3) establishing a proper testing process. Major discussion on switching project management tools from Asana to Linear or GitHub Projects. Leo joins testing efforts to formalize the path from development → demo.

---

## 1. P&G (Procter & Gamble) SSO Integration

**Status:** In progress, clarification sent via email the night before.

**Current State:**
- P&G uses Ping for SSO authentication
- CI built a middleware to translate between Ping's format and Thinkific's OpenID standard
- Current onboarding depends on Excel file with user list for batch enrollment

**What Needs to Change:**
- Automate course assignment in Thinkific as users connect (instead of batch Excel uploads)
- No middleware changes required - P&G handles filtering on their side
- Need to talk to Nelson about timeline

**WorkOS Discussion:**
- Could standardize SSO integrations across all clients through WorkOS
- Would eliminate per-client middleware implementations
- Thinkific support feedback: "many limitations found, have discussed needing another solution"

---

## 2. Thinkific Platform Limitations

**Pain Points Identified:**
- Very specific course structure, not flexible
- Multiple clicks to access chat activity (should be 1 click)
- Nelson has built hacks to improve UX but still suboptimal
- Not suitable if CI wants to be a standalone product beyond "chatbot inside a course"

**Decision:** Not critical now, but revisit if sales traction increases and clients want more than just a course.

---

## 3. Daniel's Infrastructure Sprint Tasks

### 3.1 Infra Checklist (Carried Over)
- **Status:** Only started, blocked by other project demands
- **Action:** Complete this sprint

### 3.2 Deployment Script (Main Task)
**Goal:** Automate client environment creation (currently 15-20 manual steps)

**Requirements:**
- Create client-specific environments from any git branch
- Support Docker containers + plain installation
- Generate separate database per client instance
- Create: Main App + Admin App (Analytics separate, not in scope yet)
- Documentation on how to use the script

**Naming Convention:**
- Use same client name throughout the chain (subdomain = DB name = everything)
- Example: `clientname.stoicq.com` → DB: `clientname`

**Estimate:** ~12 hours → 3 story points (using IBM sizing table Mike shared)

---

## 4. Security Warning: Bank Names in URLs (from Leo)

**Critical Lesson Learned:**
> "We used a bank name in a subdomain URL with a login page. AWS detected it as potential phishing and banned our entire application - ALL clients went down. Took days to diagnose."

**Recommendations:**
1. For bank clients: Use abbreviations (e.g., "nb" instead of "nubank")
2. Or: Route everything through `app.stoicq.com` using WorkOS authentication
3. Bank subdomains under official bank root domain are OK, but banks rarely allow this
4. Document this warning for future reference

**B2B Mitigation:** Less risk since URLs aren't indexed by Google (confirmed with site: search)

---

## 5. Technical Housekeeping

### robots.txt & AI Crawler Blocking
- **Status:** Not implemented
- **Confirmed:** Google only indexes main Stoic website
- **Action Items:**
  - Implement robots.txt to prevent indexing
  - Block AI search engine crawlers (different protocol from robots.txt)

### SSL Certificates
- Using Certigo wildcard certificates
- Two certificates covering all first-level subdomains

---

## 6. Project Management Tool Migration

**Problem Statement:**
Asana isn't working for sprint management:
- No native epics support
- Can't plan sprints effectively
- Testing board separate from development board
- Ruy is "the glue" of the process - not scalable
- No capacity metrics
- Can't track which product/client each issue contributes to
- Issue documentation lacks templates

**Options Evaluated:**

| Tool | Pros | Cons |
|------|------|------|
| **Linear** | New/modern, great MCP integration, designed for dev teams | Learning curve, migration |
| **GitHub Projects** | Free, integrated with code, has Kanban/roadmap/epics, CI/CD automation | Non-dev team may resist |
| **Notion** | Already using, Nelson uses it | Not designed for sprints |

**Key Features Needed:**
- Epics support
- Issue templates
- Capacity tracking
- Product/client tagging
- MCP integration with Claude Code (huge productivity boost)

**Decision:**
- Ruy will evaluate both Linear and GitHub Projects this sprint
- Share findings via email
- Discuss in office hours before deciding
- Migration: Start fresh for 2026, only migrate active backlog (use Asana MCP to extract)

---

## 7. Mike's Sprint Tasks

### 7.1 Admin Panel Workflow (Carry-over)
**Completed:**
- Regenerate debriefs from admin (adjust prompts live)
- Visual indicators for users with/without assessments

**Remaining:**
- Manual "pull assessment" button for missing assessments
- **Estimate:** 1 day max

### 7.2 Claude Code Skill for Reflex Development
- Created comprehensive skill in `cloud-config` repo
- Emphasis on UI development (helps Shamil)
- **Status:** Ready for testing
- **Next:** Test if it can duplicate dashboards from screenshots

### 7.3 Microsoft Teams Integration (Main Focus)
**Goal:** Send notifications via Teams

**MVP Scope:**
- Match user email (CI app ↔ Teams)
- Request notification permission once
- Send notifications via Teams

**Technical Details:**
- Already have App ID and keys connected to Teams
- Consent flow required (like camera permission on mobile)
- Considering checkbox in Chainlit sidebar: "Send me Teams notifications"
- May work without app installation if CI app acts as a Teams "user"

**Blockers:**
- Needs Teams admin permissions from IT (Javier)
- Daniel was blocked 5-6 days waiting for access previously

**Estimate:** 3-4 days MVP, full sprint to be safe

**Action:** Ruy to follow up with IT to expedite Mike's admin access

---

## 8. Testing Process Formalization

**New Workflow (Naming simplified for non-devs):**
```
Development → Testing → Demo → Production
             (testing.stoicq.com)  (demo.stoicq.com)
```

**Note:** GitHub branch still called "staging" but will rename later

**Testing Environment:**
- Domain: `testing.stoicq.com`
- When Mike marks something "Review" → it's deployed to testing
- Leo assigned to test before promotion to Demo

**Demo Environment:**
- Almost production quality
- Used for client demonstrations
- **New Rule:** Notify dev team 3+ days before any demo for QA tour

**Leo's First Testing Task:**
- Assigned: "Testing de mapro" in Asana
- Need to test: Leadership Growth Partner features
- Ruy will add more detail to the task

**Client Instance Lifecycle:**
- Problem: No visibility into which client instances are active
- Need: Process to archive/deactivate unused instances (save resources)
- Action: Document lifecycle process (especially with Nelson leaving, Octavio joining)

---

## 9. Bugs in Review/Testing

| Bug | Status | Notes |
|-----|--------|-------|
| Next step hallucination | Ready for testing | If user asks to skip step, AI explains what's missing first |
| RAG improvements | Ready for testing | Needs more testing |
| 2-3 other boxes | In review for Mike | |

---

## 10. Story Points Adoption

Shared sizing table from Mike's IBM project:
- Using standard 1, 2, 3, 5, 8, 13 scale
- Team to start using consistently
- Helps estimate capacity and velocity

---

## 11. Oseas Meeting Debrief

**Context:** Leo was in a long meeting with Oseas about product direction.

**What Oseas Wants:**
- Users do assessment → identify growth areas → create micro-habits
- Bring problems to AI → get coaching → break into micro-habits

**Current Reality:**
- Can do: One micro-habit from assessment
- Cannot do (yet): Full coaching flow with problem → micro-habit breakdown

**Decision:**
- Not possible right now, requires new version
- Q1 focus: Working toward this coaching capability
- First: Stabilize Leadership Growth Partner, get to Demo, gather feedback

---

## 12. Daily Stand-ups

- Will be via Teams messages (not calls)
- Asana form being circulated
- Concern: Many processes being set up simultaneously - need alignment

---

## 13. Roadmap & OKRs

**Status:** Ruy creating roadmap document with Q1 emphasis
**Next Step:** Share for team discussion → becomes team OKR

---

## Key Decisions Made

1. **Naming:** Use "testing" instead of "staging" for non-dev communication
2. **Tool Migration:** Evaluate Linear and GitHub Projects before deciding
3. **Testing Process:** Leo joins QA, 3-day notice before client demos
4. **Teams Integration:** Full sprint commitment, request admin access ASAP
5. **Deployment Script:** Priority for Daniel, 3 story points
6. **Bank URLs:** Document warning, use abbreviations for financial clients

---

## Blockers Identified

| Blocker | Owner | Resolution |
|---------|-------|------------|
| Mike needs Teams admin access | Ruy → IT (Javier) | Follow up immediately |
| P&G course automation | Nelson | Schedule discussion |
| Asana not supporting dev workflow | Ruy | Evaluate alternatives this sprint |
| No client lifecycle visibility | Team | Document process |

---

## Next Steps

1. **Immediate:** Ruy follow up with IT for Mike's admin permissions
2. **This Week:** Ruy adds detail to Leo's testing task, Leo begins testing
3. **Sprint:** Daniel completes deployment script, Mike delivers Teams MVP
4. **End of Sprint:** Ruy shares tool comparison (Linear vs GitHub)
5. **Before Q1 End:** Stabilize Leadership Growth Partner to Demo quality
