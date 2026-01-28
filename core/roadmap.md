# 2026 Roadmap - Conscious Insights v2

> **Purpose:** What we build and when. Guide sales conversations with Leo.
> **See also:** [vision.md](vision.md) for methodology, [alignment.md](alignment.md) for leadership sign-off
> **Last updated:** January 2026

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
| **Q2 2026** | Daily practice + feedback - GPS dashboard, transcript analysis, touchpoints |
| **H2 2026** | Full experience - real-time feedback, deep integrations, peer features |

---

## Q1 2026: Prove Coaching Works

**Goal:** Deliver a sellable Application Coaching experience. Prove the multi-session Coach + cyclic Daily Companion combination drives behavior change.

### Core Features

| Feature | Owner | Status | Description |
|---------|-------|--------|-------------|
| **MS Teams Notifications** | Mike | In progress | One-way notifications. Foundation for everything. |
| **Daily Companion Cyclic Flow** | Shamil | Ready to build | Loop instead of end. User can continue, modify habit, or go to Coach. |
| **Thinking Partner: Challenge/Gap/Commitment** | Shamil + Ruy | Ready to build | Small feature: show and store challenge, gap, action plan commitment. Foundation for multi-session. |
| **Coach Multi-Session** | Ruy (design) + Shamil (impl) | Needs Horacio | Coaching across sessions with memory. Tracks goals, progress, what's urgent vs planned. |
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

### Q1 Validation Experiment

Q1 is about proving the thesis, not measuring at scale. We run a structured pilot to validate utility and approach.

**The Experiment**

| Aspect | Details |
|--------|---------|
| **Users** | Mix of friendly clients, Leo's pipeline, internal (TBD) |
| **Owner** | Ruy in collaboration with Leo |
| **Duration** | 2-3 weeks |
| **Goal** | Validate utility and approach, not behavior change outcomes |

**What we're validating:**

| Principle | How We Test It |
|-----------|----------------|
| Multi-session Coach feels like a coach who knows you | Do users reference previous sessions? Do they feel continuity? |
| Cyclic Daily Companion keeps people engaged | Do users loop? Do they modify habits when stuck? |
| "Don't nag, give alternatives" works | When users struggle, do they feel supported vs. guilty? |
| Connected goals matter | Do users see how daily actions connect to what they want? |

**Signals we're looking for:**

| Signal | Question |
|--------|----------|
| Came back | Did they use it more than day 1? |
| Found it useful | "This helped me" vs "It's nice but..." |
| Felt supported when stuck | "It gave me options" vs "I felt bad for failing" |
| Would continue | "I want to keep using this" |

**Sales signal:**

| Metric | How to Measure |
|--------|----------------|
| Features open doors | Leo tracks: conversations that shifted from "nice chatbot" to "this is different" |
| Pipeline opportunities | New opportunities generated from feature demos |

**NOT measuring yet:**
- Actual behavior change outcomes (too early, need longer timeframe)
- Completion rate percentages (not enough volume for statistical significance)
- NPS scores (need more users first)

---

## Q2 2026: Daily Practice + Feedback

**Goal:** Tighter integration between Coach and Daily Companion. Add feedback on real practice through transcript analysis. Make progress visible through GPS Dashboard.

### Features

| Feature | Description |
|---------|-------------|
| **GPS Dashboard** | Visual progress toward Destination Goal. Shows trajectory: where you started, key moments, where you are. Helps users see how daily actions connect to what they want. |
| **Behavior Adoption Tracking** | Mini-pulse surveys embedded in micro-habit check-ins. Gives visibility into *actual behavior adoption* (not just usage metrics). Self-reported data aggregated across users shows whether people are practicing desired behaviors. Answers: "Are we moving the needle?" |
| **Call Transcript Analysis** | User shares transcript, LLM analyzes against their Tracking Goal. "You asked 2 questions before responding. Here's a moment you could have paused..." |
| **Before/After Touchpoints** | Pre-meeting: "You have a meeting with Pedro. Remember your practice." Post-meeting: "How did it go?" |
| **Calendar Read Access (MS Graph)** | Know user's schedule to enable context-aware reminders |
| **Adaptive Reminders** | Timing and frequency adjust based on user patterns |
| **Coach ↔ Daily Companion Data Flow** | Goals and progress shared between modes. Coach sees Daily Companion struggles. Daily Companion knows Coach commitments. |

### Behavior Adoption Tracking Details

**The problem:**
- Current analytics show *usage* (topics discussed, session length, sentiment)
- No visibility into *actual behavior change* - are people doing the work?
- No way to segment by department/team for enterprise reporting

**The solution:**
- Mini-pulse surveys embedded in Daily Companion check-ins (not a separate survey)
- Self-reported data on behavior practice ("Did you pause before responding today?")
- **Consolidated view**: conversation themes + pulse survey results in one report
- **Segmented by org structure**: show data per department/area (e.g., "Marketing team: 72% practicing")

**Why this matters for sales:**
- Enterprises need to show ROI on coaching investment
- "3,847 conversations" is vanity; "72% practicing target behaviors" is impact
- Segmentation lets L&D see which teams need attention
- Differentiates from chatbots that only show engagement metrics

**Implementation approach:**
- Phase 0: Manual Excel reports (export data, manually group by department) - use to validate value before building
- Phase 1: Simple yes/no pulse questions during check-in + basic segmentation
- Phase 2: Contextual questions based on user's specific habit + full dashboard
- Future: Triangulate with transcript analysis for validated data

**Prerequisites:**
- Capture "who is who" in our database (department, team, role)
- Not a big technical lift, just needs to be prioritized

**Source:** Oseas feedback (Jan 27, 2026) - current Stoic Analytics shows topics but not adoption. Manual workaround viable for early clients (e.g., Vitro 50-80 users).

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

**Goal:** Complete the vision - real-time feedback, deep integrations, seamless experience.

### Features

| Feature | Description | Notes |
|---------|-------------|-------|
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

## Platform & Operations

Internal tooling and automation - not user-facing, but critical for scaling.

### Q1: Sprint Automation (OKR Feature #4)

**Goal:** Remove Ruy and Mike as bottlenecks for client onboarding and coach creation.

| Feature | Owner | Status | Bottleneck Removed |
|---------|-------|--------|-------------------|
| **Environment Generation** | Daniel | In progress | Mike (~half day per client) |
| **Profile/Prompt Creation** | Daniel + Ruy | Not started | Ruy (prompt customization) |
| **Testing Automation** | Daniel | Not started | Manual QA cycles |

**Environment Generation:**
- Automate creation of client environments (`client.stoicq.com`)
- Automate experimental branches

**Profile/Prompt Creation:**
- Templatize coach prompts (victim-protagonist, difficult conversations, etc.)
- Self-service customization layer (change greeting, terminology, company name)
- Reduce Ruy involvement from "write every prompt" to "approve template changes"

**Testing Automation:**
- Automated smoke tests for new deployments
- Regression testing for prompt changes
- Reduce manual QA cycles before shipping

### Q2: Enterprise Readiness & Automation

| Feature | Description |
|---------|-------------|
| **LMS Integration** | Deploy AI coaches into client LMS (via WorkOS SSO or per-LMS connector) |
| **SOC 2 Compliance Readiness** | Policies, controls, and audit preparation |
| **GDPR Full Audit** | Complete GDPR compliance review and documentation |
| **Thinkific SSO** | Access chatbot from Thinkific student dashboard |
| **Self-Service Chatbot Creation** | Nelson/Axialent can create chatbots without dev help |

---

## Dependencies

```
Q1 Foundation
├── Horacio meeting (this week) → Coach methodology
├── MS Teams Notifications (Mike) → Foundation for touchpoints
├── Coach Multi-Session (Ruy + Shamil) → Core differentiator
└── Leo validation → Voice vs Bidirectional decision

Q2 Builds On Q1
├── GPS Dashboard → Needs Q1 goal storage working
├── Calendar MS Graph → Before/After touchpoints
├── Transcript analysis → Requires goals in structured memory
└── Adaptive reminders → Requires usage data from Q1

H2 Builds On Q2
├── Real-time feedback → Needs transcript analysis foundation
└── Full context integrations → Needs Context Manager architecture
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
| Behavior adoption tracking: scope & timing | Ruy + Oseas | Q2 planning - pulse survey design, org segmentation, manual vs built |
| Voice vs Bidirectional priority | Leo | Q1 - customer validation |
| System-triggered Coach methodology | Ruy + Horacio | After Horacio meeting |
| Full calendar integration needed? | Leo | Q1 - is reschedule/delete enough? |
| Transcript analysis: manual vs Teams first? | Ruy | Q2 planning |
| Real-time feedback feasibility | Mike | H2 planning - technical research |
| Coach handoff interface: how does Daily Companion hand off? | Ruy | During Coach Multi-Session design |

---

## Team Assignments

| Person | Focus |
|--------|-------|
| **Mike** | MS Teams integration, technical architecture |
| **Shamil** | Daily Companion cyclic flow, Coach features |
| **Daniel** | Infrastructure, deployment automation |
| **Leo** | Customer validation, demo approval, sales |
| **Ruy** | Methodology, roadmap, Coach design, Horacio/Dolo coordination |

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
| Jan 27, 2026 | Added Q2 feature: Behavior Adoption Tracking - pulse surveys + org segmentation + consolidated reporting. Includes manual-first approach for validation. Source: Oseas feedback on Progress Visibility. |
| Jan 20, 2026 | Expanded Q1 Sprint Automation (OKR #4): environment generation, profile/prompt creation, testing automation. Added Q2 Enterprise Readiness: LMS integration, SOC 2, GDPR audit. |
| Jan 2026 | Initial version - separated Q1/Q2/H2, added transcript analysis, real-time feedback, Platform & Operations section |
