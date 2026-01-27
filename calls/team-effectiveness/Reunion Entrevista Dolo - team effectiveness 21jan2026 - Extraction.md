# Dolo Call Extraction

**Source:** Reunion Entrevista Dolo - team effectiveness 21jan2026
**Extraction Date:** 23 Jan 2026

---

## 1. Design Principles

How should coaching/team development work?

### DP1: Stewardship of AI

> "Yo creo que tiene que ser human led en general... necesitas el stewardship, necesitas la revisión de que eso tiene sentido."

Don't deploy AI blindly. Maintain thoughtful human oversight in the development process of a team. This is about responsible use, not about limitation.

Many things CAN be automated (assessment collection, pattern analysis, AI coaching, meeting minutes, etc.). But there needs to be a human in the loop who:
- Validates that outputs make sense
- Provides context interpretation
- Makes final decisions on interventions

**Implication for product:** Build in checkpoints for human review. Don't create fully autonomous team development — create AI-augmented human-led processes.

---

### DP2: Work Both Levels Simultaneously

> "Trabajás en la dimensión individual y en la dimensión colectiva en simultáneo... Son procesos paralelos."

You can't separate individual development from team dynamics. The individual patterns CREATE the team patterns. HPT works both levels in parallel:
- Individual coaching for each leader
- Team interventions for collective dynamics

**Implication for product:** Don't build "individual coaching" and "team coaching" as separate products. They're intertwined. The individual coaching must be contextualized in team outcomes.

---

### DP3: Trust Before Task

> "Sin esa confianza, no puedes hacer la verdad indiscutibles, no puedes tener conversaciones difíciles."

The first sessions in any team process focus on:
1. Building trust and psychological safety
2. Clarifying purpose (why this team exists)
3. Creating burning platform (the gap)
4. Making operating agreements

Only AFTER trust is established can you work on execution, accountability, difficult conversations.

**Implication for product:** Any team-level features must account for trust level. Don't push accountability tools on teams that haven't built safety first.

---

### DP4: Content Foreground/Background Flip

> "En los talleres el contenido está en el forefront, en las facilitaciones el contenido está en el background."

Same distinction Richi made:
- **Workshops:** Philosophy/skills foreground, business context as examples
- **Facilitation:** Business foreground, philosophy as intervention lens

The consultant must be fluent in BOTH modes and know when to use which.

**Implication for product:** An AI assistant might operate differently depending on mode — teaching mode vs. observation mode.

---

### DP5: Interventions Vary by Team

> "No hay un manual, porque las intervenciones varían mucho de equipo a equipo... El consultor entiende cómo se combinan los elementos."

There's no fixed sequence. The consultant reads the diagnostic and the team's specific challenges, then selects from a toolkit:
- Purpose work (if clarity is missing)
- Role clarity (if accountability is the issue)
- Communication skills (if conversations are poor)
- Strategic alignment (if goals are unclear)

**Implication for product:** Can't create a rigid "HPT program." Need adaptive pathways based on diagnostic results.

---

## 2. Methodology References

Frameworks, concepts, how things connect.

### HPT Process Model

```
Context → Diagnostic → Interventions → Tracking
   ↓          ↓              ↓            ↓
Objectives  Team +       Workshops    Self-report
Goals      Individual    Facilitation   Leader check
Success    assessments   Coaching       Re-measure
criteria
```

---

### Assessment Frameworks Used

| Framework | Level | What it measures |
|-----------|-------|------------------|
| **Lencioni (5 Dysfunctions)** | Team | Trust, conflict, commitment, accountability, results |
| **Katzenbach** | Team | 4 dimensions (to be detailed) |
| **Team Pulse** (internal) | Team | Custom dimensions based on above |
| **DISC** | Individual | Behavioral style |
| **LSI** | Individual | Thinking/behavioral styles |
| **OCI** | Organization/Team | Culture patterns |
| **Group Styles Inventory** | Team | Group behavioral patterns |
| **Leadership Impact (LI)** | Individual | Leadership effectiveness |

**Key insight:** The theoretical framework (Lencioni vs Katzenbach) is public — consultants choose which to use. However, Axialent DOES have a **proprietary assessment instrument** — the internal Team Survey (4-Quadrant model) that operationalizes Katzenbach. Dolo has historical data from all HPT processes until 2019.

**Benchmark opportunity:** Dolo is extracting this historical data. Leo noted companies monetize benchmarks ("el promedio de tu industria es 8.9"). This data could enable industry/region benchmarking.

---

### Three Intervention Types (Team Level)

| Type | Content Relation | Use When |
|------|------------------|----------|
| **Workshops** | Foreground | Teaching frameworks, building agreements, clarifying purpose |
| **Group Coaching** | Challenge-based | Working through team dilemmas with coaching approach |
| **Meeting Facilitation** | Background | Real business meetings — intervene to improve dynamics |

Plus: **Individual Coaching** (parallel track for each team member)

---

### First Sessions Content

Initial workshops typically cover:
1. Trust-building exercises
2. Purpose/Why clarification (Legacy work)
3. Burning platform (the gap between current and desired state)
4. Individual "why" connected to team "why"
5. Operating agreements

**Sequence matters:** Trust and purpose FIRST, then execution skills.

---

### Skilled Facilitator Framework (Schwartz)

The methodology Axialent uses for meeting facilitation training. This is the unique skill that separates HPT from other offerings.

**Also referenced:** "Teaching from the Back of the Room" for workshop delivery.

---

### HPT = Component Assembly

Key insight: There is NO separate "HPT methodology." HPT is the assembly of:
- Coaching (same handbook as Leadership Development)
- Teaching/Workshops (same playbook as Leadership Development)
- Facilitation (unique skill — Skilled Facilitator)

> "La parte de skill building es la misma... tenés que mirarlo distinto, por eso tenés que entender el framework con el que lo estás mirando."

The consultant's skill is knowing HOW to combine these components for a specific team's needs.

---

## 3. Digitization Ideas

Product possibilities, what could be built.

### ID1: Team Pulse — Ongoing Assessment Tool

> "Una de las cosas que quiero hacer es un TeamPulse que nos permita hacer el diagnóstico inicial y que nos permita hacer el seguimiento."

**The problem:** Current assessments (Lencioni via Wiley, etc.) capture initial state but don't allow tracking over time. Data stays in external systems.

**Product idea:**
- Initial diagnostic on HPT dimensions
- Periodic re-measurement (lightweight pulse)
- Track trends over time
- See if interventions are moving the needle

**Dolo wants this for 2026.** Could be a Stoic product.

---

### ID2: AI Coach for Conversation Prep

> "Recontra utilizaría los AI coaches para complemento de la parte de coaching individual o incluso del coaching de equipo para preparar conversaciones difíciles."

**Use case:** Before a difficult conversation, team member practices with AI. The AI helps them:
- Clarify what they want to say
- Anticipate reactions
- Find better framing

This is the "role play" functionality Richi described, now specifically for team context.

---

### ID3: Pre-Workshop Wizards

Ruy's idea: Instead of doing everything in live workshops, pre-work wizards could help teams:
- Draft their purpose statement
- Do initial RACI exercises
- Surface individual perspectives before group session

**Dolo's response:** "Definitivamente podés... pero no puedes saltear la instancia de conversación y de validación grupal."

**Implication:** Wizards can PREPARE but not REPLACE live sessions.

---

### ID4: AI Pattern Analysis on Diagnostics

> "En los diagnósticos de cultura ya yo utilizo o ya utilizamos inteligencia artificial para un montón de análisis de patrones."

Already happening at Axialent. AI analyzes qualitative diagnostic data to find patterns humans might miss.

**Product opportunity:** Standardize this. Make it part of the Team Pulse product.

---

### ID5: Learning Recommendations Engine

> "Estamos tratando de activar los learning journeys dentro del LMS y los learning recommendations a partir de una serie de preguntas."

**Idea:** Same logic could work for:
- **Consultants:** Help prepare/design workshops based on diagnostic
- **Participants:** Recommend self-led learning based on gaps

---

### ID6: Benchmark Database

Leo's insight:
> "Yo conozco empresas que monetizan el benchmark... querés ver el promedio de tu industria en este país, del high performance team, es 8.9."

**Opportunity:** Axialent has historical data from HPT processes (2019 and earlier). Could:
- Create industry benchmarks
- Show teams how they compare
- Monetize the data itself

**Blocker:** Data infrastructure is a mess. Needs cleanup first.

---

### ID7: Meeting Minutes with Human Review

> "Podés usar una IA para que te arme las meeting minutes y después las revisás y las mandás."

Simple use case. AI generates meeting summary, human reviews before sending.

**Dolo's caution:** "Sino después te dice cualquier cosa."

---

## 4. Action Items

### For Ruy

- [ ] Review HPT proposals in Moure (both Lencioni-based and Katzenbach-based structures)
- [ ] Meet with Leo — get his HPT experience, documentation, roleplay of processes
- [ ] Meet with Valentín — deep dive on how he runs HPT
- [ ] Read Skilled Facilitator (Schwartz) — the facilitation methodology
- [ ] Read Lencioni (5 Dysfunctions) — understand the framework
- [ ] Read Katzenbach — understand the framework
- [ ] Schedule biweekly sync with Dolo (post-vacation, early Feb)

### For Dolo

- [ ] Send old Readiness materials for HPT
- [ ] Send facilitation training materials
- [ ] Find HPT offering deck and send to Ruy
- [ ] Partner round on "Blended by Design" mindset (post-vacation)

### For Product Roadmap

- [ ] Consider Team Pulse as a Stoic product (Dolo wants this for 2026)
- [ ] AI coach for conversation prep — aligns with "role play" from Richi
- [ ] Pre-workshop wizards (with caveat: prep not replace)

### Open Questions

1. **Lencioni vs Katzenbach:** Which framework should the digital product use? Or should it support both?
2. **Assessment ownership:** If we build Team Pulse, who owns the data? Axialent or client?
3. **Facilitation digitization:** Is there ANY role for AI in meeting facilitation? Or is this purely human?
4. **Historical data:** How do we get access to Dolo's historical HPT data? What state is it in?

---

## Synthesis for Team Effectiveness Vision

**What this call clarifies:**

1. **No proprietary HPT framework.** Axialent uses public frameworks (Lencioni OR Katzenbach) for team assessment. The differentiation is CB philosophy applied to teams + consultant judgment + facilitation skill.

2. **HPT = component assembly.** The consultant combines coaching + teaching + facilitation based on team needs. There's no "HPT manual" — the consultant IS the integration layer.

3. **Many things CAN be automated.** Assessment collection, pattern analysis, AI coaching, meeting minutes, conversation prep — all candidates. Dolo is not limiting, she's advocating for thoughtful stewardship.

4. **Human stewardship required.** Not "AI can't do this" but "don't deploy blindly." Human in the loop for validation, context, final decisions.

5. **Meeting facilitation is the unique skill.** This is where HPT differs from Leadership Development — and it's the hardest to digitize (stays human-led).

6. **Team Pulse is a strong candidate.** Initial assessment + ongoing tracking. Dolo actively wants this for 2026.

7. **Trust-first sequencing matters.** Any team product must respect that trust/safety comes before accountability/execution.

