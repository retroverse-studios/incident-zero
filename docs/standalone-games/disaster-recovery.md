# Disaster Recovery Module: Standalone Play Guide

**Version:** 2.2 - Playtest Edition
**Duration:** 30-45 minutes
**Players:** 1 Threat Orchestrator + 2-4 Blue Team members
**Best For:** Crisis management training, incident response procedures, stakeholder communication

> **v2.2:** the card system is canonical. You play the 13 Crisis Action cards against the 12 Event cards while managing 5 Stakeholder trust meters, over one 8-turn clock. Track advances are deterministic; dice appear only in the optional Justification bonus and ACTION-13's "no guarantee" roll. This guide uses the exact same rules, numbers, and tier table as `docs/rules/module-disaster-recovery.md`.

---

## Module Overview

The **Disaster Recovery Module** teaches players how to **manage a real breach** — investigation, remediation, stakeholder communication, and the ransom decision — under extreme time and budget pressure.

Players balance three progress tracks (Investigation %, Remediation %, Communication %) and five stakeholder trust meters while an event timeline turns up the heat. At the end, a single Reputation score (0-100) is computed from what they achieved.

---

## What You Need

From `cards/disaster-recovery/`:
- 13 Crisis Action cards (ACTION-01 to ACTION-13)
- 12 Event cards (6 Scheduled + 6 Triggered)
- 5 Stakeholder cards (trust meters)
- A d20, and paper for the tracks/trust/budget (tracker sheets: see print pack, coming)

**Money mapping:** 1 Budget ≈ $50K.

---

## Setup (5 minutes)

### 1. Set the Crisis Scenario

**The breach has already succeeded.** The Threat Orchestrator reveals the full attack chain:

> "Your organization has experienced a significant data breach. Here's what happened:
>
> **Attack Chain:**
> 1. Phishing Campaign → Employee clicked malicious link
> 2. Credential Harvesting → Login credentials captured
> 3. VPN Access → Attacker gained network access
> 4. Lateral Movement → Access to production servers
> 5. Database Exfiltration → 500,000+ customer records stolen
>
> **Current Status:**
> - Breach detected; the crisis clock starts now
> - Attacker demanding $1M ransom (= 20 Budget) or they publish the data
> - Media starting to ask questions
> - You have 8 turns (72 narrative hours) to respond
>
> **Your Challenge:**
> Investigate the breach, remediate it, and communicate with stakeholders — before the deadlines land."

### 2. Blue Team Setup

- **Budget:** 50 (emergency crisis fund; floor 0 — the free Holding Statement is always available)
- **Progress tracks:** Investigation 0%, Remediation 0%, Communication 0%
- **Stakeholder trust:** Customers 50%, Regulators 60%, Media 40%, Board 70%, Executives 80% (clamp 0-100%)
- **Reputation is not tracked during play** — it is computed once at game end (see Scoring)

### 3. Build the Event Timeline (place on table)

| Turn | Time | Scheduled Event / Deadline |
|------|------|----------------------------|
| 1 | +6h | Internal discovery |
| 2 | +12h | EVENT-01 First Media Coverage; internal legal/executive escalation complete (narrative) |
| 3 | +18h | EVENT-04 Board Meeting |
| 4 | +24h | — |
| 5 | +36h | EVENT-03 Customer Notification Window (**ACTION-09 recommended by end of this turn**); EVENT-09 Shareholder Pressure (public companies); **default ransom deadline (ACTION-13)** |
| 6 | +48h | EVENT-02 Regulatory 72h Deadline — escalation begins (-10 Regulator trust per un-notified turn) |
| 7 | +60h | EVENT-12 Government Subpoena (medium/large breaches) |
| 8 | +72h | **GDPR 72-hour deadline: ACTION-10 must be complete. Game ends.** |

Lay the 6 Triggered events (EVENT-05, -06, -07, -08, -10, -11) face-up where their trigger conditions can be read. Each fires once, when its condition is met.

### 4. Optional Difficulty Variant: Scope-Scaled Start (clearly optional)

Default: the final Reputation computation starts at 100. For harder games:

| Scope | Records | Start computation at |
|-------|---------|----------------------|
| Small (Beginner) | ~50K | 100 (default) |
| Medium (Intermediate) | ~500K | 90 |
| Large (Advanced) | 5M+ | 80 |

---

## Gameplay Loop (25-35 minutes)

### Turn Sequence

**1. START OF TURN**
- Complete any in-flight multi-turn action that finishes now (apply its track advance)
- Resolve this turn's Scheduled event; check all un-fired Triggered events
- Apply decay/deadline penalties (Customer decay from Turn 3 if no communication yet; Regulator -10/turn from Turn 6 if un-notified)
- Announce remaining Budget, tracks, and trust meters

**2. BLUE TEAM'S TURN (2-3 minutes discussion)**
- Play **ONE** Crisis Action card: pay its cost, apply its track advance — **or** take the free **Holding Statement** (0 Budget, +5% Communication)
- **Multi-turn actions (Duration N):** occupy the action slot only on the turn started; the advance completes at the start of the Nth following turn; one in flight at a time
- **Justification bonus (optional):** strong, specific technical justification → roll d20; on 11+ that action's advance gains +5%
- **ACTION-13 Ransom Decision** may be declared at any time before the ransom deadline; it does not use the action slot (once per game)

**3. APPLY STAKEHOLDER EFFECTS**
- Apply the action's trust effects (table below)

**4. END OF TURN**
- **Any stakeholder trust at 0% = immediate loss ("the company collapses")**
- Advance the turn counter; the game ends after Turn 8 (Turn 10 if EVENT-08 fired)

### Crisis Action Quick Reference (identical to the cards)

| Card | Category | Cost | Advance | Duration | Trust effects |
|------|----------|------|---------|----------|---------------|
| ACTION-01 Forensic Analysis | Investigation | 12 | +25% Inv | 2 turns | Regulators +10, Board +5 |
| ACTION-02 Threat Hunting | Investigation | 8 | +15% Inv | 1 turn | — |
| ACTION-03 Log Analysis | Investigation | 5 | +10% Inv | 1 turn | — |
| ACTION-04 Third-Party IR | Investigation | 20 | +30% Inv, +20% Rem | 3 turns | Regulators +15, Board +15 |
| ACTION-05 Patch & Harden | Remediation | 10 | +20% Rem | 1 turn | Executives +5 |
| ACTION-06 Containment | Remediation | 8 | +15% Rem | 1 turn | Executives +5 |
| ACTION-07 Rebuild from Backup | Remediation | 15 | +25% Rem | 2 turns | Exec +5, Cust +5, Board +5 |
| ACTION-08 Credential Reset | Remediation | 6 | +12% Rem | 1 turn | Executives +5 |
| ACTION-09 Customer Notification | Communication | 10 | +20% Comm | 1 turn | Customers +15, Media +5 |
| ACTION-10 Regulatory Notification | Communication | 8 | +10% Comm | 1 turn | Regulators +20 |
| ACTION-11 Media Management | Communication | 12 | +15% Comm | 1 turn | Media +20, Customers +10 |
| ACTION-12 Board Communication | Communication | 9 | +12% Comm | 1 turn | Board +20, Executives +5 |
| ACTION-13 Ransom Decision | Crisis Decision | 0/5/20 | Pay: +20% Rem | Instant | — (scoring only) |
| *Holding Statement (free rule)* | Communication | 0 | +5% Comm | 1 turn | — (stops Customer decay) |

---

## The Ransom Decision (ACTION-13)

Declare before the ransom deadline (default: start of Turn 5). One option, once per game:

- **PAY — 20 Budget (≈ $1M):** -15 Reputation at scoring. Data-publication event skipped/cancelled; +20% Remediation immediately. **No guarantee:** TO rolls d20 — on 1-5 the keys don't work (no refund, +0% Remediation; publication stays cancelled).
- **NEGOTIATE — 5 Budget:** -5 Reputation at scoring. Data-publication event delayed 2 turns (default: to start of Turn 7).
- **REFUSE — 0 Budget:** no immediate change; **if the data-publication event triggers later, -20 Reputation at scoring.** No decision by the deadline = REFUSE.

**Data-publication event:** if the team has not PAID by the (possibly delayed) deadline: Customer trust -20, Media trust -15, plus the REFUSE penalty if applicable.

**Facts:** payment may violate OFAC sanctions if the actor is sanctioned; many insurers restrict or exclude ransom coverage; the FBI discourages payment; payment guarantees nothing.

---

## Deadline Management (the only clock)

- **End of Turn 5 — Customer notification recommended (ACTION-09).** Miss it: Customer trust -10 per later turn; EVENT-05 Class Action may trigger; never notified = -15 Reputation at scoring.
- **Start of Turn 5 — Ransom decision (ACTION-13)** (+2 turns if NEGOTIATE). No decision = REFUSE.
- **Turn 6 onward — Regulatory escalation:** -10 Regulator trust per turn while un-notified.
- **End of Turn 8 — GDPR 72-hour deadline (ACTION-10).** Never notified = -20 Reputation at scoring (deferred fine — GDPR fines run to €20M or 4% of global turnover, whichever is higher; narrative-only).

---

## Scoring & Final Reputation (identical to the module rules)

At game end, compute Reputation:

```
FINAL REPUTATION = 100 (or 90/80 with the scope variant), then apply:

1. TRACK RESULTS (per track: Investigation, Remediation, Communication)
   50-100% -> -0    |  25-49% -> -5   |  10-24% -> -10  |  0-9% -> -20

2. STAKEHOLDER TRUST (average of the five meters)
   70%+ -> +5  |  50-69% -> 0  |  30-49% -> -10  |  below 30% -> -20

3. DECISION & EVENT MODIFIERS (each at most once)
   +5   Customers notified transparently by end of Turn 5
   +3   per quality investigation completed (ACTION-01 or ACTION-04), MAX +6 per game
   -5 / -15 / -20   ACTION-13: Negotiate / Pay / Refuse-and-published
   -10  each: EVENT-05 Class Action, EVENT-06 Regulatory Fine, EVENT-08 Second Breach
   -15  customers never notified in-game
   -20  regulators never notified in-game

4. CLAMP to 0-100.
```

**Worked example:** see the module rules (`docs/rules/module-disaster-recovery.md`) — a 50-Budget team runs ACTION-02, -06, -10, NEGOTIATE, -05, -09 plus Holding Statements and finishes Inv 25 / Rem 35 / Comm 45, trust average 54 → Reputation 85.

### Outcome Tiers (v2.2 — the ONE tier table)

| Final Reputation | Outcome | Interpretation |
|------------------|---------|----------------|
| **85-100** | Exemplary | Crisis well-managed; stakeholder trust preserved; the organization recovers |
| **70-84** | Managed | Adequate response; some damage; recovery likely |
| **55-69** | Damaged | Poor response; significant customer loss; regulatory scrutiny; recovery uncertain |
| **40-54** | Mismanaged | Major reputational/financial damage; leadership changes likely |
| **Below 40** | Catastrophic | Company survival in question; CEO likely replaced |

**Loss precedence:** (1) any stakeholder trust at 0% at any point = immediate loss; (2) otherwise, the tier table above. Below-20% trust is a critical *warning state* only.

---

## Debrief & Reflection (5-10 minutes)

**PART 1: INVESTIGATION QUALITY (2 min)**
1. "Did you investigate adequately? What's the total impact?"
2. "What important information did you miss?"
3. "Would better forensics have changed your decisions?"

**PART 2: COMMUNICATION STRATEGY (2 min)**
1. "How did you prioritize stakeholder notifications?"
2. "What would you communicate differently?"
3. "Did transparency help or hurt your reputation?"

**PART 3: FINANCIAL DECISIONS (2 min)**
1. "Did you pay the ransom? Why or why not?"
2. "What was your total incident cost (Budget spent × $50K, plus deferred penalties)?"
3. "Would different decisions have saved money?"

**PART 4: RESPONSE QUALITY (2 min)**
1. "If you replayed, what would you do first?"
2. "Which stakeholder relationship was hardest to preserve?"
3. "What was your biggest crisis decision?"

**PART 5: REAL-WORLD CONNECTION (2 min)**
1. "Compare your spending to actual breaches (Target, Equifax, etc.)"
2. "What's harder: prevention or response?"
3. "Why is it so expensive to manage a real breach?"

---

## Tips for Threat Orchestrators

### Breach Scenario Variations

**Small Breach (Beginner)** — 50,000 records, opportunistic attacker, no subpoena (skip EVENT-12), total real-world loss ~$1-5M (narrative).

**Medium Breach (Intermediate)** — 500,000 records, ransom-seeking criminal group, full event timeline, total loss ~$5-50M (narrative).

**Large Breach (Advanced)** — 5M+ records, sophisticated attacker, use the scope variant (start computation at 80), total loss ~$50M+ (narrative).

### Pressure Escalation

- **Turns 1-2:** discovery, media first contact
- **Turn 3:** board meeting — reward preparation
- **Turns 4-5:** customer notification window + ransom deadline converge
- **Turns 6-7:** regulatory escalation, publication fallout, subpoena
- **Turn 8:** final reckoning

### Decision Consequences

- **Transparent vs. evasive:** early transparency protects trust; silence triggers EVENT-07 and decays Customers
- **Thorough vs. quick investigation:** ACTION-01/04 cost turns and budget but add the forensic scoring bonus and regulator trust
- **Remediation timing:** below 30% Remediation at Turn 6 risks EVENT-08 (second breach, +2 turns of pain)
- **Ransom:** paying trades Reputation for certainty; negotiating buys time; refusing gambles on the publication fallout

---

## Sample Scenarios to Try

### Scenario 1: "Credential Breach" (Small, Beginner)
**Scope:** 50,000 customer passwords exposed. **Attacker:** opportunistic; ransom demand small — try REFUSE and manage the fallout. **Budget:** 50.
**Focus:** communicating bad news without panic. **Lesson:** even small breaches require careful stakeholder management.

### Scenario 2: "Supply Chain Breach" (Medium, Intermediate)
**Scope:** 500,000 records via a compromised vendor. **Budget:** 50 (+ any carried over from prior modules).
**Focus:** ACTION-04 Third-Party IR shines here; multi-stakeholder communication. **Lesson:** vendor relationships complicate crisis response.

### Scenario 3: "Nation-State Attack" (Large, Advanced)
**Scope:** 5M+ records; attacker won't negotiate (ACTION-13 offers REFUSE only). Use the scope variant (start at 80).
**Focus:** damage control; accept a "Damaged" tier as a good result. **Lesson:** some breaches are unwinnable; response quality still matters.

---

## Extensions & Variations

### Extended Crisis Mode (60 minutes)
- Pre-arm EVENT-08 (the second breach fires automatically at Turn 6): 10 turns total
- Budget: 60
- More complex stakeholder negotiations

### Litigation Track
- Track lawsuit exposure narratively: evidence preserved (ACTION-01/04 completed) reduces it; EVENT-05 raises it
- Discuss settlement costs in the debrief

### Competitive Breach Response
- Multiple teams respond to the same breach with separate boards
- Highest final Reputation wins

---

## Next Steps After This Module

**If you scored 70+ (Managed or better):**
- Continue to **Audit & Compliance Module** → validate response procedures post-breach
- Transition to **Hardening Module** → prevent similar breaches

**If you scored below 70:**
- Discuss what went wrong
- Replay the scenario with different decisions
- Study real breach case studies (Target, Equifax, SolarWinds)

**Standalone:** play again with a different breach type or attacker profile

---

## Need Help?

- **Questions about rules?** See [Core Rules](../rules/core-rules.md) and [Module Rules](../rules/module-disaster-recovery.md)
- **The cards themselves?** See `cards/disaster-recovery/`
- **Want to combine modules?** See [Module Combinations](../module-combinations.md)
- **Understanding timing?** See [FRAMEWORK.md](../FRAMEWORK.md)

---

*Disaster Recovery Module - Standalone Play Guide*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.2 - Playtest Edition*
