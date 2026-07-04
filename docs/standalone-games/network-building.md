# Incident Zero: Network Building Standalone Mini-Game
## Infrastructure Design Competition

**Version:** 2.2 - Playtest Edition
**Last Updated:** July 2026

---

## Overview

**Network Building Standalone** is a **30-45 minute competitive resource management game** where teams design IT infrastructure under budget constraints with random business requirements and operational challenges.

**Core Concept:**
- **Budget:** Limited funding (40-60 Network Budget tokens by difficulty; 50 standard)
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

**Game Duration: 5-7 turns (by difficulty) × 4-5 minutes per turn = 20-30 minutes gameplay**
- **Setup:** 5 minutes (explain rules, distribute materials)
- **Gameplay:** 20-30 minutes
- **Scoring & Debrief:** 5-10 minutes
- **Total:** 30-45 minutes

**Each turn represents ~1 quarter of the fiscal year:**
- Reveal a Business Requirement (what does the business need this quarter?)
- Reveal an Operational Event (failure, budget change, attack, opportunity)
- Team deploys components, handles the event, or passes

---

## Game Components

### Network Budget Tokens
- **Starting Budget:** 50 Network Budget (Standard; see Difficulty Levels)
- **Costs:** Servers (3-12), Security Devices (6-15), Architecture (0-12)
- **Tokens:** Physical tokens, spreadsheet, or tracking sheet

### Component Cards

#### SERVER CARDS (print from `cards/network-building/core-deck/server-cards.md`)
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
- Backup Server (9 Budget, 1 capacity, High security)
- Cloud Workload (4 Budget, 2 capacity, Medium security)
- Legacy System (3 Budget, 1 capacity, Very Low security)
- Honeypot Decoy (7 Budget, 1 capacity, Medium security)

**Overload rule:** a server may host more services than its capacity for **+1 Budget per extra service** — but overloaded servers are a recorded risk (see Variations, now a standard rule).

#### SECURITY DEVICE CARDS (print from `cards/network-building/core-deck/security-device-cards.md`)
Each has: Type, Cost, Benefit

```
┌──────────────────────┐
│ FIREWALL             │
│ Cost: 12             │
│ Blocks traffic       │
│ between network      │
│ zones (segmentation) │
└──────────────────────┘
```

**Security Device Types Available (v2.2 — benefits stated in plain language; the Scoring section says what each counts as):**
- Firewall (12 Budget) — blocks traffic between network zones; counts as *Firewall* and toward *segmentation*
- IDS (10 Budget) — spots attacks in progress; counts as *detection*
- IPS (14 Budget) — blocks known exploits in real time; counts as *detection*
- Email Gateway (6 Budget) — filters phishing and email malware
- WAF (11 Budget) — protects web applications from injection/XSS attacks
- SIEM (15 Budget) — central logging and alerting; counts as *detection*, helps audits
- Network Segmentation Switch (10 Budget) — isolates network zones; counts as *segmentation*
- VPN Gateway (9 Budget) — secure remote access for staff
- Load Balancer (8 Budget) — spreads load across duplicated services; counts as *redundancy*
- Honeypot Network (8 Budget) — decoy segment that exposes intruders; counts as *detection*

#### BUSINESS REQUIREMENT CARDS (print from `cards/network-building/standalone/business-requirement-cards.md`)
20 cards (REQ-01 to REQ-20) of random quarterly business needs. Each names the requirement, what satisfies it, and the score impact.

```
┌──────────────────────┐
│ BUSINESS REQUIREMENT │
├──────────────────────┤
│ REQ-01: "New Product │
│ Launch Website"      │
│                      │
│ Satisfied by: Web    │
│ Server or cloud web  │
│                      │
│ Missed: -5 points    │
└──────────────────────┘
```

#### OPERATIONAL EVENT CARDS (print from `cards/network-building/standalone/operational-event-cards.md`)
16 cards (EVT-01 to EVT-16) of random incidents, opportunities, and challenges. Each states its effect and which designs mitigate it.

```
┌──────────────────────┐
│ OPERATIONAL EVENT    │
├──────────────────────┤
│ EVT-01: "Email       │
│ Server Failure"      │
│                      │
│ Pay 5 Budget to fix  │
│ OR -10 points        │
│                      │
│ Mitigated by:        │
│ redundant/cloud email│
└──────────────────────┘
```

---

## Game Setup (5 minutes)

### 1. Explain Scoring System

**Final Score = Security Score + Budget Score + Capability Score + Resilience Score − Requirement/Event penalties (+ bonuses)**

Teams win by maximizing total score, not just saving budget.

### 2. Distribute Starting Materials

**Each Team Receives:**
- Starting Budget: 50 Network Budget tokens (Standard difficulty)
- Infrastructure Summary Sheet (to track what they've built)
- Score Tracking Sheet
- Network Diagram Worksheet (optional, for visualization)

### 3. Create Card Decks

**Shuffle and place face-down:**
- Business Requirement deck (all 20 cards; 1 drawn per turn)
- Operational Event deck (all 16 cards; 1 drawn per turn)

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
- When is the deadline? (end of this turn unless the card says otherwise)
- What's the penalty if you skip? (points deduction)

**Teams Discuss: Do we have it? If not, how do we get it?**

#### **Phase 2: Reveal Operational Event (1 minute)**

**Threat Orchestrator flips top Operational Event Card:**

"OPERATIONAL EVENT: Your Email Server just failed. It's been down for 2 hours. You can:
- **Option A:** Pay 5 budget for emergency repair (get email back online)
- **Option B:** Skip repair (email stays down all quarter) - lose 10 points (users upset, productivity down)
- **Option C:** Use this as an excuse to upgrade (replace with new server, normal cost)"

**Teams Decide:** How to handle the incident?

#### **Phase 3: Team Actions (2-3 minutes) (v2.2)**

**Teams may take ANY NUMBER of the following actions, in any order, limited only by budget** (previously one action per turn):

##### **Action A: Deploy a Server**
- **Select a Server Card** from available servers
- **Pay the Cost** (from budget)
- **Mark Capacity** on infrastructure sheet (overloading costs +1 Budget per extra service)
- **Consequence:** Servers stay deployed (can't remove them)
- **Duplicates allowed:** each copy costs full price

**Example:**
"We're deploying a Database Server on-premises. Cost: 10 budget. Remaining: 40 budget. This satisfies the Q2 acquisition requirement. No penalty!"

##### **Action B: Deploy a Security Device**
- **Select a Security Device Card**
- **Pay the Cost**
- **Note the Benefit** (what it protects and what it counts as for scoring)
- **Can be deployed multiple times** (multiple firewalls, IDS on different segments, etc.)

**Example:**
"We're deploying an IDS on our internal network. Cost: 10 budget. Remaining: 30 budget. That gives us detection — if a ransomware or insider event comes up, we're covered."

##### **Action C: Handle Operational Event**
- **Select the event option** (fix it, skip it, upgrade it)
- **Deduct cost from budget**
- **Update score** (penalties if skipped)

**Example:**
"Email Server failed. We're paying 5 budget for emergency repair. That lets us avoid the -10 penalty. Remaining: 25 budget."

##### **Action D: Pass**
- **Cost:** 0
- **Effect:** End the turn without (further) deployments
- **Use When:** Budget is low OR you're satisfied with current design OR you're holding a reserve for surprises
- **Note:** You still suffer any requirement penalties or event consequences

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

**Final Score = Security + Budget + Capability + Resilience − requirement/event penalties (+ bonuses)**

Requirement and event penalties/bonuses (from the cards) are tracked as they happen and applied to the final total. Dimension scores can go negative.

#### 1. SECURITY SCORE (0-30 points)
Measures defensive capability against attacks

| Security Metric | Points | How Scored |
|-----------------|--------|-----------|
| **IDS or IPS Deployed** | +5 | Detect/prevent network attacks |
| **SIEM Deployed** | +5 | Centralized logging & detection |
| **Firewall Deployed** | +4 | Perimeter / zone enforcement |
| **Backup Server Deployed** | +4 | Ransomware recovery |
| **Email Gateway Deployed** | +3 | Phishing protection |
| **WAF Deployed** | +3 | Web application protection |
| **Honeypot Deployed** | +3 | Early warning system |
| **Network Segmentation** | +3 | Lateral movement prevention (Segmentation Switch or segmented architecture) |

**Maximum Security Score: 30 points** (5+5+4+4+3+3+3+3 = 30)

**Examples:**
- Only Email Gateway: 3 points (basic phishing defense, weak)
- IDS + SIEM + Email Gateway: 13 points (good detection)
- Full suite (IDS + SIEM + Firewall + Backup + Email Gateway + WAF + Honeypot + Segmentation): 30 points (enterprise-grade, but expensive)

#### 2. BUDGET SCORE (0-20 points) (v2.2)
Rewards **smart utilization**: meeting the business's needs within budget while keeping a small contingency reserve. Hoarding budget is NOT rewarded — an unspent token did no work.

**Budget Remaining at Game End → Points:**

| Budget Remaining | Points | Reading |
|------------------|--------|---------|
| **5-15 left** | 20 | Requirements met, plus a contingency reserve for surprises |
| **1-4 left** | 15 | Fully invested, but nothing left for the next incident |
| **0 left** | 10 | Ran completely dry |
| **16-25 left** | 10 | Under-invested; capability probably missing |
| **26+ left** | 5 | Hoarding — budget is not the goal |

**Anti-hoarding check:** if the team missed **2 or more** Business Requirements during the game, halve their Budget Score (round down). Saving money by failing the business is not efficiency.

**Examples:**
- Spent 42, left 8: 20 points (met needs, kept a reserve)
- Spent 46, left 4: 15 points (all-in; one bad event from trouble)
- Spent 20, left 30: 5 points (a pile of tokens and a network full of gaps)

#### 3. CAPABILITY SCORE (0-25 points)
Does infrastructure meet business needs?

| Capability | Points | Notes |
|-----------|--------|-------|
| **Email Service** | +3 | Basic business function (Email Server or cloud-hosted) |
| **Web Service** | +3 | Public presence / e-commerce |
| **Database Service** | +4 | High-value data management |
| **File Storage** | +2 | Internal collaboration |
| **Domain Controller** | +3 | User identity & security |
| **Development Capability** | +2 | Dev Server or dev via overload |
| **Backup Server** | +3 | Disaster recovery |
| **Remote Access (VPN Gateway)** | +2 | Work-from-home support |
| **Cloud Workload** | +2 | Scalability & redundancy |
| **Honeypot** | +1 | Early-warning capability |

**Maximum Capability Score: 25 points** (3+3+4+2+3+2+3+2+2+1 = 25)

**Penalties for Missing Key Services:**
- No Email service: **-5** (business can't communicate)
- No Database service: **-10** (core data has no home)
- No Domain Controller: **-3** (no central identity)
- No VPN Gateway *(only if a remote-work requirement card was drawn)*: **-3**

*(Ransomware consequences for missing backups come from the event cards themselves — see EVT-11.)*

**Examples:**
- Email, Web, Database, File, Domain Controller, Backup: 3+3+4+2+3+3 = **18 points** (good)
- The same plus VPN Gateway and a Honeypot: 18+2+1 = **21 points** (excellent)
- Email, Web, File, Domain, Backup but NO Database: 3+3+2+3+3 = 14, minus 10 = **4 points** (the penalty bites)

#### 4. RESILIENCE SCORE (0-25 points)
Ability to survive and recover from failures

**Resilience Factors:**

| Factor | Points | Criteria |
|--------|--------|----------|
| **Backup Server** | +8 | Can recover from ransomware/data loss |
| **Detection** | +7 | IDS/IPS/SIEM can spot attacks early |
| **Redundancy** | +5 | Duplicate server in the same role OR Load Balancer |
| **Isolation** | +3 | Network segmentation prevents spread |
| **Recovery Plan** | +2 | Has BOTH Backup Server and detection |

**Maximum Resilience Score: 25 points** (8+7+5+3+2 = 25)

**Penalties for Vulnerabilities (v2.2):**
- No Backup Server: **-10** (one disaster from catastrophe)
- Single point of failure (all critical services on one server): **-5**
- No detection capability: **-3**
- Flat network (no segmentation): **-2**

**Examples:**
- Backup + Detection + Segmentation + Redundancy: 8+7+3+5, +2 recovery plan = **25 points** (maximum; very resilient)
- Backup + Detection, flat network, no redundancy: 8+7+2−2 = **15 points** (adequate)
- No backup, no detection, flat network: −10−3−2 = **−15 points** (high risk; yes, scores go negative)

---

## Final Scoring Example

### Team A's Infrastructure (resilience-first)

**Built (total 46 of 50; 4 remaining):**
- Email Server (8): handles email
- Web Server (7): public website
- Database Server (10): customer data
- File Server (6): internal files
- Backup Server (9): disaster recovery
- Email Gateway (6): phishing defense

*Check: 8+7+10+6+9+6 = 46 ✓. No Domain Controller (too expensive; skipped for budget). Flat network.*

**Scoring Team A:**

**Security Score:**
- Email Gateway: +3
- Backup Server: +4
- No IDS/IPS/SIEM/Firewall/WAF/Honeypot/Segmentation: 0
- **Total: 7 points**

**Budget Score:**
- 4 budget remaining → 1-4 band
- **Total: 15 points**

**Capability Score:**
- Email +3, Web +3, Database +4, File +2, Backup +3 = 15
- No Domain Controller: −3
- **Total: 12 points**

**Resilience Score:**
- Backup Server: +8
- No detection: −3
- Flat network: −2
- **Total: 3 points**

**Team A Final Score: 7 + 15 + 12 + 3 = 37 points**

---

### Team B's Infrastructure (security-first, no backup)

**Built (total 47 of 50; 3 remaining):**
- Email Server (8)
- Web Server (7)
- Database Server (10)
- Domain Controller (12)
- IDS (10)

*Check: 8+7+10+12+10 = 47 ✓. No Backup Server (sacrificed for detection). Flat network.*

**Scoring Team B:**

**Security Score:**
- IDS: +5
- **Total: 5 points**

**Budget Score:**
- 3 left → 1-4 band
- **Total: 15 points**

**Capability Score:**
- Email +3, Web +3, Database +4, Domain Controller +3 = 13
- **Total: 13 points**

**Resilience Score:**
- Detection: +7
- No Backup Server: −10
- Flat network: −2
- **Total: −5 points (negative!)**

**Team B Final Score: 5 + 15 + 13 − 5 = 28 points**

**RESULT: Team A (37) beats Team B (28)**

**Lesson:** Having Backup is critical for resilience, even if it means fewer security devices.

---

## Competitive Play (2-4 Teams)

### Setup for Multiple Teams

**Each team:**
- Separate budget (50 tokens each at Standard)
- Separate infrastructure tracking sheet
- Separate score tracker

**Simultaneous Play:**
- All teams reveal the same requirement and event at the same time
- Teams take turns choosing actions (round-robin) OR all teams act simultaneously
- Simultaneous is faster; rotating turns allows player agency

### Scoreboard

**Track all teams' scores throughout game (illustrative):**

| Team | Sec | Budget | Cap | Res | TOTAL |
|------|-----|--------|-----|-----|-------|
| **Team A** | 8 | 20 | 12 | 5 | **45** |
| **Team B** | 12 | 15 | 18 | 10 | **55** |
| **Team C** | 5 | 10 | 8 | 2 | **25** |

**Winner:** Team with highest total score after the final turn

### Tie-Breaking

**If two teams tie:**
1. **First tiebreaker:** Security Score (defense is critical)
2. **Second tiebreaker:** Resilience Score (ability to survive matters)
3. **Third tiebreaker:** Capability Score (business requirement fulfillment)

---

## Random Elements & Replayability

### Requirement & Event Card Variability

**Each game is different because:**

1. **Card Order Randomized:** Shuffle both decks each game — a 5-7 turn game uses only 5-7 of the 20 requirements and 16 events
2. **Card Selection:** The Threat Orchestrator may curate the decks (see difficulty options on the card files)
3. **Consequence Ordering:** Early disasters force different choices than late surprises

**Example Game Flow Variations:**

**Game 1 (Tough Start):**
- Turn 1: Ransomware wave (REQ-12) → Must buy Backup + Detection early
- Turn 2: Budget cut (EVT-05) → Can't afford nice devices
- Turn 3: M&A integration (REQ-08) → Need more capacity
- Result: Teams forced into defensive posture

**Game 2 (Growth-Focused):**
- Turn 1: Product launch (REQ-01) → Need Web Server
- Turn 2: Data acquisition (REQ-02) → Need Database
- Turn 3: Emergency funds (EVT-06) → +10 budget!
- Result: Teams build bigger, more capable infrastructure

### Difficulty Levels (v2.2 — more budget = easier)

**Beginner Mode (Generous):**
- Starting Budget: **60**
- Kind decks (remove EVT-11 and REQ-12 before shuffling)
- Turn Limit: 7 (extra time)

**Standard Mode:**
- Starting Budget: **50**
- Random card draws
- Turn Limit: 6

**Advanced Mode (Challenging):**
- Starting Budget: **40** (tight budget)
- Harsh decks (remove EVT-06, EVT-07, EVT-16 — fewer breaks)
- Requirement penalties doubled
- Turn Limit: 5

---

## Example Full Game Walkthrough (6 Turns, Standard 50)

### TURN 1

**Phase 1: Business Requirement**
*TO flips card: "New Product Launch Website — need modern web server capability. If missing by end of Q1: -5 points."*

**Phase 2: Operational Event**
*TO flips card: "Emergency Funds! A surprise rebate arrives. +10 Budget (one time)."*

**Budget update: 50 + 10 = 60**

**Phase 3: Team Actions**
"We're deploying a Web Server to meet the launch requirement. Cost: 7 budget. Remaining: 53. We know we'll need a backup server eventually — holding the rest for now."

**Phase 4: End of Turn**
- Infrastructure: Web Server
- Budget: 53

---

### TURN 2

**Phase 1: Business Requirement**
*"Customer Data Acquisition — must have a functioning Database by end of Q2 or lose 10 points."*

**Phase 2: Operational Event**
*"Email Server Failure — pay 5 budget for emergency repair OR skip and lose 10 points."*

The team has no email server, so the TO rules the event inert — there's nothing to break. *(TO tip: when an event targets a component the team doesn't own, it fizzles — but it's a great moment to point at the capability gap.)*

**Phase 3: Team Actions**
"We're deploying a Database Server (10 budget) to handle the acquisition — that's critical. The failure event doesn't apply to us, so no repair cost. Total this turn: 10. Remaining: 43."

**Infrastructure:** Web Server, Database Server
**Budget:** 43

---

### TURN 3

**Phase 1: Business Requirement**
*"Ransomware Wave in Sector — you need Backup AND Detection capability OR lose 20 points."*

**Phase 2: Operational Event**
*"Vendor Promotion — next security device this turn costs 2 less."*

**Phase 3: Team Actions**
"Critical quarter. We're deploying:
- Backup Server (9 budget)
- IDS at the promo discount (10 − 2 = 8 budget)
That satisfies the ransomware requirement. We'll also grab a Cloud Workload (4) for future flexibility. Total: 21 budget. Remaining: 22."

**Infrastructure:** Web, Database, Backup, IDS, Cloud Workload
**Budget:** 22

---

### TURN 4

**Phase 1: Business Requirement**
*"Work-From-Home Program — need remote access capability. Missing: -3 points."*

**Phase 2: Operational Event**
*"IT Staff Burnout — you may deploy at most ONE component this turn."*

**Phase 3: Team Actions**
"We need remote access, and burnout limits us to one deployment. VPN Gateway it is (9 budget). Remaining: 13."

**Infrastructure:** Web, Database, Backup, IDS, Cloud, VPN Gateway
**Budget:** 13

---

### TURN 5

**Phase 1: Business Requirement**
*"Cyber-Insurance Renewal — Backup + Email Gateway + detection: +5 points if all present, -5 if not."*

**Phase 2: Operational Event**
*"Hardware Recall — pick an on-prem server: pay 3 budget or it's offline this quarter."*

**Phase 3: Team Actions**
"We deploy an Email Gateway (6 budget) — with our Backup and IDS that completes the insurance checklist: +5 points. For the recall we pay 3 to keep the Database Server online (it's load-bearing). Total: 9. Remaining: 4."

**Infrastructure:** Web, Database, Backup, IDS, Cloud, VPN Gateway, Email Gateway
**Budget:** 4

---

### TURN 6 (Final Turn)

**Phase 1: Business Requirement**
*"Single Sign-On Rollout — must have a Domain Controller OR lose 5 points."*

**Phase 2: Operational Event**
*"Quiet Quarter — no incident."*

**Phase 3: Team Actions**
"A Domain Controller costs 12; we have 4. We can't buy it. We pass and take the -5 penalty."

**Final Infrastructure & Budget Check:**
- Web Server (7)
- Database Server (10)
- Backup Server (9)
- IDS (10, paid 8 with promo)
- Cloud Workload (4)
- VPN Gateway (9)
- Email Gateway (6)
- Recall fee (3)
- **Total spent: 7+10+9+8+4+9+6+3 = 56 of 60 available (50 start + 10 windfall)**
- **Final Budget: 4 remaining ✓**

---

## FINAL SCORING (Walkthrough Team)

**Security Score:**
- IDS: +5
- Email Gateway: +3
- Backup Server: +4
- **Total: 12 points**

**Budget Score:**
- 4 remaining → 1-4 band
- Missed only 1 requirement (no halving)
- **Total: 15 points**

**Capability Score:**
- Web +3, Database +4, Backup +3, VPN +2, Cloud +2 = 14
- No Email service: −5 *(an Email Gateway is a security device — it filters mail, it doesn't host mailboxes; they never deployed an Email Server or cloud email)*
- No Domain Controller: −3
- **Total: 6 points**

**Resilience Score:**
- Backup Server: +8
- Detection (IDS): +7
- Recovery Plan (backup + detection): +2
- Flat network: −2
- **Total: 15 points**

**Requirement/Event adjustments:**
- Turn 5 insurance bonus: +5
- Turn 6 missed SSO requirement: −5

**FINAL SCORE: 12 + 15 + 6 + 15 + 5 − 5 = 48 points**

**Lesson:** This team survived the ransomware quarter and kept every event in check — but never bought email or identity. Detection and backups scored well; missing core business services bled capability points all game.

---

## Variations & House Rules

### Overload Servers (v2.2 — now a STANDARD rule, not a variation)
Servers may exceed capacity at **+1 Budget per extra service**. This is the same rule as the Network Building module.
- Example: 3 services on a 2-capacity server costs +1 budget
- Trade-off: cheaper than a new server now, but overloaded servers are recorded risks (single point of failure; events and later modules punish them)

### Variation 1: "Upgrade Existing"
**Optional Rule:** Allow teams to upgrade servers already deployed (swap for a better one, pay the difference).
- Example: Replace File Server (6) with Domain Controller (12) — pay 6, keep the hosted services
- Creates flexibility but adds complexity

### Variation 2: "Disaster Strikes Mid-Game"
**Optional Rule (High Difficulty):** If EVT-11 (Ransomware Strikes) is drawn and the team has NO Backup Server, they take the -20 immediately AND must deploy a Backup Server by the end of the next turn (mandatory).
- Creates an urgent decision point
- Teaches that failures have compounding consequences

### Variation 3: "Tech Debt"
**Optional Rule:** Each Legacy System deployed costs 1 extra budget per turn to maintain (not paid upfront).
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
6. **"If this network gets attacked (Incident Response module), which vulnerabilities do you see?"**

### Competitive Reflection

7. **"Why did Team X score higher? What did they do differently?"**
8. **"What was the winning strategy?"**

---

## Quick Reference Sheets

### Scoring Summary (1 page)

```
NETWORK BUILDING STANDALONE SCORING (v2.2)

SECURITY SCORE (max 30):
  IDS or IPS: +5 | SIEM: +5 | Firewall: +4 | Backup: +4
  Email Gateway: +3 | WAF: +3 | Honeypot: +3 | Segmentation: +3

BUDGET SCORE (max 20) — smart utilization, not hoarding:
  5-15 left: 20 | 1-4 left: 15 | 0 left: 10 | 16-25 left: 10 | 26+ left: 5
  Missed 2+ requirements? Halve it (round down).

CAPABILITY SCORE (max 25):
  Email: +3 | Web: +3 | Database: +4 | File: +2 | Domain: +3
  Dev: +2 | Backup: +3 | VPN: +2 | Cloud: +2 | Honeypot: +1
  Penalties: no Email -5 | no Database -10 | no DC -3
             no VPN (if remote-work card drawn) -3

RESILIENCE SCORE (max 25):
  Backup: +8 | Detection: +7 | Redundancy: +5 | Segmentation: +3
  Recovery Plan (Backup AND Detection): +2
  Penalties: no Backup -10 | single point of failure -5
             no Detection -3 | flat network -2

FINAL = Security + Budget + Capability + Resilience
        − requirement/event penalties (+ bonuses)
```

### Component Quick Reference

```
SERVERS (Cost / Capacity / Security Profile):
  Email (8/1/Low) | Web (7/1/Low) | Database (10/1/Med)
  File (6/2/Low) | Domain (12/2/Med) | Dev (5/3/Low)
  Backup (9/1/High) | Cloud (4/2/Med) | Legacy (3/1/VLow) | Honeypot (7/1/Med)
  Overload: +1 Budget per service beyond capacity

SECURITY DEVICES (Cost — benefit):
  Firewall (12 — zone control) | IDS (10 — detection) | IPS (14 — detection+blocking)
  Email Gateway (6 — anti-phishing) | WAF (11 — web app defense)
  SIEM (15 — detection+logging) | Segmentation Switch (10 — isolation)
  VPN Gateway (9 — remote access) | Load Balancer (8 — redundancy)
  Honeypot Network (8 — detection/deception)
```

---

## Ready for Play!

This is a complete, standalone 30-45 minute competitive mini-game.

**To run a session:**
1. Print server and device cards (`cards/network-building/core-deck/`)
2. Print the requirement and event decks (`cards/network-building/standalone/`)
3. Give each team a budget tracker
4. Run 5-7 turns (4-5 min each, per difficulty)
5. Calculate final scores
6. Declare winner
7. 10-minute debrief

---

## v2.2 Playtest Edition Changes

Summary of changes for playtesters:

1. **Difficulty labels unified with the module:** Beginner 60 / Standard 50 / **Advanced** 40 (was "Hard"). More budget = easier.
2. **Any-number actions (v2.2):** Phase 3 now allows any number of deployments per turn, matching the module rules; the old "one action" wording contradicted the game's own walkthrough.
3. **Real card decks:** Business Requirements (20 cards, REQ-01..REQ-20) and Operational Events (16 cards, EVT-01..EVT-16) now exist as printable files in `cards/network-building/standalone/`; inline example lists replaced by references to them.
4. **Budget Score redefined around smart utilization:** the table now rewards finishing with a 5-15 token contingency reserve and no longer rewards hoarding (the old table gave 20 points for 40+ unspent, while the examples assumed the opposite). Anti-hoarding check added.
5. **Scoring tables recomputed:** Security items now sum to the stated max 30; Capability items sum to 25 (Honeypot +1 added — it was in an example but missing from the table); Resilience factors sum to 25 and penalties were rebalanced (no Backup −10). All worked examples now add up.
6. **Worked examples rebuilt:** Team A (37) and Team B (28) are clean, verified builds; the 6-turn walkthrough's budget ledger reconciles (56 spent of 60 available, 4 left, score 48). All AI drafting scratch-work removed.
7. **Overload is standard:** +1 Budget per extra service beyond capacity — same rule as the module.
8. **Terminology:** "VPN Gateway" (was VPN Concentrator), "Backup Server" (was Backup System); device "+1 stat" effects replaced with plain-language benefits tied to the scoring categories.
9. **Component costs verified** against the module rules (the canonical source): servers 3-12, devices 6-15.

---

*Incident Zero: Network Building Standalone Mini-Game*
*Infrastructure design competition with multi-dimensional scoring*
*v2.2 - Playtest Edition*
