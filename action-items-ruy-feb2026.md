# Action Items - Ruy (February 2026)

Triaged from January 2026 file + Oseas call (Jan 30).
**Created:** January 30, 2026

---

## This Week Focus (Feb 3-7)

**Note:** Monday Feb 3 is feriado. 4-day week.

### Mercado Libre Opportunity (Feb 11 meeting)

- [ ] **Review Nelson's Meli proposal deck** — Nelson leading, Ruy reviews. Due: before sending to Laura (tonight or tomorrow)
- [ ] **Articulate AI Coach + Thinking Partner for Meli** — Requirements and positioning. Thinking Partner = ready now ("aspirin for headaches"). AI Coach = Q2 roadmap capability. Emphasize: practical application + org-level analytics visibility.
- [ ] **Send video note to Oseas** — pending topics that didn't fit in 1:1. He's in meetings all day tomorrow.

### AI Coach (OKR #1 — critical path)

- [ ] **Design LGP check-in dialogue prompt** — write the prompt/spec for chat-based check-in: rating (1-5) → assess struggle → adapt microhabit (trigger/action) or tactical coaching → schedule next. **Blocks Shamil.**
- [ ] **Build AI Coach MVP plan** — scope with Mike: current memory structure or Getzep drop-in. Demo-able, not production. Discuss architecture (Getzep stores messages → needs Postgres decision or graph-only solution). **Mike context (Jan 30 Slack):** "MVP at best" given other priorities. Getzep could work for multi-session memory but has Postgres dependency — either drop Postgres and go back to full Zep, or use graph-only solutions. Mike to discuss further.
- [ ] **Create AI Coach concept visuals** — storyboards/comic strips showing concrete use cases (preparing for important meeting, being more effective at work). Eye candy for Oseas to show prospects.
- [ ] **Add concrete examples to vision doc** — make "why AI coaching" visceral, not abstract. Practical scenarios.

### Ship what's built

- [ ] **Stabilize Shamil's fixer feature for demo** — server is unstable ("pinche servidor es bien inestable"). Oseas wants to start selling this immediately. Needs stable enough for client demos.
- [ ] **Prepare/ensure demos ready for Feb 9 Madrid meeting** — Oseas preparing slides incorporating dashboard + fixer + Teams into commercial storyline. Mike needs Teams demo ready.
- [ ] **Fix shipping process for done features** — voice STT, data features, Thinking Partner are all built but not shipped. Establish: dev done → staging → demo → team tests → ship. Talk to Leo about owning this flow.
- [ ] **Demo Thinking Partner to Oseas** — show what's already shipped

### Nelson Items (from Jan 30 call)

- [ ] **Review Nelson's Blended Leadership Journey doc** — 10-page Word doc on how to sell hybrid HPT learning journey using current platform. Give him feedback on how to hack it in CI. [SharePoint link](https://axialent.sharepoint.com/:w:/s/ContentDevelopment/IQD6WZAns4oARbVxGZLi8OvEAfZGEeE92-hW58-txw7C6kA?e=fDdVJJ)
- [ ] **Follow up: Nelson analytics portal spec** — Nelson writing spec for analytics portal (Thinkific + Typeform + CI data). Review with him next week. Watch for impact on Shamil's work.
- [x] **Send Nelson chatbot builder resources** — prompt design guide, Custom Bot FRD, Claude conversation, chatbot-design directory README. Sent via chat + email.

### Quick wins (carry from Jan)

- [ ] **Ensure Oseas is admin/owner on OnePassword vault** — board audit requires him to have admin control over all infrastructure access. He's the only legal employee of Stoic.
- [ ] **Follow up on Oseas vision sign-off** — he committed to reading vision docs. Check if he did, get confirmation.
- [ ] **Schedule one working session with Oseas/Nelson/Leo** — align on PMF materials, then they run validation conversations. Target: before Feb second week.
- [ ] **Add privacy policy draft to Asana ticket** — Jonathan's request
- [ ] **Send language policy note to Nelson/Dolo** — single language per user at provisioning
- [ ] **Ask Mike to follow up on user instructions** — check if sufficient for 5-user test
- [ ] **Share dashboard access with Oseas** — for prospect demos
- [ ] **Share all CI platform access with Oseas** — 1Password access, code repos, tools, dashboards. Audit-readiness so he can show he has access to everything.
- [ ] **Share repository access with Nelson** — so he can iterate on vision docs
- [ ] **Hacer extensión de contrato de Daniel** — due Feb 3

### Process

- [ ] **Test Linear this sprint** — evaluate vs Asana for sprint management
- [ ] **Decide sprint management process: roadmap → backlog → sprint** — includes Linear vs Asana, backlog format, sprint file naming, how Daniel picks up work after leave
- [ ] **Add estimation review to next sprint planning** — 15 min at start: estimated vs actual, why the gap
- [ ] **Talk to Leo about office hour scheduling** — request lighter day/week for technical work

### Calls to process

- [ ] **Process Horacio call (Jan 27)** — `calls/cont explicación coaching : htp horacio 27ene2026.txt`

---

## February Priorities

### PMF Process Design (OKR #2 — Oseas owns, Ruy designs)

- [ ] **Establish "Mike office hours" for prototype ideas** — biweekly, lightweight. Mike presents prototype ideas, team decides what to pursue commercially. Agreed in Jan 30 call.
- [ ] **Establish prioritization process with Oseas and Leo** — how do we decide what to build? Backlog triage cadence.
- [ ] **Define PMF segments + hypotheses with Leo** — which 1-2 customer segments for Q1? Hypothesis per segment?
- [ ] **Design the design sprint** — format, features in scope, schedule, participants
- [ ] **PMF process doc (1-pager)** — Segment → Hypothesis → Test → Learn → Iterate
- [ ] **User research: interview people who manage teams** — input to design sprint. Potential: Peppe.
- [ ] **Customer validation questions** — would they buy application coaching? Voice vs bidirectional? Does vision resonate?
- [ ] **GPS dashboard mockups** — team effectiveness visualization for HPT validation

### AI Coach Deep Work

- [ ] **AI Coach technical exploration (2-3 weeks)** — After Meli materials complete, protected time to explore implementation: memory architecture, session continuity, how to make it work. Output: implementation approach + realistic timeline. "Necesito meterme a las tripas."
- [ ] **Process strategic brain dump** — review `thinking/strategic-brain-dump.md`, land insights into core docs
- [ ] **Discuss AI coaching dependency with team** — review `team-effectiveness/ai-coaching-dependency.md` with Mike/Shamil. Does minimum (Coach mode + simple check-ins) feel right for TE pilot?

### Research

- [ ] **Competitor benchmark** (HIGH PRIORITY) — MindGym, Cloverleaf, Franco's benchmark on Notion, consumer behavior change apps. Answer: are we 80/20 replaceable?
- [ ] **HCI research review** (NotebookLM) — longitudinal goal setting, persistence vs abandonment, intervention timing
- [ ] **Review bug list from Mike** — he prepared list to review
- [ ] **Schedule follow-up with Richi** — after he reviews TE materials

### Infrastructure

- [ ] **Check if support team can set up Azure environment** — instead of Daniel. Needs Stoic credit card + finance auth. Target: Feb second week.
- [ ] **Escalate Microsoft sandbox request to Mario** — or buy Boetus licenses (~$50-80/mo)
- [ ] **Add re-engagement ideas to backlog** — beyond check-in redesign

---

## Blocked Items

| Item | Blocked By | Next Step |
|------|------------|-----------|
| Graph memory decision | Technical prototype | Mike exploring Getzep. Discuss architecture. |
| Environment automation completion | Daniel baby leave (~Feb 16) | Document/transfer before leave |
| Microsoft Teams testing (Mike + Daniel) | No sandbox environment | Escalate to Mario or buy Boetus licenses |
| LGP accountability loop (Shamil) | Ruy hasn't designed check-in dialogue prompt | **Ruy to write prompt spec — THIS WEEK** |
| Infrastructure script handoff | Daniel's baby leave ~Feb 16 | Document before leave. Mike is emergency backup. |

---

## System Fixes (workflow)

- [x] **Fix `/process-call` to capture action items to Todoist** — added Step 8: Todoist Sync Prep, references todoist-org skill. Fixed hardcoded month.
- [x] **Fix `/review-action-items` to sync with Todoist** — added Step 5: Todoist Sync Prep, references todoist-org skill.
- [x] **Fix `/todoist-org` skill** — added explicit MCP tool instructions: labels param required, label names without @, project mapping, no due dates unless real deadline.
- [x] **Fix hardcoded month in `/today` and `/weekly-plan`** — changed to `{month}{year}` pattern.
- [ ] **Update Todoist project structure** — consolidate Stoic projects, archive dead projects (Crypto Learning, Old Writing Ideas, MetaDevelopment, etc.)

## Someday / Backlog

- [ ] **Personal Life Coach prototype** — hackathon idea. Gym/Brain/Relationship coach components.
- [ ] **Brilliant assessments integration** — investigate automation possibilities
- [ ] **Follow up on Inworld.ai TTS** — Oseas to connect with cousin for credits + dev relationships. Mike already evaluated, recommends. See `sprints/backlog.md`.

---

## Key Reflections & Context *(reference, not tasks)*

### Process Insight (Jan 30 triage)
- Deep-work weeks (like this vision week) break weekly rituals → items pile up → systems diverge.
- **Fix:** Trigger `/triage` at end of sprint or when file feels heavy. Don't wait for end of month.
- The action items file is upstream (capture). Todoist is downstream (execution). Triage is the bridge.

### Strategic Context (from Oseas)
- **3-month runway** to prove Stoic works
- If it doesn't work → potential pivot to Axialent digitalization
- Focus 100% on Stoic roadmap for now
- **AI Coach is the single unlock** for both behavior change AND team effectiveness. Build this first.

### Oseas Call Outcome (Jan 30)
- **Oseas owns PMF.** Ruy builds showable artifacts. Oseas/Nelson/Leo drive validation conversations.
- Realistic Q1 output = AI Coach MVP (demo-able, not production) per Mike
- Eye candy matters — prospects need to see it, not read about it

### MELI = AI Coach Forcing Function (Feb 3 Nelson call)
- **MELI opportunity IS the AI Coach MVP.** Same work, not separate tracks. Q2-Q3 timeline.
- Key design decision: **Microhabits as ONE tool within coaching**, not the forced structure. Coach establishes agenda first, then uses microhabits/conversations/frameworks as needed.
- Proposed session sequence: Assessment → Workshop → Plan of Coaching → 6 weekly sessions → monthly maintenance
- **"Axia"** proposed as coach name (gender-neutral, sounds good). Different "flavors" for ADN MELI vs Leading at MELI.
- Google Chat is MELI's official platform (context for future integration)

### Nelson's Guiding Principle (Jan 27)
> "Todo esto tiene que estar siempre girado acerca del impacto."

### Positioning Insight (from Mike)
> "Si nos quedamos como 'tenemos un chatbot de coaching', competimos con todos. Si nos posicionamos como 'somos dueños del ciclo de cambio de comportamiento', es otra conversación."

### Oseas's Concern: User Willingness
- People don't naturally persist with self-development
- Anchor to things people actually care about (promotions, avoiding problems)
- Make it genuinely useful for work, not just "be a better person"

### Self-Reflection (from Jan)
- **"Yo soy un cuello de botella"** — blocking things by not shipping
- **"Lo necesita un SISTEMA"** — need systems, not just tasks
- **"Ship with confidence"** — can't ship without process

### Coaching Insights
- AI can have **super tactical sessions** focused on specific things
- Help people in day-to-day workflow — coaching for things that wouldn't otherwise get dedicated attention
- Coaching typically runs 4-6 sessions focused on one thing, then maintenance
