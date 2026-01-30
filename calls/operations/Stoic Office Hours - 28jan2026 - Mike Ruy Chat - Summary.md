# Mike-Ruy Chat Summary (Post Product Strategy)
**Date:** January 28, 2026
**Participants:** Ruy (PM/CTO), Mike (Dev Lead)
**Context:** Informal debrief immediately after Product Strategy session with Oseas/Nelson

---

## Executive Summary
Quick tactical debrief after the intense product strategy session. Mike proposed a user-facing dashboard as a visual "wow factor" for demos. Ruy and Mike aligned on Q1 priorities: fix bugs for 5 users by Friday, then focus on AI Coach multi-session architecture. Discussed three memory approaches for the AI Coach. Confirmed Shamil moves to help Ruy with Coach implementation.

---

## 1. User Dashboard as Visual Win
**Status:** Idea — not committed

**What was discussed:**
- Mike proposed: when users log in, show a dashboard instead of jumping straight to chat
- Content: session count, key topics, next reminder, progress visualization
- Rationale: demos need visual "wow" — graphs and numbers beat a chat interface for sales
- Ruy connected this to the behavior change vision: users need visibility into their goals to stay motivated
- Both agreed on a timeline/gamified visual showing microhabit check-ins and progress toward goals

**Decision:** Not committed for this sprint. Captured as idea.

---

## 2. Standalone UX Question
**Status:** Open question

- Ruy noted: the standalone experience (outside Thinkific) is an unresolved design problem
- Connects to the AI General Coach — what does a user see besides a chat?
- The dashboard idea could be part of the answer

---

## 3. Immediate Priorities (This Week)
**Status:** Agreed

**Decisions made:**
- Fix known bugs by Friday so 5 users can test
- Don't touch prompts/base personality — prompt changes are a "time sink"
- Send clear usage instructions ("setting") so users have correct expectations
- Most user feedback is feature requests, not bugs — need discipline to filter

---

## 4. Quarter-Level Focus
**Status:** Discussed

**Ruy outlined three tracks:**
1. **Enterprise Integration** — specs confirmed, Ruy will write them up
2. **Metrics/Dashboard** — Nelson owns the spec for buyer-facing dashboards; dev implications TBD
3. **AI Coach Multi-Session** — the main R&D focus for Ruy this quarter

**Mike's reaction:** Optimistic about Q1 "based on the idea that there's not much more" added to scope.

---

## 5. AI Coach Memory Architecture
**Status:** Exploring three approaches

**Three options discussed:**
1. **Hack existing memory system** — extend current user facts with structured challenge/goal data
2. **Structured JSON with get/set** — code a proper memory layer, compare with option 1
3. **Session artifacts (Nelson's idea)** — like Claude Projects: generate a text summary after each session, feed it as context to the next. Simple, might work well enough.

**Ruy's insight:** The core technology is memory + prompting. UX and screens matter but aren't the hard part.

**Mike's comment:** "Hay que buscar e interrogar a Claude también" — prototype with Claude to test approaches.

**Plan:** Ruy develops hypotheses, shares with Mike and Shamil, Shamil helps implement. Mike consulted for architectural decisions.

---

## 6. Shamil's Role Shift
**Status:** Confirmed

- Shamil moves from Teams work to helping Ruy with Coach implementation
- Ruy noted Shamil delivered a feature today — "ya le está agarrando la onda"
- Mike comfortable with this: Teams work is "a bit to the side" for now

---

## 7. Process Improvements
**Status:** Sprint/quarter goal

- Need better development system: configured platform, good bug filters
- Align on PMF testing with Leo
- Bug triage discipline: most feedback = feature requests, not bugs

---

## 8. Sprint Planning Logistics
- Sprint planning Thursday (Jan 30)
- Calendar invite was accidentally deleted — Ruy resending
- Shamil requested 10-11 slot

---

## Key Decisions Made

| Decision | Details |
|----------|---------|
| Fix bugs by Friday | 5 users testing, no prompt changes |
| AI Coach is Ruy's Q1 focus | Memory architecture + prompting |
| Shamil helps Ruy on Coach | Shifts from Teams to Coach implementation |
| Nelson owns dashboard specs | Dev implications assessed after spec |
| Don't touch prompts now | Time sink, defer |

---

## Next Steps

1. Ruy: Fix bugs and prepare user instructions by Friday
2. Ruy: Write enterprise integration specs
3. Ruy: Develop AI Coach memory hypotheses, share with Mike + Shamil
4. Mike: Continue Teams bug fixes, available for architecture decisions
5. Ruy: Resend sprint planning invite for Thursday
