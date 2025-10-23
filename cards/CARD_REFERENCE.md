# Incident Zero: Card Reference Index

Comprehensive index of all cards across all modules. Use this document to quickly find cards, understand their properties, and see relationships between cards.

---

## Quick Navigation

- [Incident Response Module Cards](#incident-response-module-cards)
- [Defense Cards by Vector](#defense-cards-by-vector)
- [Threat Cards by Step](#threat-cards-by-step)
- [Hardening Module Cards](#hardening-module-cards)
- [Other Module Cards](#other-module-cards)
- [Card Properties Reference](#card-properties-reference)

---

## Incident Response Module Cards

### Core Threat Deck (12 Cards)

#### INITIAL COMPROMISE (3 cards)

| Card ID | Name | Vector | Cost | Best Against | File |
|---------|------|--------|------|--------------|------|
| T-01 | Phishing Campaign | SOCIAL_ENGINEERING | 5 | Email-based attacks | core-deck/threat-defense-cards.md |
| T-02 | Watering Hole Attack | WEB_EXPLOIT | 5 | Web-based initial access | core-deck/threat-defense-cards.md |
| T-03 | Credential Harvesting (Form) | CREDENTIAL_ABUSE | 5 | Credential stealing | core-deck/threat-defense-cards.md |

#### PIVOT & ESCALATE (5 cards)

| Card ID | Name | Vector | Cost | Best Against | File |
|---------|------|--------|------|--------------|------|
| T-04 | Lateral Movement via SMB | NETWORK | 5 | Network reconnaissance | core-deck/threat-defense-cards.md |
| T-05 | Privilege Escalation (Kernel Exploit) | MALWARE | 5 | Local privilege escalation | core-deck/threat-defense-cards.md |
| T-06 | Mimikatz Credential Dumping | CREDENTIAL_ABUSE | 5 | Credential extraction | core-deck/threat-defense-cards.md |
| T-07 | Scheduled Task Persistence | MALWARE | 5 | Persistence establishment | core-deck/threat-defense-cards.md |
| T-08 | Registry Run Key Persistence | MALWARE | 5 | Persistence establishment | core-deck/threat-defense-cards.md |

#### PERSISTENCE (2 cards)

| Card ID | Name | Vector | Cost | Best Against | File |
|---------|------|--------|------|--------------|------|
| T-09 | Beaconing to C2 Server | NETWORK | 5 | C2 communication | core-deck/threat-defense-cards.md |
| T-10 | SQL Database Exfiltration | DATA_EXFIL | 5 | Data theft | core-deck/threat-defense-cards.md |

#### C2 & EXFIL (2 cards)

| Card ID | Name | Vector | Cost | Best Against | File |
|---------|------|--------|------|--------------|------|
| T-11 | Ransomware Payload Deployment | MALWARE | 5 | Ransomware infection | core-deck/threat-defense-cards.md |
| T-12 | File Encryption & Ransom Note | MALWARE | 5 | Data encryption | core-deck/threat-defense-cards.md |

---

### Core Defense Deck (24 Cards)

#### BASIC TIER (10 Budget) - 8 Cards

| Card ID | Name | Vector | Cost | Effect | File |
|---------|------|--------|------|--------|------|
| D-01 | Email Authentication Setup | SOCIAL_ENGINEERING | 10 | Validates email senders | core-deck/threat-defense-cards.md |
| D-02 | User Security Training | SOCIAL_ENGINEERING | 10 | Reduces phishing success | core-deck/threat-defense-cards.md |
| D-03 | Firewall Rules | NETWORK | 10 | Blocks unauthorized traffic | core-deck/threat-defense-cards.md |
| D-04 | Basic Antivirus | MALWARE | 10 | Detects known malware | core-deck/threat-defense-cards.md |
| D-05 | Password Policy Enforcement | CREDENTIAL_ABUSE | 10 | Enforces strong passwords | core-deck/threat-defense-cards.md |
| D-06 | DLP (Basic) | DATA_EXFIL | 10 | Monitors data movement | core-deck/threat-defense-cards.md |
| D-07 | Web Input Validation | WEB_EXPLOIT | 10 | Prevents injection attacks | core-deck/threat-defense-cards.md |
| D-08 | Backup System (Offline) | DATA_EXFIL | 10 | Recovery from data loss | core-deck/threat-defense-cards.md |

#### ADVANCED TIER (15 Budget) - 8 Cards

| Card ID | Name | Vector | Cost | Effect | File |
|---------|------|--------|------|--------|------|
| D-09 | Multi-Factor Authentication | CREDENTIAL_ABUSE | 15 | Second factor for auth | core-deck/threat-defense-cards.md |
| D-10 | EDR (Endpoint Detection & Response) | MALWARE | 15 | Detects process anomalies | core-deck/threat-defense-cards.md |
| D-11 | Network Segmentation | NETWORK | 15 | Isolates network zones | core-deck/threat-defense-cards.md |
| D-12 | SIEM (Security Information & Event Management) | NETWORK | 15 | Centralizes logging | core-deck/threat-defense-cards.md |
| D-13 | Web Application Firewall | WEB_EXPLOIT | 15 | Protects web apps | core-deck/threat-defense-cards.md |
| D-14 | IDS (Intrusion Detection System) | NETWORK | 15 | Detects intrusions | core-deck/threat-defense-cards.md |
| D-15 | Email Gateway | SOCIAL_ENGINEERING | 15 | Blocks phishing emails | core-deck/threat-defense-cards.md |
| D-16 | Credential Guard | CREDENTIAL_ABUSE | 15 | Protects credential storage | core-deck/threat-defense-cards.md |

#### ELITE TIER (25 Budget) - 8 Cards

| Card ID | Name | Vector | Cost | Effect | File |
|---------|------|--------|------|--------|------|
| D-17 | Threat Hunting | MALWARE | 25 | Proactive threat search | core-deck/threat-defense-cards.md |
| D-18 | Memory Forensics | CREDENTIAL_ABUSE | 25 | Analyzes memory dumps | core-deck/threat-defense-cards.md |
| D-19 | Deception Technology (Honeypots) | NETWORK | 25 | Traps for attackers | core-deck/threat-defense-cards.md |
| D-20 | Behavioral Analytics | MALWARE | 25 | Detects anomalies | core-deck/threat-defense-cards.md |
| D-21 | Zero Trust Architecture | NETWORK | 25 | Never trust, always verify | core-deck/threat-defense-cards.md |
| D-22 | Advanced DLP | DATA_EXFIL | 25 | Smart data protection | core-deck/threat-defense-cards.md |
| D-23 | Threat Intelligence Integration | WEB_EXPLOIT | 25 | Real-time threat data | core-deck/threat-defense-cards.md |
| D-24 | Incident Response Playbook | SOCIAL_ENGINEERING | 25 | Automated IR procedures | core-deck/threat-defense-cards.md |

---

### Expansion Threat Deck (8 Cards)

| Card ID | Name | Vector | Step | File |
|---------|------|--------|------|------|
| T-13 | Compromised Software Vendor Update | WEB_EXPLOIT | INITIAL_COMPROMISE | expansion-deck/advanced-threats.md |
| T-14 | Malicious Third-Party Library Injection | WEB_EXPLOIT | INITIAL_COMPROMISE | expansion-deck/advanced-threats.md |
| T-15 | API Credential Theft (Cloud) | CREDENTIAL_ABUSE | INITIAL_COMPROMISE | expansion-deck/advanced-threats.md |
| T-16 | DNS Hijacking | NETWORK | INITIAL_COMPROMISE | expansion-deck/advanced-threats.md |
| T-17 | Data Staging & Exfil | DATA_EXFIL | PERSISTENCE | expansion-deck/advanced-threats.md |
| T-18 | Command & Control Polymorphism | NETWORK | C2_EXFIL | expansion-deck/advanced-threats.md |
| T-19 | Ransomware as a Service (RaaS) | MALWARE | C2_EXFIL | expansion-deck/advanced-threats.md |
| T-20 | Zero-Day Exploitation | WEB_EXPLOIT | INITIAL_COMPROMISE | expansion-deck/advanced-threats.md |

---

### Expansion Defense Deck (8 Cards)

| Card ID | Name | Vector | Tier | File |
|---------|------|--------|------|------|
| D-25 | Supply Chain Risk Management | WEB_EXPLOIT | ADVANCED | expansion-deck/advanced-defenses.md |
| D-26 | Cloud Security Posture Management | WEB_EXPLOIT | ADVANCED | expansion-deck/advanced-defenses.md |
| D-27 | API Rate Limiting & Monitoring | WEB_EXPLOIT | ADVANCED | expansion-deck/advanced-defenses.md |
| D-28 | DNS Security (DNSSEC) | NETWORK | ADVANCED | expansion-deck/advanced-defenses.md |
| D-29 | Code Signing Verification | MALWARE | ADVANCED | expansion-deck/advanced-defenses.md |
| D-30 | Ransomware-Specific Behavior Detection | MALWARE | ELITE | expansion-deck/advanced-defenses.md |
| D-31 | Polymorphic Detection Signatures | NETWORK | ELITE | expansion-deck/advanced-defenses.md |
| D-32 | Zero-Day Exploit Mitigations | WEB_EXPLOIT | ELITE | expansion-deck/advanced-defenses.md |

---

## Defense Cards by Vector

### SOCIAL_ENGINEERING Defenses
- D-01: Email Authentication Setup (BASIC, 10)
- D-02: User Security Training (BASIC, 10)
- D-15: Email Gateway (ADVANCED, 15)
- D-24: Incident Response Playbook (ELITE, 25)

**Total:** 4 cards

**Covers:** Phishing, social engineering, pretexting

---

### WEB_EXPLOIT Defenses
- D-07: Web Input Validation (BASIC, 10)
- D-13: Web Application Firewall (ADVANCED, 15)
- D-23: Threat Intelligence Integration (ELITE, 25)
- D-25: Supply Chain Risk Management (ADVANCED, 15)
- D-26: Cloud Security Posture Management (ADVANCED, 15)
- D-27: API Rate Limiting & Monitoring (ADVANCED, 15)
- D-32: Zero-Day Exploit Mitigations (ELITE, 25)

**Total:** 7 cards

**Covers:** Web exploits, injection attacks, supply chain

---

### CREDENTIAL_ABUSE Defenses
- D-05: Password Policy Enforcement (BASIC, 10)
- D-09: Multi-Factor Authentication (ADVANCED, 15)
- D-16: Credential Guard (ADVANCED, 15)
- D-18: Memory Forensics (ELITE, 25)

**Total:** 4 cards

**Covers:** Credential harvesting, credential dumping, privilege escalation

---

### MALWARE Defenses
- D-04: Basic Antivirus (BASIC, 10)
- D-10: EDR (ADVANCED, 15)
- D-17: Threat Hunting (ELITE, 25)
- D-20: Behavioral Analytics (ELITE, 25)
- D-29: Code Signing Verification (ADVANCED, 15)
- D-30: Ransomware-Specific Behavior Detection (ELITE, 25)

**Total:** 6 cards

**Covers:** Malware execution, persistence, ransomware

---

### NETWORK Defenses
- D-03: Firewall Rules (BASIC, 10)
- D-11: Network Segmentation (ADVANCED, 15)
- D-12: SIEM (ADVANCED, 15)
- D-14: IDS (ADVANCED, 15)
- D-19: Deception Technology (ELITE, 25)
- D-21: Zero Trust Architecture (ELITE, 25)
- D-28: DNS Security (ADVANCED, 15)
- D-31: Polymorphic Detection Signatures (ELITE, 25)

**Total:** 8 cards

**Covers:** Lateral movement, C2 beaconing, network reconnaissance

---

### DATA_EXFIL Defenses
- D-06: DLP (Basic) (BASIC, 10)
- D-08: Backup System (BASIC, 10)
- D-22: Advanced DLP (ELITE, 25)

**Total:** 3 cards

**Covers:** Data exfiltration, database theft, data loss prevention

---

## Threat Cards by Step

### INITIAL COMPROMISE (3 cards)
- T-01: Phishing Campaign (SOCIAL_ENGINEERING)
- T-02: Watering Hole Attack (WEB_EXPLOIT)
- T-03: Credential Harvesting (CREDENTIAL_ABUSE)
- T-13: Compromised Software Vendor (WEB_EXPLOIT) - expansion
- T-14: Malicious Library Injection (WEB_EXPLOIT) - expansion
- T-15: API Credential Theft (CREDENTIAL_ABUSE) - expansion
- T-16: DNS Hijacking (NETWORK) - expansion
- T-20: Zero-Day Exploitation (WEB_EXPLOIT) - expansion

**Total:** 8 cards

---

### PIVOT & ESCALATE (5 cards)
- T-04: Lateral Movement via SMB (NETWORK)
- T-05: Privilege Escalation (Kernel) (MALWARE)
- T-06: Mimikatz Credential Dumping (CREDENTIAL_ABUSE)
- T-07: Scheduled Task Persistence (MALWARE)
- T-08: Registry Run Key Persistence (MALWARE)

**Total:** 5 cards

---

### PERSISTENCE (2 cards)
- T-09: Beaconing to C2 Server (NETWORK)
- T-10: SQL Database Exfiltration (DATA_EXFIL)
- T-17: Data Staging & Exfil (DATA_EXFIL) - expansion

**Total:** 3 cards

---

### C2 & EXFIL (2 cards)
- T-11: Ransomware Payload Deployment (MALWARE)
- T-12: File Encryption & Ransom Note (MALWARE)
- T-18: C2 Polymorphism (NETWORK) - expansion
- T-19: Ransomware as a Service (MALWARE) - expansion

**Total:** 4 cards

---

## Hardening Module Cards

### Pentester Tactic Cards (8 Cards)

| Card ID | Name | Effect | Difficulty Increase | File |
|---------|------|--------|----------------------|------|
| PT-01 | Bypass Basic Defenses | Disables 10-Budget defenses | +1 | hardening/core-deck/pentester-tactic-cards.md |
| PT-02 | Social Engineering Specialist | +1 to SOCIAL_ENGINEERING attacks | +1 | hardening/core-deck/pentester-tactic-cards.md |
| PT-03 | Persistence Expert | +1 to PERSISTENCE techniques | +1 | hardening/core-deck/pentester-tactic-cards.md |
| PT-04 | Supply Chain Attack | Bypasses vendor verification | +2 | hardening/core-deck/pentester-tactic-cards.md |
| PT-05 | Detection Evasion | +2 to avoid detection | +2 | hardening/core-deck/pentester-tactic-cards.md |
| PT-06 | Budget Drain (IR Overload) | Increases investigation costs | +1 | hardening/core-deck/pentester-tactic-cards.md |
| PT-07 | Zero-Day Exploit | Bypasses known defenses | +3 | hardening/core-deck/pentester-tactic-cards.md |
| PT-08 | Multi-Vector Attack | Affects multiple vectors | +2 | hardening/core-deck/pentester-tactic-cards.md |

**Total:** 8 cards

**Used in:** Hardening Module for defense testing

---

## Other Module Cards

### Disaster Recovery Module
**Status:** Card decks to be designed
- Crisis Action Cards (stakeholder, communication, remediation)
- Event Timeline Cards (deadlines, escalations)
- Crisis Scenario Cards

### Network Building Module
**Status:** Card decks to be designed
- Server Cards (10 types)
- Security Device Cards (10 types)
- Architecture Cards (5 options)
- Business Requirement Asset Cards

### Audit & Compliance Module
**Status:** Card decks to be designed
- Audit Domain Assessment Cards (6 domains)
- Compliance Framework Cards (NIST, CIS, PCI-DSS, HIPAA)
- Remediation Action Cards

---

## Card Properties Reference

### Threat Card Properties
- **Title:** Card name
- **Step:** Attack chain step (INITIAL_COMPROMISE, PIVOT_ESCALATE, PERSISTENCE, C2_EXFIL)
- **Vector:** Attack vector (SOCIAL_ENGINEERING, WEB_EXPLOIT, CREDENTIAL_ABUSE, MALWARE, NETWORK, DATA_EXFIL)
- **Cost:** Budget cost to reveal (usually 5)
- **Clue:** What TO reads to guide investigation
- **Why This Works:** Educational explanation

### Defense Card Properties
- **Title:** Card name
- **Tier:** BASIC, ADVANCED, or ELITE
- **Cost:** Budget to deploy (10, 15, or 25)
- **Vector:** Which threat vector it counters
- **Description:** What the defense does
- **Effect:** How it helps in gameplay

### Pentester Tactic Card Properties
- **Title:** Card name
- **Effect:** What the tactic does to difficulty
- **Difficulty Increase:** How much harder defense becomes
- **Target Vectors:** Which vectors are affected
- **Countermeasure:** Which defenses work against it

---

## Card Usage Patterns

### Minimum Recommended Deck
- 3 Threat Cards (for 3-card attack chain)
- 24 Defense Cards (full core deck)
- **Total:** 27 cards (sufficient for learning)

### Standard Deck
- 12 Threat Cards (core deck)
- 24 Defense Cards (core deck)
- **Total:** 36 cards (recommended for ongoing play)

### Complete Collection
- 20 Threat Cards (core + expansion)
- 32 Defense Cards (core + expansion)
- 8 Pentester Tactics (for Hardening)
- **Total:** 60 cards (full variety)

---

## Download Guides

### For Incident Response Only
- Download: `incident-response/core-deck/`
- Includes: 12 threat + 24 defense cards

### For Incident Response + Hardening
- Download: `incident-response/core-deck/` + `hardening/core-deck/`
- Reuses: Defense cards (buy once, use twice)
- Adds: Pentester tactic cards

### For Full Collection
- Download: All modules' core-decks + expansion-decks
- Total: 60+ cards across all modules

---

## License & Attribution

All cards are licensed under **CC BY-NC-SA 4.0** (Creative Commons Attribution-NonCommercial-ShareAlike).

---

*Incident Zero: Card Reference Index*
*v2.1 - Balanced & Refined Edition*
*Last Updated: October 2025*
