# Leadership Alignment: Q1 2026 Direction

> **For:** Oseas, Leo, Mike, Nelson
> **From:** Ruy
> **Purpose:** Commit to the direction so we can execute
> **See also:** [vision.md](vision.md) for platform vision, [vision-behavior-change.md](vision-behavior-change.md) for LD product spec, [MVP-offer-hpt.md](MVP-offer-hpt.md) for HPT product spec, [roadmap.md](roadmap.md) for engineering roadmap
> **Updated:** January 29, 2026

---

## Why

**We help people have better conversations — with themselves and their teams.**

That's what drives leadership development. That's what makes teams effective. A leader who can listen instead of dominate. A team that honors its commitments instead of letting them drift. An organization where people show up consciously, not reactively.

Coaching is how you get there — the mechanism that helps people see their patterns, close the gap between intention and behavior, and actually change.

---

## What We're Building

An **AI Coach with memory** — persistent, scalable, embedded in the flow of work.

Not a chatbot. A system that knows where you started, what you're working on, where you've struggled, and what's next. It remembers your journey across sessions, adapts when you struggle, and connects daily actions to who you want to become. Always present — not a session you attend and forget.

![The experience: reminded of what matters, sees progress, acts with intention](../site/diagrams/gps-dashboard-comic-strip.png)

This AI Coach is the core engine. Once it works, it powers two design spaces:

- **Leadership Development** — Help individuals have better conversations with themselves. Close the gap between who they say they want to be and who they show up as. Behavior change at scale.
- **Team Effectiveness** — Help teams have better conversations with each other. Track commitments, evolve together, turbocharge team performance. This works because individuals are actually growing.

We're not choosing between these markets — we're building the foundation that makes both possible.

---

## The Bet

We are building **one platform with two design spaces** — Leadership Development and Team Effectiveness — sharing the AI Coach as common foundation. The Q1 shared foundation enables excellence in digitizing both paths. We coordinate validation efforts with Axialent.

### What's Hard to Replicate
- The complete behavior change methodology (grounded in research, not intuition)
- The system that orchestrates the entire cycle (goals → habits → adjustment → evolution)
- The integrations that create stickiness (reach users where they are)
- The structured memory of the user's change trajectory
- The accumulated knowledge of what interventions work, when, and how

### Jan 28 Decisions (Oseas, Nelson, Mike, Ruy)

1. **AI Coach is the shared technology investment** — build this first, it unlocks both LD and HPT
2. **Validate both markets in parallel** — see which has customer pull
3. **HPT validation uses current product** — Nelson leads with slides and visual prototypes
4. **Impact visibility in lockstep** — coaching quality and reporting quality must advance together
5. **Commercial validation required** — Thierry + Fernando Fascioli review all product direction
6. **Don't over-design HPT now** — co-design with Dolo is Q2+. Focus on common foundation.
7. **Stoic is a separate spin-off** — commercial relationship with Axialent unresolved

**Full vision:** [vision.md](vision.md) — covers why we exist, the two design spaces, strategic filter, and what's shared

---

## Q1 Strategy: Validate + Build

The shared foundation we build in Q1 enables both design spaces. The AI Coach, Teams integration, and check-in loop are not LD-specific — they're the platform layer that makes both LD and HPT digitization possible.

We run two tracks in parallel, coordinated with Axialent:

| Track | Owner | What Happens |
|-------|-------|--------------|
| **Validate** | Leo + Nelson | Run customer conversations for LD and HPT. Test if direction resonates. Track requests by path and source. |
| **Build** | Mike + Shamil + Daniel | Ship shared foundation: Teams notifications, check-in loop, Thinking Partner, Coach Multi-Session. |

---

## Q1 Scope

### What We're Building

| Feature | Owner | Status | Why It Matters |
|---------|-------|--------|----------------|
| MS Teams Notifications | Mike | In progress | Reach users where they are. Foundation for check-ins. |
| Check-in Loop | Shamil | Ready to build | Loop instead of end. Users can continue, modify, or escalate to Coach. |
| Thinking Partner: Challenge/Gap/Commitment | Shamil + Ruy | Ready to build | Show and store challenge, gap, action plan commitment. |
| Coach Multi-Session | Ruy + Shamil | Needs Horacio | Coaching with memory. Tracks goals, progress, what's urgent vs planned. |
| Voice OR Bidirectional Chatbot | TBD | Validate with Leo | Choose one based on customer pull. |

### Q1 Validation Experiment

| Aspect | Details |
|--------|---------|
| **Users** | Mix of friendly clients, Leo's pipeline, internal (TBD) |
| **Owner** | Ruy + Leo |
| **Duration** | 2-3 weeks |
| **Goal** | Validate utility and approach, not behavior change outcomes |

**What we're validating:**

| Principle | How We Test It |
|-----------|----------------|
| Multi-session Coach feels like a coach who knows you | Do users reference previous sessions? Do they feel continuity? |
| Check-in loop keeps people engaged | Do users loop? Do they modify habits when stuck? |
| "Don't nag, give alternatives" works | When users struggle, do they feel supported vs. guilty? |
| Connected goals matter | Do users see how daily actions connect to what they want? |

**Signals we're looking for:**

| Signal | Question |
|--------|----------|
| Came back | Did they use it more than day 1? |
| Found it useful | "This helped me" vs "It's nice but..." |
| Felt supported when stuck | "It gave me options" vs "I felt bad for failing" |
| Would continue | "I want to keep using this" |

**NOT measuring yet:** Actual behavior change outcomes (too early), completion rate percentages (not enough volume), NPS scores (need more users first).

### What's NOT in Q1
- GPS Dashboard (needs goal storage foundation first)
- Full context integrations (calendar, email)
- HPT engineering (validation uses current product)
- Peer accountability features

---

## What's Decided vs What's Not

### Decided

The 7 decisions above. We're building the AI Coach as shared foundation, validating both markets, and shipping a sellable Application Coaching experience in Q1.

### Not Decided

| Open Question | How We Resolve It |
|---------------|-------------------|
| **Are we differentiated or 80/20 replaceable?** | Competitive research. Can a $10/month app or good GPT prompting do 80% of what we do? We assume our methodology + orchestration + memory is hard to replicate — but we haven't proven it. Competitors exist: Torch, MindGym, Cloverleaf, plus every generic AI coaching app. |
| **Stoic's commercial model** | Does Stoic sell independently or operate as Axialent's digital arm? |
| **Where to go deep — LD, HPT, or combined?** | Customer pull tells us. Both paths will generate requests. The question isn't "kill one" — it's "what's the common layer that serves both?" |
| **Pricing model** | Does digital add-on increase ticket (100→115) or decrease it (100→50)? |
| **Long-term team effectiveness product** | Beyond the MVP, the full vision is sketched but not designed. |

These are the real unknowns. The alignment we're asking for is on the **direction** — build the shared foundation, validate both paths, let evidence guide depth.

---

## PMF Process

We're consultants. Our DNA is to tailor everything for every client. That instinct is the enemy of product-market fit. We need a disciplined process to find the repeatable pattern.

### What We Track

| Dimension | What We Capture |
|-----------|-----------------|
| **Customer requests** | Every feature request, tagged: LD, HPT, or shared |
| **Request source** | Axialent pipeline vs direct Stoic client |
| **Sales signal** | Did the conversation shift from "nice chatbot" to "this is different"? |
| **What opened the door** | Which positioning/feature got the meeting or moved the deal? |

### Who Owns It

- **Leo** owns tracking — captures every customer conversation and request
- **Ruy** reviews — aggregates patterns, connects to roadmap decisions

### How We Decide What to Build Next

1. Build shared foundation first (serves both paths)
2. Path-specific features only when pull is undeniable and repeated
3. When both paths request the same underlying capability → that's the signal to invest
4. Current product gets bug fixes and ship-what's-built only. New features go to the new vision.

### What Evidence Looks Like

We may not get a clean "kill this path" signal. Both paths will likely generate requests — from Axialent for HPT, from direct clients for LD. The question isn't which path to kill. It's:

- **What's the common layer?** If both paths keep requesting the same underlying capability, that's the core.
- **Where's the pull strongest?** Not just volume of requests, but strength of signal — are people ordering, or just saying "sounds interesting"?
- **What are prospective customers asking for?** Future orders matter more than friendly feedback.

---

## Key Risks

| Risk | Why It's Real | Mitigation |
|------|---------------|------------|
| **Capital** | Runway is finite. Both paths need investment. We can't do everything. | Speed to signal. Q1 validation tells us where to go deep before money runs out. If neither path shows pull by end of Q1, we reassess. |
| **Scope creep from two design spaces** | Two paths = constant pressure to split focus. Every client conversation pulls in a different direction. | Shared foundation first. Path-specific only when pull is undeniable. The strategic filter: does it scale a consultant or augment a consultant? If not for both paths, it waits. |
| **Visibility as scope creep** | "Make invisible visible" (Oseas principle) is infinite — you can always build one more dashboard or report. | Visibility features get built only when they're blocking a sale. Not "what would be cool to show" but "what makes a buyer say yes." |
| **Current product gravity** | Existing clients and sales pull toward incremental improvements on what exists, not the new bet. | Clear rule: current product gets bug fixes and ship-what's-built (STT, Executive Summary). New features go to the new vision only. |
| **Consultant DNA vs product discipline** | We're consultants. We tailor everything. That's the enemy of repeatable product. | PMF process above. Track requests, find patterns, resist custom work. Build the thing that 10 clients need, not the thing 1 client asked for. |
| **MS Teams blocked by client IT** | Enterprise IT can block our primary integration channel. | Fallback channels (email, web). Escalate early. |

---

## Your Role

| Person | What We Need From You |
|--------|----------------------|
| **Oseas** | **PMF owner** (confirmed Jan 30). Strategic alignment. Board communication. Drives validation via Nelson (HPT) and Leo (LD). Lockstep validation on visibility — help us know when visibility is blocking sales vs. nice-to-have. |
| **Leo** | Own PMF tracking. Run LD validation conversations. Track every request by path and source. |
| **Nelson** | Build Axialent Offerings. Axialent market validation. Impact/visibility design. Thierry coordination. See [MVP-offer-hpt.md](MVP-offer-hpt.md) for HPT product spec and [team effectiveness research](../team-effectiveness/research/synthesis-v2.md) for methodology background. |
| **Mike** | Ship Teams notifications. Support Shamil on multi-session architecture. Flag blockers early. |
| **Shamil** | Check-in loop, Thinking Partner, Coach features. |
| **Daniel** | Infrastructure, deployment automation. |
| **Ruy** | Methodology, roadmap, Coach design (demo-able MVP + concept visuals). Produces showable artifacts for PMF validation. |

---

## The Question

> Are we aligned on this direction?
>
> If yes, we start executing. Leo and Nelson validate, Mike, Shamil, and Daniel build. Ruy coordinates.
>
> If concerns, let's surface them now — not after we've started building.

---

*Document version: January 29, 2026*
