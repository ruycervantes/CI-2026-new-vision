# /diagrams - Create whiteboard-style diagrams

Generate diagrams for documents using the project's visual style.

## Workflow

1. **User points to a document** — "Look at this doc and suggest diagrams"
2. **Discuss what diagrams would help** — What concepts need visual explanation? What's the story?
3. **Create prompts file** — Save to `archive/diagram-prompts/<topic>-diagrams.md`
4. **Generate images** — Use nanobanana-gemini-images skill
5. **Review and iterate** — Adjust prompts if needed, regenerate

## Style Guide

All diagrams use **whiteboard/sketch aesthetic**:
- Hand-drawn look, collaborative feel
- As if drawn during a strategy meeting
- Professional but informal

### Colors
- **Blue** — Team/consultant elements
- **Green** — Personal/AI elements
- **Yellow/Gold** — Highlights, key elements
- **White background** — Always
- **Black** — Text, outlines

### Visual Elements
- Rounded rectangles for containers/zones
- Curved arrows (not straight) for relationships
- Small icons next to labels (people, clipboard, chat bubble, etc.)
- Annotations on the side for context
- Dotted lines for secondary connections

## Prompt Structure

Each diagram prompt should have:

```markdown
## [Number]. [Diagram Name]

**Purpose:** What this diagram explains

**For document section:** Where it will be used

**Prompt:**
```
[Detailed prompt with:]
- TITLE at top
- Spatial layout (what goes where: left, right, top, bottom, center)
- Labels and subtitles for each element
- Icons for each element
- Arrow labels for relationships
- Annotations/callouts
- Style instructions at the end
```

**Key Elements Checklist:**
- [ ] Element 1
- [ ] Element 2
- [ ] etc.

**Output filename:** `<prefix>-<number>-<name>.png`
```

## Example Prompt Pattern

```
Create a whiteboard-style diagram showing [WHAT]. Hand-drawn, [ORIENTATION: horizontal/vertical] flow.

TITLE at top: "[TITLE]"
Subtitle: "[SUBTITLE]"

[SECTION 1] - [POSITION]:
Draw [SHAPE] containing:
• [ELEMENT] (icon: [ICON])
• [ELEMENT]
Label: "[LABEL]"
Annotation: "[CONTEXT]"

[SECTION 2] - [POSITION]:
...

[CONNECTIONS]:
• Arrow from [A] to [B] labeled: "[RELATIONSHIP]"
• Dotted line connecting [X] and [Y]

At the bottom: "[TAGLINE OR KEY INSIGHT]"

Style: Hand-drawn whiteboard sketch. [COLOR INSTRUCTIONS]. White background with subtle texture. Professional but informal, like drawn during a strategy meeting.
```

## Generating Images

After creating the prompts file, generate each image:

```bash
python3 ~/.claude/skills/nanobanana-gemini-images/scripts/generate.py \
  --prompt "[FULL PROMPT TEXT]" \
  --output site/diagrams/<filename>.png \
  --size 2K
```

The script auto-loads `GEMINI_API_KEY` from the project's `.env` file.

## File Locations

- **Prompts:** `archive/diagram-prompts/<topic>-diagrams.md`
- **Images:** `site/diagrams/<prefix>-<number>-<name>.png`
- **Style reference:** `archive/diagram-prompts/diagram-prompts-v2.md`

## Common Diagram Types

| Type | Best For | Key Elements |
|------|----------|--------------|
| **Two-panel comparison** | Before/after, old vs new | Side-by-side panels, arrow between, contrast in color |
| **Timeline/journey** | Processes, phases, user journeys | Horizontal flow, waypoints, loop for iteration |
| **Two-track parallel** | Simultaneous processes | Stacked horizontal lanes, connection points between |
| **Hierarchy** | Levels, dependencies | Vertical stack with arrows between levels |
| **Hub and spoke** | Central concept with connections | Central element, radiating connections |

## Tips

- **Discuss before creating** — Understand what story the diagram needs to tell
- **One concept per diagram** — Don't overload; split into multiple if needed
- **Labels matter** — Clear, concise labels are more important than visual complexity
- **Iterate** — First generation often needs adjustment; prompts are saved for re-running
