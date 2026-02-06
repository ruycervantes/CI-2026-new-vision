# Product Strategy Catch-Up — Nelson & Ruy (1-on-1)
**Date:** 27 January 2026
**Participants:** Nelson (product/operations lead), Ruy (PM + CTO)
**Type:** 1-on-1 product strategy alignment

---

## Executive Summary
Nelson and Ruy aligned on three strategic pillars for Accelen/Stoic: (1) a data layer ("Impact") to demonstrate client impact, (2) an AI general coach that maintains multi-session memory and context, and (3) blended journeys for HPT and Leadership Development. They agreed that the AI coach is the critical unlock — enabling individual coaching at scale within team effectiveness processes — and discussed concrete next steps for HPT validation with Horacio and Richie.

---

## 1. Data Layer / Impact Platform
**What was discussed:**
- Nelson's top priority: building a data layer so Axialent "has memory" — tracking how many people were impacted, connecting data sources (clients, users, surveys, assessments, platform progress, chatbot usage)
- Evolution path: data layer → analytics portal (client-facing impact) → intelligence portal (coach-facing insights)
- Data sources to connect: surveys, CB Assessments, CB Assessment 360, Thinkific progress, chatbot conversations
- Named it "Impact" — the purpose is demonstrating measurable impact to clients

**Decisions made:**
- Start with easiest data sources first (surveys, assessments)
- AI coaches data integration is Phase 2 (after coach is built)
- Not assigning to specific quarters yet — need to solve other things first

---

## 2. AI General Coach (Multi-Session)
**What was discussed:**
- Need to "unanchor" the coach from Thinkific lessons so it feels like a real coaching experience, not a lesson within an LMS
- Coach must maintain conversation threads across sessions (1, 2, 3... 6+) — tracking goals, challenges, commitments, adjustments
- Two implementation paradigms discussed:
  - **Artifacts approach**: Generate a summary artifact after each session, feed it as context into the next session (like Claude projects)
  - **Memory/graph approach**: Use agent memory tools that build a knowledge graph across sessions
- Claude Agent SDK mentioned as a potential path — give the agent file skills and let it manage its own memory
- Torch cited as a competitor doing similar things: AI coach as "TA" (teaching assistant) to a human coach, where AI session data feeds back to the human coach
- Coach needs to handle: goal-setting, tracking commitments, processing setbacks, recalibrating when habits aren't working (the "adjust" stage)
- Exporting coach data for human coaches is "technically easy" — all sessions stored in the system, just prompting work

**Key insight — the Torch model:**
- Nelson described Torch's approach: they provide a human coach + AI practice coach, where AI session data feeds to the human coach
- Both agreed this is "a company in itself" — enormous potential
- The AI coach as TA to the professor, not replacement

**Decisions made:**
- Ruy focuses on building the AI coach (this was already agreed but got derailed by HPT work)
- Nelson offered to handle the chatbot wizard himself to avoid distracting Ruy

---

## 3. Chatbot Wizard / Content-Connected Agents
**What was discussed:**
- Nelson wants to build a wizard for creating content-connected chatbots (for reflections, roleplay, learning)
- Use case: replace "el huevo" (an existing tool/approach that feels tedious) with AI-powered reflection chatbots connected to learning content
- Nelson has learned Claude Code and Cursor enough to potentially build this himself
- Ruy described existing tooling: base prompts, prompt design patterns, automated testing pipeline (3 tests: no loops, no data leakage, follows instructions)
- Concern about Nelson becoming a bottleneck if he's the only one who can create chatbots
- Ruy suggested: if there's a good business need and Nelson validates the wizard is needed, Shamil could work on this

**Decisions made:**
- Parked for now — Nelson will bring it back if needed
- Ruy won't prioritize it this quarter unless Nelson validates demand
- Ruy offered to share the tooling/skills so Nelson can prototype independently

---

## 4. Blended Journeys — HPT (Team Effectiveness)
**What was discussed:**
- HPT and Leadership Development are "the same dog in different costumes" — very similar processes
- Culture/strategic planning explicitly excluded for now ("esa huevada")
- Nelson's HPT process map: Diagnosis (individual DISC + collective) → Kickoff → Between-workshops (content + AI chatbots + community) → Live workshops → Loop
- Ruy proposed using CB Assessment + Axialent's Team Tool instead of DISC/Lencioni because:
  - Team Tool is proprietary to Axialent (Dolo says they have benchmark data)
  - Horacio designs with extreme detail — many digitizable components
- Ruy's proposed HPT flow: Assessment → identify gap → kickoff call → 3 teaching sessions (aula invertida, topic-specific based on assessment gaps) → in-person facilitation for difficult conversations → AI coaching throughout

**Key concept — Team Document:**
- Ruy pushed strongly for a "team document" — a living digital artifact that captures team agreements, pain points, progress
- This document feeds into: AI Coach context (so coaching connects to team goals), content chatbots (contextualizes learning), and impact measurement
- Horacio already does this manually with extensive notes — the opportunity is digitizing it
- Both agreed this connects individual coaching to team context, creating intrinsic motivation ("I need to prepare this conversation because it affects the team")

**Impact measurement approach:**
- Nelson emphasized everything must be "girado acerca del impacto"
- Agreed: impact is best demonstrated through qualitative changes participants articulate themselves, not just quantitative score changes
- Process: assessments establish the FROM → team document tracks progress → coaching sessions generate reflection → participants articulate their own impact

**Decisions made:**
- Nelson agrees team document is valuable — include it in AI Coach and content chatbots
- Ruy will share Horacio interview notes, design principles doc, and digitization opportunities table with Nelson
- Next steps: Nelson reviews docs → iterate → generate visualizations → validate with Horacio + Richie
- Agreed to create visual storytelling (diagrams, comics) for the HPT pitch rather than building a coded prototype

---

## 5. Shamil's Role — Resource Allocation Tension
**What was discussed:**
- Tension: Should Shamil work on AI Coach features or on the data/analytics layer?
- Ruy noted Shamil had 2 idle days because Ruy didn't have feature specs ready — bottleneck risk
- Nelson needs the data layer but doesn't want to distract from the coach
- Ruy suggested Shamil could work on the chatbot wizard if validated

**Decisions made:**
- No resolution yet — depends on what gets prioritized between AI coach, data layer, and chatbot wizard

---

## 6. Business Strategy — Spinning Off & Commercial Pressure
**What was discussed:**
- Agreement among Nelson, Leo, and Ruy that there should be a separation ("spinning") — doing two different things (Accelen consulting vs CI product)
- Oseas also agrees but something is blocking the decision
- Nelson's concern: Oseas is telling all partners to sell HPT, creating pricing/commercial bottleneck before the product is ready
- Nelson's preferred approach: find ONE partner to sell, nail the product, THEN scale to all partners
- Ruy agreed from product perspective: better to have 1 client to test with than 5 clients delivering the same old thing
- Revenue justification: AI coaching enables 20% higher ticket price by adding individual coaching to team processes (currently only team leader gets coaching; AI coach could serve everyone)

---

## 7. HPT Deliverables — Demo, Pitch, Pricing
**What was discussed:**
- Nelson identified three needs: (1) demo/experience visualization, (2) pitch focused on impact not features, (3) pricing
- Ruy showed Nelson the visual storytelling approach using diagrams and comics (generated via Claude Code + Gemini API)
- Agreed: visual storytelling is sufficient — no need for coded prototype
- Process: Ruy shares docs → Nelson iterates → generate visualizations → validate with Horacio and Richie

**Decisions made:**
- Ruy shares: design principles doc, Horacio notes, digitization table
- Nelson reviews and iterates on the narrative
- Next conversation with Horacio to validate approach
- Richie consulted for team expertise; Horacio for process digitization

---

## Key Decisions Made

| Decision | Details |
|----------|---------|
| AI Coach is the priority | Ruy focuses on multi-session AI coach over chatbot wizard and other features |
| Team Document is core to HPT | Living artifact connecting assessments, coaching, and impact measurement |
| Use CB Assessment + Team Tool | Over DISC/Lencioni for HPT diagnosis |
| Visual storytelling for HPT pitch | Diagrams/comics, no coded prototype |
| Start data layer with easy sources | Surveys and assessments first, AI coach data later |
| One HPT partner first | Validate with one client before scaling to all partners |

---

## Blockers Identified

| Blocker | Owner | Resolution |
|---------|-------|------------|
| Brilliant API rate limits and poor endpoints | Nelson | Contact Brilliant about roadmap; consider switching providers |
| Shamil capacity allocation unclear | Ruy/Nelson | Decide after Q1 priorities settle |
| Oseas blocking the spin-off decision | Oseas | Unknown — Leo and Nelson both raised it |
| Ruy got pulled into HPT research instead of AI coach | Ruy | Re-confirm AI coach as primary focus |

---

## Next Steps

1. Ruy shares with Nelson: Horacio interview notes, design principles doc, digitization opportunities table
2. Nelson reviews and iterates on HPT narrative
3. Nelson contacts Brilliant about API improvements
4. Ruy focuses on AI Coach multi-session architecture
5. Schedule follow-up with Horacio to validate HPT approach
6. Consult Richie for team effectiveness expertise
7. Decide Shamil's allocation (AI coach vs data layer vs wizard)
