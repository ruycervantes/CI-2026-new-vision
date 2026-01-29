# Engineering Roadmap — 2026

> **Purpose:** What we build and when. Guide sales conversations with Leo.
> **See also:** [vision.md](vision.md) for platform vision, [vision-behavior-change.md](vision-behavior-change.md) for LD product spec, [alignment.md](alignment.md) for leadership sign-off
> **Last updated:** January 28, 2026

---

## Strategic Context

### The Bet

The AI Coach is a persistent coaching relationship — not a one-shot chatbot. It's the shared technology foundation serving both Leadership Development and Team Effectiveness.

- **In LD:** We own the complete behavior change cycle — goals, habits, adjustment, evolution. The methodology orchestrates real change, not just conversation.
- **In HPT:** The AI Coach makes individual coaching possible at scale within team context. Teams change because each person has ongoing conversations about how they're showing up relative to the team's agreements — not just the leader getting coached.

> "Si nos quedamos como 'tenemos un chatbot de coaching', competimos con todos."

### Dual Value Proposition (Jan 28 alignment)

1. **Increase impact** — individual AI coaching for everyone in the process (not just the team leader)
2. **Make it visible** — reporting/analytics that shows sponsors whether it's working

> "Si no estoy incrementando el impacto, ¿para qué te lo compro? Y si no es visible, no me entero." — Oseas

### Lockstep Principle

Coaching quality and reporting quality must advance together. 10 points of coaching + 2 points of reporting = unsellable.

### Validation Determines What Comes Next

Q1 commitments are firm. Everything after depends on which path shows customer pull:

| Outcome | What it means |
|---------|---------------|
| **LD pulls** | Go deep on individual behavior change (presence, integrations, "Pepe Grillo") |
| **HPT pulls** | Go deep on team effectiveness (team memory, meeting facilitation, conversation tracking) |
| **Both pull** | Combined path — individual coaching within team context |

Commercial validation: Thierry + Fernando Fascioli (board-designated) review all product direction.

---

## Shared Foundation (Q1 2026 — Build Now)

**Goal:** Deliver a sellable Application Coaching experience. Prove the multi-session Coach + cyclic Daily Companion combination works as a persistent coaching relationship.

### Core Features

| Feature | Owner | Status | Description |
|---------|-------|--------|-------------|
| **MS Teams Notifications** | Mike | In progress | One-way notifications. Foundation for everything. |
| **Daily Companion Cyclic Flow** | Shamil | Ready to build | Loop instead of end. User can continue, modify habit, or go to Coach. |
| **Thinking Partner: Challenge/Gap/Commitment** | Shamil + Ruy | Ready to build | Show and store challenge, gap, action plan commitment. Foundation for multi-session. |
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

**Option A: Voice** — Ship STT (already built) + TTS play button → later full voice-to-voice

**Option B: Bidirectional Teams Chatbot** — Check-ins via Teams bot → later richer interactions

**Decision:** Leo validates with customers which has more pull.

### Ship What's Built

Already done, just need deployment: Speech-to-text (STT), Executive Summary, Data features.

### Smaller Items

| Item | Notes |
|------|-------|
| Calendar: Reschedule & Delete | Our internal events only, not full MS Graph |
| Auto-naming threads | Like ChatGPT - rename after a few messages |

### Q1 Validation Experiment

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

**Sales signal:** Leo tracks conversations that shift from "nice chatbot" to "this is different."

---

## Feature Candidates by Path

Features beyond Q1 are organized by which path they serve, prioritized by customer pull — not assigned to specific quarters.

### Serves Both Paths

| Feature | Description | Notes |
|---------|-------------|-------|
| **GPS Dashboard** | Visual progress toward Destination Goal. Shows trajectory: where you started, key moments, where you are. | Mike proposed user dashboard as "wow factor." |
| **Behavior Adoption Tracking** | Mini-pulse surveys embedded in check-ins. Self-reported data on behavior practice, segmented by org structure. | Serves LD sponsors AND HPT progress visibility. Manual-first for validation (Phase 0: Excel). |
| **Call Transcript Analysis** | User shares transcript, LLM analyzes against their goals. For LD: individual conversations. For HPT: team meeting dynamics. | Phase 1: manual upload. Phase 2: Teams integration. |
| **Before/After Touchpoints** | Pre-meeting: "You have a meeting with Pedro. Remember your practice." Post-meeting: "How did it go?" | Requires calendar read access. |
| **Calendar Read Access (MS Graph)** | Know user's schedule to enable context-aware reminders. | Enterprise integration. |
| **Adaptive Reminders** | Timing and frequency adjust based on user patterns. | AI Coach evolution. |
| **Coach ↔ Daily Companion Data Flow** | Goals and progress shared between modes. Coach sees Daily Companion struggles. Daily Companion knows Coach commitments. | |

### Leadership Development Path

| Feature | Description | Notes |
|---------|-------------|-------|
| **Deep Context Integrations** | Email, chats, calendar — the "Pepe Grillo" always-present companion. | Privacy concerns, needs Context Manager architecture. |
| **Seamless Mode Transitions** | Fluid Coach ↔ Daily Companion without explicit switching. | Polish after foundation solid. |
| **Peer Accountability** | Social goal-setting features. | Research needed. |

### Team Effectiveness Path

| Feature | Description | Notes |
|---------|-------------|-------|
| **Team Agreement Doc** | Living artifact structured around Katzenbach dimensions. Updated by humans and AIs. | Core HPT concept — co-design with Dolo Q2+. |
| **Meeting Facilitation Support** | Real-time AI during team meetings — topic tracking, goal reflection, ambient visualization. | Technically complex. Reference: Chen et al. "Are We On Track?" |
| **Team Conversation Tracking** | Capture agreements across meetings, track whether honored, surface patterns. | |
| **Individual-to-Team Bridge** | AI coach knows personal patterns AND team context. Aggregate individual patterns to team level (privacy-preserving). | |

### Needs Exploration

| Feature | Description | Notes |
|---------|-------------|-------|
| **Real-Time Feedback** | "During" meeting interventions. Feedback while practicing, not just after. | Technically complex, privacy implications. Potentially more useful for HPT. |
| **Full Context Integrations** | Deep calendar, email, potentially other sources. | What do you pull in? What does a consultant do that we can replicate? |

---

## Platform & Operations

Internal tooling and automation — not user-facing, but critical for scaling.

### Q1: Sprint Automation (OKR Feature #4)

**Goal:** Remove Ruy and Mike as bottlenecks for client onboarding and coach creation.

| Feature | Owner | Status | Bottleneck Removed |
|---------|-------|--------|-------------------|
| **Environment Generation** | Daniel | In progress | Mike (~half day per client) |
| **Profile/Prompt Creation** | Daniel + Ruy | Not started | Ruy (prompt customization) |
| **Testing Automation** | Daniel | Not started | Manual QA cycles |

### Enterprise Readiness (Post-Q1)

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

Post-Q1 Builds On Q1
├── GPS Dashboard → Needs Q1 goal storage working
├── Calendar MS Graph → Before/After touchpoints
├── Transcript analysis → Requires goals in structured memory
├── Adaptive reminders → Requires usage data from Q1
└── HPT co-design with Dolo → Requires validation signals

Later Builds On Post-Q1
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
| Behavior adoption tracking: scope & timing | Ruy + Oseas | Post-Q1 planning |
| Voice vs Bidirectional priority | Leo | Q1 - customer validation |
| System-triggered Coach methodology | Ruy + Horacio | After Horacio meeting |
| Full calendar integration needed? | Leo | Q1 - is reschedule/delete enough? |
| Transcript analysis: manual vs Teams first? | Ruy | Post-Q1 planning |
| Real-time feedback feasibility | Mike | Later - technical research |
| Coach handoff interface | Ruy | During Coach Multi-Session design |

---

## Team Assignments

| Person | Focus |
|--------|-------|
| **Mike** | MS Teams integration, technical architecture |
| **Shamil** | Daily Companion cyclic flow, Coach features |
| **Daniel** | Infrastructure, deployment automation |
| **Leo** | Customer validation, demo approval, sales |
| **Nelson** | Impact/visibility design, HPT blended journey spec, Thierry coordination |
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
| Both paths demand resources simultaneously | Shared foundation buys time; let customer pull determine depth |

---

## Changelog

| Date | Change |
|------|--------|
| Jan 28, 2026 | **Restructured:** Reorganized from quarterly timeline to shared foundation + feature candidates by path. Visibility as design constraint. Added HPT feature candidates. Source: platform vision restructuring. |
| Jan 28, 2026 | Added: dual value proposition (increase impact + make visible), lockstep principle, AI Coach as shared foundation for LD + HPT, Nelson owns visibility, Thierry/Fascioli commercial review gate. Source: Product Strategy Office Hours (Oseas, Nelson, Mike, Ruy). |
| Jan 27, 2026 | Added Q2 feature: Behavior Adoption Tracking - pulse surveys + org segmentation + consolidated reporting. Source: Oseas feedback on Progress Visibility. |
| Jan 20, 2026 | Expanded Q1 Sprint Automation (OKR #4): environment generation, profile/prompt creation, testing automation. Added Q2 Enterprise Readiness. |
| Jan 2026 | Initial version. |
