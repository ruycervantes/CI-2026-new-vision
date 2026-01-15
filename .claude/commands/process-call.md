# /process-call - Deep analysis of meeting transcripts

Processes call transcripts into structured summaries, strategic analysis, and action items. Designed to capture not just what was said, but the deeper implications and finer points.

## Instructions

### Step 1: Locate and read the transcript

1. Check `calls/` folder for unprocessed transcripts (`.txt` files without corresponding `-Summary.md`)
2. If user specifies a file, use that instead
3. Read the full transcript - these are often messy with:
   - Speaker labels that may be inconsistent
   - Echo/duplication from transcription
   - Mixed Spanish/English
   - Interruptions and crosstalk

### Step 2: Identify participants and context

- Who was on the call? (Match speakers to team members: Ruy, Mike, Daniel, Leo, Shamil, etc.)
- What type of meeting? (Sprint planning, 1:1, strategy, demo review, etc.)
- What was the stated agenda vs what was actually discussed?

### Step 3: Create structured summary

Create `calls/[Filename] - Summary.md` with these sections:

```markdown
# [Meeting Type] Summary
**Date:** [Date]
**Participants:** [Names and roles]
**Absent:** [If relevant]

---

## Executive Summary
[2-3 sentence overview of key outcomes]

---

## 1. [Topic Name]
**Status:** [Current state]
**What was discussed:** [Details]
**Decisions made:** [If any]
**Action items:** [If any]

[Repeat for each major topic - aim for 8-15 topics for substantial meetings]

---

## Key Decisions Made
[Table format: Decision | Details]

---

## Blockers Identified
[Table format: Blocker | Owner | Resolution]

---

## Next Steps
[Numbered list of immediate actions]
```

### Step 4: Deep analysis (THE CRITICAL STEP)

This is where you "think hard." Create `calls/[Filename] - Analysis.md` examining:

#### 4.1 Patterns and recurring themes
- Is someone consistently a bottleneck?
- Are decisions being deferred repeatedly?
- What topics keep coming up but not getting resolved?

#### 4.2 What's said vs what's implied
- Read between the lines
- Note hedging language ("maybe," "we should consider")
- Identify things people avoided saying directly

#### 4.3 Technical debt being created
- Workarounds discussed
- "We'll fix it later" items
- Platform limitations being patched around

#### 4.4 Single points of failure
- Dependencies on one person's knowledge
- Architecture risks revealed in passing
- What would break if X person/system disappeared?

#### 4.5 Process gaps revealed
- Where did the conversation expose missing documentation?
- What questions couldn't be answered?
- What required tribal knowledge?

#### 4.6 Alignment gaps
- CEO expectations vs engineering reality
- Sales promises vs product capability
- Team assumptions that conflict

#### 4.7 Measurement gaps
- What can't they track that they need to?
- What decisions are being made without data?

#### 4.8 Strategic implications
- How does this discussion affect the 3-month runway?
- What's the opportunity cost of current priorities?
- Are they building toward PMF or away from it?

#### 4.9 Warnings and risks
- Lessons learned shared (like the bank URL ban story)
- Near-misses mentioned
- Security or reliability concerns raised

#### 4.10 Hidden dependencies
- Which clients are driving technical decisions?
- What external factors constrain choices?

### Step 5: Extract action items by owner

Parse the transcript for commitments made. Organize by person:

```markdown
### [Person]'s Tasks
- [ ] **[Task name]** [estimate if given]
  - [Context/details]
  - [Dependencies]
```

Be thorough - people make commitments casually that get forgotten.

### Step 6: PROPOSE changes to action-items (CRITICAL REVIEW STEP)

**Do NOT edit action-items-ruy-jan2026.md yet.** First, present a structured proposal for user review.

Read the current action items file and prepare a proposal showing:

#### 6.1 Proposed additions for Ruy

Present as a numbered list so user can reference by number:

```markdown
## Proposed Additions to Your Action Items

### New Tasks (items you committed to)
1. **[Task]** → Section: [target section]
   - Context: [why this is attributed to you]

2. **[Task]** → Section: [target section]
   - Context: [quote or moment from call]

### Items to Mark Complete
3. **[Existing task]** - appears resolved per discussion at [timestamp/context]

### New Blockers
4. **[Blocker]** - Owner: [who], Resolution: [what]

### Items Mentioned But NOT Yours (for awareness)
These came up but are owned by others:
- Mike: [task]
- Leo: [task]
- Daniel: [task]
```

#### 6.2 Flag uncertain attributions

If a task is ambiguous about ownership, flag it:
```markdown
### ⚠️ Needs Your Input
5. **[Task]** - Unclear owner. You were mentioned but [reason for uncertainty]
   - Add to your list?
   - Assign to someone else?
   - Skip?
```

#### 6.3 Ask for explicit feedback

End with:
```markdown
---
**Please review and respond:**
- Which items to ADD? (list numbers, or "all" / "none")
- Which items to SKIP? (list numbers)
- Any corrections to tasks or sections?
- Anything missing?
```

**STOP and wait for user response before proceeding to Step 7.**

### Step 7: Apply approved changes only

After user provides feedback:

1. Apply ONLY the approved additions
2. Skip items user rejected
3. Make any corrections user specified
4. Update Reference section with new files
5. If sprint planning or significant meeting, add section header

### Step 8: Update README.md if needed

- Update "Current Sprint" table if sprint planning
- Update "Next Actions" section
- Add reference to new call summary

### Step 9: Present final summary

Show:
1. Summary of topics covered
2. **Key strategic insights** (the analysis findings)
3. What was added to your action items (after approval)
4. Files created/updated
5. Any remaining questions

### Step 10: Commit changes

```bash
git add calls/ action-items-ruy-jan2026.md README.md
git commit -m "[Meeting type] [Date]: summary, analysis, and action items

- [Key outcome 1]
- [Key outcome 2]
- [Key insight from analysis]

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

## Analysis framework checklist

Use this checklist when doing Step 4 analysis:

- [ ] Who is the bottleneck in this conversation?
- [ ] What's being kicked down the road?
- [ ] What platform/tool limitations are being worked around?
- [ ] What would break if [key person] left?
- [ ] What can't they measure that matters?
- [ ] Where do CEO/leadership expectations differ from reality?
- [ ] What security/reliability risks were mentioned in passing?
- [ ] Which client is driving the most technical decisions?
- [ ] What process is missing that caused confusion?
- [ ] What's the meta-theme of this meeting?

## Output files

| File | Purpose |
|------|---------|
| `calls/[Name] - Summary.md` | Structured topic-by-topic summary |
| `calls/[Name] - Analysis.md` | Deep strategic implications |
| `action-items-ruy-jan2026.md` | Updated with new tasks |
| `README.md` | Updated if sprint planning |

## Parameters

You can specify:
- Custom transcript: `/process-call calls/strategy-call-jan20.txt`
- Skip commit: `/process-call --no-commit`
- Summary only (skip analysis): `/process-call --summary-only`

Default: Process most recent unprocessed `.txt` in `calls/`

## Example insights to surface

Good analysis finds things like:
- "The 'testing vs staging' rename is a symptom - the real problem is no shared process"
- "P&G SSO work is actually patching around Thinkific limitations - if they pivot to standalone, this is throwaway"
- "Story points without retrospectives are vanity metrics"
- "The 3-day demo notice rule will fail without automation"
- "Client lifecycle visibility gap means they can't measure retention, which means they can't validate PMF"

These insights connect scattered comments into strategic understanding.
