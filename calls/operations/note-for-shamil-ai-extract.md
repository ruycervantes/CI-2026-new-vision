# Note for Shamil: AI Extract Feature

Hey Shamil,

Here's a summary of what we discussed for the Thinking Partner sidebar feature.

---

## What It Does

The sidebar shows a progressive summary of the coaching conversation. As the user advances through the conversation stages, the sidebar fills up with extracted information.

## The 6 Fields to Extract

| Field | When to Populate |
|-------|------------------|
| **My Challenge** | After context understanding stage |
| **Goal** | After context understanding stage |
| **Gap** | After gap identification + acknowledgement |
| **Approach** | After framework is offered (e.g., "difficult conversation") |
| **Key Insights** | During/after bridget profile conversation |
| **Commitment** | After contracting stage (near end) |

## Conversation Flow (for reference)

1. Context understanding
2. Gap identification
3. Gap acknowledgement → user is asked "how important is it to bridge this gap?"
4. Framework selection → jumps to Bridget profile
5. Framework application
6. Committing
7. Feedback

## Implementation Approach

**Try LLM inference first** (the "lazy way"):
- After each user message, call an LLM
- Prompt should analyze: given the conversation so far, which fields can we fill?
- If a field can be extracted, return it; if not, wait for next turn

**Fallback if LLM doesn't work reliably:**
- Build a state machine that explicitly tracks conversation state
- More complex but deterministic

Start with LLM approach and see if it works well enough.

## UI Requirements

- Icons: use **Lucid React** (already in project)
- Copy button: let user copy the full summary as text
- Fields appear progressively (don't show empty fields, or show them grayed out)

## Where to Look

- `AI Extract` code exists but isn't working - start there
- Configuration profiles: Thinking Partner vs Bridget profiles
- Prompts: check the conversation stage markers in the prompt files

## Next Steps

1. Review the codebase and understand current AI Extract implementation
2. Provide estimate by tomorrow (fill in Asana)
3. If you have questions, ping me

---

Let me know if anything is unclear.

Ruy
