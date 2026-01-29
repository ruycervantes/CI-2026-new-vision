# Roadmap Restructuring — Thinking Scratch File
*28 Jan 2026 — from /think session*

---

## The Core Insight

The roadmap shouldn't be organized by timeline (Q1/Q2/H2) or by market (LD vs HPT). It should be organized by:

1. **Shared foundation** — build now, serves everything
2. **Validation** — ongoing, determines what we prioritize next
3. **Feature candidates** — organized by which path they serve, prioritized by customer pull

### Three Possible Outcomes from Validation

| Outcome | What it means |
|---------|---------------|
| **LD pulls** | Go deep on individual behavior change |
| **HPT pulls** | Go deep on team effectiveness |
| **Both pull** | Combined path — individual coaching feeds team effectiveness |

Option 3 is actually what the product naturally suggests — individual coaching within team context.

The decision isn't "pick one" — it's "where is the customer pull, and does it validate combining them?"

---

## Visibility as Design Constraint (Not a Feature Track)

Impact visibility isn't a separate feature to build later. It's a design principle that applies to everything:

- **The problem:** Making the invisible visible. Individual leadership change takes 2 years to show with traditional 360s. Team progress is hard to measure without digital.
- **The principle:** Every feature we build must store process data that can later demonstrate impact. Don't build opaque coaching.
- **Current state:** We already have analytics (themes, process tracking). This needs to evolve, not start from zero.
- **Roadmap implication:** Visibility is a constraint on how we build, not a line item for when we build.

---

## Feature Reclassification

Going through current roadmap features and classifying by what they serve:

### Foundation (Build Now — Q1)

| Feature | Category | Notes |
|---------|----------|-------|
| MS Teams Notifications | Enterprise Integration | Must-have, in progress |
| Daily Companion Cyclic Flow | AI Coach | In progress (Shamil) |
| Thinking Partner | AI Coach | Ready to build |
| Coach Multi-Session | AI Coach | Core technology bet |
| Voice OR Bidirectional | AI Coach | Validate with Leo |

### Next Wave (Tentative — depends on validation signals)

| Feature | Serves | Notes |
|---------|--------|-------|
| GPS Dashboard | Both | Visual progress. Could demo for LD or HPT. Mike proposed user dashboard as "wow factor." Possibly Q2. |
| Behavior Adoption Tracking | Both | Pulse surveys showing actual behavior change. Serves LD sponsors AND HPT progress visibility. |
| Call Transcript Analysis | Both | For LD: analyze individual's conversations. For HPT: analyze team meeting dynamics, how team is reacting. Could come from Teams integration. |
| Before/After Touchpoints | Both | For LD: "how did your meeting go?" For HPT: check on everyone, how's the team doing. |
| Calendar Read Access | Enterprise Integration | Enables context-aware features for both paths |
| HRMS Integration | Enterprise Integration | Needs to be in integration track |
| Adaptive Reminders | AI Coach evolution | Could serve individual habits or team commitments |

### Later / Needs Exploration

| Feature | Serves | Notes |
|---------|--------|-------|
| Real-Time Feedback (during meetings) | Potentially MORE useful for HPT | Key HPT intervention: meeting facilitation by consultant. AI could augment this. "Fast meeting facilitation for the team." Difficult — needs research on how to do it. |
| Full Context Integrations | Both | What do you pull in? The question is what a consultant does that we can replicate or augment. |
| Mode Transitions (Coach ↔ Daily Companion) | AI Coach | Polish, not path-dependent |

---

## The Strategic Frame for Features

> **Build things that either:**
> 1. Do what a consultant does but for every team (scale what's currently human-delivered)
> 2. Augment a consultant (give them capabilities they don't have today)

This is the filter for prioritization. Every feature should pass one of these tests.

---

## Both Paths Have Real Depth (Key Realization)

The two paths are NOT "same engine, different framing." Beyond the shared foundation, they diverge into genuinely different products with different engineering surfaces.

### Individual Path (LD) — Goes Deep Into Presence
- Deep integrations: email, chats, calendar
- The "Pepe Grillo" — an always-present consciousness companion
- Individual memory across sessions and time
- Behavior tracking, habit formation, transcript analysis of individual conversations
- Full context integrations that make the coach aware of your day-to-day
- This is already well-described in `core/vision.md` (behavior change vision)

### Team Path (HPT) — Goes Deep Into Collective Intelligence
- **Team memory:** Team Agreement Doc as living artifact, structured around Katzenbach dimensions (purpose, roles, relationships, processes). Updated by humans AND AIs. A testament of the team's ongoing conversation about being a team, evolving, and striving for excellence.
- **Team context management:** Not just individual context across sessions, but team conversation history across facilitations, coaching, and regular meetings.
- **Meeting facilitation support:** Real-time AI support during team meetings — topic tracking, goal reflection, ambient visualization. (Reference: Chen et al. "Are We On Track?" — AI-assisted active and passive goal reflection during meetings. Two modes: ambient visualization that evolves as meeting unfolds, and interactive questioning that prompts reflection.)
- **Team conversation tracking:** Capture agreements, track whether they're being honored, surface patterns across meetings.
- **Individual-to-team bridge:** AI coach knows both individual patterns AND team context, can reference team agreements in individual coaching, can surface individual patterns to team-level (aggregate, privacy-preserving).
- This is partially described in `team-effectiveness/mvp-offer.md` but the full engineering vision is much larger.

### The Resource Reality
Both paths are full products. Without significant funding, can't do both justice. The shared foundation buys time to validate, but eventually the paths diverge into substantially different engineering efforts.

### Where This Belongs
This depth acknowledgment needs to live somewhere — either:
- In the platform vision (to ensure we're not underestimating either path)
- In the roadmap framing (to make the resource tradeoff explicit)
- Or both

---

## The Converged Vision (from /think Jan 28)

### What Stoic Does
We help humans become more conscious — of themselves, of how they show up in conversations, of the gap between who they want to be and who they are — so they can be more effective.

### The Medium is Conversations
- **With yourself:** Reflection, awareness, closing the gap between espoused values and values-in-action. The Daily Companion is a continuous conversation with yourself. Microhabits bridge awareness to action.
- **With others:** Showing up differently in difficult conversations, giving feedback, being a learner instead of a know-it-all.
- **As a team:** Facilitation, agreements, commitment tracking, evolving together.
- **As an organization:** Organizations are networks of conversations. Improve the conversations, improve the organization.

### The Unifying Thread
"Helping humans have better conversations through increased consciousness."

This is why the same company should do both LD and HPT — it's not two different bets, it's **one competence applied at two levels**.

### The Unfair Advantage (Broader Than CB)
Not just Conscious Business methodology. Three pillars:
1. **Axialent's coaching methodology** — decades of praxis, Richie's design principles (the gap as raw material, real content creates real learning, zero attachment to direction), deep sensibility for what makes conversations transformative
2. **Scientific foundation** — behavioral science, HCI research, CSCW research. Bring frontier science to human development, not just one methodology.
3. **Enterprise integration** — be in the flow of work. Not a separate app — your coach embedded where you already work. "Tu coach para personas que trabajan en enterprise."

### The Values Anchor
- AI for human flourishing. Team Human.
- Work is and will continue to be a source of satisfaction beyond generating money.
- In a moment of massive uncertainty about how AI transforms work, we're an instrument that helps people navigate this transition with greater consciousness and effectiveness.
- Greater consciousness → greater effectiveness (not the other way around).

### The Behavior Change Distinction
Behavior change is a powerful starting point for LD, but LD is broader. There are other aspects to leadership development beyond behavior change. The deeper work is consciousness — understanding why you fall back into reactive patterns, why you become a know-it-all instead of a learner.

### What's Common (AI Coach) and Two Design Spaces

**Common:** The AI Coach — multi-session memory, behavior change methodology, consciousness-raising through conversation. This is what we build now.

**Design Space 1: Inside the Individual (LD)**
- Conversation with yourself → awareness → microhabits → behavior change
- Deep integrations (email, chats, calendar) — the "Pepe Grillo"
- Individual memory and trajectory tracking
- Closing the gap between who you say you want to be and who you show up as
- Well-described in current behavior change vision

**Design Space 2: Inside the Team (HPT)**
- Team memory (Team Agreement Doc as living artifact across Katzenbach dimensions)
- Meeting facilitation support — ambient visualization, conversation tracking
- Team conversation tracking across meetings — agreements, commitments, patterns
- Individual-to-team bridge — coach knows both personal patterns and team context
- "Teams are made through conversations" — help teams have better conversations and manage commitments
- Partially described in MVP offer, but full vision is much larger

### For the Vision Document
The vision should show:
1. The core (consciousness, better conversations, scientific foundation, values)
2. What's shared (AI Coach, enterprise integration, visibility as design constraint)
3. The two design spaces with honest depth — neither is trivial
4. The resource reality — can't do both fully without funding; shared foundation buys validation time
5. How we decide where to go deep — customer pull, not predetermined timeline

---

## Open Questions

1. How do we structure the roadmap document itself? Not by quarter, not by path — by what?
2. How do we represent the validation activities and their signals?
3. Where do LD-only features live? In the roadmap or in `core/vision-behavior-change.md`?
4. Where do HPT-only features live? In the roadmap or in `team-effectiveness/`?
5. What's the right level of detail for "later" features that we haven't designed?
6. How does the Q1 experiment / validation plan connect to the roadmap?

---

## What Hasn't Changed

- Platform & Operations section (sprint automation, infra) — stays as-is
- Team assignments — same people, same general areas
- Dependencies — still valid
- Risks and mitigations — mostly still apply
