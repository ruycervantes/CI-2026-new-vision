# Sprint Stories - January 2026

---

## Sprint 3

Sprint Planning: Thursday, January 30

---

### Shamil: Daily Companion Cyclic Flow

Loop instead of end after check-in. User can continue, modify habit, or go to Coach.

**Points:** TBD

**Requirements:**
- After check-in, present options: Continue / Modify habit / Go to Coach
- "Modify habit" allows adjustment without starting over
- "Go to Coach" hands off conversation to Coach mode

**Acceptance Criteria:**
- [ ] User completes check-in and sees options (not just end)
- [ ] "Continue" loops back to next cycle
- [ ] "Modify habit" allows user to adjust their habit
- [ ] "Go to Coach" transitions to Coach mode
- [ ] Flow documented

**Pre-work (from Sprint Planning Jan 29):**
- [ ] Experience the full LGP accountability partner flow as a user (before Jan 30 check-in)
- [ ] Study code: step prompts, trigger words, extraction mechanism, step succession
- [ ] Propose recurring weekly technical sync time to Mike

**Notes:** FRD at `sprints/daily-companion-cyclic-flow-frd.md`. Check-in with Ruy Jan 30 to clarify gaps. Prompt/spec for new check-in dialogue pending from Ruy.

---

### Daniel: Infrastructure Automation Script

Modular, step-based infrastructure provisioning script (separate repo from app). Evolved from install script into a broader automation platform that handles full environment creation.

**Points:** TBD (target 50-75% completion this sprint)

**Progress (from Sprint Planning Jan 29):**
- Vulture API integration working (subdomain creation tested)
- Cloud Panel integration in progress (no API key — working around it)
- Step-based architecture: each step runs isolated and can be tested independently

**Steps:**
1. Cloud Panel site creation
2. Database creation
3. Database permissions
4. DNS entry (via Vulture API)
5. Admin app installation (optional — instances sharing DB don't need it)
6. Postmark setup (optional — use default message stream)
7. Scientific packages (skipped for now)
8. StatusGator monitoring entry
9. Opt-in robot configuration

**Acceptance Criteria:**
- [ ] Cloud Panel site creation automated
- [ ] Database + permissions automated
- [ ] DNS via Vulture API automated
- [ ] Admin app installation as optional step
- [ ] Postmark as optional step with defaults
- [ ] Script runs end-to-end for a new client environment
- [ ] Documentation updated

**Also this sprint:**
- [ ] Add testing, demo, and client instances to StatusGator (quick, today Jan 29)
- [ ] Opt-in robot as optional step in automation script

**Dependency:** No P&G firefighting. Baby leave ~Feb 16 — script must be documented/transferable before then.

---

### Daniel: WorkOS SSO POC (Boetus)

Create POC using Boetus.com Microsoft tenant for SSO + provisioning testing.

**Points:** TBD

**Requirements:**
- Configure WorkOS to handle Boetus.com authentication
- Route users to either Thinkific or Conscious Insights based on role
- Test provisioning flow

**Acceptance Criteria:**
- [ ] WorkOS configured for Boetus.com Microsoft tenant
- [ ] SSO login works (user signs in via Microsoft → lands in app)
- [ ] Basic provisioning tested
- [ ] Architecture documented (routing middleware for multi-tenant)

**Dependency:** Installation script completed first. Daniel available (~1 month govt leave, baby due Feb 5).

---

### Mike: MS Teams Integration — Development

Continue Teams integration development (local environment).

**Points:** 21 (updated from 13, Sprint Planning Jan 29)

**Acceptance Criteria:**
- [ ] Local dev environment stable
- [ ] Core Teams integration feature complete
- [ ] Production deployment requirements documented (Azure instance, manifest updates)

**Notes:** Mike spent ~4-5 days last sprint. Acknowledged estimates are optimistic. Admin panel marked done.

---

### Mike: MS Teams Integration — Staging & Testing on Azure

Deploy and test Teams integration on Azure environment. Separate task from development.

**Points:** TBD

**Acceptance Criteria:**
- [ ] Azure environment provisioned (Ruy checking if support team can set up)
- [ ] Teams integration deployed to Azure staging
- [ ] End-to-end testing on real Azure/Teams environment
- [ ] Axialent Teams admin access requested (via Mario) when ready

**Dependency:** Azure environment setup (deferred to ~second week of Feb). Development task above. Daniel support for deployment.

---

### Leo: Demo + Voice vs Bidirectional Validation

Demo tomorrow (Tue Jan 28). Continue customer conversations to validate Voice vs Bidirectional priority.

**Points:** TBD

**Acceptance Criteria:**
- [ ] Demo delivered
- [ ] Customer feedback captured on Voice vs Bidirectional preference
- [ ] Decision input for Q1 roadmap

---

---

## Sprint 2

Sprint Planning: Thursday, January 16

---

## Dev Team

### Shamil: Thinking Partner - Extract Goal/Gap
Extract user's goal and gap from Thinking Partner conversation. Store in DB, display in UI, and make available for future conversations. Implementation exists in dev branch.

**Acceptance Criteria:**
- [ ] Identifies Destination Goal from conversation
- [ ] Identifies the Gap (current vs desired state)
- [ ] Records how the gap was proposed to close (action plan)
- [ ] Records user's commitment
- [ ] All data saved to DB and available for future conversations
- [ ] Data displayed in UI

---

### Daniel: Deployment Script - Environment Creation Automation
Automate the creation of new environments. Each client needs their own environment (e.g., telus.stoyq.com), and we need custom environments for experimental branches (e.g., experimentalbranch.stoyq.com).

**Requirements:**
- Create client-specific environments (client.stoyq.com)
- Create custom environments for experimental branches (branchname.stoyq.com)
- Pull specified branch from Git and deploy to the environment
- Support both Docker containers and plain installation

**Acceptance Criteria:**
- [ ] Script creates new client environments on demand (e.g., telus.stoyq.com)
- [ ] Script creates custom environments for any Git branch (e.g., experimentalbranch.stoyq.com)
- [ ] Pulls correct branch from Git and deploys automatically
- [ ] Supports Docker container deployment
- [ ] Supports plain installation deployment
- [ ] Documentation for how to use the script

---

### Leo: Testing → Demo Approval Process
Formalize the existing informal flow from feature testing to demo approval. Test the Leadership Growth Partner flow end-to-end.

**Flow:** ci.dev.boetus.com → staging → demo.stoicyou.com → production

**Dependency:** Mike deploys Leadership Growth Partner from dev to staging first.

**Acceptance Criteria:**
- [ ] Mike deploys latest to staging (Leadership Growth Partner flow)
- [ ] Leo tests in staging
- [ ] Process documented: dev → staging → demo → production
- [ ] Bug submission process defined (how to report issues found)
- [ ] Cleanup process defined (how to resolve bugs before promotion)
- [ ] Clear criteria for "demo ready"
- [ ] Signs off before features go to demo.stoicyou.com
- [ ] Ready for client demos and customer shipping

---

## Mike

### Mike: MS Teams Notifications
Continue MS Teams notifications work.

**Status:** In progress

---

### Mike: Deploy Leadership Growth Partner to Staging
Move Leadership Growth Partner flow from dev to staging.

**Flow:** ci.dev.boetus.com → staging → demo.stoicyou.com

**Acceptance Criteria:**
- [ ] Leadership Growth Partner flow deployed from dev to staging
- [ ] Ready for Leo to test

**Blocks:** Leo's Testing → Demo Approval Process

---
