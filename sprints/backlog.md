# Backlog — Committed Work Not Yet in a Sprint

> Work that's been decided but not assigned to a specific sprint yet.
> Pull from here when creating sprint stories.

---

## WorkOS SSO/Provisioning POC (Daniel)

**Source:** Enterprise Connections call, Jan 27, 2026
**Strategy doc:** `enterprise/integration-strategy.md`

### POC Scope

1. Configure WorkOS to handle Boetus.com authentication (team's own Microsoft tenant — can experiment freely)
2. Route users to either Thinkific or Conscious Insights based on role
3. Test provisioning flow
4. Handle single URL limitation: build routing middleware to direct users to correct instance (pg.stoic, axialent.stoic, etc.)

### Technical Context

- WorkOS does NOT replace Postgres user database — it handles the IdP translation layer
- P&G went direct (custom middleware) because "all we needed was translation" — WorkOS is the scalable multi-client path
- Shamil attempted a WorkOS POC previously and got stuck — Daniel should document as he builds
- Daniel holds critical WorkOS knowledge; documentation is important for bus factor

### Success = (undefined — needs acceptance criteria before starting)

### If POC succeeds → Phase 2

- Implement for Axialent internal use (staging environment)
- Then real clients = production

### Dependencies

- Installation script should be finished first
- Daniel available ~1 month during government leave (baby due ~Feb 5)
- Mike will need Daniel support in last 15 days of Q1 for Teams production deployment

---

## Evaluate Inworld.ai for TTS (Mike)

**Source:** Email thread — Oseas/Mike/Ruy, Jan 29, 2026

Top model in TTS benchmarks: best quality, much cheaper than ElevenLabs. Oseas has a personal connection (cousin works at Inworld in San Francisco). Strategic angle: credits + developer relationships to accelerate.

- Evaluate Inworld Runtime for voice/TTS: https://inworld.ai/runtime
- Benchmarks: https://artificialanalysis.ai/-families/inworld
- Pursue credits and dev access through Oseas's connection

### Dependencies

- Mike already reviewed and recommends it
- Oseas to facilitate intro for credits/dev relationships
