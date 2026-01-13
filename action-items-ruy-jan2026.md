# Consolidated Action Items - Ruy (January 2026)

Consolidated from meetings with Mike and Oseas on January 13, 2026, plus handwritten notes.

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

## This Week (Before Sprint Planning Thursday)

### Research & Preparation

- [ ] **Competitor benchmark** (HIGH PRIORITY)
  - Review habit change apps with AI coaches (Oseas: "dedícale una hora")
  - Check MindGym and others in Mural
  - Answer: Are we 80/20 replaceable by a $10 app?
  - Document differentiators

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
  - Q1 features (3 of 4)
  - OKRs structure
  - Dependencies

- [ ] **Update pitch slides**
  - Add goal-based development flow (missing piece)
  - Share URL with Mike after update

- [ ] **Update vision document** (`conscious-insights-v2-english.md`)
  - Add goal-based development flow (can do now)
  - Add goals dashboard detail (can do now)
  - Multi-session coaching methodology (after Horacio interview)

### Sprint Planning Prep

- [ ] **Write sprint stories** for Thursday
  - Shamil: Thinking Partner feature (extract goal/gap)
  - Daniel: Deployment script automation
  - Leonardo: Testing → demo approval process ownership
  - Mike: Continue MS Teams notifications

---

## Process & Systems (NEW - from Handwritten Notes)

### Shipping Process (CRITICAL)
- [ ] **Define proceso para ship features**
  - Testing → UAT → Demo → Production
  - Who approves at each stage?
  - Leo owns demo approval (agreed with Mike)

- [ ] **Arreglar versiones de demos**
  - ci.demo - what goes here?
  - bsetus.com - what goes here?
  - staging - what goes here?
  - Document what should be in each environment

- [ ] **Especificación de versiones**
  - Stop the "desmadre"
  - Clear version management process

- [ ] **Comunicar cuando features ship**
  - Notify: Data, Nelson, Axialent
  - Who is responsible for communication?

### Unshipped Features (Technical Debt)
- [ ] **Ship voice STT** - done but not shipped
- [ ] **Ship data features** - done but not shipped
- [ ] **Thinking Partner** - needs Horacio testing before ship

---

## Administrative Tasks (NEW - from Handwritten Notes)

- [ ] **Nuevos contratos para Daniel y Mike**
- [ ] **Set up Claude-Code account for Shamil**
  - Create shared account like oas@stoic.enterprise

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

- [ ] **Dev tools discussion**
  - Linear vs Asana for development tracking
  - Asana OK for general coordination, dev can have own tool

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
- Handwritten notes: `handwritten-notes-transcription.md`
- Vision document: `conscious-insights-v2-english.md`
- Pitch slides: `index.html` (Netlify deployed)
