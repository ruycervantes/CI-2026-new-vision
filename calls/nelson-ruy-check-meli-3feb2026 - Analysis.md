# MELI Proposal Strategy Call - Strategic Analysis
**Date:** February 3, 2026
**Call:** Ruy + Nelson

---

## Meta-Theme

**This call was about turning abstract product vision into a sellable, deliverable offer.** Nelson is trying to create proposal materials for MELI; Ruy is providing product design guardrails. The conversation revealed the gap between "what we want to build" and "what we can promise to deliver in Q2."

---

## 1. Patterns and Recurring Themes

### The "Sobreenfocados en microhábitos" Problem
Both Ruy and Nelson converged on this independently. The current product design is microhabit-first, but:
- It doesn't match how coaching actually works
- It forces users into a structure that may not fit their needs
- It limits what the coach can do

**Pattern:** The team has been building toward a specific implementation (microhabits) when they needed to build toward a goal (behavior change). This is a common product trap.

### Nelson as Design Partner
Nelson isn't just asking questions to understand — he's actively shaping product direction:
- "¿Cómo coexisten o cómo funciona?" (pushing for clarity)
- "Eso del microhábito, tengo una duda" (raising methodology concerns)
- "Poner una idea loca" (bringing heartbeat concept)

**Pattern:** Nelson is functioning as an external product voice, grounded in what clients will accept.

### Ruy's "Todavía no lo tengo 100% bajado"
Ruy explicitly admitted the design isn't fully worked out. This is honest, but reveals that the MELI proposal is being built on top of incomplete internal alignment.

---

## 2. What's Said vs What's Implied

### Said: "Yo lo ofrecería así"
**Implied:** Ruy is designing the offer in real-time on this call. There's no pre-existing product-market fit spec being referenced.

### Said: "El reto es meterlo en Google Chat"
**Implied:** This is being positioned as the technical challenge, but the real challenge is that the coaching experience doesn't exist yet. Google Chat is a delivery vehicle for something that's still being designed.

### Said: "Para hacer eso, necesitas tener el contexto de base"
**Implied:** The "heartbeat" feature Nelson wants requires memory architecture that doesn't exist yet. This is a polite way of saying "not this quarter."

### Said: "Estoy pensando cómo lo usaría yo"
**Implied:** Nelson is stress-testing the product by imagining himself as a user. His example (upload a transcript of a difficult conversation) is a use case that isn't in the current design at all.

### Said: "Hay que ponerle un nombre"
**Implied:** The branding is being invented in this call. This is fine for early stage, but it means MELI will be the forcing function for brand decisions.

---

## 3. Technical Debt Being Created

### Promise: "6 sessions over 6 weeks"
**Debt:** This implies session continuity and memory. Current architecture doesn't support multi-session coaching relationships reliably.

### Promise: "Coach receives assessment context"
**Debt:** This requires integration between assessment system and coach. How does that data flow? Who builds it?

### Promise: "Personalized heartbeat reminders"
**Debt:** This requires:
- User context storage
- Proactive outreach infrastructure (not reactive chat)
- Message generation based on past conversations
None of this exists.

### Promise: "Two coach flavors"
**Debt:** This sounds simple ("just different knowledge bases") but actually means:
- Two sets of prompts to maintain
- Two testing paths
- Potential for divergence over time

---

## 4. Single Points of Failure

### Ruy as Design Bottleneck
All product design decisions flow through Ruy. Nelson can't answer client questions without checking with Ruy. This works for now but won't scale.

### Horacio as Methodology Source
Ruy mentioned: "Es un problema de sentarme con Horacio, con Tolo y empezar a afinar los prompts."

Horacio isn't on this call. The coaching methodology isn't documented in a way that others can build from. If Horacio is unavailable, the coach development stalls.

### Memory Architecture Not Decided
Ruy: "Tengo que tener muy bien aterrizada la memoria."

This is the foundational technical decision that enables everything else. It's still open.

---

## 5. Process Gaps Revealed

### No Product Spec
This call is generating product design, but where does it get documented? Ruy said "voy a aterrizar todo esto en documentos" — meaning it's not documented yet.

### No Pricing Framework
They discussed features but never mentioned pricing. How does 6 sessions vs 12 sessions affect cost? What's the per-user price point? MELI will ask.

### No Capacity Planning
If MELI wants to start Q2 with 100+ leaders, can the team deliver? The call didn't address scale.

---

## 6. Alignment Gaps

### Nelson's Transcript Use Case
Nelson asked: "Si yo te digo, oye, acabo de tener una conversación difícil con mi jefe... ahí te va el transcripto. ¿Cómo cachamos algo así?"

This is a real user behavior (people share transcripts for coaching). Ruy's response: "No sería el caso de uso con el que empezaría."

**Gap:** Nelson is thinking about what users actually do; Ruy is thinking about what's buildable. Both are valid, but they need explicit prioritization.

### Content Strategy Ambiguity
Ruy: "Por un lado se me hace padre y por el otro lado siento que podemos sobresaturar a las personas de demasiado chatbot."

This isn't resolved. The content delivery approach (Axia-learning-mode vs content catalog vs email) is still TBD.

---

## 7. Measurement Gaps

### No Success Metrics Discussed
What does "the coaching worked" look like for MELI? How do we prove ROI? Neither Ruy nor Nelson raised this.

### No Usage Tracking Design
Nelson's "token counter" idea was one attempt at this, but Ruy was skeptical. What WILL they track?

### No Client Lifecycle Visibility
How do we know if someone completed their 6 sessions? If they stopped at session 3, why?

---

## 8. Strategic Implications

### Q2 Timeline is Aggressive
MELI wants Q2-Q3. That's 2-3 months. The current state:
- No memory architecture
- No multi-session coaching flow built
- No Google Chat integration
- Prompts need refining with Horacio

This is a lot to deliver while also supporting existing clients.

### MELI is Shaping the Product
MELI's requirements are driving design decisions:
- Google Chat (because that's what they use)
- Post-workshop reinforcement (because that's their lifecycle)
- Two coach flavors (because they have two programs)

**Risk:** Building custom for MELI might not generalize. **Opportunity:** If it works for MELI, it validates the approach at scale.

### The "Axia" Decision is Real
Naming the coach "Axia" isn't just branding — it's a positioning decision. They're committing to a personified AI coach with "different flavors." This is the right direction but requires consistent execution.

---

## 9. Warnings and Risks

### Ruy's Personal Bandwidth
Ruy mentioned buying a depa, receiving IKEA furniture, child helper being sick. These are normal life things, but they're eating into work time on a 3-month runway.

### Promise-Capability Gap
The call generated several promises:
- Coach with persistent memory
- Heartbeat-style proactive outreach
- Two specialized coach flavors
- Content delivery system
- Group coaching for supervisors

Each promise is individually reasonable. Together, they exceed current capacity.

### No Written Agreement Yet
This is all verbal. Nelson is going to create slides. What if MELI interprets the offer differently than intended?

---

## 10. Hidden Dependencies

### MELI's LMS Decision
The content delivery discussion hinged on "nuestro LMS o el de ellos." This is a client decision that affects technical scope.

### Horacio/Tolo Availability
Refining prompts requires coaching experts. Their availability isn't mentioned.

### Mike's Capacity
Building Google Chat integration, memory architecture, and multi-session coaching is engineering work. Mike's name didn't come up, but he's implied in all of it.

---

## Key Strategic Insights

### 1. The Real Product is Emerging
This call revealed what the AI Coach actually needs to be:
- Context-aware (assessment results, conversation history)
- Agenda-driven (user sets their priorities)
- Flexible (microhabits as one tool among many)
- Personified (Axia with different "flavors")

This is clearer than previous specs. It should be documented.

### 2. The MELI Opportunity is a Forcing Function
MELI's timeline forces decisions that have been deferred:
- Memory architecture
- Coach naming
- Session structure
- Content strategy

This is actually healthy — external pressure creates focus.

### 3. Social Learning is the Upsell
Ruy's group coaching idea ("monthly cohort calls enriched by analytics") is the premium tier. The AI coach is the base; human-facilitated social learning is the multiplier. This is a good business model insight.

### 4. The Microhabit Pivot is Correct
Moving from "microhabit machine" to "coaching relationship where microhabits are one tool" is the right product direction. It matches how real coaching works. But it requires rebuilding the current flow.

---

## Action Implications for Ruy

### Document the Session Structure
The 6-session sequence Ruy described needs to be written down:
1. Assessment + debrief
2. Workshop
3. Plan of coaching (establish agenda)
4. Sessions 1-6 (weekly, working through agenda)
5. Monthly maintenance

This is the offer. It should exist as a product spec.

### Clarify What "Axia" Is
If the coach is now "Axia," this needs to propagate:
- Vision docs
- Product specs
- Demo materials
- Developer documentation

### Scope the MELI MVP
What's the minimum version of this that can demo in Q2?
- Assessment debrief (already exists?)
- Coaching session flow (needs Horacio + prompts)
- Memory (what's the simplest version?)
- Google Chat (is this really needed for pilot?)

### Talk to Mike
This call generated engineering requirements. Mike needs to know:
- Memory architecture is critical path
- Google Chat integration is client-requested
- Q2 timeline for MELI
