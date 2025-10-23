# Variable Turn Length Proposal

**Version:** 1.0 - Design Discussion
**Date:** October 2025
**Status:** For Review & Playtesting

---

## Executive Summary

**Current Rule:** Fixed 7-turn game length
**Proposed Change:** Variable 5-15 turns based on attack chain complexity
**Rationale:** Reflects real-world incident timelines and attack complexity
**Implementation:** Threat Orchestrator chooses complexity tier, then roll d4 for variation

---

## Problem Statement

### Current Limitation

The fixed 7-turn structure doesn't reflect how actual cybersecurity incidents unfold:

- **Simple phishing campaign:** Detected & contained in hours/days = 3-5 turns
- **Credential compromise:** Discovered over days, lateral movement investigated = 7-10 turns
- **Supply chain attack:** Hidden for weeks, affects multiple customers = 12-15+ turns
- **Multi-vector APT:** Sophisticated attack with persistence, stealth = 15+ turns

A fixed 7-turn game treats all attacks as equally complex, which is unrealistic and limits educational depth.

### Player Feedback

"Why does every game take exactly 7 turns? Some breaches are caught quickly, others drag on forever."

---

## Proposed Solution: Variable Turn Length (5-15 Turns)

### Design Goals

1. ✅ **Reflect Reality** - Game length should match attack complexity
2. ✅ **Educational** - Players learn that different attacks have different timelines
3. ✅ **Varied Gameplay** - Not every game follows identical turn sequence
4. ✅ **Tactical Depth** - Difficulty should affect game length
5. ✅ **Simple Mechanics** - Easy to implement without overcomplicating rules

### Proposed Mechanic

**Step 1: Threat Orchestrator Selects Complexity Tier**

The TO determines which tier matches the attack chain:

| Tier | Name | Attack Examples | Base Turns |
|------|------|-----------------|-----------|
| **1** | **Quick** | Single phishing, weak malware, basic credential abuse | 5-7 |
| **2** | **Standard** | Credential theft with lateral movement, persistence hooks | 8-10 |
| **3** | **Complex** | Supply chain compromise, multi-stage attack, hidden persistence | 11-13 |
| **4** | **Epic** | Multi-vector APT, coordinated attack, deep entrenchment | 14-15 |

**Step 2: Roll d4 for Variation**

Roll a d4 to add randomness while keeping it tight:

| Roll | Modifier | Result |
|------|----------|--------|
| 1 | -1 turn | Attack resolves slightly faster than expected |
| 2-3 | ±0 turns | As planned for this complexity tier |
| 4 | +1 turn | Attack proves more complex than initially thought |

**Step 3: Calculate Final Turn Count**

```
Final Turns = Base Turns (from Tier) + d4 Modifier (-1, 0, 0, +1)
```

### Examples

**Example 1: Phishing Campaign**
- Complexity: TIER 1 (Quick) → 5-7 base turns
- Roll d4: Result = 2 (modifier: ±0)
- Final: 5-7 + 0 = **6 turns**
- Narrative: Quick to identify, standard response time

**Example 2: Credential Compromise with Lateral Movement**
- Complexity: TIER 2 (Standard) → 8-10 base turns
- Roll d4: Result = 4 (modifier: +1)
- Final: 8-10 + 1 = **9-11 turns**
- Narrative: Attacker moved deeper than initial assessment suggested

**Example 3: Supply Chain Breach**
- Complexity: TIER 3 (Complex) → 11-13 base turns
- Roll d4: Result = 1 (modifier: -1)
- Final: 11-13 - 1 = **10-12 turns**
- Narrative: Multiple organizations coordinated response faster than expected

**Example 4: APT Multi-Vector Campaign**
- Complexity: TIER 4 (Epic) → 14-15 base turns
- Roll d4: Result = 4 (modifier: +1)
- Final: 14-15 + 1 = **15+ turns** (cap at 15 or allow extended game)
- Narrative: Sophisticated adversary established deep presence, long response needed

---

## Alternative Approaches Considered

### Option A: Pure d10 + 5

**Mechanic:** Roll d10, add 5 (Range: 5-15)

**Pros:**
- Simple math
- Even distribution
- Predictable

**Cons:**
- No narrative connection to threat
- Every result equally likely (doesn't feel strategic)
- Doesn't reflect TO's attack design

**Verdict:** Too mechanical, doesn't serve narrative

---

### Option B: Pure d20 with Min/Max Clamp

**Mechanic:** Roll d20, apply min 5 / max 15 (Range: 5-15)

**Pros:**
- Uses standard d20 mechanic
- Possible larger variation

**Cons:**
- Wasteful (rolls 1-5 all become 5, 16-20 all become 15)
- Not all die results equally valued
- More variance than needed

**Verdict:** Inefficient, too much swing potential

---

### Option C: Threat Orchestrator Picks (No Roll)

**Mechanic:** TO declares 5-15 directly

**Pros:**
- Perfect control over game length
- No randomness
- Can tailor to available time/difficulty

**Cons:**
- No surprise or suspense
- Takes away player agency
- Every game is exactly as TO plans

**Verdict:** Too predictable, removes game tension

---

### Option D: Recommended - Tier + d4 Roll (Hybrid)

**Mechanic:** TO selects tier (determines range) → Roll d4 (adds variation)

**Pros:**
- ✅ TO controls attack narrative complexity
- ✅ Adds randomness & surprise
- ✅ Tight variation (±1 turn) keeps game paced
- ✅ Simple to explain and execute
- ✅ Minimal mechanic overhead
- ✅ Reflects attack complexity narratively
- ✅ Encourages TO to think deeply about attack design

**Cons:**
- Requires TO to think about complexity tier upfront
- Slightly more sophisticated than fixed length

**Verdict:** **RECOMMENDED** - Best balance of narrative, mechanics, and simplicity

---

## Implementation Guide

### For Threat Orchestrators

When designing your attack chain:

1. **Assess complexity** - Does your attack chain fit TIER 1, 2, 3, or 4?
   - Phishing only? → TIER 1
   - Has lateral movement? → TIER 2
   - Supply chain or sophisticated persistence? → TIER 3
   - Multi-stage APT? → TIER 4

2. **Announce tier** - Tell Blue Team: "This is a TIER 2 (Standard) attack"

3. **Roll d4** - Roll publicly so everyone sees the variation

4. **Announce result** - "Base is 8-10 turns, you rolled a 3 (no modifier), so **10 turns total**"

5. **Explain narratively** - "This is a sophisticated lateral movement attack that will take time to fully contain"

### For Blue Teams

Understanding the tier gives you strategic information:

- **TIER 1 attacks:** Time-pressure is tight, need quick decisions
- **TIER 2 attacks:** Moderate time, can be more thorough
- **TIER 3 attacks:** Long game, focus on systematic investigation
- **TIER 4 attacks:** Epic response, multiple teams, extended engagement

---

## Critical Rules: Protecting Game Integrity

### Rule 1: Threat Orchestrator Can Accept Any Roll (Even if Feels Wrong)

**The Real-World Reason:**
In actual incidents, sometimes the unexpected happens:
- A "simple" phishing attack goes deeper than expected (roll +1 = longer game)
- A "complex" supply chain attack is discovered and contained faster (roll -1 = shorter game)
- Attackers are caught in 5 turns when 15 were expected
- A breach takes 15 turns to fully contain when 5 were planned

**The Rule:**
The Threat Orchestrator is **allowed (and encouraged)** to accept the result of the d4 roll as-is, even if:
- The result feels too tight/hard to accomplish in that many turns
- The result feels longer than necessary for the attack complexity
- The result creates an unexpected game dynamic

**This is intentional.** Real breach response is messy, unpredictable, and rarely goes exactly to plan.

**Example:**
- TO designs a TIER 2 (8-10 turns) credential theft attack
- Roll d4: Result = 1 (modifier: -1) = 7-9 turns (tighter than planned!)
- TO can say: "Your team's faster response than expected. You have 8 turns. Good luck."
- This creates tension and requires different strategy

**Counter-Example (What NOT to Do):**
- TO should NOT say: "That roll feels too tight. Let me re-roll."
- TO should NOT adjust the result after seeing what it is
- Accept the chaos - that's incident response!

---

### Rule 2: Players Do NOT Get to Question Attack Tier Based on Turn Length

**The Problem This Prevents:**
If Blue Team could guess the tier from the turn count, they could reverse-engineer attack difficulty:
- 6 turns → "Oh, this is just TIER 1, probably just phishing"
- 14 turns → "This is TIER 4, must be APT, let's plan for persistence"

This removes the uncertainty that makes incident response interesting.

**The Rule:**
Blue Teams:
- ✅ CAN ask: "What's the threat narrative?" (TO explains scenario)
- ✅ CAN see: The turn count
- ✅ CAN infer: Some strategy based on scenario
- ❌ CANNOT ask: "What tier is this?" (directly)
- ❌ CANNOT deduce: Tier from turn count
- ❌ CANNOT second-guess: Whether the tier matches the turns

**Why This Matters:**
Turn count is just **one piece of information**. Forcing Blue Team to work with:
1. The attack narrative (provided by TO)
2. Turn count (they can see it)
3. Cards/threats drawn
4. Their own strategy and experience

This creates realistic uncertainty. In real incidents, you don't know if a breach is simple or complex until you investigate.

**Example:**
- TO: "You have 8 turns. A user reported a suspicious email from 'your IT department' asking for password reset."
- Player: "Is this TIER 1 or TIER 2?"
- TO: "I'm not telling. You have 8 turns to figure it out. Is it just phishing, or did someone get deeper access? Investigate and decide."

**Another Example:**
- TO: "You have 14 turns. Your monitoring detected unusual database queries from a contractor's VPN."
- Player: "That's a long game... must be TIER 4?"
- TO: "Or maybe TIER 3 that felt longer than expected. Or TIER 4 that you'll solve faster. You'll figure it out as you investigate."

**The Teaching Moment:**
Real incident response doesn't come with difficulty labels. You get:
- Symptoms (suspicious email, unusual queries, etc.)
- Time (however many turns the dice provide)
- Your skills and tools
- That's it

Players must investigate, not assume.

---

### Rule 3: TO Modifier Authority (Bonus Rule)

**Additional Authority for Threat Orchestrator:**

The TO can also decide to apply a small modifier themselves if they feel the random roll misses the mark, but this should be rare:

| Situation | Allowed Modifier |
|-----------|------------------|
| Roll feels genuinely unreasonable | ±1 turn max (after dice roll) |
| Player morale concerns | ±1 turn max |
| Time constraint for session | Announce before rolling |
| Too complex to resolve in time | Add 1-2 turns |

**When to Use (Rarely):**
- You rolled -1 on a TIER 3 complex attack, now it's 10 turns, but you have massive second-stage persistence planned that needs 12+ turns to fully resolve
- You rolled 5 turns for a TIER 2, but a new player group needs more experience to resolve it

**When NOT to Use:**
- Because you "like" the original plan better
- To guarantee a specific outcome
- To punish players
- Multiple times in one session (use dice result instead!)

**Format:**
"I rolled a [1], which gives us [10-12] turns. Actually, this persistence attack needs more time. I'm adding 1 turn. Final: **13 turns total**."

---

### Summary: The Philosophy

**Accept Chaos.** Real incident response is unpredictable:
- Sometimes you get lucky and discover a breach quickly (short game)
- Sometimes an attack is more entrenched than expected (long game)
- Sometimes your response is faster/slower than planned
- **This is realism, not a bug.**

The dice represent real-world uncertainty. The TO's tier represents their attack complexity. Together, they create a realistic incident response scenario.

**Players don't get to "game" the system** by trying to deduce difficulty from turn count. They have to actually respond to the threat, not the meta-game.

---

## Why This Works

### Narrative Authenticity

Real breaches vary dramatically in timeline:

- **2013 Target breach:** ~2 months before detection (real: 60+ days) = TIER 3/4
- **2020 SolarWinds:** ~9 months before discovery = TIER 4 (Epic)
- **2019 Capital One:** ~2.5 months = TIER 3 (Complex)
- **Typical phishing (caught quickly):** 1-3 days = TIER 1 (Quick)

Our variable system maps to these real timelines.

### Gameplay Balance

- **New players:** Start with TIER 1 (6 turns, fast feedback)
- **Intermediate:** TIER 2 (9 turns, moderate complexity)
- **Advanced:** TIER 3/4 (12-15 turns, deep analysis needed)

Games scale from 30-45 min (quick) to 90-120 min (epic).

### Educational Value

Players learn:

1. Not all attacks are equal
2. Complexity affects response time
3. Simple attacks can be resolved quickly
4. Sophisticated attacks need sustained effort
5. Planning response time based on attack type matters

### Mechanical Elegance

- TO makes one meaningful choice (attack tier)
- Roll adds variance (±1 turn) without overwhelming complexity
- Result is announced and explained
- Everyone knows game length from Turn 1

---

## Playtesting Recommendations

### Test Scenarios

1. **TIER 1 Game (5-7 turns)**
   - Challenge: Can quick response be interesting?
   - Teach: Rapid detection and containment

2. **TIER 2 Game (8-10 turns)**
   - Challenge: Standard difficulty vs. fixed 7?
   - Teach: Balanced investigation & response

3. **TIER 3 Game (11-13 turns)**
   - Challenge: Does extended game maintain engagement?
   - Teach: Complex investigation, persistence detection

4. **TIER 4 Game (14-15 turns)**
   - Challenge: Can we maintain interest in long game?
   - Teach: Deep forensics, supply chain implications

### Playtesting Questions

- Does the attack tier feel narratively appropriate?
- Does the game length match the attack complexity?
- Does the d4 roll feel like appropriate variance?
- Do players feel the time is well-spent at each tier?
- Would you prefer more/less variation in turn length?
- Should different modules have different tier ranges?

### Potential Adjustments

If playtesting reveals issues:

- **Tiers feel mismatched:** Adjust base turn ranges for tiers
- **d4 variation too much:** Try d3 (-1, 0, +1) instead
- **Variation too little:** Try d6 (-2, -1, 0, 0, +1, +2)
- **Games feel rushed:** Increase TIER 1 base to 6-8 instead of 5-7

---

## Module Adaptations

### Incident Response Module

- **Current:** Fixed 7 turns
- **Proposed:** 5-15 turns (use this system)
- **Reason:** IR is primary attack/response module

### Hardening Module

- **Current:** Variable phase length
- **Proposed:** Could use similar tier system
- **Adaptation:** Instead of "attack complex," use "defense test difficulty"
  - TIER 1: Basic defenses tested
  - TIER 2: Standard defenses tested
  - TIER 3: Advanced defenses tested
  - TIER 4: Elite defenses tested

### Disaster Recovery Module

- **Current:** Fixed 7 turns (crisis response)
- **Proposed:** Could incorporate variable length
- **Adaptation:** "Crisis severity" determines initial turn count
  - TIER 1: Minor incident (5-7 turns recovery)
  - TIER 2: Standard incident (8-10 turns recovery)
  - TIER 3: Major incident (11-13 turns recovery)
  - TIER 4: Catastrophic incident (14-15+ turns recovery)

### Network Building Module

- **Current:** N/A (not time-limited)
- **Proposed:** Not applicable

### Audit & Compliance Module

- **Current:** N/A (not time-limited)
- **Proposed:** Not applicable

---

## Decision Matrix

| Aspect | Current (Fixed 7) | Proposed (5-15 Variable) | Winner |
|--------|------------------|------------------------|--------|
| **Narrative Realism** | ❌ All same | ✅ Matches complexity | Proposed |
| **Educational Value** | ⚠️ Basic | ✅ Shows variation | Proposed |
| **Gameplay Variety** | ❌ Identical | ✅ Different each game | Proposed |
| **Rules Complexity** | ✅ Simple | ⚠️ Slightly more complex | Current |
| **TO Control** | ❌ None | ✅ Tier selection | Proposed |
| **Player Fairness** | ✅ All equal | ✅ Varied by attack type | Proposed |
| **Mechanical Elegance** | ✅ Clean | ✅ Elegant | Tie |
| **Learning Curve** | ✅ Minimal | ⚠️ Slight increase | Current |

**Overall:** Proposed system wins on narrative and educational value with minimal added complexity.

---

## Implementation Path

### Phase 1: Core Rules Update
- Update core-rules.md to reflect variable turn length
- Add Tier system and d4 roll mechanics
- Include complexity assessment examples

### Phase 2: Module Updates
- Update Incident Response module rules
- Update Hardening module rules (if applicable)
- Update Disaster Recovery rules (if applicable)

### Phase 3: Card Updates
- Add "Complexity Tier" guidance to threat card descriptions
- Suggest typical tiers for different threat types
- Update card examples

### Phase 4: Playtesting
- Test all four tiers in real games
- Gather feedback on narrative fit
- Adjust tiers if needed

### Phase 5: Rollout
- Document final rules
- Create quick-reference guide
- Update player aids

---

## Quick Reference Card (for Threat Orchestrators)

```
VARIABLE TURN LENGTH - QUICK REFERENCE

Step 1: Choose Attack Complexity Tier
┌─────────────────────────────────────────┐
│ TIER 1 (Quick)          → 5-7 turns     │
│ TIER 2 (Standard)       → 8-10 turns    │
│ TIER 3 (Complex)        → 11-13 turns   │
│ TIER 4 (Epic)           → 14-15 turns   │
└─────────────────────────────────────────┘

Step 2: Roll d4 for Variation
┌─────────────────────────────────────────┐
│ Roll 1  → -1 turn (faster than expected) │
│ Roll 2-3 → ±0 turns (as planned)        │
│ Roll 4  → +1 turn (more complex)        │
└─────────────────────────────────────────┘

Step 3: Announce Final Turn Count
"This is a TIER 2 attack. I rolled a [3],
so we have [8-10 + 0 = 9 turns] total."

Why? Different attacks take different times
to investigate and contain. This makes the
game feel more realistic!
```

---

## Conclusion

**Recommendation:** Implement variable turn length (5-15 turns) using the Tier + d4 system.

**Benefits:**
- Reflects real incident timelines
- Enhances narrative immersion
- Increases gameplay variety
- Minimal rules overhead
- Educationally valuable

**Next Steps:**
1. Review and approve proposal
2. Update core rules
3. Playtest with all modules
4. Gather feedback and iterate
5. Roll out to community

---

*This proposal is open for discussion, feedback, and playtesting.*
*Please test and report results!*
