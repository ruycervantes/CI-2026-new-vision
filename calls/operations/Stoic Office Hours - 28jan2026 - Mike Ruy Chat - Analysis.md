# Mike-Ruy Chat — Analysis
**Date:** January 28, 2026
**Context:** Debrief after Product Strategy session (Oseas, Nelson, Mike, Ruy)

---

## 1. Patterns and Recurring Themes

**Mike thinks visually, Ruy thinks methodologically.** Mike's first instinct after the Oseas session was "show a dashboard with graphs — that's what sells." Ruy immediately connected it to behavior change theory ("users need to see their goals"). This is a productive complementarity — Mike pushes toward what's demo-able, Ruy grounds it in what's effective.

**Prompt avoidance.** Ruy explicitly said prompt work is a "time sink" he always underestimates. This is notable because the AI Coach's core is prompting + memory. If Ruy avoids prompt work, who does it? This could become a bottleneck for Coach quality.

**Scope anxiety.** Mike is "optimistic about Q1 *based on the idea that there's not much more*." This is a warning: the product strategy session just expanded the conceptual scope (two market bets, shared foundation, impact visibility). Mike is signaling he needs the scope to stay contained for engineering.

---

## 2. What's Said vs What's Implied

**"Yo creo que la otra chamba es nomás asegurarme que las instrucciones están bien"** — Ruy is downplaying the onboarding/context-setting work. Getting users to use the product correctly is a design problem, not just "instructions." This is where UX matters.

**"La mayoría son request features, no son bugs"** — This is actually good news buried as a complaint. If users are requesting features rather than reporting bugs, the core product works. The challenge is prioritization discipline, not quality.

**Mike's "Hay que buscar e interrogar a Claude"** — Mike is comfortable with AI-assisted prototyping. This is an asset: the team can prototype memory approaches faster than building from scratch.

---

## 3. Technical Implications

### Three Memory Approaches — Trade-offs

| Approach | Pros | Cons |
|----------|------|------|
| Hack existing facts | Fast, no new infra | May not scale, messy data model |
| Structured JSON get/set | Clean, queryable, supports dashboards | More engineering, needs design |
| Session artifacts (text) | Simple, transparent, LLM-native | Hard to extract structured data, context window limits |

**The real answer is probably hybrid:** artifacts for coaching quality (LLM reads the story), structured data for dashboards and reporting (machines read the numbers). This aligns with Option C in the AI coach design doc.

### Dashboard Data is Already There
Mike noted "tenemos todos los datos del db" — the data exists, it's just not surfaced. A user dashboard could be a relatively quick win that creates the "wow" Oseas wants while the deeper Coach work happens.

---

## 4. Alignment Gaps

**Oseas wants "wow" demos → Mike proposes dashboards → Ruy wants methodology depth.** These aren't contradictory but they compete for attention. Risk: the team builds a pretty dashboard that doesn't actually improve coaching, because that's what demos well.

**Nelson's spec timeline is unclear.** Ruy said "Nelson se lo queda" for dashboard specs, but Nelson is in Barcelona doing this alongside HPT validation. No timeline was set. If Nelson's specs are late, the "lockstep" between coaching and visibility stalls.

---

## 5. Strategic Implications

### The 5-User Test is the Right Move
Getting 5 real users by Friday with clear instructions is the most valuable thing they can do. It forces quality, creates feedback, and gives Leo something concrete for sales conversations. Everything else is planning.

### Memory Architecture is THE Technical Decision of Q1
The three options Ruy described will determine:
- How sophisticated the Coach can be (memory quality)
- How fast they can build dashboards (data structure)
- How hard it is to iterate on coaching quality (prompt flexibility)

This decision should involve Mike, Shamil, and possibly a prototype comparison. Don't decide theoretically.

### Shamil's Transition is Well-Timed
Moving Shamil from Teams to Coach implementation makes sense: Teams notifications are working (Mike can maintain), and Coach work needs implementation capacity. But Shamil needs clear specs — Ruy's "bottleneck for specs" problem applies here.

---

## 6. Risks

| Risk | Likelihood | Impact |
|------|-----------|--------|
| Prompt work avoidance delays Coach quality | High | High — the Coach IS prompting |
| Mike overloaded (Teams bugs + architecture consults + sprint planning) | Medium | Medium — single point of failure for tech decisions |
| 5-user test reveals fundamental UX problems | Medium | Low — better to find now |
| Memory architecture chosen without proper comparison | Medium | High — hard to change later |
| Nelson dashboard specs delayed | Medium | Medium — breaks lockstep principle |

---

## 7. What This Confirms from Earlier Calls

- **AI Coach is Q1 focus** — now confirmed by both Ruy and Mike (not just strategy session)
- **Dashboard idea has legs** — both user-facing (engagement) and buyer-facing (sales). Two dashboards, one data source.
- **Team is optimistic but capacity-constrained** — Mike's "as long as nothing more is added" is a boundary that needs respecting
- **Ruy's self-awareness is strong** — knows prompts are his time sink, knows he's a bottleneck. Whether he acts on this awareness is the question.
