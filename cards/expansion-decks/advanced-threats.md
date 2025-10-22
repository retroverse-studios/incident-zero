# Incident Zero: Expansion Threat Cards
## Advanced Attack Scenarios & Additional Threats

This document provides additional Threat Cards for expanding **Incident Zero** gameplay beyond the base 12-card deck. These cards introduce more sophisticated attack vectors and modern threat landscape scenarios.

---

## ADDITIONAL THREAT CARDS (6 Cards)

### Supply Chain Attack Threats

#### Card T-13: Compromised Software Vendor Update
```
┌─────────────────────────────────────┐
│ THREAT CARD                         │
├─────────────────────────────────────┤
│ COMPROMISED SOFTWARE VENDOR UPDATE  │
├─────────────────────────────────────┤
│ Step:    INITIAL COMPROMISE         │
│ Vector:  WEB EXPLOIT                │
├─────────────────────────────────────┤
│ CLUE FOR THREAT ORCHESTRATOR:       │
│ "Your monitoring systems detect     │
│ unusual outbound connections from   │
│ a recently deployed software update │
│ to an IP address not associated     │
│ with the vendor. The update was     │
│ digitally signed but verification   │
│ shows the signature was backdated.  │
│ Hundreds of organizations received  │
│ the same malicious update."         │
├─────────────────────────────────────┤
│ WHY THIS WORKS:                     │
│ Supply chain compromises affect     │
│ entire industries simultaneously.    │
│ Organizations trust vendor updates  │
│ and often deploy them automatically │
│ without deep inspection. The        │
│ attacker gains access to thousands  │
│ of targets at once. Real-world      │
│ example: SolarWinds, 3CX.           │
│                                     │
│ DETECTION DIFFICULTY: High          │
│ The malware appears legitimate due  │
│ to trusted vendor origin.           │
└─────────────────────────────────────┘
```

#### Card T-14: Malicious Third-Party Library Injection
```
┌─────────────────────────────────────┐
│ THREAT CARD                         │
├─────────────────────────────────────┤
│ MALICIOUS THIRD-PARTY LIBRARY       │
│ INJECTION                           │
├─────────────────────────────────────┤
│ Step:    INITIAL COMPROMISE         │
│ Vector:  MALWARE                    │
├─────────────────────────────────────┤
│ CLUE FOR THREAT ORCHESTRATOR:       │
│ "Your dependency scanning tool      │
│ alerts on a typosquatted NPM        │
│ package (npm package manager) that  │
│ was installed in your build         │
│ pipeline. The malicious package has │
│ the same name as a popular logging  │
│ library but with a slight misspell. │
│ It has been downloaded 50k times.   │
│ Your build logs show it was         │
│ installed 6 days ago."              │
├─────────────────────────────────────┤
│ WHY THIS WORKS:                     │
│ Developers rely on open-source      │
│ packages from package managers      │
│ (npm, PyPI, Maven). Attackers       │
│ upload malicious packages with      │
│ names similar to popular libraries  │
│ (typosquatting). Once downloaded,   │
│ the malicious code runs during      │
│ build/deployment. This affects      │
│ every application built from that   │
│ point forward.                      │
│                                     │
│ DETECTION DIFFICULTY: High          │
│ Requires dependency scanning and    │
│ behavior analysis of build processes.│
└─────────────────────────────────────┘
```

---

### Insider Threat Cards

#### Card T-15: Malicious Insider Data Theft
```
┌─────────────────────────────────────┐
│ THREAT CARD                         │
├─────────────────────────────────────┤
│ MALICIOUS INSIDER DATA THEFT        │
├─────────────────────────────────────┤
│ Step:    C2 & EXFIL                 │
│ Vector:  DATA EXFIL                 │
├─────────────────────────────────────┤
│ CLUE FOR THREAT ORCHESTRATOR:       │
│ "Your DLP system flags a large      │
│ volume of sensitive data being      │
│ copied by an IT operations          │
│ employee during off-hours. Their    │
│ user account accessed databases     │
│ they don't normally interact with.  │
│ The data was copied to a removable  │
│ USB drive connected to a shared     │
│ workstation. Security badge logs    │
│ show they entered the building at   │
│ 2 AM when the office was empty."    │
├─────────────────────────────────────┤
│ WHY THIS WORKS:                     │
│ Insiders have legitimate access and │
│ often bypass security controls.     │
│ Their activities may not trigger    │
│ alerts because their permissions    │
│ are valid. Detection requires:      │
│ - Behavioral analysis (unusual      │
│  times/volumes)                     │
│ - Physical security controls        │
│ - DLP and USB device control        │
│ - Privileged access management      │
│ Insiders cause 30-40% of data      │
│ breaches in many industries.        │
│                                     │
│ DETECTION DIFFICULTY: Very High     │
│ Insider actions often look normal   │
│ to automated systems.               │
└─────────────────────────────────────┘
```

#### Card T-16: Disgruntled Employee Sabotage
```
┌─────────────────────────────────────┐
│ THREAT CARD                         │
├─────────────────────────────────────┤
│ DISGRUNTLED EMPLOYEE SABOTAGE       │
├─────────────────────────────────────┤
│ Step:    PIVOT & ESCALATE           │
│ Vector:  MALWARE                    │
├─────────────────────────────────────┤
│ CLUE FOR THREAT ORCHESTRATOR:       │
│ "A recently terminated database     │
│ administrator appears to have       │
│ retained remote access using a      │
│ dormant service account they        │
│ created months ago. Logs show       │
│ connection attempts from their      │
│ home IP address. They've been       │
│ modifying stored procedures and     │
│ adding logic bombs set to trigger   │
│ in 30 days. Your team notices       │
│ their employee laptop is still      │
│ configured with VPN certificates."  │
├─────────────────────────────────────┤
│ WHY THIS WORKS:                     │
│ Disgruntled employees often have    │
│ privileged access and deep system   │
│ knowledge. They may have created    │
│ backdoors before termination.       │
│ Offboarding failures (not revoking  │
│ certs, not disabling accounts) are  │
│ common. Defense requires:           │
│ - Complete offboarding procedures   │
│ - Privileged access review          │
│ - Anomalous activity detection      │
│ - Behavior analysis for terminated  │
│  employees                          │
│                                     │
│ DETECTION DIFFICULTY: High          │
│ Requires correlation of access      │
│ patterns and employee status changes.│
└─────────────────────────────────────┘
```

---

### IoT Device Compromise

#### Card T-17: Compromised IoT Device as Pivot Point
```
┌─────────────────────────────────────┐
│ THREAT CARD                         │
├─────────────────────────────────────┤
│ COMPROMISED IOT DEVICE AS PIVOT     │
│ POINT                               │
├─────────────────────────────────────┤
│ Step:    INITIAL COMPROMISE         │
│ Vector:  NETWORK                    │
├─────────────────────────────────────┤
│ CLUE FOR THREAT ORCHESTRATOR:       │
│ "Your network monitoring detects    │
│ unusual traffic from an IoT device  │
│ (surveillance camera) in the        │
│ building. The device is communicating│
│ with a command server overseas and  │
│ tunneling internal network traffic. │
│ Your asset inventory shows this     │
│ camera was never formally added to  │
│ any security program. It's running  │
│ firmware from 2019 with known       │
│ vulnerabilities."                   │
├─────────────────────────────────────┤
│ WHY THIS WORKS:                     │
│ IoT devices are often neglected in  │
│ security programs (cameras, printers,│
│ thermostats, building automation).  │
│ They run outdated firmware and have │
│ weak or default credentials. Once   │
│ compromised, they provide network   │
│ access and can pivot to critical    │
│ systems. Many organizations don't   │
│ inventory or monitor IoT devices.   │
│                                     │
│ DETECTION DIFFICULTY: Medium        │
│ Requires network monitoring and     │
│ device inventory practices.         │
└─────────────────────────────────────┘
```

---

### Cloud API Abuse

#### Card T-18: Cloud API Token Theft & Abuse
```
┌─────────────────────────────────────┐
│ THREAT CARD                         │
├─────────────────────────────────────┤
│ CLOUD API TOKEN THEFT & ABUSE       │
├─────────────────────────────────────┤
│ Step:    PIVOT & ESCALATE           │
│ Vector:  CREDENTIAL ABUSE           │
├─────────────────────────────────────┤
│ CLUE FOR THREAT ORCHESTRATOR:       │
│ "Your AWS CloudTrail logs show API  │
│ calls from unusual IP addresses     │
│ using API keys belonging to a       │
│ developer who left the company 6    │
│ months ago. The calls are creating  │
│ new IAM users, accessing S3 buckets │
│ with customer data, and launching   │
│ EC2 instances in regions where you  │
│ don't normally operate. The API key │
│ was embedded in old GitHub          │
│ repository code."                   │
├─────────────────────────────────────┤
│ WHY THIS WORKS:                     │
│ Cloud API tokens/keys are often     │
│ exposed in code repositories or     │
│ configuration files. Once exposed,  │
│ they provide direct access to cloud │
│ resources. Attackers can spin up    │
│ resources, steal data, or deploy    │
│ cryptominers. Many organizations    │
│ fail to rotate or revoke old API    │
│ keys. Detection requires:           │
│ - API audit logging                 │
│ - Anomalous API pattern detection   │
│ - Key rotation policies             │
│ - Secrets scanning in repos         │
│                                     │
│ DETECTION DIFFICULTY: Medium-High   │
│ Requires cloud monitoring and       │
│ secrets management practices.       │
└─────────────────────────────────────┘
```

---

### DNS Tunneling for Data Exfiltration

#### Card T-19: DNS Tunneling Data Exfiltration
```
┌─────────────────────────────────────┐
│ THREAT CARD                         │
├─────────────────────────────────────┤
│ DNS TUNNELING DATA EXFILTRATION     │
├─────────────────────────────────────┤
│ Step:    C2 & EXFIL                 │
│ Vector:  DATA EXFIL                 │
├─────────────────────────────────────┤
│ CLUE FOR THREAT ORCHESTRATOR:       │
│ "Your DNS query logs show massive   │
│ volume of unusual subdomains being  │
│ queried through an external DNS     │
│ resolver. The subdomain names look  │
│ like Base64-encoded data. Queries   │
│ are happening in steady intervals.  │
│ Query timestamps align with your    │
│ database being accessed. Your DLP   │
│ didn't flag anything because DNS is │
│ typically trusted."                 │
├─────────────────────────────────────┤
│ WHY THIS WORKS:                     │
│ DNS tunneling encodes data in DNS   │
│ queries to bypass firewalls and DLP │
│ systems. Organizations often allow  │
│ DNS traffic without inspection. DNS │
│ queries are typically high-volume   │
│ and hard to distinguish from normal │
│ activity. Attackers can exfil small │
│ amounts of data over weeks.         │
│ Defense requires:                   │
│ - DNS query content analysis        │
│ - Anomalous query pattern detection │
│ - DNS rate limiting                 │
│ - External DNS access restrictions  │
│                                     │
│ DETECTION DIFFICULTY: Very High     │
│ Requires specialized DNS monitoring │
│ tools and baseline analysis.        │
└─────────────────────────────────────┘
```

---

### Physical Security Bypass

#### Card T-20: Physical Access + Badge Cloning Attack
```
┌─────────────────────────────────────┐
│ THREAT CARD                         │
├─────────────────────────────────────┤
│ PHYSICAL ACCESS + BADGE CLONING     │
│ ATTACK                              │
├─────────────────────────────────────┤
│ Step:    INITIAL COMPROMISE         │
│ Vector:  CREDENTIAL ABUSE           │
├─────────────────────────────────────┤
│ CLUE FOR THREAT ORCHESTRATOR:       │
│ "Your security team discovers that  │
│ an RFID badge belonging to a        │
│ manager was cloned using a portable │
│ reader. The cloned badge was used   │
│ to gain access to your secure data  │
│ center after-hours. Badge access    │
│ logs are timestamped, but the       │
│ person's schedule shows they weren't│
│ in the office that evening. Your    │
│ server room CCTV captured footage   │
│ of an unknown individual installing │
│ a wireless device in the network    │
│ rack."                              │
├─────────────────────────────────────┤
│ WHY THIS WORKS:                     │
│ Physical security is often          │
│ overlooked in cybersecurity         │
│ programs. RFID badges can be cloned │
│ with inexpensive readers. Once      │
│ inside the data center, attackers   │
│ can install rogue network devices,  │
│ steal hardware, or gain console     │
│ access to servers. Defense requires:│
│ - Encrypted badge technology        │
│ - Multi-factor access (biometric)   │
│ - CCTV monitoring                   │
│ - Environmental controls            │
│ - Equipment inventory tracking      │
│ - Badge deactivation on exit        │
│                                     │
│ DETECTION DIFFICULTY: High          │
│ Requires integration of physical    │
│ and cyber security monitoring.      │
└─────────────────────────────────────┘
```

---

## Integrating Expansion Threats into Your Game

### Attack Vector Summary (Expansion Cards)
- **WEB EXPLOIT:** Compromised Software Vendor Update (T-13)
- **MALWARE:** Malicious Third-Party Library Injection (T-14), Disgruntled Employee Sabotage (T-16)
- **NETWORK:** Compromised IoT Device as Pivot Point (T-17)
- **CREDENTIAL ABUSE:** Cloud API Token Theft & Abuse (T-18), Physical Access + Badge Cloning (T-20)
- **DATA EXFIL:** Malicious Insider Data Theft (T-15), DNS Tunneling Data Exfiltration (T-19)

### Suggested Scenario Combinations

#### Scenario 4: "Supply Chain Nightmare" (5-card chain - Expert)
Teaches: Third-party risk management, vendor security assessment, incident response at scale
1. **Compromised Software Vendor Update** (Initial Compromise) → WEB EXPLOIT
2. **Lateral Movement via SMB** (Pivot & Escalate) → NETWORK
3. **Scheduled Task Persistence** (Persistence) → MALWARE
4. **Beaconing to C2 Server** (C2 & Exfil) → NETWORK
5. **SQL Database Exfiltration** (C2 & Exfil) → DATA EXFIL

**Special Rule:** Reveal this threat to 3+ teams (representing industry-wide detection). First team to detect gains +20 Budget (represents vendor advisory advantage).

#### Scenario 5: "Insider Threat Explosion" (4-card chain - Intermediate)
Teaches: Insider risk detection, privileged access management, offboarding procedures
1. **Disgruntled Employee Sabotage** (Pivot & Escalate) → MALWARE
2. **Lateral Movement via SMB** (Pivot & Escalate) → NETWORK
3. **Mimikatz Credential Dumping** (Pivot & Escalate) → CREDENTIAL ABUSE
4. **Malicious Insider Data Theft** (C2 & Exfil) → DATA EXFIL

**Special Rule:** The employee's offboarding checklist is partially incomplete. Teams get a -2 penalty to detect the first insider threat (represents delayed detection in real situations).

#### Scenario 6: "Modern Infrastructure Attack" (5-card chain - Expert)
Teaches: IoT security, cloud security, API management, defense breadth
1. **Compromised IoT Device as Pivot Point** (Initial Compromise) → NETWORK
2. **Lateral Movement via SMB** (Pivot & Escalate) → NETWORK
3. **Cloud API Token Theft & Abuse** (Pivot & Escalate) → CREDENTIAL ABUSE
4. **DNS Tunneling Data Exfiltration** (C2 & Exfil) → DATA EXFIL

**Parallel threat:** Teams must defend against both cloud and on-premises infrastructure simultaneously.

#### Scenario 7: "Physical Meets Cyber" (4-card chain - Intermediate)
Teaches: Physical security integration, environmental controls, holistic security
1. **Physical Access + Badge Cloning** (Initial Compromise) → CREDENTIAL ABUSE
2. **Lateral Movement via SMB** (Pivot & Escalate) → NETWORK
3. **Scheduled Task Persistence** (Persistence) → MALWARE
4. **Ransomware Payload Deployment** (C2 & Exfil) → MALWARE

**Special Rule:** The first defense deployed must address the physical security aspect (badge systems, CCTV review, environmental controls). Teams get a narrative bonus: "Your physical security team noticed the intruder before full compromise."

#### Scenario 8: "Supply Chain + Insider Collusion" (5-card chain - Hard)
Teaches: Complex attack coordination, detecting collusion, multi-vector threats
1. **Malicious Third-Party Library Injection** (Initial Compromise) → MALWARE
2. **Disgruntled Employee Sabotage** (Pivot & Escalate) → MALWARE
3. **Cloud API Token Theft & Abuse** (Pivot & Escalate) → CREDENTIAL ABUSE
4. **DNS Tunneling Data Exfiltration** (C2 & Exfil) → DATA EXFIL
5. **Malicious Insider Data Theft** (C2 & Exfil) → DATA EXFIL

**Special Rule:** Two threats must be revealed to understand the full scope (supply chain + insider collaboration). Incomplete investigation leads to missed detection of the insider component.

---

## Recommended Defense Cards for Expansion Threats

### For Supply Chain Attacks (T-13, T-14)
- **Software Composition Analysis (SCA)** - ADVANCED - Scans dependencies for known vulnerabilities and unauthorized packages
- **Vendor Security Assessment Program** - ADVANCED - Vets third-party vendors before deployment
- **Code Signing Verification** - ELITE - Validates digital signatures on all updates before deployment

### For Insider Threats (T-15, T-16)
- **Privileged Access Management (PAM)** - ELITE - Monitors and controls privileged user activities in real-time
- **User & Entity Behavior Analytics (UEBA)** - ELITE - Detects anomalous behavior from trusted accounts
- **Badge & Offboarding Audit** - ADVANCED - Verifies that terminated employees' access is fully revoked
- **Physical Security Integration** - ADVANCED - Monitors badge logs and CCTV correlated with system access

### For IoT Device Compromise (T-17)
- **IoT Device Inventory & Classification** - BASIC - Catalogues all IoT devices and creates security policies for each
- **Network Segmentation for IoT** - ADVANCED - Isolates IoT networks from critical systems
- **Firmware Update Automation** - ADVANCED - Automatically patches and updates IoT firmware
- **IoT Behavioral Monitoring** - ELITE - Detects anomalous network traffic from IoT devices

### For Cloud API Abuse (T-18)
- **API Key Secrets Scanning** - ADVANCED - Scans repositories and storage for exposed API keys
- **Cloud Identity & Access Management (IAM) Hardening** - ADVANCED - Implements least-privilege access and MFA for API calls
- **Cloud Audit Logging & Monitoring** - ADVANCED - Monitors all API calls and detects anomalous patterns
- **API Rate Limiting & Anomaly Detection** - ELITE - Detects and blocks unusual API activity

### For DNS Tunneling (T-19)
- **DNS Query Content Analysis** - ELITE - Inspects DNS queries for encoded data patterns
- **DNS Rate Limiting & Anomaly Detection** - ADVANCED - Detects suspicious DNS query patterns
- **Internal DNS Monitoring** - BASIC - Monitors DNS traffic for unusual destinations
- **DNS Filtering Service** - ADVANCED - Blocks known malicious domains and suspicious patterns

### For Physical Security Bypass (T-20)
- **Multi-Factor Physical Access Controls** - ADVANCED - Requires badge + biometric for sensitive areas
- **RFID Encryption & Frequency Hopping** - ELITE - Uses encrypted, dynamic badges resistant to cloning
- **Environmental Controls (CCTV + Sensors)** - ADVANCED - Integrates video monitoring with access logs
- **Hardware Inventory Management** - BASIC - Tracks and audits all equipment in secure areas

---

## Difficulty Adjustments Using Expansion Cards

### Easy + Expansion (6-card chain)
- 3 base cards + 1-2 expansion cards
- Example: Phishing → Lateral Movement → Mimikatz → Insider Data Theft
- **Learning Focus:** Introduction to modern threat landscape

### Medium + Expansion (4-5 card chains with expansion)
- Mix of base and expansion cards
- Focus on one modern threat (supply chain, insider, or cloud)
- **Learning Focus:** Specialized threat scenarios

### Hard + Expansion (5+ card chains with 2+ expansion cards)
- Complex scenarios combining base + expansion cards
- Multi-vector attacks (physical + cyber, insider + supply chain)
- **Learning Focus:** Enterprise-grade incident response

---

## Teaching Notes for Threat Orchestrators

### Supply Chain Attacks (T-13, T-14)
**Real-world context:**
- SolarWinds (2020) - 18,000+ organizations affected
- 3CX (2023) - Trojanized build system
- XcodeGhost (2015) - Compromised Xcode developer tool
- Typosquatted packages discovered monthly on npm/PyPI

**Discussion points after reveal:**
- "How do you verify software authenticity?"
- "What's the difference between detecting supply chain compromises vs. traditional malware?"
- "Why is this harder to detect than direct attacks?"

### Insider Threats (T-15, T-16)
**Real-world context:**
- ~30-40% of data breaches involve insiders (Verizon DBIR)
- Manning, Snowden, Reality Winner cases (government sector)
- Thousands of employee theft cases in financial/tech industries

**Discussion points after reveal:**
- "How would you detect insider threat indicators before damage occurs?"
- "Why is offboarding security often weak?"
- "What's the difference between a malicious insider and negligent employee?"

### IoT Device Compromise (T-17)
**Real-world context:**
- Mirai botnet (2016) - Millions of compromised IoT devices
- Connected cameras, printers, thermostats often neglected
- "Shadow IT" problem in many organizations

**Discussion points after reveal:**
- "Should IoT devices be on the same network as critical systems?"
- "How do you patch thousands of IoT devices?"
- "Why are credentials often factory-default on IoT?"

### Cloud API Abuse (T-18)
**Real-world context:**
- AWS credentials leaked in GitHub ~8 times per day (GitHub telemetry)
- Tesla's Kubernetes cluster hacked via exposed credentials
- Capital One breach involved compromised IAM role

**Discussion points after reveal:**
- "How do you manage API keys for thousands of developers?"
- "Why is secrets rotation hard in practice?"
- "How would you know if someone used your AWS API key?"

### DNS Tunneling (T-19)
**Real-world context:**
- Used by DNS.Exfiltrator, OilRig APT, Turla malware families
- Hard to detect because DNS is typically trusted
- Can exfil ~20 KB/hour via subdomains

**Discussion points after reveal:**
- "Why is DNS hard to monitor?"
- "What would a normal DNS query pattern look like?"
- "How would you distinguish data exfil from normal DNS activity?"

### Physical Security Bypass (T-20)
**Real-world context:**
- RFID cloning demonstrated on hotel keys, building badges
- Rogue network devices found in data centers (Target breach had physical component)
- USB drops with malware remain effective attack vectors

**Discussion points after reveal:**
- "Should cybersecurity teams care about physical security?"
- "How do you audit data center access?"
- "What's harder to defend: cyber or physical attacks?"

---

## Expansion Threat Card Deck Summary

| Card | Title | Step | Vector | Difficulty |
|------|-------|------|--------|------------|
| T-13 | Compromised Software Vendor Update | INITIAL | WEB EXPLOIT | Hard |
| T-14 | Malicious Third-Party Library Injection | INITIAL | MALWARE | Medium |
| T-15 | Malicious Insider Data Theft | C2 & EXFIL | DATA EXFIL | Very Hard |
| T-16 | Disgruntled Employee Sabotage | PIVOT & ESCALATE | MALWARE | Hard |
| T-17 | Compromised IoT Device as Pivot Point | INITIAL | NETWORK | Medium |
| T-18 | Cloud API Token Theft & Abuse | PIVOT & ESCALATE | CREDENTIAL ABUSE | Hard |
| T-19 | DNS Tunneling Data Exfiltration | C2 & EXFIL | DATA EXFIL | Very Hard |
| T-20 | Physical Access + Badge Cloning | INITIAL | CREDENTIAL ABUSE | Hard |

---

## Quick Integration Checklist

- [ ] Print expansion threat cards on different colored cardstock (e.g., gold) to distinguish from base deck
- [ ] Create corresponding expansion defense cards for each threat type
- [ ] Add expansion cards to scenario briefings with "*Advanced Scenario*" label
- [ ] Brief threat orchestrators on real-world context (provided above)
- [ ] Adjust starting budget (+20) if using expansion cards to offset higher difficulty
- [ ] Consider extending turn limit (8-12) for scenarios with 5+ cards
- [ ] Create hybrid scenarios mixing base + expansion cards for variety

---

*Expansion Threat Card Set for Incident Zero*  
*Use these cards to add modern threat scenarios to your game*  
*For discussion and teaching notes, see above sections*