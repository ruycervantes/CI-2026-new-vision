# Minimum AI Coaching for Team Effectiveness

**Date:** 26 Jan 2026
**Status:** Working thinking, not final

---

## The Dependency

Team Effectiveness MVP = Human consultant (team level) + AI coach (individual level)

The AI coach is what scales. If it doesn't work → the offering collapses.

---

## What We Need (Minimum)

### 1. Coach Mode
- **Memory across sessions** — Maintain thread of what we've worked on
- **Coaching goals tracked** — Know what the person is developing toward
- **Team context injected** — What the team committed to, shared agreements from Team Agreement Doc

This is the core. Deep conversations that help people see their patterns and work on them.

### 2. Daily Companion (Bare Minimum)
- Simple check-in prompt ("Did you practice X?")
- Yes/no logging
- Decent interaction quality

**Status:** Close to what we have now. 1-2 sprints to polish interactions.

---

## What We're NOT Blocking On

These make the individual product stronger but aren't required for team effectiveness:

| Feature | Why it can wait |
|---------|-----------------|
| GPS Dashboard | Team context + human consultant provide progress visibility |
| Goal Hierarchy visualization | Coach tracks goals internally, no UI needed yet |
| If-Then habit builder UI | Coach can create these conversationally |
| Sophisticated Adjust stage | Human consultant catches patterns, triggers coach conversations |

---

## Why Team Context Changes the Equation

In pure individual coaching, you need Daily Companion + GPS + Adjust to create:
- Accountability (someone checking on you)
- Progress visibility (seeing you're moving)
- Adaptation (help when stuck)

In team effectiveness, these come from elsewhere:
- **Accountability** → Team commitment ("I did my session" visible to team)
- **Progress visibility** → Human consultant tracks across individuals
- **Adaptation** → Consultant observes patterns, directs to coach

The team structure provides what the product would otherwise need to build.

---

## Implication for Roadmap

**To launch team effectiveness MVP, we need:**
1. Coach mode that holds memory + goals + team context
2. Minimal Daily Companion (check-in, logging)

**We do NOT need:**
- Full `core/vision.md` implementation
- GPS Dashboard
- Sophisticated habit tracking

This is less than the full individual behavior change vision, but enough to deliver value in the team context.

---

## Open Questions

- How does team context get into the AI coach? (Read from shared doc? Manual input? Consultant updates?)
- What's the handoff between consultant and AI coach? ("Work on X with your coach this week")
- How do we show the team "3 people did their sessions" without exposing content?
