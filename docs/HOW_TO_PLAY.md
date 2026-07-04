# How to Play Incident Zero

**Version:** 2.2 - Playtest Edition
**Read time: ~15 minutes. First game: ~45 minutes.**

This is the learn-to-play manual — read it once, run your first game, then use the [module rules](rules/core-rules.md) as reference during play. Exact tables and numbers live in the reference docs; this manual teaches the flow.

---

## 1. What Is This Game?

**Incident Zero** is a cybersecurity board game for classrooms and training rooms. One player is the **Threat Orchestrator (TO)** — part facilitator, part adversary, part narrator. Everyone else is the **Blue Team**: security defenders making decisions under budget and time pressure.

The game's signature rule: **you get better dice odds by explaining your reasoning like a real analyst.** Say "we investigate suspicious activity" and you roll flat. Say "we pull the mail gateway logs to check the sender's real IP against threat intel" and you roll at +3. Talking like a professional is literally how you win — that's the point.

There are **6 modules** covering the security lifecycle. Each is a standalone 30-45 minute game; they also chain together (the outcome of one feeds the setup of the next). This manual teaches **Incident Response** first — it's the flagship and the best hook.

## 2. What You Need

- **People:** 2-7 (1 TO + 1-6 defenders; 3-5 total is the sweet spot)
- **Dice:** one d20 (plus a d4 and d6 for advanced options)
- **Printed:** the [Tracker Sheets](../cards/print-templates/tracker-sheets.md), and the card deck for your module — for Incident Response that's the [Threat & Defense cards](../cards/incident-response/core-deck/threat-defense-cards.md) (see the [A4 Print Guide](../cards/print-templates/a4-layout-guide.md); index cards with titles written on them are fine for a first game)
- **Pencil** for the trackers

## 3. The Core Loop (all modules)

Every module runs on the same engine:

1. **Turns.** A fixed number of turns (announced at setup). Each turn: start-of-turn penalties → 2-3 minutes of team discussion → ONE team action → end of turn.
2. **Budget.** One shared pool representing money, staff, and time. Every action costs Budget. Run dry and you can't act.
3. **The d20 roll.** Uncertain actions need `roll + modifiers ≥ 11`.
4. **Justification modifiers.** **+2** for strong technical reasoning (methodology — *why* this approach works), **+1** for naming real tools or techniques (Wireshark, EDR, Mimikatz, a MITRE technique). The TO judges honestly; vague = +0.
5. **Debrief.** Every session ends with 5-10 minutes of "what happened, why, what would you do differently." This is where the learning locks in — don't skip it.

## 4. Your First Game: Incident Response (Beginner)

**The setup (TO does this privately, 5 min):** An attacker is inside the fictional company's network. The TO secretly builds a 3-card **attack chain** in kill-chain order and keeps it face-down:

> **Suggested first chain:** T-01 Phishing Campaign (INITIAL COMPROMISE / SOCIAL ENGINEERING) → T-04 Lateral Movement via SMB (PIVOT & ESCALATE / NETWORK) → T-07 Scheduled Task Persistence (PERSISTENCE / MALWARE)

- Turn limit: **(3 cards × 2) + 1 = 7 turns.** Announce it.
- Blue Team Budget: **100.** The team draws a shared hand of **5 Defense cards**.
- Blue Team wins by **revealing all 3 chain cards** (in order — you always work on the earliest unrevealed card) before turn 7 ends.

**The three actions (Blue Team picks ONE per turn):**

| Action | Cost | On success (roll+mods ≥ 11) |
|--------|------|------------------------------|
| **Investigate** | 5 | 1st success on a link = the TO gives a clue. 2nd success on the same link = **card revealed!** |
| **Deploy Defense** | 10/15/25 by tier | If the card's vector AND chain step match the hidden card = **revealed immediately.** Partial match = defense stays on the table and gives **+2** to future rolls against any link matching its vector |
| **Emergency Response** | 15 | No roll. Contain one already-revealed threat (removes its ongoing penalty) |

**The pressure (TO applies at the START of each turn):**
- **Active Breach Cost:** -5 Budget while *any* chain card is still unrevealed (the breach is burning money whether you see it or not)
- **Uncontained Threats:** -5 Budget per revealed-but-uncontained threat (revealing the *next* card in the chain auto-contains the previous one)

**When a card is revealed,** the team immediately picks ONE reward: draw 2 Defense cards, **+10 Budget**, or Fast-Track (next Investigate succeeds on 5+).

### Scripted opening — read this at the table

**TURN 1.** *TO:* "Start of turn: one attacker action is still hidden — Active Breach Cost, minus 5. Budget: 95. Something is wrong at Meridian Logistics: the helpdesk queue is full of password-reset complaints. What do you do?"
*Team (after discussion):* "Investigate. We pull the mail gateway logs and check sender domains against our threat-intel feed — if this is phishing, the return-path won't match the display name." *TO:* "That's a real methodology and a real tool — **+2 and +1.** Roll." *Rolls 9. 9+3 = 12 ≥ 11 — success.* *TO reads a clue from T-01:* "Several employees received emails claiming to be from IT, asking them to 're-authenticate'. The link goes to a look-alike domain registered 4 days ago." *(First success on this link — clue only. Budget: 95 - 5 = 90.)*

**TURN 2.** *TO:* "Active Breach Cost, minus 5. Budget: 85."
*Team:* "Keep digging on the phishing — we check the mail gateway for who *clicked*, and pull those workstations' proxy logs." *TO:* "+2, +1. Roll." *Rolls 10. 13 ≥ 11 — second success on the same link.* *TO flips T-01 face-up:* "**Phishing Campaign — revealed!** Three users entered credentials on the fake page. This threat is now uncontained. Choose a reward." *Team takes Budget Grant: 85 - 5 + 10 = 90.*

**TURN 3.** *TO:* "Two cards still hidden: Active Breach minus 5. One uncontained threat: minus 5. Budget: 80. You know how they got in — you don't yet know where they went."
*From here, you're on your own.* (A strong play: Deploy the Network Segmentation defense — if the next hidden card is network lateral movement, vector + step match reveals it instantly *and* auto-contains the phishing.)

### How it ends
- **All 3 cards revealed by end of turn 7** → win. Count remaining Budget for bragging rights.
- **Turn 7 ends with cards still hidden** → the attack completes. Read the unrevealed cards' "Why This Works" text aloud — that's the real lesson — and go to debrief. (Losses are teachable; the debrief is identical either way.)

**Debrief prompts:** What did you spend the most on, and was it worth it? Which clue actually changed your next decision? What one defense, bought before turn 1, would have changed everything?

## 5. The Other Five Modules (one paragraph each)

- **Network Building** — *before the attack.* Design a company network under a hard budget: which servers, which security devices, what architecture. Business Requirement and Operational Event cards stress the design. Teaches trade-offs — you can't afford everything, and the gaps you leave matter later.
- **Hardening** — *build defense-in-depth.* Deploy and upgrade layered defenses over 7 turns, then a **pentester attacks** (Pentester Tactic cards, each stating which defenses help). Teaches which control blunts which technique — and that signature antivirus won't save you.
- **Disaster Recovery** — *the breach happened.* A crisis-management exercise on an 8-turn clock: advance Investigation/Remediation/Communication tracks, keep five stakeholder trust meters alive, hit the GDPR 72-hour notification deadline, and face the ransom decision. The most "real tabletop exercise" module.
- **Forensics** — *after the fire is out.* Run investigations (disk, memory, logs, network, malware) to collect Evidence cards and push four meters: Attribution, Timeline, Attack Chain, Chain of Custody. Sloppy evidence handling costs you the case. Teaches actual forensic discipline.
- **Audit & Compliance** — *prove it.* Assess six security domains PASS/FAIL against real framework criteria (NIST CSF, CIS, PCI DSS). Or play **Variation C**, the debate format: argue risk acceptance vs. negligence in front of judges — the best large-group mode in the box.

**Chaining modules:** outcomes carry forward (audit gaps raise your DR costs; an IR loss sets up DR; IR's revealed chain seeds Forensics). See [Module Combinations](module-combinations.md). Full lifecycle = all six in sequence, 4-5 hours across sessions.

## 6. Where to Go Next

| You want... | Read |
|-------------|------|
| **You're the Threat Orchestrator** | [The TO Guide](TO_GUIDE.md) — the role, judging justifications, per-module screens |
| Exact rules for a module | [docs/rules/](rules/core-rules.md) — core + one file per module |
| Solo/standalone setup for any module | [docs/standalone-games/](standalone-games/incident-response.md) |
| Every card, indexed | [cards/CARD_REFERENCE.md](../cards/CARD_REFERENCE.md) |
| To run a playtest and report back | [docs/playtesting/](playtesting/README.md) |
| Variable game length & difficulty tiers | [core-rules §3a](rules/core-rules.md) |

## 7. Quick Reference (photocopy this)

**Roll:** d20 + modifiers ≥ 11 · **+2** strong justification · **+1** real tool/technique named · **+2** matching deployed defense (IR)
**IR costs:** Investigate 5 · Deploy 10/15/25 · Emergency Response 15
**IR start-of-turn:** -5 while any card hidden · -5 per uncontained revealed threat
**Reveal:** 2 successful Investigates on a link, or 1 full-match Deploy (vector + step) · always the earliest unrevealed card
**Reward per reveal (pick 1):** 2 Defense cards / +10 Budget / next Investigate succeeds on 5+
**Turn limit:** (chain cards × 2) + 1 → 3 cards = 7 turns
**Budgets:** NB 40-60 · DR 50 · Forensics 75 · IR 100 · Audit 100 · Hardening 150
