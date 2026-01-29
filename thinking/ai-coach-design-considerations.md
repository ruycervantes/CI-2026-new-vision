# AI Coach Design Considerations
*Working document — started 28 Jan 2026 from Nelson/Ruy product strategy conversation*

---

## What We're Building
A general-purpose AI coach that maintains context across multiple sessions (6+) within a development journey. Not a one-shot chatbot — a persistent coaching relationship.

## Core Requirements

### 1. Multi-Session Memory
The coach must track across sessions:
- **Goals** — what the person is working toward (destination goal, management goals, tracking goals)
- **Commitments** — what they said they'd do, and what happened
- **Challenges** — where they're stuck, recurring patterns
- **Adjustments** — how plans evolved when things didn't work
- **Progress** — what changed from session 1 to session N

### 2. Two Implementation Paradigms

**Option A: Artifacts (session summaries)**
- After each session, generate a structured summary artifact
- Feed artifact as context into the next session
- Like Claude Projects — build context through accumulated documents
- Nelson's framing: "un proyecto en Claude que se le va generando un artefacto al final de cada conversación y lo sumo al contexto del proyecto"

**Option B: Agent Memory (knowledge graph)**
- Use agent memory tools that build a graph of the person's development journey
- Memory is structured and queryable, not just text
- More sophisticated but less transparent to the user

**Option C: Hybrid**
- Agent manages its own memory graph internally
- Also produces human-readable artifacts for the user (and for human coaches)

**Open question:** Which gives better coaching quality? Need to prototype both.

### 3. Claude Agent SDK Approach
- Give the agent file skills — let it read/write its own memory
- Agent manages its own state across sessions
- Ruy has experimented with this pattern already
- Key design question: which skills to give the agent

### 4. Decoupled from Thinkific
- Cannot feel like a "lesson" — must feel like going to your coach
- May start inside Thinkific but needs its own experience
- The LMS container creates the wrong mental model
- Long-term: standalone experience with multiple entry points (web, Teams, etc.)

---

## Connection to Team Context

### Team Document as Context
When used within an HPT process, the AI coach receives:
- Team assessment results (what the team scored, where gaps are)
- Team agreements (what they committed to in workshops)
- Individual's role in the team plan ("your responsibility is X")

This enables contextual coaching:
- "I see in the team document that you agreed to improve how you communicate expectations. Want to start there, or with what was planned for this session?"
- "In the last team update, the group noted progress on X but struggles with Y. How is that showing up for you?"

### Individual-to-Team Bridge
- Coaching is individual (private, safe space for struggles)
- But connects to team goals (intrinsic motivation: "this matters because my team needs me to change")
- Social accountability: team can see who completed sessions (not content)
- Wins can be shared; struggles stay private

---

## Behavior Change Integration

### The Adjust Stage (Critical)
When users aren't adhering to commitments:
- Don't just track failure ("you didn't do it 3 times")
- Offer recalibration: "Would you like to adjust this habit? Maybe instead of A, try B?"
- This is what differentiates from simple habit trackers
- Reference: the vision's adjust stage where users reinterpret and adapt

### Intrinsic Motivation Loop
1. Connect behavior change to something that matters deeply (team context, personal values)
2. Track progress with lightweight check-ins
3. When struggling, help find alternative paths (not shame)
4. When succeeding, reinforce the connection to why it matters

### Microhabits
- Still valuable but should be embedded in the coaching relationship
- Not a standalone feature — the coach sets and tracks habits as part of the conversation
- Check-ins become part of coaching sessions, not separate notifications

---

## Data Export / Human Coach Integration

### The "Torch Model" (TA to the Professor)
- AI coach handles day-to-day practice and reflection
- Human coach handles deeper strategic conversations
- AI generates summaries and insights that feed to the human coach
- Human coach can see: what the person is working on, where they're stuck, session count, key themes

### What to Export
- Session summaries (per session and aggregated)
- Goal progress tracking
- Recurring patterns / stuck points
- Engagement metrics (frequency, depth of sessions)
- Team-level aggregate: "how is this group's coaching going?"

### Technical Note
All sessions stored in our system → export is "puro prompting" — feed conversations to a summarizer prompt. Not a hard technical problem, but needs thoughtful prompt design.

---

## Content-Connected Coaching vs. General Coaching

### CB Assessment Debrief Coach
- Already exists in some form
- Lives within a specific course/cycle
- This is fine as-is — it's bounded and structured

### General AI Coach (NEW — what we're building)
- Not tied to a specific course or content
- Maintains thread across sessions within a development journey
- Uses team context when available
- This is the strategic unlock

### Content Chatbots / AI Mentors (Nelson's wizard)
- Tied to specific content (pre-workshop reflection, content review)
- More like "learning buddies" than coaches
- Nelson wants to build a wizard for creating these
- Could share underlying technology with the general coach
- Parked for now — Nelson may prototype independently

---

## Analytics / Impact Connection

### What the AI Coach Generates for Impact Measurement
- Every coaching conversation = analyzable data
- Can extract: themes, progress indicators, commitment completion rates
- Can identify: team-level patterns across individual coaching sessions
- Can generate: qualitative impact statements ("before coaching, I struggled with X; now I can do Y")

### Nelson's "Impact" Platform Vision
- AI coach data feeds into the data layer
- Combined with: assessments, surveys, platform engagement
- Enables: impact portal for clients, intelligence portal for coaches
- This is Phase 2 — after the coach works

---

## Oseas's Lockstep Principle (Confirmed 28 Jan)

> "Si tengo 10 de coaching y 2 de reporte, no lo vendo."

Coaching quality and reporting/visibility quality must advance together. Every coaching capability we build must have a corresponding visibility output. This means:

- Every session → generates data that can feed a dashboard
- Every goal tracked → has a progress indicator visible to sponsors
- Every behavior change → has evidence that can be shown to the buyer
- Impact reporting is NOT an afterthought — it's a first-class design requirement

### What buyers need to see (minimum):
- Are people using it? (adherence, session count, engagement)
- Is it working? (self-reported progress, goal completion, pattern changes)
- What's changing? (qualitative themes, before/after narratives)
- Aggregate view: how is this group/team doing overall?

### Implication for architecture:
Every coaching interaction must produce structured, queryable data — not just conversation logs. Design the data model alongside the coaching experience, not after.

---

## Open Design Questions

1. **How does the coach "know" Conscious Business?** Single mega-prompt vs. modular skills (preparing difficult conversations, understanding victim/protagonist, etc.)
2. **How do we handle the first session?** Does it start from CB Assessment debrief results? Cold start? Team document?
3. **What's the minimum viable memory?** How many sessions can we support before context windows become a problem?
4. **Privacy boundaries:** When coaching is connected to team context, what's private vs. shared?
5. **Session cadence:** Is the coach always available, or do we encourage a rhythm (weekly, bi-weekly)?
6. **Quality assurance:** How do we know the coaching is good? Who evaluates? Horacio? Richie?
7. **Content depth:** Does the general coach need deep knowledge of conflict resolution techniques, habit formation science, etc., or does it reference content modules?

---

## Next Steps
- [ ] Prototype Option A (artifacts) vs. Option B (memory graph) — small test
- [ ] Define the first session experience
- [ ] Identify which CB/coaching skills to encode
- [ ] Validate with Horacio: does this approach match what good coaching looks like?
- [ ] Clarify: does this ship as part of Thinkific experience or standalone?
