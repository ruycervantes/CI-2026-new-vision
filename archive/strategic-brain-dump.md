# Strategic Brain Dump: 2026 Planning

*Working document for January offsite with Oseas*

---

## 1. Operational Commitments (Must Handle)

Current client commitments that require execution regardless of strategic pivot:

| Client | Status | What's Needed |
|--------|--------|---------------|
| TELUS International | Active | User onboarding, ongoing support |
| Aleatica | Committed | Onboard new users, create chatbots |
| Sigma | Possible | TBD |
| P&G | Active | SSO now working, continued support |
| Caja Popular Mexicana | Active | Recently onboarded 70 users |

### Aleatica Decision Point
- Already passed security reviews — significant sunk cost
- **Binary choice:** Sell ConsciousInsights as-is OR drop the deal
- Not feasible to switch them to another platform after compliance work

---

## 2. Chatbot Creation Bottleneck

**Current state:** Creating new chatbots takes too much of Ruy's time (3-4 days per client)

### Partial Solutions in Place
- Skills automation process (some improvement)
- Documentation of best practices

### Options to Explore
1. **Build a wizard/interface** — like Edumi's practical chatbot creation flow
2. **Use existing LMS with AI** — Nelson showed solutions with built-in AI scenario creation
3. **Systematize the process further** — templates, better tooling
4. **Automate prompt creation with Claude skills** — create scaffolding based on existing prompts to generate new ones faster

### Prompt Automation Idea
> Based on the prompts we have, could create Claude skills that scaffold new prompt creation. Lots of patterns are reusable — this could significantly reduce the cognitive load of chatbot creation.

### Open Question
> How do we create chatbots without requiring so much of Ruy's cognitive load?

---

## 3. Build vs. Partner/Platform Decisions

### The Upstream Dependency
> Build vs. partner decisions depend heavily on the strategic split between Stoic and Axialent. What does Stoic own? What does Axialent do? Until that's clear, these decisions are hard to make.

### Option A: Improve Our Platform
- Create better interfaces for chatbot creation
- Invest in making ConsciousInsights self-service
- Pros: Own the product, control roadmap
- Cons: Development time, still need to sell B2B enterprise

### Option B: Use Third-Party LMS + Our AI Layer
- Nelson showed LMS solutions with AI scenario practice built in
- Could work for Axialent's cohort-based learning
- Pros: Faster to market, less maintenance
- Cons: Dependency, less differentiation, margins

### Key Insight
> If we take ideas from other platforms and build our own, we'd need to sell to individuals/B2C — probably not the right direction given enterprise focus.

---

## 4. Strategic Product Directions

### Direction A: Culture Dashboard
**Client interest:** CrediCorp wants a pilot

**Components:**
- AI transcription of meetings → behavior analysis
- AI-based assessments (alternative to Brilliant?)
- Culture measurement over time

**Nelson's idea:** Start collecting Stoic's own team calls to experiment with extracting behaviors — dogfooding the culture dashboard concept.

**Questions:**
- Is this a pivot from coaching to analytics?
- What's the competitive landscape?
- How does this relate to what we already have?

---

### Direction B: Team-Level Dashboards
**Concept:** Take culture solution and bring it down to team level

- More actionable than org-wide culture metrics
- Connects to team effectiveness research
- Could feed into coaching interventions

---

### Direction C: Team Effectiveness / HCI Research Direction
**Source:** Papers from HCI, CSCW conferences

**Research Groups Identified:**
| University | Researcher | Notes |
|------------|------------|-------|
| Notre Dame | Diego Gómez-Zará | Downloaded code to study |
| Clemson | Nathan McNeese | |
| Rice | Unhelkar (Socratic) | Via Thierry |

**Why this research matters:**
- HCI/CSCW tradition = designing systems with the right interactions for usefulness and usability
- They've applied team performance frameworks for automated feedback in experimental settings
- Clear findings on what interactions work, how to measure impact
- Saves us methodological groundwork

**The Gap (Our Opportunity):**
> All these groups focus on the "IT": feedback on task execution, coordination, operational alignment.
> None are working on the "WE": feedback on interpersonal relationships, trust, psychological safety.
> **That's exactly what we know how to do.**

**Potential Partnership Value:**
1. Interaction patterns that work (from their research)
2. Help designing rigorous evaluations
3. European funding programs (academia + empresa) — relevant if Plia advances

**Prerequisite:** Strategic clarity on what we want to build. Without it, easy to get lost in research without landing something concrete.

---

## 5. Assessment Tool Problem

**Current pain:** Brilliant Assessments API is a nightmare
- Rate limits
- Not designed for our use case
- 3 sprints of Mike's time
- Will be unmanageable at scale

### Options
1. **Build our own assessment tool** — significant investment but full control
2. **Find alternative provider** — need to evaluate
3. **Use AI-based assessments** — Nelson mentioned a solution (paste details below)

**Decision needed:** Is assessment a core capability we need to own?

---

## 6. Automation & Packaging Priorities

To reduce operational burden and enable scale:

| Area | Current State | Target State |
|------|---------------|--------------|
| New instance creation | Mike: 2-3 days manual | Automated/self-service |
| Chatbot creation | Ruy: 3-4 days | Wizard or templates |
| User onboarding | Semi-manual | Streamlined flow |
| Prompt creation | Ruy-dependent | Nelson-capable or templated |

---

## 7. Unresolved Questions for Offsite

### Strategic
- [ ] What do we want to sell in 2026? (Current product vs. pivot)
- [ ] What's the ICP? (Enterprise size, industry, region)
- [ ] How do we avoid compliance nightmares? (Data residency, security reviews)
- [ ] What's the Axialent/Stoic boundary? (Revenue, costs, IP)

### Operational
- [ ] Who maintains current product if we pivot?
- [ ] How do we reduce Ruy's operational load?
- [ ] What can be handed to Nelson/Axialent?
- [ ] What needs Mike's continued involvement?

### Team
- [ ] How does Ruy stay in the loop with Barcelona centralization?
- [ ] What's Mike's actual role? (Coding vs. orchestrating)
- [ ] How do we work with external dev team (Arcadia or similar)?

---

## 8. Q1 2026 Focus (Draft)

### The Clarified Approach

**Memory:** Start with "team of one" — individual memory across chats using Graffiti. Mike has a proposal. This is the foundation; team memory comes later.

**MS Teams:** Strip to bare minimum — a chatbot that sends notifications for check-ins. That's it. No complex slash commands.

**Thinking Partner:** Already built. Needs polish and validation.

---

### Q1 Candidates (Prioritized)

| Priority | Item | Effort | Notes |
|----------|------|--------|-------|
| 🔴 | **Show Thinking Partner to Oseas** | Low | Voice feature will click differently than talking about it |
| 🔴 | **Polish Thinking Partner** | Medium | Mike could work on rough edges during winter break |
| 🔴 | **Test Thinking Partner with internal users** | Low | Axialent enthusiasts, CB community — get signal if people like it |
| 🟡 | **Individual memory (team of one)** | Medium | Graffiti-based, Mike's proposal |
| 🟡 | **MS Teams notifications MVP** | Medium | Already scoped down |
| 🟡 | **CPM: Push accountability partner usage** | Low | Bug in Nelson's session meant it wasn't shown in onboarding — need recovery action |
| 🟢 | **Offer Thinking Partner free to existing clients** | Low | Aleatica, P&G, TELUS — "we built this, want to try it?" — gets usage data for free |
| 🟢 | **Aleatica chatbots** | High | Committed, but timing flexible? |
| ⚪ | **Assessment tool** | High | Needed but not wanted — defer if possible |

---

### What's NOT in Q1
- Full team memory
- Culture dashboard (prototype exists, but not focus)
- New client onboarding beyond commitments
- Building our own assessment tool

---

### Immediate Actions (Before Vacation)

1. **Show Oseas the Thinking Partner** — with voice, live demo
2. **Align with Mike** on what he can polish during break
3. **Brain dump cleanup** — get backlog out of head, into Asana (not a system change, just cleanup)

---

## 9. Development Priorities for 2026

### Core Platform Extensions

| Priority | Description | Strategic Value |
|----------|-------------|-----------------|
| **Teams/Org Memory** | Memory across teammates, across chats | Foundation for any "team effectiveness" solution |
| **Thinking Partner / Orchestrating Agent** | Jump steps, jump profiles | Enables flexible coaching experiences |
| **MS Teams Integration** | Be present in tools people already use | Distribution/adoption |
| **Assessment Tool** | Build our own (not wanted, but needed) | Escape Brilliant API nightmare |

### Memory MVP Insight
> The MVP for memory might be: memory across chats for effective individual coaching first. Then extend to team memory.

---

## 9. Strategic Focus Options (Pick One or Combine)

Three possible focal points — can be mixed:

### Focus A: Individual
- Coach individuals
- Give personal insights
- Current ConsciousInsights strength

### Focus B: Team
- Individual coaching that rolls up to team
- OR direct team coaching
- Team memory enables this

### Focus C: Organization/Culture
- Understand individuals → gain cultural insight
- Culture dashboards, org-wide analytics
- Aleatica prototype direction

### Key Insight
> These can be combined. E.g., "Focus on individuals but gain organizational insight" or "Team coaching with culture measurement." But we need to decide the primary lens.

---

## 11. The ConsciousInsights Lego Advantage

**What we have:** A working, compliant, configurable platform

**The point:** Not that we plan to build all combinations — but that we *can* prototype faster because the foundation exists.

**Examples of fast prototyping:**
- Thinking partner: idea → working prototype in focused week
- Team memory: Graffiti already has the approach, Mike has proposal
- New chatbot types: Skills are semi-automated now

> "The Lego advantage is that it's there, and we can use what we have to prototype faster."

---

## 11. Learning Loops (Acceleration)

### Learning from Customers
- **Customer sprint** — align Rodrigo's effort tightly with product learning
- Structured feedback → product decisions

### Get Beta Users
- Internal (Axialent)
- External pilots
- Essential for validating before big builds

---

## 12. Work Organization Challenges

### Current Pain Points
- Need more visibility on tasks at different levels
- Bug fixes, new features, experiments all competing
- Backlog decisions made "as God gives me to understand"
- Missing structured product management process

### What's Needed
- Product roadmap (clear, shared)
- Way to organize features AND experiments
- Balance current workload vs. new development
- Flexibility for change (don't over-commit)

### Tools Discussion
- Asana limitations (jumping between boards)
- Linear? GitHub Issues?
- Decision deferred to sprint planning

---

## 13. Build vs. Partner — Option C Added

### Option A: Improve ConsciousInsights
- Build better interfaces, self-service chatbot creation
- Own the product fully

### Option B: Use Third-Party LMS + Our AI Layer
- Axialent cohort-based learning
- Less control, faster to market

### Option C: Third-Party LMS with Built-in AI Layer *(NEW)*
- Different from what we have
- Already has AI scenarios, practice tools
- Could be interesting for certain use cases
- Worth evaluating what they do better/differently

---

## 14. Resources & References

### AI Assessment Solution: InnerLogic
**URL:** https://www.innerlogic.com/

> "A smarter way to deploy your engagement strategy. Built on AI-native architecture, innerlogic provides the ultimate hub of employee engagement solutions for capturing meaningful feedback and turning it into strategic growth."

**Features:**
- Intelligent surveys with conversational AI
- Automated reporting workflows for instant impact
- Scalable action planning & manager activation tools

**Potential:** Could we build something with this? Or partner? Alternative to Brilliant nightmare.

### LMS Solutions Reviewed
- Edumi (or similar) — wizard for chatbot creation
- Solution with AI scenario practice built-in
- *Add more details from Nelson's demo*

### Relevant Research Papers
- HCI papers on human-AI collaboration
- CSCW papers on team effectiveness
- *Add specific references*

---

## 16. Ruy's Growth Edge

### PM Reality Check

> "I need to get my shit together and put the backlog somewhere."

**The actual problem:** Backlog exists but is scattered and unorganized (Asana + Notion graveyard). Not a skills issue — a cleanup issue.

**What to do:**
- Don't change systems (Linear migration = more work)
- Streamline what's in Asana
- Clean up the Notion graveyard
- Get it out of your head and visible

**When:** After vacation, when mental energy returns. Not now.

---

## 17. Ruy's Constraints & Needs

### What burns me out
- High-cognitive-load tasks piling up
- "Invisible" operational work (compliance, integrations, fixes)
- Believing I can do 10 complex tasks/week (I can't)
- Gap between strategy and execution capacity

### What I need
- Working sessions with Oseas (not just syncs)
- Realistic scoping of Q1 goals
- Time/space for prototyping (thinking partner took 3 months of "next week")
- Not being out of the loop with Barcelona team

### What energizes me
- The team performance / research direction
- Building prototypes that work (thinking partner, culture dashboard)
- Solving real problems with AI + methodology

---

*Last updated: December 16, 2025*
