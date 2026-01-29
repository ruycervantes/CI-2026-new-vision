# Daily Companion Cyclic Flow — FRD Draft

> **Status:** Ready for sprint planning (Thu)
> **Owner:** Shamil (implementation), Ruy (design)
> **Date:** January 27, 2026

---

## Core Insight (Why This Matters)

People don't fail at habits because they're lazy. They fail because they **get stuck and don't know how to adapt**.

The shame of repeated "failure" makes them disengage entirely. If we just send notifications over and over, they block out and stop using the system.

**The fix:** When someone struggles, offer alternatives. Make it a conversation, not a scorecard.

---

## Current State vs New State

**Current (linear):**
```
Microhabit → Follow-up → Check-in (form: stars + comment) → [END]
```

User gets calendar invite (ICS) → comes back → fills out form → done. No path forward if struggling.

**New (cyclic):**
```
Microhabit → Follow-up → Check-in (dialogue) → [Continue / Modify / Tactical Coaching] → Schedule Next → Loop
```

The check-in becomes a short conversation. Always ends with scheduling the next check-in — no dead ends.

---

## The Check-in Dialogue Flow

**Time-bounded:** 5-7 minutes max (not exchange-bounded — some users take longer per message)

### Flow:

1. **Rating:** "How's it going? 1-5?"

2. **Open exploration:** "Tell me more — how did it go?"
   - NOT "what did you learn" — just "how did it go"

3. **Branch based on response:**

   | Signal | Response |
   |--------|----------|
   | Struggling (low rating, negative sentiment) | "Do you want to talk about it? Is this still the right thing for you?" |
   | Okay but low rating | Explore why — forgot? circumstances? wrong habit? |
   | Good | Acknowledge, reinforce |

4. **Action based on dialogue:**
   - **Continue** — habit is working, keep going
   - **Modify** — adjust the habit (trigger, action, or both)
   - **Tactical coaching** — quick tips on how to follow through

5. **Schedule next check-in** — the loop closes here

---

## Scope

### In Scope (Q1)

- [ ] Replace form-based check-in with dialogue
- [ ] Conversational flow: rating → exploration → action
- [ ] Ability to modify habit from within check-in
- [ ] Tactical coaching responses (simple prompting)
- [ ] Schedule next check-in at end (cyclic)
- [ ] Store check-in data (rating, notes, outcome)

### Out of Scope (Future)

- [ ] Automatic handoff to Coach mode
- [ ] Pattern detection triggering Coach ("3 bad weeks → let's talk")
- [ ] System-initiated outreach based on patterns

### Open / Investigate

- [ ] **How easy is it to retrieve previous check-in history?** If easy → pattern detection could be in scope. If hard → just ask user directly.
- [ ] **What data is already stored from check-ins?** Need to understand current schema.
- [ ] **Where does modification happen?** New step? Edit existing habit record?

---

## Shamil's Assignment

**Goal:** Understand the system deeply, then propose the technical approach. Build the skill to refine PRDs with technical details before implementing.

### Step 1: Experience it as a User (Day 1)

Do a complete flow of the accountability partner (leadership partner) yourself:
- Set up a microhabit
- Get the ICS calendar invite
- Come back and do the check-in
- See the follow-up flow

Understand how it feels. Note what works, what's clunky, where the "end" happens.

### Step 2: Understand the Data Model (Day 1-2)

You know Postgres by now. Find:
- Where check-in data is stored
- How habits are tracked
- What data is available to put in context window
- How the current steps work

### Step 3: Use Available Resources

- **Claude Code repo docs** — Mike documented the system, use it
- **Ask Ruy** — if stuck or need clarification

### Step 4: Propose Before Implementing

Come back with:
- Answers to the Open Questions below
- Your proposed technical approach
- Any clarifying questions

**Do not start implementation until we review together.**

### Timeline

| Day | What |
|-----|------|
| Wed-Thu | Explore system as user + investigate data model |
| Fri | 30-min check-in with Ruy to review findings (evening BCN = afternoon GDL) |
| Sprint 3 | Implementation (~1 sprint scope) |

If stuck before Friday, ping Ruy — don't spin for too long.

---

## Open Questions (for Shamil to Answer)

| Question | Notes |
|----------|-------|
| How easy is it to retrieve previous check-in history? | Determines if pattern detection could be in scope |
| What data is already stored from check-ins? | Current schema |
| Where does modification happen? | New step? Edit existing habit record? |
| What would need to change to replace form with dialogue? | Technical delta |

---

## Open Questions (for Ruy)

| Question | Notes |
|----------|-------|
| Boundary: tactical coaching vs Coach handoff | For now, Daily Companion handles it. Handoff logic is future. |
| What exactly can be modified? | Just trigger? Whole habit? Need to define. |

---

## Implementation Notes from Mike (Sprint Planning Jan 29)

These are technical pointers Mike gave during the call. Shamil should study these before proposing an approach.

### Step prompt architecture
The bot uses **trigger words** — when the LLM says a specific word, the text that follows gets extracted into the sidebar. This is similar to the AI extract Shamil already built (first iteration). Shamil needs to understand:
- How step prompts are built (`profiles.toml`)
- How step succession works (based on trigger words)
- How text after the trigger gets extracted and placed in the sidebar

### Sidebar update on commitment change
If the user modifies their microhabit during the check-in dialogue, the **commitment in the sidebar must update**. Same trigger-word extraction flow: the bot says the trigger word, then states the new commitment, and it gets captured. This is the same mechanism as the existing extraction — just applied to an updated commitment.

### Existing chat capability
You can already chat at the check-in point in the current flow. The question is whether we need a **different prompt** for the new check-in step — yes, we do (Ruy to design).

### Testing shortcuts
- **Play button** — auto-advances through steps you've already seen (don't have to type/copy-paste). Very useful for testing the long LGP flow.
- **Gear button** (in message area) — jump to a different profile step directly. Saves time when you need to skip to a specific point in the flow.

### Where the new step fits
The new check-in dialogue is likely a **new step between "practice design" and "follow-up"** — something like "reporting back results" or "follow-up check-in." After this step completes (with possible habit modification), the flow returns to schedule the next check-in.

### Why chat-based (not form)
Beyond the coaching rationale: replacing the form with a text dialogue means check-ins could eventually happen inside **Microsoft Teams or other messaging platforms** — no need to come back to the app. This is a strategic enabler.

---

*Shamil: propose technical approach before implementing. This is how we do feature-driven development.*
