# Sprint Demo Summary
**Date:** January 28, 2026
**Participants:** Ruy (PM/CTO), Mike (Dev Lead), Shamil (Dev), Daniel (absent most of call)
**Type:** Sprint demo / feature review

---

## Executive Summary

Shamil demoed the new Thinking Partner sidebar with progressive information extraction (challenge, goal, gap, key insights, commitment). Mike demoed the VLAN assessment admin dashboard and discussed multiple bug fixes and feature requests from Nelson. Key technical discussions around sidebar UX improvements and date handling reliability in calendar features.

---

## 1. Thinking Partner Sidebar (Shamil)

**Status:** Working, needs UX refinements

**What was demoed:**
- New panel that extracts and displays challenge, goal, gap, key insights (up to 5), and my commitment
- Updates progressively every ~3 messages
- Information persists when switching bots (e.g., to Player Mindset, Difficult Conversations)
- Copy summary button copies the entire sidebar content

**Issues identified:**
- UI flickering/rendering issues (caching problem with LangChain)
- Information appears too early and changes frequently, causing confusion
- Too much information displayed at once ("wall of text")
- Fields show empty before content is ready

**Decisions made:**
- **Progressive display:** Show only "My Challenge" initially, then reveal fields progressively as they're filled
- **Highlight commitment:** Make "My Commitment" more visually prominent (white background or different style)
- **Improve extraction timing:** Add conditional logic to prompts ("Only if you think a goal has been clearly defined, extract the goal")

**Prompt improvements discussed:**
- Add "IF" conditions to extraction prompts in `profiles.toml`
- Use XML-style prompting: `<critical>Only if gap has been identified...</critical>`
- Considered structured JSON output but rejected due to token streaming requirement

---

## 2. Bot Switching Behavior

**What was discussed:**
- Current bots it can switch to: Player Mindset, Difficult Conversations, Commitments
- Bots without sidebar (like Leadership Growth) would need different handling
- Question about what happens when switching to Leadership Growth Partner

**Future consideration:**
- Need to rethink for multiple coaching sessions running simultaneously
- Approach field currently just shows bot name (e.g., "Player Mindset") - possibly redundant with header

---

## 3. VLAN Assessment Admin (Mike)

**Status:** Complete, production-ready

**What was demoed:**
- New dashboard card showing:
  - CronScript status confirmation (running)
  - Last run info and current settings
  - Manual fetch capability (go back in time)
  - Assessment list with email, type, date
  - Search functionality
  - Detection of users without accounts (CDs icon)
  - Ability to create user accounts directly (pre-fills email)
- Profiles list improvements:
  - Now alphabetically sorted
  - Defaults appear at beginning
- "Stoic" branding: Bot now identifies as "I am Stoic, your leadership coach" (Jonathan's request)

---

## 4. Bug Fixes and Tickets (Mike)

**Resolved/discussed items:**

| Ticket | Status | Notes |
|--------|--------|-------|
| Bot identifies as Stoic | Done | Changed from "Conscious Insights" |
| Privacy policy link | Needs discussion | Ruy has draft ready; needs to add to ticket |
| Remove "new chat" confirmation step | Won't do | Chainlit default, would be hacky; good to have for long discussions |
| "Continue with ThinkIFIC" → "Continue with Axialent" | Deferred | Requires renaming in auth code everywhere; suggest "Axialent LMS" or "learnaxialent.com" |
| Tutorial wizard (onboarding) | Deferred | Needs standalone UX decision first; library available (`driver.js`-style) |
| Language settings for users | Under discussion | See Language section below |

---

## 5. Language Settings & Assessment Mismatch

**Problem:**
- Leo did assessment in Spanish, connected to CI in English, saw Spanish results
- Users who do assessments in one language but use app in another get mismatched content

**Current behavior:**
- If user has assessments in both languages, fetches based on current app language
- If user only has one language, shows that regardless of app language

**Discussion:**
- Multi-language support creates complexity:
  - Memory storage in different languages
  - Assessment availability must match
  - User confusion

**Tentative decision:**
- Default to single language (set at provisioning)
- Remove language selector from normal user UI (keep for admins/testing)
- If no matching assessment, show message: "You don't have an English assessment, please go do it"
- Ruy to send note to team about language policy

---

## 6. Date Handling Issues (Mike)

**Problem:**
- LLM unreliable for date calculations (~90% accuracy, but 10% failures noticeable)
- Says "Friday 31st" when 31st is actually Saturday
- Year changes cause issues (December → January)
- Timezone-dependent calculations

**Current workaround:**
- Passing next 30 days of dates explicitly in prompt
- Calendar scheduling itself works fine; issue is in text responses

**Proposed solution:**
- Use Python datetime library as a tool
- LLM calls date calculation tool instead of guessing
- Chainlit now has native date picker (previously unavailable) - but conflicts with "full text" approach

**Status:** Not urgent, but needs a ticket

---

## 7. Asana / Project Management Discussion

**Pain points raised:**
- No sprint view / backlog management
- Testing vs Development boards separated
- No epic support
- No capacity metrics
- Can't easily see submission dates on feedback
- No email notifications for new feedback forms
- Workflows feature exists but not sprint-focused

**Proposed solution:**
- Ruy to test Linear next sprint
- Linear has: sprint templates, epics, user stories → tasks flow, better dev focus
- If Linear works better, will migrate from Asana

---

## 8. Cursor / Claude Code Usage

**What was mentioned:**
- Shamil not using Cursor this sprint (auth token issues)
- Using VS Code instead
- Ruy considering turning off Cursor licenses if not being used
- Shamil to try fixing it next sprint

---

## 9. Linter Addition (Shamil)

**What was mentioned:**
- Shamil added a linter to the repository
- Purpose: reduce messiness, simplify development
- Makefile updates visible

---

## Key Decisions Made

| Decision | Details |
|----------|---------|
| Progressive sidebar display | Start with "My Challenge" only, reveal fields as populated |
| Highlight commitment | Make it visually distinct when filled |
| Add extraction conditionals | "Only if X has been identified..." in prompts |
| Remove new chat confirmation | Won't do (Chainlit default, useful feature) |
| Language: single per user | Remove selector for normal users, keep for admins |
| Test Linear | Next sprint, Ruy to evaluate vs Asana |

---

## Blockers Identified

| Blocker | Owner | Resolution |
|---------|-------|------------|
| Privacy policy link | Ruy | Has draft, needs to add to ticket |
| Language policy decision | Ruy | Send note to team (Nelson, Dolo) |
| Standalone UX decisions | Ruy | Needed before tutorial wizard |
| Date calculation reliability | Mike | Create ticket, implement datetime tool |

---

## Next Steps

1. **Shamil:** Implement progressive sidebar display + commitment highlighting
2. **Shamil:** Add conditional logic to extraction prompts in `profiles.toml`
3. **Mike:** Create ticket for date calculation fix
4. **Mike:** Implement language selector removal for normal users
5. **Ruy:** Add privacy policy draft to ticket
6. **Ruy:** Send note about language policy to Nelson/Dolo
7. **Ruy:** Test Linear next sprint
8. **Shamil:** Try to fix Cursor authentication
