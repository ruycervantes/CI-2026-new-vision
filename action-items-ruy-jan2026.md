# Consolidated Action Items - Ruy (January 2026)

Consolidated from meetings with Mike and Oseas on January 13, 2026, plus handwritten notes (Jan 13 & Jan 14).
**Updated:** January 15, 2026 - Sprint Planning Call outcomes + handwritten notes (Jan 15) added.

---

## Key Reflections & Context *(reference, not tasks)*

### Strategic Context (from Oseas)
- **3-month runway** to prove Stoic works
- If it doesn't work → potential pivot to Axialent digitalization
- Focus 100% on Stoic roadmap for now

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

---

## Sprint Planning Outcomes (Jan 15, 2026)

### Ruy's Sprint Tasks

- [ ] **Evaluate Linear vs GitHub Projects** for development tracking
  - Problems with Asana: no epics, testing/dev boards split, no capacity metrics, can't track product/client per issue
  - Linear: modern, great MCP/Claude Code integration, designed for dev
  - GitHub: free, integrated, has Kanban/roadmap/epics, CI/CD automation
  - Action: Write comparison, share via email, discuss in office hours

- [ ] **Document testing/shipping process** - IN PROGRESS
  - See details: `sprint-methodology-fix.md` → "Testing & Shipping Process" section
  - **Open questions to resolve:**
    - Who notifies sales team when features ready for demo?
    - Can deployment script enforce 3-day demo notice?

- [ ] **Add detail to Leo's testing task** (in Asana)
  - Explain how to test Leadership Growth Partner in testing version
  - Give access to testing.stoicq.com
  - See transcript: `calls/Sprint Planning 15 jan 2026.txt`

- [ ] **Talk to Nelson** about P&G course automation timeline

### Blockers

| Blocker | Owner | Resolution |
|---------|-------|------------|
| P&G course automation | Nelson | Schedule discussion |
| No client lifecycle visibility | Team | Document archival process |
| Oseas's coaching vision | Ruy | Requires new version (Q1 roadmap) |

---

## This Week (Post-Sprint Planning)

### Research & Preparation

- [ ] **Review bug list from Mike** - he prepared list to review
- [ ] **Email Oseas** - clarify his product testing request/expectations
  - Gap: Oseas expects assessment → growth areas → micro-habits coaching
  - Reality: currently one micro-habit from assessment
  - "Lo que dijo Oseas ahorita no lo podemos hacer" → requires new version
  - Risk: if he demos his vision (not reality), creates misaligned expectations
  - **Action:** Share Q1 roadmap for explicit alignment on what ships when
- [ ] **Organize personal work/tasks backlog** → prioritized list in Todoist

- [ ] **Competitor benchmark** (HIGH PRIORITY) - First draft for ongoing review
  - Key competitors: MindGym, Cloverleaf
  - Ask Franco for his benchmark document
  - Review others in [Mural board](https://app.mural.co/t/axialent8953/m/axialent8953/1764890677283/ad8559ddadff366460dab38357447aaeeeea02d1)
  - Review consumer behavior change apps (App Store)
  - Check apps against goal setting theory requirements (HCI research)
  - Answer: Are we 80/20 replaceable by a $10 app?
  - Document: What do we do that they can't?

- [ ] **HCI research review** (NotebookLM)
  - Longitudinal goal setting patterns
  - What makes people persist vs abandon?
  - Intervention timing and frequency

- [ ] **Interview Horacio** about coaching methodology (BLOCKS: Thinking Partner ship, vision methodology)
  - How does he take notes?
  - What does he track session-to-session?
  - How does he handle goal evolution?
  - Get photos of his notebook if possible
  - **Also:** Get him to test Thinking Partner to refine prompts
  - **Also:** Validate multi-session coaching methodology in vision doc

### Documents & Materials

- [ ] **Create roadmap document** for Leo and team
  - First draft: `roadmap-q1-2026-draft.md` (Jan 14)
  - **Next:** Review vision doc, then refine roadmap
  - **Add:** Sprint Automation section
  - Purpose: help sell / validate with customers
  - Q1 features, OKRs structure, dependencies
  - **Flag Nelson's requests** (Thinkific SSO, chatbot creation) for Q2+ discussion

- [ ] **Update pitch slides**
  - Add goal-based development flow (missing piece)
  - Share URL with Mike after update

---

## Process & Systems (NEW - from Handwritten Notes)

### Personal Workflow
- [ ] **Define daily/weekly review process**
  - What to review, when, how long
  - Could include CC → Todoist if useful

### Unshipped Features (Technical Debt)
- [ ] **Ship voice STT** - done but not shipped
- [ ] **Ship data features** - done but not shipped
- [ ] **Ship Thinking Partner** - blocked on Horacio interview

---

## Administrative Tasks (NEW - from Handwritten Notes)

- [ ] **Nuevos contratos para Daniel y Mike**
- [ ] **Set up Claude-Code account for Shamil**
  - Create shared account like oas@stoic.enterprise
- [ ] **Email transition: stoic.enterprises → stoicyou.com**
  - Transition ruy@ and others
  - Helpdesk ticket already created for related issue

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

## Operations Requests (Nelson/Axialent)

*Flag these for roadmap discussion - potential Q2+ items*

### Thinkific SSO Integration
- [ ] **Thinkific as SSO provider** (feasible, needs roadmap discussion)
  - Access chatbot from student dashboard (not from lesson)
  - CI shows sidebar menu with coaches
  - "Home" link redirects back to Thinkific
  - *Context:* Makes chatbots an element, not a learning activity

### Chatbot Creation Interface
- [ ] **Self-service chatbot creation for Axialent** (backlog)
  - Nelson wants autonomy to create chatbots
  - Ruy has scripts that could be automated
  - Even basic/unpolished would help

### Nelson's Role
- [ ] **Clarify Nelson's new role** - understand implications for collaboration/requests

---

## Strategic Questions to Resolve *(reference, not tasks)*

| Question | Source | How to Resolve |
|----------|--------|----------------|
| Which angle has most customer pull? (behavior change vs team performance vs culture compass) | Oseas | Customer validation |
| Are we differentiated from habit apps? | Oseas | Competitor research |
| Voice vs bidirectional chatbot priority? | Mike | Customer validation |
| Can we show ROI to L&D buyers? | Oseas | Need to define metrics |
| Will L&D buyers who buy courses see value in this? | Oseas | Customer interviews |

---

## Blocked Items

| Item | Blocked By | Next Step |
|------|------------|-----------|
| Vision methodology + Thinking Partner ship | Horacio interview | Schedule interview |
| Feature 3 vs 4 priority | Customer validation | Talk to Leo |
| Graph memory decision | Technical prototype | Mike to explore |

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
- **Sprint Planning (Jan 15):** `calls/Sprint Planning 15 jan 2026 - Summary.md`
- Vision document: `conscious-insights-v2-english.md`
- Pitch slides: `index.html` (Netlify deployed)
- Nelson chat (Jan 13): WhatsApp - Thinkific SSO & chatbot creation requests
