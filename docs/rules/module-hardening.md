# Hardening Module: Complete Rules

**Version:** 2.2 - Playtest Edition
**Module Duration:** 20-45 minutes (standalone or after Incident Response)
**Prerequisites:** None (can play standalone) or completion of Incident Response module
**Learning Focus:** Defense-in-depth, security architecture, proactive hardening, layered controls

---

## Module Overview

The **Hardening Module** teaches players how to build **multi-layered security controls** that work together to protect critical systems. Players transition from reactive incident response to proactive security design.

This module can be:
- **Standalone:** Play alone with generated threat context
- **Continuation:** Follow a successful Incident Response (players harden against discovered threats)
- **Paired:** Combined with other modules for complete security lifecycle training

---

## Core Mechanics: What's Different from Incident Response

| Aspect | Incident Response | Hardening |
|--------|------------------|-----------|
| **Focus** | Detect hidden threats | Build defenses against known threats |
| **Time Pressure** | High (variable turn limit, 100 budget) | Lower (7 turns, carries budget forward) |
| **Actions** | Investigate, Deploy, Emergency Response | Deploy, Upgrade, Playbook, Test |
| **Rolls Needed** | Investigation & Defense deployments | Test & Drill and Pentester defense rolls |
| **Scoring** | Detection efficiency | Defense layering & breadth |
| **Threats** | Hidden chain | Known vectors, Pentester tactics |

---

## Setup

### Step 1: Determine Your Context

#### Option A: Standalone Play (Fresh Start)
Generate threat context from scratch (v2.2 — one standard procedure):
- Roll **1d6 for each of the six threat vectors** (SOCIAL_ENGINEERING, WEB_EXPLOIT, CREDENTIAL_ABUSE, MALWARE, NETWORK, DATA_EXFIL):
  - **1-2:** No notable threat on this vector
  - **3-4:** Intermediate threat on this vector
  - **5-6:** Advanced threat on this vector
- Or use Threat Orchestrator's chosen scenario
- Budget: 150 (full planning allocation)

#### Option B: Continuation from Incident Response
Use the attack chain that was just discovered:
- All **revealed threat cards** now represent known attack vectors
- Each vector gets a defense priority
- Budget carries over (minimum 20, maximum 150)
- Example: If IR revealed Phishing, Lateral Movement, and Data Exfil, you harden against those specific vectors

#### Option C: Hypothetical Scenario
Threat Orchestrator describes a realistic scenario:

> "Imagine your team successfully detected an attack chain:
> 1. Phishing campaign (SOCIAL ENGINEERING vector)
> 2. Lateral movement via SMB (NETWORK vector)
> 3. Data exfiltration (DATA EXFIL vector)
>
> You have time to harden your network. Here are the threat vectors you need to defend against..."

### Step 2: Initialize Trackers

- **Budget:** Starting allocation (150 for solo, carry-over if continuing from IR)
- **Security Score:** 0 (will accumulate points)
- **Turn Counter:** 1
- **Hardening Upgrades:** 0 (track total count)
- **Playbooks Created:** 0 (track total count — **maximum 2 per game, v2.2**)
- **Deployed Defenses:** [] (track list on paper/whiteboard)

### Step 3: Prepare Card Decks

- **Defense Cards Deck:** Shuffle all available cards (D-01 to D-24, see `cards/hardening/core-deck/defense-cards.md`)
- **Pentester Tactic Cards:** Set aside 2-4 cards from PT-01 to PT-08 (by difficulty level, see `cards/hardening/core-deck/pentester-tactic-cards.md`)
- **Asset Cards:** Place relevant systems on table (Email Server, Database, Workstations, etc. — shared components, see `cards/network-building/core-deck/asset-cards.md`)

### Step 4: Deal Starting Hand

Each Blue Team receives **5 Defense Cards** (drawn randomly, face down in hand)

### Step 5: Read Opening Narrative

Threat Orchestrator provides context for the hardening scenario:

> "Your detection team successfully identified an attack chain. Now you have time and resources to harden your defenses to prevent similar attacks in the future. Here's what you're defending against and what assets are at risk..."

---

## Gameplay: 7 Turns

The Hardening module runs **7 turns** at every difficulty level (v2.2 — difficulty scales through the number of Pentester Tactics, not the turn count). One action per turn.

### Turn Structure

**START OF TURN**
- Announce turn number: "Hardening Turn 3..."
- Announce remaining Budget
- Declare any Pentester Challenge scheduled for this turn

**PLANNING PHASE (2-3 minutes)**
- Team discusses hardening strategy
- Decides which action to take this turn
- Prepares for any mid-turn Pentester Challenge

**ACTION PHASE**
- Execute chosen action (see below)
- Resolve rolls if applicable
- Update trackers

**END OF TURN**
- Advance turn counter
- Draw 1 new Defense Card
- Check if Pentester Challenge occurs (typically turn 3-4)

---

## Four Hardening Actions

### Action 1: Deploy a New Defense 🛡️

**Cost:** 10/15/25 Budget (based on card tier)
**Roll Required:** None—automatic success

**How it works:**
1. Choose a Defense Card from your hand
2. Announce which Asset or threat vector it protects
3. Place card on the table (face up)
4. Optional: Explain the deployment strategy (enhances learning but not required)

**Effect:**
- Defense is immediately active and deployed
- Counts toward Security Score (5 points per defense)
- Cannot be undone (represents permanent security improvement)
- Stays on board for remainder of module and beyond (if continuing)

**Quick-Win Rule (v2.2):** You may deploy **up to 2 BASIC-tier defenses as a single action** (pay 10 Budget each). This keeps foundational hygiene affordable within the 7-turn limit.

**Examples:**
- Deploy Multi-Factor Authentication (ADVANCED - 15 Budget) on VPN access
- Deploy EDR on all workstations (ADVANCED - 15 Budget)
- Deploy Data Loss Prevention (DLP) on network gateways (ADVANCED - 15 Budget)
- Deploy Email Authentication (BASIC - 10 Budget) and User Security Training (BASIC - 10 Budget) together as one action (v2.2 Quick-Win)

**Strategic Notes:**
- BASIC defenses (10 Budget) are cheaper but carry smaller printed bonuses against Pentester Tactics
- ADVANCED defenses (15 Budget) provide good balance of cost/effectiveness
- ELITE defenses (25 Budget) are expensive but carry the largest printed bonuses against Pentester Tactics

---

### Action 2: Harden an Existing Defense ⬆️

**Cost:** 5 Budget per upgrade
**Roll Required:** None

**How it works:**
1. Choose a Defense Card already deployed (earlier this game, or carried over from Incident Response)
2. Pay 5 Budget
3. Mark defense with **+2 effectiveness bonus** (track on paper)
4. Optional: Describe the hardening (e.g., "Tuning behavioral analytics in EDR")

**Effect:**
- Defense effectiveness increases by +2
- Bonuses stack (EDR with three upgrades = +6 total)
- Counts toward Security Score (2 points per upgrade)
- Makes defense more resistant to Pentester Tactics

**Examples of Hardening:**
- "Harden our MFA by requiring hardware tokens instead of SMS" → MFA now has +2
- "Enhance Network Segmentation with microsegmentation inside critical zones" → NS now has +2
- "Improve SIEM with threat intelligence integration" → SIEM now has +2

**Strategic Value:**
- Fewer, well-hardened defenses can beat many basic ones
- Upgrades compound: 3 upgrades on one defense = +6 bonus
- Cost-effective way to improve security posture without full new deployments

---

### Action 3: Prepare an Incident Response Playbook 📋

**Cost:** 10 Budget per playbook
**Roll Required:** None
**Limit (v2.2):** Maximum **2 playbooks per game**

**How it works:**
1. Choose a specific threat vector you want to prepare for (SOCIAL ENGINEERING, WEB EXPLOIT, CREDENTIAL ABUSE, MALWARE, NETWORK, or DATA EXFIL)
2. Write a 1-2 sentence playbook describing your response plan
3. Place playbook on the table with vector marked
4. When an attack using this vector occurs, you get **one-time +3 bonus** to your defense roll

**Effect:**
- Provides one-time +3 bonus to defense roll when matching vector is attacked
- Playbook is discarded after use (one-time only)
- Counts toward Security Score (10 points per playbook)
- Forces strategic thinking about which threats matter most

**Example Playbooks:**
- **SOCIAL ENGINEERING:** "Credential Compromise Response - Forced MFA re-authentication and access token revocation across all systems"
- **MALWARE:** "Ransomware Response - Immediate backup isolation, network segmentation, and process termination"
- **NETWORK:** "Lateral Movement Detection - Real-time network behavior analysis and suspicious SMB activity alert protocol"
- **DATA EXFIL:** "Data Theft Response - DLP block, endpoint containment, and forensic image capture"
- **WEB EXPLOIT:** "Web Attack Response - Immediate application firewall rule deployment and vulnerable component isolation"

**Strategic Considerations:**
- Playbooking is expensive (10 Budget) but provides large bonus (+3)
- You can only use each playbook once, and only create two per game (v2.2) — plan carefully
- Encourages predicting which threats are most dangerous
- Reflects real-world incident response playbook development
- Playbooks alone cannot win the game: victory requires **at least 4 deployed defenses** (v2.2)

---

### Action 4: Test & Drill Defenses 🎯

**Cost:** 0 Budget (represents time investment)
**Roll Required:** 11+ on d20

**How it works:**
1. Announce you're conducting a security drill
2. Choose one or more deployed defenses to test
3. For each defense, roll 1d20
4. Defenses with roll 11+ are successful; 10 or less fail

**Effect:**
- Successful tests: Defense works properly (tracked as "tested")
- Failed tests: Implementation issues found (no penalty, but noted)
- Tests don't contribute to final score but provide confidence
- Teaches the importance of validation and testing

**Educational Value:**
- Reflects real-world practice of security testing
- Validates that deployments actually work
- Low-cost way to use budget on preparation vs. initial deployment

---

## Mid-Game: Pentester Challenge

### When Pentester Tactics Are Used

Typically after turn 3 or 4, once teams have deployed initial defenses.

**Timing Options:**
- **Per turn:** One Pentester Tactic drawn each turn (turns 3-6)
- **Multiple attacks:** 2-4 Pentester Tactics total (depends on difficulty)
- **Final challenge:** All remaining Tactics drawn at end of turn 6

### Pentester Tactic Cards (PT-01 to PT-08)

**(v2.2)** The Hardening module uses the standard Pentester Tactic deck, **PT-01 to PT-08**, defined in [`cards/hardening/core-deck/pentester-tactic-cards.md`](../../cards/hardening/core-deck/pentester-tactic-cards.md). Each card is a realistic red-team technique with a printed **DC** (difficulty class) and a list of printed **defense bonuses** for specific Defense Cards.

| Card | Tactic | Target Vectors | Difficulty | Primary Defense |
|------|--------|----------------|------------|-----------------|
| PT-01 | Social Engineering - Pretexting Attack | SOCIAL_ENGINEERING, CREDENTIAL_ABUSE | BASIC (DC 12) | D-02 User Training |
| PT-02 | Malware Evasion - Living-off-the-Land | MALWARE, CREDENTIAL_ABUSE | INTERMEDIATE (DC 13) | D-08 EDR |
| PT-03 | Credential Dumping - Mimikatz | CREDENTIAL_ABUSE, MALWARE | INTERMEDIATE (DC 13) | D-16 Credential Guard |
| PT-04 | Lateral Movement - Network Traversal | NETWORK, CREDENTIAL_ABUSE | INTERMEDIATE (DC 13) | D-09 Network Segmentation |
| PT-05 | Privilege Escalation - Unpatched Kernel Exploit | MALWARE, WEB_EXPLOIT | ADVANCED (DC 14) | D-03 Patch Management |
| PT-06 | Data Exfiltration - Unmonitored Channel | DATA_EXFIL, NETWORK | ADVANCED (DC 14) | D-11 DLP |
| PT-07 | Supply Chain Compromise - Trusted Update | MALWARE, WEB_EXPLOIT | ADVANCED (DC 14) | D-08 EDR / D-13 Threat Hunting |
| PT-08 | Insider Threat - Malicious Administrator | CREDENTIAL_ABUSE, DATA_EXFIL, NETWORK | EXPERT (DC 15) | D-22 SIEM / D-20 Zero Trust |

For expansion play, 8 additional tactics (PT-09 to PT-16) are available in [`cards/hardening/expansion-deck/advanced-tactics.md`](../../cards/hardening/expansion-deck/advanced-tactics.md).

---

### Attack Resolution: One Canonical Formula (v2.2)

When a Pentester Tactic Card is drawn:

**1. Threat Orchestrator Describes the Attack**

> Example (PT-01): "A pentester calls your IT helpdesk impersonating a VIP executive, demanding emergency access to critical systems..."

**2. Blue Team Chooses ONE Deployed Defense to Resolve With**

> Example: "We resolve this with our User Security Training (D-02) — staff are trained to verify callers."

**3. Roll the Defense Roll**

> **Defense roll = d20 + printed defense bonus for the chosen defense (from the tactic card's bonus list) + hardening upgrades on that defense (+2 each) + relevant playbook (+3, one-time, matching vector)**
>
> **Success if the total ≥ the tactic card's printed DC.**

Notes:
- Only ONE defense's printed bonus applies per roll. If your chosen defense isn't on the tactic's bonus list, its printed bonus is +0 (upgrades and playbooks still apply).
- **Multi-vector or multi-phase tactics** (e.g., PT-09): resolve each vector/phase as a **separate roll**, one chosen defense per roll.
- Playbooks are discarded after use.

**4. Worked Example**

```
Tactic: PT-01 Social Engineering - Pretexting (DC 12)
Chosen defense: D-02 User Security Training (printed bonus +2 vs PT-01)
D-02 has 1 hardening upgrade (+2)
SOCIAL ENGINEERING playbook available (+3)

Roll 1d20 = 7
Total = 7 + 2 (printed) + 2 (upgrade) + 3 (playbook) = 14
14 ≥ DC 12 → SUCCESS. Playbook is discarded.
```

**5. Outcome**

- **Success:** Defense holds; count it as a **Pentester Tactic Defended** (+5 Security Score); attacks continue
- **Failure:** Attack succeeds; apply the consequence printed on the tactic card; no score for this tactic; attacks continue

*(v2.2: the old -10 Reputation penalty has been removed from Hardening — failed defenses simply score nothing and trigger the card's printed consequence. Reputation remains a Disaster Recovery mechanic.)*

---

## Scoring: Security Score Calculation

### Final Security Score Formula (v2.2 — one formula, used in both rules and standalone guide)

```
Security Score = (Defenses Deployed × 5)
               + (Hardening Upgrades × 2)
               + (Playbooks Created × 10)      [max 2 playbooks]
               + (Pentester Tactics Defended × 5)
               + (Budget Remaining / Starting Budget) × 10
```

### Example Scoring (7 turns, 150 starting budget)

```
Turn 1: Deploy D-01 Email Auth + D-02 User Training (2 BASIC as one action)  -20
Turn 2: Deploy D-04 Firewall Rules + D-19 Backup & DR (2 BASIC)              -20
Turn 3: Deploy D-08 EDR (ADVANCED)                                           -15
        → PT-02 strikes: defended ✓
Turn 4: Deploy D-09 Network Segmentation (ADVANCED)                          -15
Turn 5: Create MALWARE playbook                                              -10
        → PT-01 strikes: defended ✓
Turn 6: Harden D-08 EDR (+2)                                                  -5
Turn 7: Deploy D-11 DLP (ADVANCED)                                           -15
        → PT-06 strikes: defended ✓ (D-11's printed +4 bonus vs DC 14 carried the roll)

Budget spent: 100 → 50 remaining

Defenses Deployed:      7 × 5  = 35 points
Hardening Upgrades:     1 × 2  =  2 points
Playbooks Created:      1 × 10 = 10 points
Tactics Defended:       3 × 5  = 15 points
Budget Efficiency: (50/150) × 10 ≈ 3 points
─────────────────────────────────────
FINAL SECURITY SCORE:            65 points → Strong (Victory)
```

### Security Score Tiers (v2.2 — rescaled for the 7-action economy)

| Score | Level | Interpretation | Real-World Equivalent |
|-------|-------|-----------------|----------------------|
| **75+** | Exceptional | Enterprise-grade security posture | Large financial institution |
| **60-74** | Strong | Comprehensive defense-in-depth | Mid-market company |
| **45-59** | Adequate | Basic layered protection | Startup/small business |
| **30-44** | Weak | Minimal defenses, significant gaps | Under-resourced organization |
| **Below 30** | Vulnerable | Inadequate protection, likely to fail | High-risk organization |

---

## Winning & Losing Hardening

### Victory Condition ✓ (v2.2)

**Blue Team Wins Hardening if ALL of:**
- **Final Security Score ≥ 60** (strong, comprehensive defense-in-depth)
- **AND at least 4 defenses deployed** (playbooks and upgrades alone cannot win)
- **AND majority of Pentester Tactics defended against** (defenses actually work)

**Interpretation:** Team successfully built layered, effective defenses within constraints.

### Defeat Condition ✗

**Blue Team Loses Hardening if:**
- **Final Security Score < 45** (inadequate overall protection)
- **OR Budget exhausted** before completing hardening strategy
- **OR majority of Pentester Tactics succeeded** (defenses aren't effective)

**Interpretation:** Defenses are insufficient against realistic threats.

Scores between 45 and 59 that meet the tactic/defense requirements count as a **partial success** — adequate protection with room to improve.

---

## Difficulty Levels

All difficulty levels run **7 turns** (v2.2); difficulty scales via Pentester Tactic count.

### Beginner Hardening
- **Starting Budget:** 150
- **Pentester Tactics:** 2 cards
- **Turn Limit:** 7 turns
- **Best For:** First-time players, teaching core mechanics
- **Focus:** Deploy basic defenses, understand layering

### Intermediate Hardening
- **Starting Budget:** 150
- **Pentester Tactics:** 3 cards
- **Turn Limit:** 7 turns
- **Best For:** Standard play, balanced challenge
- **Focus:** Balance deployment, upgrades, and playbooks

### Advanced Hardening
- **Starting Budget:** 150
- **Pentester Tactics:** 4 cards
- **Turn Limit:** 7 turns
- **Best For:** Experienced players, comprehensive strategy
- **Focus:** Optimize defense layers, predict threats, handle complexity

### Expert: Continuation from Incident Response (Loss)
- **Starting Budget:** Carry over from IR (may be low)
- **Pentester Tactics:** 4 cards (harder variants, may include PT-09 to PT-16)
- **Turn Limit:** 7 turns
- **Best For:** Advanced play, realistic recovery scenarios
- **Focus:** Harden after breach, limited resources

---

## Tips for Threat Orchestrators

### Balancing Defense Deployment

**Too Easy:**
- Teams deploy 8+ defenses with large budget remaining
- Almost all Pentester Tactics fail
- No meaningful decisions required
- Game feels trivial

**Too Hard:**
- Teams can only afford 3-4 defenses with budget exhausted
- Almost all Pentester Tactics succeed
- Team feels overwhelmed
- Frustration rather than learning

**Just Right (within 7 actions and 150 Budget):**
- Teams deploy 5-7 defenses with some budget remaining (the Quick-Win rule for BASIC pairs makes this achievable)
- 50-70% of Pentester Tactics fail (defenses work)
- Teams debate priorities and trade-offs
- Players learn through strategic choices

**Adjustments:**
- Lower budget (100) for harder game
- Higher budget (200) for easier game
- Fewer/more Pentester Tactics
- Provide feedback: "Your defenses are working well" or "Your SIEM isn't catching these"

### Using Pentester Tactics Effectively

**Timing:** Draw first tactic after turn 3-4 (let teams deploy initial defenses)

**Narrative:** Always frame tactics as specific scenarios:
- "Your red team just attempted a supply chain attack..."
- "An advanced attacker is using living-off-the-land techniques..."
- "A coordinated insider attack is beginning..."

**Strategy:** Escalate difficulty
- Turns 1-2: No tactics (deployment phase)
- Turn 3: First tactic (softer: PT-01, DC 12)
- Turn 4: Second tactic (medium: PT-02 to PT-04, DC 13)
- Turn 5+: Third/fourth tactics (harder: PT-05 to PT-08, DC 14-15)

### Common Teaching Moments

**Defense-in-Depth:** When a chosen defense earns only a +0/+1 printed bonus, discuss why layers matter
**Cost-Benefit:** Teams overspend on Elite defenses; discuss Advanced alternatives
**Upgrades:** Teams ignore upgrades; show how +2 bonuses compound
**Playbooks:** Teams underestimate playbooks; demonstrate their power (+3 bonus) — and note the 2-per-game cap

---

## Extensions & Variations

### Extended Hardening (60 minutes)
- Start with Budget: 200
- Play 9 turns (instead of 7)
- 5-6 Pentester Tactics (instead of 2-4)
- Raise the playbook cap to 3
- More complex strategic decisions

### Compliance-Enhanced Hardening
- Add compliance requirements (PCI-DSS, HIPAA, etc.)
- Some defenses count toward compliance
- Score includes compliance satisfaction
- Teams balance security and regulatory needs

### Competitive Hardening Tournament
- Multiple teams hardening simultaneously
- Same starting conditions
- Highest Security Score wins
- Tiebreaker: Most Budget remaining

### Defense Architecture Detailed Play
- Focus on how defenses work together
- Create explicit layers: Prevention, Detection, Response
- Score based on how well layers complement each other
- More discussion-based, less combat-focused

---

## Educational Objectives

| Learning Goal | How Module Teaches It |
|---------------|----------------------|
| Defense-in-depth concept | Deploy multiple layers, see some fail while others succeed |
| Resource prioritization | Limited budget forces choices between defenses |
| Trade-offs in security | BASIC cheap but weak vs. ELITE expensive but strong |
| Proactive vs. reactive | Hardening teaches prevention vs. IR's response focus |
| Layering effectiveness | Pentester Tactics show how weak defenses alone fail |
| Incident playbooks | Playbook mechanic teaches the value of preparation |
| Security architecture | Thoughtful defense selection teaches how to think architecturally |
| Cost-benefit analysis | Every budget point spent has consequences |

---

## Quick Reference: Actions & Costs

| Action | Cost | Roll | Effect | Score |
|--------|------|------|--------|-------|
| **Deploy Defense** | 10/15/25 | None | Active immediately (up to 2 BASIC per action, v2.2) | +5 each |
| **Harden Upgrade** | 5 | None | +2 effectiveness | +2 |
| **Create Playbook** | 10 | None | One-time +3 bonus (max 2 per game, v2.2) | +10 |
| **Test & Drill** | 0 | 11+ | Validates defense | +0 |

**Pentester defense roll (v2.2):** d20 + printed bonus (one chosen defense) + upgrades (+2 each) + playbook (+3) ≥ tactic DC. Each tactic defended: +5 Score.

---

## Continuing to Other Modules

**After Winning Hardening:**
- Continue to **Incident Response** (test your defenses)
- Continue to **Audit & Compliance** (verify your hardening)
- Play again with new threat vectors

**After Losing Hardening:**
- Replay with different strategy
- Try higher budget variation
- Study which Pentester Tactics caused most losses
- Plan for those tactics in next iteration

---

## v2.2 Playtest Edition Changes

Changes for playtesters to validate, and why they were made:

1. **Pentester Tactics unified to the PT-01–PT-08 deck.** The 8 tactics previously embedded in this document (Bypass Basic Defenses, Zero-Day, etc.) are replaced by the printed card deck in `cards/hardening/core-deck/pentester-tactic-cards.md`. This removes duplicate, conflicting tactic definitions (including a "Persistence Expert" tactic that referenced a nonexistent PERSISTENCE vector).
2. **One canonical resolution formula.** Defense roll = d20 + printed defense bonus for ONE chosen defense (per the tactic card) + hardening upgrades on that defense (+2 each) + relevant playbook (+3), vs. the tactic's printed DC. The old "+2 to +4 by tier", "roll 11+/13+", and multi-defense "synergy stacking" texts are removed. **Validate:** do DCs 12-15 feel fair with the printed bonuses?
3. **Fixed turn count: 7 turns, one action per turn**, plus the **Quick-Win rule** (deploy up to 2 BASIC defenses as one action). **Validate:** can teams realistically field 5-7 defenses in 7 actions?
4. **Single scoring formula** (shared with the standalone guide) including Pentester results and budget efficiency; tiers rescaled (win at 60+). Reputation removed from Hardening scoring — failed tactics simply score 0 and trigger their printed consequence.
5. **Anti-playbook-spam:** playbooks capped at **2 per game**, and victory requires **≥4 deployed defenses**.

**Designer note — why playbook spam can't win (v2.2 math):**
- *Playbook-spam strategy:* 2 playbooks (cap) = 20 pts; 0 defenses = 0 pts; with no deployed defenses every Pentester roll is d20 + 0 (+3 once per playbook) vs DC 12-15, so expect ~1 of 3 tactics defended = 5 pts; budget efficiency (130/150) × 10 ≈ 9 pts. **Total ≈ 34** — below the 60 threshold, and it fails the ≥4-defenses gate regardless. **Cannot win.**
- *Balanced layered strategy:* 7 defenses (35) + 1 upgrade (2) + 1 playbook (10) + 3 of 3 tactics defended (15) + budget efficiency (50/150 × 10 ≈ 3) = **65 → Victory.** See the worked example above.

---

## Need Help?

- **Questions about Incident Response?** See [Module: Incident Response](module-incident-response.md)
- **Want to play multiple modules?** See [Module Combinations](../module-combinations.md)
- **Understanding framework?** See [Framework](../FRAMEWORK.md)

---

*Hardening Module - Complete Rules*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.2 - Playtest Edition*
