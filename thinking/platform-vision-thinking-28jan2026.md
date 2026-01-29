# Platform Vision
*Working draft — 28 Jan 2026*

---

## Why We Exist

We help humans become more conscious — of themselves, of how they show up, of the gap between who they want to be and who they are — so they can be more effective.

We live in a moment of massive uncertainty. AI is reshaping work, roles are shifting, and people need to navigate this transition with greater awareness and adaptability. We believe AI should serve human flourishing — that technology can increase human consciousness rather than diminish it.

We believe work is and will continue to be a source of meaning and satisfaction beyond generating money. And we believe that helping people become more conscious makes them more effective — not the other way around.

---

## What We Do

**We help humans have better conversations.**

- **With yourself:** Reflection, awareness, closing the gap between your espoused values and your values-in-action. Understanding why you fall back into reactive patterns. Turning awareness into action through practice.
- **With others:** Showing up differently in difficult conversations, giving feedback, being a learner instead of a know-it-all.
- **As a team:** Having conversations that build alignment, honor commitments, and evolve how the team works together.
- **As an organization:** Organizations are networks of conversations. Improve the conversations, improve the organization.

This is the unifying thread across everything we build. Whether we're helping an individual leader close the gap between intention and behavior, or helping a team track and honor their agreements, the core competence is the same: **increasing consciousness to enable better conversations.**

---

## How We Do It

### AI That Increases Consciousness

Not AI that replaces human judgment, but AI that helps you see what you couldn't see — your patterns, your reactivity, your progress, your team's dynamics.

The AI Coach is a persistent coaching relationship — not a one-shot chatbot. It maintains context across sessions, tracks your goals and commitments, and helps you bridge awareness to action.

### Three Pillars of Our Approach

**1. Coaching Methodology (Axialent)**
Decades of application coaching praxis — Richie, Horacio, the Conscious Business framework. Not just theory: a structured process for how to coach behavior change. Design principles grounded in real practice: the gap as raw material, real content creates real learning, zero attachment to direction.

**2. Scientific Foundation**
Behavioral science, HCI research, CSCW research. We don't rely on one methodology alone — we bring frontier research on how technology can genuinely help humans develop. We design based on what works, validated by science.

**3. Enterprise Integration**
Be in the flow of work. Not a separate app people go to — your coach embedded where you already work. Teams, email, calendar. Your coach for people who work in enterprise.

### Visibility as Design Constraint

Every feature we build must make the invisible visible. Individual leadership change normally takes 2 years to show with a 360. Team progress is hard to measure without digital tools. We design for observability from the start — every coaching interaction produces structured, queryable data that can demonstrate impact.

This is Oseas's lockstep principle: coaching quality and visibility quality must advance together. 10 points of coaching + 2 points of reporting = unsellable.

---

## Two Design Spaces

The AI Coach is the shared technology foundation. Beyond it, there are two design spaces — each with genuine depth, each a full product.

### Design Space 1: Inside the Individual (Leadership Development)

**The core:** A continuous conversation with yourself — increasing consciousness of how you think and act, closing the gap between who you say you want to be and who you show up as.

**What this looks like as product:**
- Goal hierarchy (destination → management → tracking goals)
- Daily Companion: microhabits that bridge awareness to action, cyclic check-ins, the adjust stage when things aren't working
- Coach mode: deep conversations about setbacks, goals, and growth
- Multi-session memory: the coach knows your trajectory across sessions
- The "Pepe Grillo": deep integrations (email, chats, calendar) that make the coach present in your day-to-day, not just when you open the app

**Where this is described:** `core/vision-behavior-change.md` (detailed product spec)

**Note:** Behavior change is a powerful starting point, but leadership development is broader than behavior change alone. The deeper work is consciousness itself.

### Design Space 2: Inside the Team (Team Effectiveness)

**The core:** Teams are made through conversations. We help teams have better conversations and manage their commitments — so they evolve together rather than stagnate.

**What this looks like as product:**
- **Team memory:** The Team Agreement Doc — a living artifact structured around Katzenbach dimensions (purpose, roles, relationships, processes). A testament of the team's ongoing conversation about who they are, how they evolve, and how they strive for excellence. Updated by humans AND AIs.
- **Individual coaching in team context:** Each person gets an AI coach that knows both their personal patterns AND their team's agreements. "I see the team committed to improving decision-making. How is that showing up for you?"
- **Meeting facilitation support:** Real-time AI support during team meetings — topic tracking, goal reflection, ambient visualization. Augmenting what a consultant does in meeting facilitation. (Reference: Chen et al. "Are We On Track?" — AI-assisted goal reflection during meetings.)
- **Team conversation tracking:** Capture agreements across meetings, track whether they're being honored, surface patterns over time.
- **Accountability model:** Social commitment to the process (visible), private content in individual coaching.
- **Before/during/after:** Preparing for conversations, supporting during, reflecting after — at the team level.

**Where this is described:** `team-effectiveness/mvp-offer.md` (near-term MVP), team effectiveness vision (evolving)

**Note:** The near-term validation uses current product + consultant-led process (Nelson is leading). The full engineering vision is significantly larger — meeting facilitation, real-time feedback, team dynamics visualization.

### Why the Same Company Should Do Both

It's not two different bets — it's **one competence applied at two levels.** Helping humans have better conversations through increased consciousness. The individual path helps you show up better in conversations. The team path helps the team have better conversations together. The individual work feeds the team work and vice versa.

### The Resource Reality

Both design spaces are full products with substantial engineering depth. Without significant funding, we can't do both justice simultaneously. The shared foundation (AI Coach, enterprise integration, visibility) buys us time to validate which path has customer pull — or whether a combined path is viable.

---

## Strategic Filter for What We Build

> **Build things that either:**
> 1. Scale what a consultant does — deliver to every team member what was previously only possible for executives
> 2. Augment a consultant — give them capabilities they don't have today (real-time meeting analysis, cross-session pattern detection, team dynamics visualization)

Every feature should pass one of these tests.

---

## What's Shared (Build Now)

| Layer | What it is |
|-------|------------|
| **AI Coach** | Multi-session coaching with memory, goal tracking, behavior change methodology. The core technology bet. |
| **Enterprise Integration** | Teams notifications, WorkOS/SSO, calendar, flow-of-work presence. |
| **Visibility** | Design constraint: every feature stores process data that demonstrates impact. Analytics, reporting, dashboards. |
| **CB Methodology** | Conscious Business embedded in prompting and coaching design. |
| **Scientific Foundation** | Behavioral science, HCI, CSCW informing design decisions. |

---

## Decisions Made

1. **AI Coach is the shared technology investment** — build this first, it unlocks both paths (Oseas, Nelson, Mike, Ruy — Jan 28)
2. **Validate both markets in parallel** — LD and HPT, see which has customer pull
3. **HPT validation uses current product** — no new engineering needed for validation. Nelson builds slides, visual prototypes, uses existing capabilities
4. **Impact visibility in lockstep** — coaching quality and reporting quality must advance together (Oseas, Jan 28)
5. **Commercial validation required** — Thierry + Fernando Fascioli review all product direction (board mandate)
6. **Don't over-design HPT now** — co-design with Dolo is Q2+. Focus on common foundation.
7. **Stoic is a separate spin-off** — decided. What's unresolved is commercial relationship with Axialent.

## Decisions Not Made

1. **Stoic's commercial model** — does Stoic sell independently or operate as Axialent's digital arm?
2. **Where to go deep** — LD, HPT, or combined? Waiting for customer pull.
3. **Are we differentiated?** — "80/20 replaceable by a $10 app?" hasn't been answered. Need competitive research.
4. **Long-term team effectiveness product** — beyond the MVP, the full vision is sketched but not designed.
5. **Pricing model** — does digital add-on increase ticket (100→115) or decrease it (100→50)?

---

## The Competitive Question (Unresolved)

> "Are we differentiated or 80/20 replaceable by a $10 app?"

- Anyone can build an AI coaching chatbot with good prompting
- What's hard to replicate: the complete methodology, the orchestration of the full cycle, the accumulated knowledge of what works, the scientific rigor
- But we haven't proven this is hard to replicate — it's an assumption
- Lots of competitors: Torch (AI + human coach), MindGym, Cloverleaf, plus every generic AI coaching app
- Need to do competitive research to answer this honestly

---

## Document Structure

| Document | Purpose |
|----------|---------|
| **This document** (`core/vision.md` when promoted) | Platform vision — the why, the what, the two design spaces |
| `core/vision-behavior-change.md` | LD product spec — detailed behavior change product design |
| `team-effectiveness/mvp-offer.md` | HPT near-term MVP — the 90-day hybrid cycle |
| `core/roadmap.md` | Engineering roadmap — shared foundation + feature candidates by path |
| `thinking/ai-coach-design-considerations.md` | AI Coach architecture — memory, implementation paradigms, design questions |

---

*This is a working document. It will be promoted to `core/vision.md` when ready.*
