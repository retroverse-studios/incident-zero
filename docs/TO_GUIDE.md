# The Threat Orchestrator's Guide

**Version:** 2.2 - Playtest Edition
**Audience:** anyone about to run Incident Zero — teacher, trainer, or the friend who volunteered.

---

## 1. The Role

The **Threat Orchestrator (TO)** is Incident Zero's dungeon master. You wear three hats, usually in the same minute:

- **The Adversary** — you built the hidden attack chain; you know what the Blue Team doesn't. You want them challenged, not beaten.
- **The Narrator** — you turn card text into a story. "You failed the roll" is a rules outcome; "the log archive was rotated last night — whatever was there is gone" is a game.
- **The Teacher** — you award the justification bonuses, ask "why?", and run the debrief. Every roll is a chance to make someone articulate real security reasoning.

If you've ever run a tabletop RPG, you already have 80% of this. The remaining 20% is the adjudication rubric in §4 — it's the part that makes this game educational rather than just thematic.

**A good TO makes the game.** The same scenario is flat or unforgettable depending on how you deliver clues and how honestly you judge reasoning. That's why this guide exists.

## 2. Golden Rules

1. **Be fair, not nice.** Never fudge dice — in either direction. The rules already give you legitimate difficulty dials (§5); use those, not your thumb on the d20.
2. **Never block on ignorance.** If players are stuck, sell them a hint through the fiction ("your SOC junior suggests looking at outbound traffic...") rather than letting three turns die in silence.
3. **Announce costs before actions.** "That's 15 Budget — confirm?" prevents every argument you'd otherwise have.
4. **Explain outcomes.** Success or failure, say *why* in security terms. The explanation is the lesson; the roll is just pacing.
5. **Keep the clock.** 2-3 minutes of planning per turn, firmly. Deliberation past that point is quarterbacking, not strategy.
6. **Let them be wrong.** A confidently wrong plan that fails teaches more than a corrected plan that succeeds. Save the correction for the debrief.

## 3. Session Prep (15 minutes)

- [ ] Pick the module; skim its rules doc and its **v2.2 Playtest Edition Changes** section
- [ ] Build your scenario (IR: choose the chain; Hardening: threat profile; DR: pick scenario + place scheduled events on the timeline; Forensics: pick tier; Audit: pick sample org; NB: shuffle REQ/EVT decks)
- [ ] Print/lay out: [tracker sheets](../cards/print-templates/tracker-sheets.md), the module's cards, one d20 (d4/d6 where the module calls for them)
- [ ] **Rehearse your first clue out loud once.** Seriously — the first clue sets the session's tone.
- [ ] Decide your difficulty posture (§5) based on who's at the table
- [ ] First time running anything? Use the fully scripted opening in [How to Play §4](HOW_TO_PLAY.md)

## 4. Judging Justifications (the heart of the job)

The +2/+1 modifiers are the game's teaching engine. Your consistency is what makes them meaningful.

**+2 — Strong technical justification.** The player explains *methodology*: what they'll look at, and why that would reveal or stop this specific thing.
- ✅ "We pull the mail gateway logs and compare the return-path against the display-name domain — spoofed senders won't match." *(mechanism stated)*
- ✅ "Deploy EDR because living-off-the-land attacks won't trip signature AV — we need behavioral detection." *(threat-to-control logic)*
- ❌ "We investigate the email server thoroughly." *(a location is not a method)*

**+1 — Real tool or technique named.** Wireshark, Splunk queries, Mimikatz, a MITRE technique ID, an actual CVE.
- ✅ "Check LSASS access events — that's Mimikatz behavior, T1003."
- ❌ "We use our security tools." *(no it isn't)*

**Rulings that keep it fair:**
- **Judge the reasoning, not the vocabulary.** A beginner saying "check if the email really came from who it says" in plain words has the mechanism — award the +2. A buzzword salad without a mechanism gets +0.
- **Consistency beats generosity.** Whatever bar you set on turn 1 is the bar all game.
- **Escalate the bar as the group learns** — by session three, "we check the SIEM" that earned +1 in session one should need a specific query. Announce the escalation openly ("you're professionals now — I want specifics").
- **Expert groups ("Expert Mode"):** award +2 only for named artifacts, ATT&CK technique IDs, or detection logic. This is the challenge ceiling for practitioner tables — the card math never has to change.
- **One player monologuing every justification?** Ask a different player to give it each turn ("Sam, you're on comms — why does this matter to the regulator?").

## 5. Difficulty Dials (live, legitimate)

**Signs it's too easy:** no failed rolls; goal in sight with 40+ Budget spare; players bored.
**Signs it's too hard:** no progress for 3+ turns; consecutive failures; frustration replacing discussion.

| Easier (pick 1-2) | Harder (pick 1-2) |
|---|---|
| Richer clues (more specific detail per success) | Vaguer clues (accurate but terse) |
| Suggest an angle through the fiction | Expert-mode justification bar |
| Shorter chain / lower tier next game | Longer chain, expansion cards |
| Beginner budgets (module max) | Minimum budgets |

Never adjust by fudging a roll or changing a printed number mid-game — players smell it, and it teaches that outcomes are arbitrary.

## 6. Failure Modes (yours, not theirs)

| Failure | Symptom | Fix |
|---|---|---|
| The Encyclopedia | You lecture after every roll | One sentence of "why," save the rest for debrief |
| The Softie | Everyone always gets +2 | Re-read §4; require the mechanism |
| The Sphinx | Clues so cryptic nobody moves | Clues must be *actionable*: each should suggest at least one sensible next investigation |
| The Railroader | You steer them to *your* solution | Multiple paths are valid; score the outcome, not the route |
| The Accountant | You narrate numbers, not events | Lead with fiction, then state the numbers |
| The Rusher | Debrief skipped because time ran out | Protect the last 10 minutes like it's the win condition — it is |

## 7. Module Panels (your screen, one per module)

### 🔎 Incident Response — you are the hidden attacker
- **Setup:** secret chain in kill-chain order (3-5 cards) · turns = (chain × 2) + 1 → 7/9/11 · Budget 100 · team draws 5 Defense cards
- **Start of every turn, announce:** -5 Active Breach (any card hidden) · -5 per uncontained revealed threat · then current Budget
- **Actions:** Investigate 5 (1st success on a link = clue, 2nd = reveal) · Deploy 10/15/25 (vector+step match = reveal; partial = stays, +2 later vs its vector) · Emergency Response 15 (contain, no roll)
- **Always target the earliest unrevealed card.** On reveal: +1 uncontained, previous auto-contains, team picks reward (2 cards / +10 Budget / next Investigate 5+)
- **Your craft:** progressive clues — first success is a symptom, second-to-last is nearly a name. Announce "your deployed defenses are helping here" when the +2 persistence applies — it's a clue in itself.

### 🛡️ Hardening — you become the pentester mid-game
- **Setup:** threat profile via 1d6 across all 6 vectors · 7 turns · Budget 150 (or IR carryover)
- **Actions (one/turn):** Deploy defense 10/15/25 (two BASIC may be one action) · Upgrade 5 (+2 on that defense) · Playbook 10 (+3, **max 2 per game**) · Test & Drill (roll)
- **Pentester Challenge (turns 3-4):** draw PT cards. Resolution: d20 + printed bonus of the ONE chosen defense + its upgrades + relevant playbook ≥ the card's DC. No stacking across defenses. Multi-vector tactics = separate rolls, one defense each.
- **Victory gate:** score ≥60 AND ≥4 defenses deployed AND majority of tactics defended. Score = defenses×5 + upgrades×2 + playbooks×10 + tactics defended×5 + (Budget left/150)×10.
- **Your craft:** narrate the pentester as a person with a plan; read the card's teaching point after each resolution, win or lose.

### 🏗️ Network Building — you are the demanding business
- **Setup:** Budget 60/50/40 (easier→harder) · 5 turns = design-review phases · REQ deck (1/turn) + EVT events between turns
- **Turn rule:** place ANY number of affordable components. Required: Email, Web, Database, Identity (DC), Backup. Overload = +1 Budget per extra service over capacity.
- **Scoring:** max 40 · tiers 32-40 / 22-31 / 12-21 / <12 · smart utilization beats hoarding (5-15 left is the sweet spot)
- **Your craft:** play the CFO and the auditor — every REQ card is a stakeholder with a voice. "Legal called: we're in PCI scope now."

### 🚨 Disaster Recovery — you are the crisis itself
- **Setup:** 8 turns (~72h) · Budget 50 · 3 tracks (Investigation/Remediation/Communication) + 5 stakeholder trust meters at start values · place scheduled events: EVENT-01 T2, 04 T3, 03+09 T5, 02 T6, 12 T7; triggered events fire on conditions
- **Turn:** one ACTION card (0-20 Budget; Holding Statement is free). Advances are deterministic — **dice only for**: optional Justification bonus (strong reasoning → d20, 11+ = +5% on that advance) and ACTION-13's pay-the-ransom reliability roll (1-5 = keys fail)
- **Deadlines:** customers by T5 · regulator penalties from T6, hard GDPR line T8 · **Loss: any trust meter hits 0%** · final Reputation computed at game end (tiers 85/70/55/40)
- **Your craft:** you are the ringing phone. Open every turn in-fiction: "The journalist calls again. The board wants a number. What do you do?"

### 🔬 Forensics — you are the evidence
- **Setup:** tier sets turns (TIER 2 ≈ 8-10, TIER 3 = 11-13, +d4 variation) · Budget 75 · 4 meters at 0%
- **Actions:** Investigation card (printed cost/DC; Duration N = results arrive N turns later, one in flight) · Analyze evidence 5 (DC 10, once per card, only two meters) · Follow lead 5
- **Key rulings:** evidence card's printed impacts replace the investigation's advance line (no double counting) · +5% Chain of Custody each time evidence is discovered AND the team states preservation (hash/image/export) · partial success band = DC-2 to DC-1 · haste -2
- **Victory (checked first, at game end):** V1 Attribution≥90+Timeline≥80 · V2 Timeline≥80+Chain≥80+CoC≥70 · V3 any two ≥70. Budget-out is NOT a loss.
- **Your craft:** describe evidence sensorily ("the timestamp is three hours *before* the alert"). Ask "how are you preserving that?" every single time — that question IS the chain-of-custody lesson.

### 📋 Audit & Compliance — you are the organization under review
- **Setup:** pick sample org (or the debate Variation C) · no budget during assessment (100 only for optional remediation cards)
- **Scoring:** 6 domains, PASS/FAIL against printed criteria (stars: 1-2★=FAIL, 3★+=PASS, PARTIAL=FAIL) → X/6 · gap penalties for later modules capped at -30 total
- **Ruling discipline:** the printed criteria decide, not vibes — untested backups FAIL even if the team likes the org. Disagreement about a borderline call is not a problem; it's the lesson. Let them argue, then apply the criterion.
- **Your craft:** in Variation C you're the judge panel — score arguments on risk reasoning, not rhetoric.

## 8. Running the Debrief (10 minutes, non-negotiable)

Three rounds, in order: **What happened?** (players narrate, you correct only facts) → **Why did it work that way?** (connect two or three key moments to real-world security — this is where you finally get to lecture, briefly) → **What would you do differently?** (go around the table; everyone answers). Losses debrief better than wins: read any unrevealed cards' "Why This Works" text aloud — it's the payoff for losing.

## 9. First Session? Do This

1. Run beginner **Incident Response** with the scripted opening in [How to Play §4](HOW_TO_PLAY.md) — your first two turns are literally written out
2. Keep the [tracker sheet](../cards/print-templates/tracker-sheets.md) visible to everyone; public state builds trust in your fairness
3. Log frictions on the [session notes form](playtesting/session-notes-form.md) — your confusion is playtest data too
4. Forgive yourself one rules mistake per session; announce it, fix it forward, don't replay
