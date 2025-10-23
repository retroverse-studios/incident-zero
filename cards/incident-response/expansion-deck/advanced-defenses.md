# Incident Zero: Expansion Defense Cards
## Advanced Security Controls & Defensive Capabilities

This document provides additional Defense Cards for expanding **Incident Zero** gameplay beyond the base 24-card deck. These cards introduce modern security architectures and advanced defensive capabilities that complement the base game.

---

## ADDITIONAL DEFENSE CARDS (18 Cards)

### Application Whitelisting Defenses

#### Card D-19: Application Whitelisting (Basic)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ APPLICATION WHITELISTING            │
│ (BASIC - 10 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: MALWARE             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy application whitelisting on  │
│ critical workstations and servers.  │
│ Maintain an approved applications   │
│ list (Word, Excel, Chrome, etc.).   │
│ Block execution of any unapproved   │
│ binaries. Use AppLocker (Windows)   │
│ or similar tools.                   │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Prevents execution of malware and   │
│ unauthorized tools. Attackers cannot│
│ run ransomware, backdoors, or       │
│ penetration tools if they're not on │
│ the whitelist. Effective against    │
│ zero-days if not signed by trusted  │
│ publishers.                         │
│                                     │
│ LIMITATION: False positives if      │
│ maintenance is poor. Users may      │
│ struggle with legitimate tools      │
│ being blocked.                      │
└─────────────────────────────────────┘
```

#### Card D-20: Advanced Application Control with AI
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ ADVANCED APPLICATION CONTROL WITH AI│
│ (ADVANCED - 15 Budget)              │
├─────────────────────────────────────┤
│ Countermeasure: MALWARE             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy AI-powered application       │
│ control that learns normal program  │
│ execution patterns. System builds a │
│ baseline of legitimate applications │
│ and automatically flags deviations. │
│ Prevents execution of suspicious    │
│ or anomalous applications.          │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Combines whitelisting with behavior │
│ analysis. Adapts to legitimate new  │
│ applications without manual updates.│
│ Catches polymorphic malware variants│
│ that might bypass static whitelisting│
│ (different packing, slight name     │
│ changes). Reduces false positives.  │
│                                     │
│ LEARNING CURVE: Requires baseline   │
│ training period (1-2 weeks).        │
└─────────────────────────────────────┘
```

#### Card D-21: Living-Off-The-Land Blocker (ELITE)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ LIVING-OFF-THE-LAND BLOCKER         │
│ (ELITE - 25 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: MALWARE             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy advanced script and tool     │
│ control that restricts execution of │
│ PowerShell, WScript, cmd.exe, and   │
│ other "living-off-the-land" tools.  │
│ Allow only specific, monitored usage│
│ with strong justification logging.  │
│ Monitor for obfuscation patterns.   │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Directly targets attacker techniques│
│ used in privilege escalation and    │
│ lateral movement (scheduled tasks,  │
│ registry modification, credential   │
│ dumping). Makes PowerShell and cmd  │
│ attacks extremely difficult.        │
│ Works especially well with EDR.     │
│                                     │
│ IMPACT: May break legitimate admin  │
│ tasks; requires strong change       │
│ management.                         │
└─────────────────────────────────────┘
```

---

### Behavioral Analytics Defenses

#### Card D-22: Baseline Behavior Learning System (Advanced)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ BASELINE BEHAVIOR LEARNING SYSTEM   │
│ (ADVANCED - 15 Budget)              │
├─────────────────────────────────────┤
│ Countermeasure: NETWORK             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy behavioral analytics that    │
│ establishes baseline profiles for   │
│ users, systems, and network traffic.│
│ System learns what "normal" looks   │
│ like, then alerts on deviations.    │
│ Monitors: login times, file access, │
│ network destinations, resource usage.│
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Detects anomalies like:             │
│ - Unusual login geography/time      │
│ - Data access patterns changing     │
│ - Lateral movement via SMB          │
│ - New network destinations          │
│ Works best as a *combination* with  │
│ other tools. Requires good baseline  │
│ data (1-2 weeks of normal traffic). │
│                                     │
│ DETECTS: Insider threats,           │
│ compromised credentials, APT tactics.│
└─────────────────────────────────────┘
```

#### Card D-23: Process Behavior Analysis (Advanced)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ PROCESS BEHAVIOR ANALYSIS           │
│ (ADVANCED - 15 Budget)              │
├─────────────────────────────────────┤
│ Countermeasure: MALWARE             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy process-level behavioral     │
│ monitoring that learns what each    │
│ application normally does (file I/O,│
│ network calls, registry access,     │
│ child processes spawned). Blocks    │
│ anomalous behavior from legitimate  │
│ binaries.                           │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Catches:                            │
│ - Legitimate apps compromised by    │
│  supply chain attack                │
│ - Process injection attacks         │
│ - Unexpected child process creation │
│ - Anomalous registry/file writes    │
│ Example: Word.exe normally doesn't  │
│ spawn PowerShell; if it does, block │
│ and alert.                          │
│                                     │
│ DETECTS: Zero-day malware, APT      │
│ techniques, supply chain compromises.│
└─────────────────────────────────────┘
```

#### Card D-24: Machine Learning Anomaly Detection (ELITE)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ MACHINE LEARNING ANOMALY DETECTION  │
│ (ELITE - 25 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: MALWARE             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy ML models trained on terabytes│
│ of security data. System detects    │
│ subtle anomalies humans would miss: │
│ subtle timing changes, rare resource│
│ combinations, statistical outliers. │
│ Continuously retrains on new data.  │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Catches advanced attacks that bypass│
│ signature and rule-based systems.   │
│ Detects:                            │
│ - Polymorphic malware variations    │
│ - Advanced persistent threats (APT) │
│ - Zero-day exploits (by behavior)   │
│ - Sophisticated insider threats     │
│ - Supply chain compromises          │
│                                     │
│ TRADE-OFF: False positives require  │
│ human analysis. Requires large      │
│ datasets for training.              │
└─────────────────────────────────────┘
```

---

### Container Security Defenses

#### Card D-25: Container Image Scanning (Basic)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ CONTAINER IMAGE SCANNING            │
│ (BASIC - 10 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: MALWARE             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Scan all container images before    │
│ deployment for known vulnerabilities│
│ and malicious packages. Integrate   │
│ scanning into CI/CD pipeline.       │
│ Block images with critical CVEs     │
│ from being deployed.                │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Prevents deployment of vulnerable   │
│ containers. Catches:                │
│ - Old base images with known CVEs   │
│ - Malicious packages in dependencies│
│ - Secrets accidentally baked into   │
│ images                              │
│ Works best when combined with       │
│ runtime monitoring.                 │
│                                     │
│ LIMITATION: Only catches known      │
│ vulnerabilities (CVE databases).    │
└─────────────────────────────────────┘
```

#### Card D-26: Container Runtime Protection (Advanced)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ CONTAINER RUNTIME PROTECTION        │
│ (ADVANCED - 15 Budget)              │
├─────────────────────────────────────┤
│ Countermeasure: MALWARE             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy runtime security monitoring  │
│ that enforces security policies on  │
│ running containers. Monitor syscalls│
│ (system calls), network connections,│
│ and file access. Enforce AppArmor   │
│ or SELinux profiles.                │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Detects and blocks:                 │
│ - Container escape attempts         │
│ - Lateral movement between containers│
│ - Privilege escalation in container │
│ - Anomalous process execution       │
│ - Unexpected network connections    │
│ Works against both known and unknown│
│ attacks (zero-day exploits).        │
│                                     │
│ REQUIREMENT: Requires kernel-level  │
│ instrumentation; varies by platform.│
└─────────────────────────────────────┘
```

#### Card D-27: Kubernetes Network Policy & RBAC (ELITE)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ KUBERNETES NETWORK POLICY & RBAC    │
│ (ELITE - 25 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: NETWORK             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Implement Kubernetes network policies│
│ to restrict container-to-container  │
│ communication. Deploy role-based     │
│ access control (RBAC) for API access│
│ and service accounts. Enforce pod   │
│ security policies and admission     │
│ controllers.                        │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Implements micro-segmentation in    │
│ containerized environments. Prevents:│
│ - Lateral movement between pods     │
│ - Container escape attacks accessing │
│  host network                       │
│ - Privilege escalation via RBAC     │
│ - Unauthorized Kubernetes API access│
│                                     │
│ COMPLEXITY: Requires mature         │
│ Kubernetes operations and expertise. │
└─────────────────────────────────────┘
```

---

### Cloud Security Posture Management (CSPM)

#### Card D-28: Cloud Configuration Auditing (Basic)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ CLOUD CONFIGURATION AUDITING        │
│ (BASIC - 10 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: CREDENTIAL ABUSE    │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy continuous cloud configuration│
│ monitoring (AWS Config, Azure Policy│
│ Manager, GCP Cloud Asset Inventory).│
│ Scan for misconfigured resources:   │
│ - Public S3 buckets                 │
│ - Overly permissive IAM policies    │
│ - Unencrypted databases             │
│ - Open security groups              │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Detects misconfigurations that allow│
│ unauthorized access:                │
│ - Public database access            │
│ - Exposed credentials in configs    │
│ - Overly broad IAM permissions      │
│ - Disabled encryption/logging       │
│ Alert on drift from secure baseline.│
│                                     │
│ LIMITATION: Only catches known      │
│ misconfiguration patterns.          │
└─────────────────────────────────────┘
```

#### Card D-29: Cloud Access & Permission Auditing (Advanced)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ CLOUD ACCESS & PERMISSION AUDITING  │
│ (ADVANCED - 15 Budget)              │
├─────────────────────────────────────┤
│ Countermeasure: CREDENTIAL ABUSE    │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Audit all IAM roles, service        │
│ accounts, and API credentials for   │
│ over-privilege. Implement least-    │
│ privilege access. Regularly review  │
│ who has what permissions. Detect    │
│ and revoke unused credentials.      │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Prevents attackers from leveraging: │
│ - Exposed API keys with broad       │
│  permissions                        │
│ - Service accounts with admin access│
│ - Stale credentials from departed   │
│  employees                          │
│ - Cross-account trust abuse         │
│ Reduces blast radius if credentials │
│ are compromised.                    │
│                                     │
│ REQUIRES: Strong governance process │
│ to maintain least-privilege state.  │
└─────────────────────────────────────┘
```

#### Card D-30: Cloud Compliance & Audit Trail (ELITE)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ CLOUD COMPLIANCE & AUDIT TRAIL      │
│ (ELITE - 25 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: DATA EXFIL          │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Enable comprehensive cloud audit    │
│ logging (CloudTrail, Stackdriver,   │
│ Activity Monitor). Forward all logs  │
│ to immutable, centralized storage.  │
│ Monitor for unauthorized API calls, │
│ data access, and resource changes.  │
│ Enable MFA Delete on audit logs.    │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Provides forensic trail for:        │
│ - Detecting API token abuse        │
│ - Investigating data exfiltration   │
│ - Compliance reporting              │
│ - Incident response timeline        │
│ Prevents attackers from covering    │
│ tracks (immutable logs). Enables    │
│ rapid investigation of cloud API    │
│ compromises.                        │
│                                     │
│ COST: High storage requirements.    │
└─────────────────────────────────────┘
```

---

### Incident Response Playbooks

#### Card D-31: Playbook: Ransomware Response (Advanced)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ PLAYBOOK: RANSOMWARE RESPONSE       │
│ (ADVANCED - 15 Budget)              │
├─────────────────────────────────────┤
│ Countermeasure: MALWARE             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Pre-built, tested ransomware response│
│ playbook covering:                  │
│ - Immediate network isolation steps │
│ - Communication procedures          │
│ - Forensic data collection          │
│ - Restoration procedures            │
│ - Stakeholder notifications         │
│ Train incident response team on     │
│ playbook annually.                  │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ During Phase 2 or when ransomware   │
│ is detected:                        │
│ Get +4 bonus to defense rolls when  │
│ responding to ransomware threats.   │
│ Reduces response time, limiting     │
│ damage.                             │
│                                     │
│ EDUCATIONAL VALUE: Teaches incident │
│ response process and coordination.  │
└─────────────────────────────────────┘
```

#### Card D-32: Playbook: Credential Compromise Response (Advanced)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ PLAYBOOK: CREDENTIAL COMPROMISE     │
│ RESPONSE                            │
│ (ADVANCED - 15 Budget)              │
├─────────────────────────────────────┤
│ Countermeasure: CREDENTIAL ABUSE    │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Pre-built playbook for credential   │
│ compromise scenarios:               │
│ - Identify affected accounts        │
│ - Forced password reset procedures  │
│ - Session invalidation              │
│ - MFA re-enrollment process         │
│ - Forensic user activity review     │
│ - Privileged account audit          │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ When investigating compromised      │
│ credentials:                        │
│ Get +4 bonus to defense rolls.      │
│ Allows rapid containment before     │
│ lateral movement occurs.            │
│                                     │
│ EXAMPLE USE: During "Mimikatz       │
│ Credential Dumping" threat, playbook│
│ helps isolate affected accounts.    │
└─────────────────────────────────────┘
```

#### Card D-33: Playbook: Insider Threat Response (ELITE)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ PLAYBOOK: INSIDER THREAT RESPONSE   │
│ (ELITE - 25 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: DATA EXFIL          │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Comprehensive insider threat        │
│ response playbook including:        │
│ - HR coordination protocols         │
│ - Legal review and preservation     │
│ - Forensic evidence collection      │
│ - Physical security response        │
│ - System access removal procedures  │
│ - Communication to management       │
│ Requires cross-functional team      │
│ coordination.                       │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ When responding to insider threats: │
│ Get +5 bonus to defense rolls.      │
│ Requires strong organizational      │
│ processes to be effective.          │
│                                     │
│ EXAMPLE USE: When "Malicious        │
│ Insider Data Theft" is detected,    │
│ playbook coordinates response across │
│ security, HR, legal, and executives.│
└─────────────────────────────────────┘
```

#### Card D-34: Playbook: Supply Chain Breach Response (ELITE)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ PLAYBOOK: SUPPLY CHAIN BREACH       │
│ RESPONSE                            │
│ (ELITE - 25 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: WEB EXPLOIT         │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Specialized playbook for supply     │
│ chain compromises:                  │
│ - Vendor notification procedures    │
│ - Industry coordination             │
│ - Affected system inventory         │
│ - Patch deployment prioritization   │
│ - Third-party impact assessment     │
│ - Public communication strategy     │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ During Phase 2 when defending       │
│ against supply chain attacks:       │
│ Get +5 bonus to defense rolls.      │
│ Requires vendor relationships and   │
│ industry collaboration.             │
│                                     │
│ LEARNING: Teaches that supply chain │
│ incidents require industry response.│
└─────────────────────────────────────┘
```

---

### Backup & Disaster Recovery

#### Card D-35: Backup Strategy - 3-2-1 Rule (Basic)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ BACKUP STRATEGY - 3-2-1 RULE        │
│ (BASIC - 10 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: MALWARE             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Implement the 3-2-1 backup rule:    │
│ - 3 copies of data                  │
│ - 2 different media types           │
│ - 1 copy offline/offsite            │
│ Regular backup verification testing.│
│ Document retention and recovery RPO/│
│ RTO (Recovery Point/Time Objectives).│
├─────────────────────────────────────┤
│ EFFECT:                             │
│ If ransomware encrypts data:        │
│ Recovery becomes possible without   │
│ paying ransom. Offline backups      │
│ ensure attacker cannot delete them. │
│ Reduces ransomware attack impact    │
│ significantly.                      │
│                                     │
│ LIMITATION: Only effective if       │
│ backups are regularly tested and    │
│ truly offline.                      │
└─────────────────────────────────────┘
```

#### Card D-36: Immutable Backup Storage (Advanced)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ IMMUTABLE BACKUP STORAGE            │
│ (ADVANCED - 15 Budget)              │
├─────────────────────────────────────┤
│ Countermeasure: MALWARE             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy backup storage with WORM     │
│ (Write-Once-Read-Many) protection.  │
│ Once backups are written, they      │
│ cannot be modified or deleted,      │
│ even by administrators. Implement   │
│ MFA Delete on storage. Use air-gapped│
│ backup network.                     │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Even if attacker gains admin access │
│ or compromises backup system:       │
│ Backups remain protected and        │
│ unmodifiable. Enables guaranteed    │
│ recovery. Works against double-     │
│ extortion ransomware attacks.       │
│                                     │
│ COST: Higher storage cost for       │
│ immutable solutions.                │
└─────────────────────────────────────┘
```

#### Card D-37: Disaster Recovery Plan & Testing (ELITE)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ DISASTER RECOVERY PLAN & TESTING    │
│ (ELITE - 25 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: MALWARE             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Establish comprehensive disaster    │
│ recovery plan (DRP) including:      │
│ - Failover procedures               │
│ - Alternate site readiness          │
│ - Recovery procedures (step-by-step)│
│ - Communication protocols           │
│ - Key personnel contacts            │
│ Conduct quarterly DRP drills and    │
│ recovery testing.                   │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ During ransomware or supply chain   │
│ attacks:                            │
│ Get +3 bonus to all defense rolls   │
│ after initial containment. Enables  │
│ business continuity.                │
│                                     │
│ EDUCATIONAL VALUE: Teaches business │
│ continuity planning and resilience. │
└─────────────────────────────────────┘
```

---

## Defense Card Integration Guide

### By Threat Type Mapping

**Against Supply Chain Attacks (T-13, T-14):**
- D-25: Container Image Scanning
- D-31: Software Composition Analysis
- D-28: Cloud Configuration Auditing

**Against Insider Threats (T-15, T-16):**
- D-22: Baseline Behavior Learning System
- D-23: Process Behavior Analysis
- D-33: Playbook: Insider Threat Response

**Against IoT Compromise (T-17):**
- D-19: Application Whitelisting
- D-25: Container Image Scanning (if containerized)
- D-22: Baseline Behavior Learning System

**Against Cloud API Abuse (T-18):**
- D-28: Cloud Configuration Auditing
- D-29: Cloud Access & Permission Auditing
- D-30: Cloud Compliance & Audit Trail

**Against DNS Tunneling (T-19):**
- D-22: Baseline Behavior Learning System (network baseline)
- D-24: Machine Learning Anomaly Detection

**Against Physical Security Bypass (T-20):**
- D-22: Baseline Behavior Learning System (detection)
- D-32: Playbook: Credential Compromise Response

**Against Ransomware (T-11, supply chain variants):**
- D-35: Backup Strategy - 3-2-1 Rule
- D-36: Immutable Backup Storage
- D-37: Disaster Recovery Plan & Testing
- D-31: Playbook: Ransomware Response

---

## Sample Defense Card Combinations

### "Enterprise Ransomware Defense" (4 cards, 60 Budget)
- D-35: Backup Strategy - 3-2-1 Rule (10 Budget)
- D-36: Immutable Backup Storage (15 Budget)
- D-26: Container Runtime Protection (15 Budget)
- D-31: Playbook: Ransomware Response (15 Budget)
- **Total Effect:** Multi-layered ransomware defense with recovery guarantee

### "Cloud-Native Security" (4 cards, 55 Budget)
- D-25: Container Image Scanning (10 Budget)
- D-27: Kubernetes Network Policy & RBAC (25 Budget)
- D-29: Cloud Access & Permission Auditing (15 Budget)
- D-30: Cloud Compliance & Audit Trail (25 Budget) - *Adjusted*
- **Total Effect:** Comprehensive containerized environment protection

### "Insider Threat Detection & Response" (4 cards, 70 Budget)
- D-22: Baseline Behavior Learning System (15 Budget)
- D-24: Machine Learning Anomaly Detection (25 Budget)
- D-33: Playbook: Insider Threat Response (25 Budget)
- D-35: Backup Strategy - 3-2-1 Rule (10 Budget)
- **Total Effect:** Multi-stage insider threat defense

### "Zero-Trust Architecture" (5 cards, 75 Budget)
- D-21: Living-Off-The-Land Blocker (25 Budget)
- D-23: Process Behavior Analysis (15 Budget)
- D-27: Kubernetes Network Policy & RBAC (25 Budget)
- D-29: Cloud Access & Permission Auditing (15 Budget)
- D-22: Baseline Behavior Learning System (15 Budget) - *Adjusted*
- **Total Effect:** Comprehensive assume-breach architecture

---

## Phase 2 Hardening with Expansion Defense Cards

### Phase 2 Scenario: Enterprise Defense Build-Out (90 minutes)

**Starting Budget:** 150 (inflated for comprehensive build)

**Turn 1-3: Foundation (BASIC tier)**
- D-28: Cloud Configuration Auditing (10)
- D-19: Application Whitelisting (10)
- D-35: Backup Strategy - 3-2-1 Rule (10)
- **Running Total:** 30 Budget spent

**Turn 4-6: Advanced Layer (ADVANCED tier)**
- D-22: Baseline Behavior Learning System (15)
- D-26: Container Runtime Protection (15)
- D-29: Cloud Access & Permission Auditing (15)
- D-31: Playbook: Ransomware Response (15)
- **Running Total:** 90 Budget spent

**Turn 7-9: Expert Layer (ELITE tier)**
- D-30: Cloud Compliance & Audit Trail (25)
- D-24: Machine Learning Anomaly Detection (25)
- D-37: Disaster Recovery Plan & Testing (25)
- **Running Total:** 165 Budget (over budget - teams must choose)

**Final Security Score Calculation:**
- (7 defenses deployed × 5) = 35 points
- (3 hardening upgrades × 2) = 6 points
- (2 playbooks × 10) = 20 points
- (4 pentester tactic evasions × 5) = 20 points
- **Total: 81 points** (Strong defense-in-depth)

---

## Pentester Tactic Card Interactions with Defense Cards

When a Pentester Tactic Card is drawn in Phase 2, specific Defense Cards provide bonuses:

### Tactic 1: "Bypass Basic Defenses"
- **Countered by:** D-20 (Advanced Application Control)
- **Effect:** +2 to defense roll (upgrades to Advanced tier effectiveness)

### Tactic 2: "Social Engineering Specialist"
- **Countered by:** D-22 or D-24 (Behavioral Analytics)
- **Effect:** +2 to defense roll (baseline deviation detected)

### Tactic 3: "Persistence Expert"
- **Countered by:** D-23 (Process Behavior Analysis)
- **Effect:** +3 to defense roll (anomalous process creation detected)

### Tactic 4: "Supply Chain Attack"
- **Countered by:** D-25 (Container Image Scanning) or D-31 (SCA equivalent)
- **Effect:** +3 to defense roll (malicious dependency detected)

### Tactic 5: "Detection Evasion"
- **Countered by:** D-24 (Machine Learning Anomaly Detection)
- **Effect:** +4 to defense roll (behavioral anomaly detected despite evasion)

### Tactic 6: "Budget Drain"
- **Countered by:** D-37 (Disaster Recovery Plan)
- **Effect:** Reduce budget drain by 5 (efficiency improvement)

### Tactic 7: "Zero-Day Exploit"
- **Countered by:** D-21 (Living-Off-The-Land Blocker) or D-22/D-24 (Behavioral Analysis)
- **Effect:** +2 to defense roll (behavior-based detection of exploit)

### Tactic 8: "Multi-Vector Attack"
- **Countered by:** D-27 (Kubernetes Network Policy) or D-29 (Cloud RBAC)
- **Effect:** Defend against both vectors (segmentation prevents coordination)

---

## Teaching Notes for Defense Card Expansion

### Application Whitelisting (D-19, D-20, D-21)
**Why it matters:**
- Stops 90%+ of malware variants if properly configured
- "Defense in depth" - cheap to start, expensive to perfect
- Trade-off: Security vs. usability (users can't run unauthorized apps)

**Real-world context:**
- Used by government agencies and financial institutions
- Apple's approach (iOS/macOS sandboxing)
- Increasingly common in "zero trust" architectures

**Discussion points:**
- "What's blocked by living-off-the-land blocker that regular whitelisting isn't?"
- "Why is adoption slow despite effectiveness?"

### Behavioral Analytics (D-22, D-23, D-24)
**Why it matters:**
- Catches attacks that don't match known signatures
- Foundation for modern threat detection
- Requires "normal" baseline to be effective

**Real-world context:**
- Splunk, Elastic, Sentinel use behavioral analytics
- UEBA systems detect insider threats
- Process behavior monitoring by Crowdstrike, Falcon, Tanium

**Discussion points:**
- "What counts as 'abnormal' and who decides?"
- "How do you build a baseline without including attacks?"
- "Why can't signature-based antivirus do this?"

### Container Security (D-25, D-26, D-27)
**Why it matters:**
- Container environments have unique attack surfaces
- Rapid deployment means traditional approaches fail
- Network segmentation at container level is powerful

**Real-world context:**
- Kubernetes is now the standard container orchestrator
- Docker/container adoption is 90%+ in enterprises
- Container escape vulnerabilities (runc, containerd, etc.)

**Discussion points:**
- "How is container security different from VM security?"
- "Why is network policy critical in Kubernetes?"
- "What's an example of a container escape attack?"

### Cloud Security Posture Management (D-28, D-29, D-30)
**Why it matters:**
- Cloud misconfigurations are leading breach cause
- Shared responsibility model confuses organizations
- API-driven access requires different monitoring

**Real-world context:**
- Hundreds of millions exposed via public S3 buckets
- Capital One breach: misconfigured WAF
- Equifax: unpatched open-source component in cloud environment

**Discussion points:**
- "Who's responsible for cloud security: vendor or organization?"
- "How do you audit permissions when there are 1000s of IAM roles?"
- "Why is 'least privilege' hard to achieve in practice?"

### Incident Response Playbooks (D-31, D-32, D-33, D-34)
**Why it matters:**
- Pre-planning reduces response time significantly
- Coordination across teams is critical
- Written procedures prevent panic decisions

**Real-world context:**
- Organizations without playbooks average 9+ month detection time
- With playbooks, average drops to 3-4 months
- Playbooks required by HIPAA, PCI-DSS, NIST frameworks

**Discussion points:**
- "Who should be involved in ransomware response?"
- "How do you balance forensics with business recovery?"
- "Why test playbooks if you hope to never use them?"

### Backup & Disaster Recovery (D-35, D-36, D-37)
**Why it matters:**
- Ransomware made backups critical (not just compliance)
- Recovery is often cheapest way to respond to attacks
- Immutable backups prevent attacker deletion

**Real-world context:**
- Many ransomware attacks double-extort (steal + encrypt)
- Immutable backups became critical after backup deletion attacks
- AWS S3, Azure Blob WORM protection adopted widely

**Discussion points:**
- "Can backups be targeted by attackers?"
- "What's the difference between backup and disaster recovery?"
- "Why would immutable backups be controversial?"

---

## Expansion Defense Card Deck Summary

| Card | Title | Tier | Budget | Countermeasure |
|------|-------|------|--------|-----------------|
| D-19 | Application Whitelisting | BASIC | 10 | MALWARE |
| D-20 | Advanced Application Control with AI | ADVANCED | 15 | MALWARE |
| D-21 | Living-Off-The-Land Blocker | ELITE | 25 | MALWARE |
| D-22 | Baseline Behavior Learning System | ADVANCED | 15 | NETWORK |
| D-23 | Process Behavior Analysis | ADVANCED | 15 | MALWARE |
| D-24 | Machine Learning Anomaly Detection | ELITE | 25 | MALWARE |
| D-25 | Container Image Scanning | BASIC | 10 | MALWARE |
| D-26 | Container Runtime Protection | ADVANCED | 15 | MALWARE |
| D-27 | Kubernetes Network Policy & RBAC | ELITE | 25 | NETWORK |
| D-28 | Cloud Configuration Auditing | BASIC | 10 | CREDENTIAL ABUSE |
| D-29 | Cloud Access & Permission Auditing | ADVANCED | 15 | CREDENTIAL ABUSE |
| D-30 | Cloud Compliance & Audit Trail | ELITE | 25 | DATA EXFIL |
| D-31 | Playbook: Ransomware Response | ADVANCED | 15 | MALWARE |
| D-32 | Playbook: Credential Compromise Response | ADVANCED | 15 | CREDENTIAL ABUSE |
| D-33 | Playbook: Insider Threat Response | ELITE | 25 | DATA EXFIL |
| D-34 | Playbook: Supply Chain Breach Response | ELITE | 25 | WEB EXPLOIT |
| D-35 | Backup Strategy - 3-2-1 Rule | BASIC | 10 | MALWARE |
| D-36 | Immutable Backup Storage | ADVANCED | 15 | MALWARE |
| D-37 | Disaster Recovery Plan & Testing | ELITE | 25 | MALWARE |

**Total Expansion Cards:** 19
**Budget Range:** 10 (BASIC) to 25 (ELITE)
**Distribution:** 5 BASIC, 8 ADVANCED, 6 ELITE

---

## Building Custom Scenarios with Expansion Cards

### Template: "Expert Level Scenario"

**Setup:**
- 5-card threat chain (mix of base + expansion threats)
- Starting Budget: 120
- Turn Limit: 10

**Phase 1 Attack Chain Example:**
1. Compromised Software Vendor Update (T-13) → WEB EXPLOIT
2. Lateral Movement via SMB (T-04) → NETWORK
3. Cloud API Token Theft (T-18) → CREDENTIAL ABUSE
4. Disgruntled Employee Sabotage (T-16) → MALWARE
5. Data Exfiltration (T-19: DNS Tunneling) → DATA EXFIL

**Phase 1 Recommended Defense Starting Hand:**
- D-25: Container Image Scanning (10)
- D-22: Baseline Behavior Learning System (15)
- D-28: Cloud Configuration Auditing (10)
- D-29: Cloud Access & Permission Auditing (15)
- D-31: Playbook: Ransomware Response (15) - *reusable*

**Phase 2 Hardening Strategy:**
- Deploy D-26, D-27 for container security
- Deploy D-30 for cloud audit trails
- Deploy D-24 for insider threat detection
- Prepare D-33 playbook for insider coordination

**Pentester Tactics to Draw (Phase 2):**
1. "Supply Chain Attack" (countered by D-25, D-31)
2. "Detection Evasion" (countered by D-24)
3. "Multi-Vector Attack" (countered by D-27, D-29)

---

## Printable Card Layout

### Print Instructions
1. Print on cardstock (250 gsm minimum)
2. Use different color for expansion deck (e.g., teal background vs. white)
3. Cut along dotted lines
4. Consider laminating or card sleeves
5. Store in separate box from base deck

### Color Coding Suggestions
- **BASIC:** Light color (cream/ivory)
- **ADVANCED:** Medium color (light blue/gray)
- **ELITE:** Dark color (dark blue/purple)

---

## Recommended Deck Combinations

### Complete Game with All Cards
- **Base Threat Cards:** 12
- **Expansion Threat Cards:** 8
- **Total Threats:** 20

- **Base Defense Cards:** 24
- **Expansion Defense Cards:** 19
- **Total Defenses:** 43

**Recommended Play:** Use subsets based on experience level
- **Beginners:** Base deck only
- **Intermediate:** Base + 4 expansion threats (choose scenario)
- **Advanced:** Base + all expansion cards

---

## Quick Integration Checklist

- [ ] Print expansion defense cards on different color cardstock
- [ ] Create a separate deck organizer for expansion cards
- [ ] Brief threat orchestrators on new defense mechanics
- [ ] Create scenario cards showing which defenses are available
- [ ] Update Phase 2 hardening rules with new cards
- [ ] Prepare Pentester Tactic interaction chart
- [ ] Test scenarios with expansion cards before classroom use
- [ ] Create reference sheet linking threats to countering defenses

---

*Expansion Defense Card Set for Incident Zero*  
*Use these cards to add modern security controls to your game*  
*For integration guides and teaching notes, see above sections*