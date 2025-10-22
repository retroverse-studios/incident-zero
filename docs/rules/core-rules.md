# Incident Zero: Cooperative Cybersecurity Game
## REVISED SPECIFICATION (v2.1 - Balanced & Refined)

## Core Concept 🎯

**Incident Zero** is a cooperative (or competitive) cybersecurity game for 2+ players designed for educational environments. One player acts as the **Threat Orchestrator (TO)** (the facilitator), while all other players form one or more **Blue Teams** (the Defenders). 

The game teaches incident response, the cyber kill chain, defense-in-depth strategies, and security decision-making through hands-on gameplay. Players must balance budget constraints, technical knowledge, and strategic thinking to identify and neutralize a hidden cyber attack.

**Game Modes:**
- **Cooperative Mode:** Single Blue Team vs. the attack chain
- **Competitive Mode:** Multiple Blue Teams racing to solve the same attack chain

---

## Game Components

### Threat Cards
Represent the attacker's actions. Each card includes:
- **Title:** e.g., "Phishing Campaign"
- **Attack Chain Step:** `INITIAL COMPROMISE`, `PIVOT & ESCALATE`, `PERSISTENCE`, or `C2 & EXFIL`
- **Attack Vector:** A keyword like `SOCIAL ENGINEERING`, `WEB EXPLOIT`, `CREDENTIAL ABUSE`, `MALWARE`, `NETWORK`, or `DATA EXFIL`
- **Clue:** A short descriptive text for the Threat Orchestrator to read
- **"Why This Works":** Educational text explaining the attack's effectiveness (revealed after discovery)

### Defense Cards
Represent the Defenders' tools and procedures. Each card includes:
- **Title:** e.g., "Analyze Email Headers"
- **Countermeasure:** A keyword that matches an Attack Vector
- **Tier:** BASIC (10 Budget), ADVANCED (15 Budget), or ELITE (25 Budget)
- **Description:** What the defense does

**Examples:**
- **BASIC:** Firewall Rule, Basic Logs Review, Antivirus Scan
- **ADVANCED:** EDR Investigation, SIEM Correlation, Network Traffic Analysis
- **ELITE:** Threat Hunting, Memory Forensics, Deception Technology

### Asset Cards
Simple cards that provide scenario context:
- `EMAIL SERVER`
- `CUSTOMER DATABASE`
- `DOMAIN CONTROLLER`
- `WEB APPLICATION`
- `BACKUP SYSTEM`
- `DEVELOPER WORKSTATION`

### Game Materials
- One 20-sided die (d20)
- **Turn Tracker** (for tracking up to 10 turns in Phase 1)
- **Budget Tracker** and tokens (starting at 100)
- **Discovery Tracker** (for competitive mode)
- **Reputation/Security Score Tracker** (for Phase 2)
- **Uncontained Threats Tracker** (NEW - for tracking active penalties)
- **Pentester Tactic Cards** (NEW - 8 cards for Phase 2)

---

## Phase 1: Incident Response (The Core Game)

This is the standard way to play the game. In competitive mode, multiple teams play simultaneously.

### Setup

1. One player becomes the **Threat Orchestrator (TO)**. All others form Blue Team(s).
2. The TO secretly builds a **3-5 card Attack Chain** by selecting Threat cards in a logical sequence:
   - **Beginner:** 3 cards (e.g., `INITIAL COMPROMISE` → `PERSISTENCE` → `C2 & EXFIL`)
   - **Intermediate:** 4 cards
   - **Advanced:** 5 cards (full kill chain)
3. The TO places relevant **Asset Cards** on the table (visible to all).
4. Each Blue Team receives:
   - Starting **Budget** of 100
   - Hand of 5 **Defense Cards** (drawn randomly)
5. The **Turn Tracker** is set to 1.
6. The **Uncontained Threats Tracker** is set to 0.

**Competitive Mode Setup:**
- Each team has their own Budget and hand
- Teams **cannot share information** about their discoveries
- The TO tracks each team's progress separately using a Discovery Tracker

### Gameplay Loop

#### 1. The Scenario
The TO reads the scenario based **only** on the clue from the first hidden card in the Attack Chain.

**Example:** "Your SIEM alerts show unusual activity. Several employees have reported receiving emails from what appears to be your HR department, but the links seem suspicious. One user clicked the link before IT could respond."

#### 2. The Blue Team's Turn

The team discusses their strategy (2-3 minutes recommended) and must choose **ONE** action:

---

#### **Action A: Investigate 🔎**

**Cost:** 5 Budget

**Action:** The team describes what they are investigating and **provides technical justification** for their approach.

**Roll Modifiers:**
- **Base requirement:** Roll 11+ on d20
- **+2 bonus:** Strong technical justification (references specific logs, tools, or investigative methodology)
- **+1 bonus:** References real security tools/techniques (Wireshark, Splunk queries, specific CVEs, MITRE ATT&CK)

**Examples of good justification:**
- "We want to analyze the email headers in our mail gateway logs to identify the sender's true IP and check it against threat intelligence feeds"
- "We'll query our EDR for any processes spawned after the user clicked the link, looking for PowerShell or suspicious child processes"

**Outcome:**
- **Success (Modified roll 11+):** The TO gives a **verbal clue** about the *next* hidden threat in the chain
- **Failure:** The TO says "Your investigation yields no actionable intelligence" (turn wasted, but team learned something)

---

#### **Action B: Deploy a Defense 🛡️**

**Cost:** Depends on card tier (10, 15, or 25 Budget)

**Action:** The team plays a **Defense Card** on a specific Asset and **explains why they chose this defense**.

**Roll Modifiers:** Same as Investigate action (+2 for justification, +1 for specific tool/technique references)

**Outcome:**
- **Success (Modified roll 11+):** 
  - If the played card's `Countermeasure` keyword **matches** the hidden card's `Attack Vector` AND it's the correct step in the chain → **The Threat card is REVEALED!**
  - If it matches but wrong step, or right step but wrong vector → Defense is deployed but no reveal (still useful for Phase 2)
  - If neither matches → Defense is deployed but ineffective against current threat
- **Failure:** Budget spent, but defense is not properly implemented (card is discarded)

---

#### **Action C: Emergency Response 🚨** *(Revised)*

**Cost:** 25 Budget

**Action:** The team describes their containment strategy for a **previously revealed** Threat card. The team must explain the containment methodology (quarantine, lateral movement prevention, data protection, etc.).

**Effect:** Remove one already-revealed Threat card from play AND immediately reduce **Uncontained Threats by 1** (see below for penalty mechanics).

**Educational Purpose:** Teaches incident triage, containment procedures, and the cost-benefit of reactive vs. proactive security. The expense forces teams to prioritize which threats to contain.

**When to use:** 
- If a team is running out of time/budget, they might need to contain what they've found rather than chase the full chain
- To prevent budget drain from active uncontained threats (see penalty mechanics below)
- When defending critical assets

---

#### **3. Uncontained Threats Penalty** *(NEW MECHANIC)*

**At the START of each turn**, for every **revealed but uncontained** threat still in play:
- **Deduct 5 Budget** from the Blue Team's total

**How Uncontained Threats are tracked:**
1. When a threat is **revealed**, it becomes an "Uncontained Threat" (add 1 to the counter)
2. When **Emergency Response** is used, remove that threat and decrement the counter
3. When the **next card in the chain is revealed**, the previous uncontained threat is automatically considered "mitigated" (decrement the counter)

**Example Flow:**
- Turn 1: Team reveals "Phishing Campaign" → Uncontained Threats = 1
- Turn 2: Team starts turn. Budget drain: -5 Budget. Team chooses to Investigate, fails.
- Turn 3: Team has only spent 30 Budget so far. They could use Emergency Response (-25) to contain the phishing threat, eliminating the -5/turn drain. Or they could keep investigating the next card, accepting the drain.
- Turn 4: If they never contained the phishing threat, another -5 Budget drain occurs.

**Strategic Depth:** This mechanic creates a meaningful choice:
- **Spend 25 Budget now** (Emergency Response) to eliminate a single 5/turn drain
- **Accept the drain** and use remaining budget to investigate new threats
- **Try to progress quickly** through the chain to automatically mitigate old threats

---

#### 4. End of Turn

- Turn Tracker advances by one
- Each Blue Team draws **1 Defense Card**
- In **competitive mode**, the TO updates each team's Discovery Tracker privately
- **Uncontained Threats Penalty** is applied at the START of the next turn (not immediately)

---

### Discovery Rewards (Competitive & Cooperative)

When a Blue Team **successfully reveals** a Threat card in the Attack Chain:

**Immediate Reward (Choose ONE):**
1. **Intelligence Bonus:** Draw 2 Defense Cards (keep both)
2. **Budget Grant:** Gain +15 Budget (represents management approval)
3. **Fast-Track:** On your next Investigate action, you succeed on a roll of **5+ instead of 11+** (you still must pay the 5 Budget cost and provide justification; you get a modified roll based on your justification quality). 

**Rationale for Fast-Track Change:** This keeps the reward powerful but not game-breaking. Teams still need to use their next turn thoughtfully—they get a better chance but not a guaranteed win. They could still fail if they roll poorly (5-6 on d20 is risky with bad justification).

**Competitive Mode - First Discovery Bonus:**
- The **first team** to reveal each specific card in the chain gets an **additional +10 Budget**
- Other teams can still discover the same card later for the standard reward
- This simulates the "intelligence sharing" advantage of being first to detect a threat

**Information Sharing in Competitive Mode:**
- Teams do **NOT** automatically know what others have discovered
- However, after **any team** reveals a card, the TO may optionally announce: "A detection has been made in the industry - you may purchase this intelligence"
- Cost: 20 Budget to learn what card was revealed (you don't automatically solve it, but you know what to look for)

---

### Winning and Losing Phase 1

**Blue Team Wins:** 
- They successfully reveal **all** hidden Threat cards in the Attack Chain
- In competitive mode: First team to reveal all cards wins, OR team with most cards revealed when time expires

**Blue Team Loses:** 
- Turn Tracker reaches 10, OR
- Budget reaches 0 (including Uncontained Threats penalties)

**Competitive Tiebreaker:** If multiple teams finish on the same turn, the team with the **most Budget remaining** wins.

---

### Post-Phase 1: Lessons Learned Debrief

**Mandatory 5-minute structured debrief** (even if they lost):

The TO facilitates discussion of these questions:
1. What was the attacker's initial access vector?
2. What defense should have been deployed first?
3. Did Uncontained Threats penalties force you to make reactive decisions? Was that realistic?
4. What would you do differently if you replayed this scenario?

---

## Phase 2: Security Hardening (Optional Advanced Play)

After Phase 1 ends (win or lose), teams can continue to Phase 2 for 20-30 additional minutes of gameplay. This teaches **defense-in-depth** and proactive security.

### Phase 2 Setup

1. Clear the board of all Threat cards (revealed or hidden)
2. Each Blue Team's remaining **Budget carries over** to Phase 2 (minimum 20 Budget if they ended Phase 1 with less)
3. Each team **keeps** all Defense Cards they deployed in Phase 1 (these represent permanent security improvements)
4. Each team is dealt **5 new Defense Cards**
5. Create a **Security Score** tracker starting at 0
6. **Shuffle Pentester Tactic Cards** and place the deck face-down near the TO (NEW)

### Phase 2 Objective

Teams are now **protecting against a future attack** by the same threat actor. They must:
1. Deploy additional defenses from their hand
2. Strengthen deployed defenses using **Hardening Actions**
3. Prepare for the Pentester to test their resilience

### Phase 2 Gameplay

Each turn in Phase 2 (5-7 turns maximum), a Blue Team can choose:

#### **Hardening Action 1: Deploy a New Defense**

Same as Phase 1, but with no roll needed—if you pay the Budget, the defense is automatically deployed. No technical justification required (though the TO may ask for it for educational value).

#### **Hardening Action 2: Harden an Existing Defense**

**Cost:** 5 Budget per hardening

**Action:** Choose a Defense Card already deployed in Phase 1 or Phase 2. Spend 5 Budget to improve it:
- Add +2 to the defense's "blocking power" (tracked on a note card next to the defense)
- This defense will be more effective when tested by the Pentester

**Example:**
- "We're hardening our EDR deployment by tuning behavioral analytics and adding threat intelligence integration" → +2 bonus

#### **Hardening Action 3: Prepare an Incident Response Playbook**

**Cost:** 10 Budget per playbook

**Action:** Create a custom playbook for a specific attack scenario. Write a 1-2 sentence description. When the Pentester attacks using that vector, your team gets a one-time **+3 bonus** to your defense roll.

**Example Playbooks:**
- "Ransomware Outbreak Response" - Automatic backup isolation and network segmentation
- "Credential Compromise Incident" - Forced MFA re-authentication and access token revocation
- "Supply Chain Attack Detection" - Monitoring for unusual DNS and C2 beaconing patterns

---

### Phase 2 Pentester Challenge *(NEW MECHANIC - Refined)*

After teams finish deploying and hardening defenses, the TO draws **Pentester Tactic Cards** to conduct simulated attacks.

#### Pentester Tactic Cards (8 Total)

Each card describes a specific attack the TO can execute against the Blue Team's hardened defenses. The TO draws **1 card per turn** (up to 3-4 cards total).

**Card Examples:**

##### Tactic 1: "Bypass Basic Defenses"
```
PENTESTER TACTIC: BYPASS BASIC DEFENSES
Effect: Choose one BASIC-tier (10 Budget) defense that the Blue Team 
deployed. That defense is treated as if it wasn't there for this attack.

Strategic Impact: Forces teams to layer defenses, not just deploy 
cheap tools. Teams must invest in stronger controls.
```

##### Tactic 2: "Social Engineering Specialist"
```
PENTESTER TACTIC: SOCIAL ENGINEERING SPECIALIST
Effect: The next attack targeting a SOCIAL ENGINEERING vector gains 
+2 to the Blue Team's defense roll difficulty (they must roll higher 
to stop it).

Strategic Impact: Reminds teams that user training must be ongoing; 
one-time training is not enough.
```

##### Tactic 3: "Persistence Expert"
```
PENTESTER TACTIC: PERSISTENCE EXPERT
Effect: If the Pentester successfully lands a PERSISTENCE attack, 
create a hidden persistent threat card. Blue Team must spend 15 Budget 
to remediate it (instead of normal Emergency Response cost).

Strategic Impact: Teaches the cost of advanced persistent threats and 
why detection speed matters.
```

##### Tactic 4: "Supply Chain Attack"
```
PENTESTER TACTIC: SUPPLY CHAIN ATTACK
Effect: Choose one Defense Card deployed by the Blue Team. That 
defense is temporarily compromised and cannot be used this turn.

Strategic Impact: Highlights risk from third-party dependencies and 
the importance of vendor security assessments.
```

##### Tactic 5: "Detection Evasion"
```
PENTESTER TACTIC: DETECTION EVASION
Effect: The next attack targeting a MALWARE vector bypasses the Blue 
Team's SIEM and EDR for this turn (they don't get these bonuses).

Strategic Impact: Teaches that advanced attackers can evade even good 
defenses; defense-in-depth and layering are essential.
```

##### Tactic 6: "Budget Drain - Incident Response Overload"
```
PENTESTER TACTIC: BUDGET DRAIN - INCIDENT RESPONSE OVERLOAD
Effect: Blue Team's next Defense deployment costs +10 Budget (overhead 
from managing the "attack").

Strategic Impact: Reminds teams that incident response is expensive; 
prevention is cheaper than response.
```

##### Tactic 7: "Zero-Day Exploit"
```
PENTESTER TACTIC: ZERO-DAY EXPLOIT
Effect: For this attack, Blue Team's roll difficulty increases by 3 
(they need a 14+ instead of 11+). They cannot use playbooks for this 
attack.

Strategic Impact: Emphasizes that no defense is perfect; teams must 
assume breach and have detection/response plans.
```

##### Tactic 8: "Multi-Vector Attack"
```
PENTESTER TACTIC: MULTI-VECTOR ATTACK
Effect: The Pentester attacks two different vectors simultaneously. 
Blue Team must defend against both or loses +10 Reputation on one.

Strategic Impact: Teaches that coordinated attacks are harder to defend 
against; teams need holistic, layered strategies.
```

---

#### Phase 2 Attack Resolution

When the Pentester draws a tactic card and launches an attack:

1. **TO describes the attack scenario** (e.g., "Attacker sends a phishing email with a malicious PDF")
2. **Tactic Card effects apply** (e.g., "Bypass Basic Defenses" disables their cheap antivirus)
3. **Blue Team chooses a defense** to deploy against the attack
4. **Roll with modifiers:**
   - Base: 11+ (same as Phase 1)
   - Apply Tactic Card penalties
   - Apply Hardening bonuses
   - Apply Playbook bonuses (if applicable)
5. **Outcome:**
   - **Success:** No reputation loss, defense holds
   - **Failure:** -10 Reputation (represents a breach or incident)

---

### Phase 2 Scoring

**Final Security Score = (Defenses Deployed × 5) + (Hardening Upgrades × 2) + (Playbooks Created × 10) - (Reputation Lost)**

**Suggested Scoring Tiers:**
- **100+:** Exceptional security posture (enterprise-grade)
- **70-99:** Strong defense-in-depth (mid-market)
- **40-69:** Basic protection (startup/cost-constrained)
- **Below 40:** Vulnerable to advanced attacks

---

### Phase 2 Win/Loss

**Blue Team Wins Phase 2:** 
- Final Security Score ≥ 70 AND Budget remaining ≥ 10
- They successfully built layered defenses within budget constraints

**Blue Team Loses Phase 2:**
- Final Security Score < 40 OR they ran out of Budget before completing hardening
- Their defenses were inadequate or they couldn't afford comprehensive protection

---

## Difficulty Scenarios

### 1. Startup: "Lean Security"
- **Starting Budget:** 80
- **Attack Chain:** 3 cards
- **Turn Limit:** 12 (generous for learning)
- **Learning Focus:** Basic incident response, resource prioritization

### 2. Mid-Market: "Balanced Response"
- **Starting Budget:** 100 (standard)
- **Attack Chain:** 4 cards
- **Turn Limit:** 10 (standard)
- **Learning Focus:** Defense-in-depth, investigation vs. defense trade-offs

### 3. Enterprise: "Advanced Threats"
- **Starting Budget:** 120
- **Attack Chain:** 5 cards (full kill chain)
- **Turn Limit:** 10
- **Special Rule:** Uncontained Threats penalties are doubled (-10 per turn instead of -5)
- **Learning Focus:** Managing complex incident response, prioritization under extreme pressure

### 4. Budget-Constrained: "Maximum Efficiency"
- **Starting Budget:** 60
- **Attack Chain:** 4 cards
- **Special Rule:** Defense cards cost -5 Budget (agile deployment)
- **Win Condition:** Only need to reveal 3 cards (shorter chain)
- **Learning Focus:** Risk prioritization, security on a budget

### 5. Advanced Persistent Threat (APT)
- **Starting Budget:** 100
- **Attack Chain:** 5 cards (full kill chain)
- **Special Rule:** Failed investigations give the TO a "Intelligence Gathering" token (TO gets bonus info about Blue Team's strategy)
- **Learning Focus:** Nation-state tactics, long-term persistence

---

## Educational Objectives by Game Element

| Game Mechanic | Learning Objective |
|---------------|-------------------|
| Attack Chain sequence | Understanding the cyber kill chain |
| Budget constraints | Resource allocation and risk management |
| Justification bonuses | Articulating technical decisions |
| Defense tiers | Cost-benefit analysis of security tools |
| Investigation actions | Log analysis and threat hunting methodology |
| Emergency Response | Incident containment and triage |
| **Uncontained Threats Penalties** | **Cost of delayed response; why dwell time matters** |
| Phase 2 Hardening | Defense-in-depth and proactive security |
| **Pentester Tactics** | **Attacker capabilities; sophisticated evasion techniques** |
| Lessons Learned debrief | Critical thinking and post-incident analysis |
| Scenario variety | Context-specific security considerations |

---

## Recommended Play Structure for Classroom

### First Playthrough (60 minutes)
- **Setup & Rules:** 10 minutes
- **Phase 1:** 25-30 minutes (use 3-card chain, Startup scenario)
- **Lessons Learned:** 10 minutes
- **Discussion:** 10 minutes

### Advanced Session (90 minutes)
- **Setup:** 5 minutes
- **Phase 1:** 30-35 minutes (4-card chain)
- **Lessons Learned:** 10 minutes
- **Phase 2:** 30 minutes (with Pentester Tactics)
- **Final Debrief:** 10 minutes

### Competitive Tournament (2 hours)
- **Setup:** 10 minutes
- **Phase 1 (all teams):** 40 minutes
- **Brief Break:** 5 minutes
- **Phase 2 (finalists):** 35 minutes (optional)
- **Awards & Debrief:** 30 minutes

---

## Tips for the Threat Orchestrator

### Creating Effective Attack Chains

**Good chains tell a story:**
1. Start with realistic initial compromise (phishing, web exploit, stolen creds)
2. Show logical progression (reconnaissance → access → escalation)
3. End with attacker objective (data theft, ransomware, persistence)

**Example Chain (Intermediate):**
1. **Phishing Campaign** (Initial Compromise) → `SOCIAL ENGINEERING`
2. **Credential Harvesting** (Pivot & Escalate) → `CREDENTIAL ABUSE`
3. **Lateral Movement** (Pivot & Escalate) → `NETWORK`
4. **Data Exfiltration** (C2 & Exfil) → `DATA EXFIL`

### Giving Good Clues

**After successful Investigation rolls:**
- **Too vague:** "You find something suspicious"
- **Too specific:** "The attacker used Mimikatz to dump credentials from LSASS"
- **Just right:** "Your memory forensics shows a credential-dumping tool was executed with admin privileges on the Domain Controller"

**Progressive disclosure:** Each clue should narrow down the next card without giving it away completely.

### Using Pentester Tactic Cards Effectively

**When to draw a tactic:**
- After the Blue Team has deployed significant defenses in Phase 2
- When the team seems over-confident ("We have EDR and MFA, we're unhackable")
- To force teams to think about *combinations* of attacks

**Drawing strategy:**
- **Turn 1-2:** Use softer tactics (Bypass Basic Defenses, Social Engineering Specialist) to teach layering
- **Turn 3+:** Use harder tactics (Zero-Day Exploit, Multi-Vector Attack) to remind teams nothing is perfect

**Narrative approach:** Always frame the tactic card as a specific, realistic attack scenario:
- "The attacker has just released a zero-day exploit targeting your unpatched systems..."
- "The threat actor has launched a coordinated multi-vector attack combining phishing, watering hole, and supply chain compromise..."

### Balancing Difficulty

- **Too easy:** Teams solving chain in 4-5 turns with budget to spare
- **Too hard:** Teams hitting turn 10 with only 1 card revealed
- **Just right:** Teams revealing final card on turns 7-9 with 20-40 Budget remaining, and 1-2 Uncontained Threats penalties applied during the game

**Adjust by:**
- Number of cards in chain (3-5)
- Quality of clues (more/less specific)
- Starting Budget (60-120)
- Turn limit (8-12)
- Pentester Tactic intensity in Phase 2

---

## Sample Attack Chain with Full Details

### Scenario: "The Insider Threat"

**Context:** Medium-sized tech company, 200 employees, SaaS product

**Asset Cards in Play:**
- Employee Workstation
- Code Repository
- Production Database
- Customer Portal
- Backup System

---

#### Card 1: Compromised Credentials
- **Step:** INITIAL COMPROMISE
- **Vector:** CREDENTIAL ABUSE
- **Clue:** "Your SIEM shows a successful VPN login from an unusual geographic location at 2 AM. The username belongs to a developer who's currently on vacation. The login came from an IP address in Eastern Europe."
- **Why This Works:** "Credential stuffing attacks exploit password reuse. If this developer used the same password on a breached website, attackers could have purchased their credentials on the dark web. MFA would have prevented this."

---

#### Card 2: Lateral Movement
- **Step:** PIVOT & ESCALATE
- **Vector:** NETWORK
- **Clue:** "The compromised account accessed the internal code repository and made several git clone requests. Network logs show unusual SMB traffic between the developer workstation and a production server."
- **Why This Works:** "Once inside the network, attackers perform reconnaissance and move laterally using legitimate protocols like SMB. Many organizations have flat network architecture with insufficient segmentation, allowing easy movement."

---

#### Card 3: Privilege Escalation
- **Step:** PIVOT & ESCALATE
- **Vector:** MALWARE
- **Clue:** "A scheduled task was created on the production server under a service account. This task executes a PowerShell script that attempts to access the database server with elevated credentials."
- **Why This Works:** "Attackers use living-off-the-land techniques with built-in Windows tools like PowerShell and scheduled tasks to avoid detection. Service accounts are often over-privileged and poorly monitored."

---

#### Card 4: Data Exfiltration
- **Step:** C2 & EXFIL
- **Vector:** DATA EXFIL
- **Clue:** "Your data loss prevention system flagged unusual outbound HTTPS traffic. The production database logs show a large SELECT query was executed, and the results were written to a temp file. This file was then transferred to an external cloud storage service."
- **Why This Works:** "Attackers often exfiltrate data over encrypted channels (HTTPS) to common cloud services (Dropbox, Google Drive) that appear legitimate. Without DLP and egress filtering, this traffic blends in with normal business activity."

---

## Quick Reference: Action Summary

| Action | Cost | Roll Needed | Effect |
|--------|------|-------------|--------|
| Investigate | 5 | 11+ (base) | Get clue about next card |
| Deploy Defense | 10/15/25 | 11+ (base) | Reveal card if match |
| Emergency Response | 25 | None | Remove revealed threat; eliminate 1 Uncontained Threat |
| Draw Card (Hardening) | 5 | None | Add card to hand |
| Harden Defense (Phase 2) | 5 | None | +2 bonus to defense |
| Prepare Playbook (Phase 2) | 10 | None | +3 bonus for specific vector |

**Roll Bonuses:**
- +2: Strong technical justification
- +1: References real tools/techniques

**Phase 1 Penalties:**
- -5 Budget per Uncontained Threat at start of each turn

---

## Variants and Extensions

### Solo Mode
- Use a simplified 3-card chain
- Player has 12 turns instead of 10
- All Defense deployments automatically succeed (no roll)
- Focus: Learning the mechanics and attack patterns

### Team vs. Team
- Two teams: One plays Red Team (builds attack), other plays Blue Team (defends)
- Swap roles after each round
- Score based on: Cards revealed, Budget remaining, turns taken

### Campaign Mode
- Play 3 scenarios back-to-back
- Budget carries over between scenarios (but resets to minimum 60)
- Unlock "Advanced Defense Cards" after completing scenarios
- Final scenario: APT with 5-card chain and enhanced Pentester Tactics

### Hardcore Mode
- **Uncontained Threats penalties double** to -10 Budget per turn
- **Pentester Tactics are drawn in Phase 1** (teams must defend AND harden simultaneously)
- Teams must decide: reveal cards or prepare defenses?
- **Learning Focus:** Balancing reactive vs. proactive security under extreme constraints

---

## Conclusion

**Incident Zero** provides a hands-on, engaging way to teach cybersecurity concepts through gameplay. The combination of cooperative decision-making, resource management, and technical justification creates multiple learning opportunities.

**Key Pedagogical Strengths:**
- Forces students to articulate "why" not just "what"
- Simulates real-world resource constraints
- Teaches both reactive (incident response) and proactive (hardening) security
- **Uncontained Threats penalties create urgency and model real-world incident costs**
- **Pentester Tactics teach attacker sophistication and why defense-in-depth matters**
- **Balanced Fast-Track keeps rewards powerful but not game-breaking**
- Scalable difficulty for different skill levels
- Natural debriefing moments that reinforce learning

**Remember:** The goal isn't to win—it's to think like a security professional. Every decision should have a reason, and every failure is a learning opportunity.

---

*Version 2.1 - Balanced & Refined Edition*  
*Updated with: Uncontained Threats penalty mechanics, balanced Fast-Track reward, and Pentester Tactic Cards*  
*For questions or additional scenario packs, contact: [your contact info]*