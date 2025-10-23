# Incident Zero: Compliance Audit Phase
## Foundational Architecture & Pre-Game Preparation

---

## Overview: The Complete Security Operations Curriculum

**Incident Zero** now offers a complete **systems thinking progression**:

```
┌─────────────────────────────────────────────────────────────┐
│ PHASE 0A: NETWORK BUILDING (Optional)                       │
│ "What infrastructure do we have?"                           │
│ - Build network with constraints                            │
│ - Make trade-off decisions                                  │
│ - Create exploitable gaps (intentionally or accidentally)   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ PHASE 0B: COMPLIANCE AUDIT (Optional)                       │
│ "Are we audit-ready?"                                       │
│ - Audit findings reveal security gaps                       │
│ - Teams learn what's broken before attack                   │
│ - Create specific vulnerabilities for attack to exploit     │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ PHASE 1: ATTACK CHAIN (Standard)                            │
│ "Can we detect the attack?"                                 │
│ Threats specifically leverage network gaps & audit findings │
└─────────────────────────────────────────────────────────────┘
                    ↙                           ↖
        WIN                                      LOSE
            ↓                                       ↓
┌──────────────────────┐              ┌──────────────────────┐
│ PHASE 2A: HARDENING  │              │ PHASE 2B: DISASTER   │
│ "Build better defense"               │ "Manage crisis"      │
│ - Use audit findings │              │ - Audit failures     │
│ - Fix network gaps   │              │   cost MORE $$$      │
│ - Deploy controls    │              │ - Network gaps make  │
│                      │              │   recovery harder    │
└──────────────────────┘              └──────────────────────┘
            ↓                                       ↓
┌──────────────────────┐              ┌──────────────────────┐
│ PHASE 2C: POST-AUDIT │              │ PHASE 2C: POST-AUDIT │
│ (Optional)           │              │ (Optional)           │
│ "Did we improve?"    │              │ "Are we better?"     │
└──────────────────────┘              └──────────────────────┘
```

---

# PHASE 0B: COMPLIANCE AUDIT

## Purpose
A **hypothetical third-party audit** reviews the network infrastructure teams just built. Audit findings reveal specific security gaps that will become **vulnerabilities in the attack chain**.

This models the reality: "Auditors find what attackers will exploit."

## Audit Concept

**The audit happens BEFORE the attack**, so:
- Teams see what's broken
- Teams learn about vulnerabilities
- Teams still can't do much about them (it's already built in Phase 0A)
- When Phase 1 attack happens, teams recognize: "That's the network gap the audit found!"

---

## Compliance Audit Setup (10 minutes)

### Audit Scenario

**"Your organization is undergoing a routine security audit by an external firm. They're evaluating your network infrastructure against industry standards (NIST, CIS, HIPAA if applicable, PCI-DSS if handling cards, etc.). Let's see what they find."**

### Audit Framework

Auditors review **6 domains**:

1. **Network Segmentation** - Are critical systems isolated?
2. **Access Control** - Is identity properly managed?
3. **Incident Detection** - Can you see attacks?
4. **Backup & Recovery** - Can you recover from failure?
5. **Third-Party Risk** - Are cloud/vendor systems managed?
6. **Security Operations** - Do you have logging/monitoring?

---

## Compliance Audit Gameplay (10 minutes)

### Audit Process

**Threat Orchestrator (Acting as Auditor)** reviews the Network from Phase 0A and asks 6 questions:

For each domain, teams **pass or fail** based on their network design:

#### **Domain 1: Network Segmentation**

**Audit Question:** "Do you have network segmentation?"

**PASS if:** 
- Implemented segmented architecture (cost 5+), AND
- Deployed firewall between zones, AND
- Different types of servers in different zones

**FAIL if:**
- Flat network (no architecture cost)
- Segmentation but no firewall
- All servers in single zone

**If FAIL:** 
Finding: "Network Segmentation Gap"
- **Consequence in Phase 1:** Lateral movement easier (-1 to defend against NETWORK attacks)
- **Consequence in DR:** Recovery takes longer (+10 to crisis budget costs)

#### **Domain 2: Access Control & Identity**

**Audit Question:** "Is your identity system properly secured?"

**PASS if:**
- Domain Controller deployed, AND
- Domain Controller on separate network segment, AND
- Multi-factor authentication (implied by good architecture)

**FAIL if:**
- No Domain Controller
- DC on same segment as untrusted systems
- DC overloaded with too many services (more than 2)

**If FAIL:**
Finding: "Identity System Vulnerability"
- **Consequence in Phase 1:** Privilege escalation easier (-1 to defend against CREDENTIAL_ABUSE)
- **Consequence in DR:** Credential dumping (Mimikatz) more damaging (+15 to crisis costs)

#### **Domain 3: Incident Detection & Response**

**Audit Question:** "Can you detect and respond to attacks?"

**PASS if:**
- IDS or IPS deployed, OR
- SIEM system deployed, OR
- Email Gateway + Honeypot deployed

**FAIL if:**
- None of the above
- Only one security device total

**If FAIL:**
Finding: "Incident Detection Gap"
- **Consequence in Phase 1:** Investigation rolls harder (-1 to Investigate actions)
- **Consequence in DR:** Forensic investigation takes longer (+10 to crisis budget)

#### **Domain 4: Backup & Recovery**

**Audit Question:** "Do you have working backups?"

**PASS if:**
- Backup System deployed, OR
- Cloud backup configured, OR
- Multiple hosting locations (on-prem + cloud)

**FAIL if:**
- No Backup System
- Single point of failure (all on-prem or all cloud)

**If FAIL:**
Finding: "Disaster Recovery Gap"
- **Consequence in Phase 1:** None (network gap, not detection issue)
- **Consequence in DR:** Ransomware is catastrophic; recovery impossible without backups (+25 to crisis costs)

#### **Domain 5: Third-Party Risk Management**

**Audit Question:** "Are cloud/vendor systems properly managed?"

**PASS if:**
- Cloud systems isolated properly, AND
- VPN or private network used, AND
- Monitoring of cloud systems

**FAIL if:**
- Cloud systems on internet-exposed networks
- No monitoring of cloud services
- Credentials stored locally for cloud access

**If FAIL:**
Finding: "Cloud Security Gap"
- **Consequence in Phase 1:** API attacks easier (-1 to defend against WEB_EXPLOIT)
- **Consequence in DR:** Cloud compromise spreads quickly; recovery requires cloud provider help (+20 to crisis costs)

#### **Domain 6: Security Operations & Monitoring**

**Audit Question:** "Do you have centralized logging and monitoring?"

**PASS if:**
- SIEM system deployed, OR
- Email Gateway + IDS deployed

**FAIL if:**
- No SIEM
- Only basic security devices

**If FAIL:**
Finding: "Security Operations Gap"
- **Consequence in Phase 1:** Investigations slower (-1 to Investigation rolls)
- **Consequence in DR:** "We can't find the attacker" (+5 to forensic costs)

---

## Audit Findings Report

After all 6 domains are audited, **Threat Orchestrator produces an Audit Findings Report**:

### Example Audit Report

```
SECURITY AUDIT FINDINGS REPORT
Organization: Acme Corp
Date: Q4 2024
Auditor: External Security Firm

DOMAIN FINDINGS:

✓ PASS - Network Segmentation
  Comment: Organization implemented 3-zone segmentation with
  firewalls. Good separation of DMZ, internal, and sensitive zones.

✗ FAIL - Access Control & Identity
  Finding: Domain Controller overloaded with SIEM and other services.
  Risk: If DC is compromised, entire identity system at risk.
  Recommendation: Isolate DC to dedicated server or minimal services.

✗ FAIL - Incident Detection & Response
  Finding: No SIEM system. No centralized logging. IDS present but
  insufficient without log correlation.
  Risk: Attacks may not be detected; investigation will be slow.
  Recommendation: Deploy SIEM for centralized logging and alerting.

✓ PASS - Backup & Recovery
  Comment: Backup system deployed and on separate network segment.
  Good disaster recovery posture.

✗ FAIL - Third-Party Risk Management
  Finding: Cloud web server is internet-accessible without WAF.
  Risk: Web application attacks can reach systems directly.
  Recommendation: Deploy WAF in front of cloud web server.

✓ PASS - Security Operations & Monitoring
  Comment: Email Gateway and IDS provide reasonable monitoring.

SUMMARY: 3 PASS, 3 FAIL

EXPLOITABLE FINDINGS:
1. Overloaded Domain Controller (Credential Abuse vulnerability)
2. No centralized logging (Detection vulnerability)
3. Unprotected cloud web server (Web Exploit vulnerability)

ESTIMATED RISK: Medium-High
If an attacker gains initial access, they can move laterally due to
ID system vulnerabilities. Detection will be slow due to lack of
centralized logging.
```

---

## Audit Scoring

**Teams Receive an Audit Score:**

| Score | Interpretation |
|-------|-----------------|
| **6/6 PASS** | Enterprise-grade security | No modifiers in Phase 1/DR |
| **5/6 PASS** | Strong security | -1 to one attack type in Phase 1 |
| **4/6 PASS** | Adequate security | -1 to two attack types in Phase 1 |
| **3/6 PASS** | Concerning gaps | -1 to three attack types; Phase 1 easier |
| **Below 3/6** | High risk | Multiple -1 modifiers; easier attacks in Phase 1 |

---

## Audit Findings as Attack Vectors

**Each FAIL finding maps to specific threats in Phase 1:**

```
AUDIT FINDING → ATTACK VECTOR → THREAT CARD MODIFICATION

Network Segmentation FAIL
  → NETWORK vulnerabilities become easier (-1)
  → "Lateral Movement via SMB" attack gains +1 bonus

Identity System FAIL
  → CREDENTIAL_ABUSE vulnerabilities become easier (-1)
  → "Mimikatz Credential Dumping" attack gains +1 bonus

Incident Detection FAIL
  → All attacks become harder to detect (-1 Investigation)
  → Investigation rolls need 12+ instead of 11+

Backup/Recovery FAIL
  → Ransomware more effective in Disaster Recovery
  → If ransomware succeeds, no backup to restore from (+25 crisis costs)

Third-Party Risk FAIL
  → WEB_EXPLOIT attacks easier (-1)
  → Cloud API attacks more effective (+1 to Cloud API abuse)

Security Operations FAIL
  → Forensic investigation slower in Phase 1 (-1 Investigation)
  → Forensic recovery slower in DR (+5 crisis costs)
```

---

# PHASE 1: MODIFIED ATTACK CHAIN

## Integration of Network & Audit Findings

### Dice Roll: Network Gaps & Audit Findings

**Before Phase 1 Begins:**

**Threat Orchestrator rolls dice to determine if Phase 0 decisions actually matter:**

#### **Dice Roll 1: "Do Network Gaps Apply?"**

Roll 1d20:
- **1-10:** Network gaps DON'T apply (teams got lucky; architecture doesn't matter)
- **11-15:** Network gaps PARTIALLY apply (-1 to some defenses)
- **16-20:** Network gaps FULLY apply (-1 or -2 to relevant defenses)

**Narrative:**
- **Lucky Roll (1-10):** "Despite some design gaps, your network is holding up so far. Maybe you got lucky."
- **Partial (11-15):** "Your network segmentation isn't perfect, so lateral movement is slightly easier than ideal."
- **Full (16-20):** "Your network design is creating real vulnerabilities that the attacker is exploiting."

#### **Dice Roll 2: "Do Audit Findings Matter?"**

Roll 1d20:
- **1-10:** Audit findings don't manifest (good luck; attackers miss the gaps)
- **11-15:** One audit finding is exploited (attackers use one discovered vulnerability)
- **16-20:** Multiple audit findings exploited (attackers use all discovered gaps)

**Narrative:**
- **Lucky (1-10):** "The audit findings didn't become attack vectors; the attackers used different techniques."
- **Partial (11-15):** "The attackers found and exploited the identity system vulnerability the audit discovered."
- **Full (16-20):** "The attackers strategically targeted all three security gaps the audit identified."

---

### Network Gap Modifiers in Phase 1

**If dice roll says network gaps apply, these modifiers activate:**

#### **Segmentation Gap Active:**
- **Effect:** Lateral movement attacks gain +1 bonus
- **Threat:** "Lateral Movement via SMB" rolls +1 extra
- **Defense Impact:** Deploying "Network Segmentation" defense gets +2 bonus (fixing the gap)

**Narrative during Phase 1:**
"Your investigation reveals that the attacker successfully moved from the web server to your file server using SMB traffic. This wouldn't have been possible if you had proper network segmentation in place."

#### **Identity System Gap Active:**
- **Effect:** Credential-based attacks gain +1 bonus
- **Threat:** "Mimikatz Credential Dumping" rolls +1 extra
- **Defense Impact:** Deploying "Credential Guard" or "MFA" gets +2 bonus (fixing the gap)

**Narrative during Phase 1:**
"The Domain Controller has too many services running on it. The attacker was able to dump credentials from LSASS because the system wasn't hardened."

#### **Detection Gap Active:**
- **Effect:** All Investigation rolls require 12+ instead of 11+
- **Impact:** Your SIEM/IDS gaps make attacks harder to find
- **Defense Impact:** Deploying IDS, IPS, or SIEM gets +1 bonus (fixing the gap)

**Narrative during Phase 1:**
"You're trying to investigate lateral movement, but without centralized logging, you have to piece together evidence from multiple sources. That's taking longer."

#### **Backup Gap Active:**
- **Effect:** No effect in Phase 1 (backup isn't needed until Disaster Recovery)
- **Impact:** BIG impact if you lose Phase 1 and enter Disaster Recovery

#### **Third-Party Risk Gap Active:**
- **Effect:** Cloud/web-based attacks gain +1 bonus
- **Threat:** "Cloud API Token Theft" or "Watering Hole" roll +1 extra
- **Defense Impact:** Deploying "Cloud CSPM" or "WAF" gets +1 bonus (fixing the gap)

#### **Security Operations Gap Active:**
- **Effect:** Forensic investigation slower (-1 to Investigation rolls)
- **Investigation Penalty:** Same as detection gap

---

### Audit Finding Narrative Integration

**When Attack Chain Progresses, Reference Audit Findings:**

**Example Phase 1 Scenario:**

```
TURN 3: Team attempts to Investigate "Suspicious Lateral Movement"

TO says: "You're reviewing SMB traffic logs to determine how the attacker
moved from the web server to your file server. However, your audit report
noted 'Network Segmentation Gap' - these servers are on the same network
zone without proper microsegmentation. Your investigation shows the
attacker exploited exactly what the audit team warned about.

You need a 12+ to piece this together (normally 11+) because your logging
isn't centralized. Also noted in audit: 'Incident Detection Gap - No SIEM.'

You rolled 13 with +2 justification bonus = 15. SUCCESS.

You discover: The attacker used the network gap to move laterally.
Your team is now investigating Credential Dumping next."
```

---

### Rogue Employee / Compromised System Narrative

**Alternative to Phase 0: Pre-Generate Gaps for Standalone Play**

If teams **skip Phase 0A & 0B** and jump straight to Phase 1, TO can use **narrative dice rolls** to create gaps:

**Roll 1d20 at Phase 1 Start:**

| Roll | Narrative | Effect |
|------|-----------|--------|
| 1-3 | "Your network administrator left last month without proper documentation" | Segmentation Gap active |
| 4-6 | "A rogue employee created an unauthorized network bridge to bypass firewalls" | Segmentation Gap active |
| 7-9 | "Your backup system failed silently 2 weeks ago; nobody noticed" | Backup Gap active |
| 10-12 | "Your SIEM license lapsed; monitoring went dark for a week" | Detection Gap active |
| 13-15 | "Cloud infrastructure was configured hastily for a project deadline" | Third-Party Risk Gap active |
| 16-18 | "A recent employee departure left credentials widely shared" | Identity System Gap active |
| 19-20 | "Lucky day; infrastructure is solid. No pre-existing gaps" | No modifiers |

**Narrative Examples:**

"Three months ago, a rogue administrator created a management backdoor in your DMZ that bypasses the firewall. Your current IT team doesn't know about it. When the attacker discovers this backdoor, they skip the entire perimeter defense."

"Your backup system hasn't been tested in 8 months. When ransomware hits in Disaster Recovery, you'll discover it hasn't been backing up properly."

---

# PHASE 2: HARDENING & DISASTER RECOVERY INTEGRATION

## Using Network/Audit Findings in Phase 2

### Phase 2 - Hardening Path

**If teams WON Phase 1 and enter Hardening Phase:**

Teams can see their audit findings and network gaps:

"Your security team has learned from this incident. The audit identified 3 critical gaps. Now you have time and budget to fix them.

**Priority 1:** Deploy Network Segmentation to fix the lateral movement vulnerability
**Priority 2:** Deploy SIEM to improve incident detection
**Priority 3:** Deploy MFA to secure credential access"

**Hardening Bonuses:**
- Fixing an audit-identified gap gives +2 defense bonus (you know exactly what to fix)
- Example: "We're deploying Network Segmentation Switch to fix the segmentation gap discovered in the audit." → +2 bonus to network defense score

---

### Phase 2 - Disaster Recovery Path

**If teams LOST Phase 1 and enter Disaster Recovery:**

Audit findings create ADDITIONAL COSTS:

**Audit Finding Costs in DR:**

| Finding | DR Impact | Cost |
|---------|-----------|------|
| **Segmentation Gap** | Attacker can access everything; more data compromised | +10 crisis budget |
| **Identity Gap** | Full credential compromise; all users affected | +15 crisis budget |
| **Detection Gap** | Attack undetected longer; dwell time higher | +5 crisis budget |
| **Backup Gap** | No recovery option; must rebuild from scratch | +25 crisis budget |
| **Third-Party Risk Gap** | Cloud compromise; must coordinate with cloud provider | +10 crisis budget |
| **Security Ops Gap** | Can't determine scope of breach; forensic investigation slow | +5 crisis budget |

**Example DR Scenario:**

```
Teams enter Disaster Recovery with 50 crisis budget.

Audit findings WERE:
- Segmentation Gap
- Detection Gap
- Backup Gap

Additional DR Costs activate:
- Segmentation Gap adds +10 (attackers accessed more systems)
- Detection Gap adds +5 (breach undetected longer; more data stolen)
- Backup Gap adds +25 (can't restore; must rebuild)

ADDITIONAL COSTS: 40 (out of 50 available)
Effective available budget: 50 - 40 = 10

Teams now have only 10 budget for crisis response actions.
Forensic investigation costs 15 (can't afford it).
Customer notification costs 10 (last action possible).

Reputation damage is higher due to gap-related compromises.
```

---

# PHASE 2C: POST-INCIDENT AUDIT (Optional)

## Purpose

**After Phase 2 (Hardening or DR), teams undergo another audit to see if they improved.**

This closes the loop: "Did we learn from our mistakes?"

---

## Post-Incident Audit Setup (10 minutes)

### Same 6 Domains, New Questions

**Auditor reviews improvements:**

#### **Domain 1: Network Segmentation**
- **Question:** "Did you fix the segmentation gap?"
- **If Hardening Path:** Teams likely deployed segmentation → PASS
- **If DR Path:** Teams had limited budget; may have skipped it → Might FAIL again

#### **Domain 2: Access Control**
- **Question:** "Did you secure the identity system?"
- **If Hardening Path:** Teams likely deployed MFA, Credential Guard → PASS
- **If DR Path:** Depends on remediation priorities

#### **Domain 3: Incident Detection**
- **Question:** "Can you detect faster next time?"
- **If Hardening Path:** Teams likely deployed SIEM/IDS → PASS
- **If DR Path:** Budget-constrained; likely limited improvement

#### **Domain 4: Backup & Recovery**
- **Question:** "Do you have working backups now?"
- **If Hardening Path:** Teams likely deployed backup system → PASS
- **If DR Path:** May not have been priority

#### **Domain 5: Third-Party Risk**
- **Question:** "Is cloud properly secured?"
- **If Hardening Path:** Teams likely deployed cloud controls → PASS
- **If DR Path:** Limited improvement likely

#### **Domain 6: Security Operations**
- **Question:** "Do you have monitoring now?"
- **If Hardening Path:** Teams likely deployed SIEM/logging → PASS
- **If DR Path:** Limited improvement

---

## Post-Audit Scoring

### Improvement Comparison

```
FIRST AUDIT (Before Incident):      POST AUDIT (After Incident):
- Network Segmentation: FAIL         - Network Segmentation: PASS
- Identity System: FAIL              - Identity System: PASS
- Detection: FAIL                    - Detection: PASS
- Backup: PASS                       - Backup: PASS
- Third-Party: FAIL                  - Third-Party: FAIL
- Operations: FAIL                   - Operations: PASS

FIRST SCORE: 2/6                     POST SCORE: 5/6

IMPROVEMENT: +3 domains (150% improvement)
```

### Narrative Impact

**To Teams:**
"Congratulations! Your first audit identified critical gaps. This incident occurred because of those gaps. Now, your post-incident audit shows you've learned and improved significantly. 5 out of 6 domains now pass.

**However:** Your third-party risk management is still weak. Cloud infrastructure remains a vulnerability. This will be addressed in the next phase of your security roadmap.

**Lesson:** Security improvement is ongoing. Each incident teaches you something new."

---

# FULL GAME FLOWS

---

## Flow 1: Network Building → Attack Chain → Hardening/DR

**Timeline: 90-120 minutes**

```
NETWORK BUILDING (15 min)
  ↓
COMPLIANCE AUDIT (10 min)
  ↓
DICE ROLLS (Network gaps? Audit findings? - 2 min)
  ↓
ATTACK CHAIN / PHASE 1 (35-40 min)
  ↓
  ├─ WIN → HARDENING (25-30 min, Fix discovered gaps)
  └─ LOSE → DISASTER RECOVERY (30-35 min, Gaps cost more $$$)
  ↓
DEBRIEF (15 min)

TOTAL: 100-120 minutes
```

## Flow 2: Compliance Audit Only → Attack Chain → Hardening/DR

**Timeline: 60-90 minutes**

```
COMPLIANCE AUDIT (10 min - Using pre-built network)
  ↓
DICE ROLL (Do audit findings matter? - 1 min)
  ↓
ATTACK CHAIN / PHASE 1 (35-40 min)
  ↓
  ├─ WIN → HARDENING (20-25 min, Fix audit gaps)
  └─ LOSE → DISASTER RECOVERY (25-30 min, Audit costs manifest)
  ↓
DEBRIEF (10-15 min)

TOTAL: 75-100 minutes
```

## Flow 3: Attack Chain Only → Hardening/DR (Skip Both)

**Timeline: 60-90 minutes**

```
PHASE 1 (35-40 min)
  ├─ Dice roll for random network gap (1d20)
  └─ Dice roll for random audit finding (1d20)
  ↓
  ├─ WIN → HARDENING (20-25 min)
  └─ LOSE → DISASTER RECOVERY (25-30 min)
  ↓
DEBRIEF (10-15 min)

TOTAL: 65-90 minutes
```

## Flow 4: Full Marathon (Everything)

**Timeline: 3-3.5 hours**

```
NETWORK BUILDING (15 min)
  ↓
COMPLIANCE AUDIT (10 min)
  ↓
DICE ROLLS (2 min)
  ↓
ATTACK CHAIN / PHASE 1 (35-40 min)
  ↓
  ├─ WIN:
  │   ├─ HARDENING (25-30 min)
  │   └─ POST-AUDIT (10 min) - Did you improve?
  │   └─ TOTAL: ~45 min Phase 2
  │
  └─ LOSE:
      ├─ DISASTER RECOVERY (30-35 min)
      └─ POST-AUDIT (10 min) - How badly were you hit?
      └─ TOTAL: ~45 min Phase 2
  ↓
FINAL DEBRIEF (20 min) - Comparing improvement path

TOTAL: 180-200 minutes (3-3.5 hours)
```

## Flow 5: Skip Network → Audit → Attack → Response → Post-Audit

**Timeline: 2-2.5 hours**

```
COMPLIANCE AUDIT (10 min - Pre-built network)
  ↓
ATTACK CHAIN (35-40 min)
  ↓
  ├─ WIN → HARDENING → POST-AUDIT (35-40 min)
  └─ LOSE → DR → POST-AUDIT (40-50 min)
  ↓
DEBRIEF (15 min)

TOTAL: 115-155 minutes (2-2.5 hours)
```

---

# MATERIALS CHECKLIST

---

## Phase 0A: Network Building Materials

### Server Cards (10 types)
- [ ] Email Server (8 Budget, capacity 1)
- [ ] Web Server (7 Budget, capacity 1)
- [ ] Database Server (10 Budget, capacity 1)
- [ ] File Server (6 Budget, capacity 2)
- [ ] Domain Controller (12 Budget, capacity 2)
- [ ] Development Server (5 Budget, capacity 3)
- [ ] Backup System (9 Budget, capacity 1)
- [ ] Cloud Workload (4 Budget, capacity 2)
- [ ] Legacy System (3 Budget, capacity 1)
- [ ] Honeypot Decoy (7 Budget, capacity 1)

### Security Device Cards (10 types)
- [ ] Firewall (12 Budget)
- [ ] IDS (10 Budget)
- [ ] IPS (14 Budget)
- [ ] Load Balancer (8 Budget)
- [ ] VPN Concentrator (9 Budget)
- [ ] Email Gateway (6 Budget)
- [ ] WAF (11 Budget)
- [ ] Network Segmentation Switch (10 Budget)
- [ ] SIEM System (15 Budget)
- [ ] Honeypot Network (8 Budget)

### Network Architecture Cards
- [ ] Flat Network (0 Budget)
- [ ] Segmented Network 3-zone (5 Budget)
- [ ] Fully Isolated (12 Budget)
- [ ] Cloud Hybrid (8 Budget)
- [ ] Cloud First (6 Budget)

### Tracking Sheets
- [ ] Network Budget Tracker (50 tokens)
- [ ] Infrastructure Summary Card (document what was built)
- [ ] Network Gaps Registry (vulnerabilities discovered)
- [ ] Service Allocation Sheet (what runs on what server)

## Phase 0B: Compliance Audit Materials

### Audit Framework
- [ ] 6-Domain Audit Questionnaire
- [ ] Audit Findings Report Template
- [ ] Pass/Fail Decision Tree (for TO)

### Audit Cards (6 domains)
- [ ] Network Segmentation Assessment Card
- [ ] Access Control & Identity Assessment Card
- [ ] Incident Detection & Response Assessment Card
- [ ] Backup & Recovery Assessment Card
- [ ] Third-Party Risk Management Assessment Card
- [ ] Security Operations Assessment Card

### Reference Materials
- [ ] Audit Score Interpretation Chart
- [ ] "Exploitable Findings" Conversion Map
- [ ] Narrative Gap Examples (for standalone play)

## Phase 1 Modified Materials

### Dice & Rolls
- [ ] 1d20 die
- [ ] "Network Gaps Apply?" Dice Roll Chart
- [ ] "Audit Findings Matter?" Dice Roll Chart

### Modifier Sheets
- [ ] Network Gap Modifiers (what applies -1 where)
- [ ] Audit Finding Attack Vector Map
- [ ] Phase 1 with Modifiers Reference Sheet

## Phase 2 Integration Materials

### Hardening Phase
- [ ] Network Gap Fix Bonuses Chart
- [ ] "Which audit gap will you fix first?" Decision Cards

### Disaster Recovery Phase
- [ ] Audit Finding Cost Modifiers Chart
- [ ] "How many audit findings are hurting us?" Calculation Sheet

## Phase 2C: Post-Audit Materials

### Post-Audit Assessment
- [ ] Post-Audit 6-Domain Questionnaire
- [ ] Improvement Comparison Sheet
- [ ] Before/After Scoring Chart

---

# QUICK REFERENCE: SETUP BY SCENARIO

---

## Scenario A: First-Time Players (90 min)

**Setup:**
1. DO NOT play Network Building (too complex first time)
2. Start with Compliance Audit (simpler, teaches foundations)
3. Use Dice Roll to create random audit gaps
4. Play Phase 1 with audit modifiers active
5. Play Phase 2 (Hardening or DR based on outcome)

**Rationale:** Audit phase is faster to understand than Network Building. Allows players to see how pre-existing gaps matter.

## Scenario B: Experienced Players (120 min)

**Setup:**
1. Play full Network Building (15 min)
2. Play Compliance Audit (10 min)
3. Dice roll to determine modifiers
4. Play Phase 1
5. Play Phase 2

**Rationale:** Full scope; understand architecture → gaps → consequences

## Scenario C: Deep Dive / Marathon (3 hours)

**Setup:**
1. Network Building (15 min)
2. Compliance Audit (10 min)
3. Phase 1 with dice rolls (40 min)
4. Phase 2 - Hardening or DR (45 min)
5. Post-Audit (10 min)
6. Debrief & Strategy Discussion (20 min)

**Rationale:** Complete arc from architecture through incident to improvement

## Scenario D: Audit-Focused (75 min)

**Setup:**
1. Skip Network Building
2. Describe pre-built network: "Your company has a typical setup with email, web, database, file servers, but basic security"
3. Play Compliance Audit (10 min)
4. Phase 1 with audit gaps (40 min)
5. Phase 2 (20-25 min)

**Rationale:** Focus on how compliance/audit findings predict real vulnerabilities

---

# SUMMARY

**Incident Zero now supports a complete incident management curriculum:**

1. **Network Building** → Understand infrastructure trade-offs
2. **Compliance Audit** → Learn what auditors find (attackers will find the same things)
3. **Attack Chain** → Detect incidents; gaps make attacks easier
4. **Hardening** → Fix the discovered gaps
5. **Disaster Recovery** → Learn the cost of failed prevention
6. **Post-Audit** → Measure improvement

**Each phase cascades into the next:**
- Bad network design → Audit failures → Easier attacks → Higher recovery costs
- Good network design → Audit passes → Harder attacks → Lower recovery costs

*Incident Zero: Network Building & Compliance Audit Phases*  
*Teaching systems thinking in cybersecurity through integrated game mechanics*