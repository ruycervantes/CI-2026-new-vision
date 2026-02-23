# CPM Coaching Platform — Engagement Report

**Date:** February 23, 2026
**Period:** December 4, 2025 – February 23, 2026
**Prepared by:** Ruy Cervantes

---

## Executive Summary

> **58 CPM users. 4,091 messages. 141 conversations. When they engage, they go deep.**

The coaching platform has strong in-session engagement but lacks re-engagement mechanisms. Nearly everyone tried the product (93%), and when users engage, they go substantive — but most only came once (launch day). The email reminder system works perfectly when it fires (100% conversion on the 2 emails sent), but a configuration gap means it barely ran.

**The opportunity:** Fix the email trigger to unlock the retention that's already proven.

---

## The Funnel

```
58 registered → 54 tried it (93%) → 51 substantive (88%) → 12 returned on different days (21%)
```

- **93% adoption** — nearly everyone tried the product
- **88% went substantive** (4+ user turns) — the product holds attention
- **21% returned unprompted** — with no re-engagement mechanism in place

---

## Engagement Tiers

| Tier | Users | Avg Convos | Avg Deepest Convo (turns) |
|------|:-----:|:----------:|:-------------------------:|
| Never engaged (0 substantive) | 2 | 1.0 | 2.5 |
| Engaged once (1 substantive) | 40 | 1.8 | 10.4 |
| Returned (2-3 substantive) | 7 | 2.7 | 14.3 |
| Power user (4+ substantive) | 4 | 12.3 | 24.8 |

**Key:** Even single-session users averaged 10.4 turns in their deepest conversation — that's a real coaching interaction, not a quick look.

---

## Conversation Depth Distribution

| Depth Bucket | Convos | % of Total |
|-------------|:------:|:----------:|
| 0 turns (empty/bot only) | 42 | 29.8% |
| 1 turn (opened & left) | 8 | 5.7% |
| 2-3 turns (shallow) | 18 | 12.8% |
| 4-8 turns (moderate) | 30 | 21.3% |
| 9-20 turns (substantive) | 38 | 27.0% |
| 20+ turns (deep) | 5 | 3.5% |

- The 42 empty conversations are from the onboarding flow (bot sends intro, user doesn't reply). Normal.
- **Removing empties: 72% of conversations where the user actually spoke are substantive (4+ turns).**
- 5 conversations went 20+ turns — deep coaching sessions.

---

## Profile / Chatbot Breakdown

| Profile | Conversations | Messages | Avg Msgs/Convo | Unique Users |
|---------|:---:|:---:|:---:|:---:|
| Leadership Growth Partner | 77 | 2,264 | 29.4 | 44 |
| Difficult Conversations | 47 | 1,108 | 23.6 | 4 |
| Player Mindset | 17 | 719 | 42.3 | 5 |

- **Leadership Growth Partner** — the gateway profile. Broadest adoption (44 users), solid depth.
- **Player Mindset** — deepest per-session engagement (42.3 msgs avg) but only 5 users. When it clicks, it *clicks*.
- **Difficult Conversations** — concentrated usage. 4 power users generated 47 conversations. These users love this profile.

---

## Return Users

12 users came back on a different day. With no re-engagement nudges, this is organic retention.

| User | First Active | Last Active | Span | Active Days | Convos |
|------|-------------|-------------|:----:|:-----------:|:------:|
| Villabaldo Sanchez | Dec 15 | Feb 20 | 67 days | 2 | 46 |
| Joel Rodriguez | Dec 15 | Feb 19 | 66 days | 2 | 9 |
| Maria Araiza | Dec 15 | Feb 18 | 65 days | 3 | 84 |
| Marco Cano | Dec 15 | Feb 18 | 65 days | 2 | 27 |
| Rocio Tapia | Dec 15 | Feb 17 | 64 days | 2 | 58 |
| Tomas Alvarez | Dec 15 | Feb 17 | 64 days | 4 | 59 |
| Luis Salgado | Dec 15 | Jan 28 | 44 days | 4 | 44 |
| Daniel Avila | Dec 15 | Jan 26 | 42 days | 2 | 29 |
| Claudia Gamino | Dec 15 | Jan 21 | 37 days | 2 | 30 |
| Juan Fernandez | Dec 15 | Jan 21 | 37 days | 2 | 10 |
| Jose B. Sanchez | Dec 15 | Jan 4 | 20 days | 2 | 11 |
| Jennyfer Mexicano | Jan 14 | Jan 16 | 2 days | 2 | 7 |

Of these 12, **only Tomas and Rocio received email reminders.** The other 10 returned entirely on their own.

---

## Challenge Pipeline & Email Reminders

> **2 emails sent. 2 users returned. 100% conversion.**

### The Pipeline

```
58 CPM users
  → 14 created challenges (24%)
    → 22 total challenges (all opted in to reminders)
      → 12 have NO date ranges (Dec 15 batch) — never triggered emails
      → 2 have date ranges (Tomas, Rocio) — triggered emails
        → 4 micro habits created
          → 0 progress checks completed
```

### Email Evidence (Postmark — "Challenge Reminders" stream)

Only 2 emails were ever sent:

| Recipient | Date | Status |
|-----------|------|--------|
| tomas_alvarez@cpm.coop | Feb 13, 2:56 PM | Delivered |
| rocio_tapia@cpm.coop | Feb 17, 12:17 PM | Delivered |

### Did the emails work?

**Yes. Both converted immediately.**

- **Tomas**: Email Feb 13 → returned Feb 17 with a deep Difficult Conversations session (15 user messages).
- **Rocio**: Email Feb 17 → had 3 conversations that same day (16, 8, and 21 user messages across two profiles).

### The gap

The email triggers on the challenge's `start_date`. The 12 December 15 challenges were created without start/end dates (the older coaching flow didn't set them), so no emails were ever sent for those users. All 22 challenges have reminders enabled — the infrastructure is there, but the trigger data is missing.

### The implication

> If even half the remaining 12 challenge holders respond to a reminder at the same rate, that's 6 more returning users. The re-engagement infrastructure exists; it just needs the trigger data.

---

## Weekly Activity Trend

| Week | Conversations | Unique Users | User Messages |
|------|:---:|:---:|:---:|
| Dec 8 | 31 | 3 | 0 |
| Dec 15 (launch) | 63 | 49 | 512 |
| Dec 22 | 1 | 1 | 2 |
| Dec 29 | 4 | 3 | 44 |
| Jan 12 | 2 | 1 | 7 |
| Jan 19 | 4 | 3 | 25 |
| Jan 26 | 17 | 4 | 84 |
| Feb 2 | 3 | 1 | 2 |
| Feb 16 | 16 | 6 | 188 |

**Pattern:** Spike-driven, not steady-state. Dec 15 was the big launch. Jan 26 and Feb 16 look like facilitated sessions. The gap weeks show very low organic usage — reinforcing the need for automated re-engagement.

---

## What's Working

1. **Adoption is excellent** — 93% of registered users tried the product
2. **In-session engagement is strong** — 52% of conversations are substantive, avg 29 messages
3. **The product holds attention** — users who engage don't bounce after 1 message
4. **Power users emerge naturally** — 4 users became heavy adopters with no prompting
5. **Multiple profiles serve different needs** — Player Mindset deepest, Leadership broadest, Difficult Conversations most concentrated

## The Gap

1. **76% of engaged users only came once** — mostly on launch day
2. **Reminder system exists but barely fired** — only 2 of 22 challenges triggered emails
3. **Usage is spike-driven** — correlated with facilitated sessions, not organic habit
4. **Progress checks are empty** — 0 CPM users completed a progress check

## The Thesis

> **You don't have a product problem. You have a re-engagement problem — and you already have proof that fixing it works.**

---

## Recommended Next Steps

1. **Immediate: Fix the email trigger** — backfill start/end dates on the 12 dormant challenges, or run a manual Postmark campaign to all 14 challenge holders
2. **Fix the flow** — ensure all new challenges set start/end dates so emails fire automatically
3. **Investigate recurring reminders** — a `reminder_last_sent` field exists but is never populated. Is there a recurring reminder cron that's disabled?
4. **Add progress check nudges** — nobody has completed a progress check. The challenge → habit → check pipeline needs reminders at each step.
5. **Run another facilitated session** — the Feb 16 spike (6 users, 188 messages) shows these work
6. **Monitor monthly** — re-run this report to track return rate improvements

---

## Attached Data

- **`cpm-users-engagement-feb2026.csv`** — Per-user engagement data (58 users, 15 columns). Use this to cross-check against Thinkific enrollment, Postmark delivery logs, etc.
  - **GitHub only** — this file contains user PII (names, emails) and is available in the repo at `clients/cpm/cpm-users-engagement-feb2026.csv`. It is intentionally not published to Notion.
