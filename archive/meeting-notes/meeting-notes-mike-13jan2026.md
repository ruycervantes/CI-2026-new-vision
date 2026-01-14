# Meeting Notes: Ruy & Mike - January 13, 2026

## Context
Planning session for Q1 roadmap. Ruy presented the Conscious Insights v2 vision using the pitch slides and diagrams.

---

## Key Decisions

### Q1 Feature Priorities (Deliver 3 of 4)

| Priority | Feature | Owner | Notes |
|----------|---------|-------|-------|
| 1 | **MS Teams Notifications** | Mike | Already in progress. Foundation for everything else. |
| 2 | **Thinking Partner Multi-Session Coaching** | Ruy + Shamil | Requires memory layer. Key differentiator. |
| 3 | **Voice Integration** (text-to-speech) | TBD | "Wow factor" for demos. 11Labs exploration. |
| 4 | **Bidirectional Teams Chatbot** | Mike | Check-ins via Teams instead of app. Removes friction. |

**Decision:** Prioritize 1-3 first. Feature 4 vs Voice needs customer validation.

### Quarterly OKRs Structure
- **Objective 1:** Develop new features for a more complete coaching experience
  - KR: Deliver 3 major features with user validation criteria
- **Objective 2:** Establish Product-Market Fit validation process
  - KR: Customer validation before building features

---

## Technical Discussions

### Memory/Coaching Architecture
- Current user facts system may suffice initially (dates + facts)
- Can evolve to Graphiti later if needed
- Key: capture goals, track progress across sessions, maintain coaching methodology

### Thinking Partner Multi-Session Flow
- Session 1: Establish goals, define gap
- Subsequent sessions: Review progress, work on specific areas
- Needs: goal storage, session continuity, coaching methodology in prompts
- **Reference:** Ruy to interview Horacio about his coaching note-taking methodology

### MS Teams Integration Phases
1. Phase 1: One-way notifications (current focus)
2. Phase 2: Bidirectional chatbot (check-ins, scheduling)
3. Future: Meeting interventions (technically feasible but lower priority)

### Email/Outlook Integration
- Deprioritized for now
- Needs strong context manager and memory first
- Privacy concerns to address
- Focus on Microsoft ecosystem (most clients use it)

---

## Process Improvements Agreed

| Area | Action | Owner |
|------|--------|-------|
| Testing flow | Leonardo approves demo-ready features | Leo |
| Deployment scripts | Daniel completes automation script | Daniel |
| Demo environment | Update CI-demo with latest features | Mike + Leo |
| Sprint planning | More preparation between Ruy & Mike before planning | Ruy + Mike |

### Team Leadership Transition
- Mike takes more day-to-day leadership of dev team
- Can assign urgent tasks to Daniel/Shamil outside sprint
- Daily standups for visibility (Daniel, Shamil)
- Ruy focuses on prototyping, methodology, customer validation

---

## Next Steps: Ruy

### This Week (Before Sprint Planning Thursday)

- [ ] **Create roadmap document** from this discussion for Leo and team
- [ ] **Interview Horacio** about coaching methodology
  - How does he take notes?
  - What does he track session-to-session?
  - How does he handle goal evolution?
- [ ] **Review HCI research** (NotebookLM) - longitudinal goal setting patterns
- [ ] **Competitor benchmark** (Mural) - MindGym and others
- [ ] **Update pitch slides** - add goal-based development flow (missing piece noted)
- [ ] **Prepare sprint planning** for Thursday
  - Shamil: Thinking Partner feature (extract goal/gap)
  - Daniel: Deployment script automation
  - Leonardo: Testing approval process

### Customer Validation (With Leo)
- [ ] Set up Product-Market Fit validation process
- [ ] Validate: Would customers buy "application coaching" sessions?
- [ ] Validate: Voice vs Bidirectional Teams chatbot priority

---

## Sprint Planning Agenda (Thursday)

### Tasks to Assign
| Person | Task |
|--------|------|
| Shamil | Thinking Partner: Extract goal/gap feature |
| Daniel | Complete deployment/install automation script |
| Leonardo | Own testing → demo approval flow |
| Mike | Continue MS Teams notifications |

### Process Items
- Introduce daily standups for visibility
- Demo environment update with recent features (executive summary, TTS)

---

## Updates Needed for Vision Document

The `conscious-insights-v2-english.md` document has gaps identified during this meeting:

### 1. Goal-Based Development Flow (Main Gap)
The document talks about microhabits but **goals/metas aren't prominently featured as the starting point**. Need to add:
- User establishes personal goals first (before assessment)
- Goals connect to motivations ("quiero que me quieran más", "quiero tener más impacto")
- Goals are stored, tracked, and can evolve over time
- Goals drive which microhabits are chosen

*From meeting: "Este ciclo iterativo y basado en metas, que no está escrito aquí ahorita. Esto de guardar las metas de las personas e irlas ajustando."*

### 2. Multi-Session Coaching Methodology
**Blocked by:** Interview with Horacio about his note-taking method. Once complete, add:
- How Thinking Partner maintains context across sessions
- Session 1: establish goals/gap
- Subsequent sessions: review progress, work specific areas, reprioritize
- What gets stored between sessions (structured notes, not just conversation history)

### 3. Goals Dashboard Detail
Priority 7 mentions dashboard but lacks specifics. Add:
- What the user sees: their goals, progress toward each, trajectory
- How goals connect to microhabits visually
- Goal evolution over time (not static)

### 4. Pitch Slides Update
*"A esas necesito hacerles un ajuste de lo de goal-based development"* - same content gap applies to the HTML presentation.

---

## Open Questions

1. **Voice vs Bidirectional chatbot** - which has more customer interest?
2. **Graph memory** - can we prototype effectively with current user facts + dates?
3. **External dev resources** - can we increase Daniel's hours for infra?

---

## Quotes to Remember

> "Si nos quedamos como 'tenemos un chatbot de coaching', competimos con todos. Si nos posicionamos como 'somos dueños del ciclo de cambio de comportamiento', es otra conversación."

> "Lo que hace Horacio es ir tomando notas y entonces se queda con un cuadernito... me pregunta '¿traes algo o quieres empezar por lo que habíamos dicho?'"

---

## Files Referenced
- Vision document: `conscious-insights-v2-english.md`
- Diagrams: `diagrams/` folder
- Pitch slides: Netlify-deployed HTML presentation
