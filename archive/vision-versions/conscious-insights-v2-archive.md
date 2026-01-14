# Conscious Insights - Next Evolution

---

## Context: Why This Document

The current product is at a point where we can sell it — and we should. It works, it has value, clients understand it.

But the market is changing fast. In 12-18 months there will be many generic AI coaches. Anyone with access to Claude or GPT can build a coaching chatbot with good prompting. We already saw this with Sigma: they saw us as "a chatbot" — not as owners of a change process.

If we stay where we are, we'll be just another one in the crowd.

**This document proposes a direction for evolution** so that the product is defensible in the medium term. It's not a detailed execution plan — it's a vision to discuss and align with the team.

The central question is: **Is this the right direction?**

---

## 1. The Central Thesis

We are going to own the behavior change cycle.

This means three things:

1. **A solid change methodology** — not invented, but based on what works (behavioral science, HCI, CSCW).

2. **The right interactions at the right moments** — validated by research, not intuition. The interventions that actually move people from wanting to change to changing.

3. **Stickiness through integration** — we insert ourselves into the lifecycle of activities of people who want to change. We're not an app they open when they remember; we're part of their workflow.

### Why This Matters Now

We learned with Sigma that if they see us as "a chatbot" or "an AI agent", we lose. Sigma is an advanced client, and they saw us as just another tool — not as owners of the change process.

The market is going to be full of generic AI coaches. Anyone can put a wrapper on Claude and offer "AI coaching". Building a chat is simple. Making a coach for a debrief is simple.

**What is NOT easy to replicate:**
- The complete behavior change methodology
- The system that orchestrates the entire cycle (not just a conversation)
- The integrations that create real stickiness
- The accumulated knowledge about what works to change behaviors
- The structured memory of the user's change trajectory

If Stoic positions itself as "we have an AI coach", we compete with everyone. If Stoic positions itself as "we own the behavior change cycle", it's a different conversation.

**That's what we're going to build.**

---

## 2. Pending Research and Inputs

Before making definitive decisions about the cycle, there are two sources of input to review:

### HCI Research: Longitudinal Goal Setting & Personal Informatics

There's a body of research in HCI about how people set long-term goals and track their progress. This is directly relevant to designing the microhabit cycle.

**Resource:** [NotebookLM with relevant papers](https://notebooklm.google.com/notebook/4c0920bd-9c40-4a9b-b78a-71669e46015b)

**Questions to answer:**
- What patterns work for longitudinal goal setting?
- What makes people abandon vs. persist?
- How do you design interventions that aren't annoying but are effective?
- What does research say about frequency and timing of check-ins?

**TODO:** Review this research before designing the cycle UX.

### Competitor Benchmark

There are products in the market attacking similar problems (MindGym, among others). We need to understand what they do well, what they do poorly, and where the opportunity is.

**Resource:** [Mural with products to analyze](https://app.mural.co/t/axialent8953/m/axialent8953/1764890677283/ad8559ddadff366460dab38357447aaeeeea02d1)

**Questions to answer:**
- How do they handle the behavior change cycle?
- What integrations do they have?
- Where are their users' complaints?
- What can we do better?

**TODO:** Do a thorough benchmark of these products.

---

## 3. The Hypotheses We're Betting On

These are bets, not facts. They need to be validated:

1. **Iterative cycle hypothesis:** If we allow the user to repeat the microhabit cycle (follow-up → adjustment) multiple times before changing focus area, adherence will be higher than the current one-time flow.

2. **Conversational follow-up hypothesis:** If the weekly check-in is a short conversation with the LLM instead of a form, engagement will be higher.

3. **Adaptive reminders hypothesis:** If reminders adapt to the user (timing, channel, frequency), "treatment" adherence will increase significantly.

4. **Connected goals hypothesis:** If we connect development goals with the user's real motivations ("to be liked more", "to have more impact"), the user will be more committed to the process.

5. **Workflow integration hypothesis:** If we reach the user where they already are (MS Teams, calendar, email) instead of waiting for them to come to us, interaction frequency will be higher.

6. **Context hypothesis:** If the system has access to real user context (meetings, calendar, emails), interventions will be more relevant and useful.

---

## 4. The Change Model

### The Two Levers

For people to change, there are two levers:

**Lever 1: Transform consciousness (the mindset)**
Gain perspective, understand patterns, see what you couldn't see. Move from victim/knower/fixed to player/learner/growth. This is done through coaching — conversations that help you see differently.

**Lever 2: Act based on that mindset**
Do the things, practice. Turn insights into concrete behaviors. This is done through microhabits, daily practice, follow-up.

**The key is that the two levers feed each other:**
- Coaching gives you awareness → concrete actions come from there
- Practice gives you experiences → setbacks shake you up → by processing them in coaching, you move to another level of consciousness

### The Integrated System: Thinking Partner + Accountability Partner

Today we have two separate "bots". The evolution is to integrate them as two modes of the same change system:

```
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│  THINKING PARTNER                 ACCOUNTABILITY PARTNER       │
│  (Lever 1: Consciousness)         (Lever 2: Action)            │
│                                                                │
│  • Exec coaching sessions         • Concrete microhabits       │
│    based on Conscious Business    • Daily practice             │
│  • Gain perspective               • Check-ins and follow-up    │
│  • Process setbacks               • Adjustments based on       │
│  • Understand the gap               experience                 │
│                                                                │
│           │                              │                     │
│           │      CONCRETE ACTIONS       │                     │
│           └──────────────────►──────────┘                     │
│                                                                │
│           ┌──────────────────◄──────────┐                     │
│           │      EXPERIENCES            │                     │
│           │      (successes, setbacks)  │                     │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

**The Thinking Partner:**
- Gives you complete exec coaching sessions based on Conscious Business
- Helps you understand the gap between who you want to be and who you are
- When you have a setback, you process it here and gain awareness
- From each session come **concrete actions** that feed the Accountability Partner

**The Accountability Partner:**
- Takes the concrete actions and turns them into actionable microhabits
- Accompanies you in daily practice
- Does follow-up and adjustment
- Generates **experiences** (successes and failures) that feed the next coaching session

### Thinking Partner Triggers

- **Periodic:** Every X time, a coaching session to gain perspective
- **On-demand:** When the user has something urgent to process
- **System-suggested:** When the Accountability Partner detects patterns (e.g., "You haven't done the check-in for 3 weeks. What's going on?") — this isn't a reminder, it's an invitation to a coaching session

### The Gap is Dynamic

The gap between "who I want to be" and "who I am" isn't defined once and then closed. It's dynamic:

1. **It's seen initially in onboarding** — a first snapshot of where you are
2. **It reveals itself day by day** — you discover new aspects, new challenges, things you hadn't seen
3. **Setbacks shake you up** — and by processing them in coaching, you gain awareness, you move to another level

The system has to capture this **trajectory**, not just a state. It's not "Juan has gap X that he's closing". It's "Juan started here, went through this, had this setback, gained this awareness, is now here".

### The Three Intervention Moments

In addition to the two levers, there are three moments where the system can intervene:

| Moment | Purpose | Examples |
|--------|---------|----------|
| **BEFORE** | Gain awareness, prepare | Analyze, plan, prepare for a difficult conversation |
| **DURING** | Pause, see, offer distinctions | In-the-moment interventions to "clarify", "stop", bring awareness |
| **AFTER** | Reflect, measure, learn | Feedback on how it went, talk about what happened, process setbacks |

---

## 5. Juan's Journey

Juan is a leader at a client company. He wants to be a better leader, but more specifically: he wants his team to like him more and wants to have more impact.

### Stage 1: Juan establishes his goal

Juan enters Conscious Insights. Instead of just saying "I want to be a better leader", the system helps him connect with what really matters to him:

- "I want my employees to like me"
- "I want to have more impact"

These real motivations are saved and connected to everything that follows.

**What Juan sees:** A dashboard where his development goals are connected to his motivations.

### Stage 2: Juan does the assessment and debrief

Juan does the assessment to know himself. The debrief with the coach works well — we already have this.

**What already works:** Assessment → Debrief

### Stage 3: Juan enters the microhabit cycle

Based on the debrief, Juan chooses a microhabit to work on. For example: "Before responding in a meeting, I'll pause for 3 seconds."

**The current cycle (works 1 time):**
```
Assessment → Debrief → Microhabit → Follow-up → Check-in → [end]
```

**The new cycle (works N times):**
```
Assessment → Debrief → [Microhabit → Follow-up → Adjustment] × N times
                                       ↓
                         Change microhabit or focus area
```

**The weekly follow-up:** Instead of a form, Juan has a short conversation with the LLM. "How did it go this week with the 3-second pause?" — conversational, with managed turns, short.

**Options after each cycle:**
1. Continue with the same microhabit (adjusting)
2. Change to another microhabit within the same area
3. Change focus area completely

**What Juan sees:** His progress, his achievements, his change trajectory.

### Stage 4: The system accompanies Juan in his daily life

A typical day for Juan:

| Time | Juan does... | The system can... |
|------|--------------|-------------------|
| 8:00 | Arrives, checks email | Suggestions on how to approach something in a difficult email |
| 9:00 | Reviews calendar | Reminder: "You have a meeting with Pedro. Remember your 3-second pause." |
| 10:00 | Meeting in MS Teams | (During) Intervention if technically possible |
| 11:00 | Finishes meeting | "How did it go? Were you able to apply the pause?" |
| 14:00 | Prepares presentation | Help preparing a difficult conversation he's going to have |
| 16:00 | Urgent call with the team | — |
| 17:00 | Closes the day | Brief reflection on the day |

**Where Juan lives (channels):**
- MS Teams (messages and meetings)
- Email
- Calendar

Reminders arrive where Juan already is, not in a separate app he has to open.

### Stage 5: Juan achieves sustained change

After several weeks/months:
- Juan has iterated through several microhabits
- Has changed focus area when he mastered one
- Can see his change trajectory
- His team notices the difference

**The formula:** Want to be → Be

---

## 6. The Architecture

### Current State

Today we have:
- Two separate bots (Thinking Partner and Accountability Partner)
- Same infrastructure
- Same user memory
- But not integrated at the UX level

### What we need for the integrated cycle

```
┌─────────────────────────────────────────────────────────────┐
│                     INTEGRATED UX LAYER                     │
│         (One system from the user's perspective)            │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│              THINKING PARTNER + ACCOUNTABILITY PARTNER      │
│                    (Two modes of the same system)           │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  STRUCTURED MEMORY                          │
│              (The user's change trajectory)                 │
│                                                             │
│   • Where you started (initial assessment, initial gap)     │
│   • What you've worked on (microhabits, coaching sessions)  │
│   • Key moments (setbacks, insights, consciousness leaps)   │
│   • Where you are now                                       │
│                                                             │
│   Possibly: Graphiti or similar to organize better          │
│   (Mike is exploring this)                                  │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    CONTEXT MANAGER                          │
│        (Pulls information from the user's world)            │
└─────────────────────────┬───────────────────────────────────┘
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
     ┌─────────┐    ┌─────────┐     ┌─────────┐
     │MS Teams │    │Calendar │     │ Email   │
     └─────────┘    └─────────┘     └─────────┘
```

### Structured Memory: Why It Matters

Memory is not just "remembering what we talked about". It's a **model of the user in their change process**.

It has to capture:

1. **The starting point:** Initial assessment, initial gap between wanting to be and being
2. **The trajectory:** What microhabits they've worked on, what coaching sessions they've had, what concrete actions have come out
3. **Key moments:** Setbacks that shook them up, important insights, consciousness leaps
4. **Current state:** Where they are now in their change process

This allows the system to:
- Know when to suggest a Thinking Partner session (not just wait for the user to ask)
- Connect what happens in the Accountability Partner with what's worked on in the Thinking Partner
- Show the user their own change trajectory
- Learn what works for this specific user

**Technical note:** Mike is exploring whether we need something like Graphiti to organize this memory better. The current memory is flat; we need something that captures relationships and trajectory.

### Integrations (for stickiness)

To reach the user where they already are:

**Critical for MVP:**
- MS Teams (where they have meetings and messages) — Mike is already working on this
- Calendar (to know when to intervene)

**Future:**
- Email
- HRMS / LMS
- Meeting recordings

---

## 7. Prioritized Features

### Priority 1: The Accountability Partner iterative cycle

**What it is:** Allow the user to repeat the microhabit → follow-up → adjustment cycle multiple times, and then change focus area.

**Why first:** It's the product core. Without this, we only work once.

**Dependencies:** None external. It's product logic + UX design.

### Priority 2: Conversational follow-up

**What it is:** Redesign the weekly check-in to be a conversation with the LLM, not a form.

**Why:** Hypothesis that it increases engagement.

**Dependencies:** The iterative cycle (Priority 1).

### Priority 3: MS Teams integration

**What it is:** Being able to send reminders and receive responses through MS Teams.

**Why:** To reach the user where they already are.

**Dependencies:** Mike is already working on this. The admin panel needs to be modified.

### Priority 4: Thinking Partner ↔ Accountability Partner integration

**What it is:** Having the concrete actions from a Thinking Partner session automatically feed the Accountability Partner. Having the Accountability Partner experiences inform Thinking Partner sessions.

**Why:** It's what turns two separate features into an integrated change cycle.

**Dependencies:** Iterative cycle (Priority 1), possibly structured memory.

### Priority 5: Structured memory (change trajectory)

**What it is:** A layer that organizes user memory to capture their change trajectory: starting point, microhabits worked on, key moments, current state.

**Why:** Allows the system to be intelligent about when and how to intervene. It's what makes us not be "just a chatbot".

**Dependencies:** Mike is exploring options (Graphiti or similar). Needs technical research.

### Priority 6: Adaptive reminders

**What it is:** Reminders that adjust in timing, frequency, and channel according to the user.

**Why:** Hypothesis that adaptation increases adherence.

**Dependencies:** MS Teams integration (Priority 3) and/or calendar.

### Priority 7: Goals and progress dashboard

**What it is:** Frontend where the user sees their goals, achievements, change trajectory.

**Why:** Makes progress visible, connects motivations with actions.

**Dependencies:** The iterative cycle (Priority 1) and structured memory (Priority 5) to have data to show.

### Future (not now)

- Advanced integrations (HRMS, LMS, recordings)
- "During" meeting interventions
- Context Manager connected to multiple company agents
- Intelligent Thinking Partner triggers based on Accountability Partner patterns

---

## 8. Open Questions That Block

### Question 1: What context is really necessary?

We can connect to many things (calendar, email, Teams, HRMS, LMS, recordings...). But what information really moves the needle for coaching?

**Risk:** Building integrations that don't add value.

**How to resolve:** Start with Model A (ask the user) and see what context we actually use before building integrations.

### Question 2: How do we measure success?

What metrics tell us that the iterative cycle is working better than the current one?

**Options:**
- % of users who complete more than 1 cycle
- Weekly interaction frequency
- Net Promoter Score
- Qualitative feedback

**Needs decision before:** Launching the iterative cycle.

### Question 3: What have clients said?

Have TELUS, P&G, Sigma expressed these problems we're solving? Or are we assuming?

**Risk:** Building something that doesn't respond to real needs.

**How to resolve:** Review existing feedback and/or have specific conversations.

---

## 9. Next Steps

### This week

**Ruy:**
- [ ] Review HCI research (NotebookLM) — look for longitudinal goal setting patterns relevant to the cycle
- [ ] Do competitor benchmark (Mural) — understand what MindGym and others do
- [ ] Design the iterative cycle UX (informed by research and benchmark)
- [ ] Prototype the cycle (after having the UX resolved)

**Mike:**
- [ ] Continue with MS Teams
- [ ] Modify admin panel to create official workflow
- [ ] Make effective in Reflex

**Shamil:**
- [ ] Build the conversational check-in (microhabit follow-up)
  - Conversation with the LLM instead of form
  - Short, with managed turns
  - Can advance in parallel while Ruy resolves the cycle UX

### Dependencies

```
HCI Research + Benchmark
         ↓
   Cycle UX Design (Ruy)
         ↓
   Cycle Prototype (Ruy)
         ↓
   Larger tasks for the team

Conversational check-in (Shamil) ← Can advance in parallel
MS Teams (Mike) ← Can advance in parallel
```

### Main blocker

The iterative cycle UX is not resolved. Before resolving it, the HCI research needs to be reviewed to not reinvent the wheel. Once the UX is clear, larger tasks can be created for Shamil and the rest of the team.

---

## Footnotes

### On Activity Theory

There's a theoretical framework of Activity Theory that could inform how we think about change:

- The relationship between Being → Doing
- The movement from Activity → Action → Operation
- The concept of "Ascending to the Concrete"

This requires more study to understand how to apply it. For now it's a reference to explore, not a product foundation.

### The personal analogy

This system is similar to how I (Ruy) work:
- Horacio as my coach (high-level reflections)
- Claude/ChatGPT for thinking and planning
- Context from multiple sources (transcripts, notes, emails)
- All grounded in day-to-day workflows (Todoist, calendar)

The vision is to give something similar to Conscious Insights users.

---

## Questions for Oseas and Team

This document proposes a direction. Before executing, we need to align:

### On strategic direction

1. **Do we agree that "owning the behavior change cycle" is the right direction?**
   - Or is there another direction we should consider?
   - What risks do you see in this bet?

2. **How aggressive do we want to be in evolution vs. continuing to sell the current product?**
   - How much of development effort goes to evolution vs. stabilizing/selling what we have?
   - What's the right balance given runway and sales opportunities?

### On the integrated model

3. **Does the Thinking Partner + Accountability Partner model as two modes of the same cycle make sense?**
   - Or should they remain separate products?
   - What implications does this have for how we sell it?

4. **Is structured memory (change trajectory) a real priority or a nice-to-have?**
   - How much do we invest in this vs. in more client-visible features?

### On execution

5. **Is the implicit timeline realistic?**
   - Review research → design UX → prototype → build
   - What trade-offs need to be made?

6. **What feedback do you have on feature priorities?**
   - Is something mis-prioritized?
   - Is something critical missing?

---

**Next step:** Review this document together and make decisions on the direction.
