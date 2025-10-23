# Incident Zero: Core Rules & Mechanics

**Version:** 2.1 - Balanced & Refined Edition
**Last Updated:** October 2025

---

## Core Concept 🎯

**Incident Zero** is a modular cybersecurity board game for 2+ players designed for educational environments. One player acts as the **Threat Orchestrator (TO)** (the facilitator), while all other players form **Blue Teams** (the Defenders).

### How It Works

Players choose which **module(s)** to play based on learning objectives:

1. **Network Building Module** - Design and secure infrastructure (30-45 min)
2. **Hardening Module** - Build defense-in-depth (30-45 min)
3. **Incident Response Module** - Detect and investigate hidden attack chains (30-45 min)
4. **Disaster Recovery Module** - Manage breach crisis (30-45 min)
5. **Forensics Module** - Investigate and attribute attacks (30-45 min) **NEW in v2.1**
6. **Audit & Compliance Module** - Conduct security assessments (30-45 min)

Modules can be played **solo** or **combined in any sequence** using the modifier generation procedures documented in [FRAMEWORK.md](../FRAMEWORK.md) and [Module Combinations](../module-combinations.md).

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

---

### 3a. Variable Game Length System (v2.1 - New!)

**Philosophy:** In real incident response, some attacks move fast (hours), some take months. Fixed turn lengths feel unrealistic. This system adds realism without requiring complex calculations.

#### For Beginners & Quick Play: Default Formula

**Default Formula: (Attack Chain Cards × 2) + 1**

This gives attackers enough time to progress realistically while keeping games manageable:

| Attack Chain | Formula | Turn Count | Session Duration |
|--------------|---------|-----------|------------------|
| 3 cards | (3 × 2) + 1 | **7 turns** | 30-40 min play |
| 4 cards | (4 × 2) + 1 | **9 turns** | 35-45 min play |
| 5 cards | (5 × 2) + 1 | **11 turns** | 40-50 min play |
| 6 cards | (6 × 2) + 1 | **13 turns** | 45-55 min play |

**How to Use Default Formula:**
1. Choose number of threat cards in attack chain (3, 4, 5, or 6)
2. Apply formula: (Cards × 2) + 1 = Turn Count
3. Announce turn count to Blue Team
4. Play game normally with that turn limit

**Example Setup:**
> "I've created a 4-card attack chain. That's (4 × 2) + 1 = 9 turns. You have 9 turns to detect all four threats. Go!"

---

#### For Advanced Players: Complexity Tiers (v2.1)

Advanced Threat Orchestrators can use a **Tier + d4 system** for more control and variability:

**Step 1: Select Attack Complexity Tier**

| Tier | Turn Base | Attack Profile | Example |
|------|-----------|----------------|---------|
| **TIER 1** | 5-7 | Simple & obvious | Script kiddie using public tools |
| **TIER 2** | 8-10 | Standard sophistication | Organized cybercriminal group |
| **TIER 3** | 11-13 | Highly sophisticated | APT with operational security |
| **TIER 4** | 14-16 | Expert/Nation-state | State-sponsored group |

**Step 2: Add Randomness (Optional)**

Roll 1d4 for variation:
- **Roll 1:** -1 turn (tight timeline)
- **Roll 2 or 3:** ±0 turns (no change)
- **Roll 4:** +1 turn (extended dwell time)

**Final Turn Count = Tier Base + d4 Result**

**Example Advanced Setup:**
> "This is a TIER 2 attack (organized cybercriminals). Base is 8-10 turns. I'll roll d4 for variation... [rolls 4, +1 turn]. Final turn count: 9-11 turns."

---

#### Critical Game Integrity Rules (v2.1)

These rules protect game balance and prevent metagaming:

##### Rule 1: Accept Any Roll (Even If It Feels Wrong)

**The Rule:** Threat Orchestrators MUST accept the random result, even if it feels impossibly tight or loose.

**Why:** Real incident response is unpredictable. Sometimes attacks happen faster or slower than expected.

**Example Scenarios:**
- TIER 3 attack (11-13 base) + d4 roll of 1 = 10-12 turns (tighter than expected, but realistic)
- TIER 1 attack (5-7 base) + d4 roll of 4 = 6-8 turns (easier conditions, but acceptable)

**When Chaos Feels Realistic:**
- Tight timeline: "The attacker worked faster than expected—they had prior knowledge"
- Loose timeline: "The attacker was cautious, spending weeks in reconnaissance before striking"

**Implementation:** Lean into the randomness as realistic incident variability.

---

##### Rule 2: Players Cannot Question Tier Based on Turn Count

**The Rule:** Blue Team CANNOT deduce the attack tier from the announced turn count. They cannot ask "Is this TIER 2?" or "Is this TIER 4?" based on how many turns they have.

**Why:** Real incident response doesn't come with difficulty labels. Attackers don't advertise sophistication. Players should discover complexity through gameplay (attack chain complexity, defender evasion, tool sophistication, etc.).

**What Players CAN Ask:**
- "What are the suspicious network events?" (leads to understanding threats)
- "Can we analyze the malware?" (reveals attacker sophistication through findings)
- "Why did this attack succeed?" (post-game discussion)

**What Players CANNOT Ask:**
- "Is this a TIER 2 attack?" (deriving tier from turn count)
- "This looks like a TIER 1 because we have 7 turns" (meta-gaming difficulty)

**Implementation:** Respond to difficulty questions by saying "Investigate and find out!" Players discover sophistication through evidence, not from turn counts.

---

##### Rule 3: TO Modifier Authority (Rare & Optional)

**The Rule:** ONLY after rolling d4, the Threat Orchestrator may apply an optional ±1 turn adjustment IF the rolled result feels genuinely unreasonable for the scenario.

**When to Use (Rare):**
- Scenario setup is unusually complex (multiple attack vectors, coordination across systems)
- Player group is new and needs slightly easier conditions
- Real-world incident being taught had specific timeline constraints

**When NOT to Use (Prefer Random):**
- "The roll feels unlucky" (accept the chaos)
- "I want this exactly 10 turns" (let dice decide)
- "The attack chain is long so it should take longer" (that's what TIER system handles)

**Implementation:**
1. Roll d4 normally
2. Announce rolled result
3. ONLY IF genuinely unreasonable, apply ±1 modifier and explain why
4. Document the override for consistency in future scenarios

**Example Valid Use:**
> "TIER 2 base 8-10, rolled -1 = 7-9 turns. That's tight given we have 5-card attack chain, so I'm adding +1 modifier (explaining the discovery is methodical). Final: 8-10 turns."

**Example Invalid Use:**
> "I rolled 8-10 but I want 10-12, so I'm adding +2." (NO - use the roll as-is)

---

#### Implementation Checklist

**For Beginners (Use Default Formula):**
- [ ] Choose attack chain length (3, 4, 5, or 6 cards)
- [ ] Calculate: (Cards × 2) + 1
- [ ] Announce turn count
- [ ] Play

**For Advanced (Use Tier + d4):**
- [ ] Select TIER (1, 2, 3, or 4)
- [ ] Announce TIER basis (not the number, just why it's that complexity)
- [ ] Roll d4 for variation (hidden or public, your choice)
- [ ] Calculate final turn count
- [ ] Apply Rule 3 modifier if genuinely needed (rare)
- [ ] Announce final turn count WITHOUT revealing tier

---

#### Quick Reference Card

**Default Formula:** Turn Count = (Attack Cards × 2) + 1

**Tier System:**
- TIER 1: 5-7 turns (simple)
- TIER 2: 8-10 turns (standard)
- TIER 3: 11-13 turns (advanced)
- TIER 4: 14-16 turns (expert)
- Add d4 roll: -1, 0, 0, or +1

**Golden Rules:**
1. Accept any roll (embrace chaos)
2. Never reveal tier to players
3. Modifier authority only when truly needed (rare)

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

