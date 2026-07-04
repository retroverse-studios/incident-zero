# Design Review — v2.2 (Pre-Playtest Expert Assessment)

**Purpose:** An honest module-by-module assessment from two lenses — cybersecurity authenticity/challenge, and new-player engagement — written *before* playtesting so real feedback can confirm or refute it. Treat every claim here as a hypothesis.

---

## Overall Verdict

The game's teaching engine is the **justification mechanic**, not the dice: players win by talking like analysts. That is pedagogically excellent and rare in this genre. The corollary is that session quality depends heavily on the Threat Orchestrator — the game is a *facilitated experience* first and a board game second. The content authenticity (post-v2.2) is above commercial educational-game standard. The main engagement risks are TO-dependence, downtime in one-action-per-turn play, and two talk-heavy modules that need the right group.

**Challenge calibration:** right for students and mixed groups; mechanically shallow for security professionals unless the TO raises the justification bar (see "Expert Mode" rubric, FUTURE_WORK #16). Experts will breeze the verbal layer; their challenge must come from adjudication strictness and expansion content (zero-day, APT, OT), not card math.

---

## Module-by-Module

### Network Building — Reasonable, least distinctive
- **Expert lens:** Budget-vs-coverage trade-offs, capacity/overload (consolidation risk), and architecture choices (flat vs. zoned vs. zero-trust) are real decisions with realistic consequences. Nothing wrong; also nothing surprising to a practitioner.
- **New-player lens:** Building things is inherently satisfying and it's the gentlest on-ramp (no hidden information, no adversary). Risk: feels like a spreadsheet exercise if the TO doesn't narrate the business context. The REQ/EVT standalone decks (v2.2) are what make it a *game* rather than a worksheet — lead with them.
- **Watch in playtest:** does free placement per turn make turns feel meaty, or does the whole build collapse into turn 1?

### Hardening — Good, teaches the right instinct
- **Expert lens:** Control-to-threat mapping via per-tactic defense bonuses is genuinely how you want juniors to think (which control blunts which technique, and why signature AV loses to LOTL). Missing realism, deliberately: operational drag (alert fatigue, maintenance) — a possible v3 "operational load" stat.
- **New-player lens:** The pentester challenge is the best tension beat in the proactive modules — you built it, now it gets attacked. The v2.2 anti-playbook-spam scoring means layering actually wins, which is the lesson.
- **Watch in playtest:** do players feel the pentester rolls are fair, or "gotcha" (tactic drawn they couldn't have countered)?

### Incident Response — Good bones, the flagship loop
- **Expert lens:** Kill-chain-ordered hidden-chain deduction is a sound abstraction; vector+step matching teaches taxonomy. Honest critique: it teaches *classification*, not *analysis* — "roll to investigate email headers" doesn't exercise reading actual headers. Cheapest big upgrade: scenario packs whose clues are **fake artifacts** (log excerpts, alert screenshots) instead of prose (FUTURE_WORK #16).
- **New-player lens:** Strongest module for excitement — it's a mystery. Hidden information + escalating breach costs + clue reveals is real deduction-game tension. The v2.2 economy (Active Breach Cost, two-investigation reveal) should make wins feel earned; that's a key playtest question.
- **Watch in playtest:** dice-streak frustration (three failed rolls in a row feels bad regardless of design); whether the TO can keep clue delivery dramatic.

### Disaster Recovery — Best-in-class concept, heaviest to run
- **Expert lens:** This is a **tabletop exercise (TTX) in a box** — stakeholder trust, notification clocks, ransom dilemma are exactly what organizations pay consultants to drill. Post-v2.2 (GDPR clock, OFAC-accurate ransom framing, real pay/negotiate/refuse trade-off) it's the most professionally credible module.
- **New-player lens:** Engaging for groups who like role-play and argument; dry for players wanting dice-and-tactics. It's also the heaviest bookkeeping (5 trust meters + 3 tracks + events) — the tracker sheet is load-bearing.
- **Watch in playtest:** does bookkeeping crowd out the drama? If yes, consider collapsing to 3 stakeholder meters (Customers / Regulators / Board) in a "lite" variant.

### Forensics — Most novel, most abstract
- **Expert lens:** Almost no educational game touches chain of custody, order of volatility, or attribution confidence — this module's existence is a differentiator, and the MITRE mappings are now correct. Critique mirrors IR: meters abstract the *reasoning*; the "Why This Works" text carries the teaching. A fake evidence-timeline handout to physically assemble would convert it from abstract to tactile.
- **New-player lens:** Puzzle-solvers will like it; the four-meter structure gives clear progress feedback. Risk: without IR played first, the "case" can feel contextless — recommend the IR → Forensics pairing as the default intro sequence.
- **Watch in playtest:** is the Duration mechanic (results arrive later) satisfying anticipation or annoying delay?

### Audit & Compliance — Simple core, hidden gem inside
- **Expert lens:** The 6-domain PASS/FAIL loop is checklist-y — fine for teaching, thin for practitioners. But **Variation C (the debate format)** is the pedagogical gem of the whole box: arguing risk acceptance vs. negligence is precisely the daily texture of GRC work. Consider promoting it from "variation" to the module's headline mode.
- **New-player lens:** The base assessment mode is the least "gamey" module; the debate mode flips that completely for groups of 6-10 and needs almost no components. Market them as two different games.
- **Watch in playtest:** does anyone actually play the base mode when the debate mode exists?

---

## Cross-Cutting Engagement Risks (hypotheses to test)

1. **TO-dependence:** a flat facilitator = flat game. Mitigations queued: scenario packs with scripted clue drama, TO screen, eventually the IF/digital TO.
2. **Quarterbacking:** one confident player deciding for the table during the 2-3 min planning phase. Mitigation if observed: role cards (FUTURE_WORK #16).
3. **Downtime:** one action per turn can leave quieter players idle; watch whether table talk stays inclusive.
4. **Table presence:** text-only cards have weak shelf appeal; excitement must come from narrative until the Phase A retro art lands. Acceptable for classrooms, limiting for game-night adoption.
5. **Loss experience:** losing to the turn clock should feel like "we investigated the wrong things," never "the dice hated us." If playtesters report the latter, revisit DC spread before touching budgets.

## Suggested Playtest Order (engagement-optimized)

1. **Incident Response** (the hook — mystery + tension)
2. **Hardening** (payoff loop — build then defend)
3. **Audit Variation C** (zero-component debate game, great for big groups)
4. **Disaster Recovery** (the TTX — best with invested groups)
5. **IR → Forensics** pairing (the investigation arc)
6. **Network Building** with REQ/EVT decks (calmest; good opener for shy groups too)
