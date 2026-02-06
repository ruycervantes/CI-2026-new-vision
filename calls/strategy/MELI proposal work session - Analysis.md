# MELI Proposal Work Session - Strategic Analysis
**Call Date:** February 2, 2026

---

## Meta-Theme

**MELI is Stoic's proof-of-concept opportunity at enterprise scale.** This isn't just a client — it's a validation of whether the Stoic/Axialent combined offering can deliver an integrated "learning ecosystem" that big companies actually want. If this works, it becomes a repeatable playbook for every major enterprise client.

---

## 1. Patterns and Recurring Themes

### Theme A: MELI's "Platform Exhaustion"
Throughout the call, Laura repeatedly emphasizes that MELI doesn't want "another platform." They have:
- Google Chat (official)
- Slack (IT)
- MELI Tools portal with multiple AI tools
- An LMS
- 800+ apps atomized across the organization

**What this means:** Any solution that requires users to log into a new system will face adoption friction. The winning approach is invisible integration — the coach shows up where they already work.

### Theme B: Internal Facilitators Keep Failing
MELI has tried to train internal facilitators for 4+ years. Every year they say "we'll do it ourselves" and every year they rehire Axialent because quality drops.

**Why this matters:** This is Axialent's moat. The recurring revenue isn't just the workshop — it's that enterprises can't maintain culture consistency without external expertise. This same logic should apply to AI coaches: "You can technically build it yourself, but can you maintain the methodology integrity?"

### Theme C: Scale vs. Quality Tension
MELI wants to reach 125,000 people. Workshops reach 3,500/year max. The gap is 120,000+ people who get nothing.

**Strategic implication:** AI isn't a nice-to-have for MELI — it's the only way to close this gap. Frame the AI coach not as "enhancement" but as "the only way to reach the 97% you're currently missing."

---

## 2. What's Said vs. What's Implied

### Said: "No queremos sumar plataformas"
**Implied:** We've been burned by tech implementations that employees ignore. Prove to us this will actually get used.

### Said: "Queremos un ecosistema de aprendizaje"
**Implied:** We don't know what that means exactly, but it sounds like what we need. Help us define it.

### Said: "Para siempre" (recurring every 2 years)
**Implied:** We want this to be infrastructure, not a project. If you can become embedded in our operating rhythm, you're essentially un-fire-able.

### Said: "AI como habilitador"
**Implied:** We're not ready to replace humans with AI. Position AI as support, not replacement.

### Unsaid but obvious: Laura is nervous about her internal credibility
She keeps asking "how do we show the value" and "how do we make sure they don't think they can do it themselves." She needs Stoic to make her look good internally.

---

## 3. Technical Debt Being Created

### Assessment Customization
Oseas committed to customizing the CB Assessment to MELI language. This is a one-time development cost, but:
- It creates a MELI-specific fork
- Future updates to core CB Assessment won't automatically flow to MELI
- Need to track MELI vocabulary mapping as a maintained artifact

### Multiple Integration Paths
The team discussed Google Chat, MELI Tools portal, LMS integration, and WhatsApp as potential delivery channels. If they try to do all of them:
- Testing matrix explodes
- Mike becomes a bottleneck on integrations
- Each channel requires separate IT approval

**Recommendation:** Pick ONE primary channel for Phase 1. MELI Tools portal seems easiest (just a link/SSO). Google Chat is more ambitious but more sticky.

### Personal Dashboard (Doesn't Exist)
Oseas mentioned this multiple times as part of the solution, but it's vaporware. Building it requires:
- Design decision: web app? embedded widget? mobile?
- Data model for individual progress tracking
- Integration with micro-habit coach
- This is probably 2-4 weeks of Shamil's time

---

## 4. Single Points of Failure

### Laura Roubakhine
She owns this relationship entirely. If she leaves Axialent or gets moved to another account, the institutional knowledge walks out the door. No one else on the call has direct MELI relationships.

**Mitigation:** Get Oseas or Leo into direct MELI meetings as a "co-pilot" so the relationship isn't single-threaded.

### Mike's Bandwidth
Mike is already stretched on:
- Teams integration
- AI Coach MVP
- Microsoft sandbox environment issues

Adding Google Chat integration AND personal dashboard mockups for this MELI proposal could overload him.

### Oseas's Whiteboard
The solution design exists in Oseas's head and a whiteboard. If he can't articulate it clearly to Ruy/Nelson/Mike, implementation will drift from intent.

**Mitigation:** The recording helps, but someone needs to translate the whiteboard into a structured spec with clear deliverables.

---

## 5. Process Gaps Revealed

### No Standard "Ecosystem Proposal" Template
Oseas improvised a whiteboard design on the call. There's no reusable framework for "here's what a learning ecosystem looks like with Stoic/Axialent." Every major deal will require reinventing this.

**Opportunity:** After MELI, codify this into a "Learning Ecosystem Playbook" — assessment, workshop, AI coach, dashboards, community, recognition.

### No Clear Pricing Model for Digital Components
Laura's question "how do we price an agent?" has no good answer. The team settled on "bundle it" but that means:
- No clear margin tracking on digital vs. facilitation
- Hard to upsell digital separately later
- If Axialent wants to credit Stoic's contribution to their target, there's no formula

### No Demo Environment Ready
Oseas offered to do a live demo on Feb 11 if needed, but:
- Personal dashboard doesn't exist
- Google integration doesn't exist
- What exactly would they demo?

They could demo the existing micro-habit coach or conversation AI, but it's not customized to MELI language yet.

---

## 6. Alignment Gaps

### Axialent Revenue Target vs. Stoic Inclusion
Laura mentioned Axialent has a $600K + $700K digital target. The team agreed digital components count toward Axialent's target even if Stoic delivers them. But this creates:
- Incentive for Axialent to undercount Stoic's contribution
- No clear revenue share or transfer pricing
- If this scales (multiple MELIs), the accounting becomes messy

### Oseas's Optimism vs. Engineering Reality
Oseas confidently said "we can deliver everything they ask for" and suggested timelines like "Wednesday" for a refined proposal and "demo on Feb 11."

**Reality check:**
- Mike's availability for new integrations is limited
- Personal dashboard is net-new development
- CB Assessment customization is real work
- IT security review takes weeks

### "For Now" vs. "For Real" Features
Several features discussed are either:
- Existing but not MELI-customized (AI coach, micro-habits)
- Conceptual but not built (personal dashboard, Google integration)
- Ideas thrown out casually (WhatsApp push notifications, community leaderboards)

The proposal needs to clearly separate "Phase 1 deliverables" from "future roadmap."

---

## 7. Measurement Gaps

### No Metrics Defined for Success
MELI shared 96% favorability and 98% applicability for workshops, but:
- What does "favorability" actually measure?
- No metrics discussed for the new ecosystem elements
- How will they measure if AI coaches are working?
- What's the target for micro-habit completion rates?

**Recommendation:** Propose a metrics framework as part of the solution. This differentiates Stoic as serious about outcomes, not just activity.

### No Baseline for Current State
MELI has 125,000 employees but:
- We don't know current engagement rates for non-workshop interventions
- No data on how internal facilitators perform vs. Axialent
- No visibility into their existing AI tool usage (MELI GPT, Verdi)

---

## 8. Strategic Implications

### PMF Validation Opportunity
This MELI deal directly validates Stoic's value proposition:
- **Individual coaching at scale** (micro-habits, AI coach)
- **Enterprise integration** (their platform, not ours)
- **Methodology + technology** (Axialent content + Stoic tech)

If MELI signs and succeeds, it's a case study for every other enterprise prospect.

### Runway Impact
The 3-month runway pressure makes this deal complicated:
- Can't say no to the opportunity
- But the development ask (dashboard, integration, assessment customization) could consume resources needed for core AI Coach MVP

**Risk:** Chasing MELI's specific requirements delays the generic product that could serve multiple clients.

### Axialent Dependency
This deal came through Axialent, not Stoic. Stoic is positioned as the tech provider, not the relationship holder. If Stoic wants to own enterprise clients directly, this model doesn't build that muscle.

---

## 9. Warnings and Risks

### Laura's Credibility is on the Line
She explicitly said she needs to show "the value of us doing it vs. them doing it internally." If the proposal is weak, she looks bad. If she looks bad, she may hesitate to bring Stoic into future deals.

### IT Approval Wildcard
Every integration option requires MELI IT approval. Oseas mentioned Stoic has passed reviews for Credicorp, Telus, P&G, etc., but:
- Each client's security review is different
- MELI is known for strict infosec
- This could add weeks or months to timeline

### Over-promising Trap
The team said yes to everything:
- Google Chat integration? "Sure, after Teams"
- Personal dashboard? "We'll mock it up"
- Assessment customization? "We did it for Sigma"
- WhatsApp push notifications? "Technically easy"

If they deliver all of this, it's amazing. If they deliver 40% of it, Laura will feel oversold.

---

## 10. Hidden Dependencies

### Teams Integration Must Work First
Google Chat integration is explicitly dependent on Teams being done. But Teams is blocked by Microsoft sandbox environment issues. So:
- Teams blocked → Google Chat blocked → MELI integration blocked

### Mike's Architecture Decisions
Everything flows through Mike's technical architecture:
- Graph memory for AI coach?
- Getzep or full Zep?
- How does the personal dashboard connect to the coach?

If Mike's architecture decisions aren't made, nothing else can be built.

### MELI's Internal Politics
Laura is in Culture & Experience. But the request touches:
- IT (for approvals)
- Possibly HR Tech (for LMS integration)
- Possibly the MELI AI team (for MELI Tools integration)

Getting buy-in across these silos could slow things down regardless of what Stoic builds.

---

## Recommendations for Ruy

### 1. Review the Recording, Then Scope Ruthlessly
The proposal needs to separate:
- **Phase 1 (Feb-March):** Workshop + existing AI coach + manual dashboards
- **Phase 2 (Q2):** Personal dashboard, Google integration, assessment customization
- **Phase 3 (Future):** Community features, WhatsApp, gamification

Don't promise Phase 3 in the Phase 1 proposal.

### 2. Create a MELI-Specific Demo
Even if the personal dashboard isn't built, create:
- Mockups of what it would look like
- A conversation with the AI coach using MELI vocabulary
- A sample "team progress report" for the Learning team

Visual artifacts > promises.

### 3. Push Back on Wednesday Deadline
Feb 4 is tomorrow (since the call was Feb 2). That's not enough time to do this well. Counter-propose:
- Send rough outline by Wednesday Feb 5
- Refined proposal by Monday Feb 10
- Laura's meeting is Feb 11 — she has time to review

### 4. Clarify Revenue Attribution
If this becomes a $100K+ deal, the Axialent/Stoic split matters. Get clarity now on:
- What counts as "digital" revenue?
- Does Stoic invoice separately or through Axialent?
- What's the transfer price?

### 5. Flag the Dashboard as New Development
Oseas mentioned it casually, but it's a real feature that doesn't exist. Either:
- Scope it out of Phase 1
- Get Mike's estimate for building it
- Find a workaround (manual spreadsheet reports to start)

---

## Opportunity Size Estimate

If MELI:
- Continues 150 workshops/year × $9,000 average = **$1.35M/year workshops**
- Adds ecosystem components for 5,000 managers at $50/person = **$250K/year digital**
- Scales to shipping supervisors (1,500 × $20/person) = **$30K/year digital**

**Total potential:** $1.5M+ annually, with 80% going to Axialent and Stoic providing the tech layer.

This is why it's worth the effort — but only if execution is clean.
