# AI Coach Spec — Execution Plan

*Created: Feb 9, 2026 | Updated: Feb 10, 2026 (Phase A.2 + multi-case extension complete)*
*Status: Phase A.2 complete + multi-case validation — 4 cases analyzed, 30 praxis principles documented*

---

## Overview

Four workstreams, sequenced. Each feeds the next.

```
Doc A (Methodology + Praxis)
    → Doc B (AI Design Synthesis)
        → Technical (Memory, Architecture)
            → Prompt Architecture (Buildable Specs)
```

| Workstream | What | Depends On |
|-----------|------|-----------|
| **1. Doc A** | Human coaching methodology + praxis | Transcript processing (done), interviews |
| **2. Doc B** | AI coaching design synthesis — what AI can/can't do | Doc A + shared foundation from TE docs |
| **3. Technical** | Memory architecture, commitment tracking, CB knowledge injection | Doc B (what needs to be tracked + constraints) |
| **4. Prompt Architecture** | Pre-coaching prompt, Session N template, closing prompt | Doc A (what to encode) + Doc B (design constraints) + Technical (memory approach) |

---

## Workstream 1: Doc A — Coaching Methodology + Praxis

**Purpose:** Document how Axialent coaches actually do individual coaching — the formal methodology AND the observed praxis. This is the *human coaching reference* that everything else builds on.

**Analogous to:** `team-effectiveness/research/methodology.md` (but for individual coaching, not HPT)

### Two Layers to Extract

**Layer 1: Theory (formal methodology)**
- Source: Axialent Coaching Handbook (`axialent-coaching-handbook-summary.md`)
- The 8-step session process
- Role plays, centering, receiving
- Product vs process objectives
- The Gap as raw material

**Layer 2: Praxis (observed practice)**
- Sources: Coaching Knowledge Framework, Ruy's 4 sessions, Horacio's case study, Richi call
- Praxis principles (named, documented as principles alongside theory)
- Inter-session architecture (the connective tissue between sessions)
- How theory adapts in reality

### The Core Focus: Inter-Session Architecture

The handbook documents *within-session* process well. What's underdocumented is *between-session* architecture:

- How session 0 (setup) feeds session 1
- How session 1's closing/commitment becomes session 2's opening
- How the "one long conversation" manifests concretely
- How topics get selected, tracked, graduated, or parked across sessions
- How commitments carry (commit → report → adjust → recommit)
- How themes deepen over time (tactical → identity-level)

**The sequence mechanics observed in Ruy's sessions:**
```
Session 0 (Setup):  Challenge list → initial prioritization → explain process
Session 1:          Reconnect (read back items) → validate → select → work → commit
Session 2:          Commitment follow-up → report → new work → commit
Session 3:          Light follow-up → theme graduation (surface resolves, deeper emerges)
Session 4 (Final):  Convergence → retrospective → gift question → "second season" framing
```

### Praxis Principles to Document

From Horacio's craft (to be named and documented as principles):

| Principle | Source | Description |
|-----------|--------|-------------|
| **One Long Conversation** | Horacio interview | Sessions are not isolated events — one continuous conversation distributed across moments |
| **Track What's Left Out** | Ruy Session 1 | Coach notices what was chosen AND what was avoided, surfaces the pattern |
| **Yellow Lights** | Horacio interview | Personal reminders flagging topics for future exploration |
| **Named Entity Tracking** | Horacio interview | If coachee mentions "Julián" in session 3, recall "Julián from session 2 who..." |
| **Everything Reveals or Conceals** | Horacio interview | All information is data — either exposing or covering something |
| **Commitment as Doorway** | Ruy Session 2 | Session 2+ opens through commitment follow-up, not fresh exploration |
| **Outlier vs Design** | Ruy Session 2 | When coachee reports success, ask: "was this luck or intentional?" |
| **Theme Graduation** | Ruy Session 3 | Surface issues resolve, revealing deeper root causes |
| **Side Comments as Signals** | Ruy Session 3 | The most important insight may come from an aside, not the declared agenda |
| **Desdoblamiento** | Ruy Session 3 | Third-person self-observation exercise |
| **Gift Question** | Ruy Session 4 | Personalized self-coaching question left as closing ritual |
| **Second Season Framing** | Ruy Session 4 | Engagement endings are chapter boundaries, not story endings |
| **Convergence in Final Session** | Ruy Session 4 | Last session consolidates and connects threads, doesn't expand |
| **Frustration-as-Signal Reframe** | Ruy Session 4 | Teaching coachee to use frustration as self-coaching tool |
| **Hat Switch** | Ruy Session 3 | Explicitly marking transition between roles (dual-role relationships) |
| **"Hay que" → "Voy a"** | Ruy Session 2 | Catching hedging language, converting impersonal to personal commitment |
| **Forced Compliance vs Flowing Integration** | Ruy Session 3 | Distinguishing behavioral compliance from genuine integration |
| **Session Scheduling Within Session** | Horacio interview | Schedule next session before ending current one |
| *NEW from multi-case analysis (12 additional — see `coaching-cases-analysis.md` for full details):* | | |
| **Diagnostic as Conversational Re-entry (#19)** | CASO 1, 2, 3 | LSI as persistent "conversational pantry" |
| **Vacuum/Bache as Productive Space (#20)** | CASO 1, 3 | Dead spots precede deeper theme emergence |
| **Parallel Track Recognition (#21)** | CASO 1 | Meta-structural awareness of non-converging themes |
| **Safe Space as Primary Value (#22)** | CASO 1 | Relational container itself as therapeutic agent |
| **Behavioral Substitution (#23)** | CASO 1 | Coachee does productive-but-avoidant work |
| **Mirror Cases Across Arc (#24)** | CASO 1 | Structurally similar situations recurring across engagement |
| **Coach Self-Disclosure as Resolution (#25)** | CASO 2 | Deliberate personal story creates identification and breakthrough |
| **Mid-Engagement Drift (#26)** | CASO 1, 2 | Predictable momentum loss at sessions 3-4 |
| **"Tarea" as Integration Homework (#27)** | CASO 2 | Commitments to synthesize learning into personal system |
| **Role Play as Modeling (#28)** | CASO 3 | Coach demonstrates behavior coachee has never performed |
| **Acceptance as Resolution (#29)** | CASO 3 | Stance change as valid resolution (not just action) |
| **Micro-Escalation in Skill Teaching (#30)** | CASO 3 | Full demonstration first, then micro-practice |

### Outline

```
1. SHARED FOUNDATION (reference, not rewrite)
   - Pointer to synthesis-v2.md for: BE→DO→HAVE, The Gap, Subject→Object,
     Real Content Creates Real Learning, Trust Before Task, Foundational Accord
   - What's coaching-specific vs shared with HPT

2. THE COACHING METHODOLOGY (Theory — from Handbook)
   2.1 Core Philosophy — Development model, not defective model
   2.2 The 8-Step Session Process
   2.3 Role Plays — Direct and inverse
   2.4 Centering and Receiving
   2.5 Product vs Process Objectives

3. THE COACHING PRAXIS (Observed Practice — from interviews + sessions)
   3.1 Praxis Principles (table above, expanded with examples)
   3.2 How Theory Adapts in Practice
       - Session flexibility (not every session has explicit commitment)
       - Two modes: coaching vs. advisory
       - Challenge interventions in practice

4. THE ENGAGEMENT LIFECYCLE
   4.1 Setup / Pre-coaching
       - Meeting Zero (coach, coachee, boss/sponsor)
       - Diagnostic selection and administration
       - Establishing goals and expectations (all parties)
       - Explaining the coaching process
       - Logistics (scheduling cadence, calendar, communication)
   4.2 The Session Arc
       - Session 0 → Session 1 transition
       - Session 1: Opening the relationship
       - Sessions 2-5: The middle (commitment-driven openings, theme evolution)
       - Session N (final): Closing the engagement
   4.3 Between Sessions
       - Coach preparation ritual (15 min pre-session review)
       - Note-taking practice (during + post-session cleanup)
       - Follow-up on commitments
   4.4 Closing the Engagement
       - The closing session anatomy (retrospective, feelings, gift question, continuation path)
       - Reporting to stakeholders (boss, HR) — confidentiality boundaries
       - Artifacts produced
       - Post-engagement follow-up
       - "Second season" framing

5. THE INTER-SESSION ARCHITECTURE (the core value-add)
   5.1 Session opening grammar by session number
   5.2 How commitments carry across sessions
   5.3 How topics are selected, tracked, graduated, or parked
   5.4 How themes deepen over time
   5.5 The "one long conversation" in practice

6. CASE STUDIES
   6.1 Horacio's coaching cases — 3 sanitized engagements (CASO 1-3)
       - CASO 1: COACHEE1/EMPRESA1 — anxiety/leadership, behavioral substitution pattern
       - CASO 2: COACHEE2/EMPRESA2 — instrumental reasoning, ITC breakthrough
       - CASO 3: COACHEE3/EMPRESA3 — green/defensive, reclamo skill, only role play case
   6.2 Ruy's 4-session coaching engagement with Horacio
   6.3 Cross-case comparison — universality table, 30 praxis principles, coachee typology
```

### Sources Per Section

| Section | Have | Need |
|---------|------|------|
| 1. Shared Foundation | synthesis-v2.md, methodology.md | Identify what's shared vs coaching-specific |
| 2. Methodology | Handbook summary (complete) | Already documented |
| 3. Praxis Principles | Coaching Knowledge Framework + 4 session analyses | **Augment session analyses** with methodology-specific extraction |
| 4.1 Setup | Horacio mentions it (high-level) | **Interview Horacio** + **Ruy reconstructs Dec 17** |
| 4.2 Session Arc | 4 processed sessions + Horacio case (sessions 1-3) | **Interview Horacio** for sessions 4-6 of his case |
| 4.3 Between Sessions | Coaching Knowledge Framework (note-taking, prep) | Mostly covered |
| 4.4 Closing | Ruy Session 4 analysis (closing anatomy) | **Interview Horacio** on reporting/artifacts/stakeholder communication |
| 5. Inter-Session Architecture | 4 session analyses (partial) | **Augment with methodology-specific extraction pass** |
| 6.1 Horacio case | Detailed sessions 1-3 | **Interview Horacio** for sessions 4-6 |
| 6.2 Ruy case | 4 sessions processed | **Augment with inter-session analysis** |

### The Reprocessing Question

The 4 coaching session transcripts were processed with a *product design research* lens. For Doc A, we need a *methodology extraction* pass focused on:

1. **Session opening mechanics** — Exactly how does each session begin? What's the first thing said? How is prior context introduced?
2. **Commitment cycle** — What was committed? How was it followed up? What happened when it was/wasn't done?
3. **Topic threading** — How do themes from session N appear in session N+1? What vocabulary carries over?
4. **Handbook mapping** — Which of the 8 steps are visible in each session? Where does practice diverge from theory?

**Approach:** Don't rewrite the existing summaries. Create an **additional analysis document** — an inter-session architecture extraction that reads across all 4 sessions as one arc.

---

## Workstream 2: Doc B — AI Coaching Design Synthesis

**Purpose:** Given what we know about how coaching works (from Doc A), what can and can't an AI do? What's essential to preserve? What changes? Where does AI have advantages?

**Analogous to:** `team-effectiveness/research/synthesis-v2.md`

**Depends on:** Doc A (must be substantially complete first)

### Proposed Structure (modeled on synthesis-v2.md)

```
0. THE MENTAL MODEL
   - What is AI coaching? (not a chatbot, not therapy, not advice)
   - The persistent coaching relationship (4 touchpoints)
   - One coach, one memory, one long conversation

1. THE PROBLEM
   - Why do people need coaching support between human sessions?
   - Why can't current tools deliver this?
   - What gap does AI coaching close?

2. THE MECHANISMS
   - Which coaching mechanisms can AI deliver?
   - Which require adaptation?
   - Which are out of scope?

   Mapping against Doc A:
   | Mechanism | Human Coach | AI Coach | Notes |
   |-----------|------------|----------|-------|
   | The Gap | Identifies through questions | Same — questioning + assessment data | AI advantage: assessment integration |
   | Memory/Continuity | 15-min prep, notes | Perfect recall | AI advantage: never forgets |
   | Challenge interventions | Reads energy, timing | Must be designed carefully | AI limitation: no non-verbal cues |
   | Role plays | Embodies the counterpart | Can simulate conversations | Different but possible |
   | Named entity tracking | Human memory | Structured tracking | AI advantage: reliable |
   | Commitment follow-up | Manual tracking | Automated + proactive | AI advantage: consistency |
   | Non-verbal cues | Full access | Text/voice only | AI limitation |
   | Emotional attunement | Felt sense | Inferred from language | AI limitation |

3. THE INTERVENTIONS
   - What does the AI Coach actually do in each touchpoint?
   - Scheduled sessions, on-demand, check-ins, reminders
   - How each maps to the 8-step methodology

4. THE DESIGN LOGIC
   - Essential vs contingent (what must be preserved, what can change)
   - Memory architecture implications
   - The lockstep principle (coaching + visibility advance together)
   - Privacy boundaries (individual vs team context)
   - Session cadence design

5. HUMAN vs AI
   - What the human coach does that AI can replicate
   - What AI does better (memory, availability, consistency, scale)
   - What AI can't do (physical presence, felt sense, organizational navigation)
   - The Torch Model (AI as "TA" to human coach)

6. THE FOUNDATIONAL ACCORD (adapted for AI)
   - How CB values are embedded in the AI Coach's behavior
   - What the AI Coach will and won't do
```

### What Feeds Doc B from Doc A

| From Doc A | Informs Doc B |
|-----------|--------------|
| Praxis principles | Which can AI replicate? Which need adaptation? |
| Inter-session architecture | Memory architecture requirements |
| Engagement lifecycle | Session type taxonomy for prompts |
| Closing process | How AI handles engagement endings |
| Case studies | Reference examples for design decisions |

### What Feeds Doc B from TE Docs (Shared Foundation)

| From TE Docs | How It Applies to AI Coaching |
|-------------|------------------------------|
| BE→DO→HAVE | AI works at all levels — awareness (BE), skill practice (DO), tracking results (HAVE) |
| The Gap | AI identifies and tracks gaps across sessions |
| Subject→Object | AI helps make patterns visible through longitudinal tracking |
| Real Content | AI must work with user's real situations, not hypotheticals |
| Trust Before Task | AI must build trust before challenging — session sequencing matters |
| Social Accountability | Team context injection — AI knows team agreements |
| Foundational Accord | AI embodies CB values in every interaction |
| 90-Day Cycle | Engagement design: ~12 sessions over ~90 days |

---

## Workstream 3: Technical Considerations

*Unchanged from previous plan — these are informed by Doc B*

### Memory Architecture

**Decision needed:** Which paradigm?
- **A) Artifacts** — Session summaries as documents fed forward
- **B) Knowledge Graph** — Structured graph of person's development journey
- **C) Hybrid** — Agent manages memory internally + produces human-readable artifacts

**What memory must track** (from Doc A praxis principles):
- Goal Hierarchy (Destination → Management → Tracking) and evolution
- Commitments per session + follow-up status
- Named entities (people, situations) across sessions
- Yellow lights (topics flagged for future exploration)
- Session trajectory (flow, not every detail)
- Key moments / revelations that "change the picture"
- Theme status (active, parked, graduated)

### Commitment Tracking

- Per-session commitments with deadlines
- Follow-up status
- Modification history
- Connection to check-in loop (Daily Companion)

### CB Knowledge Injection

- Option A: Single mega-prompt
- Option B: Modular skills per CB topic

---

## Workstream 4: Prompt Architecture

*Depends on Doc A + Doc B + Technical*

### Prompts to Design

| Prompt | Informed By | Key Requirements |
|--------|-----------|-----------------|
| **Pre-coaching** | Doc A §4.1 (Setup) | CB assessment debrief + goal setting + process explanation |
| **Session 1** | Doc A §4.2 + §5.1 | Reconnect to setup, establish gap, first deep work |
| **Session N (2-5)** | Doc A §5 (Inter-session architecture) | Commitment follow-up opening, memory injection, connection-making |
| **Closing session** | Doc A §4.4 (Closing) | Convergence, retrospective, gift question, continuation path |
| **Between-session** | Doc B §3 (Interventions) | Check-ins, reminders, nudges |

### Open Decision

Run AI Coach through the chatbot design process (`chatbot-design/`)? Would produce formal Project Brief + Chatbot Specification.

---

## Execution Phases

### Phase A — Process Existing Material ✅ COMPLETE

- [x] `/process-call` on 4 coaching session transcripts (Sessions 1-4)
- [x] `/process-call` on Jan 27 Horacio continuation call
- [x] 10 files created: Summary + Analysis for each

### Phase A.2 — Methodology-Specific Extraction ✅ COMPLETE

- [x] **Inter-session architecture analysis** — `research/coaching/analysis/inter-session-architecture-analysis.md`
  - Session opening mechanics (grammar by session position)
  - Commitment cycle (commit → act → report → extract → recommit)
  - Topic threading (theme map, theme graduation, vocabulary continuity)
  - Handbook mapping (which 8 steps visible per session, where practice diverges)
- [x] **Theory-praxis mapping** — Comprehensive table: theory concepts observed, theory concepts absent, praxis innovations not in theory (18 documented)
- [x] **Shared foundation identification** — Reference vs. rewrite decision table for Doc A. 9 shared concepts identified, 5 team-specific concepts excluded, clear guidance on what to reference vs. write new.

### Phase A.2 Extension — Multi-Case Validation ✅ COMPLETE (Feb 10, 2026)

- [x] **CASO 1 analysis** — `research/coaching/analysis/caso1-inter-session-architecture-analysis.md`
  - COACHEE1 at EMPRESA1: Chemical company sales leader, 6+LSI sessions
  - Key finding: two parallel tracks (interpersonal + anxiety) that never converge
  - 6 new praxis principles (#19-24): Diagnostic Re-entry, Vacuum as Productive Space, Parallel Track Recognition, Safe Space as Primary Value, Behavioral Substitution, Mirror Cases
- [x] **CASO 2 analysis** — `research/coaching/analysis/caso2-inter-session-architecture-analysis.md`
  - COACHEE2 at EMPRESA2: Industrial engineer/sales manager, 6+LSI sessions
  - Key finding: horizontal theme graduation (interpersonal → motivation → procrastination) vs. vertical
  - 4 new praxis principles (P19-P22): Coach Self-Disclosure, Mid-Engagement Drift, Integration Homework, Coach Note-to-Self
- [x] **CASO 3 analysis** — `research/coaching/analysis/caso3-inter-session-architecture-analysis.md`
  - COACHEE3 at EMPRESA3: Supply chain planning, 15yr tenure, 6+LSI sessions
  - Key finding: only case with role play deployed (Modified Direct Version); "bache" productive emptiness pattern
  - 5 new praxis principles (#19-23): Bache as Productive Emptiness, Role Play as Modeling, Acceptance as Resolution, Micro-Escalation in Skill Teaching, Coach's Private Concern as Predictive Tracker
- [x] **Cross-case comparison** — `research/coaching/analysis/coaching-cases-analysis.md`
  - Universality assessment: 11 universal, 5 context-dependent, 1 N/A, 1 likely universal
  - 30 total praxis principles (18 original + 12 new, deduplicated)
  - Session 3 emergence pattern confirmed across 3/4 cases
  - Commitment→opening quality correlation confirmed across 4/4 cases
  - Coachee typology (4 types observed)
  - 12 AI Coach design principles derived from multi-case evidence
- [x] **Updated inter-session architecture analysis** — Added Part 8 (cross-case validation) to original doc

### Phase B — Ruy Reconstructs Setup Session

- [ ] Write down what you remember from Dec 17 setup session
  - What did Horacio explain about the coaching process?
  - What goals/expectations were discussed?
  - Was your boss/sponsor involved?
  - What logistics were agreed?
  - What was the diagnostic plan?

### Phase C — Interview Horacio (Ruy schedules)

**Topics:**
- [ ] Setup session structure (validate Ruy's recollection)
- [ ] Sessions 4-6 of his chemical company case
- [ ] Logistics: scheduling, cancellations, frequency
- [ ] Commitment tracking: what happens when homework isn't done?
- [ ] Engagement-level goal setting
- [ ] Closing: last session, reporting to stakeholders, confidentiality, artifacts
- [ ] Post-engagement follow-up

### Phase D — Interview Richi (Ruy schedules)

- [ ] His perspective on setup/pre-coaching
- [ ] Methodology validation
- [ ] Beta testing follow-up

### Phase E — Draft Doc A (PAI drafts, Ruy validates)

- [ ] Write Doc A using outline above
- [ ] Merge interview findings
- [ ] Complete case studies
- [ ] Ruy reviews and finalizes

### Phase F — Draft Doc B (PAI drafts, Ruy validates)

- [ ] Write Doc B using synthesis-v2.md as structural model
- [ ] Map mechanisms (human → AI)
- [ ] Identify essential vs contingent
- [ ] Ruy reviews — this is where key design decisions get made

### Phase G — Technical + Prompt Architecture

- [ ] Memory architecture decision (informed by Doc B)
- [ ] Prompt templates (informed by Doc A + Doc B)
- [ ] Optionally: run through chatbot design process

### Suggested Timeline

```
Week 1:  Phase A.2 (methodology extraction — PAI)
         Phase B (Ruy writes setup recollection)
         Schedule interviews with Horacio + Richi

Week 2:  Phase C (interview Horacio)
         Phase D (interview Richi, if available)
         Phase E starts (draft Doc A skeleton)

Week 3:  Phase E completes (Doc A finalized)
         Phase F (draft Doc B)

Week 4:  Phase G (technical + prompt architecture)
```

---

## Existing Asset Inventory

### Research Documents (Coaching)
| File | What It Covers | Feeds |
|------|---------------|-------|
| `research/coaching/axialent-coaching-handbook-summary.md` | 8-step session process, role plays, centering, receiving | Doc A §2 (Theory) |
| `research/coaching/coaching-knowledge-framework.md` | 3-layer model, 14 design implications, praxis observations | Doc A §3 (Praxis) |
| `research/coaching/ai-coach-design-considerations.md` | Memory paradigms, open questions, architecture decisions | Doc B §4-5 |
| `research/coaching/minimum-ai-coaching-for-te.md` | What's needed for HPT MVP vs. full vision | Doc B §4 |
| `research/coaching/analysis/horacio-case-study-analysis.md` | 6-session case study (sessions 1-3 detailed) | Doc A §6.1 |
| `research/coaching/analysis/horacio-intervention-setups.md` | Engagement types, setup structures | Doc A §4.1 |
| `research/coaching/analysis/inter-session-architecture-analysis.md` | Opening mechanics, commitment cycle, topic threading, theory-praxis mapping, shared foundation + cross-case validation (Part 8) | Doc A §4, §5 + Doc B |
| `research/coaching/analysis/caso1-inter-session-architecture-analysis.md` | CASO 1 full A.2 analysis: COACHEE1/EMPRESA1 (chemical company, 6+LSI sessions) — parallel tracks, safe space, behavioral substitution | Doc A §6.1 |
| `research/coaching/analysis/caso2-inter-session-architecture-analysis.md` | CASO 2 full A.2 analysis: COACHEE2/EMPRESA2 (industrial, 6+LSI sessions) — horizontal graduation, ITC, mid-engagement drift | Doc A §6.1 |
| `research/coaching/analysis/caso3-inter-session-architecture-analysis.md` | CASO 3 full A.2 analysis: COACHEE3/EMPRESA3 (supply chain, 6+LSI sessions) — role play, bache, reclamo | Doc A §6.1 |
| `research/coaching/analysis/coaching-cases-analysis.md` | Cross-case comparison: universality table (30 principles), session arc comparison, coachee typology, 12 AI Coach design principles | Doc A §4-7 + Doc B |

### Research Documents (Team Effectiveness — Shared Foundation)
| File | Shared Foundation Content | Team-Specific Content |
|------|--------------------------|----------------------|
| `team-effectiveness/research/synthesis-v2.md` | BE→DO→HAVE, The Gap, Subject→Object, Real Content, Trust Before Task, Social Accountability, Foundational Accord, 90-Day Cycle | I/Wi/It dimensions, 4-Quadrant model, HPT interventions, meeting facilitation |
| `team-effectiveness/research/methodology.md` | Assessment frameworks (LSI, CB Assessment), praxis notes (role modeling, consultant coherence, zero attachment) | Katzenbach/Lencioni, 4-Quadrant maturity levels, accountability framework |

### Core Documents
| File | Content |
|------|---------|
| `core/vision-behavior-change.md` | 4 touchpoints, goal hierarchy, check-in loop, adjust stage, memory architecture |
| `core/vision.md` | Platform vision, AI Coach as shared foundation |
| `core/roadmap.md` | Q1 build plan, feature candidates |
| `core/MVP-offer-hpt.md` | 90-day team effectiveness cycle |

### Processed Coaching Sessions (Phase A — COMPLETE)
| File | Key Findings |
|------|-------------|
| `calls/sesiones-coaching-ruy/...-sesion-1 - Summary.md` | Memory-driven opening, structured choice, tracking what's left out |
| `calls/sesiones-coaching-ruy/...-sesion-1 - Analysis.md` | Session 1 unique character, 8-step mapping, memory as trust signal |
| `calls/sesiones-coaching-ruy/...-sesion-2 - Summary.md` | Commitment follow-up as architecture, outlier-vs-design reframe |
| `calls/sesiones-coaching-ruy/...-sesion-2 - Analysis.md` | Session opening grammar, "hay que" → "voy a" conversion |
| `calls/sesiones-coaching-ruy/...-sesion-3 - Summary.md` | Theme graduation, desdoblamiento, side comments as signals |
| `calls/sesiones-coaching-ruy/...-sesion-3 - Analysis.md` | Mid-process continuity, vocabulary continuity, identity emergence |
| `calls/sesiones-coaching-ruy/...-sesion-4 - Summary.md` | Closure anatomy, gift question, "second season" framing |
| `calls/sesiones-coaching-ruy/...-sesion-4 - Analysis.md` | Convergence pattern, complete development arc, 5-component closure |

### Other Processed Calls
| File | Key Content |
|------|------------|
| `calls/application-coaching/...richi and ruy - Summary.md` | Live coaching demo, "moments of truth," "ayúdame a ayudarte" |
| `calls/application-coaching/...horacio and ruy 22jan - Summary.md` | HPT process, Western Union case |
| `calls/cont explicación coaching : htp horacio 27ene2026 - Summary.md` | Western Union PPT walkthrough, equalization, modality boundaries |
| `calls/strategy/...Nelson 27ene2026 - Summary.md` | Memory paradigms, torch model |

### Missing (No Recording)
- **Setup session** — Dec 17, 2025 (Ruy to reconstruct + validate with Horacio)

### Chatbot Design + Platform Assets
| Asset | Status |
|-------|--------|
| Chatbot Design Process (6-phase) | Available — not yet applied to AI Coach |
| Thinking Partner chatbot | Working — potential base for Session N prompt |
| CB Assessment Debrief | Exists on platform |
| Daily Companion FRD | Designed (`sprints/daily-companion-cyclic-flow-frd.md`) |

---

*Next step: Phase B — Ruy reconstructs setup session (Dec 17) + Phase E — Draft Doc A skeleton (can start with available material)*
