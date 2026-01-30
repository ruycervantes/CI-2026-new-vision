# Chatbot Design

This directory contains the process, instructions, and examples for designing custom chatbots on the Conscious Insights platform.

## How It Works

Chatbot design follows a 6-phase collaborative process where you work with Claude to go from idea to specification. The process is emergent — you discover the right design through dialogue, not by filling in a template.

### The Pipeline

```
1. Think about what you want (use the FRD below for framing)
2. Have a design conversation with Claude using the process instructions
3. Claude helps you surface design tensions, sketch structure, and draft specs
4. Output: Project Brief + Chatbot Specification
5. Build the chatbot from the spec
```

### Phase Overview

| Phase | What Happens |
|-------|-------------|
| **1. Understand Context** | What's the program? Who's it for? What gap does this chatbot fill? |
| **2. Clarify Intent** | What type of chatbot? What does the user arrive with / leave with? |
| **3. Surface Design Tensions** | Structured vs. flexible? Prescriptive vs. emergent? Name tradeoffs explicitly. |
| **4. Sketch Structure** | Modes, phases, domains, principles — confirm the skeleton before writing. |
| **5. Draft & Iterate** | Project Brief first, then Chatbot Specification. Small adjustments, not rewrites. |
| **6. Confirm Outputs** | Two clean documents: Project Brief + Chatbot Specification. |

### Two Outputs Per Chatbot

1. **Project Brief** — The context document. Program, problem, gap, success criteria.
2. **Chatbot Specification** — The design document. Identity, flow, domains, principles.

## Key Resources

| Resource | Description |
|----------|-------------|
| [Custom Bot FRD (Notion)](https://www.notion.so/axialent/Custom-Bot-Development-Feature-Requirement-Document-198073cafffb8064b678fa5d222e3006) | Feature Requirement Document — how Ruy thinks about creating custom bots |
| [Prompt Design Guide (GitHub)](https://github.com/stoicenteprises/conscious-insights/blob/main/docs/prompt_design_guide.md) | Instructions used to automate prompt creation. Use after you have clarity on what you're building. |
| [Duke Chatbot Design Session (Claude)](https://claude.ai/share/19c5a808-f836-49f7-9f46-3595f20cf548) | Shared conversation showing the full design process in action — backward-engineered script + examples of successful chatbot creation. |

## Files in This Directory

| File | Description |
|------|-------------|
| `chatbot-design-process-instructions.md` | Full instructions for Claude on how to run a chatbot design session (the 6-phase process detailed above) |
| `ai-adoption-conversations-coach-proposal.md` | Example: Chatbot that helps leaders identify and prepare for critical AI adoption conversations |
| `ai-leadership-action-plan-facilitator-proposal.md` | Example: Chatbot that facilitates leaders creating a personal AI adoption action plan |

## Guiding Principles

- **Clarify before drafting** — Don't write until intent is clear.
- **Surface tensions as choices** — Make design decisions visible and collaborative.
- **Sketch before drafting** — Confirm structure before writing full documents.
- **Use the user's language** — Listen for words and frameworks that matter.
- **Stay in service of the outcome** — Users should leave with clarity and capability, not dependency.
