# ConsciousInsights Repository Organization Strategy

**Created:** February 6, 2026
**For discussion with:** Mike
**Author:** Ruy Cervantes

---

## Executive Summary

Today I reorganized the ConsciousInsights documentation and repository structure with PAI. This document captures what was done, the current state, and recommendations for discussion.

**Key outcomes:**
- Created dedicated `compliance` repo for security/compliance docs
- Archived 6 legacy repos from 2024
- Identified a proposed 5-core-repo model for going forward

---

## What Was Done Today

### 1. Compliance Repo Created
**New repo:** [stoicenteprises/compliance](https://github.com/stoicenteprises/compliance)

Migrated from the old `conscious-insights-documentation` repo:
- `policies/` — Canonical security and privacy policies (updated Feb 2026 for P&G SIG)
- `clients/` — Client-specific assessment packages (PG, Credicorp, Aleatica, telus)
- `AI_compliance/` — EU AI Act compliance materials

### 2. Legacy Repo Archived and Renamed
- `conscious-insights-documentation` → renamed to `ci-docs-archive` and archived
- Contains old PRDs from 2024-2025, now superseded by this repo

### 3. Five 2024 Repos Archived
| Repo | Why Archived |
|------|--------------|
| `cb-assessment-2024` | One-time 2024 project |
| `AI_eng_translations` | Completed translations |
| `docs` | Superseded by knowledgebase2026 |
| `CB-knowledge-base` | Superseded by knowledgebase2026 |
| `boetus-app` | Abandoned project |

---

## Current Repository Landscape

### stoicenteprises (Organization)

#### Active Repos (14)

| Repo | Last Active | Purpose | Recommendation |
|------|-------------|---------|----------------|
| `conscious-insights` | Feb 6, 2026 | **Main application** | ✅ Keep (core) |
| `compliance` | Feb 6, 2026 | **Security/compliance docs** | ✅ Keep (core) |
| `knowledgebase2026` | Feb 4, 2026 | **Public knowledge base** | ✅ Keep (core) |
| `ci-instance-provisioning` | Feb 2, 2026 | **Infrastructure/DevOps** | ✅ Keep (core) |
| `claude-config` | Jan 21, 2026 | Claude Code workflows | ✅ Keep (utility) |
| `analytics-app` | Nov 25, 2025 | Analytics dashboard | ⚠️ Review — still used? |
| `ci-api-client` | Nov 13, 2025 | API client library | ⚠️ Review — still used? |
| `dashboard-repo` | Nov 6, 2025 | Dashboard testing | ⚠️ Review — merge or archive? |
| `dashboard-repo_nelson` | Nov 6, 2025 | Dashboard testing (Nelson) | ⚠️ Review — merge or archive? |
| `analytics` | Nov 3, 2025 | Shared analytics | ⚠️ Review — merge into analytics-app? |
| `sysops-tools` | Oct 30, 2025 | Sysops utilities | ⚠️ Review — still used? |
| `ci-next` | Jul 31, 2025 | Old prototype | 🗑️ Recommend archive |
| `analytics-research` | Jul 18, 2025 | Research code | ⚠️ Review — merge or archive? |
| `prompt-library` | Jan 29, 2025 | Prompts archive | ⚠️ Review — merge into main app? |
| `conscious-insights-backend` | Jan 20, 2025 | Admin panel | ⚠️ Review — still used? |

#### Archived Repos (6)

| Repo | Archived Date | Reason |
|------|---------------|--------|
| `ci-docs-archive` | Feb 6, 2026 | Superseded by compliance + knowledgebase2026 |
| `boetus-app` | Feb 6, 2026 | Abandoned project |
| `CB-knowledge-base` | Feb 6, 2026 | Superseded by knowledgebase2026 |
| `docs` | Feb 6, 2026 | Superseded by knowledgebase2026 |
| `AI_eng_translations` | Feb 6, 2026 | Completed project |
| `cb-assessment-2024` | Feb 6, 2026 | Completed project |

### ruycervantes (Personal)

| Repo | Last Active | Purpose | Recommendation |
|------|-------------|---------|----------------|
| `CI-2026-new-vision` | Feb 4, 2026 | **Working space** (this repo) | ✅ Keep (personal workspace) |
| `conscious-insights-documentation` | May 2025 | Old fork | 🗑️ Archive or delete |
| `stoic-flowise` | Jun 2024 | Old Flowise experiment | 🗑️ Archive or delete |

---

## Proposed 5-Core-Repo Model

| Repo | Owner | Purpose | Audience |
|------|-------|---------|----------|
| **conscious-insights** | stoicenteprises | Main application code | Developers |
| **compliance** | stoicenteprises | Security policies, client assessments | Auditors, enterprise clients |
| **knowledgebase2026** | stoicenteprises | Public knowledge base (vision, pitch, research) | Prospects, public |
| **ci-instance-provisioning** | stoicenteprises | Infrastructure/DevOps | DevOps |
| **CI-2026-new-vision** | ruycervantes | Ruy's working space (action items, drafts) | Internal only |

Everything else either:
- Merges into one of the core repos
- Gets archived
- Is a utility repo (like `claude-config`)

---

## Open Questions for Discussion

### 1. Analytics Repos
We have 4 analytics-related repos:
- `analytics-app`
- `analytics`
- `analytics-research`
- `dashboard-repo` / `dashboard-repo_nelson`

**Question:** Should these be consolidated? What's actually being used?

### 2. Backend/Admin
- `conscious-insights-backend` — Is the admin panel still separate from main app?
- `ci-api-client` — Is this library still used?

### 3. Notion Sync
- Should compliance docs live in Notion and sync to GitHub?
- Or is GitHub the source of truth?

### 4. Public vs. Private
- What should be in `knowledgebase2026` (public)?
- What stays private?

### 5. Team Access
- Who needs access to which repos?
- Should we create GitHub teams?

---

## Recommended Next Steps

1. **Immediate:** Review the "⚠️ Review" repos in the table above
2. **Short-term:** Archive `ci-next` and other clearly obsolete repos
3. **Medium-term:** Consolidate analytics repos if appropriate
4. **Ongoing:** Create a repo map in `knowledgebase2026` for discoverability

---

## Links

- [stoicenteprises/compliance](https://github.com/stoicenteprises/compliance) — New compliance repo
- [stoicenteprises/conscious-insights](https://github.com/stoicenteprises/conscious-insights) — Main app
- [stoicenteprises/knowledgebase2026](https://github.com/stoicenteprises/knowledgebase2026) — Public KB
- [stoicenteprises repos](https://github.com/orgs/stoicenteprises/repositories) — Full org view
