# Call Processing Plan — 28 Jan 2026

## Goal
Process 3 call transcripts in sequence, producing updated roadmap/vision, a new AI coach design doc, and enterprise integration specs.

## Sequence

### Step 1: Process Nelson 1-on-1 (27 Jan)
**Source:** `calls/Sesión product strategy catch up con Nelson 27ene2026.txt`

**Outputs:**
- `thinking/ai-coach-design-considerations.md` — exploratory design ideas for the AI general coach feature (memory, multi-session tracking, document artifacts, agent SDK approaches, integration with team context, etc.)
- Extracted agreements/decisions from the Nelson conversation (captured in the summary/analysis)
- Notes flagged for roadmap/vision (not applied yet — wait for Step 2 to confirm)

**Use:** `/process-call` on the Nelson file

---

### Step 2: Process Product Strategy — Office Hours (28 Jan)
**Source:** `calls/Stoic Office Hours - 28jan2026 - Product Strategy (Oseas Nelson Mike Ruy).txt`

**Outputs:**
- Confirmed roadmap items (what Oseas/Nelson/Mike agreed on)
- Enrich `thinking/ai-coach-design-considerations.md` with confirmed ideas (especially analytics emphasis from Oseas) — stays in `thinking/` until `core/` is cleaned up
- **Apply updates to `core/roadmap.md`** — now informed by both Nelson 1-on-1 and group agreements
- **Apply updates to `core/vision.md`** if needed

---

### Step 3: Process Mike Ruy Chat — Office Hours (28 Jan)
**Source:** `calls/Stoic Office Hours - 28jan2026 - Mike Ruy Chat.txt`

**Outputs:**
- Q1 shipping specifics → refine `core/roadmap.md` if needed
- Sprint focus and team organization → feed into sprint planning
- Concrete next actions for the team
- Enterprise integration decisions/priorities (feed into Step 4)

---

### Step 4: Write Enterprise Integration Specs
**Sources:** Mike Ruy Chat outputs + `enterprise-integration-notes.md` (existing strategy doc)

**Outputs:**
- Updated or new enterprise integration specs — Q1 focus areas for identity/SSO (WorkOS), Teams integration, and any HRMS phasing decisions from the Mike conversation
- Refine `enterprise-integration-notes.md` with concrete Q1 scope and priorities

---

### Step 5: Update Platform Vision + Explore + Restructure

**Three sub-steps, done in order:**

**5-explore. Explore and refine the common vision (/think)**
- Continue `/think` session to explore what the platform vision should capture
- Key inputs: `thinking/roadmap-restructure-thinking-28jan2026.md` (feature reclassification, both-paths-have-depth realization, resource reality), `thinking/platform-vision-thinking-28jan2026.md` (current platform vision framing), `thinking/ai-coach-design-considerations.md` (AI coach design), `team-effectiveness/mvp-offer.md` (HPT MVP, Team Agreement Doc concept)
- Key realizations to integrate:
  - Both paths (LD and HPT) are full products with genuine engineering depth, not just "same engine, different framing"
  - LD goes deep into presence/integrations ("Pepe Grillo")
  - HPT goes deep into collective intelligence: team memory (Team Agreement Doc as living artifact across Katzenbach dimensions), meeting facilitation support, team conversation tracking, individual-to-team bridge
  - Reference: Chen et al. "Are We On Track?" paper — ambient visualization + interactive questioning during meetings
  - Can't do both without significant funding — shared foundation buys time to validate
  - Three validation outcomes: LD pulls, HPT pulls, or both pull (combined path)
  - Visibility is a design constraint on everything, not a separate feature track
  - Strategic filter: build things that scale what a consultant does OR augment a consultant
  - Features classified by path (LD / HPT / both) and prioritized by customer pull, not by quarter

**5a. Update Platform Vision**
- Update `thinking/platform-vision-thinking-28jan2026.md` with insights from /think exploration
- Then promote → `core/vision.md`
- Must capture: the real depth of both paths, not just "two market bets"
- Must acknowledge the resource tradeoff honestly

**5b. Behavior Change Vision**
- Current `core/vision.md` → becomes `core/vision-behavior-change.md` (or similar)
- It's the detailed product spec for the Leadership Development path
- Stays as-is, it's good — just repositioned as one product under the platform vision

**5c. Team Effectiveness MVP**
- `team-effectiveness/mvp-offer.md` serves as the current TE product description
- Not a full vision yet — it's the near-term MVP for market validation

**5d. Roadmap Restructuring**
- Restructure `core/roadmap.md` — NOT by quarter, NOT by path
- Structure: shared foundation (build now) → feature candidates organized by which path they serve (LD / HPT / both) → prioritized by customer pull
- Visibility is a design constraint, not a feature track
- Q1 commitments are firm; everything after depends on validation signals
- Input: `thinking/roadmap-restructure-thinking-28jan2026.md`

**5e. Alignment**
- `core/alignment.md` needs updating to reflect the new structure and decisions

**5f. README.md**
- Currently stale (references old files like `conscious-insights-v2-english.md`, sprint data from Jan 15)
- Rewrite to reflect: platform vision framing, document map pointing to new structure, current strategic context
- Should reference `core/vision.md` (platform), `core/vision-behavior-change.md` (LD product), `team-effectiveness/mvp-offer.md` (TE MVP), `core/roadmap.md` (engineering roadmap)
- Update team section to include Nelson and Oseas roles
- Update Active Files table to match actual document structure

---

### Downstream: Update Team Status
After all processing and restructuring is complete, update team status with new agreements and direction.

## Progress

| Step | Status |
|------|--------|
| Step 1: Nelson 1-on-1 | ✅ Done |
| Step 2: Product Strategy Office Hours | ✅ Done |
| Step 3: Mike Ruy Chat | ✅ Done |
| Step 4: Vision + Roadmap Restructuring | ✅ Done |
| Step 5: Enterprise Integration Specs | Pending (was Step 4) |
| Downstream: Team Status | Pending |
