# Sprint Planning Summary
**Date:** January 29, 2026
**Participants:** Ruy (PM/CTO), Shamil (Dev), Mike (Dev Lead), Daniel (Dev/Infra)
**Absent:** Leo (Sales)

---

## Executive Summary
Sprint planning covering three workstreams: Shamil's AI extraction work wrapping up and transitioning to Leadership Growth Partner (LGP) accountability loop improvements; Daniel's infrastructure automation script progressing well with Cloud Panel + Vulture DNS integration; Mike finishing admin panel and continuing Microsoft Teams integration. The team also discussed time tracking, Azure environment setup, StatusGator monitoring, and scheduling regular technical sync meetings.

---

## 1. Shamil: AI Extraction Task Completion
**Status:** Nearly complete, polishing today
**What was discussed:** Shamil showed extraction working yesterday, has small adjustments remaining. Will push to dev and notify via Discord.
**Decisions made:** Task marked complete.
**Action items:**
- Shamil: Push extraction to dev, notify via Discord
- Shamil: Estimated ~3 days spent (between 3-8 story points)

## 2. Time Tracking / Estimation Practice
**Status:** New process being introduced
**What was discussed:** Ruy wants the team to start estimating task time upfront and commenting on actual time spent when done, to build estimation capability. Shamil missed this from the previous sprint planning (was sick).
**Decisions made:** Team members should add a comment on tasks with estimated vs actual time.
**Action items:**
- All devs: Start estimating tasks and adding completion comments with actual time

## 3. Shamil: Leadership Growth Partner — Accountability Loop Improvement
**Status:** New task for this sprint
**What was discussed:** The current accountability partner flow is too linear: do microhabit → follow-up → check-in → done. No way to adapt the microhabit if struggling. Ruy wants to:
1. Replace the form-based check-in with a dialogue (chat-based)
2. Add coaching/adjustment capability when user is struggling
3. Enable microhabit modification (trigger, action, or both)
4. Then schedule next check-in

The rationale: people fail habits not from laziness but from not knowing how to adapt. Also, chat-based check-ins enable future Microsoft Teams integration.

**Decisions made:**
- Shamil must first experience the LGP flow as a user (do the full flow himself)
- Then understand the code: how steps work, trigger words, extraction, profiles
- Meet with Ruy tomorrow (Jan 30) for 30 min to clarify gaps
- New step to be built between "practice design" and "follow-up"

**Action items:**
- Shamil: Complete full LGP user flow today/tomorrow
- Shamil: Study code — step prompts, trigger words, extraction mechanism, step succession
- Ruy: Schedule 30-min check-in with Shamil for Jan 30
- Ruy: Flesh out prompt/dialogue design for the new check-in step (not built yet)

## 4. Daniel: Infrastructure Automation Script
**Status:** In progress, good momentum
**What was discussed:** Daniel demonstrated live:
- Vulture API integration working — can create subdomains programmatically (tested with "deploy-test-2")
- Cloud Panel integration in progress (API key issue — Cloud Panel doesn't have one, working around it)
- Created a new repo for infrastructure automation (separate from app repos)
- Script is step-based and modular: Cloud Panel site → database → DB permissions → DNS → etc.
- Scientific packages and Postmark will be optional/skipped for now

**Decisions made:**
- Postmark setup is optional (use default message stream; token stays the same)
- Admin app installation is optional (instances sharing DB don't need duplicate admins)
- Scientific packages skipped for now
- New separate repo created for infrastructure automation

**Action items:**
- Daniel: Continue infrastructure script, target 50-75% completion this sprint
- Daniel: Make admin installation optional in script
- Mike: Provide Postmark token/data if Daniel can't find in 1Password

## 5. Daniel: StatusGator Monitoring Setup
**Status:** Quick task, doing today
**What was discussed:** Which instances to monitor on StatusGator.
**Decisions made:** Monitor: testing, demo, and all client instances. Dev is optional (Mike is on it daily). Not personal dev instances.
**Action items:**
- Daniel: Add testing, demo, and client instances to StatusGator today

## 6. Daniel: Opt-in Robot
**Status:** Quick task
**What was discussed:** Will add as another optional step in the infrastructure automation script, testing with real sites.
**Action items:**
- Daniel: Add opt-in robot as step in automation script

## 7. Mike: Admin Panel
**Status:** Complete
**What was discussed:** Mike confirmed admin panel work is done (from sprint demo).
**Decisions made:** Marked as done.
**Actual time:** ~2-3 days (mixed with other work, hard to isolate)

## 8. Mike: Microsoft Teams Integration
**Status:** In progress, main focus this sprint
**What was discussed:** Mike spent ~4-5 days last sprint on Teams. Initial estimate was 13 points (~2 weeks), updated to 21 points. Testing will be a separate task once Azure environment is available.
**Decisions made:**
- Update estimate to 21 story points
- Testing/staging on Azure will be a separate task
**Action items:**
- Mike: Continue Teams integration development

## 9. Azure Environment Setup
**Status:** Deferred to second week of February
**What was discussed:** Need Azure tenant for Teams testing. Daniel can set it up (DNS entries, payment, manifests, new users) — estimated 3-4 hours. Requires Stoic credit card + finance authorization code before 2pm Mexico time.
**Decisions made:** Not urgent for this sprint. Mike can continue with local fake Teams environment. Possibly delegate to support team instead of Daniel.
**Action items:**
- Ruy: Check if support team can handle Azure setup instead of Daniel
- Ruy: Get Stoic credit card authorization when ready
- Daniel/Ruy: Schedule Azure setup for ~second week of February

## 10. Daniel: Infrastructure Checklist
**Status:** Deferred
**What was discussed:** Daniel had a task to create housekeeping checklist for infrastructure. Won't work on it this sprint — focusing on automation script.
**Decisions made:** Deferred, focus on one thing.

## 11. Mike: Update Script Idea
**Status:** Idea stage
**What was discussed:** Mike suggested adding an "update all instances" capability to the infrastructure automation script.
**Action items:**
- Daniel: Consider adding update capability as future step

## 12. Technical Sync Meetings
**Status:** Needs scheduling
**What was discussed:** Shamil raised the lack of technical discussion meetings — current meetings are either non-technical (office hours) or process (sprint planning, retro). Need a space for pair programming, technical problem-solving (e.g., flashing sidebar, websockets).
**Decisions made:**
- Shamil and Mike will schedule a recurring weekly 1-hour technical sync
- Shamil prefers a fixed calendar slot
- Could be during Gather hours or at a separate time
- Ruy will check with Leo about freeing up office hour slots

**Action items:**
- Shamil: Propose a recurring time to Mike for weekly technical sync
- Ruy: Talk to Leo about reserving lighter office hour days for technical work

---

## Key Decisions Made

| Decision | Details |
|----------|---------|
| Estimation practice | Team to estimate upfront, comment actual time on completion |
| LGP accountability loop | Replace form check-in with dialogue, add coaching/adapt capability |
| Infrastructure automation | Separate repo, modular step-based approach |
| Postmark | Optional, use defaults |
| Admin app | Optional in install script |
| StatusGator | Monitor testing, demo, client instances |
| Azure setup | Deferred to ~Feb second week, possibly delegate to support |
| Teams estimate | Updated from 13 to 21 points |
| Technical syncs | Shamil + Mike weekly recurring meeting |

---

## Blockers Identified

| Blocker | Owner | Resolution |
|---------|-------|------------|
| Cloud Panel lacks API key | Daniel | Working around it, adjusting script |
| Azure environment for Teams testing | Ruy/Daniel | Deferred; local testing for now |
| No technical meeting slot | Shamil/Mike | Schedule recurring 1:1 |
| LGP check-in prompt not designed yet | Ruy | Will design before Shamil implements |

---

## Next Steps

1. Shamil: Push extraction to dev today, then start LGP user flow experience
2. Shamil + Ruy: Meet Jan 30 to discuss LGP accountability loop implementation
3. Daniel: Continue infrastructure automation, add StatusGator monitoring today
4. Mike: Continue Teams integration
5. Ruy: Check with support team about Azure setup
6. Ruy: Talk to Leo about office hour scheduling
7. Shamil: Propose technical sync time to Mike
8. Ruy: Send vision/roadmap docs to Shamil and Daniel
