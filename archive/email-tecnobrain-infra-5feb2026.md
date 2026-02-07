Subject: Follow-up: StoicYou.com infrastructure — 3 requests from today's call

TO: Mario
CC: Jorge, Oriana, Daniel Alvarado, Nelson Granja, Yonatan

---

Hi Mario,

*Quick note for those in CC: Yonatan — you're here because TecnoBrain has been coming to you with questions about the domain/email setup. This email lays out the full picture so they have the context they need. Section 1 is also your pending email request, flagged as urgent. Daniel — you're here in case TecnoBrain has questions about DNS or the test environment setup. Nelson — section 2 involves the help@stoic.enterprises transition and we'll need your input. Jorge and Oriana — you'll be executing on these requests.*

Following up on our call today with Jorge and Oriana. Below is a recap of the three requests we discussed, organized by priority. I'm including an infrastructure reference map at the end for clarity.

---

**1. URGENT — StoicYou.com Email Setup (Yonatan's pending requests)**

Yonatan has been requesting email accounts under stoicyou.com since January 14. The core issue: MX records point to Microsoft 365, but the mailboxes were created in SiteGround — so nothing delivers.

**What's needed:**
- Confirm with Yonatan the full list of email accounts he needs (we know of at least: info@stoicyou.com and a "contact" distribution group for 4 people)
- Recommended path: create these mailboxes in Microsoft 365 (not SiteGround) so they align with where DNS is routing. If it's only 2-3 accounts, this should be straightforward.
- If more accounts are needed, let's evaluate whether to consolidate all stoicyou.com email in Microsoft or adjust DNS to route to SiteGround instead.

**Please prioritize this — it's been over 3 weeks.**

---

**2. IMPORTANT — Stoic Enterprises → StoicYou.com Transition Plan**

We need to consolidate from two domains to one. Stoic Enterprises (stoic.enterprises) has a few active Microsoft 365 accounts that need to migrate to stoicyou.com over time.

**What's needed:**
- Oriana to share the full inventory of active stoic.enterprises email accounts and licenses
- Nelson (CC'd): help@stoic.enterprises is currently in use and tied to our LMS platform. Nelson, when you have a moment, I'd like to coordinate on what you need for a transition plan — timeline, forwarding, etc.
- Once we have the full picture, we'll create a migration plan

**This is not urgent but it is important.** Let's get the inventory first and plan from there.

---

**3. NEW REQUEST — Microsoft 365 Test Environment (boetus.com)**

Our development team needs an isolated Microsoft 365 environment for Teams integration testing. We've been using Axialent's environment with limited access, and it's too slow for our development pace.

**What's needed:**
- **New, separate Microsoft 365 tenant** (not added to existing tenants — security isolation)
- **Domain:** boetus.com (our existing test domain)
- **Licenses:** 2x Business Standard ($12.50/mo annual or $15/mo monthly)
- **Accounts:** test1@boetus.com, test2@boetus.com
- **Admin access:** Full administrator for Daniel Alvarado and Mike (our dev leads)
- **TecnoBrain access:** Internal .onmicrosoft.com account (no extra license needed)
- **Billing entity:** Stoic, Spain. Please confirm pricing options (annual vs monthly) and we'll validate with Agustín Carrizo which card/entity to use.

Jorge — could you send over the pricing comparison when you have it?

---

**Infrastructure Reference Map**

For everyone's reference, here's who manages what:

| Domain | Service | Provider | Admin |
|--------|---------|----------|-------|
| stoicyou.com | DNS | Vultr | Daniel Alvarado (ai.app@axialent.com) |
| stoicyou.com | Web hosting (www) | SiteGround | Yonatan / Sam |
| stoicyou.com | Email (to be set up) | Microsoft 365 | TecnoBrain (pending) |
| stoic.enterprises | Email + accounts | Microsoft 365 | TecnoBrain |
| stoic.enterprises | help@ mailbox | Microsoft 365 | Nelson Granja (Axialent) |
| boetus.com | Test environment | Microsoft 365 (new) | TecnoBrain (to set up) |

**Also:** Jorge — there was a request about a blocked mailbox at joel@strausscomms.com. This domain is not ours and we have no context on it. Please clarify directly with Yonatan what this is and whether it's something TecnoBrain needs to handle separately.

---

Thanks everyone. Happy to jump on another call if anything needs clarification.

Ruy
