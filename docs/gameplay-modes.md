# Incident Zero: Game Modes & Play Variants
## Three Mini-Games, Two Full Campaigns, Flexible Play Options

---

## Overview: Flexible Game Architecture

**Incident Zero** can now be played in **6 different configurations**:

### Three Standalone Mini-Games (30-45 minutes each)
1. **Phase 1: Incident Response** - Pure attack detection & investigation
2. **Phase 2: Hardening** - Pure defensive layering & security planning
3. **Phase 2: Disaster Recovery** - Pure crisis management & response

### Two Full-Length Campaigns (90-120 minutes each)
4. **Campaign A: Detect & Defend** - Phase 1 (Win) → Phase 2 Hardening
5. **Campaign B: Attack & Recover** - Phase 1 (Lose) → Phase 2 Disaster Recovery

### Mixed Options (60-75 minutes)
6. **Quick Campaign** - Any mini-game + any Phase 2 variant (skips full Phase 1)

This document explains how to set up and run each configuration.

---

# STANDALONE MINI-GAMES

---

## Mini-Game 1: Phase 1 - Incident Response (30-45 minutes)

### Purpose
Players practice **attack detection, investigation, and incident response** in a race against the clock.

**Best For:**
- Introduction to the game
- Teaching incident response basics
- Quick classroom sessions
- Team competitions

### Setup (5 minutes)

**1. Select Difficulty:**
- **Beginner:** 3-card chain, 100 Budget, 12 turns (generous)
- **Intermediate:** 4-card chain, 100 Budget, 10 turns (standard)
- **Advanced:** 5-card chain, 100 Budget, 10 turns (challenging)

**2. Threat Orchestrator Builds Chain:**
- Select 3-5 threat cards in logical sequence
- Write down clues for each hidden card
- Place relevant Asset Cards on table

**3. Blue Team Setup:**
- Receive 100 Budget
- Draw 5 Defense Cards (random)
- Place Turn Tracker at 1
- Place Uncontained Threats Tracker at 0

**4. TO Reads Opening Scenario:**
"Your security team is monitoring the network today when alerts begin firing. Here's what you're seeing..."

### Gameplay (25-35 minutes)

Standard Phase 1 loop:
- **Turn:** 2-3 minutes of discussion
- **Action:** Investigate, Deploy Defense, or Emergency Response
- **Roll:** 1d20 + modifiers
- **Result:** Clue, reveal, or nothing
- **End Turn:** Advance tracker, draw card, apply penalties

### Winning Mini-Game 1

**Win Condition:** Reveal all threat cards before:
- Turn Tracker reaches 10, OR
- Budget reaches 0

**Score:**
- **Turns Used:** Lower is better (fast detection = less damage)
- **Budget Remaining:** Higher is better (efficient investigation)
- **Cards Revealed:** Should be 100% if you win

**Scoring Example:**
```
Beginner (3-card chain):
- Revealed all 3 cards on turn 7: 7 points
- Budget remaining: 45: +4 points
- Total: 11 points (out of 12 possible)
- Result: Good detection, some wasted budget

Intermediate (4-card chain):
- Revealed 3 of 4 cards by turn 10: 3 points
- Budget remaining: 0: +0 points
- Total: 3 points
- Result: LOST - Ran out of budget before full chain reveal
```

### Debrief (5-10 minutes)

**For Winners:**
1. "What was your investigation strategy?"
2. "Which action type (Investigate vs. Deploy Defense) was most effective?"
3. "Did Uncontained Threats penalties change your decisions?"

**For Losers:**
1. "What went wrong in your investigation?"
2. "Would you have benefited from more defensive deployments?"
3. "How would you investigate differently next time?"

**Everyone:**
1. "What was the attacker's kill chain?"
2. "Why isn't this easy to detect in real life?"

---

## Mini-Game 2: Phase 2 - Hardening (30-45 minutes)

### Purpose
Players practice **security layering, defense-in-depth, and proactive hardening** in a controlled environment.

**Best For:**
- Teaching security architecture
- Building defensive capabilities
- Strategic planning exercises
- "What if we had unlimited time to harden?" scenarios

### Setup (5 minutes)

**1. Assume Successful Detection:**
Threat Orchestrator describes a hypothetical attack:

"Imagine your team successfully detected this attack chain during Phase 1:
1. Phishing campaign (SOCIAL ENGINEERING) - compromised user account
2. Lateral movement via SMB (NETWORK) - access to file server
3. Privilege escalation with PowerShell (MALWARE) - domain admin creds
4. Data exfiltration via cloud storage (DATA EXFIL) - customer database copied

Your team stopped it after card 2 (lateral movement). Now you have time to build defenses to prevent this from ever happening again."

**2. Set Hardening Budget:**
- **Standard:** 150 Budget (more than Phase 1, represents planning time)
- **Generous:** 200 Budget (unlimited planning scenario)
- **Constrained:** 100 Budget (limited resources)

**3. Blue Team Receives:**
- 5 starting Defense Cards (random)
- Scenario-specific Asset Cards on table
- Hardening/Enhancement tokens for tracking upgrades

**4. Optional: Pentester Tactic Deck Ready**
- Shuffle 3-4 Pentester Tactic Cards (TO will draw these)
- TO will test defenses mid-game

### Gameplay (20-35 minutes)

**Turn Structure (5-7 turns, 3-4 minutes per turn):**

Each turn, team chooses ONE:

#### **Action 1: Deploy New Defense**
- **Cost:** 10/15/25 Budget (by tier)
- **Effect:** Defense is automatically deployed (no roll needed)
- **Explanation:** "Why are we deploying this defense?"

#### **Action 2: Harden Existing Defense**
- **Cost:** 5 Budget per upgrade
- **Effect:** +2 bonus to defense effectiveness
- **Cumulative:** Can upgrade same defense multiple times

#### **Action 3: Create Incident Response Playbook**
- **Cost:** 10 Budget per playbook
- **Effect:** +3 bonus when responding to specific threat vector
- **Planning:** Teams write 1-2 sentence scenario

#### **Action 4: Test & Drill**
- **Cost:** 0 Budget (represents time, not money)
- **Effect:** Roll for simulated attack; if successful (roll 11+), defense holds
- **Purpose:** Validate that defenses actually work

### Mid-Game: Pentester Challenge (Turn 3-4)

After team deploys initial defenses, TO draws a Pentester Tactic Card:

"Your simulated red team just attempted an attack using technique: **'Detection Evasion'**"

Team chooses a deployed defense to counter. Roll (11+ to defend):
- **Success:** Defense held; continue
- **Failure:** Tactic succeeded; -5 points to final score (represents a successful attack)

Team can deploy additional defenses or upgrade existing ones to prepare for next tactic.

### Winning Mini-Game 2

**Score Calculation:**
```
Defenses Deployed: Count × 5 points each
Hardening Upgrades: Count × 2 points each
Playbooks Created: Count × 10 points each
Pentester Tactics Defended: Count × 3 points each
Budget Efficiency: (Budget Remaining / Starting Budget) × 10

Example (150 starting budget):
- 6 defenses deployed: 30 points
- 5 hardening upgrades: 10 points
- 2 playbooks created: 20 points
- 4 of 4 pentester tactics defended: 12 points
- 20 budget remaining: 1.3 points
Total Score: 73 points (out of ~100)
Result: Strong defense-in-depth
```

**Scoring Tiers:**
- **85+:** Exceptional security posture (enterprise-grade)
- **65-84:** Strong layered defenses (mid-market ready)
- **45-64:** Adequate protection (startup level)
- **Below 45:** Vulnerable to sophisticated attacks

### Debrief (5-10 minutes)

1. **Defense Strategy:**
   - "How did you prioritize which defenses to deploy first?"
   - "What layers do you think are most important?"

2. **Budget Management:**
   - "Did you run out of budget? Would more budget have helped?"
   - "Which defenses provided the best value?"

3. **Pentester Results:**
   - "Which tactics surprised you?"
   - "How would you harden further against them?"

4. **Real-World Application:**
   - "If you had to defend your actual organization, what would you deploy?"
   - "Why is this hard even with unlimited budget?"

---

## Mini-Game 3: Phase 2 - Disaster Recovery (30-45 minutes)

### Purpose
Players practice **crisis management, forensics, and stakeholder communication** during a real breach.

**Best For:**
- Teaching incident response procedures
- Crisis management training
- Understanding breach consequences
- Practicing under pressure

### Setup (5 minutes)

**1. Present Crisis Scenario:**

Threat Orchestrator reveals a full attack chain that succeeded:

"Your organization has experienced a significant breach. Here's what happened:

**Attack Chain (now fully revealed):**
1. Phishing Email → Employee clicked malicious link
2. Credential Harvesting → Login credentials captured
3. VPN Access → Attacker gained network access
4. Lateral Movement → Access to production servers
5. Database Exfiltration → 500,000 customer records stolen

**Current Status:**
- Breach discovered 24 hours ago (late discovery)
- Customer database is compromised
- Attacker is demanding $1M ransom
- No public disclosure yet (but attacker claims to have media contacts)
- Your organization has 48 hours to decide on payment/negotiation

**Your Challenge:**
Manage the crisis, investigate the breach, communicate with stakeholders, and minimize damage."

**2. Set Crisis Budget:**
- **Standard:** 50 (emergency crisis fund)
- **Plus:** Remaining Phase 1 budget (if this transitions from failed Phase 1)
- **Total:** Usually 50-80 Budget

**3. Initialize Tracking:**
- **Reputation Tracker:** Starts at 100
- **Financial Impact Sheet:** Track all costs
- **Stakeholder Log:** Track who was notified and when
- **Turn Tracker:** Set to 1 (represents hours/days)

**4. Place Crisis Timeline on Table:**
- Turn 1 (6h): Internal discovery & legal notification
- Turn 2 (12h): Regulatory notification deadline
- Turn 3 (18h): Customer notification deadline begins
- Turn 4 (24h): Media discovers breach (external pressure)
- Turn 5 (30h): Ransom deadline (attacker threat)
- Turn 6 (36h): First lawsuits filed
- Turn 7 (48h): Crisis period ends

### Gameplay (20-35 minutes)

**Turn Structure (7 turns maximum, 3-4 minutes per turn):**

Each turn, team chooses ONE Crisis Response Action:

#### **Action 1: Forensic Investigation**
- **Cost:** 5-15 Budget (by scope)
- **Roll:** 11+ to succeed (identify scope and timeline)
- **Result:** Gain information for stakeholder communication

#### **Action 2: Stakeholder Communication**
- **Cost:** 0-10 Budget (depending on scope)
- **Options:** Customers, regulators, media, legal, insurance
- **Reputation:** +5 (transparent), 0 (adequate), -2 to -20 (poor)
- **Late Penalties:** -10 per day after regulatory deadline

#### **Action 3: Evidence Preservation**
- **Cost:** 5-20 Budget
- **Effect:** Secure forensic evidence, prevent data loss, establish chain of custody
- **Importance:** Required for legal proceedings and investigation

#### **Action 4: Remediation & Hardening**
- **Cost:** 10-25 Budget
- **Effect:** Remove attacker access, patch vulnerabilities, reset credentials
- **Outcome:** Prevents re-compromise

#### **Action 5: Ransom Decision**
- **Options:**
  - **Pay:** Spend ransom amount (10-30% of budget), -15 reputation, no guarantee
  - **Negotiate:** Spend 5 Budget, roll 10+ to reduce demand
  - **Refuse:** Spend 0, +5 reputation, but attacker publishes data

### Crisis Timeline & Pressure

**Key Moments:**
- **Turn 3 (18h):** Customer notification deadline appears
- **Turn 4 (24h):** Media discovers breach; public awareness rises; pressure increases
- **Turn 5 (30h):** Ransom deadline; must make payment decision
- **Turn 7 (48h):** Crisis period ends; team must complete all actions by this point

### Winning Mini-Game 3

**Final Reputation Score:**
- **Starting:** 100
- **Gains:** Transparent communication (+5), successful investigation (+3), quick remediation (+3)
- **Losses:** Late notification (-10/day), poor communication (-20), ransom payment (-15), failed investigation (-5)

**Score Calculation:**
```
Forensic Investigation Quality: 0-25 points
Stakeholder Communication: 0-20 points
Evidence Preservation: 0-15 points
Remediation Effectiveness: 0-20 points
Financial Management: 0-15 points (Budget efficiency)
Final Reputation Score (90-100): 5 bonus points

Example:
- Thorough investigation: 25
- Transparent communication, on-time: 20
- Proper evidence handling: 15
- Complete remediation: 20
- Efficient budget use: 12
- Final reputation 92: 5 bonus
Total: 97 points (excellent crisis response)
```

**Outcome Tiers:**
- **85+:** Crisis well-managed; recovery likely; stakeholder trust maintained
- **65-84:** Adequate response; some damage; recovery possible
- **45-64:** Poor response; significant damage; recovery uncertain
- **Below 45:** Crisis mismanaged; major reputational/financial damage; company survival in question

### Debrief (5-10 minutes)

1. **Investigation Quality:**
   - "Did you investigate adequately?"
   - "What important information did you miss?"

2. **Communication Strategy:**
   - "How did you prioritize stakeholder notifications?"
   - "What would you communicate differently?"

3. **Financial Decisions:**
   - "Did you pay the ransom? Why or why not?"
   - "What was the total incident cost?"

4. **Response Quality:**
   - "If you replayed, what would you do first?"
   - "Which stakeholder relationship was most important to preserve?"

5. **Real-World Connection:**
   - "Compare your spending to actual breaches you've heard about"
   - "What's hardest about crisis management?"

---

# FULL CAMPAIGNS (Combined Play)

---

## Full Campaign A: Detect & Defend (90-120 minutes)

### Overview
**"We Caught It - Now Let's Build Better Defenses"**

Teams play through attack detection (Phase 1) and, if they win, transition directly to security hardening (Phase 2 Hardening).

### Full Campaign A Timeline

| Phase | Duration | Activity |
|-------|----------|----------|
| Setup | 10 min | Rules explanation, team formation |
| **Phase 1: Incident Response** | 35-40 min | Detect attack chain before budget/turns run out |
| **Checkpoint** | 2 min | Determine if team won or lost |
| **Phase 2: Hardening (Win Path)** | 25-30 min | Build defenses, harden systems, prepare for future |
| Debrief | 15 min | Lessons learned, reflection |
| **Total** | 90-115 min | |

### Setup (10 minutes)

1. **Brief Teams:**
   - "You're a security team. An attack is happening *right now*. Can you detect it?"
   - "If you stop the attack, we'll then look at hardening your systems"

2. **Select Difficulty:**
   - **Beginner:** 3-card chain, 100 budget, 12 turns
   - **Intermediate:** 4-card chain, 100 budget, 10 turns
   - **Advanced:** 5-card chain, 100 budget, 10 turns

3. **TO Builds Hidden Chain:**
   - Select threat cards
   - Write clues for each card
   - Set Asset Cards

### Phase 1: Incident Response (35-40 minutes)

Standard Phase 1 gameplay:
- Teams Investigate, Deploy Defenses, or use Emergency Response
- Roll for success
- Progress through the hidden attack chain
- Apply Uncontained Threats penalties

**Victory Condition:** Reveal all cards before Turn 10 or Budget 0

### Checkpoint & Transition (2 minutes)

**If Team Won Phase 1:**
"Excellent work! Your team detected the attack chain in time.
- Attack stopped at card X (before full exfiltration)
- Partial customer data compromised, but contained
- Now we need to harden your systems to prevent this from happening again"

→ **Proceed to Phase 2: Hardening**

**If Team Lost Phase 1:**
"Unfortunately, your team ran out of time/budget before detecting the full chain.
Thank you for playing Phase 1. You can either:
- Option A: Proceed to Phase 2 - Disaster Recovery (see Campaign B)
- Option B: Replay Phase 1 with different strategy
- Option C: Stop here and discuss lessons learned"

Most groups proceed to **Campaign B: Attack & Recover** if they lose Phase 1.

### Phase 2: Hardening (25-30 minutes, Win Path Only)

**Transition Narrative:**
"Now that we've stopped this attack, your security team wants to prevent it from ever happening again. You have time and resources to harden your defenses. Here's what you successfully detected:

- **Initial compromise vector:** [Reveal threat 1 vector]
- **Lateral movement:** [Reveal threat 2 vector]
- **Persistence mechanism:** [Reveal threat 3 vector]
- **Exfiltration method:** [Reveal threat 4 vector if applicable]

**Key Question:** What defenses would have stopped this attack at each stage?"

**Hardening Budget:**
- Standard: 150 (fresh allocation representing planning time)
- Plus: Any remaining Phase 1 budget (if they were efficient)

**Hardening Gameplay:**
- Deploy defenses against each vector
- Harden existing defenses
- Create incident response playbooks
- Defend against 3-4 Pentester Tactics

### Debrief (15 minutes)

**Part 1: Attack Analysis (4 min)**
1. "What was the attacker's kill chain?"
2. "Why was it hard to detect in Phase 1?"
3. "Where should detection have happened?"

**Part 2: Defense Strategy (5 min)**
1. "Why did you deploy defenses in that order?"
2. "What layers work together effectively?"
3. "Did the Pentester Tactics reveal gaps?"

**Part 3: Lessons (6 min)**
1. "What would you deploy first if replaying?"
2. "How much does early detection save?"
3. "Why is layered defense important?"

---

## Full Campaign B: Attack & Recover (90-120 minutes)

### Overview
**"We Missed It - Now Manage the Crisis"**

Teams play through attack detection (Phase 1) and, if they lose, transition directly to disaster recovery (Phase 2 Disaster Recovery).

### Full Campaign B Timeline

| Phase | Duration | Activity |
|-------|----------|----------|
| Setup | 10 min | Rules explanation, team formation |
| **Phase 1: Incident Response** | 35-40 min | Try to detect attack chain (will likely fail or barely escape) |
| **Checkpoint** | 2 min | Determine outcome (loss triggers DR path) |
| **Phase 2: Disaster Recovery (Loss Path)** | 30-35 min | Crisis management, forensics, stakeholder communication |
| Debrief | 15 min | Lessons learned, consequences reflection |
| **Total** | 105-120 min | |

### Setup (10 minutes)

1. **Brief Teams:**
   - "You're a security team. An attack is happening *right now*. Can you detect it *fast enough*?"
   - "We're using a challenging scenario. If you don't catch it in time, you'll enter crisis management"

2. **Select Challenging Scenario:**
   - **Intermediate:** 4-card chain, 100 budget, 10 turns (medium difficulty)
   - **Advanced:** 5-card chain, 100 budget, 10 turns (high difficulty)
   - **Enterprise:** 5-card chain with special rules (very high difficulty)

3. **TO Notes:**
   - Consider using expansion threats (supply chain, insider, IoT) for added complexity
   - Phase 1 will be challenging; some teams will run out of budget

### Phase 1: Incident Response (35-40 minutes)

Standard Phase 1 gameplay, but with challenging scenario design:
- More complex attack chains
- Misleading clues to cause investigative missteps
- Tight budget constraints
- Uncontained Threats penalties apply

**Note:** Most teams will **NOT** successfully reveal all cards. This is intentional.

### Checkpoint & Transition (2 minutes)

**If Team Lost Phase 1 (Likely):**
"Your team ran out of budget/turns before detecting the full chain. The attack succeeded.

**Breach Details (Now Revealed):**
- Full attack chain: [Reveal all 4-5 threat cards]
- Customer data compromised: 500,000 records
- Attacker demanding ransom: $1M
- Timeline: You have 48 hours to respond
- Media: Rumors are spreading; public disclosure likely

Your focus now shifts from *detection* to *crisis management*."

→ **Proceed to Phase 2: Disaster Recovery**

**If Team Won Phase 1 (Possible but Hard):**
"Impressive! You detected the attack chain against challenging odds.
You can proceed to Phase 2 - Hardening (Campaign A path) instead of Disaster Recovery."

### Phase 2: Disaster Recovery (30-35 minutes, Loss Path)

**Transition Narrative:**
"The breach has occurred. Your team is now in crisis mode. Here's what happened:

**Attack Chain (Full Revelation):**
1. [Threat 1]: [Description] - Attackers gained initial access
2. [Threat 2]: [Description] - Moved laterally across network
3. [Threat 3]: [Description] - Escalated privileges
4. [Threat 4]: [Description] - Exfiltrated customer data
5. [Threat 5 if applicable]: [Description] - Established persistence

**Current Situation:**
- Breach confirmed
- 500,000+ customer records compromised
- Attacker has contacted you with ransom demand
- Media is investigating
- You have 48 hours to respond

**Your Crisis Team:**
- Legal: Requires immediate compliance with notification laws
- Finance: Calculating total cost
- PR: Managing public perception
- Security: Investigating and remediating
- Executive Leadership: Waiting for your recommendations

**Available Crisis Budget:** 50 (emergency fund) + [any remaining Phase 1 budget]

**Your Tasks in 48 Hours:**
1. Investigate the breach (forensics)
2. Notify stakeholders (customers, regulators, media)
3. Preserve evidence (legal protection)
4. Remediate systems (remove attacker access)
5. Make ransom decision (pay, negotiate, or refuse)"

**Disaster Recovery Gameplay:**
- 7 turns (each turn = ~6-12 hours of real time)
- Choose ONE crisis action per turn
- Manage reputation score (starts at 100)
- Track financial costs

### Debrief (15 minutes)

**Part 1: Detection Failure (4 min)**
1. "Why wasn't the attack detected in Phase 1?"
2. "What broke down in your investigation?"
3. "What signs did you miss?"

**Part 2: Crisis Response (5 min)**
1. "How well did you manage the crisis?"
2. "Which stakeholder communication was most important?"
3. "Did you make the right ransom decision?"

**Part 3: Consequences (6 min)**
1. "What was the total incident cost (financial + reputation)?"
2. "How different is this from Phase 1 cost if you'd detected early?"
3. "What would prevent this next time?"

**Part 4: Connection (Critical)**
"Detection costs less than a dollar per breach. Crisis management costs $1M+. 
This is why incident detection is a priority."

---

## Mixed Option: Quick Campaign (60-75 minutes)

### Concept
**"Skip Phase 1 - Jump Straight to Either Hardening or Disaster Recovery"**

Useful for time-constrained sessions where you want to teach *either* hardening *or* crisis management, but don't have 2 hours.

### Quick Campaign: Hardening Only (60-75 minutes)

**Setup (5 min):**
- TO describes a hypothetical Phase 1 scenario: "Your team caught this attack after 2 hours of investigation. You now have time to harden..."
- Establish 150 Budget (more than Phase 1, represents planning resources)

**Play Phase 2: Hardening (40-45 min):**
- Deploy defenses against attack vectors
- Defend against Pentester Tactics
- Build incident response playbooks

**Debrief (15-20 min):**
- Discuss defense strategy
- Analyze Pentester results
- Connect to real organizational hardening

**Total: 60-75 minutes**

### Quick Campaign: Disaster Recovery Only (60-75 minutes)

**Setup (5 min):**
- TO describes Phase 1 failure: "Your team ran out of time. The attack succeeded. Here's what happened..."
- Establish 50 Budget (emergency crisis fund)
- Describe breach scope and impact

**Play Phase 2: Disaster Recovery (40-45 min):**
- Manage crisis actions (forensics, communication, remediation)
- Make ransom decisions
- Track reputation and costs

**Debrief (15-20 min):**
- Discuss crisis response quality
- Analyze financial/reputational impact
- Compare to real incident costs

**Total: 60-75 minutes**

---

# TOURNAMENT STRUCTURE

---

## Tournament Mode: Multiple Teams, Mixed Paths (2-2.5 hours)

### Setup (10 minutes)

1. **Form Teams:** 2-4 teams of 3-5 people
2. **Select Scenario:** All teams play same Phase 1 scenario
3. **Brief Teams:** "You're all responding to the same attack. Who can detect it fastest?"

### Phase 1: All Teams Simultaneous (40 minutes)

- All teams play identical Phase 1 scenario
- TO manages multiple investigations simultaneously (or use assistant TO)
- Teams cannot see each other's progress
- Victory: First team to reveal all cards / best score

### Bracket Determination (5 minutes)

**After Phase 1 Ends:**
- **Teams that Won Phase 1** (revealed all cards in time):
  - Advance to **Phase 2: Hardening**
  - Challenge: Build best security posture
- **Teams that Lost Phase 1** (ran out of budget/turns):
  - Advance to **Phase 2: Disaster Recovery**
  - Challenge: Manage crisis best

### Phase 2: Split Bracket (30-35 minutes)

**Simultaneous:**
- **Hardening Group:** Deploy defenses, defend against Pentester Tactics
- **Disaster Recovery Group:** Manage crisis, communicate with stakeholders

### Final Scoring (10 minutes)

**Hardening Track Winners:**
- Highest Security Score (70-100 scale)
- Bonus: Budget efficiency

**Disaster Recovery Track Winners:**
- Highest Reputation Score (0-100 scale)
- Bonus: Financial efficiency

**Optional: Cross-Track Winner**
- Best "Incident Response Score" combining both:
  - Phase 1 Detection Score (how well did you detect?)
  - Phase 2 Response Score (how well did you respond?)
  - If you won Phase 1: Focuses on hardening quality
  - If you lost Phase 1: Focuses on crisis management quality

### Awards & Debrief (15-20 minutes)

**Awards:**
- "Best Detection" (fastest Phase 1 clear)
- "Best Defense" (highest hardening score)
- "Best Crisis Manager" (highest disaster recovery score)
- "Most Improved" (learned most from debrief)

**Debrief:**
- Compare strategies across teams
- Discuss differences between winning and losing paths
- Highlight key learning moments

---

# SETUP REFERENCE: Quick Start Guide

---

## Choosing Your Game Mode

### If You Have 30-45 Minutes: Play One Mini-Game
- **Want to teach detection?** → Mini-Game 1: Phase 1
- **Want to teach defense?** → Mini-Game 2: Hardening
- **Want to teach crisis response?** → Mini-Game 3: Disaster Recovery

### If You Have 90-120 Minutes: Play a Full Campaign
- **Want natural game flow?** → Campaign A (Detect & Defend) or Campaign B (Attack & Recover)
- **Want both paths represented?** → Tournament mode with split bracket

### If You Have 60-75 Minutes: Play Quick Campaign
- **Limited time, must teach hardening?** → Quick Campaign: Hardening
- **Limited time, must teach crisis response?** → Quick Campaign: Disaster Recovery

### If You Have 2-2.5 Hours: Play Tournament
- Multiple teams compete in Phase 1
- Winners go to Hardening, Losers go to Disaster Recovery
- Determine best detectors AND best responders

---

## Materials Needed by Game Mode

### Mini-Game 1: Phase 1 Only
- 12 Threat Cards (base deck)
- 24 Defense Cards (base deck)
- 6 Asset Cards (relevant to scenario)
- Turn Tracker, Budget Tracker, Uncontained Threats Tracker
- 1d20 die
- Reference sheets for roll modifiers

### Mini-Game 2: Hardening Only
- 24 Defense Cards (base deck)
- 6 Asset Cards
- 4-6 Pentester Tactic Cards
- Reputation/Security Score Tracker
- Defense tracking sheet
- 1d20 die for pentester challenges

### Mini-Game 3: Disaster Recovery Only
- 8 Crisis Action Cards (or use descriptions)
- 8-12 Threat Cards (for reference, fully revealed)
- Timeline tracker (6-7 turns)
- Reputation tracker (0-100)
- Financial impact sheet
- Stakeholder communication log
- 1d20 die for forensic/negotiation rolls

### Full Campaign A: Detect & Defend
- All Phase 1 materials
- All Hardening materials
- Transition narrative cards

### Full Campaign B: Attack & Recover
- All Phase 1 materials
- All Disaster Recovery materials
- Transition narrative cards

### Tournament Mode
- All Phase 1 materials
- Hardening materials (for winner bracket)
- Disaster Recovery materials (for loser bracket)
- Multiple scoresheets
- Team assignment sheet

---

## Time Management Tips

### For Quick Setup
- Pre-build threat chains before game starts
- Have scenario cards printed and ready
- Use pre-written clues
- Have default Defense Card starting hands

### For Large Groups
- Use assistant Threat Orchestrators
- Pre-assign teams
- Have parallel games running (Phase 1 in Room A, Phase 2 outcomes in Room B)

### For Time-Constrained Sessions
- Use beginner difficulty (3-card chains are faster)
- Reduce Pentester Tactics to 2-3 instead of 4
- Reduce debrief to 5 minutes instead of 15
- Use "strict" turn limits (10 minutes per turn maximum)

---

## Replayability: Different Each Time

### Scenario Variations
- **Supply Chain Focus:** Use T-13, T-14 threats, CSPM defenses
- **Insider Threat Focus:** Use T-15, T-16 threats, behavioral analytics defenses
- **Cloud-Native Focus:** Use T-18 threat, cloud security defenses
- **IoT Focus:** Use T-17 threat, IoT-specific defenses

### Difficulty Progressions
- **Session 1:** Beginner (3-card chain, Hardening path)
- **Session 2:** Intermediate (4-card chain, both paths)
- **Session 3:** Advanced (5-card chain + expansion threats, deep debrief)

### Different Team Compositions
- Play with different team sizes (2 vs. 5 people per team)
- Play competitively vs. cooperatively
- Play with different role assignments (CISO, SOC Lead, Forensics, etc.)

---

# SUMMARY: Six Ways to Play

| Mode | Duration | Focus | Best For |
|------|----------|-------|----------|
| **Mini-Game 1** | 30-45 min | Detection | Intro, quick sessions |
| **Mini-Game 2** | 30-45 min | Hardening | Defense strategy |
| **Mini-Game 3** | 30-45 min | Crisis Response | Incident management |
| **Campaign A** | 90-120 min | Detect + Defend | Full arc, winning path |
| **Campaign B** | 90-120 min | Attack + Recover | Full arc, losing path |
| **Tournament** | 2-2.5 hours | Competition | Multiple teams, mixed |

---

## Pedagogical Value by Mode

### Phase 1 (Detection)
- **Teaches:** Kill chain, investigation methodology, budget prioritization
- **Key Insight:** Dwell time matters; early detection saves millions
- **Real-World:** SOC analysts, threat hunting, SIEM tuning

### Phase 2: Hardening (Win Path)
- **Teaches:** Defense-in-depth, layered security, strategic planning
- **Key Insight:** Prevention is cheaper than response
- **Real-World:** Security architects, GRC teams, budget planning

### Phase 2: Disaster Recovery (Lose Path)
- **Teaches:** Incident response procedures, crisis management, stakeholder communication
- **Key Insight:** Perfect prevention is impossible; response capability matters
- **Real-World:** Incident responders, legal/compliance, PR/communications

### Tournament Mode
- **Teaches:** All of the above, plus competitive thinking
- **Key Insight:** Both detection and response are critical skills
- **Real-World:** Competing security teams, red team vs. blue team dynamics

---

*Incident Zero: Flexible Play Modes & Configurations*  
*Mix and match to fit your curriculum and time constraints*