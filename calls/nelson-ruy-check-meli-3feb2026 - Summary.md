# MELI Proposal Strategy Call - Summary
**Date:** February 3, 2026
**Participants:** Ruy (PM/CTO), Nelson (Sales/BD)
**Type:** Strategy / Product Design Session

---

## Executive Summary

Ruy and Nelson aligned on how to structure the AI Coach offering for MercadoLibre's leadership programs. Key decision: replace the microhabit-first approach with a Coach-first model where microhabits become one tool among many. They agreed on naming the coach "Axia" (gender-neutral, sounds good) and defined distinct flavors for ADN MELI (basic CB frameworks) vs Leading at MELI (CB + 4 additional leadership themes). Timeline is Q2-Q3 2026.

---

## 1. Current State of MELI Relationship

**Context:** MELI uses Google Chat (not Slack) company-wide except IT. Previous integration used Google Sign-In which simplified authentication.

**What they want:** Post-ADN MELI reinforcement for leaders after completing the in-person workshop.

**Timing:** Q2-Q3 2026 start (2-3 months out)

---

## 2. Integration Approach

**Decision:** Google Chat is official at MELI. Onboarding/assessment needs a web app (can't do it in Google Chat), but follow-up/coaching CAN happen in Google Chat.

**Technical note:** Thinkific with Google Sign-In works as quasi-SSO for them.

**Ruy's position:** "Yo lo ofrecería así" — offer assessment+debrief in app, then coaching follow-up in Google Chat.

---

## 3. Microhabit vs Coaching Debate (Key Design Decision)

**Nelson's concern:** Are we marrying coaching methodology with microhabits without validation? "Es solo una idea que venimos desde la teoría de gestión del cambio?"

**Ruy's response:** Microhabits come from behavior change theory, not coaching methodology per se. In application coaching, every session ends with a commitment — sometimes that's a microhabit, sometimes it's a conversation to have, sometimes it's something else.

**Resolution:** Don't force microhabits from the start. Instead:
- Assessment debrief → establishes context
- Coach receives that context → starts coaching relationship
- Microhabits are ONE tool the coach can propose, not the mandatory structure

**Nelson's reframe:** "El hábito... como un tool dentro del proceso de coaching"

---

## 4. Proposed User Journey

**Ruy's sequence:**
1. **Assessment + Debrief** — understand your profile
2. **Workshop** (ADN MELI in-person)
3. **Plan of Coaching session** — post-workshop, establish coaching agenda/themes
4. **6 sessions over 6 weeks** (1 per week) — coaching on established themes
5. **Then:** monthly check-ins or extend as needed

**Key insight:** First session should establish the user's agenda: "Platícame cuáles son los temas que traes" → refine → coach confirms "estos son tus prioridades" → then coaching starts.

---

## 5. Heartbeat Check-ins (Proactive Outreach)

**Nelson raised:** Open Interpreter/Open Cloud has "heartbeat" concept — wake the AI periodically to reach out proactively.

**Ruy agreed it's powerful but noted dependencies:**
- Need established context (agenda, past sessions)
- Could connect to calendar for contextual triggers ("¿Cómo te fue en tu sesión de equipo?")
- For now: personalized reminders based on context, not calendar integration

**Simpler version:** Every 3 days, contextual message: "¿Cómo te está yendo con tus reuniones de equipo?" based on what user has discussed.

---

## 6. Coach Naming Decision

**Problem:** "Conscious Insights" doesn't build relationship. Need a name for the coach.

**Options discussed:** Aurelio, Axia

**Decision: Axia**
- Gender-neutral
- "Suena bonito" (sounds good)
- Different "flavors" of Axia for different use cases

---

## 7. Two Coach Flavors for MELI

**ADN MELI Coach (for new leaders entering MELI culture):**
- Conscious Business frameworks (mindsets, agreements, basics)
- Focus: Learn to think/act in MELI culture

**Leading at MELI Coach (for leaders of leaders):**
- All CB frameworks PLUS:
  1. How to build teams to win
  2. How to break silos
  3. How to lead with startup mentality
  4. How to generate value with AI

**Key distinction:** Same coaching methodology, different knowledge base loaded.

---

## 8. Content Delivery Strategy

**Options discussed:**
1. Email content delivery (traditional)
2. Mount content library in their LMS
3. Axia in "learning mode" — shares content conversationally

**Ruy's concern:** Don't over-saturate with chatbots. Maybe a Spotify-like content page for browsing/recommendations alongside the coach.

**For MELI specifically:** Content catalog of capsules. Validate: our LMS or theirs?

---

## 9. Social Learning / Accountability

**Nelson's question:** "¿Cómo se motivas a las personas a hacer su coaching?" (beyond intrinsic motivation)

**Ruy's solution:** Monthly cohort calls
- Share how you're applying the learning
- Learn from others' experiences
- Coach becomes embedded in the sharing ("lo que estás haciendo está metido cómo estás utilizando las herramientas")

**For supervisors specifically:** Add group coaching layer facilitated by humans, potentially enriched by analytics.

**Nelson's idea:** Token counter for conversations (like step counter for health). Ruy skeptical of value to users.

---

## 10. Demo Assets

**Ruy showed:** Thinking Partner prototype with lateral sidebar showing progress/commitments.

**Nelson requested:** Screenshots of coach interface, especially sidebar, to include in proposal slides.

**Ruy committed:** Send screenshot to Nelson.

---

## 11. Division of Work

**Nelson:**
- Modify slides for MELI proposal
- Create slides for each coach flavor (ADN MELI, Leading at MELI)
- Map the 6-session sequence onto timeline
- Write up how each coach works (personalization explanation)

**Ruy:**
- Document all this in internal specs
- Review Nelson's slides when ready
- Send screenshot of coach interface

---

## Key Decisions Made

| Decision | Details |
|----------|---------|
| Coach name | "Axia" — gender-neutral, sounds good |
| Microhabit approach | Tool within coaching, not forced structure |
| Two coach flavors | ADN MELI (CB basics) vs Leading at MELI (CB + 4 leadership themes) |
| Session cadence | 6 weekly sessions post-workshop, then monthly |
| Integration | Assessment in app, follow-up in Google Chat |
| Social learning | Monthly cohort calls for supervisors |

---

## Blockers Identified

| Blocker | Owner | Resolution |
|---------|-------|------------|
| No Google Chat integration yet | Mike | Technical work needed |
| Memory architecture for coaching | Ruy/Mike | "Tengo que tener muy bien aterrizada la memoria" |
| Coach methodology documentation | Ruy | Needs Horacio/Tolo to refine prompts |

---

## Next Steps

1. **Nelson:** Update proposal slides with 6-session coaching sequence
2. **Nelson:** Create coach flavor slides (ADN MELI vs Leading at MELI)
3. **Ruy:** Send screenshot of coach interface with sidebar
4. **Ruy:** Document coaching sequence in internal specs
5. **Ruy:** Review Nelson's slides when ready
6. **Both:** Validate content delivery approach (our LMS vs theirs)
