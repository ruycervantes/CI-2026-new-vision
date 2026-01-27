# OKRs Review & Strategy Session Summary
**Date:** January 20, 2026
**Participants:** Ruy (PM/CTO), Leo (Sales/PMF)
**Duration:** ~45 minutes

---

## Executive Summary

Ruy and Leo aligned on Ruy's Q1 OKRs structure (3 objectives: Feature Development, Product Decision/PMF, Team Performance/Process). They discussed LMS integration strategy for partners, pricing/setup fee review needs with Nelson, and established a weekly PMF review cadence. The conversation surfaced that the "High Performance Team" direction remains undefined and needs exploration alongside the existing Behavior Change vision.

---

## 1. Q1 OKRs Structure

**Status:** Draft complete, needs refinement

**Three objectives defined:**

1. **Feature Development** - Deliver 3-4 key features
   - Microsoft Teams integration (in production)
   - New coaching version (more complete sessions, not just profiles)
   - Voice/Speech-to-text capabilities
   - Automation (environment generation + prompt customization)

2. **Product Decision + PMF Process** - Two key results:
   - Validated vision/roadmap decided
   - Running PMF process with weekly cadence

3. **Team Performance & Process Improvement**
   - Better development processes
   - Release lifecycle improvements
   - Team growth

**Action items:**
- [ ] Ruy: Finalize and send OKRs to Leo and Oseas today

---

## 2. LMS Integration Strategy (Partner Opportunity)

**Status:** Frequently requested, not yet prioritized

**Context:** Leo hearing from 4-5 partners that they want AI coaches integrated into their existing LMS (not Thinkific)

**Technical approach options:**

| Option | Pros | Cons | Cost |
|--------|------|------|------|
| **Per-LMS connector** | Custom, optimized | Dev effort per client | Variable |
| **WorkOS** | Universal SSO, enterprise-ready | Per-connection fee | $125/month per connection |

**Key technical requirements:**
- iFrame support in target LMS
- Single Sign-On (SSO) - critical for user tracking and security
- Rate limiting (security without SSO is risky)

**Decision:** Not Q1 priority until a committed client materializes. Have clarity on *how* to execute when needed.

**Leo's request:** Enable sales team to offer LMS integration as an option

---

## 3. Setup Fee / Pricing Review

**Status:** Needs urgent review

**Concern:** Nelson's pricing model may not account for:
- Mike's time for environment setup
- Ruy's time for prompt customization
- Thinkific costs
- Realistic effort estimates

**Current:** $4,000 per coach for setup (customization)

**Action items:**
- [ ] Schedule meeting with Nelson tomorrow (Leo to propose)
- [ ] Review if setup fee covers actual costs

---

## 4. Automation as Q1 Priority

**Status:** Added to feature list

**Problems to solve:**
- Mike spends ~half day per client on environment setup (bottleneck)
- Ruy becomes bottleneck on prompt customization for new coaches
- Past experience: Duke, Credit Corp projects had delays due to this

**Resolution:** Add "Sprint Automation" as 4th feature candidate

---

## 5. PMF Process & Weekly Cadence

**Status:** Agreed to implement

**What was discussed:**
- Need shared accountability for PMF validation
- Can't just be Ruy alone (didn't happen in 2024)
- Include commercial conversations and user experiments

**Structure agreed:**
- Weekly 30-min review (Thursday/Friday)
- Participants: Ruy, Leo (possibly Oseas, Rodrigo)
- Review: customer meetings, experiments, learnings

**Leo's commitment:** Find a weekly slot and propose meeting

---

## 6. High Performance Team vs Behavior Change Direction

**Status:** Needs parallel exploration

**Context:**
- Behavior Change direction is well-defined
- High Performance Team is "an idea, not a concept yet"
- Oseas meeting (yesterday) surfaced need to explore both
- Market feedback: investors and clients interested in team performance

**Concern:** HPT gets "yes" responses because it's vague ("Do you want a magic wand?")

**Next steps:**
- Ruy: Reconnect with previous exploration (Mural, dispersed notes)
- Leo: Independently brainstorm what's viable as a first step
- Both: Present ideas at Dolo meeting tomorrow

---

## 7. AI Coach in Teams Access

**Status:** Not available for general use

**Context:** Leo wanted to try the Teams AI Coach himself

**Reality:**
- Oseas has an old hardcoded version
- Proper setup requires environment configuration
- This is part of the automation problem

**Resolution:** Part of OKR work to make this deployable

---

## 8. Notion Organization

**Status:** "Un gallinero" (a mess)

**Problems:**
- 18 months of unorganized additions
- OKR dashboard exists but unusable
- Leo can't navigate it

**Decision:**
- Create new Notion workspace "Stoic New"
- Leo gets admin access to organize
- Migrate relevant content from old workspace
- Use for OKRs, processes, PMF tracking

**Action items:**
- [x] Ruy: Created new workspace and added Leo as admin

---

## Key Decisions Made

| Decision | Details |
|----------|---------|
| OKR structure | 3 objectives: Features, Product/PMF, Team Performance |
| PMF process | Weekly review meeting (Thu/Fri) |
| LMS integration | Ready to execute when client commits, not Q1 priority |
| Automation | Added as potential 4th feature for Q1 |
| Notion | New workspace created, Leo to organize |

---

## Blockers Identified

| Blocker | Owner | Resolution |
|---------|-------|------------|
| Pricing model unclear | Nelson | Meeting tomorrow |
| HPT direction undefined | Ruy | Explore Mural/notes, present at Dolo meeting |
| Teams AI Coach not deployable | Mike/Ruy | Part of automation OKR |

---

## Next Steps

1. **Today:** Ruy sends OKRs to Leo and Oseas via email
2. **Tomorrow:** Meeting with Nelson on pricing/setup fees
3. **Tomorrow:** Dolo meeting - bring HPT exploration
4. **This week:** Leo proposes weekly PMF review slot
5. **Ongoing:** Leo organizes new Notion workspace
