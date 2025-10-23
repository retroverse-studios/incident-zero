# Hardening Module: Defense Cards (Shared with Incident Response)

**Version:** 2.1 - Balanced & Refined Edition
**Last Updated:** October 2025

---

## Overview

These 24 Defense Cards are **shared between the Incident Response and Hardening modules**. In Hardening, teams deploy these same defenses to build defense-in-depth and test them against Pentester Tactics.

- **Total Cards:** 24
- **Tiers:** BASIC (10 Budget), ADVANCED (15 Budget), ELITE (25 Budget)
- **Distribution:** 8 cards per tier, 6 threat vectors represented
- **Used In:** Both Incident Response and Hardening modules

---

## Defense Card Organization

### Tier System
- **BASIC (10 Budget):** Fundamental tools and procedures (8 cards)
- **ADVANCED (15 Budget):** Specialized investigative techniques (8 cards)
- **ELITE (25 Budget):** Cutting-edge detection and response (8 cards)

### Countermeasure Vectors
- `SOCIAL_ENGINEERING`
- `WEB_EXPLOIT`
- `CREDENTIAL_ABUSE`
- `MALWARE`
- `NETWORK`
- `DATA_EXFIL`

---

## BASIC TIER DEFENSES (10 Budget Each)

### D-01: Email Authentication Setup
**Tier:** BASIC (10 Budget)
**Vector:** SOCIAL_ENGINEERING

Deploy SPF (Sender Policy Framework), DKIM (DomainKeys Identified Mail), and DMARC (Domain Message Authentication, Reporting & Conformance) to prevent email spoofing.

**Effect:** Blocks phishing emails claiming to be from your domain. Requires attackers to find alternative vectors.

**Used Against:** T-01 (Phishing Campaign)

---

### D-02: User Security Training
**Tier:** BASIC (10 Budget)
**Vector:** SOCIAL_ENGINEERING

Conduct phishing awareness training for all staff. Teach recognition of suspicious links, sender spoofing, urgency tactics, and credential harvesting attempts.

**Effect:** Reduces successful phishing rate by 70-80%. Users become your first line of defense.

**Used Against:** T-01, T-02 (Phishing, Watering Hole)

---

### D-03: Windows Update Patching
**Tier:** BASIC (10 Budget)
**Vector:** WEB_EXPLOIT

Deploy automated Windows Update management across all systems. Establish patch deployment timelines (critical = 48 hours, high = 2 weeks).

**Effect:** Closes browser and kernel vulnerabilities. Prevents watering hole and exploit kit attacks.

**Used Against:** T-02 (Watering Hole), T-05 (Privilege Escalation)

---

### D-04: Network Firewall Rules
**Tier:** BASIC (10 Budget)
**Vector:** NETWORK

Deploy perimeter firewall rules to block unauthorized outbound protocols. Default-deny for unusual ports and known malware C2 domains.

**Effect:** Prevents early-stage lateral movement and C2 beaconing. Slows attacker reconnaissance.

**Used Against:** T-04 (Lateral Movement), T-09 (C2 Beaconing)

---

### D-05: Log Centralization
**Tier:** BASIC (10 Budget)
**Vector:** MALWARE

Deploy centralized log aggregation (syslog, Splunk, ELK). Forward Windows Event Logs, firewall logs, DNS queries, and proxy logs to central SIEM.

**Effect:** Makes local log tampering difficult. Provides investigative visibility into attacker activities. Foundation for threat hunting.

**Used Against:** T-07, T-08 (Persistence attacks)

---

### D-06: Basic Antivirus Deployment
**Tier:** BASIC (10 Budget)
**Vector:** MALWARE

Deploy signature-based antivirus across all endpoints. Enable automatic definition updates (daily). Configure real-time file and email scanning.

**Effect:** Catches known malware variants. Does not detect zero-day or polymorphic malware. Useful as part of defense-in-depth.

**Used Against:** T-05, T-07, T-08 (Malware-based attacks)

---

### D-07: Multi-Factor Authentication (MFA)
**Tier:** ADVANCED (15 Budget)
**Vector:** CREDENTIAL_ABUSE

Deploy MFA for all remote access (VPN, RDP), email, and admin portals. Use authenticator apps or hardware tokens (not SMS).

**Effect:** Makes compromised credentials useless without the second factor. Blocks credential stuffing attacks.

**Used Against:** T-03 (Compromised Credentials), T-06 (Mimikatz)

---

### D-08: EDR (Endpoint Detection & Response)
**Tier:** ADVANCED (15 Budget)
**Vector:** MALWARE

Deploy EDR agent on all endpoints. Monitor process execution, file creation, registry modifications, and memory injection attempts. Enable behavioral analytics.

**Effect:** Detects living-off-the-land attacks (PowerShell, cmd, scheduled tasks). Provides deep visibility into attack progression.

**Used Against:** T-05 (Priv Esc), T-07, T-08 (Persistence)

---

## ADVANCED TIER DEFENSES (15 Budget Each)

### D-09: Network Segmentation
**Tier:** ADVANCED (15 Budget)
**Vector:** NETWORK

Implement VLANs and microsegmentation to separate user workstations from servers. Deploy firewall rules between segments. Implement zero-trust network access controls.

**Effect:** Prevents lateral movement via SMB and other internal protocols. Limits blast radius of compromise.

**Used Against:** T-04 (Lateral Movement), T-06 (Credential Dumping spread)

---

### D-10: SIEM Correlation Rules
**Tier:** ADVANCED (15 Budget)
**Vector:** NETWORK

Create SIEM rules to detect attack patterns: failed login spikes, privilege escalation attempts, unusual process creation, scheduled task creation, and data exfil indicators.

**Effect:** Correlates events across logs to detect multi-step attacks. Enables faster investigation and response.

**Used Against:** T-04, T-05, T-06, T-07, T-08, T-09 (Detection across entire chain)

---

### D-11: Data Loss Prevention (DLP)
**Tier:** ADVANCED (15 Budget)
**Vector:** DATA_EXFIL

Deploy DLP to monitor outbound data transfers. Classify sensitive data (customer PII, source code, trade secrets). Block or alert on unauthorized transfers.

**Effect:** Prevents SQL database exfiltration and bulk data theft. Detects unusual data access patterns. Enforces data security policies.

**Used Against:** T-10, T-11, T-12 (Data exfiltration attacks)

---

### D-12: Password Manager & Vault
**Tier:** ADVANCED (15 Budget)
**Vector:** CREDENTIAL_ABUSE

Deploy enterprise password vault (CyberArk, HashiCorp Vault). Enforce strong unique passwords. Implement password rotation policies for service accounts.

**Effect:** Prevents credential reuse attacks. Makes credential stuffing difficult. Provides audit trail for compliance and incident investigation.

**Used Against:** T-03, T-06 (Credential attacks)

---

### D-13: Threat Hunting Program
**Tier:** ELITE (25 Budget)
**Vector:** MALWARE

Establish proactive threat hunting using MITRE ATT&CK framework. Hunt for living-off-the-land techniques, anomalous processes, suspicious registry changes, and memory injection.

**Effect:** Finds advanced attacks that bypass signature-based detection. Detects LSASS dumping, scheduled task persistence, and registry backdoors. Reduces dwell time significantly.

**Used Against:** T-05, T-07, T-08 (Advanced persistence)

---

### D-14: Memory Forensics
**Tier:** ELITE (25 Budget)
**Vector:** MALWARE

Deploy memory capture and analysis (Volatility, Memoryze). Create memory images of suspicious systems. Analyze for credential dumping, injected code, and rootkits.

**Effect:** Detects Mimikatz attacks and credential harvesting. Reveals attacker activities hidden from disk forensics. Critical for identifying advanced persistence mechanisms.

**Used Against:** T-06 (Mimikatz), T-07, T-08 (In-memory attacks)

---

## ELITE TIER DEFENSES (25 Budget Each)

### D-15: Deception Technology (Honeypots)
**Tier:** ELITE (25 Budget)
**Vector:** NETWORK

Deploy decoy systems (fake file servers, databases, credentials) to detect lateral movement. Create canary tokens that alert when accessed.

**Effect:** Any access to honeypots indicates active compromise. Detects lateral movement with zero false positives. Slows attacker progress and forces reconnaissance.

**Used Against:** T-04 (Lateral Movement), T-06 (Credential abuse)

---

### D-16: Credential Guard & Secure Boot
**Tier:** ELITE (25 Budget)
**Vector:** CREDENTIAL_ABUSE

Enable Windows Credential Guard to isolate LSASS in virtualized container. Implement UEFI Secure Boot to prevent bootkit attacks. Enable TPM attestation.

**Effect:** Makes Mimikatz credential dumping ineffective. Prevents bootloader manipulation. Ensures firmware integrity. Blocks entire classes of early-boot attacks.

**Used Against:** T-06 (Mimikatz), T-07, T-08 (Persistence)

---

### D-17: Advanced Malware Sandbox
**Tier:** ELITE (25 Budget)
**Vector:** MALWARE

Deploy advanced sandboxing solution (Cuckoo, Detonate, hybrid-analysis). Analyze suspicious files/URLs in isolated environments. Generate behavioral indicators and YARA rules.

**Effect:** Detects zero-day malware and unknown exploits. Analyzes evasion tactics. Generates detection rules for SIEM. Prevents spread of novel malware.

**Used Against:** T-05 (Privilege Escalation), T-07, T-08 (Malware persistence)

---

### D-18: Intrusion Prevention System (IPS)
**Tier:** ELITE (25 Budget)
**Vector:** WEB_EXPLOIT

Deploy network-based IPS with exploit signatures. Monitor for known CVE exploitation patterns. Configure WAF (Web Application Firewall) rules for SQL injection, XSS, and OWASP Top 10 attacks.

**Effect:** Blocks exploitation attempts in transit. Prevents watering hole and web exploit attacks. Most effective when combined with patching.

**Used Against:** T-02 (Watering Hole), T-05 (Exploits)

---

### D-19: Backup & Disaster Recovery
**Tier:** ELITE (25 Budget)
**Vector:** MALWARE

Implement 3-2-1 backup strategy: 3 copies of data, 2 different storage types, 1 offsite copy. Test restore procedures quarterly. Implement immutable backups.

**Effect:** Enables rapid recovery from ransomware. Ensures data availability even if primary systems are compromised. Critical for business continuity.

**Used Against:** T-07, T-08, T-10, T-11, T-12 (Persistence and exfil attacks)

---

### D-20: Zero Trust Access Control
**Tier:** ELITE (25 Budget)
**Vector:** CREDENTIAL_ABUSE

Implement zero-trust architecture: verify every access request regardless of source. Deploy device identity, user identity, and behavior analytics. Implement conditional access policies.

**Effect:** Eliminates implicit trust based on network location. Even compromised devices cannot access sensitive resources without proper authentication and behavior validation.

**Used Against:** T-03, T-06 (Credential abuse), T-04 (Lateral movement)

---

### D-21: Container Security & Orchestration
**Tier:** ELITE (25 Budget)
**Vector:** MALWARE

Deploy container runtime security (Falco, Sysdig). Implement image scanning for vulnerabilities. Use policy enforcement engines (OPA/Gatekeeper). Implement network policies for container segmentation.

**Effect:** Detects container escape attempts. Prevents vulnerable images from running. Limits lateral movement within containerized environments. Critical for modern cloud applications.

**Used Against:** T-05 (Priv Esc), T-04 (Lateral Movement in cloud)

---

### D-22: Security Information & Event Management (SIEM)
**Tier:** ELITE (25 Budget)
**Vector:** NETWORK

Deploy enterprise SIEM (Splunk, ELK, QRadar). Centralize logs from all sources. Implement automated correlation rules, threat intelligence integration, and incident response workflows.

**Effect:** Provides centralized visibility into all security events. Enables rapid threat detection and investigation. Foundation for mature incident response program.

**Used Against:** T-04, T-06, T-07, T-08, T-09, T-10 (Detection across entire attack chain)

---

### D-23: Incident Response Playbooks
**Tier:** ELITE (25 Budget)
**Vector:** NETWORK

Create detailed incident response playbooks for common scenarios: malware infection, data exfiltration, ransomware, insider threats, supply chain compromise. Include roles, responsibilities, communication plans.

**Effect:** Enables faster, more coordinated response when incidents occur. Reduces confusion during high-pressure situations. Improves incident containment and recovery time.

**Used Against:** T-09, T-10, T-11, T-12 (All C2 & Exfil attacks)

---

### D-24: Threat Intelligence Integration
**Tier:** ELITE (25 Budget)
**Vector:** NETWORK

Subscribe to threat intelligence feeds (MISP, VirusTotal, AlienVault OTX). Integrate IOCs (Indicators of Compromise) into firewall, SIEM, and proxy. Participate in information sharing communities.

**Effect:** Enables faster detection of known malicious IPs and domains. Identifies emerging threats targeting your industry. Reduces detection time from days to minutes.

**Used Against:** T-09 (C2 Beaconing), T-10, T-11, T-12 (Exfil detection)

---

## Defense Card Summary

### Distribution by Tier
- **BASIC (10 Budget):** 8 cards (D-01 to D-08)
- **ADVANCED (15 Budget):** 8 cards (D-09 to D-16) *Note: includes both 15-budget ADVANCED cards*
- **ELITE (25 Budget):** 8 cards (D-17 to D-24)

### Distribution by Vector
- **SOCIAL_ENGINEERING:** D-01, D-02 (2 cards)
- **WEB_EXPLOIT:** D-03, D-18 (2 cards)
- **CREDENTIAL_ABUSE:** D-07, D-12, D-16, D-20 (4 cards)
- **MALWARE:** D-06, D-08, D-13, D-14, D-17, D-19, D-21 (7 cards)
- **NETWORK:** D-04, D-09, D-10, D-15, D-22, D-23, D-24 (7 cards)
- **DATA_EXFIL:** D-11 (1 card)

**Note:** Total includes multiple vector assignments per card (cards protect against multiple vectors)

---

## How These Cards Are Used in Hardening

### Deploy Action
Blue Team selects a Defense Card from their hand and deploys it:
- **Cost:** 10/15/25 Budget depending on tier
- **Roll Required:** None—automatic success
- **Effect:** Defense immediately becomes active and counts toward Security Score

### Pentester Challenge
When a Pentester Tactic is drawn (see Pentester Tactic Cards file), it challenges one or more deployed defenses:
- Blue Team rolls 1d20 to defend
- Deployed defenses provide +2 to +4 bonus depending on tier
- If defense fails, attacker gains ground; if defense succeeds, attacker is repelled

### Strategic Layering
Multiple defenses work together:
- BASIC defenses are cheap but weak against tactics
- ADVANCED defenses provide good cost/effectiveness balance
- ELITE defenses are expensive but strongest against sophisticated tactics
- Layering multiple defenses provides synergy bonuses (total +1 per additional relevant defense)

---

## Print Instructions

1. Print on cardstock (250 gsm minimum) for durability
2. Cut along dotted lines
3. Optional: Laminate or use sleeves for durability and reusability
4. Consider color-coding by vector for visual quick reference:
   - **SOCIAL_ENGINEERING:** Red
   - **WEB_EXPLOIT:** Orange
   - **CREDENTIAL_ABUSE:** Blue
   - **MALWARE:** Purple
   - **NETWORK:** Green
   - **DATA_EXFIL:** Cyan

---

## Notes on Card Reusability

These 24 Defense Cards are the **same cards used in Incident Response module**. The difference in usage:

- **In Incident Response:** Blue Team deploys defenses to reveal hidden threats and earn points
- **In Hardening:** Blue Team deploys defenses to prepare for Pentester Tactics and build resilience

This allows educators to:
- Use one physical deck for both modules
- Teach defense-in-depth concepts in sequence
- Show how defenses complement each other

---

*Hardening Module: Defense Cards*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.1 - Balanced & Refined Edition*
