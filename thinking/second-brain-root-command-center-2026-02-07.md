# Thinking: Root Command Center + Second Brain Organization

**Date:** 2026-02-07
**Status:** Exploring — architecture crystallizing

---

## The Problem

Ruy has four organizational systems that partially overlap but don't talk to each other:
- **Google Drive** (personal files, PARA-numbered folders: 00 inbox, 01 Projects, 02 Areas, 04 Archive)
- **OneDrive** (work files, also PARA-numbered but with significant drift — loose files alongside structure)
- **Todoist** (daily/weekly execution, cleanest Personal/Work split)
- **GitHub repos** (where thinking, planning, and processing actually happen — CI-2026 being the most mature)

**The real issue isn't folder organization — it's attention allocation.** Things that have a processing system (CI work) get attention. Things that don't (crypto, real estate, health) get neglected. Not because they don't matter, but because they're invisible in any processing pipeline.

---

## Key Insight: Telos as the Spine

Telos (`~/.claude/skills/PAI/USER/TELOS/`) already has the structure for whole-life coverage:
- Missions, Goals, Challenges, Strategies (well-populated for work)
- STATUS.md has Life Area sections: Work/Career, Health, Relationships, Financial, Personal Growth, Creative/Projects (all empty templates)
- PROJECTS.md is exclusively CI/work projects

**Telos was designed for whole-life but became work-only in practice.** This mirrors the exact pattern: work gets the system, personal gets dropped.

Telos lives in PAI (available across all repos). It doesn't need to move — it's already "above" any single repo.

### The Telos Role (Nuance)

Telos is NOT an authority telling Ruy what to do. It's **his own voice from a clearer moment, reflected back when he's in the weeds.** The feedback loop:

```
Reflective Ruy → writes Telos (what matters, why, strategies)
        |
Daily Ruy → sees Telos reflected in triage/weekly plans
        |
Reality → things change, priorities shift
        |
Reflective Ruy → updates Telos based on what actually happened
```

The system's job: keep this loop spinning.

---

## Emerging Architecture

```
Telos (in PAI — the "why" layer)
├── Mission, Goals, Challenges, Strategies
├── Life Area Status (work, health, financial, personal growth, etc.)
├── Available across ALL repos via PAI
│
Root Command Center (NEW repo — the "what now" layer)
├── action-items-ruy-{month}.md (UNIFIED — work + personal)
├── thinking/ (cross-domain thinking sessions)
├── weekly plans, triage
├── CLAUDE.md (teaches Claude about Ruy's whole life, not just CI)
├── Domain folders or links:
│   ├── work/ → links to CI-2026-new-vision
│   ├── real-estate/ (tracking, decisions, action items)
│   ├── crypto-finances/ (portfolio tracking, strategy)
│   ├── health/ (fitness, medical, habits)
│   └── personal-projects/ (whatever else)
│
Domain Repos (the "how" layer)
├── CI-2026-new-vision (work — already exists, keeps team context)
├── Other repos as needed
│
Cloud Drives (file storage — PARA stays)
├── Google Drive (personal files, sheets, slides)
├── OneDrive (work files, Excel, PowerPoint)
│
Todoist (daily execution — downstream from triage)
├── Labels: @this-week, @next-week, @deep-work, etc.
├── Personal + Work projects
```

---

## Decisions Made

1. **Google Drive / OneDrive split stays** — work vs personal. PARA structure maintained. These are file storage, not processing systems.
2. **One processing system, not two** — Ruy works at one desk, interleaves personal and work throughout the day. Separate systems = things fall through cracks.
3. **New root repo (not expanding CI-2026)** — CI-2026 is already heavy with team context. Personal life shouldn't pile on top.
4. **Telos stays in PAI** — it's already available across repos. It's the connective tissue.
5. **Telos needs to be populated for personal domains** — Goals, Projects, Status sections for real estate, crypto, health, etc.

---

## Open Questions

1. **What does the root command center CLAUDE.md look like?** It needs to teach Claude about Ruy's whole life — routing to CI-2026 for work detail, to Telos for life alignment, to domain folders for personal projects.

2. **How do `/today` and `/weekly-plan` change?** Currently they're CI-focused. In the root repo, they'd need to pull from both CI and personal action items, and cross-reference Telos.

3. **How heavy do personal domain folders get?** Real estate might just need a few tracking docs. Crypto might need more. Health might be lightweight. Need to discover this through use.

4. **Should action items be one file or per-domain?** One unified file means one triage surface. Per-domain files mean cleaner separation but multiple places to check.

5. **Does CI-2026 keep its own action items file?** Or does everything move to root? Probably keep CI's for team/sprint context, but personal triage happens at root level.

6. **What's the migration path?** Don't build the whole system at once (C2 pattern!). What's the minimum viable first step?

---

## Next Steps (when ready to build)

1. Populate Telos personal domains (Goals, Projects, Status for real estate, crypto, health)
2. Create the root command center repo with minimal structure
3. Move/copy personal action items from CI-2026 to root
4. Write the root CLAUDE.md
5. Adapt `/today` and `/weekly-plan` to work from root

---

*This is a thinking file. Not a plan. Decisions still open.*
