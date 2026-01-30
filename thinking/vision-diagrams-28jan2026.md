# Vision Diagrams — Thinking Notes

> January 28, 2026 — Working through which images to use in `core/vision.md` to make the two design spaces visually distinct and communicate the AI Coach unlock.

---

## The Three Images

The vision doc needs three visuals that work together:

| Position in doc | Image | What it communicates |
|---|---|---|
| **The AI Coach Unlock** (shared foundation) | GPS Dashboard — 3-panel comic strip (NEW) | The invisible made visible. Your goals stay present, so you act with intention instead of autopilot. |
| **Design Space 1: Inside the Individual (LD)** | Email Response comic strip (EXISTS: `archive/diagrams/09-email-response-comic-strip.png`) | The personal moment of change. Trigger → Intervention → Outcome. "Glad I didn't send that first draft." |
| **Design Space 2: Inside the Team (TE)** | Ambient Visualization from "Are We On Track?" paper (EXISTS: `paper-images/Team effectiveness and visualization.png`) | The team's conversation made visible in real time. Topics, goals, connections tracked as the meeting evolves. |

### Why this pairing works

- **GPS Dashboard** sits above both design spaces — it represents what the AI Coach *produces*: structured, visible data about growth. Oseas's lockstep principle (coaching + visibility) in one artifact.
- **Email comic strip** is deeply personal — one person, one moment, one choice made differently.
- **Ambient visualization** is deeply collective — a team meeting, dynamics unfolding over time.

Nobody looks at the email comic strip and the ambient visualization and thinks "same thing."

---

## Key Insight: "Reminded of What Matters → Acting with Intention"

The GPS dashboard arc is NOT about a crisis moment (that's the email comic). It's about the daily grind making you forget your goals. The dashboard pulls you back:

> "Oh right — *this* is what I'm working on. *This* is why it matters."

If you make your goals visible all the time, it's easier to change behaviors. **Intention** is the keyword — the bridge between awareness and action (core Axialent concept: espoused values vs. values-in-action).

---

## GPS Dashboard Comic Strip — Gemini Prompt

### Story Arc

**Trigger:** Juan is lost in the noise of daily work, on autopilot
**Intervention:** GPS Dashboard on his phone shows his goals and his team's commitments
**Outcome:** He walks into his next interaction with intention — he knows what he's working on and why

### The 3 Panels

#### Panel 1: "Reminded" — The Noise
**Scene:** Juan walking through a busy office hallway between meetings, looking slightly overwhelmed or on autopilot. People passing by, maybe carrying laptops or coffee. His phone buzzes with a notification. He glances down at it.

**Juan's expression:** Distracted, slightly stressed, going through the motions.

**Visual cues:** Motion blur or busy background suggesting the rush of work. The phone notification is a gentle green glow — the coach reaching out.

---

#### Panel 2: "Of What Matters" — The GPS Dashboard (UI Mockup - CENTER)
**Scene:** Close-up of Juan's phone screen showing the GPS Dashboard. Clean, clear interface.

**Top section — My Progress:**
- Header: "Team Lead Promotion" with a destination icon
- Progress bars:
  - "Being seen as collaborative" — 68% progress, green bar
  - "Managing conflict well" — marked as "Current Focus" with a star icon
  - "Building team trust" — "Up next"
- Small trajectory chart at bottom showing upward trend labeled "Your Trajectory"

**Bottom section — My Team:**
- Header: "Team Agreements" with a team icon
- "Improve decision-making" — active commitment
- "Honor time commitments" — active commitment
- Nudge card: "Team meeting in 2 hours. Your focus today: listen before responding."

**Style:** Clean mobile UI mockup with slight hand-drawn/sketch feel to match comic aesthetic. Green accents (Conscious Insights brand). White background, clear hierarchy. Two distinct sections (individual + team) visible on one screen.

---

#### Panel 3: "Acting with Intention"
**Scene:** Juan approaching a glass-walled meeting room where colleagues are already seated. He's about to open the door. His posture is upright, calm, focused — not anxious, but *oriented*.

**Thought bubble:** "Right. Listen first today."

**Visual cues:** Phone tucked in pocket (he's absorbed the information, now he's acting on it). Maybe warmer lighting than Panel 1. His expression is purposeful — a slight, confident calm.

**Optional:** Through the glass, you can see team members at the table, suggesting this is the team meeting the dashboard referenced.

---

### Gemini Prompt

```
Create a 3-panel horizontal comic strip showing a professional named Juan being reminded of his goals by an AI coaching dashboard on his phone, then acting with intention.

Panel layout: 3 panels in a single horizontal row. Headers above each panel.

PANEL 1 (left) - Header: "REMINDED":
Juan walking through a busy office hallway between meetings, looking slightly overwhelmed and on autopilot. People passing by in the background. His phone buzzes with a notification — a gentle green glow on the screen. He glances down at it, distracted. Style: warm comic illustration with busy, slightly blurred background to convey the rush of work.

PANEL 2 (center) - Header: "OF WHAT MATTERS" - UI MOCKUP:
Close-up of Juan's phone screen showing a coaching dashboard called "GPS Dashboard." Top section labeled "My Progress" shows: "Team Lead Promotion" as the main goal, with three sub-goals as progress bars: "Being seen as collaborative" at 68%, "Managing conflict well" marked as "Current Focus" with a star, and "Building team trust" labeled "Up next." Below is a small upward trajectory chart. Bottom section labeled "My Team" shows: team agreements "Improve decision-making" and "Honor time commitments" as active items, plus a nudge card saying "Team meeting in 2 hours. Your focus today: listen before responding." Style: clean mobile UI mockup with slight hand-drawn sketch feel. Green accent colors, white background, clear visual hierarchy.

PANEL 3 (right) - Header: "ACTING WITH INTENTION":
Juan approaching a glass-walled meeting room where colleagues are seated inside. He's about to open the door. His posture is upright, calm, and purposeful — not anxious, but oriented. Phone tucked in his pocket. Thought bubble: "Right. Listen first today." Warmer lighting than panel 1. Through the glass, team members are visible at the table. Style: warm comic illustration matching panel 1, but with warmer, calmer tone.

Overall style: Cohesive comic strip feel matching a companion piece (email response comic strip). Panels 1 and 3 are illustrated in warm comic style, panel 2 is a stylized mobile UI mockup. Warm color palette with green coaching app accents. The emotional arc should be clear: autopilot → reminded → intentional. The character Juan should be consistent across panels — a Latino professional in his 30s, wearing business casual.
```

---

## Open Questions

- Does the GPS dashboard need to show enough detail that you can read the goals, or is the *shape* of the information enough? (The email comic strip has readable text in the sidebar.)
- Should "My Team" section be prominent or subtle? It needs to hint at both levels without making the dashboard feel cluttered.
- Do we want panel headers ("Reminded / Of What Matters / Acting with Intention") or simpler ones ("The Noise / The Dashboard / The Outcome")?

---

## Next Steps

1. Generate the GPS Dashboard comic strip using this prompt
2. Place all three images in `core/vision.md` at the appropriate sections
3. Consider whether the existing hand-drawn GPS sketch (`site/diagrams/03-gps-dashboard.png`) should be archived
