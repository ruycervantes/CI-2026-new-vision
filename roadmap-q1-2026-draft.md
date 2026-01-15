# Q1 2026 Roadmap - Conscious Insights v2

> **STATUS: FIRST DRAFT** - Needs vision document review before finalizing.
> **Purpose:** Help sell / validate with customers and Leo.

Based on meeting with Mike (Jan 13, 2026).

---

## Strategic Context: Why These Features

### Phased Approach to the Vision

The vision document describes the **end state** - full Coach + Daily Companion integration, GPS dashboard, seamless flow of work. We get there in phases:

| Phase | When | Focus |
|-------|------|-------|
| **Phase 1** | Q1 2026 | Multi-session coaching + basic notifications → sellable Application Coaching v1 |
| **Phase 2** | Q2 2026 | Tighter Coach ↔ Daily Companion integration, more touchpoints, flow of work |
| **Phase 3** | Future | Full GPS dashboard, deep context integrations, seamless mode transitions |

**Q1 is about proving the coaching sessions work and can be sold.**

---

### The Opportunity: Application Coaching Programs

We can increase sales by offering **Application Coaching** as part of programs we sell - similar to what Axialent does with their learning programs. Instead of just selling chatbots, we sell coaching programs that include:
- Live sessions (existing)
- **AI-powered application coaching sessions** (new)
- Accountability and practice support

This is a sellable product, not just a feature.

### The Core: Thinking Partner → Multi-Session Coach

The Thinking Partner becomes a **coach across multiple sessions over several weeks**:
- Session 1: Establish goals, understand the gap
- Session 2+: Review progress, work through challenges, adjust goals
- Ongoing: Help the person resolve their gap across time

This is what makes us "dueños del ciclo de cambio de comportamiento" (owners of the behavior change cycle) - not just another chatbot.

### Methodology Work Required

To build this right, Ruy needs to work with:
- **Horacio** - coaching methodology, note-taking approach
- **Dolo** - alignment with Axialent programs (Application Coaching)
- **Maybe Richi** - additional methodology input

**Key questions to resolve:**

| Question | Why It Matters |
|----------|----------------|
| How do Coach sessions and Daily Companion merge? | Core integration - what's the handoff? |
| What happens in Session 1 vs Session 2 vs Session 3? | Multi-session flow design |
| What data flows from Coach → Daily Companion? | Goals? Habits? Commitments? |
| What data flows from Daily Companion → Coach? | Progress? Struggles? Patterns? |
| What's the rhythm? Weekly? Bi-weekly? User-driven? | Cadence design |
| Is Axialent's Application Coaching the right model? | Or do we adapt it? |

The methodology must align with **goal setting theory** (from HCI research).

### Why This Creates a Moat

> "Si nos quedamos como 'tenemos un chatbot de coaching', competimos con todos. Si nos posicionamos como 'somos dueños del ciclo de cambio de comportamiento', es otra conversación."

Once we have:
- Multi-session memory (accumulated context)
- Goal tracking across weeks/months
- Integration into daily workflow (Teams)

...users can't easily leave. The system knows their goals, their progress, their patterns.

---

## Product Framework from Vision

These concepts from the vision document inform how we build Q1 features.

### The Change Process (4 Stages)

| Stage | Mode | What Happens |
|-------|------|--------------|
| **Know Yourself** | Coach | Assessment + Debrief → understand your patterns |
| **Set Intrinsic Goals** | Coach | Powerful conversation → OWNED goals (not assigned) |
| **Connect to Action** | Coach → Daily Companion | Create If-Then habit, handoff for execution |
| **Daily Practice** | Daily Companion | Reminders, check-ins, GPS updates |

**For Q1:** Multi-session coaching must support stages 1-3. Daily Companion (via Teams notifications) supports stage 4.

### Goal Hierarchy (3 Levels)

| Level | What It Is | Example (Juan) |
|-------|------------|----------------|
| **Destination Goal** | Extrinsic outcome user wants | Get promoted to Team Lead |
| **Management Goal** | Intrinsic mindset shift needed | Be a leader who listens |
| **Tracking Goal** | Specific microhabit practiced daily | "If I want to prove I'm right → Ask a question first" |

**For Q1:** Coach must help users set all 3 levels. Memory must store and track them. Daily Companion references Tracking Goals.

### The Adjust Stage (Key Differentiator)

When users fail, most systems just track the failure. That doesn't help.

| Don't | Do |
|-------|-----|
| Track failure ("You missed 3 days") | Reinterpret ("What got in the way?") |
| Nag ("Remember your habit!") | Anticipate barriers ("Tough week ahead. Let's plan.") |
| Create guilt | Help learn a new skill or approach |

**For Q1:** When Daily Companion detects a pattern (missed days, negative sentiment), it triggers Coach mode — not to guilt, but to help adapt.

### Mode Activation Triggers

| Trigger Type | When It Happens | Example |
|--------------|-----------------|---------|
| **Periodic** | Scheduled by system | Weekly coaching check-in |
| **On-demand** | User-initiated | "I need to talk through something" |
| **System-suggested** | Pattern detected | "You've struggled for 2 weeks. Let's talk." |

**For Q1:** Focus on periodic (scheduled sessions) and on-demand (user opens Coach). System-suggested is Phase 2+.

### The Dynamic Gap

The gap between "who I am" and "who I want to be" reveals itself day by day — it doesn't stay static. Setbacks shake you up; each reveals another level of consciousness.

**For Q1:** Coach sessions must revisit and update the gap based on what's happened since last session.

---

## Q1 Features Overview

### Tier 1: Definite (Build These)

| Feature | Owner | Details |
|---------|-------|---------|
| **MS Teams Notifications** | Mike | In progress. Foundation for everything. |
| **Thinking Partner Multi-Session** | Shamil + Ruy | Coaching across sessions with memory. Key differentiator. |

### Tier 2: Smaller/Quick Wins

| Feature | Owner | Details |
|---------|-------|---------|
| **Calendar: Reschedule & Delete** | TBD | Our internal events only. Not full MS Graph (validate first). |
| **Auto-naming threads** | Shamil? | Like ChatGPT - rename after a few messages. Low effort. |
| **Ship STT** | - | Already built, just needs shipping. |
| **Ship Executive Summary** | - | Already built, not in demo. |

### Tier 3: Choose One (Validate with Customers)

| Option A: Voice | Option B: Bidirectional Chatbot |
|-----------------|--------------------------------|
| Ship STT (ready) | Check-ins via Teams bot |
| Add TTS "play" button | Schedule next session via chat |
| → Later: full voice-to-voice | → Later: richer bot interactions |

**Decision needed:** Validate with Leo which has more customer pull.

### Tier 4: Needs Validation (Maybe Not Q1)

- Full calendar integration via MS Graph (read user's calendar)
- Outlook/email integration (privacy concerns, needs context manager first)

---

## Feature Details

### 1. MS Teams Notifications

**Status:** In progress with Mike

**Scope for Q1:**
- One-way notifications working reliably
- Foundation for future bidirectional chatbot

**Future phases:**
1. Phase 1: One-way notifications ← **Q1**
2. Phase 2: Bidirectional chatbot (check-ins, scheduling)
3. Phase 3: Meeting interventions (technically feasible but later)

---

### 2. Thinking Partner Multi-Session Coaching

**Owner:** Shamil (dev) + Ruy (methodology)

**The Problem:**
- Current: conversations are linear, no memory across sessions
- Need: coach that remembers what you're working on

**The Solution:**
- Session 1: Establish goals, define gap
- Session 2+: "¿Traes algo o quieres empezar por lo que habíamos dicho?"
- System tracks: goals, progress, what's urgent vs planned

**Technical Approach (from Mike):**
- Start with **user facts + dates** (simple, already exists)
- Can add timestamp to facts: "hace un mes estabas trabajando en X"
- Store goals as structured JSON in existing tables
- Evolve to Graphiti later if needed

**Key insight:** "No es tanto un problema de qué memoria utilizas... es más bien cómo lo guardas y cómo lo prompteas para que funcione como me está funcionando una sesión de coach."

**Methodology needs (from Horacio):**
- How does he take notes?
- What does he track session-to-session?
- How does he handle goal evolution?
- Get photos of his notebook

**Small UX fixes needed:**
- Challenges table: ask user to confirm ("¿esta es tu challenge?")
- Goals table: similar confirmation flow
- Thread auto-naming

**Blocked by:** Horacio interview

---

### 3. Calendar: Reschedule & Delete

**Scope for Q1:**
- Allow users to reschedule/delete their CI events (reminders, sessions)
- NOT full MS Graph calendar integration

**Validation needed:**
- Do we need to read user's external calendar?
- Or is managing our own events enough for now?

---

### 4. Voice Features (Phased)

**Q1 Scope:**
- Ship STT (speech-to-text) - already built
- Add TTS "play" button - simple hack, Leo's idea
- Keep Claude as LLM, send output to 11Labs for speech

**Future (post-Q1):**
- Full voice-to-voice conversation mode
- Decide what to say vs show on screen

---

### 5. Bidirectional Teams Chatbot (Alternative to Voice)

**If validated over voice:**
- Check-ins happen via Teams bot, not app
- "¿Cómo te fue esta semana?" "5 de 5" "¿Necesitas ajuste?"
- Schedule next session via chat
- Emergency coaching triggers

**Why it matters:** Removes friction - people already in Teams

---

## Process Improvements (Also Q1)

### Testing → Demo → Ship Flow

| Stage | Owner | Action |
|-------|-------|--------|
| Staging | Dev team | Feature lands here after dev |
| Testing | QA (Asana team) | Verify it works |
| Demo approval | **Leonardo** | Green flag for demos |
| Production | Daniel | Deploy script (to be automated) |

**Problem:** "Lo que pasa es que ya está listo... pero no lo hemos shipped. Entonces es como si no estuviera."

**Already built but not shipped:**
- Executive summary
- Text-to-speech
- Speech-to-text
- Data features

---

### Deployment Automation

**Owner:** Daniel

**Goal:** Stop spending "mañanas enteras" on client setup

**Task:** Complete the deployment/install script that's been pending

**Why now:** PG client delayed to May, good window to finish this

---

### Team Leadership Transition

**Agreed with Mike:**
- Mike takes more day-to-day dev leadership
- Mike can assign urgent tasks to Daniel/Shamil outside sprint
- Daily standups for Daniel, Shamil (visibility)
- Ruy focuses on prototyping, methodology, customer validation

**Sprint planning:** Ruy + Mike do prep work, come "planchados" to planning

---

### Feature Flags by Client

Some features can be activated/deactivated per client:
- Microhabits (with cyclic adjustment)
- Coaching sessions
- Voice features
- Different configurations for different contracts

---

## OKRs Structure

### Objective 1: More Complete Coaching Experience
**Key Results:**
- Deliver 3 major features with user validation criteria
- Features installed with some users for testing

### Objective 2: Product-Market Fit Process
**Key Results:**
- Validation process established with Leo
- 3 new pipeline opportunities from feature demos
- Customer validation before building (vs last year)

---

## Sellable Package for Q1

**Application Coaching Programs** (like Axialent model):
- Learning program + AI coaching sessions embedded
- Thinking Partner as multi-session coach (not just chatbot)
- Could replace or complement current Mindsets chatbots
- Notifications via Teams for accountability
- **This is a product to sell, not just a feature**

**What we're NOT selling:** "We have a coaching chatbot" (everyone has that)
**What we ARE selling:** "We own the behavior change cycle" (methodology + orchestration + memory)

---

## Hypotheses to Test in Q1

These are bets, not facts. Q1 validates them.

| Hypothesis | What We Believe | How to Validate |
|------------|-----------------|-----------------|
| **Iterative cycle** | Multiple adjust iterations over months → more change than one-shot goal | Track users who complete 2+ Coach cycles vs 1 |
| **Conversational follow-up** | Conversation beats forms → better intrinsic motivation | Compare engagement: structured survey vs Coach conversation |
| **Connected goals** | Daily actions visibly connected to Destination Goal → longer persistence | Measure drop-off with/without GPS-style progress view |
| **Workflow integration** | Reach users where they are (Teams) → higher interaction frequency | Compare interaction rates: app-only vs Teams notifications |
| **Coach-triggered** | System suggests Coach mode when patterns emerge → more breakthroughs | Track outcomes when system-suggested vs user-initiated |
| **Intrinsic > assigned** | Goals from powerful conversation → more commitment than assessment-assigned | Compare goal adherence by source |

---

## Q1 Success Metrics

| Metric | Target | How to Measure |
|--------|--------|----------------|
| **Multi-cycle completion** | % users completing 2+ coaching cycles | Track in system |
| **Interaction frequency** | Increase over baseline | Compare before/after Teams integration |
| **Goal adherence** | % of Tracking Goals practiced 3+ times/week | Daily Companion check-in data |
| **NPS** | Baseline + improvement | Survey at end of Q1 |
| **Qualitative feedback** | "This helps me change" sentiment | User interviews |
| **Sales pipeline** | 3 new opportunities from feature demos | Leo tracking |

---

## Phase 2 Preview (Q2 2026)

After Q1, the focus shifts to tighter Coach ↔ Daily Companion integration:

- **More touchpoints** - calendar integration, more apps
- **Easier progress tracking** - visible connection between daily actions and goals
- **Flow of work** - not a separate app to open, but embedded where users work
- **Iterative additions** - each quarter adds more companionship touchpoints

**Before/During/After Framework** (from earlier vision work):
| Moment | Purpose | Examples |
|--------|---------|----------|
| **Before** | Prepare, gain awareness | "You have a meeting with Pedro. Remember your practice." |
| **During** | Pause, offer distinctions | In-meeting interventions (future, technically complex) |
| **After** | Reflect, learn | "How did it go? Were you able to apply it?" |

This builds toward the full vision (GPS dashboard, seamless mode transitions).

---

## Architecture Direction (Long-term Context)

Not Q1, but informs decisions:
- API needs to be bidirectional
- Chainlit is one part, but needs more structure
- Context manager to orchestrate everything
- Can't rewrite - must evolve while selling
- Once architecture solid, integrations become "plugins" (externalizable)

---

## Vision Document Updates Needed

Once methodology work is done, update `conscious-insights-v2-english.md`:

| Section | Update Needed | Blocked By |
|---------|---------------|------------|
| Section 9 (Q1 features) | Align with this roadmap | Roadmap finalization |
| Multi-session coaching | Describe session 1 → 2 → 3 flow | Horacio/Dolo methodology work |
| Coach ↔ Daily Companion | Show data flow between modes | Methodology work |
| Before/During/After | Consider adding this framework | Phase 2 planning |
| Glossary | Add "Application Coaching" term | Methodology finalization |

**Keep vision and roadmap in sync** - roadmap is the execution plan, vision is the destination.

---

## Dependencies & Blockers

| Item | Blocked By | Resolution |
|------|------------|------------|
| Multi-session coaching methodology | Horacio, Dolo, maybe Richi | Ruy to coordinate - align with goal setting theory |
| Voice vs Chatbot priority | Customer validation | Leo to run validation |
| Graph memory decision | Technical prototype | Mike explore with facts+dates first |
| Thinking Partner ship | Methodology + Horacio testing | After methodology work |
| Application Coaching packaging | Methodology definition | How to sell this as a program |

### Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Users don't engage with goal-setting conversation | Make it shorter, test with real users, iterate on prompts |
| Coach mode feels like "more work" | Position as help, not homework; make it genuinely valuable |
| MS Teams integration blocked by IT | Have fallback channels (email, web); escalate early with IT contacts |
| We build features that don't move PMF | Validate with Leo + customers before building; kill features that don't resonate |
| Methodology work takes too long | Start with "good enough" based on Horacio interview; refine iteratively |
| Memory architecture doesn't scale | Start simple (facts+dates), prove value first, evolve to Graphiti later |

---

## Sprint Planning (Thursday) - Tasks

| Person | Task |
|--------|------|
| Shamil | Thinking Partner: Extract goal/gap feature |
| Daniel | Complete deployment/install automation script |
| Daniel | Review/check sprint items (explicit) |
| Leonardo | Own testing → demo approval flow |
| Mike | Continue MS Teams notifications |
| Mike | Prototype facts+dates memory |

---

## Validation Questions for Leo

1. Would customers buy "application coaching" sessions?
2. Voice (STT + TTS play button) vs Bidirectional Teams chatbot - which first?
3. Full calendar integration - is it needed or is reschedule/delete enough?

---

## Summary: What to Build Q1

```
DEFINITE:
├── MS Teams Notifications (Mike)
├── Thinking Partner Multi-Session (Shamil + methodology)
├── Calendar Reschedule/Delete (small)
└── Ship what's built (STT, Exec Summary, Data features)

CHOOSE ONE (validate):
├── Option A: TTS play button → later voice-to-voice
└── Option B: Bidirectional Teams chatbot

PROCESS:
├── Testing → Demo flow (Leo owns approval)
├── Deployment automation (Daniel)
└── Mike leads day-to-day dev
```
