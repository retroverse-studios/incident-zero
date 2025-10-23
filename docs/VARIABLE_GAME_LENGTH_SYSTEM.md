# Variable Game Length System (v2.1)

**Version:** 2.1 - Production Ready
**Last Updated:** October 2025
**Status:** Core System for All Modules

---

## Overview

Incident Zero v2.1 introduces a **Variable Game Length System** that adds realism and variety without requiring complex calculations. The system has two parallel tracks:

1. **Default Formula** - Simple, fast, for everyone (1 calculation, 5 seconds)
2. **Advanced Tier System** - Nuanced, variable, for experienced TOs (3 steps, optional complexity)

Both produce realistic game lengths that scale with attack complexity while maintaining educational depth.

---

## Philosophy

### Why Variable Lengths?

**Real-world basis:**
- Some cyberattacks unfold in hours (ransomware deployments)
- Others take months (APT reconnaissance and persistence)
- Fixed 7-turn limits feel artificial

**Educational value:**
- Variable timelines teach "attacks aren't one-size-fits-all"
- Tight timelines create pressure; loose timelines reward caution
- Randomness mirrors real incident response unpredictability

**Game design value:**
- Prevents pattern recognition ("all games are exactly 7 turns")
- Encourages adaptation ("we have fewer turns, prioritize differently")
- Adds replayability ("same scenario, different timeline")

---

## System 1: Default Formula (Beginners & Quick Play)

### Formula

```
Turn Count = (Number of Attack Cards × 2) + 1
```

### Quick Reference Table

| Attack Chain | Calculation | Turn Count | Session Time |
|--------------|-------------|-----------|--------------|
| 3 cards | (3 × 2) + 1 | **7 turns** | ~30-40 min |
| 4 cards | (4 × 2) + 1 | **9 turns** | ~35-45 min |
| 5 cards | (5 × 2) + 1 | **11 turns** | ~40-50 min |
| 6 cards | (6 × 2) + 1 | **13 turns** | ~45-55 min |

### Why This Formula?

- **Simple:** One multiplication, one addition—anyone can calculate
- **Realistic:** Gives attackers 2 turns per card plus 1 buffer turn
- **Balanced:** Teams aren't rushed (attackers have time) but aren't bored (games don't drag)
- **Scalable:** Works for 3-card scenarios (7 turns) through 6-card campaigns (13 turns)

### Usage Example

**Beginner Threat Orchestrator:**
> "I've selected 4 threat cards for my attack chain: Phishing → Credential Theft → Lateral Movement → Ransomware. Using the formula: (4 × 2) + 1 = 9 turns. You have 9 turns to detect and contain all four threats. Timer starts now!"

### Implementation Steps

1. **Design attack chain** (select 3, 4, 5, or 6 threat cards)
2. **Apply formula** (Cards × 2 + 1)
3. **Announce turn count** (no explanation needed—it's the default)
4. **Play normally** (use that turn count as hard limit)

---

## System 2: Advanced Tier System (Experienced TOs)

### Overview

The **Tier + d4 system** gives experienced Threat Orchestrators control over **attack sophistication** while maintaining **randomness** for realism.

```
Turn Count = [Tier Base Range] + d4 Modifier
```

---

### Step 1: Select Attack Complexity Tier

Choose ONE tier based on attack sophistication (not visibility to players):

#### TIER 1: Simple & Obvious (5-7 turns base)

**Attacker Profile:**
- Script kiddies using publicly available tools
- Low operational security
- Little reconnaissance
- Obvious techniques

**Examples:**
- Basic phishing + default malware
- Publicly known exploits
- No persistence mechanisms

**When to Use:**
- Beginner players learning the game
- Educational scenario with clear attack progression
- Teaching specific threat technique

---

#### TIER 2: Standard Sophistication (8-10 turns base)

**Attacker Profile:**
- Organized cybercriminal group
- Medium operational security
- Some reconnaissance
- Mix of known and custom tools

**Examples:**
- Targeted phishing + credential harvesting
- Lateral movement with known exploits
- Basic persistence mechanisms
- Some anti-analysis awareness

**When to Use:**
- Most standard scenarios
- Realistic criminal syndicate attacks
- Default for intermediate players

---

#### TIER 3: Highly Sophisticated (11-13 turns base)

**Attacker Profile:**
- Advanced Persistent Threat (APT) group
- Strong operational security
- Extensive reconnaissance
- Custom tools and zero-days

**Examples:**
- Multi-vector attack with coordination
- Advanced persistence (firmware, kernel modules)
- Anti-forensics techniques
- Encrypted command-and-control

**When to Use:**
- Advanced player groups
- Teaching state-sponsored attack techniques
- Scenarios based on real APT campaigns

---

#### TIER 4: Expert / Nation-State (14-16 turns base)

**Attacker Profile:**
- State-sponsored cyber operations
- Extreme operational security
- Months of reconnaissance
- Military-grade tools and exploits

**Examples:**
- Coordinated multi-system compromise
- Supply chain attacks
- Persistent access maintained for years
- Infrastructure with plausible deniability

**When to Use:**
- Research and curriculum development
- Training elite response teams
- Historical incident analysis (Stuxnet, NotPetya, etc.)

---

### Step 2: Roll for Variation (Optional)

To add unpredictability, roll **1d4** and apply modifier:

| Roll | Modifier | Interpretation | Examples |
|------|----------|-----------------|----------|
| **1** | **-1 turn** | Tight/Fast | "Attacker worked faster than expected; they had insider knowledge" |
| **2 or 3** | **±0 turns** | No change | "Timeline proceeded as expected" |
| **4** | **+1 turn** | Loose/Slow | "Attacker was cautious with extended reconnaissance phase" |

**d4 Distribution:**
- 25% chance of tight timeline (-1)
- 50% chance of baseline (±0)
- 25% chance of extended timeline (+1)

### Step 3: Calculate Final Turn Count

```
Final Turn Count = Tier Base + d4 Result
```

### Examples

**Example 1: Standard Criminal Group (TIER 2)**
```
Tier: TIER 2 (8-10 turns base)
Narrative: Organized ransomware group targeting healthcare
Roll: d4 = 2 (no modifier)
Final: 8-10 turns

Announcement: "This organized group has compromised your network.
You have 8-10 turns to detect and contain them."
```

**Example 2: APT Attack (TIER 3)**
```
Tier: TIER 3 (11-13 turns base)
Narrative: State-sponsored group conducting corporate espionage
Roll: d4 = 4 (+1 turn)
Final: 12-14 turns

Announcement: "A sophisticated actor has been operating in your network
for weeks. You have 12-14 turns to uncover the full extent of their access."
```

**Example 3: Script Kiddie (TIER 1)**
```
Tier: TIER 1 (5-7 turns base)
Narrative: Attacker using public PoC exploit
Roll: d4 = 1 (-1 turn)
Final: 4-6 turns

Announcement: "An attacker has hit your systems hard and fast.
You have only 4-6 turns before data starts being exfiltrated."
```

---

## Critical Game Integrity Rules

These three rules ensure the system maintains educational value and prevents metagaming:

---

### Rule 1: Accept Any Roll (Even If It Feels Wrong)

**Statement:** Threat Orchestrators MUST accept the d4 result as-is, regardless of whether it feels unreasonably tight or loose for the scenario.

**Rationale:** Real incident response is chaotic. Sometimes:
- Well-prepared attackers execute faster than expected (they had intel)
- Cautious attackers spend weeks in reconnaissance (defensive posture matters)
- Budget runs out faster than expected (incident response is expensive)

**Embracing the Chaos:** When a roll feels unexpected, narrate it as realism:

- **Unexpectedly tight timeline?** "The attacker had reconnaissance from a previous attack on your vendor—they knew your network layout."
- **Unexpectedly loose timeline?** "The attacker was methodical, testing defenses incrementally before committing resources."

**Implementation:**
- Roll d4 publicly (so players see it wasn't rigged)
- Accept the result immediately
- Narrate it into the scenario realistically
- Move on; don't second-guess the dice

**Example Conversation:**
```
TO: "TIER 2 attack, so 8-10 turns baseline. Rolling for variation..."
[Rolls d4: 1, which means -1]
TO: "That's tight—only 7-9 turns. But that makes sense; this group
    has compromised your supplier before and knew your infrastructure.
    You have 7-9 turns."
```

**What NOT to do:**
```
TO: "I rolled a 1, but that feels too tight. Let me roll again."
    ✗ NO - Accept the first roll

TO: "I rolled a 1, so I'm ignoring it and using 8-10 instead."
    ✗ NO - That undermines the system

TO: "That's tight but I'll add 2 turns to make it fair."
    ✗ NO - Only Rule 3 allows modifications (and only ±1, rarely)
```

---

### Rule 2: Players Cannot Question Attack Tier Based on Turn Count

**Statement:** Blue Team members CANNOT deduce (or ask about) the attack TIER from the announced turn count. They cannot use meta-information like "we have 9 turns, so this must be TIER 2."

**Rationale:**
- In reality, companies don't know attack sophistication in advance
- Attackers don't advertise their skill level
- Discovering attacker sophistication through evidence is more educational
- This prevents metagaming ("we know it's TIER 2, so let's play for 9 turns max")

**What Players CAN Do:**
- Ask "What suspicious activity have we detected?" → Investigates to understand threats
- Ask "Can we analyze the malware?" → Reveals sophistication through findings
- Ask "Why did this attack succeed?" → Post-game discussion (after game ends)
- Ask "How much damage was done?" → Forensic investigation (post-game)

**What Players CANNOT Do:**
- Ask "Is this a TIER 2 attack?" → Directly asking tier (prohibited)
- Say "This must be TIER 3 because we have 12 turns" → Meta-reasoning (prohibited)
- Assume "TIER 1 = simple, so let's focus on basics" → Meta-optimization (prevents discovery)

**Implementation:**

When players ask about tier/difficulty:

```
Player: "Is this a TIER 2 attack?"
TO: "Investigate and you'll find out. What do you want to do?"

Player: "This looks like TIER 3 based on the turn count..."
TO: "Turn count ≠ difficulty. Investigate the evidence and make your own assessment."

Player: "Can we see what we're facing?"
TO: "Some will reveal through investigation. Some will surprise you."
```

---

### Rule 3: TO Modifier Authority (Rare & Optional)

**Statement:** ONLY after rolling d4, the Threat Orchestrator may apply an optional **±1 turn adjustment** if the rolled result creates a genuinely problematic situation.

**Frequency:** This should be RARE (< 10% of games). Default: accept rolls.

**When to Use (Genuinely Justified):**

1. **Unusually Complex Setup**
   - Scenario has 6+ subsystems (normal is 3-4)
   - Multiple attack vectors that need separate investigation
   - Recommend: Extend by +1 to allow full exploration

2. **New Player Group**
   - First game ever; players still learning system
   - Recommend: Extend by +1 to reduce pressure on learning
   - (But challenge them on game 2)

3. **Specific Real-World Incident**
   - Teaching historical breach with documented timeline
   - Example: "NotPetya took 4 hours to spread; we're modeling that"
   - Recommend: Adjust to match documented timeline (with explanation)

**When NOT to Use (Accept Roll As-Is):**

1. **"The roll feels unlucky"** → Accept chaos; it's realistic
2. **"I want exactly 10 turns"** → Let the dice decide
3. **"The attack chain is long"** → That's what TIER system handles
4. **"I miscalculated the TIER"** → Reroll from scratch next game
5. **"Players are doing well, so more turns"** → Never adjust mid-game

**Implementation:**

```
Step 1: Roll d4 (publicly)
Step 2: Calculate result (Tier Base + d4)
Step 3: Announce initial turn count

THEN if genuinely needed:

Step 4: Pause
Step 5: Explain why adjustment is necessary
Step 6: Apply ±1 modification (only ±1, not more)
Step 7: Announce final turn count
Step 8: Document the decision (for consistency in future scenarios)
```

**Example Valid Use of Rule 3:**

```
Setup: "I'm teaching the SolarWinds supply chain attack.
Real timeline was 6 hours to detection.
I have TIER 3 (11-13 turns).
Rolled d4: 2 (no modifier) = 11-13 turns.
That feels right—letting me adjust by -1 to model
the documented 10-12 hour timeline. Final: 10-12 turns."
```

**Example Invalid Use of Rule 3:**

```
WRONG: "I rolled 8-10 turns but my attack chain is 5 cards.
I want it longer, so I'm adding 2 turns."
CORRECT: Use TIER 3 (11-13) if you want a longer game

WRONG: "Players are doing well, so I'm extending by +2 turns."
CORRECT: No mid-game adjustments; accept the result

WRONG: "I'm just going to ignore the roll and use 10 turns."
CORRECT: Either accept d4 result or reroll from scratch (before game starts)
```

---

## Choosing Between Systems

### Use Default Formula If:
- ✓ You're new to Incident Zero
- ✓ You want minimal prep (one calculation)
- ✓ You want consistent, predictable game lengths
- ✓ You value simplicity over variety
- ✓ Your players are learning the core mechanics

### Use Tier + d4 If:
- ✓ You're experienced with game system
- ✓ You want variety between scenarios
- ✓ You like controlling attack sophistication narratively
- ✓ You appreciate randomness and realism
- ✓ You're designing scenarios for specific learning goals

**Hybrid Approach:** Many TOs use **Default Formula for most games**, then switch to **Tier System for special campaigns or advanced groups**.

---

## Implementation Workflow

### For Beginners (Default Formula)

```
1. Design attack chain (pick 3-6 threat cards)
2. Count cards: ___
3. Calculate: (___ × 2) + 1 = ___ turns
4. Announce: "You have ___ turns."
5. Play
```

**Time Investment:** 30 seconds

### For Advanced (Tier System)

```
1. Design attack scenario
2. Choose Tier 1-4 based on sophistication (don't announce number)
3. Write down Tier Base (e.g., "TIER 2: 8-10")
4. Roll d4 (publicly or private)
5. Calculate: Base + d4 result = Final turn count
6. [Optional] Apply Rule 3 modification if genuinely needed (rare)
7. Announce final turn count (no tier numbers)
8. Play
9. [After game] Discuss attack sophistication discovered through gameplay
```

**Time Investment:** 2-3 minutes

---

## Quick Reference Card (Print & Keep at Table)

```
═══════════════════════════════════════════════════════════════
              VARIABLE GAME LENGTH SYSTEM v2.1
═══════════════════════════════════════════════════════════════

SYSTEM 1: DEFAULT FORMULA (Beginners)
────────────────────────────────────
Turn Count = (Attack Cards × 2) + 1

3 cards → 7 turns  |  4 cards → 9 turns
5 cards → 11 turns |  6 cards → 13 turns

SYSTEM 2: TIER + d4 (Advanced)
──────────────────────────────
Step 1: Choose Tier (1-4, don't reveal number)
  TIER 1: 5-7 turns (simple)
  TIER 2: 8-10 turns (standard)
  TIER 3: 11-13 turns (advanced)
  TIER 4: 14-16 turns (expert)

Step 2: Roll d4 (-1, 0, 0, or +1)

Step 3: Final Turn = Tier Base + d4 Result

CRITICAL RULES
──────────────
✓ Rule 1: Accept any roll (embrace chaos)
✓ Rule 2: Don't reveal tier (let players discover via gameplay)
✓ Rule 3: Modifier authority ONLY when genuinely needed (rare)

═══════════════════════════════════════════════════════════════
```

---

## Frequently Asked Questions

**Q: Why use (×2) + 1 and not something else?**
A: Playtesting showed this gives attackers enough time to progress realistically while keeping games from dragging. It's also easy to calculate mentally.

**Q: Can I use both systems in the same campaign?**
A: Yes! Use Default Formula for most games, Tier System for special scenarios.

**Q: What if players figure out the formula?**
A: That's fine. Knowing the formula doesn't give them an advantage (they still don't know how many cards in the chain).

**Q: Can I adjust turn count during the game?**
A: NO. Turn count is set at game start and never changes. Rule 3 modifications happen before game starts only.

**Q: What if my attack chain doesn't fit (e.g., 2 cards or 7 cards)?**
A:
- 2 cards: Use formula anyway (2 × 2 + 1 = 5 turns) or switch to Tier System
- 7+ cards: Use Tier 3-4 instead of formula

**Q: How do I explain randomness to new players?**
A: "Real incident response isn't predictable. Sometimes attackers are faster, sometimes slower. We're rolling to capture that realism."

**Q: Should I tell players the turn count?**
A: YES, always tell them at game start. (The mystery is about attack sophistication, not game length.)

**Q: Can I use a d6 or d12 instead of d4?**
A: Not recommended (changes probability distribution). Stick with d4 or no roll at all.

---

## Evolution & Future

This system was introduced in **v2.1** as players requested more realism in game pacing. Future versions may include:

- **Environmental modifiers** (weekend vs. holiday attacks take longer)
- **Player competence scaling** (teams of experts progress faster)
- **Attack type variance** (ransomware on tighter timeline than espionage)

For now, the two-track system (Default + Tier) provides both **accessibility** and **depth**.

---

## Design Notes for Future Playtests

**Questions to answer through playtesting:**

1. Does Default Formula (×2 + 1) create good pacing for all group types?
2. Are players satisfied with Tier + d4 variability?
3. Do the three Critical Rules prevent metagaming effectively?
4. Should some modules have different formulas (e.g., Forensics longer)?
5. Is Rule 3 invoked correctly or too often?

**Feedback to collect:**
- Typical game length vs. expected (from formula)
- Whether turn limits felt realistic
- Whether players felt rushed or bored
- Whether tier-hiding created effective mystery

**Report findings to:** [GitHub Issues - Variable Game Length Feedback](https://github.com/retroverse-studios/incident-zero/issues)

---

**Ready to set game length?** Pick your formula and play!

