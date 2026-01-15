# Consolidated Action Items - Ruy (January 2026)

Consolidated from meetings with Mike and Oseas on January 13, 2026, plus handwritten notes (Jan 13 & Jan 14).
**Updated:** January 15, 2026 - Sprint Planning Call outcomes added.

---

## Key Reflections & Context

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

- [x] **Follow up with IT (Javier)** for Mike's Teams admin permissions - DONE Jan 15
  - Mike was blocked 5-6 days last time waiting for access
  - Ruy called Javier directly

- [ ] **Evaluate Linear vs GitHub Projects** for development tracking
  - Problems with Asana: no epics, testing/dev boards split, no capacity metrics, can't track product/client per issue
  - Linear: modern, great MCP/Claude Code integration, designed for dev
  - GitHub: free, integrated, has Kanban/roadmap/epics, CI/CD automation
  - Action: Write comparison, share via email, discuss in office hours

- [ ] **Document testing process** (Development → Testing → Demo → Production)
  - Simplified naming: "testing" not "staging" for non-devs
  - Domain: testing.stoicq.com
  - **New rule:** Notify dev 3+ days before client demos
  - Leo owns testing approval before demo

- [ ] **Add detail to Leo's testing task** ("Testing de mapro" in Asana)
  - Explain how to test Leadership Growth Partner
  - Give access to testing.stoicq.com

- [ ] **Document bank URL warning**
  - Leo's experience: bank name + login = AWS phishing ban, ALL clients went down
  - Solution: Use abbreviations for bank clients (e.g., "nb" not "nubank")
  - Or route through app.stoicq.com via WorkOS

- [ ] **Implement robots.txt** and AI crawler blocking
  - Confirmed: Google only indexes main website
  - Need to block AI search engine crawlers too

- [ ] **Create roadmap document** with Q1 emphasis → becomes team OKR

- [ ] **Talk to Nelson** about P&G course automation timeline

### Daniel's Sprint Tasks

- [ ] **Complete infra checklist** (carried over)

- [ ] **Deployment script** (3 story points, ~12 hours)
  - Create client-specific environments from any git branch
  - Support Docker containers + plain installation
  - Generate separate DB per client
  - Apps: Main + Admin (Analytics separate, not in scope)
  - Naming convention: same client name throughout chain
  - Documentation on usage

- [ ] **Pair with Mike** on Teams integration when he hits admin permission issues

### Mike's Sprint Tasks

- [ ] **Finish assessment pull button** in admin panel (1 day max)
  - Manual button to pull missing assessments

- [ ] **Microsoft Teams integration - MVP** (full sprint)
  - Goal: Notifications via Teams
  - Match email (CI app ↔ Teams), request permission, send notifications
  - Considering checkbox in Chainlit sidebar
  - **Blocker:** Needs admin permissions from IT (Javier)

- [ ] **Request Teams admin access** from IT Service Desk
  - Contact: Javier
  - Ruy to follow up for faster response

- [ ] **Rename git branches** from staging → testing (when convenient)

- [ ] **Compare prompts** between Demo and Leadership Growth Partner instances
  - Use Claude Code to compare files between branches

### Leo's Sprint Tasks

- [ ] **Test Leadership Growth Partner** in testing.stoicq.com
  - Task: "Testing de mapro" in Asana
  - Ruy to add detailed test instructions

- [ ] **Own testing → demo approval process**
  - Test features before promotion to demo
  - Approve features for client demos

### Team Process Decisions

| Decision | Details |
|----------|---------|
| **Story Points** | Adopted IBM sizing table (1,2,3,5,8,13) |
| **Environment Naming** | development → testing → demo → production |
| **Tool Migration** | Evaluate Linear/GitHub this sprint, decide in office hours |
| **Demo Notice** | 3+ days before client demos |
| **Daily Standups** | Via Teams messages, using Asana form |

### Blockers

| Blocker | Owner | Resolution |
|---------|-------|------------|
| Mike needs Teams admin | Ruy → IT (Javier) | Follow up immediately |
| P&G course automation | Nelson | Schedule discussion |
| No client lifecycle visibility | Team | Document archival process |
| Oseas's coaching vision | Ruy | Requires new version (Q1 roadmap) |

---

## This Week (Post-Sprint Planning)

### Research & Preparation

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

- [ ] **Interview Horacio** about coaching methodology
  - How does he take notes?
  - What does he track session-to-session?
  - How does he handle goal evolution?
  - Get photos of his notebook if possible
  - **Also:** Get him to test Thinking Partner to refine prompts

### Documents & Materials

- [ ] **Create roadmap document** for Leo and team
  - First draft: `roadmap-q1-2026-draft.md` (Jan 14)
  - **Next:** Review vision doc, then refine roadmap
  - Purpose: help sell / validate with customers
  - Q1 features, OKRs structure, dependencies
  - **Flag Nelson's requests** (Thinkific SSO, chatbot creation) for Q2+ discussion

- [ ] **Update pitch slides**
  - Add goal-based development flow (missing piece)
  - Share URL with Mike after update

- [x] **Update vision document** (`conscious-insights-v2-english.md`) - DONE Jan 13
  - [x] Added Goal Hierarchy (Destination → Management → Tracking)
  - [x] Added Goals Dashboard (GPS visualization)
  - [x] Added Coach + Daily Companion modes (replaces Thinking Partner / Accountability Partner)
  - [x] Added Change Process with Adjust stage
  - [x] Added Juan's complete journey
  - [ ] Validate methodology with Horacio

### Sprint Planning Prep - DONE Jan 15

- [x] **Sprint planning completed** (Jan 15)
  - Shamil: Absent, will sync next week
  - Daniel: Deployment script (3 story points) + infra checklist
  - Leo: Testing Leadership Growth Partner
  - Mike: Teams integration MVP + assessment pull button
  - See "Sprint Planning Outcomes" section above for full details

---

## Process & Systems (NEW - from Handwritten Notes)

### Shipping Process (CRITICAL) - Updated Jan 15

- [ ] **Define proceso para ship features** - IN PROGRESS
  - Development → Testing → Demo → Production (simplified naming)
  - testing.stoicq.com = where QA happens
  - Leo owns testing approval before demo
  - **New rule:** 3+ days notice before client demos

- [ ] **Arreglar versiones de demos** - CLARIFIED
  - testing.stoicq.com = testing environment (was "staging")
  - demo.stoicq.com = client demos (almost production quality)
  - production = live client instances
  - Mike to rename git branches to match (staging → testing)

- [ ] **Especificación de versiones**
  - Stop the "desmadre"
  - Clear version management process
  - **New:** Use Claude Code to compare files between branches

- [ ] **Comunicar cuando features ship**
  - Notify: Data, Nelson, Axialent
  - Who is responsible for communication?

### Personal Workflow
- [ ] **Automate task/workflow management**
  - Review CC → Todoist automation
  - Explore better personal task capture system

### Unshipped Features (Technical Debt)
- [ ] **Ship voice STT** - done but not shipped
- [ ] **Ship data features** - done but not shipped
- [ ] **Thinking Partner** - needs Horacio testing before ship

---

## Administrative Tasks (NEW - from Handwritten Notes)

- [ ] **Nuevos contratos para Daniel y Mike**
- [ ] **Set up Claude-Code account for Shamil**
  - Create shared account like oas@stoic.enterprise
- [x] **Email transition: stoic.enterprises → stoicyou.com**
  - Transition ruy@ and others
  - Helpdesk ticket already created for related issue

---

## With Leo (This Week)

- [ ] **Set up Product-Market Fit validation process**
  - How do we validate before building?
  - Customer interview structure
  - Define the experiments/MVPs cycle

- [ ] **Validate with customers:**
  - Would they buy "application coaching" sessions?
  - Voice vs Bidirectional Teams chatbot - which first?
  - Does the vision resonate vs competitors?

- [ ] **Get Leo's help to unblock shipping**
  - Leo to accelerate feature shipping
  - Leo to help with PMF validation process

- [x] **Dev tools discussion** - DECIDED in Sprint Planning (Jan 15)
  - Asana stays for company-wide coordination
  - Dev team evaluating Linear vs GitHub Projects
  - Ruy to compare and share findings
  - Decision to be made in office hours this sprint

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

---

## Strategic Questions to Resolve

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
| Multi-session coaching methodology in vision doc | Horacio interview | Schedule interview |
| Feature 3 vs 4 priority | Customer validation | Talk to Leo |
| Graph memory decision | Technical prototype | Mike to explore |
| Thinking Partner ship | Horacio testing | Schedule with Horacio |

---

## CI Automation Backlog

*Items to track for future automation work*

- [ ] **Brilliant assessments integration** - potential issue to investigate
  - Tool where assessments are managed
  - Needs investigation for automation possibilities

---

## Team Transitions

- **Mike** takes more day-to-day leadership of dev team
- **Mike** can assign urgent tasks to Daniel/Shamil outside sprint
- **Leo** owns testing → demo approval flow
- **Ruy** focuses on prototyping, methodology, customer validation
- **Daily standups** for Daniel, Shamil visibility

---

## Summary: Top Priorities

### Immediate (Before Thursday)
1. **Competitor research** - both meetings flagged this
2. **Roadmap document** - needed for Leo and sprint planning
3. **Write sprint stories** - Thursday deadline
4. **Horacio interview** - informs coaching methodology + testing

### This Quarter (Systems to Build)
1. **PMF validation process** with Leo
2. **Feature shipping process** - stop orphaning features
3. **Version/demo environment clarity**

### Key Insight to Remember
> "Being a Product Manager + CTO... Lo más importante es que hecho pueda ser deseable, útil y viable y confortable."

---

## Reference

- Mike meeting notes: `meeting-notes-mike-13jan2026.md`
- Oseas meeting notes: `meeting-notes-oseas-13jan2026.md`
- Handwritten notes (Jan 13): `handwritten-notes-transcription.md`
- Handwritten notes (Jan 14): `handwritten/` folder (4 images)
- **Sprint Planning (Jan 15):** `calls/Sprint Planning 15 jan 2026 - Summary.md`
- Vision document: `conscious-insights-v2-english.md`
- Pitch slides: `index.html` (Netlify deployed)
- Nelson chat (Jan 13): WhatsApp - Thinkific SSO & chatbot creation requests
