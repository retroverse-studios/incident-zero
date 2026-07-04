# Disaster Recovery Module: Rules & Mechanics

**Version:** 2.2 - Playtest Edition
**Last Updated:** October 2025

> **v2.2:** the card system is canonical. The Disaster Recovery game is played with 12 Crisis Action cards (plus ACTION-13), 12 Event cards, and 5 Stakeholder cards. Track advances are deterministic — dice are used only for the optional Justification bonus and ACTION-13's "no guarantee" roll. See `cards/disaster-recovery/` for the cards themselves and **v2.2 Playtest Edition Changes** at the bottom of this document for what changed.

---

## Module Overview

The **Disaster Recovery Module** teaches crisis management and breach response when incident detection fails. This module is typically entered after losing an Incident Response module (representing an undetected or uncontained breach) but can also be played standalone to teach DR concepts.

This is not a "second chance" to solve the attack chain. Instead, it simulates the real-world consequences of a successful breach:
- **Crisis management** under pressure
- **Stakeholder communication** (board, customers, regulators)
- **Forensic investigation** with limited budget
- **Public disclosure** and legal requirements
- **Incident containment** and damage assessment
- **Financial impact** and recovery costs

### Educational Purpose

**Incident Response:** Teaches proactive threat detection and investigation
**Hardening (typically after an IR win):** Teaches proactive defense and resilience
**Disaster Recovery (typically after an IR loss):** Teaches crisis management, consequences, and recovery

---

## Components (v2.2)

| Component | Count | Purpose |
|-----------|-------|---------|
| Crisis Action cards (ACTION-01 to ACTION-13) | 13 | The actions teams play each turn |
| Event cards (EVENT-01 to EVENT-12) | 12 | 6 Scheduled + 6 Triggered pressure events |
| Stakeholder cards (STAKE-01 to STAKE-05) | 5 | Five trust meters (0-100%) |
| Progress tracks | 3 | Investigation %, Remediation %, Communication % (0-100%) |
| d20 | 1 | Optional Justification bonus; ACTION-13 "no guarantee" roll |
| Track/trust sheets | — | See print pack (coming) — a piece of paper works fine |

**Money mapping:** 1 Budget ≈ $50K. All dollar figures (fines, ransoms) use this mapping unless marked narrative-only.

---

## Entering the DR Phase

### Prerequisites for DR Phase

**Trigger:** Team lost the Incident Response module by either:
- Reaching Turn 10 with unrevealed cards remaining, OR
- Running out of Budget (reaching 0)

**Outcome:** The attack chain proceeded undetected. The threat actor succeeded.

*(Standalone play: skip Incident Response and start here — see the standalone guide.)*

### Discovery & Revelation

The Threat Orchestrator **reveals the entire unrevealed attack chain** to the Blue Team:
- All hidden Threat cards are shown
- The complete attack progression is explained
- The attacker's objectives are stated

**Example Revelation:**
"Your security team was unable to detect the attack in time. The attacker successfully:
1. Sent a phishing email (SOCIAL ENGINEERING)
2. Harvested credentials (CREDENTIAL ABUSE)
3. Moved laterally across your network (NETWORK)
4. Dumped admin credentials (CREDENTIAL ABUSE)
5. Exfiltrated your entire customer database (DATA EXFIL)

The attacker is now threatening to publish the data unless you pay $1M (20 Budget). You have 72 hours before regulators must be notified."

---

## Setup (v2.2)

1. **Establish DR Budget:**
   - Starting DR Budget = **50** (flat crisis allocation — insurance, emergency funds)
   - If entering from Incident Response: add any remaining IR budget (operational reserves)
   - If an Audit was played earlier: subtract audit gap penalties (total capped at -30 — see module-audit-compliance.md)
   - **Budget floor is 0.** Budget can never go negative; the free Holding Statement action is always available.

2. **Set the three progress tracks to 0%:** Investigation, Remediation, Communication.

3. **Set the five stakeholder trust meters to their starting values:** Customers 50%, Regulators 60%, Media 40%, Board 70%, Executives 80%. Meters clamp to 0-100%.

4. **Build the Event Timeline:** place the 6 Scheduled events on their turns (EVENT-01 Turn 2, EVENT-04 Turn 3, EVENT-03 + EVENT-09 Turn 5, EVENT-02 Turn 6, EVENT-12 Turn 7). Lay the 6 Triggered events face-up where their conditions can be read.

5. **Ransom scenarios:** note the ransom deadline (default: start of Turn 5) and put ACTION-13 where the team can see it.

6. **Reputation is NOT tracked during play.** It is **computed once, at game end** (see Final Scoring). During play, the three tracks and five trust meters are the whole state.

---

## The Crisis Clock (v2.2) — ONE clock

The game lasts **8 turns**. Each turn is one crisis phase of ~6-12 hours of narrative time:

| Turn | Narrative Time | Key Deadline |
|------|----------------|--------------|
| 1 | Detection +6h | Internal discovery |
| 2 | +12h | Internal legal/executive escalation complete (narrative; this was mislabeled a "regulatory deadline" in v2.1 — the regulatory anchor is GDPR 72h) |
| 3 | +18h | Board Meeting (EVENT-04) |
| 4 | +24h | Day 1 ends |
| 5 | +36h | **Customer notification recommended (ACTION-09)**; default ransom deadline (ACTION-13) |
| 6 | +48h | Regulatory escalation begins (EVENT-02): -10 Regulator trust per un-notified turn |
| 7 | +60h | Government subpoena (EVENT-12) |
| 8 | +72h | **GDPR 72-hour deadline: ACTION-10 must be complete. Game ends.** |

All deadlines on every card use this clock. There are no 12-hour, 24-hour, 30-day, or 60-day timers anymore; the former 30/60-day deadlines are deferred final-scoring consequences (see Final Scoring).

*(Exception: EVENT-08 Second Breach extends play to Turn 10, once per game. Scoring deadlines do not move.)*

---

## Turn Sequence (v2.2)

Each turn:

**1. START OF TURN**
- Complete any in-flight multi-turn action that finishes now (apply its track advance)
- Reveal and resolve this turn's Scheduled event
- Check all un-fired Triggered events; resolve any whose condition is met
- Apply decay/deadline penalties (e.g., Customer decay, Regulator -10/turn from Turn 6 if un-notified)

**2. TEAM ACTION (2-3 minutes discussion)**
- Play **ONE** Crisis Action card: pay its Budget cost, apply its track advance
  - **Multi-turn actions (Duration N):** the card occupies your action slot only on the turn started; its advance completes at the start of the Nth following turn. Only one multi-turn action in flight at a time.
  - **Or** take the free **Holding Statement** (0 Budget, +5% Communication; always available, counts as a Communication action for decay purposes)
- **Optional Justification bonus (v2.2):** if the team gives a strong, specific technical justification for the action, the TO may allow a d20 roll — on 11+, that action's track advance gains +5%. This is the only d20 in track advancement, and it is a bonus, never a gate.
- **ACTION-13 (Ransom Decision)** may be declared at any time before the ransom deadline; it does not use the action slot and happens once per game.

**3. APPLY STAKEHOLDER EFFECTS**
- Apply the played action's trust effects (table below)

**4. END OF TURN**
- Check the loss condition: **any stakeholder trust at 0% = immediate loss ("the company collapses")**
- Advance the turn counter

### Action → Trust Effects (v2.2 canonical table)

| Action | Trust effects when completed |
|--------|------------------------------|
| ACTION-01 Forensic Analysis | Regulators +10, Board +5 |
| ACTION-02 Threat Hunting | — |
| ACTION-03 Log Analysis | — |
| ACTION-04 Third-Party IR | Regulators +15, Board +15 |
| ACTION-05 Patch & Harden | Executives +5 |
| ACTION-06 Containment | Executives +5 |
| ACTION-07 Rebuild from Backup | Executives +5, Customers +5, Board +5 |
| ACTION-08 Credential Reset | Executives +5 |
| ACTION-09 Customer Notification | Customers +15, Media +5 |
| ACTION-10 Regulatory Notification | Regulators +20 |
| ACTION-11 Media Management | Media +20, Customers +10 |
| ACTION-12 Board Communication | Board +20, Executives +5 |
| ACTION-13 Ransom Decision | — (scoring effects only) |
| Holding Statement (free) | — (stops Customer decay) |

Where a Stakeholder card lists a range (e.g., "+2-5%"), this table is the single authoritative value (v2.2).

---

## Deadlines (v2.2)

| Deadline | Turn | If missed |
|----------|------|-----------|
| Internal legal/executive escalation | End of Turn 2 | Narrative only |
| Customer notification (ACTION-09) | End of Turn 5 (recommended) | Customer trust -10 per later turn; EVENT-05 Class Action may trigger; never notified = -15 Reputation at final scoring |
| Ransom decision (ACTION-13) | Start of Turn 5 (default; +2 turns if NEGOTIATE) | Treated as REFUSE; data-publication event fires |
| Regulatory notification (ACTION-10) — **GDPR 72h** | End of Turn 8 (escalating from Turn 6) | Regulator trust -10 per turn from Turn 6 while un-notified; never notified = -20 Reputation at final scoring (deferred fine) |

---

## Ransomware & ACTION-13 (v2.2)

If the scenario includes a ransom/extortion demand, the team must resolve **ACTION-13: Ransom Decision** before the ransom deadline (default: start of Turn 5). Exactly one option, once per game:

| Option | Cost | Reputation (at scoring) | Effect |
|--------|------|-------------------------|--------|
| **PAY** | 20 Budget (≈ $1M) | -15 | Data-publication event skipped/cancelled; +20% Remediation immediately. **No guarantee:** TO rolls d20 — on 1-5 the keys don't work: no refund, +0% Remediation (publication stays cancelled). |
| **NEGOTIATE** | 5 Budget | -5 | Data-publication event delayed by 2 turns (default: to start of Turn 7). |
| **REFUSE** | 0 Budget | 0 (**-20 if the data-publication event later triggers**) | No payment, no delay. |

**Data-publication event:** if the team has not PAID by the (possibly delayed) deadline, the attacker publishes the stolen data: Customer trust -20, Media trust -15, plus the REFUSE scoring penalty if applicable.

**Corrected facts (v2.2):** payment may violate OFAC sanctions if the threat actor is sanctioned; many insurers restrict or exclude ransom coverage. The FBI discourages payment. Payment guarantees nothing.

**Decision Framework for Teams:**
- **Small company, limited budget:** may pay (can't afford extended downtime)
- **Large company, security-conscious:** often refuses (sets precedent, funds crime)
- **Critical infrastructure:** may negotiate with government assistance
- **Regulated industry / sanctioned actor:** payment may be legally impossible

**Educational Purpose:** the ethical and practical considerations of ransom decisions; no "right" answer — it depends on risk tolerance.

---

## Financial Impact Tracking

**Immediate Costs (paid from DR Budget, floor 0):**
- Crisis Action card costs (see the Crisis Action deck)
- Event costs (subpoena legal fees, regulatory fine, lost revenue)
- Ransom payment or negotiation (ACTION-13)

**Deferred/Ongoing Costs (narrative-only; discuss in debrief):**
- Credit monitoring, legal costs, long-tail regulatory exposure, customer churn
- Real-world scale: GDPR fines run up to €20M or 4% of global turnover, **whichever is higher**; total breach costs typically run to millions

The scoring system captures deferred consequences as Reputation penalties (below) rather than as a parallel money ledger.

---

## Final Scoring (v2.2): Computing Reputation

**Reputation is computed once, at game end.** The three tracks and five trust meters drive play; Reputation (0-100) is the outcome measure.

```
FINAL REPUTATION = 100, then apply:

1. TRACK RESULTS (per track: Investigation, Remediation, Communication)
   50-100%  ->  -0
   25-49%   ->  -5
   10-24%   ->  -10
   0-9%     ->  -20

2. STAKEHOLDER TRUST (average of the five meters at game end)
   70%+     ->  +5
   50-69%   ->  0
   30-49%   ->  -10
   below 30 ->  -20

3. DECISION & EVENT MODIFIERS (each applies at most once)
   +5   Customers notified transparently by end of Turn 5 (ACTION-09)
   +3   per completed quality investigation (ACTION-01 or ACTION-04),
        MAX +6 total per game
   -5   ACTION-13 NEGOTIATE          (only one ACTION-13
   -15  ACTION-13 PAY                 modifier can apply)
   -20  ACTION-13 REFUSE and data was published
   -10  EVENT-05 Class Action triggered
   -10  EVENT-06 Regulatory Fine triggered
   -10  EVENT-08 Second Breach triggered
   -15  Customers never notified in-game (deferred statutory violation)
   -20  Regulators never notified in-game (deferred GDPR fine)

4. CLAMP the result to 0-100.
```

### Outcome Tiers (v2.2 — the ONE tier table, identical in the standalone guide)

| Final Reputation | Outcome | Interpretation |
|------------------|---------|----------------|
| **85-100** | Exemplary | Crisis well-managed; stakeholder trust preserved; the organization recovers |
| **70-84** | Managed | Adequate response; some damage; recovery likely |
| **55-69** | Damaged | Poor response; significant customer loss; regulatory scrutiny; recovery uncertain |
| **40-54** | Mismanaged | Major reputational/financial damage; leadership changes likely |
| **Below 40** | Catastrophic | Company survival in question; CEO likely replaced |

### Loss Conditions (v2.2 — ONE authoritative list, in precedence order)

1. **Any stakeholder trust meter at 0% at any point = immediate loss.** "The company collapses." Nothing else matters.
2. **Otherwise**, the game ends after Turn 8 (Turn 10 if EVENT-08 fired) and the outcome is the tier table above.

**Below 20% trust is a CRITICAL warning state only** — it triggers escalation events but is never itself a loss. The old "<30% trust = loss" rule is removed.

### Optional Difficulty Variant: Scope-Scaled Start

Default: the Reputation computation starts at **100** for every game. As a clearly-labelled optional difficulty variant, start the computation lower for bigger breaches:

| Scope | Records | Start computation at |
|-------|---------|----------------------|
| Small (Beginner) | ~50K | 100 (default) |
| Medium (Intermediate) | ~500K | 90 |
| Large (Advanced) | 5M+ | 80 |

---

## Worked Example (v2.2, recomputed)

**Scenario: "The Ransomware Nightmare"** — customer database encrypted and exfiltrated (500K records), ransom demand $1M (20 Budget), publication threatened. Standalone play, default difficulty. Budget 50.

| Turn | Action (cost) | Tracks | Events & trust |
|------|---------------|--------|----------------|
| 1 | ACTION-02 Threat Hunting (8); justification roll 14 → +5% | Inv 20 | — |
| 2 | ACTION-06 Containment (8) | Rem 15 | EVENT-01: no media action yet → Media 40→30. Exec +5 → 85 |
| 3 | ACTION-10 Notify Regulators (8); declare ACTION-13 **NEGOTIATE** (5) | Comm 10 | Customer decay (no Communication action completed yet at start of turn): Customers 50→40. Regulators 60→80. EVENT-04 unprepared (no ACTION-12) → Board 70→50. Publication delayed to start of Turn 7 |
| 4 | ACTION-05 Patch & Harden (10) | Rem 35 | No more decay (ACTION-10 completed). Exec +5 → 90 |
| 5 | ACTION-09 Customer Notification (10) | Comm 30 | Customers 40→55, Media 30→35. EVENT-03 passed → +5 Rep at scoring. (Private company: skip EVENT-09) |
| 6 | Holding Statement (0) | Comm 35 | EVENT-02: already notified → Regulators +5 → 85. EVENT-08 check: Rem 35 ≥ 30 → does not fire |
| 7 | Holding Statement (0) | Comm 40 | Data published (unpaid): Customers 55→35, Media 35→20. EVENT-12: Exec 90→80, Budget 1→0, Inv +5% → 25 |
| 8 | Holding Statement (0) | Comm 45 | Media at 20 (not below 20) → EVENT-07 does not fire. Game ends |

**Budget spent:** 8+8+8+5+10+10 = 49 of 50 (then -5 subpoena fees, floored at 0).

**Final state:** Tracks: **Inv 25, Rem 35, Comm 45.** Trust: Customers 35, Regulators 85, Media 20, Board 50, Executives 80 → **average 54**.

**Scoring:**
- Tracks: Inv 25 (-5), Rem 35 (-5), Comm 45 (-5) → **-15**
- Trust average 54 → **0**
- Modifiers: +5 (transparent customer notification by Turn 5), -5 (NEGOTIATE) → **0**
- **Final Reputation: 100 - 15 = 85 → Exemplary (barely!)**

**Lessons visible in the example:** the team skipped board prep (Board Meeting hurt), never bought media management (publication nearly triggered a frenzy at Media 20), and threading the ransom deadline with NEGOTIATE bought exactly enough time to notify everyone first. One different choice and this is a 70s game.

**Mandatory-path check (v2.2):** the cheapest mandatory beats — investigate (ACTION-03: 5), notify regulators (ACTION-10: 8), notify customers (ACTION-09: 10), remediate (ACTION-08: 6) — cost **29 Budget**. A stronger path (ACTION-02 + ACTION-10 + ACTION-09 + ACTION-05 + ACTION-06) costs **44**. Both fit a 50-Budget team with room for events.

---

## Sample Disaster Recovery Scenarios (v2.2 card sequences)

### Scenario: "The Ransomware Nightmare"
See the worked example above. Key tension: ransom decision vs. notification deadlines.

### Scenario: "The Insider Data Theft"

**Attack chain revealed:** disgruntled employee → lateral movement → Mimikatz → insider data theft. Data already for sale on dark web (no ransom demand — skip ACTION-13).

**Suggested line of play (Budget 50-60):**
1. Turn 1: ACTION-03 Log Analysis (5) — establish the insider's access timeline
2. Turn 2: ACTION-01 Forensic Analysis (12, Duration 2) — evidence for HR/legal/prosecution
3. Turn 3: ACTION-10 Regulatory/Law-Enforcement Notification (8) — FBI referral
4. Turn 4: (forensics completes: +25% Inv, +3 at scoring) ACTION-08 Credential Reset (6)
5. Turn 5: ACTION-09 Customer Notification (10) — transparent disclosure
6. Turn 6-8: ACTION-06 Containment (8), then Holding Statements

**Teaching point:** insider threats hit Executive and Board trust hardest; internal communication matters as much as external.

### Scenario: "The Supply Chain Compromise"

**Attack chain revealed:** compromised vendor update → lateral movement → cloud API token theft → DNS tunneling exfiltration → persistent C2.

**Teaching point:** teams quickly realize they **cannot finish remediation by Turn 8** — ACTION-07 rebuilds and ACTION-04 third-party IR eat the clock and the budget. That is the lesson: some incidents transition to months-long response. Expect a "Damaged"-tier result even from good play, and debrief why (complex incidents score lower on the same rubric).

---

## DR Phase Outcomes & Debrief

### Mandatory Lessons Learned Debrief (20 minutes)

After DR Phase completion, run a structured debrief:

#### Part 1: Attack Analysis (5 minutes)
1. **What was the initial compromise vector?** Why did defenses fail?
2. **How far did the attacker progress?** What could have stopped them?
3. **What was the attacker's objective?** (Data theft? Ransomware? Persistence?)

#### Part 2: Detection Failures (5 minutes)
1. **Why wasn't this detected during Incident Response?** What signs did we miss?
2. **What defense would have caught this attack?**
3. **What monitoring/logging was inadequate?**

#### Part 3: Response Evaluation (5 minutes)
1. **Was the forensic investigation adequate?** What gaps remained?
2. **Did we communicate effectively with stakeholders?** What went wrong?
3. **Was remediation thorough enough to prevent re-breach?** (Did EVENT-08 fire?)

#### Part 4: Prevention for Next Time (5 minutes)
1. **What one thing would you deploy first if you replayed?**
2. **How would you prioritize defenses differently?**
3. **What process improvements would help next time?**

---

## Comparison: Hardening vs. Disaster Recovery (the two post-IR paths)

### Win Incident Response → Hardening
- **Focus:** Proactive security improvements
- **Mindset:** "We won, now how do we make sure this never happens again?"
- **Timeline:** Leisurely (30 minutes); planning for future
- **Budget:** Focus on investment
- **Outcome:** Security Score (70-100 scale)
- **Key Mechanic:** Deploying layers of defense, hardening with playbooks
- **Educational Value:** Defense-in-depth, layered security, cost-benefit analysis
- **Realism:** How Fortune 500 companies think about security

### Lose Incident Response → Disaster Recovery
- **Focus:** Crisis management and damage control
- **Mindset:** "We failed to detect; now manage the fallout"
- **Timeline:** Urgent (8 turns / 72 narrative hours); crisis response
- **Budget:** Limited emergency funds; every card has a cost
- **Outcome:** Reputation (0-100, computed at game end)
- **Key Mechanic:** Action cards vs. an event timeline, under deadlines
- **Educational Value:** Incident response procedures, stakeholder management, consequences
- **Realism:** Real-world breach management; Target, Yahoo, Equifax situations

---

## Integration with Base Game: Full Game Flow

### Option 1: Standalone Play (Single Path)
- **Setup:** 10 min
- **Play DR:** 30-40 min
- **Debrief:** 10-15 min
- **Total:** 60-75 minutes

### Option 2: Full Campaign (Both Paths)
- **Setup:** 10 min
- **Play Incident Response:** 30-40 min
- **Checkpoint:** 2 min (determine win or lose)
- **Play second module (Hardening or DR):** 20-30 min
- **Debrief:** 15 min
- **Total:** 90-120 minutes

### Option 3: Tournament Mode
- **Setup:** 10 min
- **All teams play Incident Response simultaneously:** 40 min
- **Teams split by outcome:** Winners → Hardening (30 min); Losers → DR (30 min)
- **Final Scoring & Awards:** 15 min; **Debrief:** 10 min
- **Total:** 2-2.5 hours

---

## Teaching Notes for DR Phase

### Key Learning Objectives

**Incident Response Skills:**
- Prioritize crisis response actions under pressure
- Coordinate across teams and stakeholders
- Make decisions with incomplete information
- Understand forensic investigation requirements

**Business Impact Understanding:**
- Recognize financial costs of breaches (not just immediate costs)
- Understand regulatory & legal consequences
- Learn about reputational damage and customer churn
- Recognize insurance and recovery programs

**Stakeholder Management:**
- Communicate effectively with diverse audiences (customers, regulators, media)
- Balance transparency with liability reduction
- Manage expectations during crisis
- Follow regulatory notification requirements (the GDPR 72-hour anchor)

**Long-term Recovery:**
- Incident doesn't end when systems are "fixed"
- Organizational recovery takes months/years
- Prevention is far cheaper than response
- Importance of pre-incident preparation

### Discussion Questions After DR Phase

**For Teams That Had Better Detection (Lost Incident Response by Turn 9-10):**
- "If you'd detected the attack one turn earlier, what would have changed?"
- "What one additional control would have triggered detection?"
- "How does dwell time (time from compromise to detection) affect these costs?"

**For Teams That Lost Quickly (Out of budget by Turn 5-6):**
- "Why did your investigation fail so quickly?"
- "Which budget-saving action actually cost you more in the long run?"
- "What would aggressive early investigation have prevented?"

**For All Teams:**
- "How much did this incident actually cost (total financial + reputational)?"
- "If detection during Incident Response saves 80% of these costs, what should you invest in detection?"
- "How would a pre-prepared incident response plan have helped?"
- "What's the value of having a Disaster Recovery plan before you need it?"

### Real-World Context for DR Phase

**Average Breach Costs (2023 data; narrative-only):**
- **Detection Time (Dwell Time):** 206 days average
- **Cost per Compromised Record:** $4.50 (varies by industry)
- **Total Average Cost:** $4.5M (for 1M records)
- **Cost Breakdown:** Detection & Analysis 25%, Containment & Eradication 20%, Recovery & Restoration 20%, Legal & Regulatory 15%, PR & Communications 10%, Customer Notifications 10%

**Common Mistakes in Real Incidents:**
- Poor forensic planning → Extended investigation costs
- Late customer notification → Regulatory fines + brand damage
- Inadequate remediation → Re-compromise (in-game: EVENT-08)
- Ransom payment → Funds future attacks; doesn't guarantee data deletion
- No incident plan → Chaos and poor decisions

**Success Factors in Real Incidents:**
- Pre-incident planning and training
- Clear communication protocols
- Rapid forensic investigation
- Transparent customer communication
- Thorough remediation
- Post-incident review and improvements

---

## Variants & Extensions

### Variant: "Instant Replay" Recovery

If a team scores **85+ (Exemplary)**, they can attempt a post-game Recovery Analysis: spend 5 remaining Budget for a deep forensic review, identify the systemic failure that allowed the Incident Response loss, and describe the detection investment that would have caught it. Models "turning crisis into opportunity."

### Variant: "Ongoing Breach" (Extended Campaign)

Disaster Recovery doesn't necessarily end the incident: Week 2 threat hunting discovers a backdoor still active; Week 4 the attacker tries again; Week 8 a new variant appears. Replay DR with the Second Breach event pre-armed. Teams learn that some breaches have long tails.

### Variant: "Insurance & Legal" Module

Add negotiation flavor at debrief: Did the insurer cover this incident? (Many policies restrict or exclude ransom coverage.) How much forensic evidence was preserved for lawsuits? Could you have negotiated the regulatory settlement?

---

## Final Thought: Why This Matters

**Incident Response** teaches: "Catch attacks early"
**Hardening (after a win)** teaches: "Prevent future attacks"
**Disaster Recovery (after a loss)** teaches: **"Plan for what you'll miss"**

Together, they create a complete incident response curriculum:
1. **Detection & Investigation** (Incident Response)
2. **Hardening & Prevention** (Hardening — win path)
3. **Crisis Management & Recovery** (Disaster Recovery — loss path)

Students learn that **even with perfect security, breaches can happen**. The question isn't "Will we be attacked?" but "When we're attacked, will we respond effectively?"

---

## v2.2 Playtest Edition Changes

1. **Card system is canonical.** The freeform Actions A-E from v2.1 are replaced by the 13 Crisis Action cards; track advances are deterministic (no success/failure rolls). The optional Justification d20 (11+ → +5%) is the only roll in track advancement; ACTION-13's "no guarantee" roll is the only other die.
2. **One clock:** 8 turns, ~6-12 narrative hours each, Turn 1 ≈ detection +6h to Turn 8 ≈ 72h (fixes the v2.1 7×6h = 42h vs. "48 hours" arithmetic). GDPR 72-hour regulatory notification = ACTION-10 by end of Turn 8, escalating penalties (-10 Regulator trust/turn) from Turn 6. Customer notification recommended by Turn 5. The v2.1 "12-hour regulatory deadline" is relabeled as internal legal/executive escalation. The 30-day/60-day event deadlines are re-expressed as deferred final-scoring penalties (-20 / -15 Reputation).
3. **Reputation reconciled with the percent tracks:** the three tracks + five trust meters drive play; final Reputation (0-100) is computed once at game end (start 100; track tiers, trust average, decision/event modifiers; clamp 0-100). One outcome tier table (85/70/55/40), identical here and in the standalone guide.
4. **Single values for former contradictions:** negotiation reputation effect **-5**; late-regulator penalty **-10/turn**; transparent-notification bonus **+5**; starting reputation **flat 100** (scope-scaled 90/80 is an optional difficulty variant); turn count **8**.
5. **Event deck procedure:** 12 events split into 6 Scheduled (placed on the timeline at setup) + 6 Triggered (fire once when their condition is met). EVENT-08's "additional 7-turn cycle" is now "+2 turns, once per game."
6. **Multi-turn actions defined once:** Duration N occupies the action slot only on the start turn; the advance completes at the start of the Nth following turn; one in-flight multi-turn action at a time. ACTION-04's "runs alongside other actions" text was aligned to this rule.
7. **ACTION-13 Ransom Decision added** (Pay 20 / Negotiate 5 / Refuse 0, with the exact effects above) — this is the "Negotiation Team" card promised in v2.1.
8. **Bounds & loss:** Budget floor 0 (free Holding Statement always available); trust meters and Reputation clamp 0-100; one loss list — any trust meter at 0% = immediate loss, otherwise the tier table. "<30% = loss" removed; "<20%" is a critical warning state only.
9. **Money mapping:** 1 Budget ≈ $50K; remaining dollar figures are narrative-only.
10. **Fact corrections:** OFAC/insurance wording for ransom payment; GDPR fine = €20M or 4% of global turnover, whichever is HIGHER; California/CCPA "without unreasonable delay" + statutory damages; turnover-scale fines attributed to GDPR-style regimes (not the FTC).
11. **Balance:** forensic-quality Reputation bonus capped at +6 per game; mandatory-path cost verified at 29-44 Budget against the 50 starting budget.

---

*Disaster Recovery Phase for Incident Zero*
*For teams that experience the cost of failed detection*
*Emphasizing that response quality matters as much as prevention*
