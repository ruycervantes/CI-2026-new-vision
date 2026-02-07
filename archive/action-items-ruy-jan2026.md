# Consolidated Action Items - Ruy (January 2026)

Consolidated from meetings with Mike and Oseas on January 13, 2026, plus handwritten notes (Jan 13 & Jan 14).
**Updated:** January 29, 2026 - Added Sprint Planning (Jan 29) action items.

---

## 🎯 This Week Focus

- [ ] **Carpintero cama Enoles** - call them
- [ ] **Add privacy policy draft to Asana ticket** - Jonathan's request, you have draft ready (from Sprint Demo Jan 28)
- [ ] **Send note about language policy to Nelson/Dolo** - Decision: single language per user at provisioning, remove selector for normal users
- [ ] **Test Linear this sprint** - evaluate vs Asana for sprint management (committed Jan 28 demo)
- [ ] **Decide sprint management process: roadmap → backlog → sprint** - How does committed work flow from roadmap to backlog to sprint stories? Includes: Linear vs Asana decision, backlog format (`sprints/backlog.md` created as placeholder), sprint file naming when sprints cross months, how Daniel picks up work after leave. Related to all sprint management process decisions.
- [ ] **Define standalone UX vision** - blocks tutorial wizard, bot selection, language settings final design
- [ ] **Ask Mike to follow up on user instructions** - check if what Nelson has is sufficient for the 5-user test. Users need clear context/setting so they use it as intended (from Mike-Ruy chat Jan 28)
- [ ] **Process strategic brain dump** - review and process `thinking/strategic-brain-dump.md`, land insights into appropriate core docs
- [ ] **Design LGP check-in dialogue prompt** - write the prompt/spec for the new chat-based check-in step: rating (1-5) → assess struggle → adapt microhabit (trigger/action) or tactical coaching → schedule next. Shamil blocked on this. (from Sprint Planning Jan 29)
- [ ] **Check if support team can set up Azure environment** - instead of Daniel spending 3-4 hours. Needs Stoic credit card + finance auth before 2pm MX. Target: second week of Feb. (from Sprint Planning Jan 29)
- [ ] **Talk to Leo about office hour scheduling** - request at least one lighter office hour day/week for technical work and pair programming (from Sprint Planning Jan 29)
- [ ] **Create shipping checklist** - dev done → push to staging → demo in office hours → team tests → ship. Talk to Leo about owning this process. (from Analysis Jan 29)
- [ ] **Add estimation review to next sprint planning** - 15 min at start: each task, estimated vs actual, why the gap. (from Analysis Jan 29)
- [ ] **Add re-engagement ideas to backlog** - other features for re-engagement beyond check-in redesign (from Analysis Jan 29)
- [ ] **Do own work management review** - catch up on personal task management. Include reflection: what's not working? Doing a lot but not getting to sprint review items, vision work slipping. Why?

**Calls to Process:**
- [ ] **Process Horacio call (Jan 27)** - `calls/cont explicación coaching : htp horacio 27ene2026.txt` - coaching/HTP methodology

**Send to Nelson:**
- [ ] **Share repository access with Nelson** - so he can iterate on vision docs directly


### Still Pending (from earlier)
- [ ] **Set up Todoist plan with Irene**
- [ ] **Sacar a Enol a andar en bicicleta**
- [ ] **Discuss AI coaching dependency with team** - Review `team-effectiveness/ai-coaching-dependency.md` with Mike/Shamil. Key question: does minimum (Coach mode + simple check-ins) feel right for TE pilot?
- [ ] **Escalate Microsoft sandbox request to Mario** - Daniel writing request, or just buy Boetus licenses (~$50-80/mo)
---

## Key Reflections & Context *(reference, not tasks)*

### Strategic Context (from Oseas)
- **3-month runway** to prove Stoic works
- If it doesn't work → potential pivot to Axialent digitalization
- Focus 100% on Stoic roadmap for now
- **AI Coach is the single unlock** for both behavior change AND team effectiveness. Build this first. Enables: individual coaching at scale within team processes, 20% ticket price increase, Torch-model (AI as TA to human coach), and data for impact measurement. (Jan 27 Nelson 1-on-1 + group session)

### Nelson's Guiding Principle (Jan 27)
> "Todo esto tiene que estar siempre girado acerca del impacto." - Impact demonstration is the north star for the digital layer.

### Positioning Insight (from Mike)
> "Si nos quedamos como 'tenemos un chatbot de coaching', competimos con todos. Si nos posicionamos como 'somos dueños del ciclo de cambio de comportamiento', es otra conversación."

### Oseas's Concern: User Willingness
- People don't naturally persist with self-development
- Need to anchor to things people actually care about (promotions, avoiding problems)
- Make it genuinely useful for work, not just "be a better person"

### Stickiness Insight
> "Si esto se vuelve tu Pepe Grillo, no de la chamba sino de todo tu día, pues ahí está muy sticky."

### Product Positioning Insights (Jan 15 Handwritten)
- **"Personal Trainer for work"** - not just accountability, but helping you do what you NEED to do
- **Skills architecture** - Thinking Partner should have specialized skills it can suggest contextually
- **Broader than work** - also help with personal change

### Self-Reflection (from Handwritten Notes)
- **"Yo soy un cuello de botella"** - blocking things by not shipping
- **"Hacemos features y quedan huérfanos"** - features orphaned after building
- **"Sprints ya funcionan, pero PMF es desastre"** - need PMF validation process
- **"Lo necesita un SISTEMA"** - need systems, not just tasks
- **"Ship with confidence"** - can't ship without process

### PMF Cycle Insight
```
Visión de Producto → Validación PMF → Aprendizaje PMF → SPRINT DE DESARROLLO
                                              ↑_________________________|
```

### Horacio Call Insights (Jan 16, 2026)

**Ontology for coaching memory system:**
- Personas → Metas → Comportamiento → Ejemplos
- Key question: **"¿Qué es lo más valioso de recordar?"**

**Coaching process notes:**
- Group coaching (colectivas) vs individual instances
- A/B test idea: detailed notes vs simple tracking
- "Social Setup" / motivación social as feature concept
- **Core insight:** "Necesito poder dar algo en memoria" - system must surface relevant history

### Coaching Insights (Jan 19, 2026 - Handwritten)

**Coaching structure:**
- Coaching typically runs 4-6 specific sessions focused on one thing
- Then maintenance phase follows

**AI vs Human Coaching - Key Distinction:**
- "Las sesiones con Horacio son muy profundas. No sé si le daría eso a un AI."
- **BUT the opportunity:** "Lo chido del AI es que podemos tener sesiones súper tácticas"
- AI can have super tactical sessions focused on very specific things
- Help people in day-to-day workflow - dedicate a coaching conversation to something that otherwise wouldn't have gotten dedicated attention
- Things that would have been very difficult to address otherwise

**Skills-based architecture insight:**
- "Lo podemos implementar en skills"
- See "With Mike" section for full architecture discussion

---

## Sprint Planning Outcomes (Jan 15, 2026) *(reference, not tasks)*

### Ruy's Sprint Tasks

- **Evaluate Linear vs GitHub Projects** for development tracking
  - Problems with Asana: no epics, testing/dev boards split, no capacity metrics, can't track product/client per issue
  - Linear: modern, great MCP/Claude Code integration, designed for dev
  - GitHub: free, integrated, has Kanban/roadmap/epics, CI/CD automation
  - Action: Write comparison, share via email, discuss in office hours
  - **Prototype plan:** Test Linear MCP integration - try importing vision and roadmap docs

- **Document testing/shipping process** - IN PROGRESS
  - See details: `sprint-methodology-fix.md` → "Testing & Shipping Process" section
  - **Open questions to resolve:**
    - Who notifies sales team when features ready for demo?
    - Can deployment script enforce 3-day demo notice?

- **Add detail to Leo's testing task** (in Asana)
  - Explain how to test Leadership Growth Partner in testing version
  - Give access to testing.stoicq.com
  - See transcript: `calls/Sprint Planning 15 jan 2026.txt`

### Blockers

| Blocker | Owner | Resolution |
|---------|-------|------------|
| No client lifecycle visibility | Team | Document archival process |
| Oseas's coaching vision | Ruy | Requires new version (Q1 roadmap) |

---

## From Richi Call (Jan 22) - Team Effectiveness

### For Ruy
- [ ] **Schedule follow-up with Richi** - after he reviews materials

#
---

## This Week - Research & Documents

### Research & Preparation

- [ ] **Review bug list from Mike** - he prepared list to review
- [ ] **Competitor benchmark** (HIGH PRIORITY) - First draft for ongoing review
  - Key competitors: MindGym, Cloverleaf
  - **Franco's benchmark:** https://www.notion.so/axialent/Analisis-de-competidores-247073cafffb800ca830e7d8bd740d8d
  - Review others in [Mural board](https://app.mural.co/t/axialent8953/m/axialent8953/1764890677283/ad8559ddadff366460dab38357447aaeeeea02d1)
  - Review consumer behavior change apps (App Store)
  - Check apps against goal setting theory requirements (HCI research)
  - Answer: Are we 80/20 replaceable by a $10 app?
  - Document: What do we do that they can't?

- [ ] **HCI research review** (NotebookLM)
  - Longitudinal goal setting patterns
  - What makes people persist vs abandon?
  - Intervention timing and frequency

- [ ] **Process Horacio call (Jan 16)** - ⚠️ 3 days old, still needed?
  - Transcribe call and extract coaching methodology insights
  - Use `/process-call` command
  - Key topics: ontology, memory system, group vs individual coaching


---

## Process & Systems (NEW - from Handwritten Notes)

### Personal Workflow
- [ ] **Set up personal task system (Todoist) with daily/weekly review** - consolidate all task lists into Todoist, establish review cadence. Done when: single source of truth for tasks + doing reviews consistently.

### Hackathon Prototype (1Evening - Jan 16)
- [ ] **Personal Life Coach prototype** - done when I have a working tool I use day-to-day
  - Gym Coach component
  - Brain/Life Coach component
  - Relationship Coach component
  - "Dónde cómo sustento para recordar" - where to store life context

### Unshipped Features (Technical Debt)
- [ ] **Ship voice STT** - done but not shipped
- [ ] **Ship data features** - done but not shipped
- [ ] **Ship Thinking Partner** - blocked on Horacio interview

---

## Product Strategy & Process Definition (This Sprint)

*See detailed discussion: `pmf-design-sprint-planning.md`*

### 1. Define PMF segments + hypotheses (with Leo, ~1 hour)
- [ ] Which 1-2 customer segments for Q1?
- [ ] What's the hypothesis per segment?
- [ ] Who do we have access to? (Leo: clients, prospects, friends)
- [ ] Who are potential users beyond customers?

### 2. Design the design sprint (Ruy, before sprint starts)
- [ ] Choose format: remote accelerated (3-day) vs hybrid with research
- [ ] Which Q1 features in scope?
- [ ] Schedule: this sprint or next?
- [ ] Participant list (Leo, Ruy, who else?)

### 3. PMF process doc (1-pager, create once)
- [ ] Simple template: Segment → Hypothesis → Test → Learn → Iterate
- [ ] Living doc, updated after each validation cycle

### 4. User research (input to design sprint)
- [ ] Interview people who manage teams
- [ ] Potential: Peppe (cousin-in-law) - insight on managing people
- [ ] What would they find useful?

### 5. Customer validation (during/after design sprint)
- [ ] Would they buy "application coaching" sessions?
- [ ] Voice vs Bidirectional Teams chatbot - which first?
- [ ] Does the vision resonate vs competitors?



---

## Blocked Items

| Item | Blocked By | Next Step |
|------|------------|-----------|
| Vision methodology + Thinking Partner ship | Horacio interview | Process call notes |
| Feature 3 vs 4 priority | Customer validation | Talk to Leo |
| Graph memory decision | Technical prototype | Mike to explore |
| Environment automation completion | Daniel baby leave (~Feb 16) | P&G solution documented before leave |
| Microsoft Teams testing (Mike + Daniel) | No sandbox environment | Escalate to Mario or buy Boetus licenses |
| LGP accountability loop redesign (Shamil) | Ruy hasn't designed the check-in dialogue prompt | Ruy to write prompt spec |
| Infrastructure script handoff | Daniel's baby leave ~Feb 16 | Document before leave. No new onboarding during leave. Mike is emergency backup. |

---

## CI Automation Backlog

*Items to track for future automation work*

- [ ] **Brilliant assessments integration** - potential issue to investigate
  - Tool where assessments are managed
  - Needs investigation for automation possibilities

- [ ] **Add Todoist integration skill** - for pending items tracking

---

## Team Transitions *(reference, not tasks)*

- **Mike** takes more day-to-day leadership of dev team
- **Mike** can assign urgent tasks to Daniel/Shamil outside sprint
- **Leo** owns testing → demo approval flow
- **Ruy** focuses on prototyping, methodology, customer validation
- **Daily standups** for Daniel, Shamil visibility

---

### Key Insight to Remember *(reference)*
> "Being a Product Manager + CTO... Lo más importante es que hecho pueda ser deseable, útil y viable y confortable."

---

## Reference

- Mike meeting notes: `meeting-notes-mike-13jan2026.md`
- Oseas meeting notes: `meeting-notes-oseas-13jan2026.md`
- Handwritten notes (Jan 13): `handwritten-notes-transcription.md`
- Handwritten notes (Jan 14): `handwritten/` folder
- Handwritten notes (Jan 15): `handwritten/IMG_7706-7708`
- **Handwritten notes (Jan 16):** `handwritten/IMG_7715-7718` - Horacio call + TODOs
- **Handwritten notes (Jan 19):** `handwritten/IMG_7744-7747` - coaching insights, skills architecture, urgent items
- **Sprint Planning (Jan 15):** `calls/Sprint Planning 15 jan 2026 - Summary.md`
- **Horacio Call (Jan 16):** needs processing with `/process-call`
- **Shamil 1:1 (Jan 20):** `calls/Shamil - Ruy - discuss feature thinking partner - Summary.md` - Thinking Partner handoff, Max account setup
- **OKRs with Leo (Jan 20):** `calls/OKRs Ruy - con leo - 20jan2026 - Summary.md` - Q1 OKRs, PMF process, HPT exploration
- **Daniel 1:1 (Jan 21):** `calls/Catch up with Daniel 21jan2026 - pg and workos - Summary.md` - P&G SSO clarification, WorkOS strategy, paternity leave planning
- **Richi Call (Jan 22):** `calls/Application Coaching - richi and ruy 22jan2026 - Extraction.md` - Team effectiveness methodology, design principles, "ayúdame a ayudarte" framework
- **Nelson + Oseas (Jan 27):** `calls/Sesión con Nelson más Oseas 27enero2026 - Summary.md` - Pricing alignment, Vitro opportunity, HPT MVP design, AI coach architecture, impact measurement
- **Sprint Demo (Jan 28):** `calls/Sprint Demo -28ene2026- 2026 series - Summary.md` - Thinking Partner sidebar, VLAN assessment admin, language policy, Linear evaluation
- **Sprint Planning (Jan 29):** `calls/Sprint Planning - 29jan2026 - Summary.md` - LGP accountability loop, infra automation progress, Teams 21pts, Azure deferred, technical syncs
- Vision document: `conscious-insights-v2-english.md`
- Pitch slides: `index.html` (Netlify deployed)
- Nelson chat (Jan 13): WhatsApp - Thinkific SSO & chatbot creation requests
