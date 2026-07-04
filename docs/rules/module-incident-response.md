# Incident Response Module: Rules & Mechanics

**Version:** 2.2 - Playtest Edition
**Last Updated:** July 2026

---

## Module Overview

The **Incident Response Module** is the foundation of Incident Zero. Players act as a security operations center (SOC) team responding to an active cyberattack. The core challenge: **reveal a hidden attack chain before time runs out or budget is exhausted**.

This module teaches:
- **Primary:** Cyber kill chain understanding, threat detection, evidence gathering
- **Secondary:** Resource prioritization, incident response under pressure, forensic investigation

**Key Mechanics:**
- Hidden attack chain (3-5 Threat Cards) is pre-built by the Threat Orchestrator
- Blue Team reveals cards by successful investigation (two successes on the same chain link, v2.2) or by deploying a vector+step-matching defense
- Uncontained Threats Penalty creates urgency—revealed threats cost 5 Budget per turn until contained
- Active Breach Cost (v2.2)—while any chain card remains hidden, the breach itself costs 5 Budget per turn (dwell time is never free)
- Emergency Response action provides a way to contain uncontained threats (15 Budget, v2.2)

---

## Module Setup (5 minutes)

### 1. Choose Difficulty Level

Turn limits use the **Variable Game Length formula** from [Core Rules §3a](core-rules.md#3a-variable-game-length-system-v21---new): **Turn Limit = (Attack Chain Cards × 2) + 1**.

| Difficulty | Chain Length | Starting Budget | Turn Limit | Best For |
|------------|--------------|-----------------|-----------|----------|
| **Beginner** | 3 cards | 100 | 7 turns | First playthrough, basic learning |
| **Intermediate** | 4 cards | 100 | 9 turns | Standard play, mixed experience |
| **Advanced** | 5 cards | 100 | 11 turns | Experienced players, challenge |

**Scaling Notes:**
- Beginner: ~30 min session, teaches full kill chain with comfortable pace
- Intermediate: ~40 min session, requires focused investigation strategy
- Advanced: ~45 min session, demands efficient resource allocation and quick thinking
- Advanced Threat Orchestrators can instead use the Tier + d4 system in [Core Rules §3a](core-rules.md#3a-variable-game-length-system-v21---new)

### 2. Threat Orchestrator Preparation

**Create the Hidden Attack Chain:**
1. Select 3-5 Threat Cards from the deck
2. Arrange them in logical attack chain sequence:
   - First card: INITIAL COMPROMISE
   - Middle cards: PIVOT & ESCALATE, PERSISTENCE
   - Final card: C2 & EXFIL
3. Write down clues for each hidden card on separate paper (keep hidden from Blue Team)
4. Place relevant Asset Cards on the table (visible to all—provides scenario context). Asset Cards are shared components: see `cards/network-building/core-deck/asset-cards.md`

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
- **Apply Active Breach Cost (v2.2):** If at least one chain card is still unrevealed, deduct 5 Budget (the hidden breach is doing damage while you can't see it)
- Announce current turn number and budget remaining
- Example: "Turn 3. Start-of-turn costs: 5 for your uncontained threat, plus 5 Active Breach Cost—the chain isn't fully mapped yet. Budget drops from 85 to 75."

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

### Sequential Discovery (v2.2 clarification)

The attack chain is discovered **in order**: only the **earliest unrevealed chain card** can be investigated toward or revealed. Clues, investigation successes, and Deploy Defense reveals all target that card until it is face-up, then attention shifts to the next link. This matches how the clue system walks the kill chain.

### Deployed Defense Persistence (v2.2)

Deployed defenses stay on the table and keep working. **Whenever the chain link currently being targeted has an Attack Vector matching a deployed defense's Countermeasure Vector, add +2 to Investigate and Deploy Defense rolls against that link.** The Threat Orchestrator (who knows the hidden vector) announces when this bonus applies—hearing "your deployed defenses are helping here" is itself a useful clue. This rule is stated once here; other sections simply refer to it.

---

## Three Incident Response Actions

### Action 1: Investigate 🔎

**Cost:** 5 Budget per action
**Roll Required:** roll + modifiers ≥ 11 on d20
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
| **+2** | Deployed Defense Persistence (v2.2) | A deployed defense's vector matches the targeted chain link (see rule above) |
| **+0** | Vague investigation | "We want to find suspicious activity" |

**Success (roll + modifiers ≥ 11) — Investigation successes accumulate (v2.2):**
- **First success against a chain link:** TO provides a **verbal clue** about that card (the earliest unrevealed card in the chain)
- **Second success against the same chain link:** **THE CARD IS REVEALED!** Place it face-up; it becomes uncontained (add 1 to the Uncontained Threats Tracker) and the team chooses a Discovery Reward
- Clues should be dramatic and progressive—give more detail with each successful investigation
- Budget is spent (5 is deducted)

**Failure (roll + modifiers < 11):**
- "Your investigation yields no actionable intelligence at this time"
- Budget is spent anyway (5 is deducted)
- Team learns nothing but advances in time
- Failure is realistic—not every investigation uncovers information
- Failures do NOT count toward the two accumulated successes

**Strategic Consideration:**
- Cheap action (only 5 Budget)
- Moderate success chance (need 11+ on d20, so ~50% without bonuses)
- Two successful investigations reveal a card without needing the right Defense Card in hand (v2.2)
- Deploy Defense (full match) is faster—one successful roll—but costs more and needs the right card

---

### Action 2: Deploy a Defense 🛡️

**Cost:** 10/15/25 Budget (depending on Defense Card tier: BASIC/ADVANCED/ELITE)
**Roll Required:** roll + modifiers ≥ 11 on d20
**Special Rule:** Modifiers apply; matching defense to threat reveals cards immediately

**How It Works:**

1. **Choose a Defense Card** from your hand (or any card in your hand)
2. **Target a specific Asset or threat vector** (state what you're defending)
3. **Explain your strategy** (optional but encouraged for +2 modifier): "Why is this defense appropriate for the current situation?"
4. **Roll 1d20**
5. **Compare:** roll + modifiers ≥ 11?

**Roll Modifiers:** Same as Investigate action (+2 for justification, +1 for tools, +2 Deployed Defense Persistence if applicable)

**Success (roll + modifiers ≥ 11):**

Check if Defense Card matches the earliest unrevealed hidden threat (sequential discovery):
- **FULL MATCH:** Defense **Countermeasure Vector** matches threat's **Attack Vector** AND it's the **correct step in the chain**
  - **THREAT CARD IS REVEALED IMMEDIATELY!** Threat card is placed face-up on the table. Blue Team learns what they've been fighting.
  - Threat card is now "uncontained" (add 1 to Uncontained Threats Tracker)
  - Defense Card is discarded (used)
  - Budget is spent

- **PARTIAL MATCH:** Defense matches the vector but wrong step in chain, OR right step but wrong vector
  - Defense is deployed and stays on table (helpful for future turns)
  - Card is not revealed
  - Budget is spent
  - Defense remains active—see Deployed Defense Persistence (v2.2): it grants +2 to future rolls against any chain link matching its vector

- **NO MATCH:** Defense doesn't address current threat
  - Defense is deployed but ineffective
  - Budget is spent
  - Defense remains on table (might grant the +2 persistence bonus against future threats)

**Failure (roll + modifiers < 11):**
- Defense fails to deploy properly
- Budget is spent anyway
- Card is discarded
- No progress made, but team learns from failure

**Key Point:** Even "unsuccessful" Defense deployments can be strategically valuable. Deployed defenses stay in play and grant +2 to rolls against later threats that match their vector (v2.2).

**Strategic Consideration:**
- Expensive action (10-25 Budget, scales with defense tier)
- Moderate success chance (same 11+ threshold as Investigate)
- Two potential rewards: Defense deployment AND card reveal
- High-risk/high-reward compared to Investigate

**Example Scenario:**
```
Hidden attack chain: Phishing → Lateral Movement → Database Exfil

Team believes phishing is happening (first card).
They deploy D-01 "Email Authentication Setup" (BASIC, 10 Budget).
Email Authentication addresses SOCIAL ENGINEERING vector.

Roll: 8 + 2 (strong justification) = 10 = FAIL
Email deployment fails, 10 Budget spent, card discarded.

Next turn: Same team deploys D-02 "User Security Training" (BASIC, 10 Budget).
Roll: 13 + 1 = 14 = SUCCESS
Defense addresses SOCIAL ENGINEERING vector and is INITIAL COMPROMISE step.
PHISHING CAMPAIGN REVEALED! Threat card placed face-up.
Uncontained Threats increases to 1 (now costing 5 Budget per turn).
```

---

### Action 3: Emergency Response 🚨

**Cost:** 15 Budget (v2.2 — repriced from 25; flat cost)
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
3. **Pay the 15 Budget cost**
4. **Card is immediately removed from play**
5. **Uncontained Threats Tracker decreases by 1** (penalty stops for this threat)

**Strategic Use Cases:**

- **Panic Defense:** If you're accumulating too many uncontained threats and running out of budget
- **Time Management:** If you're approaching the turn limit and need to reduce penalties
- **Preparation for Next Module:** If continuing to Hardening or other modules, fewer threats = more budget available
- **Complexity Reduction:** If the game feels overwhelming, emergency response simplifies the threat landscape

**Example Timeline (one action per turn):**

```
Turn 3: Deploy Defense succeeds → PHISHING revealed → Uncontained Threats = 1
Turn 4: START → Deduct 5 (uncontained) + 5 (Active Breach Cost, 2 cards still hidden)
        ACTION → Emergency Response on Phishing: pay 15 Budget
        → Phishing removed from play, Uncontained Threats = 0
Turn 5: START → Deduct only 5 (Active Breach Cost; no uncontained threats)
```

---

## Uncontained Threats & Active Breach Cost

These are the core urgency mechanics of Incident Response. **Dwell time costs money—whether you can see the threat or not.**

### How the Uncontained Threats Penalty Works

**Step 1: Threat Revealed**
- When a Threat Card is successfully revealed (by two investigation successes or a full-match defense deployment)
- Add 1 to the Uncontained Threats Tracker
- This threat is now "active" and dangerous

**Step 2: Penalty Applied at Turn Start**
- At the **START of every turn**, deduct **5 Budget per uncontained threat**
- Example: 2 uncontained threats = 10 Budget penalty each turn
- This creates continuous pressure—you MUST contain threats or lose resources

**Step 3: Auto-Mitigation**
- When the **next card in the attack chain is revealed**, the previous uncontained threat is automatically "contained" (represents shift of attention to new priority)
- Uncontained Threats Tracker decreases by 1
- Penalties decrease immediately

**Step 4: Emergency Response Containment**
- Team can use Emergency Response action to **immediately** remove a threat from the board
- Cost: 15 Budget (v2.2)
- Uncontained Threats Tracker decreases by 1

### Active Breach Cost (v2.2)

- At the **START of every turn**, if **at least one chain card remains unrevealed**, deduct **5 Budget**
- This represents the hidden attacker's ongoing damage: data being staged, accounts being abused, systems being backdoored
- It stops only when the **entire chain is revealed** (which is also the victory condition, checked immediately—see below)
- **Why (v2.2):** previously, hidden threats were free and revealed ones were penalized—an inversion that punished discovery. Now dwell time always costs, and revealing cards is how you stop the bleeding.

### Example Walkthrough (v2.2 — recomputed)

```
SETUP: 3-card chain (Phishing → Lateral Movement → Database Exfil)
Budget 100, Turn Limit 7 [(3 × 2) + 1]

Turn 1: START → Active Breach Cost -5 (95). No uncontained threats.
        INVESTIGATE email headers (-5, 90). Roll succeeds.
        → 1st success vs. link 1: clue about the phishing campaign.

Turn 2: START → Active Breach Cost -5 (85).
        INVESTIGATE mail gateway logs (-5, 80). Roll succeeds.
        → 2nd success vs. link 1: ✓ PHISHING CAMPAIGN REVEALED (investigation reveal, v2.2)
        Uncontained Threats = 1. Reward: Budget Grant +10 (90).

Turn 3: START → -5 (uncontained) -5 (Active Breach) = 80.
        INVESTIGATE network logs (-5, 75). Roll succeeds.
        → 1st success vs. link 2: clue about SMB lateral movement.

Turn 4: START → -5 (uncontained) -5 (Active Breach) = 65.
        DEPLOY D-09 Network Segmentation (ADVANCED, -15, 50). Roll succeeds.
        FULL MATCH (NETWORK vector, PIVOT & ESCALATE step)
        → ✓ LATERAL MOVEMENT REVEALED immediately (deploy reveal)
        Phishing auto-mitigates; Lateral Movement now uncontained (still 1 total).
        Reward: Budget Grant +10 (60).

Turn 5: START → -10 (50).
        INVESTIGATE database access logs (-5, 45). Roll fails. No progress.

Turn 6: START → -10 (35).
        INVESTIGATE DLP alerts (-5, 30). Roll succeeds.
        → 1st success vs. link 3: clue about bulk data leaving the database.

Turn 7: START → -10 (20).
        DEPLOY D-11 Data Loss Prevention (ADVANCED, -15, 5). Roll succeeds.
        FULL MATCH (DATA EXFIL vector, C2 & EXFIL step)
        → ✓ DATABASE EXFILTRATION REVEALED — final card!
        Victory is checked IMMEDIATELY (before any start-of-turn penalties).

WIN on the final turn with 5 Budget remaining.
```

*(Arithmetic check, turn by turn: 100 → 95 → 90 | 85 → 80 → +10 = 90 | 80 → 75 | 65 → 50 → +10 = 60 | 50 → 45 | 35 → 30 | 20 → 5.)*

---

## Winning & Losing

### Victory Condition ✓

**Blue Team wins Incident Response if:**
1. ALL threat cards in the attack chain are revealed (face-up on table), AND
2. This happens within the turn limit (7/9/11 by chain length, per [Core Rules §3a](core-rules.md#3a-variable-game-length-system-v21---new))

**Victory is checked immediately when the final card is revealed (v2.2)** — before any start-of-turn penalties would apply. Revealing the last card on your final turn with 0 Budget remaining is still a win.

### Defeat Condition ✗

**Blue Team loses Incident Response if:**
1. Turn Tracker exceeds the turn limit with unrevealed cards remaining, OR
2. The team cannot take any legal action (see Budget Edge Rules below)

**Losing Scenarios:**
- Turns expired with only 2 of 4 cards revealed = attack succeeded
- Budget too low to afford any action = response ran out of resources

### Budget Edge Rules (v2.2)

- **Budget can never go below 0.** If a start-of-turn penalty would take you negative, stop at 0.
- **An action requires its full cost available.** You cannot Investigate with 4 Budget, deploy a 15-Budget defense with 12, or take Emergency Response with 14.
- **Victory is checked immediately** when the final chain card is revealed—before any start-of-turn penalties.
- **Defeat at 0 Budget occurs only if the team cannot take any legal action.** If you have 0 Budget at the start of your turn and every action costs more than you have, the game is lost. (At 5+ Budget you can always still Investigate.)

### Victory Scoring (Optional)

If you want to measure quality of victory:

```
Victory Points Formula:
Points = (Cards Revealed / Total Cards) × 50 + (Budget Remaining / Starting Budget) × 50

Examples:
- 4 of 4 cards revealed, 35 Budget remaining: (4/4 × 50) + (35/100 × 50) = 50 + 17.5 = 67.5/100 (Victory with good efficiency)
- 3 of 4 cards revealed, 15 Budget remaining: (3/4 × 50) + (15/100 × 50) = 37.5 + 7.5 = 45/100 (Partial victory, struggled)
- 2 of 4 cards revealed, 0 Budget: (2/4 × 50) + (0 × 50) = 25/100 (Defeat)
```

---

## Discovery Rewards

When your team **successfully reveals a Threat Card**, immediately **choose ONE of these rewards:**

### Reward Option 1: Intelligence Bonus 📚
- **Effect:** Draw 2 additional Defense Cards immediately (keep both)
- **When to Choose:** If you feel your current hand is weak, or you want more tactical options
- **Strategic Value:** More options = better chance of finding right defense for next threat

### Reward Option 2: Budget Grant 💰
- **Effect:** Gain +10 Budget (v2.2 — reduced from +15 to balance the Active Breach Cost economy)
- **When to Choose:** If you're running low on Budget and want more runway
- **Strategic Value:** Directly extends how long you can keep investigating/defending

### Reward Option 3: Fast-Track Investigation 🚀
- **Effect:** On your **next** Investigate action (only the next one), you succeed on 5+ instead of 11+ (still costs 5 Budget, still need justification modifiers)
- **When to Choose:** If you want a near-guaranteed next investigation success
- **Strategic Value:** Reliable progress toward the next card's clue—or its reveal (v2.2)

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
   - Both are valid; discuss trade-offs (v2.2: investigation reveals need two successes but cost less)

3. **"How did the Uncontained Threats penalty and Active Breach Cost affect your decisions?"**
   - Did they force you to make reactive decisions?
   - Were they realistic representations of incident response and dwell-time costs?

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
   - The Active Breach Cost models why every day of dwell time hurts

---

## Tips for Threat Orchestrators

### Before the Game (Preparation)

1. **Read the module rules completely** - Understand Investigate, Deploy Defense, and Emergency Response mechanics
2. **Prepare your attack chain** - Pre-build or write down your 3-5 hidden cards in sequence
3. **Write clear clues** - For each card, write 2-3 progressive clues that reveal information gradually (v2.2: expect up to two clue deliveries per card before an investigation reveal)
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
- Team reveals all cards in the first half of the turn limit with 60+ Budget remaining
- Multiple consecutive successful rolls (unlikely with d20)
- Clues are too specific/obvious
- Team makes no difficult decisions

**Action:** Make clues more subtle, reduce starting budget next time, or add extra card to chain

**The game is TOO HARD if:**
- Team gets stuck after revealing only 1 card (4+ turns with no progress)
- Multiple consecutive failed rolls
- Team is frustrated rather than challenged
- Team is out of ideas about what to investigate

**Action:** Provide more explicit clues, increase starting budget, reduce chain length

**Adjustment Options:**
- **Chain Length:** 3 (easier) vs. 4 (medium) vs. 5 (harder) — the turn limit scales automatically via (chain × 2) + 1
- **Clue Quality:** More specific/obvious (easier) vs. subtle (harder)
- **Starting Budget:** 80 (harder) vs. 100 (medium) vs. 120 (easier)
- **Turn Limit:** formula −1 (harder) vs. formula (medium) vs. formula +1 (easier)

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
**Turn Limit:** 7 [(3 × 2) + 1]

**Narrative Setup:**
> "Your startup just deployed a new customer database. An employee clicked a malicious link in an email claiming to be from IT. Security monitoring detected unusual PowerShell activity after that. Now you're investigating what happened."

**Focus:** Teaching full kill chain detection (initial → credential harvesting → data theft)
**Expected Duration:** 30 minutes
**Best For:** First-time players, classroom introduction

**Sample Defenses in Starting Hand:**
- D-01: Email Authentication Setup (BASIC, 10)
- D-02: User Security Training (BASIC, 10)
- D-07: Multi-Factor Authentication (ADVANCED, 15)
- D-08: EDR (Endpoint Detection & Response) (ADVANCED, 15)
- D-11: Data Loss Prevention (ADVANCED, 15)

---

### Scenario 2: "Nation-State Campaign" (Intermediate, 4 cards, 40 minutes)

**Attack Chain:**
1. T-02: Watering Hole Attack (INITIAL COMPROMISE - WEB EXPLOIT)
2. T-04: Lateral Movement via SMB (PIVOT & ESCALATE - NETWORK)
3. T-07: Scheduled Task Persistence (PERSISTENCE - MALWARE)
4. T-09: Beaconing to C2 Server (C2 & EXFIL - NETWORK)

**Starting Budget:** 100
**Turn Limit:** 9 [(4 × 2) + 1]

**Narrative Setup:**
> "Your organization's industry-specific website was silently compromised last month. A sophisticated attacker injected malicious code that targeted specific visitor browsers. One of your engineers visited the site and became infected. You're detecting strange network activity but aren't sure what's happening."

**Focus:** Sophisticated attack with multiple detection points; requires multiple defense/investigation attempts
**Expected Duration:** 40 minutes
**Best For:** Experienced players, demonstrating complex kill chain

**Sample Defenses:**
- D-18: Intrusion Prevention System (IPS) (ADVANCED, 15)
- D-09: Network Segmentation (ADVANCED, 15)
- D-04: Network Firewall Rules (BASIC, 10)
- D-08: EDR (Endpoint Detection & Response) (ADVANCED, 15)
- D-13: Threat Hunting Program (ELITE, 25)
- D-14: Memory Forensics (ELITE, 25)

---

### Scenario 3: "Advanced Ransomware Supply Chain" (Advanced, 5 cards, 45 minutes)

**Attack Chain:**
1. T-13: Compromised Software Vendor Update (INITIAL COMPROMISE - MALWARE)
2. T-04: Lateral Movement via SMB (PIVOT & ESCALATE - NETWORK)
3. T-05: Privilege Escalation via Kernel Exploit (PIVOT & ESCALATE - MALWARE)
4. T-09: Beaconing to C2 Server (C2 & EXFIL - NETWORK)
5. T-11: Ransomware Payload Deployment (C2 & EXFIL - MALWARE)

**Starting Budget:** 100
**Turn Limit:** 11 [(5 × 2) + 1]

**Narrative Setup:**
> "A trusted software vendor released an update to your monitoring tools three weeks ago. Today, you're detecting ransomware-like activity across your infrastructure. You suspect the vendor update was compromised. Can you trace the attack chain before the ransomware wakes up?"

**Focus:** Complex supply-chain-initiated attack; requires pattern recognition; high pressure
**Expected Duration:** 45 minutes
**Best For:** Advanced players, demonstrating supply chain risk

**Sample Defenses:**
- D-17: Advanced Malware Sandbox (ELITE, 25) — detonates vendor updates before deployment
- D-08: EDR (Endpoint Detection & Response) (ADVANCED, 15)
- D-09: Network Segmentation (ADVANCED, 15)
- D-03: Windows Update Patching (BASIC, 10) — closes the kernel exploit
- D-14: Memory Forensics (ELITE, 25)
- D-19: Backup & Disaster Recovery (BASIC, 10)
- D-11: Data Loss Prevention (ADVANCED, 15)

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
- Reduce the turn limit by 2 (e.g., a 3-card chain plays in 5 turns instead of 7)
- Optional: Remove Uncontained Threats penalty and Active Breach Cost (less bookkeeping)
- Budget costs stay the same
- Budget starts at 120 to balance speed pressure

**Best For:** Experienced teams wanting high-stakes challenge

---

### Variation 3: Extended Investigation (Advanced)

**Deeper Forensics:**
- Add "Advanced Investigate" action (costs 15 Budget, rolls 11+)
- A successful Advanced Investigate counts as TWO accumulated investigation successes (i.e., it can reveal a link in one action if you already have a clue, v2.2)
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
| **Investigate** | 5 Budget | roll + modifiers ≥ 11 | 1st success: clue; 2nd success on same link: card revealed (v2.2) | No intel gained |
| **Deploy Defense** | 10/15/25 | roll + modifiers ≥ 11 | Full match reveals card immediately | Defense not deployed |
| **Emergency Response** | 15 Budget (v2.2) | None | Threat removed, penalty stops | — |

---

## Quick Reference: Modifiers

| Bonus | When Awarded | Examples |
|-------|--------------|----------|
| **+2** | Strong technical justification | "Analyze mail headers in gateway logs to identify true sender IP, check against threat intelligence" |
| **+1** | Real security tools/techniques | "Query SIEM for scheduled tasks", "Check Mimikatz in memory", "Review EDR telemetry" |
| **+2** | Deployed Defense Persistence (v2.2) | A deployed defense's vector matches the targeted chain link |
| **+0** | Vague/no justification | "Find suspicious activity" |

---

## Quick Reference: Trackers

| Tracker | Starts At | Changes |
|---------|-----------|---------|
| **Budget** | 100 | -5 per Investigate, -10/15/25 per Defense, -15 per Emergency Response, -5 per uncontained threat at turn start, -5 Active Breach Cost at turn start while any chain card is unrevealed (v2.2); floor 0 |
| **Turn** | 1 | +1 each turn (limit = chain × 2 + 1) |
| **Uncontained Threats** | 0 | +1 when card revealed, -1 when auto-mitigated or Emergency Response used |

---

## v2.2 Playtest Edition Changes

Changes for playtesters to validate, and why they were made:

1. **Investigation reveals (accumulating successes).** The first successful Investigation of a chain link yields a clue; a **second** successful Investigation of that same link reveals the card. Deploy Defense full-match still reveals immediately. Previously only defense deployment could reveal cards, contradicting the overview text. **Validate:** does investigation-led play feel viable but slower than defense-led play?
2. **Deployed Defense Persistence.** A deployed defense grants **+2 to Investigate/Deploy rolls** against any chain link matching its vector. Partial/no-match deployments now have lasting value.
3. **Active Breach Cost.** −5 Budget at the start of each turn while at least one chain card is unrevealed. Fixes the inversion where hidden threats were free; teaches that dwell time costs money.
4. **Economy rebalance:** Budget Grant reward reduced +15 → **+10**; Emergency Response repriced 25 → **15** Budget.
5. **Budget edge rules:** Budget floors at 0; actions require full cost; victory is checked immediately on the final reveal (before start-of-turn penalties); defeat at 0 only if no legal action exists.
6. **Turn limits use the Variable Game Length formula** (chain × 2) + 1 → 7/9/11 turns, replacing the fixed 12/10/10 table (see [Core Rules §3a](core-rules.md#3a-variable-game-length-system-v21---new)).
7. **Sequential discovery clarified:** only the earliest unrevealed chain card can be revealed.
8. **Content fixes:** sample-defense lists now cite real card IDs from the canonical 24-card deck (D-01–D-24); D-11 DLP correctly listed as ADVANCED/15.

**Rough balance check (3-card beginner game, 7 turns):** worst-case fixed costs are 5/turn Active Breach + 5/turn for one uncontained threat ≈ 60-70 Budget over a full game, leaving ~30-40 for actions before rewards; two Budget Grants (+20) and cheap Investigates (5) keep an investigation-led run solvent — see the worked example above, which ends at 5 Budget on turn 7.

---

## Need Help?

- **Questions about universal rules?** See [Core Rules](core-rules.md)
- **Want to combine modules?** See [Module Combinations](../module-combinations.md)
- **Understanding modifier stacking?** See [Core Rules: Roll Modifiers](core-rules.md#4-roll-modifiers-universal)
- **How to play Incident Response standalone?** See [Standalone Play Guide](../standalone-games/incident-response.md)

---

*Incident Response Module - Rules & Mechanics*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.2 - Playtest Edition*
