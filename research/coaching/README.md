# Coaching Research

Research supporting the AI Coach design for the Stoic platform. This folder contains primary methodology sources, raw interview transcripts, detailed case analyses, and strategic synthesis documents.

## Reading Order

1. **`coaching-arc-synthesis.md`** — **START HERE.** Doc A — the full coaching arc from Meeting Zero to closing, synthesized from 4 engagements. This is the coaching process reference.
2. **`axialent-coaching-handbook-summary.md`** — The formal 8-step session methodology (Axialent theory baseline).
3. **`ai-coach-design-considerations.md`** — Forward-looking: memory paradigms, architecture decisions for Doc B.
4. **`minimum-ai-coaching-for-te.md`** — Forward-looking: what HPT needs from coaching.
5. **`ai-coach-spec-plan.md`** — Execution roadmap: 4 workstreams, phases, asset inventory.

---

## Folder Structure

```
research/coaching/
├── README.md                              ← you are here
├── coaching-arc-synthesis.md              ← Doc A (the coaching process reference)
├── axialent-coaching-handbook-summary.md  ← theory baseline (8-step methodology)
├── ai-coach-design-considerations.md     ← feeds Doc B (memory, architecture)
├── minimum-ai-coaching-for-te.md         ← feeds Doc B (HPT scope)
├── ai-coach-spec-plan.md                 ← execution roadmap
│
├── process/                               ← intermediate analysis (fed Doc A)
│   ├── coaching-knowledge-framework.md    ← earlier 3-layer synthesis (superseded by Doc A)
│   ├── inter-session-architecture-analysis.md  ← Ruy's 4-session A.2 extraction + cross-case validation
│   ├── caso1-inter-session-architecture-analysis.md  ← CASO 1: COACHEE1/EMPRESA1
│   ├── caso2-inter-session-architecture-analysis.md  ← CASO 2: COACHEE2/EMPRESA2
│   ├── caso3-inter-session-architecture-analysis.md  ← CASO 3: COACHEE3/EMPRESA3
│   ├── coaching-cases-analysis.md         ← cross-case comparison (30 principles, universality)
│   ├── setup-methodology-analysis.md      ← setup extraction (10 setup praxis principles)
│   ├── ruy-setup-session-reconstruction.md  ← Ruy's Dec 17 setup recall
│   ├── horacio-case-study-analysis.md     ← early case study (pre-A.2 format)
│   ├── horacio-intervention-setups.md     ← engagement types and setup structures
│   ├── horacio-product-discovery-summary.md  ← product discovery conversation
│   └── methodology-observations-jan2026.md  ← early observations (Jan 2026)
│
├── sources/                               ← raw methodology docs and case PDFs
│   ├── coaching_cases/                    ← Horacio's 3 sanitized cases (CS CASO 1-3)
│   └── ...                                ← Handbook, Magic Cards, CB Workbook
│
└── interviews/                            ← raw interview transcripts
    └── horacio-jan2026/                   ← 2 Horacio interviews (Jan 2026)
```

---

## Research Approach

The research follows two complementary tracks:

1. **Theory** — The Axialent Application Coaching Handbook provides the formal 8-step session methodology, rooted in Conscious Business principles. This is the "what should happen" layer.
2. **Praxis** — Observed coaching practice from Horacio (experienced Axialent coach), through Ruy's own 4-session coaching engagement, three sanitized case studies (CASO 1-3), and two extended interviews. This is the "what actually happens" layer.

**Key informants:** Horacio (coach, primary source for methodology + praxis), Richi (coach, methodology validation + live demo), Ruy (coachee, 4 sessions with transcripts).

**Current status:** Doc A (coaching-arc-synthesis.md) is the primary reference. The `process/` folder contains the intermediate analyses that fed it.

---

## Key Findings

**40 praxis principles** documented across 4 coaching engagements (30 inter-session + 10 setup):
- **11 universal** — structural principles present in all cases (One Long Conversation, Commitment as Doorway, Theme Graduation, Named Entity Tracking, etc.)
- **5 context-dependent** — specific interventions requiring conditions (Gift Question, Desdoblamiento, Outlier vs Design)
- Universal principles are *structural* (how coaching works across sessions); context-dependent ones are *techniques* (deployed based on readiness)

**Session 3 emergence pattern** — confirmed in 3 of 4 cases. Around session 3, surface issues resolve and deeper root causes emerge.

**4 coachee types observed:**
1. Identity Seeker (Ruy) — surface → depth → resolution
2. Safe Space User (CASO 1) — two themes that never converge
3. Instrumental Reasoner (CASO 2) — topic shifts laterally rather than deepening
4. Defensive Practitioner (CASO 3) — surface resolves, depth emerges, pattern reasserts

**12 AI Coach design principles** derived from multi-case evidence — see `process/coaching-cases-analysis.md` for full details.
