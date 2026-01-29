# Asana Ticket Draft: Daily Companion Cyclic Flow

**Assignee:** Shamil
**Due:** Fri Jan 31 (check-in), Sprint 3 (implementation)
**Link to FRD:** [Add Notion link here]

---

## Title

Daily Companion Cyclic Flow — Exploration + Technical Proposal

---

## Description

Replace the linear check-in flow (form → end) with a cyclic dialogue flow that keeps users engaged and offers alternatives when they struggle.

**FRD is ready** — read it before starting.

---

## Your Assignment

### Step 1: Experience it as a User (Wed)

Do a complete flow of the accountability partner yourself:
- Set up a microhabit
- Get the ICS calendar invite
- Come back and do the check-in
- See the follow-up flow

Note what works, what's clunky, where the "end" happens.

### Step 2: Understand the Data Model (Wed-Thu)

You know Postgres. Find:
- Where check-in data is stored
- How habits are tracked
- What data is available to put in context window
- How the current steps work

Use the Claude Code repo docs Mike created.

### Step 3: Answer These Questions

- How easy is it to retrieve previous check-in history?
- What data is already stored from check-ins? (current schema)
- Where does modification happen? (new step? edit existing habit?)
- What would need to change to replace form with dialogue?

### Step 4: Propose Before Implementing

Come back with:
- Your findings on the open questions
- Your proposed technical approach
- Any clarifying questions for Ruy

**Do not start implementation until we review together.**

---

## Timeline

| Day | What |
|-----|------|
| Wed-Thu | Explore system + investigate data model |
| Fri | 30-min check-in with Ruy (evening BCN = afternoon GDL) |
| Sprint 3 | Implementation |

If stuck, ping Ruy — don't spin for too long.

---

## Why This Matters

We're building your skill to:
1. Understand systems end-to-end (user experience + data model)
2. Refine PRDs with technical detail
3. Propose before implementing (feature-driven development)

This is how we ship faster and with fewer surprises.

---

## Comments for Shamil

@Shamil — Read the FRD first. The "Core Insight" section explains WHY we're doing this (people get stuck, feel shame, disengage). The dialogue flow section shows WHAT we're building.

Your job this week is to understand HOW it works today so you can propose HOW to change it. Don't code yet — explore, investigate, propose.

Questions? Ping me async or we'll cover it Friday.

— Ruy
