# Incident Response Module: Rules & Mechanics

**Version:** 2.1 - Balanced & Refined Edition
**Last Updated:** October 2025

---

## Module Overview

The **Incident Response Module** is the foundation of Incident Zero. Players act as a security operations center (SOC) team responding to an active cyberattack. The core challenge: **reveal a hidden attack chain before time runs out or budget is exhausted**.

This module teaches:
- **Primary:** Cyber kill chain understanding, threat detection, evidence gathering
- **Secondary:** Resource prioritization, incident response under pressure, forensic investigation

**Key Mechanics:**
- Hidden attack chain (3-5 Threat Cards) is pre-built by the Threat Orchestrator
- Blue Team reveals cards by successfully investigating or deploying appropriate defenses
- Uncontained Threats Penalty creates urgency—revealed threats cost 5 Budget per turn until contained
- Emergency Response action provides a budget-intensive way to contain uncontained threats

---

## Module Setup (5 minutes)

### 1. Choose Difficulty Level

| Difficulty | Chain Length | Starting Budget | Turn Limit | Best For |
|------------|--------------|-----------------|-----------|----------|
| **Beginner** | 3 cards | 100 | 12 turns | First playthrough, basic learning |
| **Intermediate** | 4 cards | 100 | 10 turns | Standard play, mixed experience |
| **Advanced** | 5 cards | 100 | 10 turns | Experienced players, challenge |

**Scaling Notes:**
- Beginner: ~30 min session, teaches full kill chain with comfortable pace
- Intermediate: ~40 min session, requires focused investigation strategy
- Advanced: ~45 min session, demands efficient resource allocation and quick thinking

### 2. Threat Orchestrator Preparation

**Create the Hidden Attack Chain:**
1. Select 3-5 Threat Cards from the deck
2. Arrange them in logical attack chain sequence:
   - First card: INITIAL COMPROMISE
   - Middle cards: PIVOT & ESCALATE, PERSISTENCE
   - Final card: C2 & EXFIL
3. Write down clues for each hidden card on separate paper (keep hidden from Blue Team)
4. Place relevant Asset Cards on the table (visible to all—provides scenario context)

**Attack Chain Strategy Tips:**
- Start simple (Beginner): Phishing → Lateral Movement → Database Exfil
- Intermediate: Phishing → Credential Dumping → VPN Access → Persistence → C2 Beaconing
- Advanced: Web Exploit → Lateral Movement → Privilege Escalation → Data Staging → Exfiltration

**Recommended First-Time Scenario (3 cards, 30 minutes):**
1. T-01: Phishing Campaign (INITIAL COMPROMISE - SOCIAL ENGINEERING)
2. T-04: Lateral Movement via SMB (PIVOT & ESCALATE - NETWORK)
3. T-10: SQL Database Exfiltration (C2 & EXFIL - DATA EXFIL)

### 3. Blue Team Setup

Initialize trackers and materials:

| Item | Starting Value |
|------|-----------------|
| **Turn Tracker** | 1 |
| **Budget Tracker** | 100 |
| **Uncontained Threats Tracker** | 0 |
| **Defense Cards** | Draw 5 (face down) |

### 4. Read the Opening Scenario

Threat Orchestrator delivers opening narrative using **only** the first hidden card's clue. Example:

> "Your security operations center is monitoring the network when alerts begin firing. Your SIEM shows suspicious email traffic coming from your IT department domain, but the headers look spoofed. Several employees have reported clicking links in emails they thought came from IT requesting password resets.
>
> You have limited time and budget to investigate before the attacker escalates. What do you do?"

---

## Gameplay Loop (25-35 minutes)

### Round Structure

Each turn represents approximately 2-4 hours of incident response operations.

**COMPLETE TURN SEQUENCE:**

**1. START OF TURN**
- **Apply Uncontained Threats Penalty:** For each revealed-but-uncontained threat, deduct 5 Budget from the tracker
- Announce current turn number and budget remaining
- Example: "Turn 3. You have 80 Budget remaining. Your Uncontained Threats penalty is 10 Budget (2 threats × 5)."

**2. BLUE TEAM'S TURN (2-3 minutes discussion)**
- Team discusses incident response strategy
- Decides on ONE action to take this turn (Investigate, Deploy Defense, or Emergency Response)
- Team member announces action and parameters (what they're investigating, which defense they're deploying, etc.)

**3. ACTION RESOLUTION**
- Perform chosen action (see three actions below)
- Roll 1d20 if action requires a roll
- Apply modifiers (see modifier rules in core-rules.md)
- Resolve outcome immediately

**4. END OF TURN**
- Advance Turn Tracker by 1
- Draw 1 new Defense Card (add to hand)
- Check if game has been won or lost (see victory/defeat conditions below)
- If still playing, return to START OF TURN

---

## Three Incident Response Actions

### Action 1: Investigate 🔎

**Cost:** 5 Budget per action
**Roll Required:** 11+ on d20
**Special Rule:** Modifiers apply and can stack

**How It Works:**

1. **Team describes what they're investigating** (email headers, system logs, network traffic, memory dumps, etc.)
2. **Provide technical justification** for your investigation approach
3. **Roll 1d20**
4. **Compare:** roll + modifiers ≥ 11?

**Roll Modifiers:**

| Bonus | When Awarded | Examples |
|-------|--------------|----------|
| **+2** | Strong technical justification | "We're analyzing email headers in the mail gateway logs to identify the true sender IP and check it against threat intelligence feeds. This helps us understand the initial compromise vector." |
| **+1** | Real security tools/techniques referenced | "We'll query our SIEM for scheduled task creation events" or "We're checking for Mimikatz usage in memory" |
| **+0** | Vague investigation | "We want to find suspicious activity" |

**Success (roll + modifiers ≥ 11):**
- TO provides a **verbal clue** about the **next card in the chain** (one card forward)
- Example: If Phishing is revealed, successful investigation gives clue about the Lateral Movement card
- Clue should be dramatic and progressive—give more detail with each successful investigation
- Budget is spent (5 is deducted)

**Failure (roll + modifiers < 11):**
- "Your investigation yields no actionable intelligence at this time"
- Budget is spent anyway (5 is deducted)
- Team learns nothing but advances in time
- Failure is realistic—not every investigation uncovers information

**Strategic Consideration:**
- Cheap action (only 5 Budget)
- Moderate success chance (need 11+ on d20, so ~40% without bonuses)
- High reward for successful investigation (information about next threat)
- Can be repeated multiple times in a game

---

### Action 2: Deploy a Defense 🛡️

**Cost:** 10/15/25 Budget (depending on Defense Card tier: BASIC/ADVANCED/ELITE)
**Roll Required:** 11+ on d20
**Special Rule:** Modifiers apply; matching defense to threat can reveal cards

**How It Works:**

1. **Choose a Defense Card** from your hand (or any card in your hand)
2. **Target a specific Asset or threat vector** (state what you're defending)
3. **Explain your strategy** (optional but encouraged for +2 modifier): "Why is this defense appropriate for the current situation?"
4. **Roll 1d20**
5. **Compare:** roll + modifiers ≥ 11?

**Roll Modifiers:** Same as Investigate action (+2 for justification, +1 for tools)

**Success (roll + modifiers ≥ 11):**

Check if Defense Card matches hidden threat:
- **FULL MATCH:** Defense **Countermeasure Vector** matches threat's **Attack Vector** AND it's the **correct step in the chain**
  - **THREAT CARD IS REVEALED!** Threat card is placed face-up on the table. Blue Team learns what they've been fighting.
  - Threat card is now "uncontained" (add 1 to Uncontained Threats Tracker)
  - Defense Card is discarded (used)
  - Budget is spent

- **PARTIAL MATCH:** Defense matches the vector but wrong step in chain, OR right step but wrong vector
  - Defense is deployed and stays on table (helpful for future turns)
  - Card is not revealed
  - Budget is spent
  - Defense remains active for future investigation/defense rolls

- **NO MATCH:** Defense doesn't address current threat
  - Defense is deployed but ineffective
  - Budget is spent
  - Defense remains on table (might help against future threats)

**Failure (roll + modifiers < 11):**
- Defense fails to deploy properly
- Budget is spent anyway
- Card is discarded
- No progress made, but team learns from failure

**Key Point:** Even "unsuccessful" Defense deployments can be strategically valuable. Deployed defenses stay in play and may counter later threats you didn't anticipate.

**Strategic Consideration:**
- Expensive action (10-25 Budget, scales with defense tier)
- Moderate success chance (same 11+ threshold as Investigate)
- Two potential rewards: Defense deployment AND card reveal
- High-risk/high-reward compared to Investigate

**Example Scenario:**
```
Hidden attack chain: Phishing → Lateral Movement → Database Exfil

Team believes phishing is happening (first card).
They deploy "Email Authentication Setup" (BASIC, 10 Budget).
Email Authentication addresses SOCIAL ENGINEERING vector.

Roll: 8 + 2 (strong justification) = 10 = FAIL
Email deployment fails, 10 Budget wasted, but card stays.

Next turn: Same team deploys "User Security Training" (BASIC, 10 Budget).
Roll: 13 + 1 = 14 = SUCCESS
Defense addresses SOCIAL ENGINEERING vector and is INITIAL COMPROMISE step.
PHISHING CAMPAIGN REVEALED! Threat card placed face-up.
Uncontained Threats increases to 1 (now costing 5 Budget per turn).
```

---

### Action 3: Emergency Response 🚨

**Cost:** 25 Budget (expensive, flat cost)
**Roll Required:** None—this always succeeds
**Special Rule:** Only works on previously revealed threats

**How It Works:**

1. **Choose a revealed Threat Card** still in play (face-up on table)
2. **Describe your containment strategy** in detail:
   - Quarantine infected systems
   - Disable compromised accounts
   - Isolate network segments
   - Kill active processes
   - Revoke stolen credentials
   - etc.
3. **Pay the 25 Budget cost**
4. **Card is immediately removed from play**
5. **Uncontained Threats Tracker decreases by 1** (penalty stops for this threat)

**Strategic Use Cases:**

- **Panic Defense:** If you're accumulating too many uncontained threats and running out of budget
- **Time Management:** If you're approaching the turn limit and need to reduce penalties
- **Preparation for Next Module:** If continuing to Hardening or other modules, fewer threats = more budget available
- **Complexity Reduction:** If the game feels overwhelming, emergency response simplifies the threat landscape

**Example Timeline:**

```
Turn 1: Phishing revealed → Uncontained Threats = 1
Turn 2: START → Deduct 5 Budget (95 remaining)
Turn 3: Lateral Movement revealed → Phishing auto-mitigates (Uncontained = 1)
Turn 3: Team also takes Emergency Response on Lateral Movement
        → Pay 25 Budget, remove Lateral Movement card
        → Uncontained Threats = 0 (no more penalties)
        → Budget now 70
```

---

## Uncontained Threats Penalty Mechanics

This is the core urgency mechanic of Incident Response. **Dwell time costs money.**

### How the Penalty Works

**Step 1: Threat Revealed**
- When a Threat Card is successfully revealed (by investigation or defense deployment)
- Add 1 to the Uncontained Threats Tracker
- This threat is now "active" and dangerous

**Step 2: Penalty Applied at Turn Start**
- At the **START of every turn**, deduct **5 Budget per uncontained threat**
- Example: 2 uncontained threats = 10 Budget penalty each turn
- This creates continuous pressure—you MUST reveal/contain threats or lose resources

**Step 3: Auto-Mitigation**
- When the **next card in the attack chain is revealed**, the previous uncontained threat is automatically "contained" (represents shift of attention to new priority)
- Uncontained Threats Tracker decreases by 1
- Penalties decrease immediately

**Step 4: Emergency Response Containment**
- Team can use Emergency Response action to **immediately** remove a threat from the board
- Cost: 25 Budget (expensive, but stops the penalty immediately)
- Uncontained Threats Tracker decreases by 1

### Example Walkthrough

```
SETUP: 3-card chain (Phishing → Lateral Movement → Database Exfil)

Turn 1: START → 0 uncontained threats, no penalty
        INVESTIGATION → "Email spoofing detected"
        Clue given about next card

Turn 2: START → Still 0 uncontained (clue doesn't count as reveal)
        DEFENSE DEPLOYMENT → Deploy Email Authentication
        Roll succeeds, card matches
        ✓ PHISHING CAMPAIGN REVEALED (card placed face-up)
        Uncontained Threats = 1

Turn 3: START → Deduct 5 Budget (now 95 remaining)
        INVESTIGATION → Investigate network logs
        Roll succeeds
        Clue given about Lateral Movement

Turn 4: START → Deduct 5 Budget (now 90 remaining)
        DEFENSE → Deploy Network Segmentation (ADVANCED, 15 Budget)
        Roll succeeds, card matches (NETWORK vector, PIVOT & ESCALATE step)
        ✓ LATERAL MOVEMENT REVEALED (placed face-up)
        Previous threat (Phishing) auto-mitigates (Uncontained = 1)
        New threat (Lateral Movement) is uncontained (Uncontained = 1)

Turn 5: START → Deduct 5 Budget (now 70 remaining)
        INVESTIGATION → Investigate database access logs
        Roll fails
        No progress

Turn 6: START → Deduct 5 Budget (now 65 remaining)
        EMERGENCY RESPONSE → Contain Lateral Movement
        Cost 25 Budget
        Card removed from play
        Uncontained Threats = 0 (no more penalties!)

Turn 7: START → No penalties!
        INVESTIGATION → Investigate suspicious file transfers
        Roll succeeds
        Clue given about Database Exfil

Turn 8: START → No penalties
        DEFENSE → Deploy Data Loss Prevention (ELITE, 25 Budget)
        Roll succeeds, card matches
        ✓ DATABASE EXFILTRATION REVEALED

WIN! All cards revealed with 40 Budget remaining
```

---

## Winning & Losing

### Victory Condition ✓

**Blue Team wins Incident Response if:**
1. ALL threat cards in the attack chain are revealed (face-up on table), AND
2. This happens BEFORE Turn Tracker reaches your turn limit (10, 12, or custom), AND
3. Budget never reaches 0 (team can always continue taking actions)

**Winning Scenarios:**
- Beginner: All 3 cards revealed by Turn 8 with 30+ Budget remaining = solid victory
- Intermediate: All 4 cards revealed by Turn 9 with 20+ Budget remaining = solid victory
- Advanced: All 5 cards revealed by Turn 9 with 10+ Budget remaining = impressive victory

### Defeat Condition ✗

**Blue Team loses Incident Response if:**
1. Turn Tracker reaches the turn limit (10 for standard) with unrevealed cards remaining, OR
2. Budget reaches 0 (team cannot take further actions even if turns remain)

**Losing Scenarios:**
- Turns expired with only 2 of 4 cards revealed = attack succeeded
- Budget exhausted on Turn 5 of 10 = response ran out of resources

### Victory Scoring (Optional)

If you want to measure quality of victory:

```
Victory Points Formula:
Points = (Cards Revealed / Total Cards) × 50 + (Budget Remaining / Starting Budget) × 50

Examples:
- 4 cards revealed (4/4), 35 Budget remaining: (100 × 50) + (35/100 × 50) = 50 + 17.5 = 67.5/100 (Victory with good efficiency)
- 3 cards revealed (3/4), 15 Budget remaining: (75 × 50) + (15/100 × 50) = 37.5 + 7.5 = 45/100 (Partial victory, struggled)
- 2 cards revealed (2/4), 0 Budget: (50 × 50) + (0 × 50) = 25/100 (Defeat)
```

---

## Discovery Rewards

When your team **successfully reveals a Threat Card**, immediately **choose ONE of these rewards:**

### Reward Option 1: Intelligence Bonus 📚
- **Effect:** Draw 2 additional Defense Cards immediately (keep both)
- **When to Choose:** If you feel your current hand is weak, or you want more tactical options
- **Strategic Value:** More options = better chance of finding right defense for next threat

### Reward Option 2: Budget Grant 💰
- **Effect:** Gain +15 Budget
- **When to Choose:** If you're running low on Budget and want more runway
- **Strategic Value:** Directly extends how long you can keep investigating/defending

### Reward Option 3: Fast-Track Investigation 🚀
- **Effect:** On your **next** Investigate action (only the next one), you succeed on 5+ instead of 11+ (still costs 5 Budget, still need justification modifiers)
- **When to Choose:** If you want guaranteed next investigation success
- **Strategic Value:** Guaranteed clue about next card in chain

**Important:** Choose only ONE reward per card reveal. Cannot combine rewards.

---

## Debrief & Reflection (5-10 minutes)

Every game should conclude with guided reflection connecting game mechanics to real security concepts.

### For Winners (Questions about Success)

1. **"What was your investigation strategy? What worked best?"**
   - Explore which investigation themes were most successful
   - Discuss whether they targeted the right logs/evidence first

2. **"Which action type was most effective for you—Investigate or Deploy Defense?"**
   - Some teams succeed with heavy investigation, others with defense-focused discovery
   - Both are valid; discuss trade-offs

3. **"How did Uncontained Threats penalties affect your decisions?"**
   - Did they force you to make reactive decisions?
   - Were they realistic representations of incident response costs?

4. **"If you replayed, what would you do differently?"**
   - Reflection on optimization and efficiency
   - Planning better strategies for next playthrough

### For Losers (Questions about Learning)

1. **"What went wrong in your investigation? Where did you get stuck?"**
   - Identify which threat was hardest to detect and why
   - Discuss investigation approaches that didn't work

2. **"Would you have benefited from more defense deployments vs. investigations?"**
   - Analyze if budget allocation strategy was optimal
   - Discuss risk/reward trade-offs

3. **"How would you investigate differently if you could replay?"**
   - Recovery and learning from failure
   - Strategic adjustments for next attempt

4. **"What was the attacker's complete kill chain?"**
   - TO reveals the full hidden attack chain (all cards, clues, explanations)
   - Discussion of what signals should have tipped them off

### For Everyone (Real-World Connection)

1. **"What was the attacker's complete kill chain? Which step was most critical?"**
   - Understand the full attack story
   - Discuss which card took longest to detect and why

2. **"Why isn't this easy to detect in real-world networks?"**
   - Real attacks hide in massive volumes of legitimate traffic
   - Attackers use living-off-the-land techniques
   - Detection requires specific telemetry (EDR, SIEM, network monitoring)

3. **"What tool or process would have helped you detect faster?"**
   - Threat hunting
   - Behavioral analytics
   - Specific log sources (PowerShell logs, Sysmon, Zeek)
   - User and Entity Behavior Analytics (UEBA)

4. **"How does game dwell time compare to real breaches?"**
   - Average dwell time in real breaches: 200+ days
   - Game represents 2-8 hours of focused investigation
   - Discussion of why real dwell times are so long

---

## Tips for Threat Orchestrators

### Before the Game (Preparation)

1. **Read the module rules completely** - Understand Investigate, Deploy Defense, and Emergency Response mechanics
2. **Prepare your attack chain** - Pre-build or write down your 3-5 hidden cards in sequence
3. **Write clear clues** - For each card, write 2-3 progressive clues that reveal information gradually
4. **Organize materials** - Sort Defense Cards by tier, prepare trackers, have dice ready
5. **Practice reading clues dramatically** - Deliver them with narrative flair to create engagement

### Crafting Effective Clues

**Poor clue (too vague, gives nothing away):**
- "You find something suspicious"
- "There's a threat somewhere"

**Bad clue (gives it away completely):**
- "The attacker used Mimikatz to dump credentials from LSASS memory"
- "You have a database exfiltration happening right now"

**Good clue (progressive disclosure, dramatic delivery):**
- "Your memory forensics shows suspicious LSASS process manipulation. A tool has dumped credential hashes from memory. Several cached domain admin credentials have been extracted."

**Excellent clue (specific without revealing, creates narrative):**
- "Your EDR shows PowerShell activity with suspicious encoding. Memory access patterns suggest credential harvesting. Your domain admin cached credentials appear to have been targeted."

### Balancing Difficulty During Play

**The game is TOO EASY if:**
- Team reveals all cards in turns 1-4 with 60+ Budget remaining
- Multiple consecutive successful rolls (unlikely with d20)
- Clues are too specific/obvious
- Team makes no difficult decisions

**Action:** Make clues more subtle, reduce starting budget next time, or add extra card to chain

**The game is TOO HARD if:**
- Team gets stuck after revealing only 1 card (5+ turns with no progress)
- Multiple consecutive failed rolls
- Team is frustrated rather than challenged
- Team is out of ideas about what to investigate

**Action:** Provide more explicit clues, increase starting budget, reduce chain length

**Adjustment Options:**
- **Chain Length:** 3 (easier) vs. 4 (medium) vs. 5 (harder)
- **Clue Quality:** More specific/obvious (easier) vs. subtle (harder)
- **Starting Budget:** 80 (harder) vs. 100 (medium) vs. 120 (easier)
- **Turn Limit:** 8 (harder) vs. 10 (medium) vs. 12 (easier)

### Running Competitive Games (Multiple Teams)

If running for tournament or competitive context:

1. **Assign different attack chains** to each team (or same chain for scoring comparison)
2. **Teams cannot see each other's progress** (prevents copying strategies)
3. **Scoring:** First team to reveal all cards wins; tiebreaker is most Budget remaining
4. **Set clear turn/budget limits** before game starts
5. **Track publicly** so teams know they're racing against time/budget

---

## Sample Scenarios to Try

### Scenario 1: "Startup Breach" (Beginner, 3 cards, 30 minutes)

**Attack Chain:**
1. T-01: Phishing Campaign (INITIAL COMPROMISE - SOCIAL ENGINEERING)
2. T-06: Mimikatz Credential Dumping (PIVOT & ESCALATE - CREDENTIAL ABUSE)
3. T-10: SQL Database Exfiltration (C2 & EXFIL - DATA EXFIL)

**Starting Budget:** 100
**Turn Limit:** 12

**Narrative Setup:**
> "Your startup just deployed a new customer database. An employee clicked a malicious link in an email claiming to be from IT. Security monitoring detected unusual PowerShell activity after that. Now you're investigating what happened."

**Focus:** Teaching full kill chain detection (initial → credential harvesting → data theft)
**Expected Duration:** 30 minutes
**Best For:** First-time players, classroom introduction

**Sample Defenses in Starting Hand:**
- Email Authentication Setup (BASIC, 10)
- User Security Training (BASIC, 10)
- Multi-Factor Authentication (ADVANCED, 15)
- EDR Agent Deployment (ADVANCED, 15)
- Data Loss Prevention (ELITE, 25)

---

### Scenario 2: "Nation-State Campaign" (Intermediate, 4 cards, 40 minutes)

**Attack Chain:**
1. T-02: Watering Hole Attack (INITIAL COMPROMISE - WEB EXPLOIT)
2. T-04: Lateral Movement via SMB (PIVOT & ESCALATE - NETWORK)
3. T-07: Scheduled Task Persistence (PERSISTENCE - MALWARE)
4. T-09: Beaconing to C2 Server (C2 & EXFIL - NETWORK)

**Starting Budget:** 100
**Turn Limit:** 10

**Narrative Setup:**
> "Your organization's industry-specific website was silently compromised last month. A sophisticated attacker injected malicious code that targeted specific visitor browsers. One of your engineers visited the site and became infected. You're detecting strange network activity but aren't sure what's happening."

**Focus:** Sophisticated attack with multiple detection points; requires multiple defense/investigation attempts
**Expected Duration:** 40 minutes
**Best For:** Experienced players, demonstrating complex kill chain

**Sample Defenses:**
- Web Application Firewall (ADVANCED, 15)
- Network Segmentation (ADVANCED, 15)
- Host-Based Firewall Rules (BASIC, 10)
- EDR Agent Deployment (ADVANCED, 15)
- Threat Hunting (ELITE, 25)
- Memory Forensics (ELITE, 25)

---

### Scenario 3: "Advanced Ransomware Supply Chain" (Advanced, 5 cards, 45 minutes)

**Attack Chain:**
1. T-13: Compromised Software Vendor Update (INITIAL COMPROMISE - MALWARE)
2. T-04: Lateral Movement via SMB (PIVOT & ESCALATE - NETWORK)
3. T-05: Privilege Escalation via Kernel Exploit (PIVOT & ESCALATE - MALWARE)
4. T-09: Beaconing to C2 Server (C2 & EXFIL - NETWORK)
5. T-11: Ransomware Payload Deployment (C2 & EXFIL - MALWARE)

**Starting Budget:** 100
**Turn Limit:** 10

**Narrative Setup:**
> "A trusted software vendor released an update to your monitoring tools three weeks ago. Today, you're detecting ransomware-like activity across your infrastructure. You suspect the vendor update was compromised. Can you trace the attack chain before the ransomware wakes up?"

**Focus:** Complex supply-chain-initiated attack; requires pattern recognition; high pressure
**Expected Duration:** 45 minutes
**Best For:** Advanced players, demonstrating supply chain risk

**Sample Defenses:**
- Vendor Security Verification (ADVANCED, 15)
- EDR Agent Deployment (ADVANCED, 15)
- Network Segmentation (ADVANCED, 15)
- Ransomware-Specific Behavior Detection (ELITE, 25)
- Kernel Exploit Mitigations (ELITE, 25)
- Memory Forensics (ELITE, 25)
- Data Loss Prevention (ELITE, 25)

---

## Extensions & Variations

### Variation 1: Solo Play Mode

**How to Play Solo:**
- Single player acts as both Blue Team AND Threat Orchestrator
- Orchestrator creates attack chain before game starts
- Orchestrator then "steps back" to investigate (hard mode: don't peek at hidden cards)
- Requires discipline: don't use knowledge of chain to guide rolls

**Best For:** Individual learning, skill practice

---

### Variation 2: Speed Mode

**Compress the Game:**
- Reduce turn limit to 8 (extra pressure)
- Optional: Remove Uncontained Threats penalty (less bookkeeping)
- Budget costs stay the same
- Budget starts at 120 to balance speed pressure

**Best For:** Experienced teams wanting high-stakes challenge

---

### Variation 3: Extended Investigation (Advanced)

**Deeper Forensics:**
- Add "Advanced Investigate" action (costs 15 Budget, rolls 11+)
- Advanced Investigate provides more detailed clues or reveals multiple cards if targeting chain end
- Allows for riskier but more rewarding investigation strategy

**Best For:** Players who want forensic investigation to feel more rewarding

---

### Variation 4: Competitive Tournament

**Multiple Teams, Same Challenge:**
1. All teams receive the same 4-card attack chain
2. All teams start with same 100 Budget, same 5 Defense Cards drawn
3. Teams play simultaneously (or in sequence) against same scenario
4. Scoring: Cards revealed + Budget remaining = final score
5. Tiebreaker: Fewest turns taken

**Best For:** Classroom competition, conference play, benchmarking

---

## Next Steps After This Module

### If You Won (Completed All Cards)

**Option 1: Continue to Hardening Module**
- Excellent choice if building defenses against discovered threats
- Use the attack chain you just discovered as the hardening context
- Natural progression: detect the attack → now prevent it

**Option 2: Continue to Audit & Compliance Module**
- Great for understanding how to detect this attack chain
- Validates that your detection methods work
- Audits your existing security controls

### If You Lost (Time/Budget Expired)

**Option 1: Continue to Disaster Recovery Module**
- Appropriate: assume the attack succeeded
- Manage the breach that just happened
- Focus on response, stakeholder communication, recovery

**Option 2: Replay with Different Strategy**
- Try again with different investigation/defense approach
- Use what you learned to optimize for next attempt

**Option 3: Study Real Breach Case Studies**
- Compare your experience to real breaches (Equifax, Target, SolarWinds)
- Understand why real dwell times are 200+ days
- Learn what signals real defenders look for

### Standalone Play

**Play Again with:**
- Different attack chain from the card deck
- Different difficulty (if you won easily or struggled)
- Competitive mode against other teams
- Extended variations with different mechanics

---

## Quick Reference: Actions & Costs

| Action | Cost | Roll Required | Success Condition | Failure Condition |
|--------|------|---------------|-------------------|--------------------|
| **Investigate** | 5 Budget | 11+ on d20 | Clue about next card | No intel gained |
| **Deploy Defense** | 10/15/25 | 11+ on d20 | Possibly reveal card | Defense not deployed |
| **Emergency Response** | 25 Budget | None | Threat removed, penalty stops | — |

---

## Quick Reference: Modifiers

| Bonus | When Awarded | Examples |
|-------|--------------|----------|
| **+2** | Strong technical justification | "Analyze mail headers in gateway logs to identify true sender IP, check against threat intelligence" |
| **+1** | Real security tools/techniques | "Query SIEM for scheduled tasks", "Check Mimikatz in memory", "Review EDR telemetry" |
| **+0** | Vague/no justification | "Find suspicious activity" |

---

## Quick Reference: Trackers

| Tracker | Starts At | Changes |
|---------|-----------|---------|
| **Budget** | 100 | -5 per Investigate, -10/15/25 per Defense, -25 per Emergency Response, -5 per uncontained threat at turn start |
| **Turn** | 1 | +1 each turn |
| **Uncontained Threats** | 0 | +1 when card revealed, -1 when auto-mitigated or Emergency Response used |

---

## Need Help?

- **Questions about universal rules?** See [Core Rules](core-rules.md)
- **Want to combine modules?** See [Module Combinations](../module-combinations.md)
- **Understanding modifier stacking?** See [Core Rules: Roll Modifiers](core-rules.md#4-roll-modifiers-universal)
- **How to play Incident Response standalone?** See [Standalone Play Guide](../standalone-games/incident-response.md)

---

*Incident Response Module - Rules & Mechanics*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.1 - Balanced & Refined Edition*
