# Incident Zero: Sample Card Sheets

## Quick Reference
- **Threat Cards:** Represent attacker actions organized by kill chain step and attack vector
- **Defense Cards:** Player tools to counter attacks, costing 10/15/25 Budget based on tier
- **Print Tip:** Cut along dotted lines; consider printing on cardstock for durability

---

## THREAT CARDS

### Attack Chain Steps
- `INITIAL COMPROMISE` - First entry point
- `PIVOT & ESCALATE` - Movement and privilege escalation
- `PERSISTENCE` - Maintaining access
- `C2 & EXFIL` - Command & control and data theft

### Attack Vectors (Countermeasure Keywords)
- `SOCIAL ENGINEERING`
- `WEB EXPLOIT`
- `CREDENTIAL ABUSE`
- `MALWARE`
- `NETWORK`
- `DATA EXFIL`

---

## SAMPLE THREAT CARD DECK (12 Cards)

### INITIAL COMPROMISE THREATS

#### Card T-01: Phishing Campaign
```
┌─────────────────────────────────────┐
│ THREAT CARD                         │
├─────────────────────────────────────┤
│ PHISHING CAMPAIGN                   │
├─────────────────────────────────────┤
│ Step:    INITIAL COMPROMISE         │
│ Vector:  SOCIAL ENGINEERING         │
├─────────────────────────────────────┤
│ CLUE FOR THREAT ORCHESTRATOR:       │
│ "Your security team reports that    │
│ several employees have received     │
│ emails claiming to be from your     │
│ IT department requesting password   │
│ resets. One user has already        │
│ clicked the link. Email headers     │
│ show the domain is spoofed."        │
├─────────────────────────────────────┤
│ WHY THIS WORKS:                     │
│ Phishing exploits human psychology  │
│ rather than technical vulnerabilities.│
│ Attackers use social engineering to │
│ create urgency and bypass technical │
│ controls. With email authentication │
│ (DMARC/SPF) and user training, this │
│ attack is highly preventable.       │
└─────────────────────────────────────┘
```

#### Card T-02: Watering Hole Attack
```
┌─────────────────────────────────────┐
│ THREAT CARD                         │
├─────────────────────────────────────┤
│ WATERING HOLE ATTACK                │
├─────────────────────────────────────┤
│ Step:    INITIAL COMPROMISE         │
│ Vector:  WEB EXPLOIT                │
├─────────────────────────────────────┤
│ CLUE FOR THREAT ORCHESTRATOR:       │
│ "A popular industry blog your       │
│ employees frequently visit has      │
│ been compromised. Logs show that    │
│ your users' browsers were           │
│ redirected to a malicious domain    │
│ hosting an exploit kit targeting    │
│ unpatched browsers."                │
├─────────────────────────────────────┤
│ WHY THIS WORKS:                     │
│ Watering hole attacks target        │
│ trusted third-party sites to infect │
│ specific user groups. They bypass   │
│ email filters and exploit browser   │
│ vulnerabilities. Defense requires   │
│ rapid patching and endpoint         │
│ monitoring.                         │
└─────────────────────────────────────┘
```

#### Card T-03: Compromised Credentials
```
┌─────────────────────────────────────┐
│ THREAT CARD                         │
├─────────────────────────────────────┤
│ COMPROMISED CREDENTIALS             │
├─────────────────────────────────────┤
│ Step:    INITIAL COMPROMISE         │
│ Vector:  CREDENTIAL ABUSE           │
├─────────────────────────────────────┤
│ CLUE FOR THREAT ORCHESTRATOR:       │
│ "Your SIEM has detected a           │
│ successful VPN login from an        │
│ unusual geographic location at      │
│ 3 AM. The username belongs to an    │
│ employee who is currently on        │
│ vacation. The login attempt came    │
│ from an IP in a known cybercrime    │
│ hosting provider."                  │
├─────────────────────────────────────┤
│ WHY THIS WORKS:                     │
│ Credential stuffing uses passwords  │
│ leaked from third-party breaches.   │
│ If employees reuse passwords, their │
│ work accounts become compromised.   │
│ Multi-factor authentication (MFA)   │
│ is the primary defense.             │
└─────────────────────────────────────┘
```

---

### PIVOT & ESCALATE THREATS

#### Card T-04: Lateral Movement via SMB
```
┌─────────────────────────────────────┐
│ THREAT CARD                         │
├─────────────────────────────────────┤
│ LATERAL MOVEMENT VIA SMB            │
├─────────────────────────────────────┤
│ Step:    PIVOT & ESCALATE           │
│ Vector:  NETWORK                    │
├─────────────────────────────────────┤
│ CLUE FOR THREAT ORCHESTRATOR:       │
│ "Network segmentation alerts show   │
│ unusual SMB traffic between a       │
│ compromised workstation and your    │
│ file server. Suspicious named pipe  │
│ activity detected. The attacker     │
│ appears to be enumerating shares    │
│ and attempting to access restricted │
│ resources."                         │
├─────────────────────────────────────┤
│ WHY THIS WORKS:                     │
│ SMB (Server Message Block) is a     │
│ legitimate protocol, so traffic     │
│ blends in. Flat network architecture│
│ allows attackers to move freely.    │
│ Without micro-segmentation and      │
│ strong authentication, lateral      │
│ movement is easy.                   │
└─────────────────────────────────────┘
```

#### Card T-05: Privilege Escalation via Kernel Exploit
```
┌─────────────────────────────────────┐
│ THREAT CARD                         │
├─────────────────────────────────────┤
│ PRIVILEGE ESCALATION VIA KERNEL     │
├─────────────────────────────────────┤
│ Step:    PIVOT & ESCALATE           │
│ Vector:  MALWARE                    │
├─────────────────────────────────────┤
│ CLUE FOR THREAT ORCHESTRATOR:       │
│ "EDR telemetry shows a suspicious   │
│ process creating a scheduled task   │
│ with SYSTEM privileges. The         │
│ scheduled task executes a           │
│ PowerShell script that attempts to  │
│ access the Domain Controller. The   │
│ script appears to be using living-  │
│ off-the-land techniques."           │
├─────────────────────────────────────┤
│ WHY THIS WORKS:                     │
│ Kernel exploits bypass security     │
│ boundaries. Attackers use built-in  │
│ Windows tools (PowerShell, schtasks)│
│ to avoid detection. Unpatched       │
│ systems and over-privileged service │
│ accounts make this highly effective.│
└─────────────────────────────────────┘
```

#### Card T-06: Mimikatz Credential Dumping
```
┌─────────────────────────────────────┐
│ THREAT CARD                         │
├─────────────────────────────────────┤
│ MIMIKATZ CREDENTIAL DUMPING         │
├─────────────────────────────────────┤
│ Step:    PIVOT & ESCALATE           │
│ Vector:  CREDENTIAL ABUSE           │
├─────────────────────────────────────┤
│ CLUE FOR THREAT ORCHESTRATOR:       │
│ "Memory forensics analysis on the   │
│ Domain Controller reveals suspicious│
│ LSASS process manipulation. A tool  │
│ has dumped credential hashes from   │
│ memory. Several cached domain admin │
│ credentials have been extracted.    │
│ Attacker now has credentials to     │
│ move to critical systems."          │
├─────────────────────────────────────┤
│ WHY THIS WORKS:                     │
│ Mimikatz attacks Windows LSASS      │
│ (Local Security Authority Subsystem)│
│ memory to extract credentials.      │
│ Without proper Credential Guard and │
│ memory protection, domain admin     │
│ credentials become compromised,     │
│ enabling full infrastructure access.│
└─────────────────────────────────────┘
```

---

### PERSISTENCE THREATS

#### Card T-07: Scheduled Task Persistence
```
┌─────────────────────────────────────┐
│ THREAT CARD                         │
├─────────────────────────────────────┤
│ SCHEDULED TASK PERSISTENCE          │
├─────────────────────────────────────┤
│ Step:    PERSISTENCE                │
│ Vector:  MALWARE                    │
├─────────────────────────────────────┤
│ CLUE FOR THREAT ORCHESTRATOR:       │
│ "Log analysis shows a scheduled     │
│ task created by the compromised     │
│ account. The task is set to execute │
│ every 6 hours and runs a script     │
│ from a hidden directory. The        │
│ activity occurs outside normal      │
│ business hours. Timestamp metadata  │
│ indicates advanced timestomping."   │
├─────────────────────────────────────┤
│ WHY THIS WORKS:                     │
│ Scheduled tasks run with privileges │
│ of the owner account and survive    │
│ reboots. They blend in with         │
│ legitimate administrative tasks.    │
│ Windows Event Logs may not be       │
│ forwarded centrally, allowing this  │
│ persistence mechanism to hide.      │
└─────────────────────────────────────┘
```

#### Card T-08: Registry Run Key Persistence
```
┌─────────────────────────────────────┐
│ THREAT CARD                         │
├─────────────────────────────────────┤
│ REGISTRY RUN KEY PERSISTENCE        │
├─────────────────────────────────────┤
│ Step:    PERSISTENCE                │
│ Vector:  MALWARE                    │
├─────────────────────────────────────┤
│ CLUE FOR THREAT ORCHESTRATOR:       │
│ "Registry analysis detects a new    │
│ entry in HKLM\\System\\CurrentVersion│
│ \\Run pointing to an executable in  │
│ an unusual location. The binary has │
│ obfuscated metadata and a fake      │
│ digital signature. It executes at   │
│ every system startup."              │
├─────────────────────────────────────┤
│ WHY THIS WORKS:                     │
│ Registry Run keys execute at startup│
│ with persistence across reboots.    │
│ They're difficult to distinguish    │
│ from legitimate startup programs.   │
│ Endpoint detection solutions must   │
│ actively monitor registry writes.   │
└─────────────────────────────────────┘
```

---

### C2 & EXFIL THREATS

#### Card T-09: Beaconing to C2 Server
```
┌─────────────────────────────────────┐
│ THREAT CARD                         │
├─────────────────────────────────────┤
│ BEACONING TO C2 SERVER              │
├─────────────────────────────────────┤
│ Step:    C2 & EXFIL                 │
│ Vector:  NETWORK                    │
├─────────────────────────────────────┤
│ CLUE FOR THREAT ORCHESTRATOR:       │
│ "Your threat intelligence feed      │
│ alerts on suspicious outbound       │
│ HTTPS connections to a domain       │
│ associated with known malware.      │
│ Netflow shows regular 3-minute      │
│ intervals of encrypted traffic.     │
│ The pattern matches documented C2   │
│ beaconing behavior."                │
├─────────────────────────────────────┤
│ WHY THIS WORKS:                     │
│ Beaconing establishes command and   │
│ control communication with the      │
│ attacker's infrastructure. Encrypted│
│ HTTPS makes payload inspection      │
│ difficult. Threat intelligence and  │
│ behavioral analysis (unusual timing)│
│ are required for detection.         │
└─────────────────────────────────────┘
```

#### Card T-10: SQL Database Exfiltration
```
┌─────────────────────────────────────┐
│ THREAT CARD                         │
├─────────────────────────────────────┤
│ SQL DATABASE EXFILTRATION           │
├─────────────────────────────────────┤
│ Step:    C2 & EXFIL                 │
│ Vector:  DATA EXFIL                 │
├─────────────────────────────────────┤
│ CLUE FOR THREAT ORCHESTRATOR:       │
│ "Database audit logs show a large   │
│ SELECT query executed by a service  │
│ account retrieving customer data.   │
│ Results (500k+ records) were piped  │
│ to a temporary file. System logs    │
│ show this file was copied to cloud  │
│ storage via encrypted connection."  │
├─────────────────────────────────────┤
│ WHY THIS WORKS:                     │
│ Database exfiltration bypasses      │
│ endpoint controls. Attackers use    │
│ legitimate protocols (HTTPS, SFTP)  │
│ to trusted services (S3, Dropbox).  │
│ Without DLP (Data Loss Prevention),  │
│ and egress filtering, detection is  │
│ nearly impossible.                  │
└─────────────────────────────────────┘
```

#### Card T-11: Ransomware Payload Deployment
```
┌─────────────────────────────────────┐
│ THREAT CARD                         │
├─────────────────────────────────────┤
│ RANSOMWARE PAYLOAD DEPLOYMENT       │
├─────────────────────────────────────┤
│ Step:    C2 & EXFIL                 │
│ Vector:  MALWARE                    │
├─────────────────────────────────────┤
│ CLUE FOR THREAT ORCHESTRATOR:       │
│ "EDR alerts spike as multiple       │
│ processes begin encrypting files    │
│ on the file server. Hundreds of     │
│ files change extension to '.locked'.│
│ A ransom note appears on all        │
│ administrative workstations. Network│
│ traffic shows exfil before encryption│
│ began (double extortion tactic)."   │
├─────────────────────────────────────┤
│ WHY THIS WORKS:                     │
│ Modern ransomware exfiltrates data  │
│ first (to extort payment), then     │
│ encrypts. Fast detection during the │
│ exfil phase is critical. Once file  │
│ encryption begins, recovery becomes │
│ difficult. Segmentation and backups │
│ are essential.                      │
└─────────────────────────────────────┘
```

#### Card T-12: Browser Extension Backdoor
```
┌─────────────────────────────────────┐
│ THREAT CARD                         │
├─────────────────────────────────────┤
│ BROWSER EXTENSION BACKDOOR          │
├─────────────────────────────────────┤
│ Step:    C2 & EXFIL                 │
│ Vector:  DATA EXFIL                 │
├─────────────────────────────────────┤
│ CLUE FOR THREAT ORCHESTRATOR:       │
│ "Browser logs show installation of  │
│ a suspicious extension claiming to  │
│ be a productivity tool. Traffic     │
│ analysis reveals the extension is   │
│ capturing keystrokes and session    │
│ cookies. User login credentials for │
│ sensitive portals are being sent to │
│ a server in a high-risk country."   │
├─────────────────────────────────────┤
│ WHY THIS WORKS:                     │
│ Browser extensions run with full    │
│ access to user activity. They can   │
│ capture credentials, intercept      │
│ HTTPS traffic (before encryption),  │
│ and persist across browser updates. │
│ Extension vetting and endpoint      │
│ protection are critical defenses.   │
└─────────────────────────────────────┘
```

---

## DEFENSE CARDS

### Tier System
- **BASIC (10 Budget):** Fundamental tools and procedures
- **ADVANCED (15 Budget):** Specialized investigative techniques
- **ELITE (25 Budget):** Cutting-edge detection and response

### Countermeasure Vectors
Defense cards counter specific Attack Vectors:
- `SOCIAL ENGINEERING`
- `WEB EXPLOIT`
- `CREDENTIAL ABUSE`
- `MALWARE`
- `NETWORK`
- `DATA EXFIL`

---

## SAMPLE DEFENSE CARD DECK (24 Cards)

### BASIC DEFENSES (10 Budget Each)

#### Card D-01: Email Authentication Setup
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ EMAIL AUTHENTICATION SETUP          │
│ (BASIC - 10 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: SOCIAL ENGINEERING  │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy SPF (Sender Policy           │
│ Framework), DKIM (DomainKeys        │
│ Identified Mail), and DMARC (Domain │
│ Message Authentication, Reporting & │
│ Conformance) to prevent email       │
│ spoofing. Implement enforcement     │
│ policies to reject spoofed emails.  │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Blocks phishing emails claiming to  │
│ be from your domain. Requires       │
│ attackers to find alternative       │
│ vectors. Also provides reporting on │
│ spoofing attempts.                  │
└─────────────────────────────────────┘
```

#### Card D-02: User Security Training
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ USER SECURITY TRAINING              │
│ (BASIC - 10 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: SOCIAL ENGINEERING  │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Conduct phishing awareness training │
│ for all staff. Teach recognition of │
│ suspicious links, sender spoofing,  │
│ urgency tactics, and credential     │
│ harvesting attempts. Run simulated  │
│ phishing campaigns.                 │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Reduces successful phishing rate by │
│ 70-80%. Users become your first     │
│ line of defense. Works best when    │
│ combined with technical controls.   │
└─────────────────────────────────────┘
```

#### Card D-03: Windows Update Patching
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ WINDOWS UPDATE PATCHING             │
│ (BASIC - 10 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: WEB EXPLOIT         │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy automated Windows Update     │
│ management across all systems.      │
│ Establish patch deployment timelines│
│ (critical = 48 hours, high = 2      │
│ weeks). Audit compliance with patch │
│ reporting.                          │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Closes browser and kernel           │
│ vulnerabilities. Prevents watering  │
│ hole and exploit kit attacks.       │
│ Should be combined with vulnerability│
│ scanning to identify gaps.          │
└─────────────────────────────────────┘
```

#### Card D-04: Network Firewall Rules
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ NETWORK FIREWALL RULES              │
│ (BASIC - 10 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: NETWORK             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy perimeter firewall rules to  │
│ block unauthorized outbound         │
│ protocols. Default-deny for unusual │
│ ports and known malware C2 domains. │
│ Whitelist only necessary business   │
│ traffic.                            │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Prevents early-stage lateral        │
│ movement and C2 beaconing.          │
│ Slows attacker reconnaissance.      │
│ Must be maintained with threat      │
│ intelligence feeds.                 │
└─────────────────────────────────────┘
```

#### Card D-05: Log Centralization
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ LOG CENTRALIZATION                  │
│ (BASIC - 10 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: MALWARE             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy centralized log aggregation  │
│ (syslog, Splunk, ELK). Forward      │
│ Windows Event Logs, firewall logs,  │
│ DNS queries, and proxy logs to      │
│ central SIEM. Configure syslog      │
│ integrity protection.               │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Makes local log tampering difficult.│
│ Provides investigative visibility   │
│ into attacker activities. Foundation│
│ for threat hunting and compliance.  │
└─────────────────────────────────────┘
```

#### Card D-06: Basic Antivirus Deployment
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ BASIC ANTIVIRUS DEPLOYMENT          │
│ (BASIC - 10 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: MALWARE             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy signature-based antivirus    │
│ across all endpoints. Enable        │
│ automatic definition updates        │
│ (daily). Configure real-time file   │
│ and email scanning.                 │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Catches known malware variants.     │
│ Does not detect zero-day or        │
│ polymorphic malware. Useful as part │
│ of defense-in-depth but insufficient│
│ as primary defense.                 │
└─────────────────────────────────────┘
```

---

### ADVANCED DEFENSES (15 Budget Each)

#### Card D-07: Multi-Factor Authentication (MFA)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ MULTI-FACTOR AUTHENTICATION (MFA)   │
│ (ADVANCED - 15 Budget)              │
├─────────────────────────────────────┤
│ Countermeasure: CREDENTIAL ABUSE    │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy MFA for all remote access    │
│ (VPN, RDP), email, and admin        │
│ portals. Use authenticator apps or  │
│ hardware tokens (not SMS). Enforce  │
│ MFA on sensitive user accounts.     │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Makes compromised credentials       │
│ useless without the second factor.  │
│ Blocks credential stuffing attacks. │
│ Most effective single security      │
│ measure against account takeover.   │
└─────────────────────────────────────┘
```

#### Card D-08: EDR (Endpoint Detection & Response)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ EDR (ENDPOINT DETECTION & RESPONSE) │
│ (ADVANCED - 15 Budget)              │
├─────────────────────────────────────┤
│ Countermeasure: MALWARE             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy EDR agent on all endpoints.  │
│ Monitor process execution, file     │
│ creation, registry modifications,   │
│ and memory injection attempts.      │
│ Enable behavioral analytics and     │
│ automated response.                 │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Detects living-off-the-land attacks │
│ (PowerShell, cmd, scheduled tasks). │
│ Enables fast incident response and  │
│ threat hunting. Provides deep       │
│ visibility into attack progression. │
└─────────────────────────────────────┘
```

#### Card D-09: Network Segmentation
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ NETWORK SEGMENTATION                │
│ (ADVANCED - 15 Budget)              │
├─────────────────────────────────────┤
│ Countermeasure: NETWORK             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Implement VLANs and microsegmentation│
│ to separate user workstations from  │
│ servers. Deploy firewall rules      │
│ between segments. Implement zero-   │
│ trust network access controls.      │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Prevents lateral movement via SMB   │
│ and other internal protocols.       │
│ Limits blast radius of compromise.  │
│ Forces attackers to find alternate  │
│ paths. Combined with MFA, highly    │
│ effective.                          │
└─────────────────────────────────────┘
```

#### Card D-10: SIEM Correlation Rules
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ SIEM CORRELATION RULES              │
│ (ADVANCED - 15 Budget)              │
├─────────────────────────────────────┤
│ Countermeasure: NETWORK             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Create SIEM rules to detect attack  │
│ patterns: failed login spikes,      │
│ privilege escalation attempts,      │
│ unusual process creation, scheduled │
│ task creation, and data exfil       │
│ indicators.                         │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Correlates events across logs to    │
│ detect multi-step attacks. Reduces  │
│ alert fatigue through smart         │
│ aggregation. Enables faster         │
│ investigation and response.         │
└─────────────────────────────────────┘
```

#### Card D-11: Data Loss Prevention (DLP)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ DATA LOSS PREVENTION (DLP)          │
│ (ADVANCED - 15 Budget)              │
├─────────────────────────────────────┤
│ Countermeasure: DATA EXFIL          │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy DLP to monitor outbound data │
│ transfers. Classify sensitive data  │
│ (customer PII, source code, trade   │
│ secrets). Block or alert on         │
│ unauthorized transfers to cloud     │
│ storage, email, USB, or external    │
│ networks.                           │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Prevents SQL database exfiltration  │
│ and bulk data theft. Detects        │
│ unusual data access patterns.       │
│ Enforces data security policies.    │
│ Works best with strong authentication│
│ and encryption.                     │
└─────────────────────────────────────┘
```

#### Card D-12: Password Manager & Vault
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ PASSWORD MANAGER & VAULT            │
│ (ADVANCED - 15 Budget)              │
├─────────────────────────────────────┤
│ Countermeasure: CREDENTIAL ABUSE    │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy enterprise password vault    │
│ (CyberArk, HashiCorp Vault). Enforce│
│ strong unique passwords. Implement  │
│ password rotation policies for      │
│ service accounts. Enable audit      │
│ logging for credential access.      │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Prevents credential reuse attacks.  │
│ Makes credential stuffing difficult.│
│ Provides audit trail for compliance │
│ and incident investigation.         │
└─────────────────────────────────────┘
```

---

### ELITE DEFENSES (25 Budget Each)

#### Card D-13: Threat Hunting Program
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ THREAT HUNTING PROGRAM              │
│ (ELITE - 25 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: MALWARE             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Establish proactive threat hunting  │
│ using MITRE ATT&CK framework.       │
│ Hunt for living-off-the-land        │
│ techniques, anomalous processes,    │
│ suspicious registry changes, and    │
│ memory injection. Use automated     │
│ tools (OSQuery, Velociraptor).      │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Finds advanced attacks that bypass  │
│ signature-based detection. Detects  │
│ LSASS dumping, scheduled task       │
│ persistence, and registry backdoors.│
│ Reduces dwell time significantly.   │
└─────────────────────────────────────┘
```

#### Card D-14: Memory Forensics
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ MEMORY FORENSICS                    │
│ (ELITE - 25 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: MALWARE             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy memory capture and analysis  │
│ (Volatility, Memoryze). Create      │
│ memory images of suspicious systems.│
│ Analyze for credential dumping,     │
│ injected code, and rootkits. Extract│
│ evidence for incident response.     │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Detects Mimikatz attacks and        │
│ credential harvesting. Reveals      │
│ attacker activities hidden from     │
│ disk forensics. Critical for        │
│ identifying advanced persistence    │
│ mechanisms.                         │
└─────────────────────────────────────┘
```

#### Card D-15: Deception Technology (Honeypots)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ DECEPTION TECHNOLOGY (HONEYPOTS)    │
│ (ELITE - 25 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: NETWORK             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy decoy systems (fake file     │
│ servers, databases, credentials)    │
│ to detect lateral movement. Create  │
│ canary tokens that alert when       │
│ accessed. Deploy honeypots for web  │
│ exploit detection.                  │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Any access to honeypots indicates   │
│ active compromise. Detects lateral  │
│ movement with zero false positives. │
│ Slows attacker progress and forces  │
│ reconnaissance, increasing detection│
│ time.                               │
└─────────────────────────────────────┘
```

#### Card D-16: Credential Guard & Secure Boot
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ CREDENTIAL GUARD & SECURE BOOT      │
│ (ELITE - 25 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: CREDENTIAL ABUSE    │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Enable Windows Credential Guard to  │
│ isolate LSASS in virtualized        │
│ container. Implement UEFI Secure    │
│ Boot to prevent bootkit attacks.    │
│ Enable TPM attestation for device   │
│ integrity validation.               │
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Makes Mimikatz credential dumping   │
│ ineffective. Prevents bootloader    │
│ manipulation. Ensures firmware      │
│ integrity. Blocks entire classes of │
│ attacks targeting early boot stage. │
└─────────────────────────────────────┘
```

#### Card D-17: Advanced Malware Sandbox
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ ADVANCED MALWARE SANDBOX            │
│ (ELITE - 25 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: MALWARE             │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy advanced sandboxing solution │
│ (Cuckoo, Detonate, hybrid-analysis).│
│ Analyze suspicious files/URLs in    │
│ isolated environments. Generate     │
│ behavioral indicators and YARA      │
│ rules. Share IOCs with threat intel.│
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Detects zero-day malware and unknown│
│ exploits. Analyzes evasion tactics. │
│ Generates detection rules for SIEM. │
│ Prevents spread of novel malware.   │
└─────────────────────────────────────┘
```

#### Card D-18: Intrusion Prevention System (IPS)
```
┌─────────────────────────────────────┐
│ DEFENSE CARD                        │
├─────────────────────────────────────┤
│ INTRUSION PREVENTION SYSTEM (IPS)   │
│ (ELITE - 25 Budget)                 │
├─────────────────────────────────────┤
│ Countermeasure: WEB EXPLOIT         │
├─────────────────────────────────────┤
│ DESCRIPTION:                        │
│ Deploy network-based IPS with       │
│ exploit signatures. Monitor for     │
│ known CVE exploitation patterns.    │
│ Configure WAF (Web Application      │
│ Firewall) rules for SQL injection,  │
│ XSS, and other OWASP Top 10 attacks.│
├─────────────────────────────────────┤
│ EFFECT:                             │
│ Blocks exploitation attempts in     │
│ transit. Prevents watering hole and │
│ web exploit attacks. Most effective │
│ when combined with patching.        │
└─────────────────────────────────────┘
```

---

## Sample Printable Card Layouts

### Print Instructions
1. Print on cardstock (250 gsm minimum)
2. Cut along dotted lines
3. Optional: Laminate or use sleeves for durability
4. For color printing: Use the color-coded vectors (red for MALWARE, blue for CREDENTIAL ABUSE, etc.)

### Recommended Colors for Vectors
- **SOCIAL ENGINEERING:** Red
- **WEB EXPLOIT:** Orange
- **CREDENTIAL ABUSE:** Blue
- **MALWARE:** Purple
- **NETWORK:** Green
- **DATA EXFIL:** Cyan

---

## Card Deck Summary

### Threat Cards (12 Total)
- INITIAL COMPROMISE: 3 cards
- PIVOT & ESCALATE: 3 cards
- PERSISTENCE: 2 cards
- C2 & EXFIL: 4 cards

### Defense Cards (24 Total)
- BASIC (10 Budget): 6 cards
- ADVANCED (15 Budget): 6 cards
- ELITE (25 Budget): 6 cards

**Distribution by Countermeasure:**
- SOCIAL ENGINEERING: 2 defenses
- WEB EXPLOIT: 2 defenses
- CREDENTIAL ABUSE: 4 defenses
- MALWARE: 6 defenses
- NETWORK: 4 defenses
- DATA EXFIL: 2 defenses

---

## Suggested Play Scenarios

### Scenario 1: Startup Security Breach (3-card chain - Beginner)
1. Phishing Campaign → Deploy Email Authentication or User Training
2. Mimikatz Credential Dumping → Deploy MFA or Credential Guard
3. Data Exfiltration via Browser Extension → Deploy DLP or Threat Hunting

### Scenario 2: SMB Lateral Movement (4-card chain - Intermediate)
1. Compromised Credentials → Deploy MFA
2. Lateral Movement via SMB → Deploy Network Segmentation
3. Privilege Escalation → Deploy EDR or Threat Hunting
4. Beaconing to C2 → Deploy Firewall Rules or IPS

### Scenario 3: Advanced Ransomware Campaign (5-card chain - Expert)
1. Watering Hole Attack → Deploy Patching or IPS
2. Privilege Escalation via Kernel Exploit → Deploy EDR
3. Scheduled Task Persistence → Deploy Memory Forensics
4. Mimikatz Credential Dumping → Deploy Credential Guard
5. Ransomware Deployment → Deploy DLP and Deception Technology

---

## Expansion Ideas

### Additional Threat Cards to Create
- Supply chain attacks
- Insider threats
- IoT device compromise
- Cloud API abuse
- DNS tunneling for data exfil
- Physical security bypass

### Additional Defense Cards to Create
- Application whitelisting
- Behavioral analytics
- Container security
- Cloud security posture management
- Incident response playbooks
- Backup & disaster recovery

---

*Sample card sheets for Incident Zero board game*
*For complete game rules, see incident-zero-game-spec.md*