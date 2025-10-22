# Incident Zero: Compliance Audit Standalone Mini-Games
## Three Variations of Security Assessment Gameplay

---

## Overview

**Compliance Audit Standalone** offers **three distinct game modes** that can be played independently:

1. **Variation A: Pre-Built Networks** (15-25 minutes) - Audit existing networks
2. **Variation B: Random Network Generation** (25-35 minutes) - Generate network, then audit
3. **Variation C: Audit the Auditor Debate** (20-30 minutes) - Interactive audit challenge

**Common Theme:** Teams understand how audits find vulnerabilities that attackers will exploit.

**Best For:**
- Standalone 20-35 minute sessions
- Teaching audit frameworks
- Understanding security gaps
- Before/after comparison with Attack Chain (Phase 1)
- Competitive assessment skills

---

# VARIATION A: PRE-BUILT NETWORKS
## "Audit the Sample Networks"

**Duration:** 15-25 minutes  
**Players:** 1-4 teams  
**Difficulty:** Easy (low cognitive load)  
**Best For:** Quick session, first-time audit introduction

---

## Concept

**"Three organizations have submitted their infrastructure for audit. Review each one and score their security posture. Which has the best design? Which is most vulnerable?"**

Teams receive 3 pre-built network descriptions and audit them against a 6-domain framework. Compare results and discuss why vulnerabilities matter.

---

## Game Materials

### Pre-Built Sample Networks (3 total)

#### SAMPLE NETWORK 1: "StartUp Tech"
```
INFRASTRUCTURE DESCRIPTION:

Startup Tech is a 50-person web development company.
Cloud-first approach, minimal on-premises systems.

DEPLOYMENT:
- Web Server (Cloud - AWS): Hosts company website and app portal
- Database Server (Cloud - AWS RDS): Customer data, 100K records
- Development Server (Cloud - AWS EC2): Dev/test environment
- Domain Controller (On-Prem): AD for user identity (1 small server)
- File Server (On-Prem): Shared documents
- Email Server (Cloud - Microsoft 365): Email via SaaS provider

SECURITY DEVICES:
- Email Gateway: None (using Microsoft 365 default)
- Firewall: AWS Security Groups (cloud provider native)
- IDS/IPS: None
- SIEM: None
- WAF: None
- Backup: AWS automated snapshots + Microsoft 365 retention
- VPN: None (all cloud-native, no remote access needed)

NETWORK ARCHITECTURE:
- Hybrid (50% Cloud, 50% On-Prem)
- Cloud systems accessible via internet (all public IP)
- On-prem systems on isolated LAN
- No network segmentation between cloud and on-prem

HOSTING:
- 50% AWS (web, database, dev)
- 50% On-Premises (AD, file sharing)

SECURITY POSTURE:
- No perimeter firewall monitoring
- Cloud infrastructure: AWS default security (basic)
- On-prem infrastructure: Minimal controls
- Identity: Single AD instance (critical point)
- No incident detection
- Backups functional but not tested
```

#### SAMPLE NETWORK 2: "Mid-Market Corp"
```
INFRASTRUCTURE DESCRIPTION:

Mid-Market Corp is a 200-person financial services company.
Balanced on-premises and cloud, mature IT operations.

DEPLOYMENT:
- Email Server (On-Prem): Exchange 2019
- Web Server (Cloud - Azure): Public website + customer portal
- Database Server (On-Prem): SQL Server, customer data, 1M records
- File Server (On-Prem): Network file shares, active collaboration
- Domain Controller (On-Prem): AD + LDAP, 200 users
- Development Server (Cloud - Azure): Dev/test
- Backup System (On-Prem): Backup appliance, off-site replication
- Legacy System (On-Prem): 15-year-old accounting system

SECURITY DEVICES:
- Firewall: Cisco ASA (perimeter) + internal segmentation firewall
- Email Gateway: Proofpoint (phishing/malware filter)
- IDS: Suricata (network-based detection)
- IPS: None (IDS only)
- SIEM: Splunk (centralized logging)
- WAF: AWS WAF (in front of web server)
- VPN: Cisco AnyConnect (remote access)
- Honeypot: None

NETWORK ARCHITECTURE:
- Segmented (3 zones: DMZ, Internal, Finance)
- Firewalls enforce zone boundaries
- On-prem systems segregated from cloud
- Cloud systems on private network (not public internet)

HOSTING:
- 40% On-Premises (core business systems)
- 60% Cloud (web, dev, supplementary)

SECURITY POSTURE:
- Perimeter monitoring active (IDS)
- Email filtering active
- Centralized logging (SIEM)
- Remote access controlled (VPN)
- Backup and recovery tested
- Legacy system isolated but unpatched
```

#### SAMPLE NETWORK 3: "Enterprise Bank"
```
INFRASTRUCTURE DESCRIPTION:

Enterprise Bank is a 1000+ person financial institution.
Highly regulated (PCI-DSS, HIPAA), on-premises focused.

DEPLOYMENT:
- Email Server (On-Prem): Custom hardened system + redundancy
- Web Server (Cloud/Hybrid): DMZ layer for customer portal
- Database Server (On-Prem): Oracle RAC, 500M+ records, air-gapped
- File Server (On-Prem): Multiple redundant file servers by department
- Domain Controller (On-Prem): Multiple DCs, LDAP + Kerberos, hardened
- Development Server (On-Prem): Isolated dev network, no access to prod
- Backup System (On-Prem): Multiple backup systems, offline vault, geographically distant
- Cloud Workload (Limited): Only non-sensitive workloads

SECURITY DEVICES:
- Firewall: Multiple Palo Alto networks (perimeter + internal + cloud boundary)
- Email Gateway: Proofpoint + internal inspection
- IDS: Multiple IDS systems (network + host-based)
- IPS: Palo Alto IPS (active blocking)
- SIEM: Splunk + IBM QRadar (redundant)
- WAF: F5 WAF (multi-layer)
- VPN: Multiple VPN concentrators, MFA required
- Honeypot: Internal honeypot network (3 decoy systems)
- Network Segmentation: Microsegmentation between critical systems
- Intrusion Prevention: Advanced threat prevention

NETWORK ARCHITECTURE:
- Fully Isolated (10+ security zones)
- Each zone has firewall enforcement
- Zero-trust network access
- Air-gapped critical systems
- Private clouds only (no public internet access)

HOSTING:
- 95% On-Premises (regulatory requirement)
- 5% Cloud (non-critical, isolated)

SECURITY POSTURE:
- Comprehensive logging (multiple SIEM)
- Advanced threat detection (IDS/IPS + honeypot)
- Incident response ready
- Backup and recovery tested quarterly
- All systems hardened per NIST guidelines
- Compliance audited annually (PCI-DSS, SOX)
```

---

## Audit Assessment Framework

### The 6-Domain Audit

Teams assess each network using this framework:

#### **Domain 1: Network Segmentation**
**Question:** "Are critical systems isolated?"

| Score | Criteria |
|-------|----------|
| **PASS** | Firewall between zones OR microsegmentation active |
| **FAIL** | Flat network OR segmentation without enforcement |

#### **Domain 2: Access Control & Identity**
**Question:** "Is identity management secure?"

| Score | Criteria |
|-------|----------|
| **PASS** | Dedicated Domain Controller, MFA for remote access, minimal over-privilege |
| **FAIL** | No DC OR DC overloaded OR no MFA OR broad admin access |

#### **Domain 3: Incident Detection & Response**
**Question:** "Can you detect attacks?"

| Score | Criteria |
|-------|----------|
| **PASS** | IDS/IPS OR SIEM deployed |
| **FAIL** | No IDS/IPS AND no SIEM |

#### **Domain 4: Backup & Disaster Recovery**
**Question:** "Can you recover from failure?"

| Score | Criteria |
|-------|----------|
| **PASS** | Backup system deployed + tested + geographically diverse |
| **FAIL** | No backup OR untested backup OR single location |

#### **Domain 5: Third-Party Risk Management**
**Question:** "Are cloud/vendor systems managed?"

| Score | Criteria |
|-------|----------|
| **PASS** | Cloud systems isolated OR not handling critical data |
| **FAIL** | Cloud systems on internet + handling sensitive data + no WAF |

#### **Domain 6: Security Operations & Monitoring**
**Question:** "Do you have centralized visibility?"

| Score | Criteria |
|-------|----------|
| **PASS** | SIEM deployed + centralized logging active |
| **FAIL** | No SIEM OR no centralized logging |

---

## Gameplay (20-25 minutes)

### Turn Structure

#### **Phase 1: Introduction (2 minutes)**

**TO explains:**
"You're security auditors reviewing three organizations' infrastructure designs. For each, you'll score them on a 6-domain framework. Your goal: Identify which has the strongest security posture and which is most vulnerable."

#### **Phase 2: Audit Each Network (5 minutes per network = 15 minutes)**

**For each network (Startup, Mid-Market, Enterprise):**

1. **TO reads network description** (2 minutes)
2. **Teams discuss and score** (2 minutes)
   - Vote on PASS/FAIL for each domain
   - Record scores on audit worksheet
3. **TO reveals "correct" audit** (1 minute)
   - Teams compare their assessment to expert audit
   - Discuss differences

#### **Phase 3: Comparative Analysis (5 minutes)**

**Teams answer:**
1. "Which organization is most secure?"
2. "Which is most vulnerable to attack?"
3. "If you HAD to use one network, which would you choose?"

---

## Pre-Built Audit Results

### Startup Tech - Audit Results

| Domain | Score | Finding |
|--------|-------|---------|
| Network Segmentation | **FAIL** | No firewall between cloud and on-prem; cloud accessible from internet |
| Access Control | **PASS** | AD in place; but overloaded (also acts as SIEM?) |
| Detection | **FAIL** | No IDS/IPS or SIEM |
| Backup & Recovery | **PASS** | AWS snapshots + M365 retention |
| Third-Party Risk | **FAIL** | Cloud systems public internet-accessible |
| Operations | **FAIL** | No centralized monitoring |

**Score: 2/6 PASS**

**Risk Rating: HIGH**
- **Vulnerabilities:** No network segmentation, no detection capability, cloud systems exposed
- **Attack Scenario:** Attacker compromises cloud web server → lateral movement to on-prem AD → full network access
- **Cost of Breach:** Very high (no detection, no segmentation to contain)

---

### Mid-Market Corp - Audit Results

| Domain | Score | Finding |
|--------|-------|---------|
| Network Segmentation | **PASS** | Firewalls between DMZ, Internal, Finance zones |
| Access Control | **PASS** | AD hardened, VPN with MFA |
| Detection | **PASS** | IDS active + SIEM deployed |
| Backup & Recovery | **PASS** | Backup appliance with off-site replication |
| Third-Party Risk | **PASS** | Cloud systems on private network, WAF in place |
| Operations | **PASS** | SIEM + centralized logging |

**Score: 5/6 PASS** (only concern: no IPS, Legacy system unpatched)

**Risk Rating: MEDIUM**
- **Strengths:** Good segmentation, detection, logging, backups
- **Weaknesses:** Legacy accounting system (vulnerable but isolated)
- **Attack Scenario:** Attacker may get into DMZ but segmentation blocks lateral movement; detection catches lateral movement attempt
- **Cost of Breach:** Moderate (good detection and segmentation limit damage)

---

### Enterprise Bank - Audit Results

| Domain | Score | Finding |
|-------|-------|---------|
| Network Segmentation | **PASS** | Microsegmentation between all critical systems |
| Access Control | **PASS** | Hardened DCs, MFA, minimal over-privilege |
| Detection | **PASS** | IDS/IPS + dual SIEM + honeypot |
| Backup & Recovery | **PASS** | Multiple offline vaults, quarterly testing |
| Third-Party Risk | **PASS** | Cloud only for non-critical, extensive monitoring |
| Operations | **PASS** | Dual SIEM, air-gapped logging |

**Score: 6/6 PASS**

**Risk Rating: LOW**
- **Strengths:** Defense-in-depth across all domains
- **Weaknesses:** Very expensive to operate; regulatory complexity
- **Attack Scenario:** Multiple layers would have to be bypassed; honeypot would alert SOC immediately
- **Cost of Breach:** Lower (but incident response costs are high due to complexity)

---

## Scoring & Comparison

### Audit Score Tiers

| Score | Assessment | Implication |
|-------|-----------|-------------|
| **6/6 PASS** | Enterprise-grade | Highest security, highest cost |
| **5/6 PASS** | Strong security | Balanced security & cost |
| **3-4/6 PASS** | Adequate but gapped | Risk exposure present |
| **Below 3/6** | High risk | Vulnerabilities likely exploited |

### Team Competition

**Which team's audit assessment was most accurate?**
- Teams that scored Startup as high-risk: +1 point
- Teams that scored Enterprise as low-risk: +1 point
- Teams that identified Legacy System as Mid-Market's weakness: +1 point

**Winner:** Team with most accurate audit assessments

---

## Debrief (5 minutes)

### Discussion Questions

1. **"Why would Startup Tech be attractive to attackers?"**
   - Answer: No detection, no segmentation, cloud exposed

2. **"If you had to recommend improvements to Startup, what's priority #1?"**
   - Answer: Network segmentation OR IDS/SIEM (detection)

3. **"Why is Enterprise Bank so expensive?"**
   - Answer: Redundancy, microsegmentation, multiple layers of defense

4. **"Which organization would you actually want to work for?"**
   - Answer: Mid-Market (good balance of security and usability)

---

# VARIATION B: RANDOM NETWORK GENERATION
## "Build-Then-Audit Mini-Game"

**Duration:** 25-35 minutes  
**Players:** 1-4 teams  
**Difficulty:** Medium (requires both building and auditing)  
**Best For:** Combined learning, deeper understanding

---

## Concept

**"Each team builds a simplified network by drawing random infrastructure cards. Then you audit each other's networks. Better auditors find more gaps."**

This combines elements of Network Building (simplified) with Audit mechanics. Teams make trade-off decisions, then their network design is audited by competitors.

---

## Game Flow

### Phase 1: Rapid Network Generation (10 minutes)

**Each team builds a network using a simplified card deck:**

#### Simplified Network Generation Cards

**SERVER CARDS (Draw 5 cards, must include certain types):**
- Email Server (must have)
- Web Server (must have)
- Database Server (must have)
- Domain Controller (should have)
- Backup System (optional)
- Development Server (optional)
- File Server (optional)
- Cloud Workload (optional)

**SECURITY DEVICE CARDS (Draw 3 cards, choose to deploy or skip):**
- Firewall
- IDS
- SIEM
- Email Gateway
- WAF
- Honeypot

**ARCHITECTURE CARD (Draw 1, determines layout):**
- Flat Network (budget-friendly, weak)
- Segmented Network (balanced)
- Fully Isolated (expensive, strong)

**Rules:**
- Must have: Email, Web, Database
- Can choose: Others
- Budget: Implicit (each card represents a choice; no money tracking)
- Time: 10 minutes to decide and document on "Network Card"

**Each team creates a Network Card:**
```
TEAM A'S NETWORK:

SERVERS:
✓ Email Server
✓ Web Server
✓ Database Server
✓ Domain Controller
✓ Backup System
✓ File Server
✗ Development Server (skipped)

SECURITY DEVICES:
✓ Firewall
✓ IDS
✗ SIEM (skipped)
✓ Email Gateway
✗ WAF (skipped)
✗ Honeypot (skipped)

ARCHITECTURE:
→ Segmented (3 zones)
```

### Phase 2: Cross-Team Audit (15 minutes)

**Each team audits a different team's network (round-robin):**

1. **Auditing Team Receives Network Card**
2. **Auditing Team Scores Network on 6 Domains**
   - PASS or FAIL for each domain
   - Write findings
3. **Present Audit Results to Building Team**

**Example Audit of Team A:**

```
AUDIT OF TEAM A'S NETWORK:

Domain 1: Network Segmentation
  Decision: Segmented (3 zones) → PASS
  Finding: Good segmentation between DMZ, Internal, Sensitive

Domain 2: Access Control
  Decision: Domain Controller present → PASS
  Finding: Identity management in place

Domain 3: Detection
  Decision: IDS present but NO SIEM → PARTIAL FAIL
  Finding: Can detect network attacks but no centralized logging for correlation

Domain 4: Backup & Recovery
  Decision: Backup System present → PASS
  Finding: Can recover from data loss

Domain 5: Third-Party Risk
  Decision: No WAF on Web Server → FAIL
  Finding: Web server vulnerable to application attacks

Domain 6: Operations
  Decision: No SIEM → FAIL
  Finding: No centralized monitoring; incident response slower

AUDIT SCORE: 3/6 PASS

CRITICAL FINDINGS:
1. Missing SIEM (no centralized logging)
2. No WAF (web server unprotected)
3. IDS without SIEM (detection blindspot)
```

### Phase 3: Auditor Scoring (5 minutes)

**Accuracy of Audits is Scored:**

| Audit Accuracy | Points |
|---|---|
| Identified all major gaps | +5 |
| Identified some gaps | +3 |
| Missed critical gap | -2 |
| Incorrect assessment | 0 |

**Team Scores:**
- **Building Teams:** Score = (6 - number of fails) × 5
  - Example: 3/6 PASS = 3 fails → 3 × 5 = 15 points
- **Auditing Teams:** Score = accuracy of audit assessment

**Winner:** Highest combined score OR winner of each category

---

## Debrief (5 minutes)

1. **"What gaps did auditors find in your network?"**
2. **"Did the auditors miss anything you're concerned about?"**
3. **"What would you fix if you had to improve?"**

---

# VARIATION C: "AUDIT THE AUDITOR" DEBATE
## Interactive Challenge & Discussion Game

**Duration:** 20-30 minutes  
**Players:** 2-4 teams  
**Difficulty:** High (requires critical thinking & argumentation)  
**Best For:** Advanced teams, strong discussion-based learning

---

## Concept

**"You're given a network design and audit findings. As a team, debate whether the auditor's findings are FAIR, HARSH, or MISSING SOMETHING. Win by making the most convincing argument."**

This is a **debate game** where teams argue the merits of audit findings, teaching that audits are interpretable and that defending infrastructure requires understanding the rationale.

---

## Game Materials

### Audit Finding Scenarios (3 total)

#### SCENARIO 1: "The Startup Defense"
```
SCENARIO:
Startup Tech built this network:
- Email (Cloud), Web (Cloud), Database (Cloud), 
  Domain Controller (On-Prem), Backup (Cloud snapshots)
- No Firewall between cloud and on-prem
- No IDS or SIEM
- Accessing cloud systems requires VPN

AUDITOR'S FINDINGS:
Domain 1: Network Segmentation → FAIL
  "No firewall between cloud and on-prem represents 
   uncontrolled lateral movement risk."

Domain 2: Detection → FAIL
  "No IDS/SIEM means attacks go undetected."

OVERALL: HIGH RISK

STARTUP'S COUNTERARGUMENT:
"We use cloud providers (AWS/Azure) which have built-in
firewalls at the cloud level. Our VPN requirement means
only authenticated users can access systems. Our small
team (20 people) means we're faster to respond. This
audit is too harsh for a startup."

YOUR JOB:
- Is the auditor FAIR? (reasonable standards)
- Is the auditor HARSH? (too strict for context)
- Is the auditor MISSING gaps? (what should they have found?)
- Vote: Fair / Harsh / Missing / Balanced
```

#### SCENARIO 2: "The Legacy System Dilemma"
```
SCENARIO:
Mid-Market Corp has this system:
- 15-year-old Accounting System (on-prem)
- Runs on Windows Server 2003 (unsupported, unpatched)
- Handles $2B in transactions annually
- Cannot be replaced for 2+ years (licensing/training)
- Isolated on separate network segment but bridged for 
  month-end consolidation

AUDITOR'S FINDINGS:
Domain 2: Access Control → FAIL
  "Legacy system runs on unsupported OS. Vulnerability 
   present = critical risk."

Domain 4: Backup & Recovery → PARTIAL
  "System backed up but no tested recovery procedure."

OVERALL: CRITICAL RISK (specifically legacy system)

CORP'S COUNTERARGUMENT:
"The system is air-gapped except for 3 days per month.
We have detective controls (IDS) watching for suspicious 
access. The cost of replacement ($2M) is greater than 
our risk tolerance. This system is a known risk we're 
accepting."

YOUR JOB:
- Is the auditor RIGHT to flag this?
- Is the corporation taking reasonable risk?
- How would you rate this scenario? Risk Acceptance vs. Negligence?
- Vote: Auditor Correct / Corp Reasonable / Need More Controls / Acceptable Risk
```

#### SCENARIO 3: "The Over-Engineering Question"
```
SCENARIO:
Enterprise Bank built this network:
- 10+ security zones with microsegmentation
- Dual SIEM systems (Splunk + QRadar)
- IDS + IPS on every zone
- Honeypot network with decoys
- All systems hardened per NIST
- Quarterly disaster recovery testing
- Air-gapped offline backups in vault
- Annual compliance audit (PCI-DSS, SOX)

COST: $5M annual IT security budget

AUDITOR'S FINDINGS:
Domain 1-6: ALL PASS ✓

AUDITOR'S COMMENT:
"Exceptional security posture. Well-engineered 
defense-in-depth. Highly resilient. Recommended 
best practices for financial institution."

STAKEHOLDER QUESTION:
"Is this over-engineered? Could we achieve 80% 
of the security with 30% of the cost?"

YOUR JOB:
- Is defense-in-depth always justified?
- What's the cost-benefit breakpoint?
- For different organization types (startup vs. bank), 
  what's appropriate?
- Vote: Over-Engineered / Justified / Right for Context / Too Expensive
```

---

## Gameplay (25-30 minutes)

### Turn Structure

#### **Phase 1: Present Scenario (3 minutes)**

**TO reads:**
1. Organization and network design
2. Auditor's findings
3. Organization's counterargument
4. Debate question

#### **Phase 2: Debate Preparation (5 minutes)**

**Each team gets assigned a position:**
- **Team A:** Defend the Auditor (findings are fair/necessary)
- **Team B:** Defend the Organization (counterargument is valid)
- **Team C:** Play Neutral Assessor (judge fairness of both)

**Teams prepare arguments:**
- 2-3 key points supporting their position
- Anticipate opponent's counterarguments
- Use security/business logic

#### **Phase 3: Debate Round (5 minutes)**

**Structure:**
1. **Auditor Position:** 1 minute opening (Team A)
2. **Organization Position:** 1 minute opening (Team B)
3. **Cross-Examination:** 2 minutes (back-and-forth)
4. **Neutral Assessment:** Team C (judge who had better argument)

#### **Phase 4: Judge's Decision & Scoring (2 minutes)**

**Team C Scores:**
- **Most convincing argument:** +3 points
- **Better use of logic:** +2 points
- **Anticipated counterarguments:** +2 points
- **Clearer presentation:** +1 point

**Repeat for each scenario (3 scenarios = 3 rounds)**

---

## Example Debate

### SCENARIO 1: Startup Defense

**AUDITOR POSITION (Team A):**
"The findings are fair because:
1. Network security standards apply to all organizations
2. Cloud provider firewalls don't replace organizational controls
3. No IDS means breaches go undetected for weeks
4. A $10M breach destroys a startup; prevention is essential"

**ORGANIZATION POSITION (Team B):**
"The counterargument is valid because:
1. Startups operate under different constraints than enterprises
2. We use VPN (authentication) to control access
3. Our cloud provider has better security than we could build
4. For 20 employees, a $50K security investment is proportional
5. We're risk-accepting; this is a known trade-off"

**CROSS-EXAMINATION (back and forth):**

**A:** "But if you get compromised, your customer data is exposed. Isn't that a problem?"

**B:** "Yes, but our VPN AND cloud provider AND limited data make that less likely than you're suggesting."

**A:** "What about detection? If you're breached, you won't know for months."

**B:** "True, but adding SIEM costs $5K/month that we don't have. We're choosing early detection (IDS) instead of centralized logging."

**C (NEUTRAL):** "Who made the better argument?"
- Team A cited industry standards
- Team B cited resource constraints
- Both had merit

**VERDICT:** Team B made slightly more convincing argument (better contextualization of risk)
- Team B: +3 points
- Team A: +2 points

---

## Debate Scoring & Winner

**After 3 scenarios:**

| Team | Scenario 1 | Scenario 2 | Scenario 3 | TOTAL |
|------|-----------|-----------|-----------|-------|
| **Team A (Auditor)** | 2 | 3 | 2 | 7 |
| **Team B (Organization)** | 3 | 2 | 2 | 7 |
| **Team C (Neutral)** | 3 | 2 | 3 | 8 |

**Winner:** Team C (Neutral Assessor)

**Award:** "Best Critical Thinking"

---

## Debrief (5 minutes)

### Key Learning Questions

1. **"Are all audit findings equally valid?"**
   - Answer: No; context matters (startup vs. bank)

2. **"How would you defend an audit finding to the board?"**
   - Teaching point: Audits need business justification, not just technical standards

3. **"What's the difference between a 'critical finding' and a 'risk we're accepting'?"**
   - Teaching point: Risk management is nuanced; not all gaps are equally important

4. **"How does this change how you think about Phase 1 attacks?"**
   - Connection: "Auditors find gaps that attackers exploit"

---

# USING ALL THREE VARIATIONS

## Which Variation When?

### Variation A: Pre-Built Networks (Quickest)
**Use When:**
- Limited time (< 30 min session)
- First exposure to audit concepts
- Want to compare different infrastructure strategies
- Non-competitive, educational focus

**Learning Value:**
- Understand how audit domains work
- See difference between good/bad designs
- Low setup time

### Variation B: Random Generation (Balanced)
**Use When:**
- Want to combine building + auditing
- 30-40 minute session
- Teams benefit from designing then being audited
- Competitive element desired

**Learning Value:**
- Teams make trade-off decisions
- See consequences of choices reflected in audit
- "This gap I chose to accept was exactly what the auditor found!"

### Variation C: Debate Game (Most Interactive)
**Use When:**
- Advanced/experienced teams
- Want deep critical thinking
- Discussion-based learning preferred
- Comfortable with argumentation/debate format

**Learning Value:**
- Audit findings are interpretable
- Context matters (startup vs. bank)
- Security decisions involve trade-offs
- Preparation for defending security to board/leadership

---

# SAMPLE PLAY SESSIONS

---

## Session 1: Pre-Built Networks Only (20 minutes)

```
Setup: 3 min
Audit Startup Tech: 4 min
Audit Mid-Market: 4 min
Audit Enterprise: 4 min
Comparison & Discussion: 3 min
Debrief: 2 min

Total: 20 minutes
```

**Perfect for:** Intro to audit concepts

---

## Session 2: Random Generation + Audit (35 minutes)

```
Setup: 3 min
Teams build networks (simplified): 10 min
Teams audit each other: 15 min
Score & announce winner: 3 min
Debrief: 4 min

Total: 35 minutes
```

**Perfect for:** Combined learning, competitive

---

## Session 3: Debate Game Intensive (30 minutes)

```
Setup & brief: 2 min

SCENARIO 1:
- Presentation: 1 min
- Prep: 3 min
- Debate: 5 min
- Scoring: 1 min
- Subtotal: 10 min

SCENARIO 2: 10 min
SCENARIO 3: 10 min

Debrief: 3 min

Total: 30 minutes
```

**Perfect for:** Advanced critical thinking

---

## Session 4: Combination Play (60 minutes)

```
Variation A (Pre-Built): 20 min
- Understand audit domains via 3 sample networks

Variation B (Random Gen): 25 min
- Build network, get audited
- See your choices reflected in audit findings

Variation C (Debate): 10 min
- Single debate scenario to reinforce learning

Debrief & Connection: 5 min
- "Now you understand how audits work"
- "In Phase 1, attackers will exploit these gaps"

Total: 60 minutes
```

**Perfect for:** Comprehensive audit education

---

# CONNECTING TO ATTACK CHAIN (Phase 1)

After playing Audit Standalone, teams can transition to Phase 1 (Attack Chain):

**Narrative Bridge:**

"You just audited how well different organizations designed their security. Now let's see what happens when an attacker encounters those same networks. The gaps you found in the audit? Attackers will find them too.

**Your audit findings were:**
- Startup Tech: HIGH RISK (no segmentation, no detection)
- Mid-Market: MEDIUM RISK (strong foundation, legacy gap)
- Enterprise: LOW RISK (defense-in-depth)

Now, if an attacker targets each of these networks, how will it go?"

---

# MATERIALS CHECKLIST

### Variation A: Pre-Built Networks
- [ ] Scenario descriptions (3 networks)
- [ ] 6-domain audit framework
- [ ] Pre-filled audit results (for TO reference)
- [ ] Scoring sheet
- [ ] Comparison chart

### Variation B: Random Generation
- [ ] Simplified server cards
- [ ] Simplified security device cards
- [ ] Architecture cards
- [ ] Network summary template
- [ ] Audit framework
- [ ] Accuracy scoring sheet

### Variation C: Audit the Auditor
- [ ] Scenario 1: Startup Defense
- [ ] Scenario 2: Legacy System
- [ ] Scenario 3: Over-Engineering
- [ ] Debate preparation guide (arguments for each side)
- [ ] Debate scoring sheet
- [ ] Judge guide (for TO or Team C)

---

# QUICK REFERENCE

| Variation | Duration | Complexity | Competition | Setup |
|-----------|----------|-----------|------------|-------|
| **A: Pre-Built** | 15-25 min | Low | Low | Minimal |
| **B: Random Gen** | 25-35 min | Medium | Medium | Moderate |
| **C: Debate** | 20-30 min | High | High | Moderate |

---

# DEBRIEF CONNECTIONS TO INCIDENT ZERO

After any Audit Standalone variation, teams should understand:

1. **Audits find real vulnerabilities** - Same gaps auditors find, attackers will exploit
2. **Context matters** - Startup vs. bank = different risk tolerance
3. **Trade-offs are real** - Can't afford everything; must prioritize
4. **Detection vs. Prevention** - Strong IDS/SIEM matters as much as hardening
5. **Incident response starts with audit** - Knowing your gaps speeds detection

**Key Teaching:** "In Phase 1 (Attack Chain), auditors played the role of the security team. Attackers play the same role, but with opposite intent. They're looking for exactly what auditors find."

---

*Incident Zero: Compliance Audit Standalone Mini-Games*  
*Three variations of security assessment gameplay*  
*Teach how audits find vulnerabilities that attackers will exploit*