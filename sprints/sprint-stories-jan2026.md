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

**Notes:** FRD at `sprints/daily-companion-cyclic-flow-frd.md`. Shamil exploring system Wed-Thu, check-in Fri Jan 31.

---

### Daniel: Installation Script Completion

Finish installation script automation (port tracking, pip isolation resolved).

**Points:** TBD

**Acceptance Criteria:**
- [ ] Script handles port tracking (text file in system directory)
- [ ] Uses pip in production (not UV) for security isolation
- [ ] Creates client environments on demand
- [ ] Documentation updated

**Dependency:** No P&G firefighting

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

### Mike: MS Teams Notifications → Production Deployment

Continue Teams development, prepare for production deployment.

**Points:** TBD

**Acceptance Criteria:**
- [ ] Local dev environment stable
- [ ] Production deployment requirements documented (Azure instance, manifest updates)
- [ ] Axialent Teams admin access requested (via Mario) when ready

**Dependency:** Daniel support for deployment (last 15 days Q1)

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
