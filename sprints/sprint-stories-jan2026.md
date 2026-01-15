# Sprint Stories - January 2026

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
