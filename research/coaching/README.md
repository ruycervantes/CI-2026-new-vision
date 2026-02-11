# Coaching Research

Research supporting the AI Coach design for the Stoic platform. This folder contains primary methodology sources, raw interview transcripts, detailed case analyses, and strategic synthesis documents.

## Research Approach

The research follows two complementary tracks:

1. **Theory** — The Axialent Application Coaching Handbook provides the formal 8-step session methodology, rooted in Conscious Business principles. This is the "what should happen" layer.
2. **Praxis** — Observed coaching practice from Horacio (experienced Axialent coach), through Ruy's own 4-session coaching engagement, three sanitized case studies (CASO 1-3), and two extended interviews. This is the "what actually happens" layer.

**Key informants:** Horacio (coach, primary source for methodology + praxis), Richi (coach, methodology validation + live demo), Ruy (coachee, 4 sessions with transcripts).

**Current status:** Phases A.2 + B + B.2 complete. 30 inter-session praxis principles + 10 setup praxis principles documented across 4 cases. 11 universal inter-session principles confirmed, 5 context-dependent. Cross-case synthesis and setup methodology extraction complete.

**Next:** Phase C (Interview Horacio — 11 refined questions from setup analysis + existing topics), Phase E (Draft Doc A — the coaching methodology + praxis reference document).

---

## File Map

### Strategic Docs (root)

The "what are we building and why" layer.

| File | Purpose | Feeds |
|------|---------|-------|
| `ai-coach-spec-plan.md` | Execution roadmap — 4 workstreams, phases, asset inventory | Everything (master plan) |
| `coaching-knowledge-framework.md` | Master synthesis — 3-layer model (methodology, praxis, product), 14 design implications | Doc A, Doc B |
| `ai-coach-design-considerations.md` | Architecture decisions — memory paradigms, open questions | Doc B (AI design synthesis) |
| `minimum-ai-coaching-for-te.md` | What's needed for HPT MVP vs. full AI Coach vision | Doc B (scope decisions) |
| `axialent-coaching-handbook-summary.md` | Formal 8-step methodology from the Axialent Coaching Handbook | Doc A §2 (Theory) |

### Analysis

The "what did we learn" layer. Case analyses follow a consistent structure: session opening mechanics, commitment cycles, topic threading, and handbook mapping.

| File | Purpose | Feeds |
|------|---------|-------|
| `analysis/inter-session-architecture-analysis.md` | Ruy's 4-session arc — the original A.2 extraction + Part 8 cross-case validation | Doc A §4-5 |
| `analysis/caso1-inter-session-architecture-analysis.md` | CASO 1: COACHEE1/EMPRESA1 — anxiety/leadership, parallel tracks, behavioral substitution | Doc A §6.1 |
| `analysis/caso2-inter-session-architecture-analysis.md` | CASO 2: COACHEE2/EMPRESA2 — instrumental reasoning, horizontal graduation, ITC breakthrough | Doc A §6.1 |
| `analysis/caso3-inter-session-architecture-analysis.md` | CASO 3: COACHEE3/EMPRESA3 — green/defensive, role play, "bache" productive emptiness | Doc A §6.1 |
| `analysis/coaching-cases-analysis.md` | Cross-case comparison — universality table, 30 principles, coachee typology, 12 AI design principles | Doc A §4-7, Doc B |
| `analysis/horacio-case-study-analysis.md` | Early Horacio case study (sessions 1-3 detailed, pre-A.2 format) | Doc A §6.1 |
| `analysis/horacio-intervention-setups.md` | Engagement types and setup structures from Horacio | Doc A §4.1 |
| `analysis/setup-methodology-analysis.md` | Setup methodology extraction — theory vs. practice, LSI debrief anatomy, 10 setup praxis principles, AI pre-coaching flow design | Doc A §4.1, Workstream 4 |
| `analysis/ruy-setup-session-reconstruction.md` | Ruy's Dec 17 setup session recall — non-LSI comparison case | Doc A §4.1 |
| `analysis/methodology-observations-jan2026.md` | Early methodology observations (Jan 2026) | Doc A §3 |
| `analysis/horacio-product-discovery-summary.md` | Summary of Horacio product discovery conversation (AI coaching product design) | Doc A, Doc B |

### Interviews

Raw transcript data from coaching methodology interviews.

| File | Purpose |
|------|---------|
| `interviews/horacio-jan2026/Coaching Ruuy - horacio 12 jan 2026.txt` | Horacio coaching session transcript (Jan 12) |
| `interviews/horacio-jan2026/Entendimiento de procesos de coaching - diseño producto AI - horacio y ruy.txt` | Extended interview — coaching process understanding for AI product design |

### Sources

Primary methodology documents and coaching case PDFs. These are the raw inputs that feed the analysis layer.

| File | Purpose |
|------|---------|
| `sources/Axialent Coaching Handbook Spanish v1 2013 - full.docx` | Original Axialent Coaching Handbook (Spanish, v1 2013) |
| `sources/Coaching Handbook - V2013 Español - Revisada para UDESA.pdf` | Revised handbook version (UDESA edition) |
| `sources/AC_MagicCards-BAC4L-ver1.pdf` | Application Coaching "Magic Cards" — quick-reference intervention cards |
| `sources/CB Standard Participant Workbook - June 2011 (A4) INTERNAL!.pdf` | Conscious Business participant workbook (PDF) |
| `sources/CB Standard Participant Workbook - June 2011 (A4) INTERNAL!.ppt` | Conscious Business participant workbook (PPT) |
| `sources/coaching_cases/CS - CASO 1.pdf` | Horacio's coaching case 1 — COACHEE1/EMPRESA1 (chemical company) |
| `sources/coaching_cases/CS - CASO 2.pdf` | Horacio's coaching case 2 — COACHEE2/EMPRESA2 (industrial/packaging) |
| `sources/coaching_cases/CS - CASO 3.pdf` | Horacio's coaching case 3 — COACHEE3/EMPRESA3 (supply chain LATAM) |

---

## Key Findings

**30 praxis principles** documented across 4 coaching engagements:
- **11 universal** — structural principles present in all cases (One Long Conversation, Commitment as Doorway, Theme Graduation, Named Entity Tracking, etc.)
- **5 context-dependent** — specific interventions requiring conditions (Gift Question, Desdoblamiento, Outlier vs Design)
- Universal principles are *structural* (how coaching works across sessions); context-dependent ones are *techniques* (deployed based on readiness)

**Session 3 emergence pattern** — confirmed in 3 of 4 cases. Around session 3, surface issues resolve and deeper root causes emerge. This is a predictable structural feature, not coincidence.

**4 coachee types observed:**
1. Clean escalation (Ruy) — surface → depth → resolution
2. Parallel tracks (CASO 1) — two themes that never converge
3. Horizontal graduation (CASO 2) — topic shifts laterally rather than deepening
4. Recursive (CASO 3) — surface resolves, depth emerges, pattern reasserts

**12 AI Coach design principles** derived from multi-case evidence — see `analysis/coaching-cases-analysis.md` for full details.

---

## Reading Order

For someone new to this research:

1. **This README** — orientation and file map
2. **`ai-coach-spec-plan.md`** — the execution roadmap (what we're building and how)
3. **`coaching-knowledge-framework.md`** — master synthesis (3-layer model, design implications)
4. **`analysis/coaching-cases-analysis.md`** — cross-case findings (30 principles, universality, coachee types)
5. **`analysis/inter-session-architecture-analysis.md`** — Ruy's case in detail (the most complete single-case analysis)
6. Individual case analyses (`caso1-`, `caso2-`, `caso3-`) as needed
7. **`axialent-coaching-handbook-summary.md`** — the formal methodology (theory layer)
