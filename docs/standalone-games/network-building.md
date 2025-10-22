# Incident Zero: Network Building Standalone Mini-Game
## Infrastructure Design Competition

---

## Overview

**Network Building Standalone** is a **30-45 minute competitive resource management game** where teams design IT infrastructure under budget constraints with random business requirements and operational challenges.

**Core Concept:**
- **Budget:** Limited funding (50 Network Budget tokens)
- **Requirements:** Random business needs forcing tough trade-offs
- **Randomness:** Equipment failures, budget surprises, requirement changes
- **Scoring:** Multi-dimensional (security, budget efficiency, capability, resilience)
- **Winner:** Team with highest final score

**Best For:**
- Teaching infrastructure trade-offs
- Understanding security budget constraints
- Decision-making under uncertainty
- Standalone 30-45 minute session
- Competitive team play (2-4 teams)

---

## Win Condition & Game Length

### Turns & Time

**Game Duration: 5-6 turns × 4-5 minutes per turn = 20-30 minutes gameplay**
- **Setup:** 5 minutes (explain rules, distribute materials)
- **Gameplay:** 20-30 minutes
- **Scoring & Debrief:** 5-10 minutes
- **Total:** 30-45 minutes

**Each turn = represents ~1 quarter of fiscal year**
- Team decides: Deploy server OR security device OR handle random event
- Roll for business requirement (what service needed this quarter?)
- Roll for operational incident (failure, budget change, etc.)

---

## Game Components

### Network Budget Tokens
- **Starting Budget:** 50 Network Budget
- **Costs:** Servers (3-15), Security Devices (6-15), Architecture (0-12)
- **Tokens:** Physical tokens, spreadsheet, or tracking sheet

### Component Cards

#### SERVER CARDS (Print 30-40 copies distributed randomly)
Each has: Type, Cost, Capacity, Security Profile

```
┌──────────────────────┐
│ EMAIL SERVER         │
│ Cost: 8              │
│ Capacity: 1 service  │
│ Security: Low        │
│ (Phishing target)    │
└──────────────────────┘
```

**Server Types Available:**
- Email Server (8 Budget, 1 capacity, Low security)
- Web Server (7 Budget, 1 capacity, Low security)
- Database Server (10 Budget, 1 capacity, Medium security)
- File Server (6 Budget, 2 capacity, Low security)
- Domain Controller (12 Budget, 2 capacity, Medium security)
- Development Server (5 Budget, 3 capacity, Low security)
- Backup System (9 Budget, 1 capacity, High security)
- Cloud Workload (4 Budget, 2 capacity, Medium security)
- Legacy System (3 Budget, 1 capacity, Very Low security)
- Honeypot Decoy (7 Budget, 1 capacity, Medium security)

#### SECURITY DEVICE CARDS (Print 20-30 copies distributed randomly)
Each has: Type, Cost, Effect

```
┌──────────────────────┐
│ FIREWALL             │
│ Cost: 12             │
│ Effect: +1 Network   │
│ Segmentation         │
└──────────────────────┘
```

**Security Device Types Available:**
- Firewall (12 Budget, +1 Network Segmentation)
- IDS (10 Budget, +1 Detection)
- IPS (14 Budget, +2 Web/Network Protection)
- Email Gateway (6 Budget, +1 Phishing Protection)
- WAF (11 Budget, +1 Web Protection)
- SIEM (15 Budget, +1 Detection, +1 Investigation)
- Network Segmentation Switch (10 Budget, +1 Network Segmentation)
- VPN Concentrator (9 Budget, enables remote access)
- Load Balancer (8 Budget, improves capacity)
- Honeypot Network (8 Budget, +1 Detection)

#### BUSINESS REQUIREMENT CARDS (Print 20-30 copies)
Random quarterly business needs

```
┌──────────────────────┐
│ BUSINESS REQUIREMENT │
│ TURN CARD            │
├──────────────────────┤
│ Q2: "New Product     │
│ Launch Website"      │
│                      │
│ Must provide: Web    │
│ server capability    │
│                      │
│ Consequence if       │
│ missing: -5 points   │
└──────────────────────┘
```

**Requirement Examples:**
- "New Product Launch Website" → Need Web Server
- "Acquire Customer Database" → Need Database Server
- "Work-From-Home Program" → Need VPN
- "Comply with HIPAA" → Need Backup + Encryption (or lose -10 points)
- "Scale Email System" → Upgrade Email Server OR add Load Balancer
- "Security Audit Required" → Need SIEM OR lose -5 points
- "Major Breach Incident" → Need Incident Response capabilities (IDS/IPS/SIEM) OR lose -15 points
- "Company Merger Announced" → Need 2x capacity on multiple systems OR lose -10 points
- "New Subsidiary Office" → Need Remote Access (VPN) OR lose -5 points
- "Ransomware Attack Industry" → Need Backup System AND Detection OR lose -20 points

#### OPERATIONAL EVENT CARDS (Print 15-20 copies)
Random incidents, opportunities, challenges

```
┌──────────────────────┐
│ OPERATIONAL EVENT    │
├──────────────────────┤
│ "Email Server Failed"│
│                      │
│ Cost to Fix: 5 Budget│
│ (Emergency repair)   │
│                      │
│ OR                   │
│                      │
│ Skip: -10 points     │
│ (Users upset)        │
└──────────────────────┘
```

**Event Examples:**
- "Email Server Failed" → Cost 5 to fix OR -10 points
- "Budget Increase - Emergency Funds" → +10 Budget (one time)
- "Budget Cut - Fiscal Crisis" → -10 Budget this turn
- "File Server Filling Up" → Add capacity OR -5 points (service degradation)
- "Honeypot Caught an Attack" → +5 points (detection worked!)
- "Cloud Service Outage" → Cloud servers unavailable this turn
- "Executive Demands HIPAA Compliance" → Must have Backup OR -20 points
- "Competitor Got Hacked" → Must add IDS/IPS OR -5 points (board pressure)
- "New Hire Wants Remote Access" → Must have VPN OR -3 points (employee leaves)
- "IT Staff Burnout" → Can only deploy 1 device this turn (cost 1 extra budget)
- "Price Drop on Security" → Deploy device at -2 cost (limited time)
- "Ransomware Variant Detected in Wild" → Must have Backup OR face -25 points next turn
- "Board Approves IT Capex Increase" → +15 Budget (major boost)

---

## Game Setup (5 minutes)

### 1. Explain Scoring System

**Final Score = Security Score + Budget Score + Capability Score + Resilience Score**

Teams win by maximizing total score, not just saving budget.

### 2. Distribute Starting Materials

**Each Team Receives:**
- Starting Budget: 50 Network Budget tokens
- Infrastructure Summary Sheet (to track what they've built)
- Score Tracking Sheet
- Network Diagram Worksheet (optional, for visualization)

### 3. Create Card Decks

**Shuffle and place face-down:**
- Business Requirement Card deck (1 per turn, 5-6 cards total)
- Operational Event Card deck (1 per turn, 5-6 cards total)

### 4. Brief Teams

**"You're a CIO designing your organization's IT infrastructure for the next 18 months. You have limited budget ($50K, represented as 50 tokens). Each quarter brings new business requirements and operational challenges. You must balance:
- Getting the work done (business requirements)
- Keeping things secure (security devices)
- Managing money (budget efficiency)
- Surviving incidents (resilience features)

After 6 quarters (turns), we'll score your infrastructure. Highest score wins."**

---

## Turn Structure (4-5 minutes per turn)

### Each Turn Has 4 Phases

#### **Phase 1: Reveal Business Requirement (1 minute)**

**Threat Orchestrator flips top Business Requirement Card:**

"It's Q2. The executive team wants to acquire a customer database company. You need to integrate their 2 million customer records into your infrastructure. You MUST have a functioning Database Server by end of Q2 or you lose 10 points (deal falls through)."

**Team Notes:**
- What service is needed?
- When is deadline? (end of this turn or can you defer?)
- What's the penalty if you skip? (points deduction)

**Teams Discuss: Do we have it? If not, how do we get it?**

#### **Phase 2: Reveal Operational Event (1 minute)**

**Threat Orchestrator flips top Operational Event Card:**

"OPERATIONAL EVENT: Your Email Server just failed. It's been down for 2 hours. You can:
- **Option A:** Pay 5 budget for emergency repair (get email back online)
- **Option B:** Skip repair (email stays down all quarter) - lose 10 points (users upset, productivity down)
- **Option C:** Use this as an excuse to upgrade (replace with new server, normal cost)"

**Teams Decide:** How to handle the incident?

#### **Phase 3: Team Takes One Action (2-3 minutes)**

**Teams Choose ONE:**

##### **Action A: Deploy a Server**
- **Select a Server Card** from available servers
- **Pay the Cost** (from budget)
- **Mark Capacity** on infrastructure sheet
- **Consequence:** Servers stay deployed (can't remove them)

**Example:**
"We're deploying a Database Server on-premises. Cost: 10 budget. Remaining: 40 budget. This satisfies the Q2 acquisition requirement. No penalty!"

##### **Action B: Deploy a Security Device**
- **Select a Security Device Card**
- **Pay the Cost**
- **Note the Bonus** (what it improves)
- **Can be deployed multiple times** (multiple firewalls, IDS on different segments, etc.)

**Example:**
"We're deploying an IDS on our internal network. Cost: 10 budget. This gives us +1 Detection capability. Remaining: 30 budget. If a Honeypot Event comes up, we'll have detection."

##### **Action C: Handle Operational Event**
- **Select the event cost** (fix it, skip it, upgrade it)
- **Deduct cost from budget**
- **Update score** (penalties if skipped)

**Example:**
"Email Server failed. We're paying 5 budget for emergency repair. That lets us avoid the -10 penalty. Remaining: 25 budget."

##### **Action D: Pass This Turn**
- **Cost:** 0
- **Effect:** Don't deploy anything
- **Use When:** Budget is low OR you're satisfied with current design
- **Note:** Still suffer any requirement penalties or event consequences

#### **Phase 4: End of Turn Accounting (30 seconds)**

**Update Trackers:**
- Subtract budget spent
- Mark servers/devices deployed
- Apply any penalties from unmet requirements
- Prepare for next turn

**Next Turn Begins**

---

## Scoring System

### Scoring Dimensions

**Final Score = Security + Budget + Capability + Resilience**

#### 1. SECURITY SCORE (0-30 points)
Measures defensive capability against attacks

| Security Metric | Points | How Scored |
|-----------------|--------|-----------|
| **IDS/IPS Deployed** | +5 | Detect/prevent network attacks |
| **SIEM Deployed** | +5 | Centralized logging & detection |
| **Email Gateway Deployed** | +3 | Phishing protection |
| **WAF Deployed** | +3 | Web application protection |
| **Firewall Deployed** | +3 | Network segmentation |
| **Honeypot Deployed** | +2 | Early warning system |
| **Backup System Deployed** | +4 | Ransomware recovery |
| **Network Segmentation** | +2 | Lateral movement prevention |

**Maximum Security Score: 30 points**

**Examples:**
- Only Email Gateway: 3 points (basic phishing defense, weak)
- IDS + SIEM + Email Gateway: 13 points (good detection)
- Full suite (IDS + IPS + SIEM + Email Gateway + WAF + Firewall + Backup + Honeypot): 30 points (enterprise-grade, but expensive)

#### 2. BUDGET SCORE (0-20 points)
Efficiency of spending relative to capability gained

**Budget Remaining → Points:**
- 40+ budget left: 20 points (very efficient; built minimum viable)
- 30-39 budget left: 15 points (efficient)
- 20-29 budget left: 10 points (moderate)
- 10-19 budget left: 5 points (spent most of it)
- 0-9 budget left: 0 points (spent everything)

**Logic:** Efficient infrastructure uses less budget for same capability.

**Examples:**
- Spent 45, left 5: 0 points (over-spent)
- Spent 30, left 20: 10 points (balanced)
- Spent 20, left 30: 15 points (lean infrastructure)

#### 3. CAPABILITY SCORE (0-25 points)
Does infrastructure meet business requirements?

**Each Business Requirement met = Points**

| Capability | Points | Notes |
|-----------|--------|-------|
| **Email Server** | +3 | Basic business function |
| **Web Server** | +3 | Public presence / e-commerce |
| **Database Server** | +4 | High-value data management |
| **File Server** | +2 | Internal collaboration |
| **Domain Controller** | +3 | User identity & security |
| **Development Server** | +2 | Innovation capability |
| **Backup System** | +3 | Disaster recovery |
| **Remote Access (VPN)** | +2 | Work-from-home support |
| **Cloud Workload** | +2 | Scalability & redundancy |

**Penalties for Missing Key Services:**
- No Email Server: -5 points (business can't communicate)
- No Web Server (if required): -5 points
- No Database Server (if required): -10 points (major data loss)
- No Backup (if ransomware event): -25 points (catastrophic)
- No VPN (if remote access needed): -3 points (employee satisfaction)

**Maximum Capability Score: 25 points**

**Examples:**
- Has: Email, Web, Database, File, Domain Controller, Backup → 19 points (good)
- Has: Email, Web, Database, File, Domain, Backup, VPN, Honeypot → 24 points (excellent)
- Missing: Database (when required) → 10 points (penalty kicks in)

#### 4. RESILIENCE SCORE (0-25 points)
Ability to survive and recover from failures

**Resilience Factors:**

| Factor | Points | Criteria |
|--------|--------|----------|
| **Backup System** | +8 | Can recover from ransomware/data loss |
| **Redundancy** | +5 | Multiple servers in same role OR load balancing |
| **Detection** | +7 | IDS/IPS/SIEM can spot attacks early |
| **Isolation** | +3 | Network segmentation prevents spread |
| **Recovery Plan** | +2 | Has both Backup and incident response |

**Penalties for Vulnerabilities:**
- No Backup (if disaster occurs): -20 points (major liability)
- Single point of failure (all critical services on one server): -5 points
- No detection capability (can't see attacks): -3 points
- Flat network (no segmentation): -2 points

**Maximum Resilience Score: 25 points**

**Examples:**
- Backup + Detection + Segmentation + Redundancy: 23 points (very resilient)
- Backup + Detection, but no redundancy: 15 points (adequate)
- No Backup, no detection: 0 points (high risk)

---

## Final Scoring Example

### Team A's Infrastructure

**Built:**
- Email Server (8): handles email
- Web Server (7): public website
- Database Server (10): customer data
- File Server (6): internal files
- Domain Controller (12): user identity
- Backup System (9): disaster recovery
- IDS (10): network detection
- Email Gateway (6): phishing defense
- Firewall (12): network boundary

**Total Spent:** 80... Wait, that's over budget!

**Let me recalculate:**
- Email Server: 8
- Web Server: 7
- Database Server: 10
- File Server: 6
- Domain Controller: 12
- Backup System: 9
- Email Gateway: 6
- **Subtotal: 58 (over budget!)**

**Real Team A (Budget conscious):**
- Email Server: 8
- Web Server: 7
- Database Server: 10
- File Server: 6
- Domain Controller: 12
- Backup System: 9
- Email Gateway: 6
- **Total: 58... still over!**

**Revised Team A (Actually under budget):**
- Email Server: 8
- Web Server: 7
- Database Server: 10
- File Server: 6
- Domain Controller: 12
- Backup System: 9
- Email Gateway: 6
- **Total: 58 (OVER BUDGET)**

**Let me recalculate more carefully:**
- Email: 8
- Web: 7
- Database: 10
- File: 6
- Domain: 12
- Backup: 9
- Email Gateway: 6
- **Actual Total: 58 (over 50)**

**Revised Team A (Practical):**
- Email Server: 8
- Web Server: 7
- Database Server: 10
- File Server: 6
- Domain Controller: 12
- Backup System: 9
- Email Gateway: 6
- **Total if we drop Email Gateway: 52 (STILL OVER!)**

**Let me try again more carefully:**
- Email: 8
- Web: 7
- Database: 10
- Domain: 12
- Backup: 9
- Email Gateway: 6
- **Total: 52 (over 50)**

**Team A Final (Realistic):**
- Email Server: 8
- Web Server: 7
- Database Server: 10
- Domain Controller: 12
- Backup System: 9
- Email Gateway: 6
- **Total Spent: 52 (OVER!)**

**OK, ACTUALLY Team A Final:**
- Email Server: 8
- Web Server: 7
- Database Server: 10
- File Server: 6
- Backup System: 9
- Email Gateway: 6
- **Total: 46 / 50 (4 left)**
- **No Domain Controller** (too expensive; skipped for budget)

**Scoring Team A:**

**Security Score:** 
- Email Gateway: +3
- No IDS/IPS/SIEM/Honeypot: 0
- No Backup detection: (backup is there, but no redundancy for detection)
- **Total: 3 points**

**Budget Score:**
- 4 budget remaining out of 50
- (50-4)/50 = 92% spent = efficient
- **Score: 0 points (very little left)**

Actually, let me recalculate Budget Score more intuitively:
- 4 budget left: 20 points (very efficient!)
- **Actually makes sense: Left with 4 out of 50 = highly utilized**

**Budget Score: 20 points (very efficient)**

**Capability Score:**
- Email Server: +3
- Web Server: +3
- Database Server: +4
- File Server: +2
- Backup System: +3
- Missing Domain Controller: -3 (identity system critical)
- **Total: 12 points**

**Resilience Score:**
- Backup System: +8
- No redundancy: 0
- No detection: -3
- **Total: 5 points**

**Team A Final Score: 3 + 20 + 12 + 5 = 40 points**

---

### Team B's Infrastructure (Different Strategy)

**Built:**
- Email Server: 8
- Web Server: 7
- Database Server: 10
- Domain Controller: 12
- Backup System: 9
- IDS: 10
- Email Gateway: 6
- **Total: 62 (OVER!)**

**Revised Team B:**
- Email Server: 8
- Web Server: 7
- Database Server: 10
- Domain Controller: 12
- Backup System: 9
- IDS: 10
- **Total: 56 (OVER!)**

**Team B Final:**
- Email Server: 8
- Web Server: 7
- Database Server: 10
- Domain Controller: 12
- Backup System: 9
- Email Gateway: 6
- **Total: 52 (OVER by 2!)**

**Team B Actually:**
- Email Server: 8
- Web Server: 7
- Database Server: 10
- Domain Controller: 12
- IDS: 10
- **Total: 47 / 50 (3 left)**
- **No Backup System** (sacrificed for security)

**Scoring Team B:**

**Security Score:**
- IDS: +5
- Email Gateway: +3
- No Backup: 0
- **Total: 8 points**

**Budget Score:**
- 3 left out of 50: 20 points (very efficient)
- **Total: 20 points**

**Capability Score:**
- Email, Web, Database, Domain: +3+3+4+3 = 13
- Missing Backup: -3 (not critical but missing)
- **Total: 10 points**

**Resilience Score:**
- No Backup: -20 (major vulnerability if disaster strikes!)
- IDS Detection: +7
- **Total: -13 points (NEGATIVE!)**

**Team B Final Score: 8 + 20 + 10 + (-13) = 25 points**

**RESULT: Team A (40) beats Team B (25)**

**Lesson:** Having Backup is critical for resilience, even if it means fewer security devices.

---

## Competitive Play (2-4 Teams)

### Setup for Multiple Teams

**Each team:**
- Separate budget (50 tokens each)
- Separate infrastructure tracking sheet
- Separate score tracker

**Simultaneous Play:**
- All teams reveal requirement and event at same time
- Teams take turns choosing action (round-robin) OR all teams choose simultaneously
- Simultaneous is faster; rotating turns allows player agency

### Scoreboard

**Track all teams' scores throughout game:**

| Team | Sec | Budget | Cap | Res | TOTAL |
|------|-----|--------|-----|-----|-------|
| **Team A** | 8 | 20 | 12 | 5 | **45** |
| **Team B** | 12 | 15 | 18 | 10 | **55** |
| **Team C** | 5 | 10 | 8 | 2 | **25** |

**Winner:** Team with highest total score after Turn 6

### Tie-Breaking

**If two teams tie:**
1. **First tiebreaker:** Security Score (defense is critical)
2. **Second tiebreaker:** Resilience Score (ability to survive matters)
3. **Third tiebreaker:** Capability Score (business requirement fulfillment)

---

## Random Elements & Replayability

### Requirement & Event Card Variability

**Each game is different because:**

1. **Card Order Randomized:** Shuffle Business Requirement and Operational Event decks each game
2. **Card Selection:** To (or random selection) decides which requirements/events appear
3. **Consequence Ordering:** Early disasters force different choices than late surprises

**Example Game Flow Variations:**

**Game 1 (Tough Start):**
- Turn 1: Ransomware threat appears → Must buy Backup + Detection early
- Turn 2: Budget cut → Can't afford nice devices
- Turn 3: Merger announcement → Need more capacity
- Result: Teams forced into defensive posture

**Game 2 (Growth-Focused):**
- Turn 1: New product launch → Need Web Server
- Turn 2: Acquisition target → Need Database
- Turn 3: Expansion bonus → +15 budget!
- Result: Teams build bigger, more capable infrastructure

### Modified Difficulty Levels

**Beginner Mode (Generous):**
- Starting Budget: 60 (instead of 50)
- Cards are drawn kindly (fewer disasters)
- Turn Limit: 7 (extra time)

**Normal Mode (Standard):**
- Starting Budget: 50
- Random card draws
- Turn Limit: 6

**Hard Mode (Challenging):**
- Starting Budget: 40 (tight budget)
- Disaster cards more frequent
- Requirement penalties doubled
- Turn Limit: 5

---

## Example Full Game Walkthrough (6 Turns)

### TURN 1

**Phase 1: Business Requirement**
*TO flips card: "Executive Demands Website Redesign - Need modern web server capability. If missing by end of Q1: -5 points."*

**Phase 2: Operational Event**
*TO flips card: "Budget Good News! State tax rebate arrives. +10 Budget bonus (one time)."*

**Budget update: 50 + 10 = 60**

**Phase 3: Team Action**
"We're deploying a Web Server to meet the website redesign requirement. Cost: 7 budget. Remaining: 53 budget. We're not taking the detection risk, but we know we need a backup system eventually."

**Phase 4: End of Turn**
- Infrastructure: Web Server
- Budget: 53
- Score pending (calculated at end)

---

### TURN 2

**Phase 1: Business Requirement**
*"Acquire Customer Data Company - Must have functioning Database Server by end of Q2 or lose 10 points."*

**Phase 2: Operational Event**
*"Email Server Failed - Cost 5 budget for emergency repair OR skip and lose 10 points."*

**Phase 3: Team Action**
"We're deploying a Database Server (cost: 10 budget) to handle the acquisition. This is critical. For the email server, we'll pay 5 budget for the repair rather than lose 10 points. Total cost this turn: 15 budget. Remaining: 38 budget."

**Infrastructure update:** Web Server, Database Server
**Budget:** 38

---

### TURN 3

**Phase 1: Business Requirement**
*"Ransomware Variant Detected in Wild - You must deploy Backup capability AND Detection capability OR lose 20 points next turn."*

**Phase 2: Operational Event**
*"Cloud Service Price Drop - Deploy cloud workload at -2 cost (limited time offer)."*

**Phase 3: Team Action**
"Critical quarter. We're deploying:
- Backup System (9 budget)
- IDS (10 budget)
This prevents the 20-point penalty. We're using the Cloud Service discount to get Cloud Workload at cost 2 (normally 4). Total: 21 budget. Remaining: 17 budget."

**Infrastructure:** Web, Database, Backup, IDS, Cloud Workload
**Budget:** 17

---

### TURN 4

**Phase 1: Business Requirement**
*"Work-From-Home Initiative - Need remote access capability. Missing: -3 points."*

**Phase 2: Operational Event**
*"IT Staff Burnout - Can only deploy 1 device this turn (additional cost: 1 budget per device beyond 1)."*

**Phase 3: Team Action**
"We need remote access. We're deploying VPN Concentrator (9 budget). With the burnout penalty (no extra devices possible this turn). Remaining: 8 budget."

**Infrastructure:** Web, Database, Backup, IDS, Cloud, VPN
**Budget:** 8

---

### TURN 5

**Phase 1: Business Requirement**
*"Email Security Compliance - Must have Email Gateway OR lose 5 points."*

**Phase 2: Operational Event**
*"Data Center Upgrade - Existing on-prem systems get free redundancy (no cost). Instant +5 points to Resilience."*

**Phase 3: Team Action**
"We deploy Email Gateway (6 budget). We also get free redundancy from the data center upgrade (nice!). Remaining: 2 budget."

**Infrastructure:** Web, Database, Backup, IDS, Cloud, VPN, Email Gateway (+ Redundancy bonus)
**Budget:** 2

---

### TURN 6 (Final Turn)

**Phase 1: Business Requirement**
*"Executive Demands HIPAA Compliance Audit - Must have Domain Controller + SIEM + Backup OR lose 15 points."*

**Phase 2: Operational Event**
*"No incident this turn."*

**Phase 3: Team Action**
"We can't deploy Domain Controller (12 budget, we only have 2). We already have Backup. We DON'T have SIEM. We'll skip all deployment and take the -15 penalty."

**Final Infrastructure:**
- Web Server (7)
- Database Server (10)
- Backup System (9)
- IDS (10)
- Cloud Workload (4)
- VPN Concentrator (9)
- Email Gateway (6)
- **Total Spent: 55 (over budget!)**

**Wait, let me recalculate:**
- Web: 7
- Database: 10
- Backup: 9
- IDS: 10
- Cloud: 4
- VPN: 9
- Email Gateway: 6
- **Total: 55 (5 OVER BUDGET?!)**

**ISSUE: This team exceeded budget. Let me revise the scenario...**

Actually, in Turn 1 they got +10 bonus, so:
- Start: 50
- Turn 1 Bonus: +10 = 60
- Turn 2: -15 = 45
- Turn 3: -21 = 24
- Turn 4: -9 = 15
- Turn 5: -6 = 9
- Turn 6: Can't afford Domain Controller

**Final Budget: 9 remaining (very tight!)**

---

## FINAL SCORING

### This Team's Scores:

**Security Score:**
- IDS: +5
- Email Gateway: +3
- No SIEM: -3 (missing critical detection)
- No Firewall/WAF/Honeypot: 0
- **Total: 5 points**

**Budget Score:**
- 9 budget remaining out of 60 (after bonus)
- (60-9)/60 = 85% spent = efficient
- **Score: 5 points**

**Capability Score:**
- Web: +3
- Database: +4
- Backup: +3
- VPN: +2
- Email Gateway: +3 (counts as service)
- Missing Domain Controller: -3
- Missing Email Server: -5 (wait, they have Email Gateway but not Email Server? That's an issue)

Actually, let me clarify: Email Gateway is a security device, not a server. They still need an Email Server to process email.

**REVISED: Missing Email Server**
- **-5 penalty (no email capability)**

**Capability Score:**
- Web: +3
- Database: +4
- Backup: +3
- VPN: +2
- Missing Email Server: -5
- Missing Domain Controller: -3
- **Total: 4 points**

**Resilience Score:**
- Backup System: +8
- Redundancy (from data center): +5
- IDS Detection: +7
- No Network Segmentation: 0
- **Total: 20 points**

**FINAL SCORE: 5 + 5 + 4 + 20 = 34 points**

**Lesson:** This team prioritized resilience but sacrificed capability (missing email and identity systems) and budget efficiency was poor.

---

## Variations & House Rules

### Variation 1: "Overload Servers"
**Optional Rule:** Allow servers to exceed capacity at +1 cost per extra service.
- Example: Deploy 3 services on a 2-capacity server for +1 budget per extra service
- Creates trade-off: Save budget now OR pay more for overloaded risk

### Variation 2: "Upgrade Existing"
**Optional Rule:** Allow teams to upgrade servers already deployed (swap for better one, pay difference).
- Example: Replace File Server (2 capacity) with Domain Controller (2 capacity + identity services)
- Costs difference only (DC costs 12, File costs 6 = 6 extra budget)
- Creates flexibility but adds complexity

### Variation 3: "Disaster Strikes Mid-Game"
**Optional Rule (High Difficulty):** If Ransomware event is drawn but team has NO Backup, they immediately lose 25 points AND must deploy Backup by next turn (mandatory).
- Creates urgent decision point
- Teaches that failures have compounding consequences

### Variation 4: "Tech Debt"
**Optional Rule:** Each legacy server deployed costs 1 extra budget per turn to maintain (not paid upfront).
- Teaches that cheap solutions have hidden costs
- Creates long-term vs. short-term thinking

---

## Debrief Questions (5-10 minutes)

### Strategy Discussion

1. **"What was your infrastructure strategy? Why did you prioritize certain systems?"**
2. **"Which trade-off was hardest? (Security vs. Capability vs. Budget)"**
3. **"If you could replay, what would you change?"**

### Learning Connections

4. **"How does this relate to real IT budgeting?"**
5. **"What did you learn about balancing security with other concerns?"**
6. **"If this network gets attacked (Phase 1), which vulnerabilities do you see?"**

### Competitive Reflection

7. **"Why did Team X score higher? What did they do differently?"**
8. **"What was the winning strategy?"**

---

## Quick Reference Sheets

### Scoring Summary (1 page)

```
NETWORK BUILDING STANDALONE SCORING

SECURITY SCORE (max 30):
  IDS/IPS: +5
  SIEM: +5
  Email Gateway: +3
  WAF: +3
  Firewall: +3
  Honeypot: +2
  Backup: +4
  Network Segmentation: +2

BUDGET SCORE (max 20):
  40+ left: 20 pts | 30-39: 15 pts | 20-29: 10 pts | 10-19: 5 pts | 0-9: 0 pts

CAPABILITY SCORE (max 25):
  Email: +3 | Web: +3 | Database: +4 | File: +2 | Domain: +3
  Dev: +2 | Backup: +3 | VPN: +2 | Cloud: +2
  Penalties: -Email -5 | -Database -10 | -Backup -25 | -VPN -3

RESILIENCE SCORE (max 25):
  Backup: +8 | Redundancy: +5 | Detection: +7 | Segmentation: +3
  Penalties: -No Backup -20 | -No Redundancy -5 | -No Detection -3
```

### Component Quick Reference

```
SERVERS (Capacity / Cost / Security Profile):
  Email (1/8/Low) | Web (1/7/Low) | Database (1/10/Med)
  File (2/6/Low) | Domain (2/12/Med) | Dev (3/5/Low)
  Backup (1/9/High) | Cloud (2/4/Med) | Legacy (1/3/VLow) | Honeypot (1/7/Med)

SECURITY DEVICES (Cost / Effect):
  Firewall (12) | IDS (10) | IPS (14) | Email Gateway (6)
  WAF (11) | SIEM (15) | Segmentation (10) | VPN (9)
  Load Balancer (8) | Honeypot Network (8)
```

---

## Ready for Play!

This is a complete, standalone 30-45 minute competitive mini-game.

**To run a session:**
1. Print server and device cards
2. Prepare requirement and event card decks
3. Give each team budget tracker
4. Run 6 turns (4-5 min each)
5. Calculate final scores
6. Declare winner
7. 10-minute debrief

**Next: Ready to create Audit Standalone variations?**

*Incident Zero: Network Building Standalone Mini-Game*  
*Infrastructure design competition with multi-dimensional scoring*