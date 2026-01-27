# Deep Analysis: OKRs Session (Ruy + Leo, Jan 20, 2026)

## Meta-Theme

**"Getting organized to make decisions, not making decisions."** This meeting was about establishing the infrastructure for decision-making (OKRs, PMF process, Notion, weekly cadence) rather than making actual product decisions. That's appropriate for a Q1 kickoff, but the 3-month runway means this organizational setup needs to translate to action within 2 weeks, not 6.

---

## 1. Patterns and Recurring Themes

### The Bottleneck Pattern
Ruy explicitly mentioned being a bottleneck twice:
- "Me empiezo a volver un cuello de botella" (prompt customization)
- "Mike por cada cliente se tarde... mediodía" (environment setup)

This is the third meeting where this pattern surfaces. The pattern is: **individual expertise creates scaling problems**. Every custom deployment requires Ruy (methodology) + Mike (technical) touch.

**Implication:** Automation isn't a nice-to-have feature—it's existential for the 3-month runway. Without it, they can't validate PMF at scale because they can't deploy at scale.

### The "We Heard This Before" Pattern
Leo mentioned hearing LMS integration requests "4-5 times" from partners. Ruy's response: "I've heard this multiple times and it hasn't materialized."

This reveals a **pipeline credibility gap**: Sales is hearing market demand, but past experience suggests these leads don't convert. Neither Ruy nor Leo questioned *why* previous requests didn't convert. Is it:
- Price?
- Timeline?
- Technical complexity communicated poorly?
- Stoic not being ready?

This pattern suggests potential dead-end pursuit if not understood.

### The "Sharpen Later" Pattern
Multiple times, decisions were deferred:
- "3 or 4 features, I'll refine later"
- "HPT needs exploration, we'll discuss at Dolo meeting"
- "Pricing review, meeting tomorrow"

Appropriate for a planning session, but creates risk: if tomorrow's meetings also defer, the runway shrinks with no decisions.

---

## 2. What's Said vs What's Implied

### Said: "Necesitamos que sea algo compartido"
**Implied:** Ruy doesn't trust himself to prioritize PMF work alone. The accountability through shared ownership is the mechanism to ensure it happens—not just the collaboration benefits.

### Said: "Eso de high performance team, es una idea, no un concepto"
**Implied:** Oseas is pushing a direction (HPT) that doesn't have Ruy's buy-in or understanding. Ruy sees it as undefined compared to his well-articulated Behavior Change vision. There's a potential CEO-CTO alignment gap forming.

### Said: "Si alguien lo pide, cómo ejecutar y lo resolvemos"
**Implied:** Leo wants permission to sell LMS integration *before* they've done it. Ruy is giving a conditional yes—"I know how, so you can promise." This is a classic pre-sale commitment that creates deadline pressure.

### Said: "Nelson ya se está saliendo"
**Implied:** Nelson's transition (role change?) means operational knowledge is walking out. The pricing model, Thinkific integration knowledge, and customer setup processes may need capture before he's fully transitioned.

---

## 3. Technical Debt Being Created

### WorkOS Decision Deferred
They discussed WorkOS ($125/connection/month) vs per-LMS custom integration, but didn't decide. If a partner commits to LMS integration, they'll have to decide under time pressure. The decision should be made now:
- **If expecting >8 LMS integrations:** WorkOS makes sense
- **If <8:** Custom integration is cheaper

By not deciding, they create future time pressure.

### Automation "Feature" Framing
Positioning automation as "a feature to ship" rather than "infrastructure to build" may mean it competes with user-facing features for priority. Automation enables other features—it should be foundational, not optional.

### Prompt Customization Workflow Undefined
Ruy mentioned being a bottleneck on prompt customization, but there's no documented process for:
- How prompts get customized
- What variables clients can change
- How to test prompt changes
- Who approves prompt changes

This will bite them with the next enterprise client.

---

## 4. Single Points of Failure

| Person | Knowledge Risk | What Breaks If Gone |
|--------|---------------|---------------------|
| **Ruy** | Coaching methodology, prompt engineering | No new coach types, methodology stalls |
| **Mike** | Environment deployment, Teams integration | No new client deployments |
| **Nelson** | Pricing model, Thinkific ops, client setup | Can't quote accurately, setup delays |
| **Horacio** | Coaching validation, methodology depth | No validation of coaching approach |

The most dangerous: **Nelson's transition** is happening now, but knowledge transfer isn't mentioned as urgent. If he's "saliendo," when? What happens to his knowledge?

---

## 5. Process Gaps Revealed

### No Definition of "Feature Complete"
Ruy mentioned features 1-4 but never defined what "done" means for each. Teams integration is "in production"—but what does that mean for sales? Can Leo demo it? Can clients use it?

### No PMF Criteria Defined
They agreed to a weekly PMF meeting, but didn't define:
- What evidence would confirm PMF?
- What evidence would reject it?
- When do they make the go/no-go decision?

Without criteria, they'll have meetings without conclusions.

### No Pricing Review Cadence
The Nelson meeting tomorrow is reactive ("this doesn't feel right"). There should be a quarterly pricing review tied to cost changes (LLM costs, dev time benchmarks, etc.).

---

## 6. Alignment Gaps

### Oseas vs Ruy: HPT Direction
Oseas seems to want exploration of High Performance Team direction. Ruy is skeptical ("it's an idea, not a concept") and has deep investment in Behavior Change.

**Risk:** If Oseas decides HPT is the direction, Ruy's work on Behavior Change vision becomes sunk cost. If Ruy resists, there's founder-CTO tension.

**Resolution needed:** Clear criteria for choosing between directions, decided together.

### Leo vs Reality: LMS Integration
Leo is hearing market demand and wants to sell it. Ruy has historical skepticism ("hasn't materialized"). They need to reconcile:
- Is past non-conversion due to Stoic not being ready?
- Or is it due to buyer behavior (talk but don't commit)?

### Sales vs Engineering: Setup Fees
$4,000 per coach for customization may be underselling or overselling. Neither Ruy nor Leo knows the actual cost. This is a **margin blind spot**.

---

## 7. Measurement Gaps

| What They Can't Measure | Why It Matters |
|------------------------|----------------|
| Actual setup cost per client | Can't price accurately |
| Time from lead to deployment | Can't predict capacity |
| Prompt customization effort | Can't estimate projects |
| PMF signals | Can't decide direction |
| User engagement in Teams | Can't prove value of Teams integration |

---

## 8. Strategic Implications for 3-Month Runway

### Week 1-2 Critical
The organizational setup (OKRs, Notion, weekly meetings) must be functional by end of January. If it takes longer, they've lost 1/3 of their runway on process, not validation.

### The HPT Exploration Risk
Exploring HPT direction sounds responsible, but:
- It could delay Behavior Change validation
- It splits Ruy's focus
- It might be CEO-directed rather than market-directed

**Question to ask:** Is there customer pull for HPT, or just investor/CEO enthusiasm?

### Automation as Force Multiplier
If automation is delivered in Q1:
- They can deploy to more customers faster
- They can run more PMF experiments
- They reduce Ruy/Mike bottleneck

If automation is pushed to Q2:
- Every new client is manual
- PMF validation is limited by deployment capacity
- Bottleneck persists

**Recommendation:** Automation should be Q1 priority #1, not feature #4.

### The Partner Pipeline Problem
Leo mentioned 4-5 partners wanting LMS integration, but none have converted. Before investing in LMS capability, they should understand *why* conversion failed. If it's price, LMS won't help. If it's capability, it might.

---

## 9. Warnings and Risks

### Nelson Transition Risk
"Nelson ya se está saliendo" was mentioned casually. This is an operational risk:
- Who owns pricing after Nelson?
- Who handles Thinkific operations?
- Where is his knowledge documented?

**Recommendation:** Schedule knowledge transfer session with Nelson before his transition completes.

### The Anonymous iFrame Temptation
Ruy mentioned they could do iFrame without auth ("lo metemos en un iframe y listo"). This was correctly flagged as a security/cost risk, but the temptation exists. In a crunch, someone might suggest it again.

**Recommendation:** Document the decision and rationale to prevent future revisiting.

### Meeting Proliferation Risk
They're adding:
- Weekly PMF review
- Tomorrow's Nelson meeting
- Dolo meeting
- Regular OKR check-ins

For a 4-person team with a 3-month runway, meeting time competes with building time. Need to be ruthless about meeting efficiency.

---

## 10. Hidden Dependencies

### P&G Driving Technical Decisions
The SSO work for P&G (mentioned) drove technical investment. Now partners are requesting LMS integration. Client-driven development is appropriate for revenue, but risks:
- Building features for one client that don't generalize
- Priority inversions (big client request > PMF validation)

### Oseas's Vision Authority
The Dolo meeting tomorrow (with Oseas?) will influence HPT direction. Ruy is preparing but seems to be in a reactive position rather than driving.

### Teams Integration Dependency on Automation
The Teams integration is "in production" but Leo can't use it. This suggests the bottleneck isn't just deployment—it's the setup/config that surrounds deployment. Teams won't deliver value until automation solves this.

---

## Key Strategic Insights

1. **Automation is infrastructure, not feature.** Treat it as Q1 sprint 0 work, not feature #4.

2. **The HPT direction needs customer evidence, not just exploration.** Before Ruy spends time elaborating HPT, find one customer who would pay for it.

3. **Nelson's transition is a knowledge risk.** Schedule explicit knowledge transfer before it's too late.

4. **The PMF process needs exit criteria.** "Weekly meetings" isn't a process—define what evidence triggers what decisions.

5. **LMS integration requests need failure analysis.** Before building capability, understand why past requests didn't convert.

6. **The 3-month runway is now 2.5 months.** January organizational work doesn't count as validation. Real validation needs to start by February 1.
