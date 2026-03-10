# Team Effectiveness Platform — Product Thesis v3

**March 9, 2026**

---

## 1. What We're Building

When Valentin and Anabel ran the HPT process with production crews, people stopped threatening to kill each other and started functioning as a team. That happened. But Sara doesn't have Valentin and Anabel in any of her seven productions. She has nothing.

The full HPT process requires a consultant embedded in each production — too expensive, too intrusive, too disruptive for a running crew. So Sara gets zero coverage of the human layer. No early warning. No team alignment. Nobody watching whether people are working the way they agreed to. She finds out about problems when they become crises.

**Our product makes the HPT process accessible for the first time.** The AI does the heavy lifting — onboarding prep, private coaching, monitoring, nudges. One consultant covers all productions — seeding the system with organizational knowledge, monitoring the dashboard, dropping in for kickoffs and key moments. The cost is a fraction of embedding a consultant per production. The intrusion is minimal — people talk to the AI on their phone.

**The unit of transformation is the conversation.** Everything we build exists to make conversations better, more frequent, or more grounded in reality.

**This is not a PLIA-only product.** Production is where we start — because PLIA gives us the richest operational data layer and Axialent gives us the methodology. But the architecture is designed to plug into any environment where teams coordinate complex work: software teams with Jira/Linear, consulting teams with deliverable trackers, any organization with project management tools and a communication layer. The ontology, the team agreement, the coaching, the pulse, and the trust architecture are industry-agnostic. What compounds is the behavioral knowledge across teams.

---

## 2. The Four Sources of Intelligence

The product's intelligence comes from four sources that build on each other. **All four are part of the minimum lovable product** — not a build sequence where each phase unlocks the next, but layers that work together from day one.

![Four Sources of Intelligence](site/diagrams/plia-teams-01-four-sources.png)

### Source 1: The Ontology (consultant-seeded, before the team exists)

An embedded consultant-engineer seeds the organizational context before any team touches the system — what iZen is, how productions work, typical failure patterns, when risks cluster, and 20+ years of Axialent methodology structured into the system's architecture. This is professional services work. Our job, not the client's.

The ontology includes cross-production lessons: "scene approval bypasses happen in month 1", "dual-unit syncs drop off in week 3-4", "in Cacao y Compania, adding a budget-check gate resolved it in a week." This is what makes the onboarding conversation informed rather than blank. Without it, every team starts from zero. With it, the system says "in 3 of the last 5 iZen productions..." during the moment the team is deciding how to work.

**The learning doesn't live in a report nobody reads. It lives inside the conversation where it matters.**

![Cross-Production Learning](site/diagrams/plia-teams-05-cross-production-learning.png)

The ontology compounds. Every production adds to it — what patterns appeared, what interventions worked, what agreements held up. By the 10th production, the system has organizational memory that no individual consultant could carry alone.

### Source 2: The Team Agreement (progressive onboarding)

Before the team meets, the AI does the prep work — individual conversations with each person, async, on their phone:

- "You're the production designer on Alfonso el Sabio. What do you need to do your best work?"
- "In 3 of the last 5 productions, scene changes hit art departments without budget approval. How should your team handle that?"
- "What does 'yes' mean when someone commits your department to something?"

The ontology surfaces lessons from previous productions at the moments they matter. The AI covers the four dimensions — purpose, roles, processes, relationships — not as a framework to fill out, but as questions that matter to the person.

The human consultant walks into the onboarding session already informed — they know what everyone said, where the tensions are, what the ontology flagged. The session is shorter, sharper, and more productive because the groundwork is done.

The consultant doesn't need to be in every room. They seed the ontology, review the AI's synthesis before the kickoff, and show up for the session itself. One consultant, seven productions — because the AI did the groundwork.

The result is a living team agreement in the team's own words. It becomes the AI's baseline: when it observes drift, it measures against what this team said, not generic best practices.

### Source 3: Operational Context (scoped, from the client's existing tools)

The product needs enough business context to know **when key moments happen** and **what the team is supposed to deliver**. Without this, coaching and pulse are disconnected from reality — the AI doesn't know that a milestone is approaching or that workload just spiked.

For PLIA, this means a scoped integration — not ingesting every budget line item or scene breakdown, but enough to know: what are the major milestones? What are the key deliverables? When do the high-coordination moments cluster? PLIA already runs 80-100 AI agents processing schedule, budget, logistics, and script data. We don't need all of it. We need the minimum slice that, combined with the ontology and team agreement, makes the coaching timely and the dashboard grounded.

**The validation question for every client:** "What is the minimum slice of your operational data that makes this meaningful?" For PLIA, we need to explore this together. For a software company, it might be sprint milestones from Jira. For a consulting firm, it might be deliverable deadlines from their tracker.

This source is deliberately scoped for the minimum lovable product. Deeper integration — full budget tracking, granular schedule analysis, cascade risk modeling — is a future layer that adds precision, not a prerequisite for delivering value.

### Source 4: Coaching + Milestone-Triggered Pulse (continuous, individual)

What individuals share privately — reflections, pulse check-ins, coaching conversations — feeds back into the system's intelligence. But pulse isn't generic. It's triggered by what matters to this team at this moment.

![Milestone-Triggered Pulse](site/diagrams/plia-teams-13-milestone-pulse.jpg)

**Milestone-triggered pulse:** The operational context tells the system when high-stakes moments are approaching. One week before design lock, the AI checks in: "How are you feeling about the design closing next week? Anything unresolved?" After a major delivery: "That sprint is done. What worked? What broke?" The timing is driven by the business, not a calendar.

**Agreement-grounded pulse:** The team agreement tells the system what to ask about. If the team agreed "flag issues early," the pulse at week 3 asks: "Anything worth flagging before it gets bigger?" If a role boundary was important during onboarding, the check-in at a coordination crunch asks about that specifically.

Elena flagged "prep time" in week 2; two weeks later, her department is at 94% with a new scene landing. The nudge isn't a cold alert — it's informed by what she herself said. Pulse trends show energy dropping. Combined with workload data, this becomes a signal before anyone escalates.

This source is strictly private at the individual level. Only anonymous aggregates reach the dashboard.

### How the sources work together

No single source is sufficient. The ontology without team agreements is generic. Team agreements without operational context can't detect consequences. Operational context without the ontology can't interpret what a schedule gap means for this team. Coaching without the other three is just a chatbot asking "how are you?"

**The hypothesis we're validating:** these four sources — ontology, team agreement, scoped operational context, and milestone-triggered pulse — are sufficient to deliver the core value proposition. This is the 80/20. If this combination catches problems early and makes coaching meaningful, we have the product. Everything beyond this (full data integration, meeting analysis, chat processing) is upside to prove later.

---

## 3. What the User Experiences

The user never sees the ontology, the data layer, or the agreement structure. They experience a private coach and a dashboard.

### The private coach

![The Onboarding Conversation](site/diagrams/plia-teams-08-onboarding-conversation.png)

The coaching starts before day one — the AI's onboarding prep is the first coaching interaction. From there, the system continues in five modes:

**Onboarding prep** — the AI learns what matters to you, while surfacing what the organization has learned. This feeds the human-facilitated session.
> "You're the production designer on Alfonso el Sabio. In 3 of the last 5 productions, scene changes hit art departments without budget approval. How should your team handle that?"

**Agreement check-ins** — the team's own words reflected back.
> "Your team agreed: 'flag issues early — a problem shared in week 2 is a conversation, in week 6 it's a crisis.' You're in week 3. Anything worth flagging?"

![The Coaching Mirror — Lucia](site/diagrams/plia-teams-10-coaching-mirror.png)

**Reflection-based** — from self-reported pulse data over time.
> "You've said 'rushed' twice in three weeks. What's driving that?"

**Milestone-aware** — triggered by operational context at key moments, not arbitrary calendar dates.
> "Design lock is next week. Your team agreed that unresolved scope questions should surface before lock, not after. Anything open?"

**Workload-aware** — from operational data, delivered privately.
> "Your department is at 94% allocation with 3 new requests in the queue. No days off in 12 days. Is this sustainable, or do you need to raise it?"

![Elena receives a private coaching nudge](site/diagrams/plia-teams-06-elena-nudge.png)

The coach remembers what you said, notices patterns in your own reflections, and asks one question. Then it waits.

### Sara's dashboard

Sara runs multiple productions. She can't be in every room. Her dashboard shows her where to pay attention — consequences and patterns, never individual behavior.

![Sara's 5-Minute Scan](site/diagrams/plia-teams-09-sara-dashboard.png)

| Production | Status | Key signal | Days open |
|---|---|---|---|
| Alfonso el Sabio | Yellow | Schedule/budget gap: scriptorium scene. Unit sync inactive. | 8 / 11 |
| Cacao y Compania | Yellow | Overdue: location permits. | 3 |
| CAPA Docuseries | Green | Clean. | — |

Pattern alert: "Scene approval bypasses in 2 of 3 productions — may indicate systemic gap in approval process across iZen."

What Sara doesn't see: who caused it, who was coached, who said what in their pulse, who ignored a nudge. She sees consequences and patterns. People, not the system, decide what to do about them.

The line producer gets the same data at daily-operations altitude. The consultant gets an intervention map. Same signals, three views.

---

## 4. The Trust Architecture

The product dies if people feel watched.

![The Trust Architecture](site/diagrams/plia-teams-03-trust-architecture.png)

Three principles:

**The individual always knows first.** If the system notices something about your behavior, it tells you before anyone else. Marcos is bypassing the approval process? Marcos gets the private nudge. If he doesn't act, the consequence — an unapproved scene on the schedule — surfaces on the dashboard. Not his behavior.

**Coaching is private. Always.** Your conversations, reflections, and pulse responses belong to you. Management never sees individual coaching data. The wall is technical, not policy.

**Aggregation is anonymous.** Management sees "art department energy dropped from 8 to 5" — not "Elena said 5." The dashboard surfaces patterns, never names.

![Two Layers, One System](site/diagrams/plia-teams-02-two-layers.png)

The onboarding conversation is also the transparency conversation. Spoken out loud, as a team: here's what the system observes in your work channels, here's what it never does. People already opted into PLIA processing their chats for operational purposes. The human-layer observation is pattern-level on top of that same data. Not new access. New interpretation.

---

## 5. We Don't Act

PLIA agents do work — order props, track budgets, resolve logistics. This product does nothing tangible. It holds up a mirror.

The system does three things:
1. **Remembers** what you agreed to — when you've forgotten or drifted
2. **Reflects** patterns you can't see from inside
3. **Asks** — one question, privately, that you can ignore

It never acts. It never escalates without your knowledge. It never does the hard conversation for you. The hard conversation is still hard. The system just makes it harder to avoid.

**"We don't fix teams. We make it easier for teams to fix themselves — and harder to pretend everything's fine."**

**"You don't have to remember. We remind you, structurally."**

---

## 6. The Operational Data Layer

![The Operational Data Layer](site/diagrams/plia-teams-04-operational-data-layer.jpg)

The product adds a human-coordination layer on top of whatever operational tools a client already uses: the ontology (cross-team lessons, methodology), team agreements (what each team said they'd do), coaching history (what individuals have flagged), and pulse signals (self-reported energy and concerns).

This is new data — but it's lightweight to capture. People tell the system things through conversations, not forms. The ontology is seeded once per client by the consultant-engineer. The heavy infrastructure is what the client already built.

**For PLIA:** Their operational layer already processes schedule, budget, logistics, and script data. We integrate at the milestone and deliverable level — enough to know when key moments happen and what's at stake, without ingesting every line item. The real value: operational data that already exists gets reinterpreted through the human-coordination lens. "Unbudgeted scene on schedule" is an operational fact. Seen through the ontology ("this pattern derailed Cacao y Compania") and the team agreement ("we agreed to flag these early"), it becomes a signal that matters for people, not just logistics.

**For other environments:** A software team's Jira tells us sprint milestones and workload. A consulting firm's deliverable tracker tells us deadlines and dependencies. The integration is scoped to key moments and deliverables — the minimum context that makes coaching timely and the dashboard grounded.

---

## 7. The Moat

![The Moat](site/diagrams/plia-teams-12-moat.jpg)

The product lives in a world where AI tools are commoditizing fast. In 36 months, any team could wire up a generic AI to read their Slack and summarize meetings. That's not what we build.

**The moat is the accumulated intellectual property — not the software.**

Three things compound and can't be replicated by a generic tool:

1. **The ontology** — cross-team behavioral knowledge that grows with every deployment. By the 10th production, the system knows things no individual consultant remembers. By the 50th team across industries, the system has organizational wisdom.

2. **The methodology** — 20+ years of Axialent's HPT process, structured into the system's architecture. Not as a static framework, but as a living engine that adapts to context. The methodology layer is designed to be composable — it starts with Axialent's approach but can incorporate complementary frameworks (Lencioni for diagnosis, Tuckman for stage-awareness, others) as the product matures.

3. **The trust relationship** — individuals share things with this system because it proved value to them first, kept their data private always, and never surprised them. That trust takes time to build and can't be bootstrapped by a new entrant.

A dashboard can be copied. A feature can be matched. An ontology that carries the behavioral learnings of hundreds of teams, interpreted through proven methodology, delivered through a trust relationship that took months to earn — that's the product.

---

## 8. Scaling

Today Sara has zero coverage of the human layer. The only option — a consultant embedded per production — is too expensive and too intrusive. So she gets nothing.

With this product, one consultant covers all seven productions:
- **Seeds the ontology** once per client, refines it per production
- **Reviews AI-prepared onboarding** syntheses, shows up for kickoffs
- **Monitors the dashboard** across all productions — intervenes where it matters
- **Does the hard conversations** in person when the system flags something the AI can't handle

The AI does the daily work — coaching, nudges, pulse, drift detection. The consultant does the judgment calls. Neither replaces the other.

---

## 9. The 80/20 Hypothesis

![The 80/20 Hypothesis](site/diagrams/plia-teams-11-eighty-twenty.jpg)

Before building deeper integrations, we validate a core hypothesis:

**Is the combination of ontology + team agreement + milestone-triggered pulse + scoped operational context + a human coach sufficient to catch team problems early and make coaching meaningful?**

This is the pareto question. We believe that "just" having a strong ontology and team agreement gives you enough to coach people on drift, surface tensions, and give signals to Sara and the coach. The gap between what people said they'd do and what they're doing — measured through pulse, interpreted through the ontology, grounded in business milestones — might be the 80% of the value.

**What we need to validate with PLIA:**
- What's the minimum slice of operational data that makes coaching timely? (Key moments and deliverables, not every line item)
- Is the team agreement + ontology enough context for the AI to give coaching that feels specific and useful?
- Do milestone-triggered pulse surveys generate better signal than periodic check-ins?
- Does Sara find the dashboard actionable without full operational data integration?

**What's explicitly beyond the minimum lovable product:**
- Processing all team chats and emails (separate privacy/consent gate, high complexity)
- Joining and analyzing meetings (requires trust already established, multiple hypothesis layers)
- Full granular budget/schedule integration (precision upgrade, not a prerequisite)
- Commitment network extraction (valuable but complex — see Appendix C)

If the 80/20 validates, everything beyond it is a precision upgrade. If it doesn't, we learn exactly what's missing and scope the next layer.

---

## 10. Beyond Production

![One Engine, Any Industry](site/diagrams/plia-teams-14-pluggable-architecture.jpg)

Every industry where teams coordinate complex work has the same pattern:

| | Film Production | Software | Consulting |
|---|---|---|---|
| What needs to be done | Scripts | PRDs / specs | SOWs / scopes |
| Who does what when | Movie Magic | Jira / Linear | Deliverable trackers |
| Resources | Movie Magic Budget | Roadmaps | Time tracking |
| Where people talk | Google Chat | Slack / Teams | Email / Teams |
| **What's missing** | **The human layer** | **The human layer** | **The human layer** |

The architecture is built for this from day one. The ontology, team agreement, coaching engine, pulse mechanism, and trust architecture are industry-agnostic. What changes per deployment is the operational data source and the domain-specific knowledge seeded into the ontology.

Production is where we start — because PLIA gives us the data layer and Axialent gives us the methodology. But the operational data layer is a pluggable interface, not a hardcoded integration. When we move to software teams, the ontology gets seeded with engineering coordination patterns instead of production patterns. The pulse gets triggered by sprint milestones instead of shoot schedules. The coaching asks about standups and code reviews instead of scene approvals.

*Sara couldn't afford this before. Now she can — and every production makes the next one smarter.*

---

## Appendices

### A. Grudin's Law — The Design Constraint

Jonathan Grudin's finding: if the people doing the work don't get direct personal benefit, they won't use the system. This is the single most common cause of death for team collaboration tools.

Our constraint: every interaction must give the person doing it something they want. The team-level intelligence is a byproduct of individuals getting value — never the other way around.

### B. What This Is Not

- **Not a dashboard company.** Dashboards inform conversations. They don't replace them.
- **Not a personal AI.** That's being commoditized. We're the team layer your personal AI can't do alone.
- **Not a surveillance tool.** Consequences and patterns surface. People don't.
- **Not a project management tool.** We integrate with PM tools for context. We don't replace them.

### C. Future Enhancement — The Commitment Network

The product works without commitment extraction. It becomes a future intelligence upgrade that adds:
- **Specificity** — not just "unbudgeted scene on schedule" but "Marcos committed Elena without her knowing, propagated through three people into a fait accompli"
- **Sharper coaching** — patterns across extracted commitments, not just operational data
- **Propagation tracking** — how assumptions harden: verbal opinion to assumed confirmation to scheduled work
- **Bilateral validation** — did both sides confirm the same understanding?

Start without it. Add it when real usage data tells you where it adds the most value. (Discussed and deliberately deferred — the complexity of reliable commitment extraction is a separate problem that someone else may solve first.)

### D. Future Enhancement — Cost-of-Dysfunction Dashboard

Sara's dashboard currently shows consequences and patterns. A future layer adds estimated financial impact: what is this problem costing you?

- Delay costs from coordination failures
- Replacement costs when someone leaves mid-production
- Rework costs from misalignment caught late vs. early
- Aggregate savings estimate: "This system has surfaced X issues that, based on historical patterns, would have cost $Y if caught at crisis stage instead of early stage"

Thierry's methodology for quantifying team misalignment cost is a starting point. This layer turns the dashboard from "here's a problem" into "here's what this problem costs you" — a retention and selling mechanism. **Open question: is this part of the minimum lovable product or v1.1?** Our current hunch: the product is lovable without it (going from nothing to visibility is the first win), but this is what makes it unjustifiable to cancel.

### E. Future Enhancement — Additional Lenses

The ontology is designed to absorb richer context over time. Future enrichments include:

- **Personality assessments** (DISC, OCI, etc.) — understand team composition, anticipate friction points ("too many chiefs, not enough builders"), tailor coaching to individual communication styles
- **Company moment / context** — expansion, contraction, restructuring, market shifts. The same team needs different behaviors in different moments. A company growing aggressively needs risk-taking; one contracting needs empathy and clarity. This changes what "good" looks like for the same team.
- **Team archetypes** — where is this team in its lifecycle? What are its structural risks based on composition? A team with seven nationalities has different coordination challenges than a homogeneous local crew.
- **Network analysis** — from communication metadata (not content), map information flow: who are the brokers, where are the bottlenecks, who is isolated? This is Leo's Team Dynamics Map concept — powerful but requires a separate data access gate.

These lenses enrich the ontology and sharpen coaching. The product architecture should be flexible enough to incorporate them without rebuilding — but none are prerequisites for the minimum lovable product. Pick one, layer it, learn, repeat.

### F. Future Evolution — Meeting Integration

A future product evolution progressively enters meetings:
1. **Pre-meeting briefing** — before key meetings, the facilitator gets a 3-line synthesis of relevant team dynamics
2. **Silent observer** — joins meetings as a participant, measures participation and energy without recording content
3. **Pre-meeting prep** — contextual briefing with patterns and suggestions for the facilitator
4. **Real-time co-facilitation** — sidebar visible only to the facilitator with gentle suggestions
5. **Post-meeting coaching** — differentiated summaries per role, one suggestion for next time

Each stage requires trust already established from the coaching relationship. This is explicitly outside the minimum lovable product — it sits behind the validation of the 80/20 hypothesis and requires its own consent/privacy gate.
