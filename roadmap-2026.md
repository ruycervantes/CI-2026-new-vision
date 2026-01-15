# 2026 Roadmap - Conscious Insights v2

> **Last updated:** January 2026
> **Purpose:** Align team on what we build and when. Guide sales conversations with Leo.

---

## Strategic Context

### The Bet

We are going to own the behavior change cycle - not just offer a coaching chatbot.

> "Si nos quedamos como 'tenemos un chatbot de coaching', competimos con todos. Si nos posicionamos como 'somos dueños del ciclo de cambio de comportamiento', es otra conversación."

### What Creates the Moat

- **Complete behavior change methodology** - grounded in research
- **System that orchestrates the full cycle** - goals, habits, adjustments, evolution
- **Integrations that create stickiness** - reach users where they are
- **Accumulated knowledge** - what interventions work, when, how
- **Structured memory of user's trajectory** - not just chat history, but a model of growth

### Phased Approach

| Phase | Focus |
|-------|-------|
| **Q1 2026** | Prove coaching works - multi-session Coach + cyclic Daily Companion |
| **Q2 2026** | Daily practice + feedback - transcript analysis, touchpoints, context |
| **H2 2026** | Full experience - GPS dashboard, real-time feedback, deep integrations |

---

## Q1 2026: Prove Coaching Works

**Goal:** Deliver a sellable Application Coaching experience. Prove the multi-session Coach + cyclic Daily Companion combination drives behavior change.

### Core Features

| Feature | Owner | Status | Description |
|---------|-------|--------|-------------|
| **MS Teams Notifications** | Mike | In progress | One-way notifications. Foundation for everything. |
| **Coach Multi-Session** | Shamil | Needs Horacio | Coaching across sessions with memory. Tracks goals, progress, what's urgent vs planned. |
| **Daily Companion Cyclic Flow** | Shamil | Ready to build | Loop instead of end. User can continue, modify habit, or go to Coach. |
| **Voice OR Bidirectional Chatbot** | TBD | Validate with Leo | Choose one based on customer pull. |

### Coach Multi-Session Details

**The shift:**
- Current: Conversations are linear, no memory across sessions
- Q1: Coach remembers what you're working on

**Session flow:**
- Session 1: Establish goals (Destination → Management → Tracking), understand the gap
- Session 2+: "¿Traes algo o quieres empezar por lo que habíamos dicho?"
- System tracks: goals, progress, what's urgent vs planned

**Technical approach:**
- Store goals as structured JSON (Goal Hierarchy)
- User facts with timestamps for trajectory
- Evolve to more sophisticated memory later if needed

**Blocked by:** Horacio methodology meeting (this week)

### Daily Companion Cyclic Flow

**Current (linear):**
```
Microhabit → Follow-up → Check-in → [END]
```

**Q1 (cyclic):**
```
Microhabit → Follow-up → Check-in → [Continue / Modify / Go to Coach] → Loop
```

**What's included:**
- Loop back after check-in (don't end)
- Modify habit option (adjust without starting over)
- User-initiated Coach handoff ("I'm stuck")

**Possible if methodology is clear:**
- System-suggested Coach triggers (LLM detects patterns in check-in history)

**NOT included:**
- Complex pattern detection logic
- Adaptive reminder timing

### Voice vs Bidirectional Chatbot

**Option A: Voice**
- Ship STT (already built)
- Add TTS "play" button
- Later: full voice-to-voice

**Option B: Bidirectional Teams Chatbot**
- Check-ins via Teams bot
- Schedule next session via chat
- Later: richer bot interactions

**Decision:** Leo validates with customers which has more pull.

### Ship What's Built

These are done, just need deployment:
- Speech-to-text (STT)
- Executive Summary
- Data features

### Smaller Items

| Item | Notes |
|------|-------|
| Calendar: Reschedule & Delete | Our internal events only, not full MS Graph |
| Auto-naming threads | Like ChatGPT - rename after a few messages |

### Q1 Success Metrics

| Metric | How to Measure |
|--------|----------------|
| Multi-cycle completion | % users completing 2+ coaching cycles |
| Interaction frequency | Before/after Teams integration |
| Goal adherence | % Tracking Goals practiced 3+ times/week |
| Sales pipeline | New opportunities from feature demos |
| Qualitative | "This helps me change" sentiment |

---

## Q2 2026: Daily Practice + Feedback

**Goal:** Tighter integration between Coach and Daily Companion. Add feedback on real practice through transcript analysis.

### Features

| Feature | Description |
|---------|-------------|
| **Call Transcript Analysis** | User shares transcript, LLM analyzes against their Tracking Goal. "You asked 2 questions before responding. Here's a moment you could have paused..." |
| **Before/After Touchpoints** | Pre-meeting: "You have a meeting with Pedro. Remember your practice." Post-meeting: "How did it go?" |
| **Calendar Read Access (MS Graph)** | Know user's schedule to enable context-aware reminders |
| **Adaptive Reminders** | Timing and frequency adjust based on user patterns |
| **Coach ↔ Daily Companion Data Flow** | Goals and progress shared between modes. Coach sees Daily Companion struggles. Daily Companion knows Coach commitments. |

### Transcript Analysis Details

**Phase 1: Manual upload**
- User uploads transcript (any source)
- Simple analysis against their active habit

**Phase 2: Teams integration**
- Pull from Teams meeting recordings
- Richer context from structured memory

### Before/During/After Framework

| Moment | Purpose | Q2 Scope |
|--------|---------|----------|
| **Before** | Prepare, gain awareness | Pre-meeting reminders based on calendar |
| **During** | Pause, offer distinctions | Not Q2 - see H2 |
| **After** | Reflect, learn | Post-meeting check-in, transcript analysis |

---

## H2 2026: Full Experience

**Goal:** Complete the vision - GPS dashboard, real-time feedback, seamless experience.

### Features

| Feature | Description | Notes |
|---------|-------------|-------|
| **GPS Dashboard** | Visual showing progress toward Destination Goal. Trajectory view: where you started, key moments, where you are. | Needs Q1+Q2 data flowing |
| **Real-Time Feedback** | "During" meeting interventions. Feedback while practicing, not just after. | Needs exploration - technically complex, privacy implications |
| **Full Context Integrations** | Deep calendar, email, potentially other sources | Privacy concerns, needs Context Manager architecture |
| **Peer Accountability** | Social goal-setting features | Research needed |
| **Seamless Mode Transitions** | Fluid Coach ↔ Daily Companion without explicit switching | Polish after foundation solid |

### Real-Time Feedback - Exploration Needed

This is a big bet requiring research:
- How to access live meeting audio/transcript?
- How to notify without being annoying?
- Privacy implications?
- What feedback is actually helpful in the moment?

Park as "needs exploration" - don't commit until researched.

---

## Dependencies

```
Q1 Foundation
├── Horacio meeting (this week) → Coach methodology
├── MS Teams Notifications (Mike) → Foundation for touchpoints
├── Coach Multi-Session (Shamil) → Core differentiator
└── Leo validation → Voice vs Bidirectional decision

Q2 Builds On Q1
├── Calendar MS Graph → Before/After touchpoints
├── Transcript analysis → Requires goals in structured memory
└── Adaptive reminders → Requires usage data from Q1

H2 Builds On Q2
├── GPS Dashboard → Needs all data flowing
└── Real-time feedback → Needs transcript analysis foundation
```

---

## What's NOT on the Roadmap

Explicitly out of scope for 2026:

| Item | Why Not |
|------|---------|
| HRMS/LMS integrations | Not validated as needed |
| Multi-language beyond EN/ES | Focus on core first |
| White-label / multi-tenant | Adds complexity, not proven needed |
| Mobile app | Web + Teams is enough for now |

---

## Open Questions

| Question | Owner | When to Resolve |
|----------|-------|-----------------|
| Voice vs Bidirectional priority | Leo | Q1 - customer validation |
| System-triggered Coach methodology | Ruy + Horacio | After Horacio meeting |
| Full calendar integration needed? | Leo | Q1 - is reschedule/delete enough? |
| Transcript analysis: manual vs Teams first? | Ruy | Q2 planning |
| Real-time feedback feasibility | Mike | H2 planning - technical research |

---

## Team Assignments

| Person | Focus |
|--------|-------|
| **Mike** | MS Teams integration, technical architecture |
| **Shamil** | Coach Multi-Session, Daily Companion cyclic flow |
| **Daniel** | Infrastructure, deployment automation |
| **Leo** | Customer validation, demo approval, sales |
| **Ruy** | Methodology, roadmap, Horacio/Dolo coordination |

---

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Horacio meeting doesn't clarify methodology | Start with "good enough" based on interview; refine iteratively |
| Users don't engage with multi-session Coach | Make sessions shorter, test with real users, iterate on prompts |
| MS Teams blocked by client IT | Fallback channels (email, web); escalate early |
| We build features that don't move PMF | Validate with Leo + customers before building |
| Transcript analysis has privacy concerns | Start with manual upload (user controls data) |

---

## Changelog

| Date | Change |
|------|--------|
| Jan 2026 | Initial version - separated Q1/Q2/H2, added transcript analysis, real-time feedback |
