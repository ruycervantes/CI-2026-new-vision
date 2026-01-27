# Team Effectiveness Vision: Work Plan

**Created:** 23 Jan 2026
**Status:** Active planning document

---

## The System We're Designing For

### The Triangle (Activity System)

Three elements in constant interaction:

```
        Shared Artifacts
       (norms, processes,
        infrastructure)
              ▲
             / \
            /   \
           /     \
          ▼       ▼
    Individual ◄──► Flow of Work
    (behavior,      (actual work,
     mindsets)       the object)
```

This is a complex system with multiple relationships. Understanding where and when to intervene requires two dimensions.

### Two Dimensions of Intervention

**Dimension 1: Levels of the System**
- **Personal** — Individual behavior, mindsets, skills
- **Team** — Collective artifacts, shared agreements, group dynamics
- **System** — Infrastructure, tools, narratives (the substrate that enables everything else)

**Dimension 2: Temporal**
- **Before** — Preparation, setup, planning for future work
- **During** — In the specific actions (meetings, conversations, tasks)
- **After** — Reflection, sense-making about what happened

### The Intervention Matrix

|  | Before | During | After |
|--|--------|--------|-------|
| **Personal** | Individual goal-setting, preparation | Self-monitoring in action | Personal reflection, coaching |
| **Team** | Building accords, planning together | Meeting facilitation, collective action | Team retrospectives, debriefs |
| **System** | Infrastructure setup, tool config | Dashboards, real-time feedback | Analytics, system-level learning |

**Interactions between cells matter.** For example:
- After/Personal (coaching) feeds into Before/Team (new accords based on what individuals learned)
- During/System (dashboard) enables After/Personal (reflection on data)
- Before/Team (shared artifacts) shapes During/Personal (how individuals act)

This framework aligns with activity theory (levels of analysis + developmental cycles) and CSCW research (time/space matrices, individual-group-organizational levels).

### Key Insight

Individual coaching is not separate from flow of work. In coaching sessions, you review what happened in the flow of work, reflect on the gap between "how we said we'd work" and "how it actually went," and work on behavior changes. The individual work is always in service of the system.

### Where the MVP Lives

The MVP primarily occupies:
- **After/Personal** — Individual coaching (AI coach)
- **Before/Team** — Assessments, opening the gap collectively (human coach facilitates)
- **System layer** — The methodology itself (CB, High Performing Teams) as narrative infrastructure

Future products can expand into other cells (During/Team for facilitation, During/System for dashboards, etc.).

---

## Three Components of Team Effectiveness

### 1. Team Setup

Shared artifacts that the team builds together:
- Principles
- Processes
- Agreements/accords
- Norms
- Infrastructure

These are what make the team more than the sum of its parts. They can be:
- Built from scratch
- Renegotiated if they need updating
- Surfaced if they exist implicitly but were never discussed

### 2. Flow-of-Work Interventions

During actual work (especially meetings), catching specific behaviors or ways of saying things that could be more effective. Bringing them to consciousness.

**Current state:** Human facilitator in meetings
**Future possibilities:** Dashboards, visualizations, real-time feedback systems

### 3. Individual Behavior Change

Personal development in service of team effectiveness. This includes:
- Reflecting on flow of work against shared accords
- Identifying personal gaps
- Working on behavior/mindset changes
- Building new habits

**Why start here:** Most digitizable, we've built pieces already, clearest path to product.

---

## Two Sequences (MVP vs. Future)

### MVP Sequence

```
Team Setup → Flow of Work (gaps emerge) → Individual Coaching (close gaps)
                                                    ↓
                                          (reflects on flow of work,
                                           works on personal changes)
```

Or shorter path:
```
Team Setup → Individual Coaching (thinking about flow of work gaps)
```

The individual coaching incorporates reflection on flow of work even without live facilitation.

### Future Sequence

```
Team Setup → Flow of Work → Immediate Feedback → Less need for later reflection
                              (live facilitator,
                               dashboards,
                               visualizations,
                               in-flow systems)
```

Interventions happen closer to the moment, more integrated into work itself.

---

## MVP Hypothesis

**Components:**
1. Team effectiveness assessment (4 quadrants, Katzenbach-based) → WHERE team underperforms
2. Individual CB assessment → WHAT behaviors/mindsets contribute to gap
3. Human coach facilitates debrief, opens the gap collectively
4. AI coach continues individual work (modified Thinking Partner)

**The bet:** We can deliver value starting with individual coaching that's connected to team outcomes, then build the other intervention layers.

---

## MVP Implementation Approach

### Phase 1: Hybrid HPT (Learn by Doing)

Run HPT engagements with human consultant + AI coaching:

| Component | Who | What |
|-----------|-----|------|
| **Team Assessment** | Consultant (Horacio) | Team Survey (4-Quadrant) + interpretation |
| **Individual Assessment** | Tech | CB Assessment |
| **Team Interventions** | Consultant | Offsites, facilitation, group work |
| **Individual Development** | AI Coach | Scaled coaching for team members |

**Why start here:**
- Consultant is the integration layer — don't try to replace yet, use it as the learning engine
- AI coaching already works — that's our scalable contribution now
- Learn what other tech opportunities exist by observing real engagements

**Assets we have:**
- Team Survey instrument (4-Quadrant) — see `research/sources/team-effectiveness/Gabinete - Cuestionario equipo v1.docx`
- Historical Team Survey data — see `research/sources/team-effectiveness/ARG LLT Survey Summary data.xlsx`
- CB Assessment (already in product)
- AI Coach (Thinking Partner — needs modification for team context)

**To make this real:**
- [ ] Find/create HPT engagement to pilot hybrid approach
- [ ] Horacio runs Team Survey + interprets + designs intervention
- [ ] AI coach deployed for team members (individual development)
- [ ] Ruy observes / documents what happens
- [ ] After engagement: capture what worked, what could be tech-supported, what products emerge

### Phase 2: Expand Based on Observation

**Note:** Phases aren't strictly sequential. We can prototype Phase 2 ideas WHILE doing Phase 1 — the hybrid engagement is the learning context for both.

Opportunities already identified from calls:

| Opportunity | Source | What it is |
|-------------|--------|------------|
| **Meeting Dashboard** | Richi | Analyze team conversations for CB patterns (knower mode, victim mode, commitment quality) |
| **Team Pulse** | Dolo | Track team health over time with periodic re-measurement |
| **Pre-workshop Wizards** | Ruy | Prep work before human-led sessions (draft purpose, RACI, etc.) |
| **Benchmark Database** | Leo | Industry/region comparisons using historical Team Survey data |

**Additional ideas:** See Mural with CHI/CSCW paper analysis for tech interventions in team effectiveness: https://app.mural.co/t/axialent8953/m/axialent8953/1764890677283/ad8559ddadff366460dab38357447aaeeeea02d1

---

## Differentiation

We are opinionated about methodology:
- **Individual development:** Conscious Business, Application Coaching
- **Team development:** High Performing Teams framework (Katzenbach + Axialent experience)

This is not generic "coaching AI." The Axialent knowledge becomes productized.

**To validate:** Does this opinionated methodology create real differentiation? Does it help us sell? Does it make us more effective?

---

## Work Plan

### Phase 1: Clarify Framework

| Step | Task | Output |
|------|------|--------|
| 1.1 | Review and polish the triangle/system explanation above | Clean framework description |
| 1.2 | List what you know vs. what you need from calls | Knowledge gaps |
| 1.3 | Sharpen MVP hypothesis | Clear MVP definition |

### Phase 2: Process Calls

**Custom extraction workflow (not /process-call):**

For each call:

**Step 1: Summary**
- Create index of call sections with line numbers
- Write executive summary
- Identify key quotes

**Step 2: Extraction**
- Extract **design principles** — How should coaching/team development work?
- Extract **methodology references** — Frameworks, concepts, how things connect
- Extract **digitization ideas** — Product possibilities, what could be built
- Extract **action items** — Next steps, decisions needed

**Step 3: Review**
- Discuss extractions to ensure they're well captured
- Refine, correct, or add missing insights
- Confirm before moving to next call

| Call | Focus Areas |
|------|-------------|
| `Reunion Entrevista Dolo - team effectiveness 21jan2026.txt` | Team effectiveness assessment, 4 quadrants, Katzenbach framework |
| `Continuación - explicación proceso coaching -horacio and ruy 22jan2026.txt` | Coaching methodology, how to run good sessions |
| `1-1 Oseas Ruy 22jan2026.txt` | MVP ideas, strategic direction, buyer (HR vs. boss of team lead) |
| `Application Coaching- preguntas sobre la metodología y la praxis - richi and ruy 22jan2026.txt` | Role playing technique, two aha moment types, design principles |

**After all calls: Synthesis**
- Pull together extractions from all calls
- Identify what's repeated across calls (strong signals)
- Identify what's different (perspectives to reconcile)
- Identify key design challenges that emerged
- Create consolidated list of design principles, methodology, and product implications

---

## Ongoing Design Challenges

Track these as they emerge from calls. These are hard problems to solve for the AI coach.

### DC1: Creating Moments of Truth in AI

**The problem:** The gap between espoused values and values-in-action is the raw material for change. But HOW you surface that gap determines whether learning anchors. In human coaching, the coach is in the room. How does AI do this?

**Possible approaches (emerging):**
- **Pattern recognition over time** — AI notices recurring themes, contradictions across sessions. Maintaining the thread across sessions is crucial. (Horacio discusses this in CB assessment methodology)
- **In-session contradictions** — User says X, then contradicts. AI names it gently. (Richi demo)
- **Role play as practice** — Before a conversation, practice with AI. Skill to build.
- **Post-conversation reflection** — "How did it go? What did you actually say?"

**Key insight from Richi:** Shared values (CB principles) help find contradictions even without full context. The frame matters.

---

### DC2: Role-Playing as Coaching Skill

**The problem:** Role-playing is a core coaching technique, but HOW a skilled coach runs a role play is tacit knowledge. What are they listening for? When do they intervene? How do they know when to "stop the tape"?

**Observations from Richi Demo (Ruy/Oseas role play):**

| Phase | What Richi Did | The Skill |
|-------|----------------|-----------|
| **Setup** | "Imagínate que eres Oseas, y yo soy Ruy" | Create safe container for practice |
| **Modeling** | Fed Ruy the opening words to try | Literally demonstrate the speech pattern |
| **Play it out** | Took on the OTHER person's role | Help coachee experience what they'll hear |
| **Stuck point** | Ruy-as-Oseas says "No tengo respuesta" | Let the difficulty surface |
| **Intervention** | "No me estás ayudando a ayudarte" | Name the underlying pattern |
| **Reframe** | "Habla de la agenda de Oseas, no la de Ruy" | Connect to principle (service vs self) |
| **Crystallize** | Ruy articulates: "Lo mío está subordinado al valor que agrego al sistema" | Coachee owns the insight |

**The underlying principle:** "Ayúdame a ayudarte" — When you need something, frame it in terms of serving the OTHER's agenda. This:
- Opens the listener's heart
- Removes defensiveness
- Makes you a giver, not a taker
- Connects individual need to system optimization

**Design questions:**
1. Can AI play the "other person" role effectively?
2. How does AI know when to "stop the tape" and intervene?
3. How does AI model alternative phrasings without being preachy?
4. How does AI help coachee discover the reframe vs. telling them?

---

## Design & Validation Approach

### Eliciting Tacit Knowledge

**The challenge:** The "magic" is not in the documentation. Expert coaches like Richi and Horacio do things that aren't captured in the Application Coaching manual or CB Workbook. We need to surface this.

**Approach:**
1. **Observe in action** — Watch how they actually coach (the Richi demo was an example)
2. **Compare to documentation** — What's in the manuals vs. what they actually do
3. **Name the gaps** — Create explicit descriptions of the tacit skills
4. **Build prototype** — Create first version that attempts these skills
5. **Get feedback** — Have them experience the AI and critique it

### Validation with Expert Coaches

**Goal:** AI coach that both Richi and Horacio find "passable" — good enough to be useful, grounded in the methodology they practice.

**Why both?**
- They may emphasize different aspects of CB/Application Coaching
- Two lenses helps find what's essential vs. personal style
- Builds broader buy-in for the approach

**Process:**
1. **Initial training sessions** — Have Richi and Horacio each interact with the AI as coachee
2. **Capture critiques** — What did it miss? What felt off? What was good?
3. **Iterate** — Refine based on their feedback
4. **Ongoing refinement** — Periodic check-ins as product evolves

### What to Elicit (Starter List)

From each expert, understand:
- **What do you listen for?** — Patterns, contradictions, emotional tone
- **When do you intervene?** — What triggers you to stop and name something?
- **What words do you use?** — Specific phrasings that work
- **What do you NOT do?** — Boundaries, things that don't help
- **What's non-negotiable?** — Principles that can't be compromised

---

### Phase 3: Build Vision Document

| Step | Task |
|------|------|
| 3.1 | Create `core/team-effectiveness-vision.md` |
| 3.2 | Draft the problem — What we're solving, for whom |
| 3.3 | Draft the methodology — Three components, how they interact |
| 3.4 | Draft the product — What we build, MVP first |
| 3.5 | Draft the differentiation — Why Axialent methodology matters |
| 3.6 | Review with Oseas/team, iterate |

---

## Parallel Track: Enterprise Integration

Separate from vision work. See `enterprise-integration-notes.md`.

Question to address: How do we integrate with enterprises so they want to work with us? What do we build in Q1 to avoid Sigma-type situations?

---

## Open Questions

1. **MVP buyer:** HR or boss of team lead? (Extract from Oseas call)
2. **Assessment mapping:** How do team assessment quadrants map to CB individual patterns? (Needs consultant work, but sketch hypothesis)
3. **Thinking Partner dependency:** Does individual coaching need to work well before we layer team effectiveness on top? Or does the team context actually help focus the coaching?
4. **Differentiation validation:** How do we test that opinionated methodology matters to buyers?

---

## Reference Materials

- Mural with team effectiveness literature: https://app.mural.co/t/axialent8953/m/axialent8953/1764890677283/ad8559ddadff366460dab38357447aaeeeea02d1
- Team effectiveness sources: `research/sources/team-effectiveness/`
- Application coaching sources: `research/sources/application-coaching/`
- Existing vision: `core/vision.md`
