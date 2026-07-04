# Disaster Recovery Module: Event Timeline Cards

**Version:** 2.2 - Playtest Edition
**Last Updated:** October 2025

---

## Overview

**Event Cards** represent external events that occur during the crisis—some predictable deadlines, some escalations triggered by the team's situation. Events create time pressure and complicate the response.

- **Total Cards:** 12 (EVENT-01 to EVENT-12)
- **Used In:** Disaster Recovery module
- **Types (v2.2):** 6 **Scheduled** events (placed on the timeline at setup) + 6 **Triggered** events (resolve when their stated condition is met)
- **Purpose:** Create time pressure and complicate decision-making

**Money mapping:** 1 Budget ≈ $50K. Dollar figures are narrative unless converted to Budget on the card.

---

## The Crisis Clock (v2.2)

The game lasts **8 turns**. Each turn is one crisis phase of roughly 6-12 hours of narrative time:

| Turn | Narrative Time | Anchor |
|------|----------------|--------|
| 1 | Detection +6h | Internal discovery |
| 2 | +12h | Legal/executive escalation complete |
| 3 | +18h | Board meets |
| 4 | +24h | Day 1 ends |
| 5 | +36h | Customer notification recommended deadline; default ransom deadline |
| 6 | +48h | Regulatory escalation begins |
| 7 | +60h | Legal/government pressure peaks |
| 8 | +72h | **GDPR 72-hour regulatory notification deadline** — game ends |

All deadlines in this module use this clock. There are no other timers.

---

## Event Deck Procedure (v2.2)

**At setup:**
1. Place the 6 **Scheduled** events face-down on the timeline at their printed turns.
2. Place the 6 **Triggered** events face-up in a reference row where everyone can read their trigger conditions.

**Each turn (start of turn):**
1. Reveal and resolve any Scheduled event placed on this turn.
2. Check every un-fired Triggered event's condition; resolve any whose condition is now met.
3. Each event fires **once per game**.

Trust changes from events clamp to 0-100%. Budget changes clamp to a floor of 0.

---

## Scheduled Events

### EVENT-01: First Media Coverage
**Scheduled:** Turn 2
**Type:** Discovery

**Description:**
A news outlet publishes a story about the breach:
- "Company Suffers Data Breach" headline
- Unnamed source gives details
- Story spreads on social media
- Phone starts ringing with reporter calls

**Resolution:**
- If ACTION-11 (Media Management) was completed before this turn: Media trust +5 (proactive framing works)
- Otherwise: Media trust -10 (the story runs without your side)

**Duration:** Ongoing narrative (media coverage continues)

---

### EVENT-04: Board Meeting
**Scheduled:** Turn 3
**Type:** Governance

**Description:**
The board of directors holds an emergency meeting to review breach scope, investigation progress, remediation plan, budget, and executive performance.

**Resolution:**
- If ACTION-12 (Board Communication) was completed before this turn: Board trust +10 (prepared briefing)
- Otherwise: Board trust -20 (the board learns details from the news, not from you)

**Team Preparation:**
- Should have forensics/investigation underway
- Should have preliminary findings
- Should have a communication plan
- CEO should be briefed

---

### EVENT-03: Customer Notification Window
**Scheduled:** Turn 5
**Type:** Deadline checkpoint

**Description:**
Counsel confirms customer notification should not wait any longer. Real-world laws require notification "without unreasonable delay" — in this game, the recommended deadline is **end of Turn 5**.

**Resolution:**
- If ACTION-09 (Customer Notification) is completed by end of Turn 5: no penalty. If it was framed transparently, +5 Reputation at final scoring.
- If not: Customer trust -10 now and at the start of each later turn until ACTION-09 is completed.
- **Deferred consequence:** if customers are never notified in-game, -15 Reputation at final scoring (the statutory notification window is missed after the game ends).

---

### EVENT-09: Shareholder Pressure
**Scheduled:** Turn 5 (public companies only — skip for private companies)
**Type:** Governance

**Description:**
Shareholder activists contact the board: demand explanations, threaten a proxy fight, and give interviews about leadership failure.

**Resolution:**
- If ACTION-12 (Board Communication) has been completed: Board trust -5 (pressure is absorbed)
- Otherwise: Board trust -15

---

### EVENT-02: Regulatory 72-Hour Deadline
**Scheduled:** Turn 6 (escalation begins; final deadline end of Turn 8)
**Type:** Deadline

**Description:**
The GDPR-style 72-hour clock is running out. Regulators expect notification of the breach (ACTION-10) before the clock expires at end of Turn 8.

**Resolution:**
- If ACTION-10 (Regulatory Notification) is already completed: Regulator trust +5 (early, cooperative notification)
- If not: Regulator trust **-10 now and at the start of each later turn** (Turns 6, 7, 8) until ACTION-10 is completed.
- **Deferred consequence:** if regulators are never notified in-game, -20 Reputation at final scoring (deferred fine — GDPR fines run up to €20M or 4% of global turnover, whichever is HIGHER; narrative-only figure).

---

### EVENT-12: Government Subpoena
**Scheduled:** Turn 7 (medium/large breaches — skip for small-scope games)
**Type:** Legal

**Description:**
A subpoena arrives (FBI, state attorney general, or a congressional inquiry): turn over evidence, provide executive testimony, comply with the investigation.

**Resolution:**
- Budget -5 (legal fees; floor 0)
- Executive trust -10 (executives in the spotlight)
- Investigation +5% (compelled evidence-sharing accelerates fact-finding)

**Opportunity:** an independent investigation can validate a good-faith response; law enforcement may help recover evidence.

---

## Triggered Events

### EVENT-05: Customer Class Action Lawsuit
**Trigger:** ACTION-09 not completed by end of Turn 5, OR Customer trust below 20% at the start of any turn.
**Type:** Legal

**Description:**
A law firm recruits customers and files a class action: "Jane Doe et al. vs. [Company Name]" — failure to protect data, failure to notify in a timely way, damages plus attorney fees.

**Effects:**
- Customer trust -15
- Board trust -10
- **-10 Reputation at final scoring**

**Team Response:** Cannot be undone — only mitigated by rebuilding trust for the rest of the game.

---

### EVENT-06: Regulatory Fine
**Trigger:** Regulator trust below 20% at the start of any turn. (If regulators are never notified in-game, the deferred -20 Reputation from EVENT-02 applies at scoring instead — do not double-apply.)
**Type:** Regulatory

**Description:**
A regulator announces a penalty for inadequate security and delayed cooperation.

**Effects:**
- Budget -10 (≈ $500K; floor 0)
- Board trust -10
- **-10 Reputation at final scoring**

**Real-world scale (narrative-only):** turnover-based regimes drive the largest penalties — GDPR fines can reach €20M or 4% of global turnover, whichever is HIGHER.

---

### EVENT-07: Media Frenzy
**Trigger:** Media trust below 20% at the start of any turn, OR no Communication-category action completed by end of Turn 3.
**Type:** Communication

**Description:**
Major outlets pick up the story: national coverage, "Massive Data Breach" headlines, social media amplification.

**Effects:**
- Media trust -20
- Customer trust -15
- Board trust -10

**Team Response:** ACTION-11 (Media Management) plus visible, transparent leadership.

---

### EVENT-08: Second Breach Discovered
**Trigger:** At the start of Turn 6, Remediation is below 30% AND ACTION-07 (Rebuild) has not been completed.
**Type:** Escalation — **once per game**

**Description:**
While responding to the first breach, investigators discover another compromised data store — the attacker maintained hidden persistence.

**Effects:**
- **The game extends by +2 turns (once per game): play now runs to Turn 10.** Scoring deadlines do NOT move — the regulatory deadline remains end of Turn 8.
- Investigation -30% (new breach invalidates part of your picture)
- Customer trust -20, Regulator trust -15, Media trust -10, Board trust -15
- Board releases +10 emergency Budget
- **-10 Reputation at final scoring**

**Prevention:** ACTION-07 (Rebuild), ACTION-04 (Third-Party IR), or strong Remediation progress by Turn 6.

---

### EVENT-10: Competitor Advantage
**Trigger:** Customer trust below 40% at the start of Turn 5 or any later turn.
**Type:** Business

**Description:**
A competitor launches a "Trust us with your data" campaign aimed at your customers.

**Effects:**
- Customer trust -10
- Budget -5 (lost revenue; floor 0)

**Team Response:** Customer communication and visible security improvements; trust can rebuild over the remaining turns.

---

### EVENT-11: Key Executive Resignation
**Trigger:** Executive trust below 30% at the start of any turn.
**Type:** Internal

**Description:**
A key executive (CISO, CTO, General Counsel, or CFO) resigns mid-crisis, citing "personal reasons" — really: "I don't trust this response."

**Effects:**
- Executive trust -10
- Board trust -10
- While Executive trust remains below 30%, the Justification bonus (optional +5% d20) is unavailable — leadership vacuum

**Prevention:** Regular internal communication, visible progress, board support.

---

## Event Deck Summary (v2.2)

| Event | Kind | Turn / Trigger | Core Effect |
|-------|------|----------------|-------------|
| EVENT-01 First Media Coverage | Scheduled | Turn 2 | Media +5 if ACTION-11 done, else -10 |
| EVENT-04 Board Meeting | Scheduled | Turn 3 | Board +10 if ACTION-12 done, else -20 |
| EVENT-03 Customer Notification Window | Scheduled | Turn 5 | -10 Customer/turn if ACTION-09 late; never = -15 Rep |
| EVENT-09 Shareholder Pressure | Scheduled | Turn 5 (public co.) | Board -5 (prepared) or -15 |
| EVENT-02 Regulatory 72h Deadline | Scheduled | Turn 6 (deadline Turn 8) | -10 Regulator/turn while un-notified; never = -20 Rep |
| EVENT-12 Government Subpoena | Scheduled | Turn 7 (med/large) | Budget -5, Exec -10, Investigation +5% |
| EVENT-05 Class Action | Triggered | Customers un-notified after T5 or trust <20% | Cust -15, Board -10, -10 Rep |
| EVENT-06 Regulatory Fine | Triggered | Regulator trust <20% | Budget -10, Board -10, -10 Rep |
| EVENT-07 Media Frenzy | Triggered | Media <20% or silent through T3 | Media -20, Cust -15, Board -10 |
| EVENT-08 Second Breach | Triggered | T6: Remediation <30%, no rebuild | +2 turns (once), Inv -30%, trust hits, -10 Rep |
| EVENT-10 Competitor Advantage | Triggered | Customer trust <40% from T5 | Cust -10, Budget -5 |
| EVENT-11 Executive Resignation | Triggered | Executive trust <30% | Exec -10, Board -10, no Justification bonus |

---

## Deadline Summary (v2.2 — the only clock)

| Deadline | Turn | If missed |
|----------|------|-----------|
| Internal legal/executive escalation | End of Turn 2 | Narrative only (relabeled from the old "12-hour regulatory deadline" — the regulatory anchor is GDPR 72h) |
| Customer notification (ACTION-09) recommended | End of Turn 5 | Customer trust -10/turn; EVENT-05 may trigger; never notified = -15 Reputation at scoring |
| Ransom decision (ACTION-13) | Start of Turn 5 (default; +2 turns if NEGOTIATE) | Treated as REFUSE; data-publication event fires |
| Regulatory notification (ACTION-10) | End of Turn 8 (escalating from Turn 6) | Regulator trust -10/turn from Turn 6; never notified = -20 Reputation at scoring |

Former "30-day"/"60-day" deadlines from v2.1 are re-expressed as the deferred final-scoring consequences above — they no longer exist as separate timers.

---

## Turn Sequence with Events (reference)

**Standard 8-Turn Disaster Recovery Game:**

| Turn | Scheduled Event | Typical Focus |
|------|-----------------|---------------|
| 1 | — | Investigate, contain |
| 2 | First Media Coverage | Investigation, media prep |
| 3 | Board Meeting | Board briefed, regulators notified early |
| 4 | — | Remediation |
| 5 | Customer Notification Window + Shareholder Pressure | Customer notification, ransom decision |
| 6 | Regulatory 72h Deadline (escalation begins) | Regulators notified (if not already), remediation |
| 7 | Government Subpoena | Final remediation, communication |
| 8 | — (game ends at +72h) | Wrap-up actions, final scoring |

---

## Gameplay Strategy

### Early Game (Turns 1-3)
- Focus on Investigation (need facts before remediation)
- Brief the board before EVENT-04 (Turn 3)
- Consider early regulator notification (bonus at EVENT-02)
- Manage media (prevent EVENT-07)

### Mid Game (Turns 4-6)
- Notify customers by end of Turn 5
- Make the ransom decision before its deadline
- Push Remediation to 30% or higher before Turn 6 (prevents EVENT-08)

### Late Game (Turns 7-8)
- Complete regulatory notification by end of Turn 8 at the latest
- Finish remediation, stabilize trust meters
- Spend remaining budget where a track is weakest

---

## Print Instructions

1. Print on cardstock (250 gsm minimum)
2. Color-code by event kind:
   - **Blue (Scheduled):** EVENT-01, EVENT-02, EVENT-03, EVENT-04, EVENT-09, EVENT-12
   - **Orange (Triggered):** EVENT-05, EVENT-06, EVENT-07, EVENT-08, EVENT-10, EVENT-11
3. Print the scheduled turn (or trigger condition) prominently on each card
4. Include consequences clearly
5. Cut along dotted lines
6. Event timeline mat: see print pack (coming)

---

*Disaster Recovery Module: Event Timeline Cards*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.2 - Playtest Edition*
