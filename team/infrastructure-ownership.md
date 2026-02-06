# Stoic Infrastructure Reference

**Last updated:** February 5, 2026
**Owner:** Ruy (ruy@stoicenterprises... TBD after migration)
**Published to:** [Notion — "Infrastructure Ownership Reference"](https://www.notion.so/axialent/) under "Operations / IT" section in "Stoic New Vision, Roadmap and Docs 2026". Share this Notion page with TecnoBrain (Mario).
**Sync:** `python3 scripts/notion-sync.py --file team/infrastructure-ownership.md`

This document is the single reference for how Stoic's infrastructure is organized, who manages what, and who to contact. If you're new to Stoic's IT or taking over from someone, start here.

---

## 1. Our Domains

| Domain | Purpose | Status |
|--------|---------|--------|
| **stoicyou.com** | Primary domain. Website, application, email. | Active — primary |
| **stoic.enterprises** | Legacy domain. Email accounts, Microsoft 365. | Active — being phased out. Migrating to stoicyou.com. |
| **boetus.com** | Test/staging domain for development. | Setting up Microsoft 365 test tenant (Feb 2026) |

**Direction:** Everything consolidates under **stoicyou.com**. stoic.enterprises will be retired once all accounts are migrated.

---

## 2. Infrastructure Map

### stoicyou.com

| Service | Provider | Admin | Contact | Notes |
|---------|----------|-------|---------|-------|
| **DNS** | Vultr | Daniel Alvarado | ai.app@axialent.com | Routes all subdomains. Changes can be made in hours. |
| **Web hosting** (www) | SiteGround | Yonatan / Sam | Via Yonatan | Website lives here. Sam is India-based contractor. |
| **Email** (to be set up) | Microsoft 365 | TecnoBrain (pending) | Mario / Jorge | MX records point to M365. Mailboxes being created. |
| **Application** | Vultr | Daniel Alvarado / Mike | ai.app@axialent.com | The Stoic/CI product platform. |

**Key point:** DNS and hosting are **separate systems**. DNS (Vultr) is just a routing table that says "send email to Microsoft, send web traffic to SiteGround, send app traffic to Vultr." Daniel manages the routing table. The actual services are managed by their respective admins.

### stoic.enterprises

| Service | Provider | Admin | Contact | Notes |
|---------|----------|-------|---------|-------|
| **Email + accounts** | Microsoft 365 | TecnoBrain | Mario / Jorge | ~4 active licenses |
| **help@ mailbox** | Microsoft 365 | Nelson Granja | nelson.granja@axialent.com | Tied to Thinkific LMS. Cannot be removed until Nelson transitions it. |

### boetus.com (test environment)

| Service | Provider | Admin | Contact | Notes |
|---------|----------|-------|---------|-------|
| **Microsoft 365 tenant** | Microsoft 365 | TecnoBrain (setup) / Daniel + Mike (usage) | Mario / Jorge | Separate tenant for Teams integration testing. Full admin for dev team. |

---

## 3. Contact Directory

**For infrastructure questions, contact in this order:**

| Person | Role | Reach via | Responsible for |
|--------|------|-----------|-----------------|
| **Ruy** | PM/CTO | Teams / email | Overall architecture decisions, escalations |
| **Daniel Alvarado** | Dev (infra) | ai.app@axialent.com / Teams | DNS (Vultr), application servers, deployment |
| **Mike** | Dev lead | Teams (Spain timezone) | DNS backup, application architecture, Teams integration |
| **Mario** | IT liaison (TecnoBrain) | Email | Microsoft 365 administration, TecnoBrain coordination |
| **Jorge** | IT ops (TecnoBrain) | Email | Microsoft 365 execution, tenant setup, licenses |
| **Oriana** | IT ops (TecnoBrain) | Email | Covering for Javier (back ~mid-Feb 2026) |
| **Nelson Granja** | Sales/LMS | nelson.granja@axialent.com | help@stoic.enterprises, Thinkific platform |
| **Yonatan** | Business ops | Email | SiteGround hosting access (via Sam), business email requirements |
| **Sam** | Contractor (India) | Via Yonatan | SiteGround hosting console |

---

## 4. "Who Do I Call When...?"

| Situation | Contact | Why |
|-----------|---------|-----|
| Need a DNS change (new subdomain, MX record, etc.) | Daniel Alvarado | He manages Vultr DNS |
| Website issue on stoicyou.com | Yonatan → Sam | SiteGround hosting |
| Email account on stoicyou.com | TecnoBrain (Jorge) | Microsoft 365 |
| Email account on stoic.enterprises | TecnoBrain (Jorge) | Microsoft 365 |
| help@stoic.enterprises issue | Nelson Granja first, then TecnoBrain | Nelson owns the business use |
| Application / platform issue | Daniel or Mike | Vultr infrastructure |
| Test environment (boetus.com) | Daniel / Mike (usage), TecnoBrain (admin) | Separate tenant |
| New Microsoft license or tenant change | TecnoBrain (Mario for approval, Jorge for execution) | Microsoft 365 admin |
| Billing / entity questions | Agustin Carrizo | Finance authority |

---

## 5. Current State & Known Issues (as of Feb 5, 2026)

### Active Issues

| Issue | Status | Owner | Details |
|-------|--------|-------|---------|
| **info@stoicyou.com not working** | URGENT — pending since Jan 14 | TecnoBrain (Jorge) | MX records point to M365, but mailboxes were created in SiteGround. Need to create in M365 instead. |
| **contact@ distribution group not delivering** | URGENT | TecnoBrain (Jorge) | Same root cause as info@. Group should deliver to 4 people. |
| **stoic.enterprises → stoicyou.com migration** | Planning | Ruy + TecnoBrain | Need inventory of all active accounts first. help@ requires Nelson coordination. |
| **boetus.com test tenant setup** | In progress | TecnoBrain (Jorge) | Pricing confirmed (~$12.50-15/mo per license). Awaiting Agustin approval. |

### Recently Resolved

| Issue | Resolution | Date |
|-------|-----------|------|
| (none yet) | | |

---

## 6. Access Notes

| System | How to get access |
|--------|-------------------|
| **Vultr (DNS)** | Contact Daniel Alvarado. He and Mike have admin. |
| **SiteGround (hosting)** | Contact Yonatan. Sam (India) has console access. |
| **Microsoft 365 (stoic.enterprises)** | TecnoBrain manages. Contact Mario/Jorge. |
| **Microsoft 365 (stoicyou.com email)** | TecnoBrain setting up. Contact Mario/Jorge. |
| **Microsoft 365 (boetus.com test)** | TecnoBrain setting up. Daniel + Mike will have full admin. |
| **Application platform** | Contact Daniel or Mike. |

---

## 7. Important Context

- **TecnoBrain** is the external IT partner managing Microsoft 365 tenants. They do NOT have access to DNS (Vultr) or web hosting (SiteGround).
- **Daniel's baby leave** is expected around Feb 16, 2026. Mike is backup for DNS and infrastructure during that period.
- **Javier** (TecnoBrain, primary IT contact) is on vacation until ~mid-Feb. Jorge and Oriana are covering.
- **strausscomms.com** — This domain is NOT ours. If requests come in related to it, redirect to Yonatan for clarification.

---

*This document should be updated when: infrastructure changes, people change roles, new services are added, or issues are resolved. If you're reading this and something is wrong, tell Ruy.*
