# Hardening Module: Complete Rules

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
| **Time Pressure** | High (10 turns, 100 budget) | Lower (5-7 turns, carries budget forward) |
| **Actions** | Investigate, Deploy, Emergency Response | Deploy, Upgrade, Playbook, Test |
| **Rolls Needed** | Investigation & Defense deployments | Playbook tests only (attacks use rolls) |
| **Scoring** | Detection efficiency | Defense layering & breadth |
| **Threats** | Hidden chain | Known vectors, Pentester tactics |

---

## Setup

### Step 1: Determine Your Context

#### Option A: Standalone Play (Fresh Start)
Generate threat context from scratch:
- Roll 1d4 for each threat vector (1-2=absent, 3=intermediate, 4=advanced)
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
- **Playbooks Created:** 0 (track total count)
- **Deployed Defenses:** [] (track list on paper/whiteboard)

### Step 3: Prepare Card Decks

- **Defense Cards Deck:** Shuffle all available cards
- **Pentester Tactic Cards:** Set aside 2-4 cards (by difficulty level)
- **Asset Cards:** Place relevant systems on table (Email Server, Database, Workstations, etc.)

### Step 4: Deal Starting Hand

Each Blue Team receives **5 Defense Cards** (drawn randomly, face down in hand)

### Step 5: Read Opening Narrative

Threat Orchestrator provides context for the hardening scenario:

> "Your detection team successfully identified an attack chain. Now you have time and resources to harden your defenses to prevent similar attacks in the future. Here's what you're defending against and what assets are at risk..."

---

## Gameplay: 5-7 Turns

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

**Examples:**
- Deploy Multi-Factor Authentication (ADVANCED - 15 Budget) on VPN access
- Deploy EDR on all workstations (ADVANCED - 15 Budget)
- Deploy Data Loss Prevention (DLP) on network gateways (ADVANCED - 15 Budget)
- Deploy Email Authentication (BASIC - 10 Budget) on email systems

**Strategic Notes:**
- BASIC defenses (10 Budget) are cheaper but less effective against Pentester Tactics
- ADVANCED defenses (15 Budget) provide good balance of cost/effectiveness
- ELITE defenses (25 Budget) are expensive but strongest against Pentester Tactics

---

### Action 2: Harden an Existing Defense ⬆️

**Cost:** 5 Budget per upgrade
**Roll Required:** None

**How it works:**
1. Choose a Defense Card already deployed (from Phase 1 or current turn)
2. Pay 5 Budget
3. Mark defense with **+2 effectiveness bonus** (track on paper)
4. Optional: Describe the hardening (e.g., "Tuning behavioral analytics in EDR")

**Effect:**
- Defense effectiveness increases by +2
- Bonuses stack (EDR with three upgrades = +6 total)
- Counts toward Security Score (2 points per upgrade)
- Makes defense more resistant to Pentester Tactics

**Examples of Hardening:**
- "Harden our MFA by requiring hardware tokens instead of SMS" → EDR now has +2
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
- You can only use each playbook once (plan carefully)
- Encourages predicting which threats are most dangerous
- Reflects real-world incident response playbook development

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
- **Final challenge:** All remaining Tactics drawn at end of turn 5

### Pentester Tactic Cards (8 Total)

Each card represents a specific attack technique the red team attempts to execute against the Blue Team's hardened defenses.

#### Tactic 1: "Bypass Basic Defenses"

```
PENTESTER TACTIC: BYPASS BASIC DEFENSES

Effect: Choose one BASIC-tier (10 Budget) Defense Card that the Blue
Team deployed. That defense is bypassed and cannot be used for this
attack.

Example: The team's basic antivirus is proven ineffective against
this malware variant; EDR is available as alternative defense.

Strategic Impact: Forces teams to layer defenses, not rely solely on
cheap tools. Teaches defense-in-depth.
```

#### Tactic 2: "Social Engineering Specialist"

```
PENTESTER TACTIC: SOCIAL ENGINEERING SPECIALIST

Effect: The next attack targeting a SOCIAL ENGINEERING vector gains
+2 to the Blue Team's defense roll difficulty (they must roll 13+
instead of 11+).

Example: Highly skilled social engineer uses psychological tactics
that are harder to stop.

Strategic Impact: Reminds teams that user training must be continuous;
one-time training wears off.
```

#### Tactic 3: "Persistence Expert"

```
PENTESTER TACTIC: PERSISTENCE EXPERT

Effect: If the Pentester successfully lands a PERSISTENCE attack,
create a hidden persistent threat card. Blue Team must spend 15 Budget
to remediate it.

Example: Attacker installs sophisticated persistence mechanism that
costs extra effort to remove.

Strategic Impact: Teaches the cost of advanced persistent threats and
why early detection is critical.
```

#### Tactic 4: "Supply Chain Attack"

```
PENTESTER TACTIC: SUPPLY CHAIN ATTACK

Effect: Choose one Defense Card deployed by the Blue Team. That
defense is temporarily compromised and cannot be used for this attack.

Example: One of your security tools itself is compromised; you cannot
rely on it for this attack.

Strategic Impact: Highlights risk from third-party dependencies and
importance of vendor security assessments.
```

#### Tactic 5: "Detection Evasion"

```
PENTESTER TACTIC: DETECTION EVASION

Effect: The next attack targeting a MALWARE vector bypasses SIEM and
EDR detection benefits for this attack. (Blue Team doesn't get the
+2 bonus from those defenses).

Example: Advanced malware using evasion techniques that bypass your
detection tools.

Strategic Impact: Teaches that no single defense is foolproof; layering
and redundancy are essential.
```

#### Tactic 6: "Budget Drain - Incident Response Overload"

```
PENTESTER TACTIC: BUDGET DRAIN - INCIDENT RESPONSE OVERLOAD

Effect: Blue Team's next Defense deployment costs +10 Budget overhead
from emergency response.

Example: Managing the "attack" consumes resources; new deployments
are more expensive and slow.

Strategic Impact: Reminds teams that incident response is expensive;
prevention is cheaper than cure.
```

#### Tactic 7: "Zero-Day Exploit"

```
PENTESTER TACTIC: ZERO-DAY EXPLOIT

Effect: For this attack, Blue Team's roll difficulty increases by 3
(they need 14+ instead of 11+). Playbooks cannot be used for this
attack (exploit is new/unknown).

Example: Brand new vulnerability with no known defense; teams must
improvise.

Strategic Impact: Emphasizes that no defense is perfect; teams must
assume breach and have detection/recovery plans.
```

#### Tactic 8: "Multi-Vector Attack"

```
PENTESTER TACTIC: MULTI-VECTOR ATTACK

Effect: The Pentester attacks two different threat vectors simultaneously.
Blue Team must defend against both or loses -10 Reputation on one
undefended vector.

Example: Coordinated attack using phishing + malware simultaneously;
team must split resources.

Strategic Impact: Teaches that coordinated attacks are harder to defend
against; holistic, layered strategies are essential.
```

---

### Attack Resolution: Step-by-Step

When a Pentester Tactic Card is drawn:

**1. Threat Orchestrator Describes the Attack**

```
Example: "The attacker is sending a sophisticated phishing email
with a malicious PDF attachment to multiple users. The email appears
to come from your CFO requesting an urgent budget approval."
```

**2. Tactic Card Effects Apply**

```
Example (Social Engineering Specialist tactic active):
"Social engineering is highly skilled; your team's defense roll
difficulty is +2 (you need 13+ instead of 11+)"
```

**3. Blue Team Chooses a Defense**

```
Example: "We'll use our User Security Training defense combined
with our Email Authentication to stop this"
```

**4. Roll with Modifiers**

```
Base: Roll 11+ on d20
- Apply Tactic Card penalties/bonuses
- Apply Hardening bonuses (+2 per upgrade)
- Apply Playbook bonuses (+3 if matching vector)

Example:
Roll 1d20 = 9
Base needed: 11
Tactic penalty: +2 (need 13+)
Hardening bonus on chosen defense: +2
Playbook bonus (SOCIAL ENGINEERING): +3
─────────────────
Modified roll: 9 + 2 + 3 = 14 ✓ SUCCESS (14 ≥ 13)
```

**5. Outcome**

- **Success:** Defense holds; no reputation loss; attacks continue
- **Failure:** Attack succeeds; -10 Reputation (represents incident); attacks continue

---

## Scoring: Security Score Calculation

### Final Security Score Formula

```
Security Score = (Defenses Deployed × 5)
               + (Hardening Upgrades × 2)
               + (Playbooks Created × 10)
               - (Reputation Lost)
```

### Example Scoring

```
Scenario: 150 starting budget, 4 turns played

Defenses Deployed: 7
  Email Auth (BASIC): 5 points
  MFA (ADVANCED): 5 points
  EDR (ADVANCED): 5 points
  SIEM (ADVANCED): 5 points
  Network Segmentation (ADVANCED): 5 points
  DLP (ADVANCED): 5 points
  Threat Hunting (ELITE): 5 points
  ────────────────────────
  Total: 7 × 5 = 35 points

Hardening Upgrades: 6 upgrades
  EDR upgraded 3 times: 6 points
  MFA upgraded 2 times: 4 points
  SIEM upgraded 1 time: 2 points
  ─────────────────────
  Total: 6 × 2 = 12 points

Playbooks Created: 2
  SOCIAL ENGINEERING playbook: 10 points
  MALWARE playbook: 10 points
  ──────────────────
  Total: 2 × 10 = 20 points

Pentester Tactics: Defended against 3 of 4
  Won 3 defense rolls: 0 reputation loss
  Lost 1 defense roll: -10 reputation

─────────────────────────────────────
FINAL SECURITY SCORE: 35 + 12 + 20 - 10 = 57 points
```

### Security Score Tiers

| Score | Level | Interpretation | Real-World Equivalent |
|-------|-------|-----------------|----------------------|
| **90-100+** | Exceptional | Enterprise-grade security posture | Large financial institution |
| **70-89** | Strong | Comprehensive defense-in-depth | Mid-market company |
| **50-69** | Adequate | Basic layered protection | Startup/small business |
| **30-49** | Weak | Minimal defenses, significant gaps | Under-resourced organization |
| **Below 30** | Vulnerable | Inadequate protection, likely to fail | High-risk organization |

---

## Winning & Losing Hardening

### Victory Condition ✓

**Blue Team Wins Hardening if:**
- **Final Security Score ≥ 70** (strong, comprehensive defense-in-depth)
- **AND Budget remaining ≥ 10** (resourceful allocation, not overspent)
- **AND majority of Pentester Tactics defended against** (defenses actually work)

**Interpretation:** Team successfully built layered, effective defenses within constraints.

### Defeat Condition ✗

**Blue Team Loses Hardening if:**
- **Final Security Score < 40** (inadequate overall protection)
- **OR Budget exhausted** before completing hardening strategy
- **OR majority of Pentester Tactics succeeded** (defenses aren't effective)

**Interpretation:** Defenses are insufficient against realistic threats.

---

## Difficulty Levels

### Beginner Hardening
- **Starting Budget:** 150
- **Pentester Tactics:** 2 cards
- **Turn Limit:** 5 turns
- **Best For:** First-time players, teaching core mechanics
- **Focus:** Deploy basic defenses, understand layering

### Intermediate Hardening
- **Starting Budget:** 150
- **Pentester Tactics:** 3 cards
- **Turn Limit:** 6 turns
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
- **Pentester Tactics:** 4 cards (harder variants)
- **Turn Limit:** 5 turns (limited recovery time)
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

**Just Right:**
- Teams deploy 5-7 defenses with some budget remaining
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
- "An advanced attacker is using detection evasion techniques..."
- "A coordinated multi-vector attack is beginning..."

**Strategy:** Escalate difficulty
- Turns 1-2: No tactics (deployment phase)
- Turn 3: First tactic (softer: "Bypass Basic Defenses")
- Turn 4: Second tactic (medium: "Social Engineering Specialist")
- Turn 5+: Third/fourth tactics (harder: "Zero-Day", "Multi-Vector")

### Common Teaching Moments

**Defense-in-Depth:** When a basic defense is bypassed, discuss why layers matter
**Cost-Benefit:** Teams overspend on Elite defenses; discuss Intermediate alternatives
**Upgrades:** Teams ignore upgrades; show how +2 bonuses compound
**Playbooks:** Teams underestimate playbooks; demonstrate their power (+3 bonus)

---

## Extensions & Variations

### Extended Hardening (60 minutes)
- Start with Budget: 200
- Play 7-8 turns (instead of 5-7)
- 5-6 Pentester Tactics (instead of 2-4)
- Allow team to create 4-5 playbooks
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
| **Deploy Defense** | 10/15/25 | None | Active immediately | +5 |
| **Harden Upgrade** | 5 | None | +2 effectiveness | +2 |
| **Create Playbook** | 10 | None | One-time +3 bonus | +10 |
| **Test & Drill** | 0 | 11+ | Validates defense | +0 |

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

## Need Help?

- **Questions about Incident Response?** See [Module: Incident Response](module-incident-response.md) (future)
- **Want to play multiple modules?** See [Module Combinations](../module-combinations.md)
- **Understanding framework?** See [Framework](../FRAMEWORK.md)

---

*Hardening Module - Complete Rules*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.1 - Balanced & Refined Edition*

