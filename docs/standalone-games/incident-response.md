# Incident Response Module: Standalone Play Guide

**Version:** 2.2 - Playtest Edition
**Duration:** 30-45 minutes
**Players:** 1 Threat Orchestrator + 2-4 Blue Team members
**Best For:** Incident response training, attack detection practice, SOC operations

---

## Module Overview

The **Incident Response Module** teaches players how to detect and investigate cyberattacks under pressure. Players must reveal a hidden attack chain before time runs out or budget is exhausted.

This is the foundation module—many other modules build upon successful or unsuccessful incident response.

---

## Setup (5 minutes)

### 1. Choose Difficulty Level

Turn limits use the **Variable Game Length formula** from [Core Rules §3a](../rules/core-rules.md#3a-variable-game-length-system-v21---new): **Turn Limit = (Attack Chain Cards × 2) + 1**.

| Difficulty | Chain Length | Budget | Turn Limit | Best For |
|------------|--------------|--------|-----------|----------|
| **Beginner** | 3 cards | 100 | 7 turns | First playthrough, basic learning |
| **Intermediate** | 4 cards | 100 | 9 turns | Standard play, mixed experience |
| **Advanced** | 5 cards | 100 | 11 turns | Experienced players, challenge |

### 2. Threat Orchestrator Preparation

**Create the Attack Chain:**
1. Select 3-5 threat cards in logical sequence
2. Arrange by attack chain step: INITIAL COMPROMISE → PIVOT & ESCALATE → PERSISTENCE → C2 & EXFIL
3. Write down clues for each hidden card (don't reveal yet)
4. Place relevant Asset Cards on the table (visible to all). Asset Cards are shared components — see `cards/network-building/core-deck/asset-cards.md`

**Recommended first-time scenario:**
- T-01: Phishing Campaign (INITIAL COMPROMISE - SOCIAL ENGINEERING)
- T-04: Lateral Movement via SMB (PIVOT & ESCALATE - NETWORK)
- T-10: SQL Database Exfiltration (C2 & EXFIL - DATA EXFIL)
- **Total:** 3 cards, ~30 minutes, teaches full attack chain concept

### 3. Blue Team Setup

- Starting Budget: **100**
- Draw 5 Defense Cards (random, face down)
- Place Turn Tracker at **1**
- Place Budget Tracker at **100**
- Place Uncontained Threats Tracker at **0**

### 4. Read the Opening Scenario

Threat Orchestrator reads opening scenario based on **only** the first hidden card's clue. Example:

> "Your security operations center is monitoring the network when alerts begin firing. Your SIEM shows suspicious email traffic coming from your IT department domain, but the headers look spoofed. Several employees have reported clicking links in emails they thought came from IT requesting password resets."

---

## Gameplay Loop (25-35 minutes)

### Round Structure

Each turn follows this structure:

**1. START OF TURN**
- **Uncontained Threats Penalty:** For each revealed-but-uncontained threat, deduct 5 Budget
- **Active Breach Cost (v2.2):** If at least one chain card is still unrevealed, deduct 5 Budget (dwell time is never free)
- Read turn number aloud ("Turn 3...")

**2. BLUE TEAM'S TURN (2-3 minutes discussion)**
- Team discusses strategy
- Decides on ONE action (see below)
- Announces action and parameters

**3. ACTION RESOLUTION**
- Roll 1d20 for success/failure
- Apply modifiers (see below)
- Determine outcome

**4. END OF TURN**
- Advance Turn Tracker by 1
- Draw 1 Defense Card
- Check if game won/lost

### Three Available Actions

#### Action 1: Investigate 🔎

**Cost:** 5 Budget
**Roll Required:** 11+ (on d20)

**How it works:**
1. Team describes what they're investigating (e.g., "Email headers in the mail gateway logs")
2. Provide technical justification for the investigation approach
3. Roll 1d20

**Roll Modifiers:**
- **+2 bonus:** Strong technical justification (references specific logs, tools, or methodologies)
- **+1 bonus:** References real security tools/techniques (Splunk, Wireshark, EDR, specific CVEs, MITRE ATT&CK)
- **No modifier:** Vague investigation (0 to +0)

**Examples of good justification:**
- "We want to analyze the email headers in the mail gateway to identify the true sender IP and check it against threat intelligence feeds"
- "We'll query our EDR agent logs for any processes spawned after the user clicked the link, looking for PowerShell or suspicious child processes"

**Outcomes (v2.2 — investigation successes accumulate):**
- **Success (roll + modifiers ≥ 11):**
  - **First success against the current chain link:** TO gives a **verbal clue** about that hidden threat (always the earliest unrevealed card — see Sequential Discovery below)
  - **Second success against the same link:** **THE CARD IS REVEALED!** It becomes uncontained and the team chooses a Discovery Reward
- **Failure:** "Your investigation yields no actionable intelligence" (turn wasted, budget spent, but team learned). Failures do not count toward the two successes.

**Sequential Discovery (v2.2 note):** Only the **earliest unrevealed chain card** can be revealed — by investigation or by defense deployment. Clues and successes always target that card, matching the clue system's walk down the kill chain.

---

#### Action 2: Deploy a Defense 🛡️

**Cost:** 10/15/25 Budget (depending on card tier)
**Roll Required:** 11+ (on d20)

**How it works:**
1. Choose a Defense Card from your hand
2. Target a specific Asset or threat vector
3. Explain why this defense is appropriate for the situation
4. Roll 1d20

**Roll Modifiers:** Same as Investigate (+2 for justification, +1 for real tools)

**Outcomes:**
- **Success (roll + modifiers ≥ 11):**
  - If card's **Countermeasure matches** the hidden threat's **Attack Vector** AND it's the correct step in the chain → **THREAT CARD REVEALED IMMEDIATELY!**
  - If it matches but wrong step, or right step but wrong vector → Defense deployed but no reveal
  - If neither matches → Defense deployed but ineffective against current threat

- **Failure:** Budget spent, defense not properly implemented (card discarded)

**Deployed Defense Persistence (v2.2):** Deployed defenses stay on the board. Whenever the chain link currently being targeted has a vector matching a deployed defense, add **+2** to Investigate and Deploy Defense rolls against it (the TO, who knows the hidden vector, announces when this applies). Full rule in [Module: Incident Response](../rules/module-incident-response.md).

---

#### Action 3: Emergency Response 🚨

**Cost:** 15 Budget (v2.2 — repriced from 25)
**Roll Required:** None—this always succeeds

**How it works:**
1. Choose a **previously revealed** Threat Card still in play
2. Describe your containment strategy (quarantine infected systems, disable compromised accounts, isolate network segments, etc.)
3. Card is immediately removed from play
4. **Uncontained Threats penalty decreases by 1**

**Strategic Use:**
- Use this if you're running out of budget and accumulating penalties
- Use this if a threat is too dangerous to leave active
- Use this to prepare for later modules (e.g., if continuing to Hardening, fewer contained threats = more budget available)

---

### Uncontained Threats Penalty & Active Breach Cost

**How it works:**
1. When a threat card is **revealed**, it becomes "uncontained" (add 1 to Uncontained Threats Tracker)
2. At the **START of each turn**, deduct **5 Budget per uncontained threat**
3. **Active Breach Cost (v2.2):** at the START of each turn, also deduct **5 Budget** if at least one chain card is still unrevealed (hidden dwell time costs money too)
4. When **Emergency Response** is used, remove that threat and decrement the tracker
5. When the **next card in the chain is revealed**, the previous uncontained threat is automatically "mitigated" (decrement tracker)

**Example (one action per turn; 3-card chain; Budget 100):**
```
Turn 1: START → -5 Active Breach Cost (95)
        Deploy Defense succeeds, full match → PHISHING REVEALED
        (-10 for the BASIC defense, 85) → Uncontained Threats = 1
        Reward: Budget Grant +10 (95)
Turn 2: START → -5 (uncontained) -5 (Active Breach: 2 cards hidden) = 85
        Emergency Response on Phishing: pay 15 (70) → Uncontained = 0
Turn 3: START → -5 (Active Breach only) = 65
        ...investigation continues toward the next chain card
```

---

## Winning & Losing

### Victory Condition ✓

**Blue Team Wins if:**
- All threat cards in the attack chain are revealed
- AND this happens within your turn limit (7/9/11 by chain length)

**Victory is checked immediately when the final card is revealed (v2.2)** — before any start-of-turn penalties.

### Defeat Condition ✗

**Blue Team Loses if:**
- Turn Tracker exceeds your turn limit with unrevealed cards remaining
- OR the team cannot afford any legal action (Budget floors at 0; an action requires its full cost — see Budget Edge Rules in [Module: Incident Response](../rules/module-incident-response.md))

### Scoring (Optional)

**If you want to score:**
```
Points = (Cards Revealed / Total Cards) × 50 + (Budget Remaining / 100) × 50

Example (4-card chain):
- 3 cards revealed: 37.5 points
- 35 budget remaining: 17.5 points
- Total: 55/100 (moderate performance)
```

---

## Discovery Rewards

When your team successfully reveals a Threat Card:

**Choose ONE reward:**

1. **Intelligence Bonus:** Draw 2 additional Defense Cards (keep both)
2. **Budget Grant:** Gain +10 Budget (v2.2 — reduced from +15; represents management approval of your response)
3. **Fast-Track:** On your **next** Investigate action, you succeed on 5+ instead of 11+ (still costs 5 Budget, still need justification modifiers)

---

## Debrief & Reflection (5-10 minutes)

**FOR WINNERS:**
1. "What was your investigation strategy? What worked?"
2. "Which action type (Investigate vs. Deploy Defense) was most effective for you?"
3. "Did Uncontained Threats penalties force you to make reactive decisions? Was that realistic?"

**FOR LOSERS:**
1. "What went wrong in your investigation? Where did you get stuck?"
2. "Would you have benefited from more defense deployments vs. investigations?"
3. "How would you investigate differently if you could replay?"

**EVERYONE:**
1. "What was the attacker's complete kill chain?"
2. "Which threat card was hardest to detect? Why?"
3. "Why isn't this easy to detect in real-world networks?"
4. "What tool or process would have helped you detect faster?"

---

## Tips for Threat Orchestrators

### Creating Effective Clues

**Poor clue (too vague):**
- "You find something suspicious"

**Too good (gives it away):**
- "The attacker used Mimikatz to dump credentials from LSASS memory"

**Just right (progressive disclosure):**
- "Your memory forensics shows suspicious LSASS process manipulation. A tool has dumped credential hashes from memory. Several cached domain admin credentials have been extracted."

### Balancing Difficulty

The game is **too easy** if:
- Teams reveal all cards in turns 1-4 with budget to spare
- Clues are too specific
- Teams succeed on every roll

The game is **too hard** if:
- Teams get stuck after revealing 1 card
- No successful rolls for 5+ turns
- Teams hit the turn limit with only 1-2 cards revealed

**Adjust by:**
- Number of cards (3 vs. 4 vs. 5 — the turn limit scales automatically via (chain × 2) + 1)
- Quality of clues (more/less specific)
- Starting budget (60 vs. 100 vs. 120)
- Turn limit (formula −1 for harder, formula +1 for easier)

### Running Multiple Teams

If running this for a tournament or competitive context:
- Assign different attack chains to each team (or same chain for scoring comparison)
- Teams cannot see each other's progress
- First team to reveal all cards wins
- Tiebreaker: Most Budget remaining

---

## Sample Scenarios to Try

### Scenario 1: "Startup Breach" (Beginner, 3 cards, 30 min)
1. T-01: Phishing Campaign
2. T-06: Mimikatz Credential Dumping
3. T-10: SQL Database Exfiltration

**Focus:** Teaching full kill chain detection in 30 minutes

### Scenario 2: "Nation-State Campaign" (Intermediate, 4 cards, 40 min)
1. T-02: Watering Hole Attack
2. T-04: Lateral Movement via SMB
3. T-07: Scheduled Task Persistence
4. T-09: Beaconing to C2 Server

**Focus:** Sophisticated attack with multiple detection points

### Scenario 3: "Advanced Ransomware" (Advanced, 5 cards, 45 min)
1. T-13: Compromised Software Vendor Update (expansion)
2. T-04: Lateral Movement via SMB
3. T-05: Privilege Escalation via Kernel Exploit
4. T-09: Beaconing to C2 Server
5. T-11: Ransomware Payload Deployment

**Focus:** Complex supply-chain-initiated attack chain

---

## Extensions & Variations

### Solo Play
- Single player as both Blue Team AND Threat Orchestrator
- Orchestrator creates chain, then steps back to investigate
- Requires more discipline but playable

### Speed Mode
- Reduce the turn limit by 2 (extra pressure)
- Remove Uncontained Threats penalty and Active Breach Cost (less bookkeeping)
- Budget costs stay the same
- Good for experienced teams wanting challenge

### Cooperative vs. Competitive
- **Cooperative:** One Blue Team, they win/lose together
- **Competitive:** Multiple Blue Teams, first to reveal all cards wins
- Competitive adds pressure and encourages faster investigation

---

## Next Steps After This Module

**If you won:**
- Continue to **Hardening Module** → Build defenses against discovered threats
- Continue to **Audit & Compliance Module** → Verify your detection methods

**If you lost:**
- Continue to **Disaster Recovery Module** → Manage the breach that succeeded
- Replay with a different strategy
- Try a different scenario

**Standalone:** Play again with a different attack chain

---

## Quick Reference: Action Costs & Outcomes

| Action | Cost | Roll | Success | Failure |
|--------|------|------|---------|---------|
| **Investigate** | 5 Budget | roll + modifiers ≥ 11 | 1st success: clue; 2nd success on same link: reveal (v2.2) | No intel (budget wasted) |
| **Deploy Defense** | 10/15/25 | roll + modifiers ≥ 11 | Full match reveals card immediately | Defense not deployed |
| **Emergency Response** | 15 (v2.2) | None | Remove revealed threat | — |

| Modifier | Effect |
|----------|--------|
| **+2** | Strong technical justification |
| **+1** | Real tool/technique referenced |
| **+2** | Deployed Defense Persistence: deployed defense's vector matches targeted link (v2.2) |

| Tracker | Starting | Changes |
|---------|----------|---------|
| **Budget** | 100 | -5 per uncontained threat + -5 Active Breach Cost while any card is hidden (start of turn, v2.2); floor 0 |
| **Turn** | 1 | +1 each turn (limit = chain × 2 + 1) |
| **Uncontained Threats** | 0 | +1 when revealed, -1 when contained or next card revealed |

*For the full list of v2.2 changes and reasoning, see the "v2.2 Playtest Edition Changes" section in [Module: Incident Response](../rules/module-incident-response.md).*

---

## Need Help?

- **Questions about rules?** See [Core Rules](../rules/core-rules.md)
- **Want to combine modules?** See [Module Combinations](../module-combinations.md)
- **Confused about modifiers?** See [FRAMEWORK.md](../FRAMEWORK.md)

---

*Incident Response Module - Standalone Play Guide*
*Part of Incident Zero, a modular cybersecurity board game*

