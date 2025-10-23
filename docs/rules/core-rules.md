# Incident Zero: Core Rules & Mechanics

**Version:** 2.1 - Balanced & Refined Edition
**Last Updated:** October 2025

---

## Core Concept 🎯

**Incident Zero** is a modular cybersecurity board game for 2+ players designed for educational environments. One player acts as the **Threat Orchestrator (TO)** (the facilitator), while all other players form **Blue Teams** (the Defenders).

### How It Works

Players choose which **module** to play based on learning objectives:

1. **Incident Response Module** - Detect and investigate hidden attack chains (30-45 min)
2. **Hardening Module** - Build defense-in-depth (30-45 min)
3. **Disaster Recovery Module** - Manage breach crisis (30-45 min)
4. **Network Building Module** - Design secure networks (30-45 min)
5. **Audit & Compliance Module** - Conduct security assessments (30-45 min)

Modules can be played **solo** or **combined in any sequence** using the modifier generation procedures documented in [FRAMEWORK.md](../FRAMEWORK.md).

---

## Game Components (Universal)

### Card Types

#### Threat Cards
Represent attacker actions. Each card includes:
- **Title:** e.g., "Phishing Campaign"
- **Attack Chain Step:** `INITIAL COMPROMISE`, `PIVOT & ESCALATE`, `PERSISTENCE`, or `C2 & EXFIL`
- **Attack Vector:** `SOCIAL ENGINEERING`, `WEB EXPLOIT`, `CREDENTIAL ABUSE`, `MALWARE`, `NETWORK`, or `DATA EXFIL`
- **Clue:** Descriptive text for the Threat Orchestrator
- **Why This Works:** Educational explanation (revealed after discovery)

**Deck Composition:**
- **12 Base Threat Cards** (see [cards/core-deck/threat-defense-cards.md](../../cards/core-deck/threat-defense-cards.md))
- **8 Expansion Threat Cards** (see [cards/expansion-decks/advanced-threats.md](../../cards/expansion-decks/advanced-threats.md))

---

#### Defense Cards
Represent security controls. Each card includes:
- **Title:** e.g., "Multi-Factor Authentication"
- **Countermeasure Vector:** One of the six attack vectors
- **Tier:** BASIC (10 Budget), ADVANCED (15 Budget), or ELITE (25 Budget)
- **Description:** What the defense does and when it applies

**Deck Composition:**
- **24 Base Defense Cards** (see [cards/core-deck/threat-defense-cards.md](../../cards/core-deck/threat-defense-cards.md))
- **Variable Expansion Defenses** (see [cards/expansion-decks/advanced-defenses.md](../../cards/expansion-decks/advanced-defenses.md))

**Examples:**
- BASIC: Email Authentication Setup, User Security Training, Firewall Rules (10 Budget)
- ADVANCED: Multi-Factor Authentication, EDR, Network Segmentation (15 Budget)
- ELITE: Threat Hunting, Memory Forensics, Deception Technology (25 Budget)

---

#### Pentester Tactic Cards
Represent sophisticated attack techniques used in Hardening module (and potentially others).

**8 Total Tactics:**
1. Bypass Basic Defenses
2. Social Engineering Specialist
3. Persistence Expert
4. Supply Chain Attack
5. Detection Evasion
6. Budget Drain - Incident Response Overload
7. Zero-Day Exploit
8. Multi-Vector Attack

See [module-hardening.md](module-hardening.md#pentester-tactic-cards-8-total) for full descriptions.

---

#### Asset Cards
Simple cards providing scenario context. Examples:
- Email Server
- Customer Database
- Domain Controller
- Web Application
- Backup System
- Developer Workstation

---

### Game Materials Required

**Physical Components:**
- One 20-sided die (d20)
- Turn Tracker (paper or board, counts 1-12+)
- Budget Tracker (shows 0-150+)
- Reputation/Security Score Tracker (shows 0-100)
- Uncontained Threats Tracker (shows 0-5)
- Tokens or counters (for tracking upgrades, penalties)

**Optional:**
- Score sheets (printable or paper)
- Playbook tracking sheet
- Stakeholder communication log (for Disaster Recovery)

---

## Universal Game Mechanics

### 1. The d20 Roll System

**When Used:** Investigation, Defense Deployment, Negotiation, and similar actions that have uncertain outcomes.

**How It Works:**
1. Player announces action and parameters
2. Player rolls 1d20 (one 20-sided die)
3. Compare result to target number (usually 11+) plus modifiers
4. Success if: `roll + modifiers ≥ target number`

**Example:**
```
Action: Investigate email headers
Target: 11+
Roll: 7
Modifiers: +2 (technical justification) +1 (referenced Splunk)
Calculation: 7 + 2 + 1 = 10
Result: FAIL (10 < 11)
```

---

### 2. Budget System (Universal)

**What is Budget?**
Abstract resource representing time, money, personnel, and tools. Spent to take actions, buy defenses, or conduct investigations.

**Budget Allocation by Module:**
- **Incident Response:** Start at 100
- **Hardening:** Start at 150 (or carry over from IR)
- **Disaster Recovery:** Start at 50 (emergency fund)
- **Network Building:** Start at 150
- **Audit & Compliance:** Start at 100

**Budget Spending:**
- **Investigate action:** 5 Budget
- **Deploy Defense:** 10/15/25 Budget (by tier)
- **Emergency Response (IR):** 25 Budget
- **Harden Upgrade (Hardening):** 5 Budget
- **Create Playbook (Hardening):** 10 Budget
- **Forensic Investigation (DR):** 5-15 Budget
- **Stakeholder Communication (DR):** 0-10 Budget
- **Evidence Preservation (DR):** 5-20 Budget
- **Remediation (DR):** 10-25 Budget
- **Ransom Payment (DR):** 10-30 Budget

**Budget = 0:** Team loses (cannot take further actions)

---

### 3. Turn System (Universal)

**Turns represent:** Time passing in the game world (6 hours, 30 minutes, or abstract unit depending on module)

**Turn Sequence:**
1. **Start of Turn:** Penalties applied, trackers announced
2. **Planning Phase:** Team discusses strategy (2-3 min)
3. **Action Phase:** Execute chosen action, resolve rolls
4. **End of Turn:** Advance tracker, draw card, check events

**Turn Limits by Module:**
- **Incident Response:** 10 turns (hard limit)
- **Hardening:** 5-7 turns
- **Disaster Recovery:** 7 turns (hard limit, represents 48 hours)
- **Network Building:** 5-8 turns
- **Audit & Compliance:** 6-8 turns

---

### 4. Roll Modifiers (Universal)

All modules use the same modifier system for consistency:

#### +2 Bonus: Strong Technical Justification
Awarded when a player provides clear, specific reasoning for their action using real security concepts.

**Examples:**
- "We're analyzing email headers in the mail gateway logs to identify the true sender IP and check it against threat intelligence feeds"
- "We're deploying EDR on all endpoints because it can detect living-off-the-land techniques"
- "We're querying our SIEM for scheduled task creation events because attackers use them for persistence"

**Criteria:**
- References specific tools (Splunk, EDR, SIEM, etc.)
- Explains methodology (why this approach works)
- Shows understanding of the threat being addressed

---

#### +1 Bonus: Real Tools or Techniques Referenced
Awarded when player references actual security tools or real attack/defense techniques.

**Examples:**
- "We'll use Wireshark to analyze the network traffic"
- "We're checking for Mimikatz usage in memory"
- "We're reviewing EDR telemetry"
- "We're looking for this specific CVE exploitation pattern"

**Criteria:**
- References real tools (Wireshark, EDR, Splunk, etc.)
- References real techniques (MITRE ATT&CK, specific CVEs)
- Shows awareness of how things actually work

---

### 5. Uncontained Threats Penalty (Incident Response Module)

**When Applied:** Incident Response module only, applied at START of each turn

**How It Works:**
1. When a threat card is **revealed**, add 1 to Uncontained Threats Tracker
2. At START of each turn, deduct **5 Budget per uncontained threat**
3. When **next card in chain is revealed**, previous threat is auto-mitigated (-1 from tracker)
4. When **Emergency Response action is used**, remove a revealed threat (-1 from tracker)

**Purpose:** Creates urgency - dwell time costs money. Teaches real-world incident response costs.

**Example:**
```
Turn 1: Phishing revealed → Uncontained Threats = 1
Turn 2: START → Deduct 5 Budget (99 remaining)
Turn 3: Lateral Movement revealed → Phishing auto-mitigated (Uncontained = 1)
Turn 3: START → Deduct 5 Budget
Turn 4: Emergency Response on Lateral Movement → Uncontained Threats = 0
```

---

## Common Roles & Responsibilities

### Threat Orchestrator (Facilitator)

**Responsibilities:**
- Manage game state and track turns/budget
- Describe scenarios and outcomes
- Roll dice when action outcomes are uncertain
- Guide the narrative

**During Incident Response:**
- Create and manage hidden attack chain
- Provide clues based on successful investigations
- Control Uncontained Threats penalties
- Be fair but challenging

**During Other Modules:**
- Describe threat context and defenses
- Draw Pentester Tactic cards (Hardening)
- Manage timeline and deadlines (Disaster Recovery)
- Guide debrief questions

**Universal Tips:**
- Explain *why* actions succeed or fail
- Ask clarifying questions about player strategy
- Balance challenge with learning
- Provide constructive feedback

---

### Blue Team (Defenders)

**Responsibilities:**
- Discuss strategy as a team
- Choose one action per turn
- Justify your decisions (gain +2 modifier)
- Manage budget carefully
- Learn from success and failure

---

## Modifier Stacking Rules

**Key Rule:** Modifiers are **additive** and can stack.

**Example (Hardening Module):**
```
Pentester Attack: Detection Evasion (adds +2 to difficulty)
Base roll needed: 11+
With tactic: 13+

Team's defense has:
- Hardening upgrade: +2
- Hardening upgrade: +2
- Playbook bonus: +3

Roll needed: 13+ (from tactic)
Team's total bonus: +7
Effective roll needed: 6+ (13 - 7)

If team rolls 8:
8 + 7 (bonuses) = 15 ≥ 6 = SUCCESS
```

---

## Difficulty & Scaling

### By Attack Chain Length

| Length | Difficulty | Best For |
|--------|-----------|----------|
| **3 cards** | Beginner | Learning mechanics, 30 min sessions |
| **4 cards** | Intermediate | Standard play, 40 min sessions |
| **5 cards** | Advanced | Challenge play, full kill chain |

---

### By Starting Budget

| Budget | Difficulty | Best For |
|--------|-----------|----------|
| **60** | Hard | Resource scarcity, tough choices |
| **100** | Standard | Balanced play, most scenarios |
| **150+** | Easy | Strategic depth, multiple options |

---

### By Turn Limit

| Turns | Difficulty | Best For |
|-------|-----------|----------|
| **8** | Hard | Time pressure, fast play |
| **10** | Standard | Balanced, most scenarios |
| **12** | Easy | Exploration, learning |

---

## Educational Objectives

### By Module

| Module | Primary Learning | Secondary Learning |
|--------|-----------------|-------------------|
| **Incident Response** | Cyber kill chain, attack detection, investigation | Resource prioritization, incident response |
| **Hardening** | Defense-in-depth, layering, proactive security | Cost-benefit analysis, security architecture |
| **Disaster Recovery** | Crisis management, stakeholder communication | Risk assessment, incident cost |
| **Network Building** | Network design, asset security, architecture | Infrastructure hardening, threat modeling |
| **Audit & Compliance** | Security assessment, governance, compliance | Risk identification, remediation prioritization |

### By Game Mechanic

| Mechanic | What It Teaches |
|----------|-----------------|
| d20 roll system | Uncertainty, risk, informed decision-making |
| Budget constraints | Resource allocation, prioritization |
| Justification bonuses | Technical reasoning, tools/techniques knowledge |
| Uncontained Threats penalty | Urgency, cost of dwell time |
| Pentester Tactics | Attacker sophistication, defense limitations |
| Playbook system | Preparation, incident response planning |
| Scoring systems | Outcome measurement, quality assessment |

---

## Cooperative vs. Competitive Play

### Cooperative Mode
- **Single Blue Team** vs. challenges
- Team wins or loses together
- Encourages discussion and consensus
- Better for learning
- Better for mixed experience levels

### Competitive Mode
- **Multiple Blue Teams** solving same challenge
- First to achieve objective wins
- Creates urgency and engagement
- Better for tournaments
- Better for same-level players

**Implementation:**
- Same setup for all teams
- Teams cannot share information (Incident Response)
- Score comparison determines winner (Hardening)
- Reputation comparison (Disaster Recovery)

---

## Debrief & Reflection (Universal)

**Every module should include a 5-15 minute debrief** with three sections:

### Part 1: What Happened?
- Summarize the scenario and outcome
- Highlight key decisions
- Acknowledge successes and failures

### Part 2: Why Did That Happen?
- Discuss the mechanisms (why the rule works that way)
- Connect to real-world security
- Explain attacker/defender motivation

### Part 3: What Would You Do Differently?
- Reflect on strategy
- Discuss trade-offs
- Plan for next playthrough

---

## Tips for Threat Orchestrators (Universal)

### Before the Game

1. **Read the module rules completely** - Know what's coming
2. **Prepare your scenario** - Pre-build attack chain or threat context
3. **Organize materials** - Sort cards, prepare trackers
4. **Know your balancing points** - Be ready to adjust difficulty if needed
5. **Practice reading clues** - Deliver them dramatically!

### During Gameplay

1. **Be clear about costs** - Announce Budget before action
2. **Resolve rolls immediately** - Announce target, let player roll, resolve
3. **Ask clarifying questions** - "Why are you investigating email headers?"
4. **Be fair but challenging** - Give honest difficulty, don't fudge rolls
5. **Narrate outcomes** - Describe what happens, not just success/failure
6. **Manage pacing** - Keep turns moving (2-3 min discussion max)
7. **Track penalties accurately** - Keep budget, turn, and threat trackers visible

### Balancing Difficulty

**Too Easy Signs:**
- Team reveals all cards/achieves goal with 40+ budget remaining
- No failed rolls
- No meaningful decisions required
- Team is bored

**Too Hard Signs:**
- Team is stuck/making no progress after 5 turns
- Multiple consecutive failed rolls
- Team frustrated rather than challenged
- No learning happening

**Adjustment Options:**
- **Easier:** Provide better clues, more starting budget, fewer tactics
- **Harder:** Less specific clues, lower budget, more tactics
- **Faster:** Shorter turn limits, simpler scenarios
- **Slower:** More turns, more complex scenarios

---

## Card Reference

For complete card descriptions and images, see:
- **Base Threat Cards** [cards/core-deck/threat-defense-cards.md](../../cards/core-deck/threat-defense-cards.md)
- **Base Defense Cards** [cards/core-deck/threat-defense-cards.md](../../cards/core-deck/threat-defense-cards.md)
- **Expansion Threats** [cards/expansion-decks/advanced-threats.md](../../cards/expansion-decks/advanced-threats.md)
- **Expansion Defenses** [cards/expansion-decks/advanced-defenses.md](../../cards/expansion-decks/advanced-defenses.md)

---

## Module-Specific Rules

For complete rules on each module:

- **Incident Response Module:** [module-incident-response.md](module-incident-response.md)
- **Hardening Module:** [module-hardening.md](module-hardening.md)
- **Disaster Recovery Module:** [module-disaster-recovery.md](module-disaster-recovery.md)
- **Network Building Module:** [module-network-building.md](module-network-building.md)
- **Audit & Compliance Module:** [module-audit-compliance.md](module-audit-compliance.md)

---

## Quick Reference: Universal Mechanics

### d20 Roll System
- **Base target:** 11+ (varies by action)
- **+2 modifier:** Strong technical justification
- **+1 modifier:** Real tools/techniques referenced
- **Modifiers stack:** All bonuses add together

### Budget System
- **Spent on:** Actions, defenses, investigations
- **Cannot go below:** 0 (team loses)
- **Tracked per turn:** Budget available announced at start of turn

### Turn System
- **Sequence:** Start → Planning → Action → End
- **Planning:** 2-3 minutes discussion
- **End of turn:** Advance tracker, draw card, apply effects

### Penalties & Bonuses
- **Uncontained Threats:** -5 Budget per threat per turn (IR only)
- **Pentester Tactics:** Add difficulty/modify actions (Hardening)
- **Reputation:** Track 0-100, affects outcome (DR)

---

## Continuing to Next Steps

**For your first game:**
1. Choose a module from [Module Combinations](../module-combinations.md)
2. Read the module-specific rules
3. Read the standalone setup guide
4. Prepare your scenario
5. Play!

**For multiple modules:**
1. Refer to [Module Combinations](../module-combinations.md) for recommended sequences
2. Refer to [FRAMEWORK.md](../FRAMEWORK.md) for modifier generation procedures
3. Play first module, generate modifiers for next
4. Continue as desired

---

## Need Help?

- **Want to combine modules?** See [Module Combinations](../module-combinations.md)
- **Understanding module flexibility?** See [FRAMEWORK.md](../FRAMEWORK.md)
- **Specific module rules?** See [module-*.md](.) files
- **How to play solo?** See standalone guide for your chosen module

---

*Incident Zero: Core Rules & Mechanics*
*v2.1 - Balanced & Refined Edition*
*Universal rules for all modules*

