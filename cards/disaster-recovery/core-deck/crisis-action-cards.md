# Disaster Recovery Module: Crisis Action Cards

**Version:** 2.2 - Playtest Edition
**Last Updated:** October 2025

---

## Overview

**Crisis Action Cards** represent the specific actions an organization can take during a breach to investigate, remediate, and respond. Teams deploy ONE Crisis Action each turn to advance three objectives: Investigation %, Remediation %, and Communication % (each tracked 0-100%). Track advances are **deterministic** — no dice are required to advance a track.

- **Total Cards:** 13 (ACTION-01 to ACTION-13)
- **Used In:** Disaster Recovery module (primary gameplay cards)
- **Cost Range:** 0-20 Budget (ACTION-13 Refuse is free; most actions cost 5-15)
- **Game Clock:** 8 turns; each turn is one crisis phase of ~6-12 hours (Turn 1 ≈ detection +6h ... Turn 8 ≈ 72h). See the module rules for the full turn table.
- **Purpose:** Drive incident response forward under time/budget pressure

**Money mapping:** 1 Budget ≈ $50K. Dollar figures on cards (fines, ransom) use this mapping unless marked narrative-only.

---

## Crisis Action Card Organization

### Action Categories

Crisis Actions are organized into three categories, plus one decision card:

1. **Investigation Actions** (4 cards)
   - Advance understanding of breach
   - Determine scope and impact
   - Gather evidence for forensics
   - Enable faster containment

2. **Remediation Actions** (4 cards)
   - Fix vulnerability that was exploited
   - Contain compromised systems
   - Recover from backup
   - Rebuild infrastructure

3. **Communication Actions** (4 cards)
   - Notify stakeholders
   - Manage media/public relations
   - Report to regulators
   - Maintain customer trust

4. **Crisis Decision** (1 card)
   - ACTION-13: Ransom Decision (Pay / Negotiate / Refuse)

### Multi-Turn Actions (v2.2)

Some actions list **Duration N** (N greater than 1). The rule, defined once:

> **Duration N:** the action occupies your action slot **only on the turn it is started**; its track advance completes and is applied **at the start of the Nth following turn**. Only one multi-turn action may be in flight at a time. While it is in flight, you may take single-turn actions on later turns, but you may not start another multi-turn action.

*Example:* ACTION-01 (Duration 2) started on Turn 2 applies its +25% Investigation at the start of Turn 4.

### Justification Bonus (v2.2) — optional

The signature d20 stays as an **optional bonus only** (it never gates track advancement): when a team plays an Action card with a strong, specific technical justification, the Threat Orchestrator may allow a d20 roll. **On 11+, that action's track advance gains +5%.** One roll per action card played.

### Free Action: Holding Statement (v2.2)

This is a standing rule, not a numbered card. On any turn, instead of playing an Action card, the team may issue a **Holding Statement** (internal update / brief public status statement):

- **Cost:** 0 Budget (always available, even at 0 Budget)
- **Effect:** +5% Communication; counts as a Communication action for stakeholder decay purposes

---

## Investigation Actions

### ACTION-01: Forensic Analysis
**Category:** Investigation
**Cost:** 12 Budget
**Investigation Advance:** +25%
**Duration:** 2 turns (multi-turn action)

**Description:**
Forensic experts analyze compromised systems to determine:
- What data was accessed
- What was exfiltrated
- How long attacker had access
- What attack techniques were used
- Evidence for legal proceedings

**Key Details:**
- Requires shutting down compromised system (removes it from operation)
- Requires forensics team (may need external consultants)
- Takes time (2 turns minimum)
- Provides detailed evidence
- Essential for legal action and regulatory compliance

**When to Use:**
- Need definitive answer about breach scope
- Legal action is likely
- Compliance investigation required
- Regulatory agency involved

**Risk if Not Done:**
- Cannot determine full extent of damage
- Cannot properly remediate (may miss persistence)
- No evidence for law enforcement
- Regulatory penalties for inadequate investigation

**Regulatory Impact:**
- Most breach notification laws require "reasonable investigation"
- Forensics evidence may be required for regulatory compliance
- Better investigation = stronger regulatory defense

**Team Trade-off:**
- Expensive (12 Budget)
- Takes time (2 turns)
- But provides high investigation %
- Provides evidence for future action

---

### ACTION-02: Threat Hunting
**Category:** Investigation
**Cost:** 8 Budget
**Investigation Advance:** +15%
**Duration:** 1 turn

**Description:**
Security team proactively searches logs and systems for:
- Other compromised systems
- Lateral movement indicators
- Persistence mechanisms
- Command & Control communication
- Evidence of data staging

**Key Details:**
- Requires SIEM with good logging (if available)
- Team searches for attack indicators
- Can discover secondary compromises
- Lower cost than forensics but less detailed
- Faster than forensics (1 turn)

**When to Use:**
- Need to know if compromise spread
- Want to find hidden persistence
- Time is critical (forensics takes 2 turns)
- Budget is constrained

**Risk if Not Done:**
- May not discover all compromised systems
- Attacker may maintain hidden access
- May lose evidence over time (logs rotate)
- Compliance investigation may be incomplete

**Regulatory Impact:**
- Shows good faith investigation effort
- Supports "reasonable investigation" standard
- Evidence of proactive security posture

**Team Trade-off:**
- Cheaper than forensics (8 Budget)
- Faster (1 turn vs. 2)
- Less detailed evidence
- Good balance of cost/time/effectiveness

---

### ACTION-03: Log Analysis
**Category:** Investigation
**Cost:** 5 Budget
**Investigation Advance:** +10%
**Duration:** 1 turn

**Description:**
Security team reviews available logs (firewall, VPN, Windows Event Log, application logs) to understand:
- When breach was discovered
- What access was gained
- What systems were accessed
- What data might have been accessed
- Timeline of attack

**Key Details:**
- Requires logs (must have been collecting logs)
- Basic analysis of existing logs
- Cheapest investigation action
- Quick (1 turn)
- Limited by log retention/quality
- Can be done internally (no external consultants)

**When to Use:**
- Budget is extremely tight
- Need quick preliminary understanding
- Good logging infrastructure in place
- Time is critical

**Risk if Not Done:**
- No understanding of what happened
- Cannot determine scope or impact
- Regulatory agencies upset about lack of investigation
- Potential for incomplete response

**Regulatory Impact:**
- Minimal investigation (may not satisfy "reasonable investigation")
- Shows attempt at investigation
- Not sufficient as sole investigation method

**Team Trade-off:**
- Cheapest investigation (5 Budget)
- Fastest (1 turn)
- Limited effectiveness
- Often insufficient alone

---

### ACTION-04: Third-Party Incident Response Engagement
**Category:** Investigation (+ Remediation)
**Cost:** 20 Budget
**Investigation Advance:** +30% (+ Remediation +20%)
**Duration:** 3 turns (ongoing engagement)

**Description:**
Bring in external incident response firm (forensics, incident handling, remediation specialists). They conduct:
- Comprehensive forensic investigation
- Breach scope determination
- Remediation recommendations
- Expert testimony for legal proceedings
- Regulatory coordination

**Key Details:**
- Very expensive (20 Budget)
- Takes significant time to mobilize
- Provides expert guidance and credibility
- Provides evidence acceptable in court
- Supports regulatory defense
- Multi-turn (Duration 3): occupies your action slot only on the turn started; see Multi-Turn Actions rule

**When to Use:**
- Major breach with legal implications
- Need expert investigation for court
- Regulatory agency demands expertise
- Internal team cannot handle scope
- Liability is significant

**Benefits:**
- Expert investigation (higher quality)
- Evidence for prosecution
- Regulatory/legal credibility
- Expert testimony available
- Ongoing support (3 turns)

**Risk if Not Done:**
- Without external expertise, breach response may be insufficient
- Legal case may fail (poor evidence)
- Regulatory penalties for inadequate investigation
- May miss critical evidence

**Regulatory Impact:**
- High credibility with regulators
- Better legal defense
- Shows serious investigation effort
- External experts satisfy "reasonable investigation"

**Team Trade-off:**
- Most expensive (20 Budget)
- Long commitment (Duration 3 — advances apply at the start of the 3rd following turn)
- But provides significant investigation + remediation
- Provides external expertise and credibility
- While in flight you may take single-turn actions, but no other multi-turn action (v2.2 Multi-Turn rule)

---

## Remediation Actions

### ACTION-05: Patch & Harden (Affected Systems)
**Category:** Remediation
**Cost:** 10 Budget
**Remediation Advance:** +20%
**Duration:** 1 turn

**Description:**
Apply patches to the vulnerability that was exploited:
- Install OS patches (if vulnerability is OS-level)
- Update application (if vulnerability is app-level)
- Change default credentials
- Remove backdoor accounts
- Harden network configuration

**Key Details:**
- Targets the specific vulnerability that was exploited
- Must know what vulnerability was exploited (requires investigation)
- Can be done on specific systems or organization-wide
- Prevents same attack from succeeding again
- Does NOT remove attacker if already inside

**When to Use:**
- Know what vulnerability was exploited
- Want to prevent re-exploitation
- Can apply patch without affecting business
- Quick remediation needed

**Risk if Not Done:**
- Attacker can re-exploit same vulnerability
- Breach scope may grow
- Regulatory agency upset about lack of remediation
- Risk of breach happening again

**Regulatory Impact:**
- Shows timely remediation
- Prevents recurrence
- Good compliance posture
- Regulatory agencies expect patching

**Team Trade-off:**
- Moderate cost (10 Budget)
- Quick (1 turn)
- Fixes vulnerability
- But only prevents re-exploitation, doesn't remove attacker

---

### ACTION-06: Containment (Isolate Compromised Systems)
**Category:** Remediation
**Cost:** 8 Budget
**Remediation Advance:** +15%
**Duration:** 1 turn

**Description:**
Remove compromised systems from network to:
- Stop attacker from using compromised system for lateral movement
- Prevent attacker from exfiltrating more data
- Preserve compromised system for forensics
- Limit blast radius of compromise

**Key Details:**
- Disconnect compromised system from network (kill network)
- System is still available for forensics
- Stops active attacker in that system
- Does NOT affect attacker if they're in other systems
- May impact business (systems are unavailable)

**When to Use:**
- Know which systems are compromised
- Want to stop active attacker
- Can tolerate system downtime
- Attacker is still actively in system

**Risk if Not Done:**
- Attacker continues using compromised system
- Lateral movement continues
- More data exfiltration
- Attacker may install additional backdoors

**Regulatory Impact:**
- Shows swift containment action
- Demonstrates incident response
- Limits liability (stopped attacker)
- Good compliance posture

**Team Trade-off:**
- Moderate cost (8 Budget)
- Quick (1 turn)
- Stops active attacker
- But impacts business operations

---

### ACTION-07: System Rebuild/Recovery from Backup
**Category:** Remediation
**Cost:** 15 Budget
**Remediation Advance:** +25%
**Duration:** 2 turns (restore + verification)

**Description:**
Rebuild compromised systems from backup:
- Restore system from clean backup (pre-compromise)
- Apply patches to prevent re-exploitation
- Restore only clean data
- Verify system is clean before returning to production
- Monitor restored system for attacker re-entry

**Key Details:**
- Requires backup of system (must exist and be clean)
- Takes time to restore (2 turns minimum)
- Removes all attacker artifacts
- Ensures system is truly clean
- Most reliable remediation method
- Dependent on backup quality/testing

**When to Use:**
- Backup exists and is verified clean
- System compromise is extensive
- Want to ensure complete attacker removal
- Business can tolerate 2-turn rebuild

**Risk if Not Done:**
- Attacker may maintain persistence (if system not rebuilt)
- Restore from backup with attacker in it = no improvement
- Compliance may require clean rebuild

**Regulatory Impact:**
- Shows complete remediation
- Demonstrates thorough approach
- Better regulatory outcome
- Shows commitment to clean recovery

**Team Trade-off:**
- Higher cost (15 Budget)
- Takes time (2 turns)
- But provides complete remediation
- Most reliable method

---

### ACTION-08: Change Credentials & Access Controls
**Category:** Remediation
**Cost:** 6 Budget
**Remediation Advance:** +12%
**Duration:** 1 turn

**Description:**
Revoke and reset all potentially compromised credentials:
- Reset passwords for all accounts that touched compromised system
- Revoke tokens/API keys
- Reset VPN credentials
- Update database passwords
- Revoke certificates/SSH keys

**Key Details:**
- Prevents attacker from using stolen credentials
- Must do if credentials were compromised (stolen by Mimikatz, etc.)
- Can cause business disruption (users locked out)
- Quick and important
- Often overlooked but critical

**When to Use:**
- Credentials were likely compromised
- Attacker had access to credential stores
- Need to prevent attacker re-entry via stolen credentials
- Quick credential reset is possible

**Risk if Not Done:**
- Attacker can use stolen credentials to re-enter
- Lateral movement using stolen creds continues
- Breach is not truly contained
- Regulatory violation (allowing unauthorized access)

**Regulatory Impact:**
- Essential remediation step
- Shows understanding of attack chain
- Prevents credential reuse attacks
- Regulatory expectation

**Team Trade-off:**
- Low cost (6 Budget)
- Quick (1 turn)
- Important and often overlooked
- Can cause short-term business disruption

---

## Communication Actions

### ACTION-09: Customer Notification
**Category:** Communication
**Cost:** 10 Budget
**Communication Advance:** +20%
**Duration:** 1 turn (but affects later turns)
**Deadline (v2.2):** Recommended by end of **Turn 5**. If not completed by then: Customer trust -10 at the start of each later turn; if never completed in-game: -15 Reputation at final scoring (deferred statutory violation).

**Description:**
Notify customers that their data may have been breached:
- Determine which customers were affected
- Prepare notification message
- Send via email, mail, or phone
- Provide information about what was accessed
- Offer credit monitoring/identity protection if applicable
- Field customer questions/complaints

**Key Details:**
- Required by breach notification laws ("without unreasonable delay" in California and most U.S. states; GDPR requires notifying individuals without undue delay when risk is high)
- Can be very expensive if many customers affected
- Notification can cause loss of customer trust
- Early notification shows good faith
- Delayed notification shows company doesn't care
- Impacts Customers stakeholder directly

**Regulatory Requirements:**
- Most laws require notification "without unreasonable delay"; some states set specific outer limits
- California: notify without unreasonable delay; CCPA statutory damages fuel class actions
- Notification must include:
  - What information was accessed
  - Recommended actions
  - Contact information
  - Free credit monitoring (sometimes)

**When to Use:**
- Customer data was accessed in breach
- Regulatory requirement to notify
- Want to rebuild customer trust
- Transparency is important

**Risk if Not Done:**
- Regulatory violation (fines, penalties)
- Customer discovery + lawsuits
- Loss of customer trust (worse than notification)
- Reputation damage from cover-up worse than from breach

**Regulatory Impact:**
- Many states REQUIRE customer notification
- California law, GDPR, and other state laws all require notification; CCPA statutory damages fuel class actions
- Without notification = regulatory violation + fines
- Proactive notification = better regulatory relationship

**Team Trade-off:**
- Moderate cost (10 Budget)
- Can be done quickly (1 turn)
- Required by law (usually)
- Impacts Customers stakeholder (see Stakeholder Cards)
- Must be done eventually

---

### ACTION-10: Regulatory/Law Enforcement Notification
**Category:** Communication
**Cost:** 8 Budget
**Communication Advance:** +10%
**Duration:** 1 turn (but ongoing for months)
**Deadline (v2.2):** Must be completed by end of **Turn 8** (the GDPR 72-hour anchor). Escalating penalty from Turn 6: if not yet completed, Regulator trust -10 at the start of Turns 6, 7, and 8. If never completed in-game: -20 Reputation at final scoring (deferred fine).

**Description:**
Notify appropriate regulatory agencies:
- Contact FBI/Secret Service (federal crimes)
- Contact state attorney general (breach notification)
- Contact relevant sector regulator (HHS for healthcare, OCC for banking, etc.)
- Contact DHS (if critical infrastructure)
- Coordinate with law enforcement

**Key Details:**
- Required by law in many cases (healthcare, financial, etc.)
- May trigger investigation by law enforcement
- Can help recover stolen data
- Provides some legal protection
- Can delay prosecution (if they're investigating)
- Required before public disclosure in some cases

**Regulatory Requirements:**
- EU data (GDPR): Must notify the supervisory authority within 72 hours; fines up to €20M or 4% of global turnover, whichever is HIGHER (narrative-only figure)
- Healthcare (HIPAA): Must report to HHS Office for Civil Rights
- Financial (GLBA/FFIEC): Must report to banking regulators
- Payment cards (PCI-DSS): Must report to card networks
- Critical infrastructure: Must report to DHS/CISA

**When to Use:**
- Data breach triggers regulatory requirement
- Want law enforcement assistance
- Want to establish good faith investigation
- Legal team recommends it

**Risk if Not Done:**
- Regulatory violation if required
- Law enforcement cannot assist
- Company appears to be hiding breach
- Regulators may impose penalties

**Regulatory Impact:**
- Required in many cases (legal obligation)
- Shows cooperation with authorities
- May help recover stolen data
- Better regulatory relationship
- May reduce penalties (self-reporting)

**Team Trade-off:**
- Moderate cost (8 Budget)
- Ongoing (involves multiple turns of coordination)
- Required by law (usually)
- Impacts Regulators stakeholder (see Stakeholder Cards)
- Must be done in most cases

---

### ACTION-11: Media/Public Relations Management
**Category:** Communication
**Cost:** 12 Budget
**Communication Advance:** +15%
**Duration:** 1 turn (but ongoing for days/weeks)

**Description:**
Manage media coverage and public perception:
- Prepare press statement
- Contact media proactively
- Manage social media response
- Coordinate CEO/executive messaging
- Defend company reputation
- Provide accurate information to media

**Key Details:**
- Can heavily influence public perception
- Proactive messaging better than reactive
- Media coverage can amplify damage
- Poor communication = reputation disaster
- Good communication = company "handled it well"
- HR firm may be needed (crisis PR)

**When to Use:**
- Breach is significant (likely to attract media)
- Company has public reputation risk
- Customers are media-aware (B2C more than B2B)
- Proactive messaging is possible

**Risk if Not Done:**
- Media covers story with only attacker's perspective
- Reputation damage from poor response
- Stock price may drop (if public company)
- "No comment" looks like company is hiding
- Social media amplifies negative coverage

**Impact if Done Well:**
- "Company handled breach responsibly"
- Trust is maintained or recovered
- Stock price less impacted
- Reputation damage is contained
- Customer retention better

**Team Trade-off:**
- Higher cost (12 Budget)
- Ongoing (multiple turns)
- Impacts Media/Board stakeholder (see Stakeholder Cards)
- Critical for public companies
- Can significantly affect perception

---

### ACTION-12: Board & Shareholder Communication
**Category:** Communication
**Cost:** 9 Budget
**Communication Advance:** +12%
**Duration:** 1 turn (but triggers Board Meeting - see Event Cards)

**Description:**
Inform board of directors and shareholders about breach:
- Prepare incident briefing for board
- Present forensics findings
- Discuss regulatory/legal implications
- Present remediation plan and costs
- Discuss risk mitigation going forward
- Field board questions

**Key Details:**
- Board must be informed promptly
- Disclosure may be required (SEC rules if public company)
- Board has fiduciary duty to inform shareholders
- Lawsuit risk if board hides information
- Board can fire CEO if response is poor
- Must include implications for D&O insurance

**Regulatory Requirements:**
- SEC disclosure rules (if public company)
- State corporate law (fiduciary duty)
- Insurance requirements (D&O coverage)

**When to Use:**
- Board needs to understand breach
- Public company (SEC disclosure likely needed)
- Board questions will come (better to be prepared)
- Shareholder lawsuits are likely

**Risk if Not Done:**
- Board discovers breach from media = crisis of confidence
- Shareholder lawsuits for non-disclosure
- SEC investigation for disclosure violations
- CEO may be fired (looked like hiding information)
- Stock price crashes when discovered

**Impact if Done Well:**
- Board is informed and supportive
- No surprise when disclosed
- Board can defend company (if sued)
- Stock market takes news in stride
- Organized response is possible

**Team Trade-off:**
- Moderate cost (9 Budget)
- Critical for public companies
- Impacts Board stakeholder (see Stakeholder Cards)
- Required by law (usually)
- Complete before EVENT-04 (Board Meeting, scheduled Turn 3) to be "prepared" (see Event Cards)

---

### ACTION-13: Ransom Decision (v2.2)
**Category:** Crisis Decision
**Cost:** Varies by option (see below)
**Timing:** Play at any time before the ransom deadline (default: start of Turn 5). Playing this card does NOT use your turn's action slot — it is a decision made in addition to your normal action. Once per game. If no decision is made by the deadline, the team is treated as having chosen REFUSE.
**Used only in scenarios with a ransom/extortion demand.**

Choose exactly ONE option:

**Option A — PAY**
- **Cost:** 20 Budget (≈ $1M at 1 Budget ≈ $50K)
- **Reputation:** -15 at final scoring
- **Effect:** The data-publication event is skipped/cancelled. +20% Remediation immediately (decryption keys restore systems).
- **No guarantee:** The Threat Orchestrator rolls a d20. On 1-5, the keys don't work — no refund, and the Remediation advance is +0% instead of +20%. (The publication event stays cancelled; the attacker took the money and moved on.)
- **Flavor:** "Criminals are not a customer-service organization."

**Option B — NEGOTIATE**
- **Cost:** 5 Budget (negotiator/counsel fees)
- **Reputation:** -5 at final scoring
- **Effect:** The data-publication event is delayed by 2 turns (default: from start of Turn 5 to start of Turn 7). Buys time to notify stakeholders and remediate before publication.

**Option C — REFUSE**
- **Cost:** 0 Budget
- **Reputation:** No immediate change. **If the data-publication event triggers later: -20 Reputation at final scoring.**
- **Effect:** No payment, no delay. Focus budget on investigation, remediation, and communication.

**Data-Publication Event (reference):** In ransom scenarios, if the team has not PAID by the ransom deadline (default: start of Turn 5; +2 turns if NEGOTIATE), the attacker publishes stolen data: Customer trust -20, Media trust -15 (and the REFUSE scoring penalty above, if applicable).

**Legal & practical facts (corrected v2.2):**
- Payment may violate OFAC sanctions if the threat actor is sanctioned; many insurers restrict or exclude ransom coverage
- Law enforcement (FBI) discourages payment — it funds and incentivizes future attacks
- Payment does not guarantee data deletion or working keys

**Educational Purpose:** There is no "right" answer — payment is a genuine trade-off between operational recovery, ethics, legality, and reputation.

---

## Crisis Action Card Summary

| Card | Category | Cost | Advance | Duration | Key Benefit |
|------|----------|------|---------|----------|------------|
| ACTION-01 | Investigation | 12 | +25% | 2 turns | Expert forensics |
| ACTION-02 | Investigation | 8 | +15% | 1 turn | Find hidden compromises |
| ACTION-03 | Investigation | 5 | +10% | 1 turn | Quick log analysis |
| ACTION-04 | Investigation | 20 | +30% Inv / +20% Rem | 3 turns | Third-party expertise |
| ACTION-05 | Remediation | 10 | +20% | 1 turn | Fix vulnerability |
| ACTION-06 | Remediation | 8 | +15% | 1 turn | Contain attacker |
| ACTION-07 | Remediation | 15 | +25% | 2 turns | Clean rebuild |
| ACTION-08 | Remediation | 6 | +12% | 1 turn | Revoke access |
| ACTION-09 | Communication | 10 | +20% | 1 turn | Notify customers (by Turn 5) |
| ACTION-10 | Communication | 8 | +10% | 1 turn | Notify regulators (by Turn 8) |
| ACTION-11 | Communication | 12 | +15% | 1 turn | Media management |
| ACTION-12 | Communication | 9 | +12% | 1 turn | Board notification (before Turn 3) |
| ACTION-13 | Crisis Decision | 0/5/20 | Pay: +20% Rem | Instant | Ransom decision (once per game) |
| *Free* | Communication | 0 | +5% | 1 turn | Holding Statement (standing rule, not a card) |

**Budget floor (v2.2):** Budget can never go below 0. If you cannot afford any card, the free Holding Statement is always available.

---

## Gameplay Strategy

### Three Competing Objectives

Teams must balance three objectives (each goes 0-100%):
- **Investigation %:** Understand scope and impact
- **Remediation %:** Fix vulnerability and remove attacker
- **Communication %:** Manage stakeholders and public perception

### Investigation vs. Remediation Trade-off

**Investigation-Heavy Strategy:**
- Spend early turns investigating (ACTION-01, ACTION-02, ACTION-04)
- Then remediate with full knowledge
- Advantage: Know exactly what happened
- Disadvantage: Takes time, attacker may still be active

**Remediation-Heavy Strategy:**
- Contain and clean immediately (ACTION-06, ACTION-07, ACTION-08)
- Investigate after containment
- Advantage: Stop attacker quickly
- Disadvantage: May miss something, incomplete cleanup

**Balanced Strategy:**
- Do some investigation + some remediation each turn
- Use cheaper actions (ACTION-03, ACTION-06, ACTION-08)
- Save expensive actions for critical moments
- Advantage: Steady progress on all three objectives

### Communication Strategy

**Early Communication:**
- Notify stakeholders early (ACTION-09, ACTION-10, ACTION-12)
- Show proactive response
- Maintain trust and credibility

**Late Communication:**
- Wait until full picture is known
- Risk: Stakeholders discover from media
- Risk: Looks like hiding information

**Selective Communication:**
- Notify regulators (required by law)
- Delay customer notification (if allowed)
- Focus on internal response first

### Mandatory Beats & Budget (v2.2)

With 50 Budget, the mandatory crisis beats are always affordable:

- Investigate (ACTION-03: 5, or ACTION-02: 8)
- Notify regulators by Turn 8 (ACTION-10: 8)
- Notify customers by Turn 5 (ACTION-09: 10)
- Remediate (ACTION-08: 6 and/or ACTION-06: 8)

Cheapest mandatory path: 5 + 8 + 10 + 6 = **29 Budget**. A stronger balanced path (ACTION-02 + ACTION-10 + ACTION-09 + ACTION-05 + ACTION-06) costs **44 Budget** — still within 50.

---

## Print Instructions

1. Print on cardstock (250 gsm minimum)
2. Color-code by action category:
   - **Blue (Investigation):** ACTION-01 to ACTION-04
   - **Red (Remediation):** ACTION-05 to ACTION-08
   - **Green (Communication):** ACTION-09 to ACTION-12
   - **Gold (Crisis Decision):** ACTION-13
3. Include cost in bold on card
4. Include progress bars (Investigation %, Remediation %, Communication %)
5. Cut along dotted lines
6. Track sheets (progress tracks, stakeholder trust): see print pack (coming)

---

*Disaster Recovery Module: Crisis Action Cards*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.2 - Playtest Edition*
