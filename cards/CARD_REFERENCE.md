# Incident Zero: Card Reference Index

**Version 2.2 - Playtest Edition**

Complete index of all cards across all six modules. This index is **generated from the card files themselves** — the card files under each module folder are the canonical source of truth. If this index ever disagrees with a card file, the card file wins.

**Total: 247 cards** across 6 modules (the 24-card shared Defense deck is counted once).

---

## Quick Navigation

- [Incident Response Module](#incident-response-module)
- [Shared Defense Deck (IR + Hardening)](#shared-defense-deck-ir--hardening)
- [Hardening Module](#hardening-module)
- [Network Building Module](#network-building-module)
- [Disaster Recovery Module](#disaster-recovery-module)
- [Forensics Module](#forensics-module)
- [Audit & Compliance Module](#audit--compliance-module)

---

## Incident Response Module

**Module total: 63 cards** (12 core threats + 24 shared defenses + 8 expansion threats + 19 expansion defenses).

| Deck | File | Card IDs | Count | Description |
|------|------|----------|-------|-------------|
| Core Threats | [threat-defense-cards.md](incident-response/core-deck/threat-defense-cards.md) | T-01 – T-12 | 12 | Attack chain steps for the Threat Orchestrator, organized by kill chain phase |
| Core Defenses (shared) | [threat-defense-cards.md](incident-response/core-deck/threat-defense-cards.md) | D-01 – D-24 | 24 | Shared with Hardening — see [Shared Defense Deck](#shared-defense-deck-ir--hardening) |
| Expansion Threats | [advanced-threats.md](incident-response/expansion-deck/advanced-threats.md) | T-13 – T-20 | 8 | Supply chain, insider, IoT, cloud, DNS tunneling, and physical attacks |
| Expansion Defenses | [advanced-defenses.md](incident-response/expansion-deck/advanced-defenses.md) | D-25 – D-43 | 19 | Whitelisting, behavioral analytics, container/cloud security, playbooks, backup/DR |

### Core Threat Deck (T-01 – T-12)

| Card ID | Title | Step | Vector |
|---------|-------|------|--------|
| T-01 | Phishing Campaign | INITIAL COMPROMISE | SOCIAL ENGINEERING |
| T-02 | Watering Hole Attack | INITIAL COMPROMISE | WEB EXPLOIT |
| T-03 | Compromised Credentials | INITIAL COMPROMISE | CREDENTIAL ABUSE |
| T-04 | Lateral Movement via SMB | PIVOT & ESCALATE | NETWORK |
| T-05 | Privilege Escalation via Kernel Exploit | PIVOT & ESCALATE | MALWARE |
| T-06 | Mimikatz Credential Dumping | PIVOT & ESCALATE | CREDENTIAL ABUSE |
| T-07 | Scheduled Task Persistence | PERSISTENCE | MALWARE |
| T-08 | Registry Run Key Persistence | PERSISTENCE | MALWARE |
| T-09 | Beaconing to C2 Server | C2 & EXFIL | NETWORK |
| T-10 | SQL Database Exfiltration | C2 & EXFIL | DATA EXFIL |
| T-11 | Ransomware Payload Deployment | C2 & EXFIL | MALWARE |
| T-12 | Browser Extension Backdoor | C2 & EXFIL | DATA EXFIL |

**By step:** INITIAL COMPROMISE 3 (T-01–03) · PIVOT & ESCALATE 3 (T-04–06) · PERSISTENCE 2 (T-07–08) · C2 & EXFIL 4 (T-09–12).

### Expansion Threat Deck (T-13 – T-20)

| Card ID | Title | Step | Vector |
|---------|-------|------|--------|
| T-13 | Compromised Software Vendor Update | INITIAL COMPROMISE | MALWARE |
| T-14 | Malicious Third-Party Library Injection | INITIAL COMPROMISE | MALWARE |
| T-15 | Malicious Insider Data Theft | C2 & EXFIL | DATA EXFIL |
| T-16 | Disgruntled Employee Sabotage | PIVOT & ESCALATE | MALWARE |
| T-17 | Compromised IoT Device as Pivot Point | INITIAL COMPROMISE | NETWORK |
| T-18 | Cloud API Token Theft & Abuse | PIVOT & ESCALATE | CREDENTIAL ABUSE |
| T-19 | DNS Tunneling Data Exfiltration | C2 & EXFIL | DATA EXFIL |
| T-20 | Physical Access + Badge Cloning Attack | INITIAL COMPROMISE | CREDENTIAL ABUSE |

### Expansion Defense Deck (D-25 – D-43)

**Distribution:** 4 BASIC (10 Budget) / 8 ADVANCED (15 Budget) / 7 ELITE (25 Budget).

| Card ID | Title | Tier (Cost) | Vector |
|---------|-------|-------------|--------|
| D-25 | Application Whitelisting | BASIC (10) | MALWARE |
| D-26 | Advanced Application Control with AI | ADVANCED (15) | MALWARE |
| D-27 | Living-Off-The-Land Blocker | ELITE (25) | MALWARE |
| D-28 | Baseline Behavior Learning System | ADVANCED (15) | NETWORK |
| D-29 | Process Behavior Analysis | ADVANCED (15) | MALWARE |
| D-30 | Machine Learning Anomaly Detection | ELITE (25) | MALWARE |
| D-31 | Container Image Scanning | BASIC (10) | MALWARE |
| D-32 | Container Runtime Protection | ADVANCED (15) | MALWARE |
| D-33 | Kubernetes Network Policy & RBAC | ELITE (25) | NETWORK |
| D-34 | Cloud Configuration Auditing | BASIC (10) | CREDENTIAL ABUSE |
| D-35 | Cloud Access & Permission Auditing | ADVANCED (15) | CREDENTIAL ABUSE |
| D-36 | Cloud Compliance & Audit Trail | ELITE (25) | DATA EXFIL |
| D-37 | Playbook: Ransomware Response | ADVANCED (15) | MALWARE |
| D-38 | Playbook: Credential Compromise Response | ADVANCED (15) | CREDENTIAL ABUSE |
| D-39 | Playbook: Insider Threat Response | ELITE (25) | DATA EXFIL |
| D-40 | Playbook: Supply Chain Breach Response | ELITE (25) | WEB EXPLOIT |
| D-41 | Backup Strategy - 3-2-1 Rule | BASIC (10) | MALWARE |
| D-42 | Immutable Backup Storage | ADVANCED (15) | MALWARE |
| D-43 | Disaster Recovery Plan & Testing | ELITE (25) | MALWARE |

---

## Shared Defense Deck (IR + Hardening)

**24 cards (D-01 – D-24), indexed once.** The same deck appears in full in **both** module folders:

- [incident-response/core-deck/threat-defense-cards.md](incident-response/core-deck/threat-defense-cards.md) (printable card layouts)
- [hardening/core-deck/defense-cards.md](hardening/core-deck/defense-cards.md) (compact reference with Hardening usage notes)

Print one physical set and use it in both modules.

**Distribution by tier (v2.2):** 8 BASIC (D-01–06, D-19, D-23) / 8 ADVANCED (D-07–12, D-18, D-24) / 8 ELITE (D-13–17, D-20–22).

| Card ID | Title | Tier (Cost) | Vector |
|---------|-------|-------------|--------|
| D-01 | Email Authentication Setup | BASIC (10) | SOCIAL ENGINEERING |
| D-02 | User Security Training | BASIC (10) | SOCIAL ENGINEERING |
| D-03 | Windows Update Patching | BASIC (10) | WEB EXPLOIT |
| D-04 | Network Firewall Rules | BASIC (10) | NETWORK |
| D-05 | Log Centralization | BASIC (10) | MALWARE |
| D-06 | Basic Antivirus Deployment | BASIC (10) | MALWARE |
| D-07 | Multi-Factor Authentication (MFA) | ADVANCED (15) | CREDENTIAL ABUSE |
| D-08 | EDR (Endpoint Detection & Response) | ADVANCED (15) | MALWARE |
| D-09 | Network Segmentation | ADVANCED (15) | NETWORK |
| D-10 | SIEM Correlation Rules | ADVANCED (15) | NETWORK |
| D-11 | Data Loss Prevention (DLP) | ADVANCED (15) | DATA EXFIL |
| D-12 | Password Manager & Vault | ADVANCED (15) | CREDENTIAL ABUSE |
| D-13 | Threat Hunting Program | ELITE (25) | MALWARE |
| D-14 | Memory Forensics | ELITE (25) | MALWARE |
| D-15 | Deception Technology (Honeypots) | ELITE (25) | NETWORK |
| D-16 | Credential Guard & Secure Boot | ELITE (25) | CREDENTIAL ABUSE |
| D-17 | Advanced Malware Sandbox | ELITE (25) | MALWARE |
| D-18 | Intrusion Prevention System (IPS) | ADVANCED (15) | WEB EXPLOIT |
| D-19 | Backup & Disaster Recovery | BASIC (10) | MALWARE |
| D-20 | Zero Trust Access Control | ELITE (25) | CREDENTIAL ABUSE |
| D-21 | Container Security & Orchestration | ELITE (25) | MALWARE |
| D-22 | Security Information & Event Management (SIEM) | ELITE (25) | NETWORK |
| D-23 | IR Program & Runbooks | BASIC (10) | NETWORK |
| D-24 | Threat Intelligence Integration | ADVANCED (15) | NETWORK + DATA EXFIL (dual-tagged) |

**Distribution by vector (v2.2):** SOCIAL ENGINEERING 2 · WEB EXPLOIT 2 · CREDENTIAL ABUSE 4 · MALWARE 8 · NETWORK 7 · DATA EXFIL 2. D-24 is dual-tagged (NETWORK + DATA EXFIL), so vector tags sum to 25 across 24 cards.

---

## Hardening Module

**Module total: 16 tactic cards** + the [Shared Defense Deck](#shared-defense-deck-ir--hardening) (24 cards, indexed above).

| Deck | File | Card IDs | Count | Description |
|------|------|----------|-------|-------------|
| Defense Cards (shared) | [defense-cards.md](hardening/core-deck/defense-cards.md) | D-01 – D-24 | 24 | Same deck as IR core — see [Shared Defense Deck](#shared-defense-deck-ir--hardening) |
| Core Pentester Tactics | [pentester-tactic-cards.md](hardening/core-deck/pentester-tactic-cards.md) | PT-01 – PT-08 | 8 | Red-team tactics that test deployed defenses (d20 vs DC) |
| Expansion Tactics | [advanced-tactics.md](hardening/expansion-deck/advanced-tactics.md) | PT-09 – PT-16 | 8 | Multi-vector, zero-day, ransomware, APT, cloud/IoT/firmware/container attacks |

### Core Pentester Tactic Deck (PT-01 – PT-08)

| Card ID | Title | Difficulty (DC) | Target Vectors |
|---------|-------|-----------------|----------------|
| PT-01 | Social Engineering - Pretexting Attack | BASIC (DC 12) | SOCIAL_ENGINEERING, CREDENTIAL_ABUSE |
| PT-02 | Malware Evasion - Living-off-the-Land Technique | INTERMEDIATE (DC 13) | MALWARE, CREDENTIAL_ABUSE |
| PT-03 | Credential Dumping - Mimikatz Attack | INTERMEDIATE (DC 13) | CREDENTIAL_ABUSE, MALWARE |
| PT-04 | Lateral Movement - Network Traversal | INTERMEDIATE (DC 13) | NETWORK, CREDENTIAL_ABUSE |
| PT-05 | Privilege Escalation - Unpatched Kernel Exploit | ADVANCED (DC 14) | MALWARE, WEB_EXPLOIT |
| PT-06 | Data Exfiltration - Unmonitored Channel | ADVANCED (DC 14) | DATA_EXFIL, NETWORK |
| PT-07 | Supply Chain Compromise - Trusted Software Update | ADVANCED (DC 14) | MALWARE, WEB_EXPLOIT |
| PT-08 | Insider Threat - Malicious Administrator | EXPERT (DC 15) | CREDENTIAL_ABUSE, DATA_EXFIL, NETWORK |

### Expansion Tactic Deck (PT-09 – PT-16)

| Card ID | Title | Difficulty (DC) | Target Vectors |
|---------|-------|-----------------|----------------|
| PT-09 | Multi-Vector Attack - Coordinated Campaign | ADVANCED (DC 14) | Multiple (per-phase rolls) |
| PT-10 | Zero-Day Exploitation - Unknown Vulnerability | EXPERT (DC 15) | MALWARE, WEB_EXPLOIT |
| PT-11 | Ransomware Deployment & Encryption | EXPERT (DC 15) | MALWARE, DATA_EXFIL, NETWORK |
| PT-12 | APT Campaign - Multi-Turn Persistent Threat | EXPERT+ (DC 16, escalates +1/turn undetected) | Multiple |
| PT-13 | Cloud-Specific Attack - Misconfigured Cloud Resources | ADVANCED (DC 14) | Multiple |
| PT-14 | IoT/OT Compromise - Industrial Network Attack | ADVANCED (DC 14) | NETWORK, MALWARE |
| PT-15 | Firmware/BIOS Attack - Bootloader Compromise | EXPERT (DC 15) | MALWARE, NETWORK |
| PT-16 | Privilege Escalation - Containerized Environment Escape | EXPERT (DC 15) | MALWARE, NETWORK |

---

## Network Building Module

**Module total: 77 cards** (33 core + 8 expansion + 36 standalone).

| Deck | File | Card IDs | Count | Description |
|------|------|----------|-------|-------------|
| Servers | [server-cards.md](network-building/core-deck/server-cards.md) | SRV-01 – SRV-10 | 10 | Server types with cost, capacity, complexity, and availability |
| Security Devices | [security-device-cards.md](network-building/core-deck/security-device-cards.md) | SEC-01 – SEC-10 | 10 | Security appliances with cost, vectors covered, and placement |
| Architectures | [architecture-cards.md](network-building/core-deck/architecture-cards.md) | ARCH-01 – ARCH-05 | 5 | Network topology choices with cost/complexity trade-offs |
| Assets | [asset-cards.md](network-building/core-deck/asset-cards.md) | ASSET-01 – ASSET-08 | 8 | Business functions the network must support |
| Legacy Systems (exp.) | [legacy-systems.md](network-building/expansion-deck/legacy-systems.md) | LEGACY-01 – LEGACY-04 | 4 | Unpatched, mission-critical legacy burdens |
| Cloud Variants (exp.) | [cloud-variants.md](network-building/expansion-deck/cloud-variants.md) | CLOUD-01 – CLOUD-04 | 4 | Modern cloud deployment alternatives |
| Business Requirements (standalone) | [business-requirement-cards.md](network-building/standalone/business-requirement-cards.md) | REQ-01 – REQ-20 | 20 | Draw-deck requirements for standalone play |
| Operational Events (standalone) | [operational-event-cards.md](network-building/standalone/operational-event-cards.md) | EVT-01 – EVT-16 | 16 | Draw-deck operational events for standalone play |

### Server Cards (SRV-01 – SRV-10)

| Card ID | Title | Cost | Key Risk |
|---------|-------|------|----------|
| SRV-01 | Email Server | 8 | Phishing, Credential Abuse |
| SRV-02 | Web Server | 7 | Web Exploits, RCE |
| SRV-03 | Database Server | 10 | SQL Injection, Data Exfil |
| SRV-04 | File Server | 6 | SMB Laterals, Ransomware |
| SRV-05 | Domain Controller | 12 | Mimikatz, Complete Compromise |
| SRV-06 | Development Server | 5 | Lateral Movement, Data Leak |
| SRV-07 | Backup Server | 9 | Ransomware, Recovery Failure |
| SRV-08 | Cloud Workload | 4 | Misconfiguration, IAM Abuse |
| SRV-09 | Legacy System | 3 | Known Vulns, Cannot Patch |
| SRV-10 | Honeypot Decoy | 7 | Detection, Early Warning |

### Security Device Cards (SEC-01 – SEC-10)

| Card ID | Title | Cost | Primary Vectors / Placement |
|---------|-------|------|-----------------------------|
| SEC-01 | Firewall (Perimeter) | 12 | NETWORK, CREDENTIAL / Perimeter |
| SEC-02 | Intrusion Detection System (IDS) | 10 | MALWARE, NETWORK / Internal |
| SEC-03 | Intrusion Prevention System (IPS) | 14 | MALWARE, WEB, NETWORK / Internal |
| SEC-04 | Load Balancer | 8 | NETWORK (availability) / Web Tier |
| SEC-05 | VPN Gateway | 9 | CREDENTIAL, NETWORK / Perimeter |
| SEC-06 | Email Gateway | 6 | SOCIAL_ENG, MALWARE / Perimeter |
| SEC-07 | Web Application Firewall (WAF) | 11 | WEB, MALWARE / Web Tier |
| SEC-08 | Network Segmentation Switch | 10 | CREDENTIAL, NETWORK / Internal |
| SEC-09 | SIEM (Security Information & Event Management) | 15 | Multiple (detection) / Central |
| SEC-10 | Honeypot Network | 8 | NETWORK (detection) / Isolated |

### Architecture Cards (ARCH-01 – ARCH-05)

| Card ID | Title | Cost | Complexity |
|---------|-------|------|------------|
| ARCH-01 | Flat Network (Traditional) | 0 | 1/5 |
| ARCH-02 | Segmented 3-Zone (DMZ Model) | 5 | 2/5 |
| ARCH-03 | Fully Isolated (Zero Trust Model) | 12 | 4/5 |
| ARCH-04 | Cloud Hybrid (Mixed On-Premises & Cloud) | 8 | 3/5 |
| ARCH-05 | Cloud First (Cloud-Only Infrastructure) | 6 | 2/5 |

### Asset Cards (ASSET-01 – ASSET-08)

| Card ID | Title | Criticality | Fulfilled By |
|---------|-------|-------------|--------------|
| ASSET-01 | Email | High | SRV-01 |
| ASSET-02 | Web | Medium | SRV-02 |
| ASSET-03 | Database | Very High | SRV-03 |
| ASSET-04 | File Storage | High | SRV-04 |
| ASSET-05 | Identity | Very High | SRV-05 |
| ASSET-06 | Development | Medium | SRV-06 |
| ASSET-07 | Disaster Recovery | Very High | SRV-07 |
| ASSET-08 | VPN/Remote Access | Medium | SEC-05 |

### Legacy System Cards (LEGACY-01 – LEGACY-04, Expansion)

| Card ID | Title | Cost | Key Challenge |
|---------|-------|------|---------------|
| LEGACY-01 | Mainframe System | 15 | Cannot patch, mission-critical |
| LEGACY-02 | Custom Business Application | 8 | Vendor no longer exists |
| LEGACY-03 | Industrial Control System (ICS) | 12 | Real-time + safety-critical |
| LEGACY-04 | Obsolete Operating System | 5 | All vulnerabilities public |

### Cloud Variant Cards (CLOUD-01 – CLOUD-04, Expansion)

| Card ID | Title | Cost | Primary Benefit |
|---------|-------|------|-----------------|
| CLOUD-01 | Containerized Microservices | 6 | Scalability & Velocity |
| CLOUD-02 | Serverless/Function-as-a-Service | 3 | Simplicity & Cost |
| CLOUD-03 | Database-as-a-Service (Managed Database) | 5 | Reliability & Compliance |
| CLOUD-04 | Content Delivery Network (CDN) | 4 | Performance & DDoS Protection |

### Business Requirement Cards (REQ-01 – REQ-20, Standalone)

| Card ID | Title | Satisfied By | Missed Penalty |
|---------|-------|--------------|----------------|
| REQ-01 | New Product Launch Website | Web Server or cloud web | -5 |
| REQ-02 | Customer Data Acquisition | Database (dedicated or cloud) | -10 |
| REQ-03 | Work-From-Home Program | VPN Gateway | -3 |
| REQ-04 | Remote Workforce Mandate | VPN Gateway + Domain Controller | -5 |
| REQ-05 | HIPAA Compliance Mandate | Backup + segmentation | -10 |
| REQ-06 | PCI Scope: Cardholder Data | Database + Firewall/Segmentation | -10 |
| REQ-07 | 99.9% Uptime SLA | Load Balancer or duplicate server | -5 |
| REQ-08 | M&A: Integrate Acquired Network | 2 spare slots or new server | -10 |
| REQ-09 | Scale Email System | 2nd Email Server / LB / cloud email | -5 |
| REQ-10 | Security Audit Ordered | SIEM, or IDS + Email Gateway | -5 |
| REQ-11 | Board Demands IR Readiness | IDS, IPS, or SIEM | -10 |
| REQ-12 | Ransomware Wave in Sector | Backup + detection | -20 |
| REQ-13 | New Subsidiary Office | VPN Gateway | -5 |
| REQ-14 | E-Commerce Expansion | Web + WAF | -5 |
| REQ-15 | Developer Hiring Spree | Dev Server or overload | -3 |
| REQ-16 | Records-Retention Regulation | File storage + Backup | -5 |
| REQ-17 | Single Sign-On Rollout | Domain Controller | -5 |
| REQ-18 | Cyber-Insurance Renewal | Backup + Email Gateway + detection | -5 (met: +5) |
| REQ-19 | Threat-Intel Pilot | Honeypot | 0 (met: +5) |
| REQ-20 | Data-Center Consolidation | Any cloud-hosted service | -3 (met: +3) |

### Operational Event Cards (EVT-01 – EVT-16, Standalone)

| Card ID | Title | Effect (Unmitigated) | Mitigated By |
|---------|-------|----------------------|--------------|
| EVT-01 | Email Server Failure | Pay 5 or -10 pts | Redundant/cloud email |
| EVT-02 | Traffic Spike | -5 pts (or +5 if ready) | LB / CDN / redundant web |
| EVT-03 | Phishing Wave | -10 pts (or +5 if ready) | Email Gateway |
| EVT-04 | Cloud Vendor Outage | -5 pts if cloud-only service | On-prem redundancy |
| EVT-05 | Budget Cut | -5 Budget | Contingency reserve |
| EVT-06 | Emergency Funds | +10 Budget | — |
| EVT-07 | Security Grant | +5 Budget if Backup | — |
| EVT-08 | File Server Filling Up | Buy capacity or -5 pts | Spare capacity |
| EVT-09 | Honeypot Triggers | +5 pts if honeypot | — |
| EVT-10 | Insider Snooping | -5 pts (or +5 if ready) | SIEM / segmentation |
| EVT-11 | Ransomware Strikes | -20 pts | Backup (+ detection: +5) |
| EVT-12 | IT Staff Burnout | Max 1 deploy this turn | Completed builds |
| EVT-13 | Vendor Promotion | Next device -2 cost | — |
| EVT-14 | New Hire Needs Remote Access | -3 pts | VPN Gateway |
| EVT-15 | Hardware Recall | Pay 3 or server offline | Redundancy / cloud |
| EVT-16 | Quiet Quarter | Nothing | — |

---

## Disaster Recovery Module

**Module total: 38 cards** (30 core + 8 expansion scenarios).

| Deck | File | Card IDs | Count | Description |
|------|------|----------|-------|-------------|
| Crisis Actions | [crisis-action-cards.md](disaster-recovery/core-deck/crisis-action-cards.md) | ACTION-01 – ACTION-13 | 13 | Investigation, Remediation, Communication actions plus the Ransom Decision |
| Event Timeline | [event-cards.md](disaster-recovery/core-deck/event-cards.md) | EVENT-01 – EVENT-12 | 12 | 6 Scheduled + 6 Triggered crisis events on the 8-turn Crisis Clock |
| Stakeholders | [stakeholder-cards.md](disaster-recovery/core-deck/stakeholder-cards.md) | STAKE-01 – STAKE-05 | 5 | Trust meters for the five stakeholder groups |
| Advanced Scenarios (exp.) | [advanced-scenarios.md](disaster-recovery/expansion-deck/advanced-scenarios.md) | SCENARIO-01 – SCENARIO-08 | 8 | High/extreme-difficulty crisis setups |

### Crisis Action Cards (ACTION-01 – ACTION-13)

| Card ID | Title | Category | Cost | Advance | Duration |
|---------|-------|----------|------|---------|----------|
| ACTION-01 | Forensic Analysis | Investigation | 12 | +25% | 2 turns |
| ACTION-02 | Threat Hunting | Investigation | 8 | +15% | 1 turn |
| ACTION-03 | Log Analysis | Investigation | 5 | +10% | 1 turn |
| ACTION-04 | Third-Party Incident Response Engagement | Investigation | 20 | +30% Inv / +20% Rem | 3 turns |
| ACTION-05 | Patch & Harden (Affected Systems) | Remediation | 10 | +20% | 1 turn |
| ACTION-06 | Containment (Isolate Compromised Systems) | Remediation | 8 | +15% | 1 turn |
| ACTION-07 | System Rebuild/Recovery from Backup | Remediation | 15 | +25% | 2 turns |
| ACTION-08 | Change Credentials & Access Controls | Remediation | 6 | +12% | 1 turn |
| ACTION-09 | Customer Notification | Communication | 10 | +20% | 1 turn |
| ACTION-10 | Regulatory/Law Enforcement Notification | Communication | 8 | +10% | 1 turn |
| ACTION-11 | Media/Public Relations Management | Communication | 12 | +15% | 1 turn |
| ACTION-12 | Board & Shareholder Communication | Communication | 9 | +12% | 1 turn |
| ACTION-13 | Ransom Decision (v2.2) | Crisis Decision | 0/5/20 | Pay: +20% Rem | Instant (once per game) |

*Standing rule (not a card): the free Holding Statement — Communication, 0 Budget, +5%.*

### Event Timeline Cards (EVENT-01 – EVENT-12)

| Card ID | Title | Kind | Turn / Trigger |
|---------|-------|------|----------------|
| EVENT-01 | First Media Coverage | Scheduled | Turn 2 |
| EVENT-02 | Regulatory 72-Hour Deadline | Scheduled | Turn 6 (deadline Turn 8) |
| EVENT-03 | Customer Notification Window | Scheduled | Turn 5 |
| EVENT-04 | Board Meeting | Scheduled | Turn 3 |
| EVENT-05 | Customer Class Action Lawsuit | Triggered | Customers un-notified after T5 or trust <20% |
| EVENT-06 | Regulatory Fine | Triggered | Regulator trust <20% |
| EVENT-07 | Media Frenzy | Triggered | Media <20% or silent through T3 |
| EVENT-08 | Second Breach Discovered | Triggered | T6: Remediation <30%, no rebuild |
| EVENT-09 | Shareholder Pressure | Scheduled | Turn 5 (public co.) |
| EVENT-10 | Competitor Advantage | Triggered | Customer trust <40% from T5 |
| EVENT-11 | Key Executive Resignation | Triggered | Executive trust <30% |
| EVENT-12 | Government Subpoena | Scheduled | Turn 7 (med/large org) |

### Stakeholder Cards (STAKE-01 – STAKE-05)

| Card ID | Title | Type | Starting Trust |
|---------|-------|------|----------------|
| STAKE-01 | Customers | External | 50% |
| STAKE-02 | Regulators | Government | 60% |
| STAKE-03 | Media / Public | External | 40% |
| STAKE-04 | Board of Directors | Internal | 70% |
| STAKE-05 | Executive Leadership | Internal | 80% |

### Advanced Scenario Cards (SCENARIO-01 – SCENARIO-08, Expansion)

| Card ID | Title | Difficulty | Key Pressure |
|---------|-------|------------|--------------|
| SCENARIO-01 | Multi-Region Breach with Data Sovereignty Issues | HIGH | 3 different regulatory timelines |
| SCENARIO-02 | Ransomware with Extortion Threat | HIGH | $10M decision + data publication threat |
| SCENARIO-03 | Supply Chain Compromise (Vendor Breach Affects Customers) | HIGH | Vendor failure, customer trust |
| SCENARIO-04 | Insider Threat Revealed Mid-Crisis | HIGH | Organizational trust collapse |
| SCENARIO-05 | Critical Infrastructure Breach (Safety/Lives at Risk) | EXTREME | Lives at risk, government control |
| SCENARIO-06 | Stock Price Crash (Public Company Panic) | HIGH | Financial crisis + board pressure |
| SCENARIO-07 | Ransomware + Data Breach + Business Email Compromise | EXTREME | 3 simultaneous attacks, multiple ransoms |
| SCENARIO-08 | Breach During Merger/Acquisition | EXTREME | Deal value + regulatory blocks |

---

## Forensics Module

**Module total: 28 core cards** (12 Investigation + 12 Evidence + 4 Findings). **Expansion deck: PLANNED — not yet available** (no card file exists yet; see the module README's design notes).

| Deck | File | Card IDs | Count | Description |
|------|------|----------|-------|-------------|
| Investigation Actions | [investigation-cards.md](forensics/core-deck/investigation-cards.md) | DISK-01/02, MEM-01/02, LOG-01/02, NET-01/02, MALW-01/02, TIMELINE-01, THREAT-01 | 12 | Forensic techniques rolled d20 vs DC, with Budget cost and Duration |
| Evidence & Findings | [evidence-cards.md](forensics/core-deck/evidence-cards.md) | EVD-01 – EVD-12, FIND-01 – FIND-04 | 16 | Discovered evidence artifacts and synthesis/conclusion cards |

### Investigation Action Cards (12)

| Card ID | Title | DC | Cost | Duration |
|---------|-------|----|------|----------|
| DISK-01 | Disk Image & Analysis | 12 | 10 | 2 turns (rush: +5 Budget for 1) |
| DISK-02 | File System Carving | 14 | 15 | 3 turns |
| MEM-01 | Memory Dump & Analysis | 13 | 15 | 2 turns |
| MEM-02 | Memory Forensics Deep Dive | 15 | 20 | 3 turns |
| LOG-01 | Event Log Analysis | 11 | 5 | 1 turn |
| LOG-02 | Deep Log Correlation | 13 | 10 | 2 turns |
| NET-01 | Network Traffic Analysis | 12 | 10 | 2 turns |
| NET-02 | Packet Capture Deep Analysis | 14 | 15 | 3 turns |
| MALW-01 | Malware Analysis (Dynamic) | 12 | 15 | 2 turns |
| MALW-02 | Malware Analysis (Static) | 14 | 10 | 2 turns |
| TIMELINE-01 | Timeline Reconstruction | 13 | 5 | 1 turn |
| THREAT-01 | Threat Attribution Analysis | 15 | 20 | 3 turns |

### Evidence Cards (EVD-01 – EVD-12)

| Card ID | Title | Type |
|---------|-------|------|
| EVD-01 | Credential Dumper Malware | Malware & Persistence |
| EVD-02 | Command-and-Control Callback Domain | Attack Infrastructure |
| EVD-03 | Persistence Mechanism (Scheduled Task) | Malware & Persistence |
| EVD-04 | Suspicious Admin Login (Timeline) | Credentials & Access |
| EVD-05 | Lateral Movement Evidence (Pass-the-Hash) | Lateral Movement |
| EVD-06 | Data Exfiltration Evidence | Exfiltration |
| EVD-07 | Attacker Infrastructure Map | Attack Infrastructure |
| EVD-08 | Encryption Keys Recovered | Malware & Persistence |
| EVD-09 | Attacker Command History | Attack Activity |
| EVD-10 | Malware Behavior Profile | Malware & Persistence |
| EVD-11 | File Staging Artifacts | Attack Activity |
| EVD-12 | Anti-Forensics Evidence | Attack Activity |

### Findings Cards (FIND-01 – FIND-04)

| Card ID | Title | Triggered When |
|---------|-------|----------------|
| FIND-01 | Threat Attribution Report | Attribution Confidence ≥ 70% |
| FIND-02 | Attack Surface Analysis | Attack Chain ≥ 75% |
| FIND-03 | Persistence Mechanisms Discovered | Multiple persistence artifacts found |
| FIND-04 | Investigative Gaps & Recommendations | Investigation completes (Victory or Failure) |

---

## Audit & Compliance Module

**Module total: 25 cards** (6 core + 19 expansion). The expansion — 11 framework cards and 8 remediation cards — lives entirely in one file.

| Deck | File | Card IDs | Count | Description |
|------|------|----------|-------|-------------|
| Audit Domains | [audit-domain-cards.md](audit-compliance/core-deck/audit-domain-cards.md) | DOMAIN-01 – DOMAIN-06 | 6 | Domain assessments scored 1-5 stars with PASS/FAIL mapping |
| Frameworks & Remediation (exp.) | [compliance-frameworks.md](audit-compliance/expansion-deck/compliance-frameworks.md) | FRAMEWORK-NIST-01–05, FRAMEWORK-CIS-01–03, FRAMEWORK-PCI-01–03, REMEDIATION-01–08 | 19 | Framework assessment variants (5 NIST + 3 CIS + 3 PCI) plus 8 remediation actions |

### Audit Domain Cards (DOMAIN-01 – DOMAIN-06)

| Card ID | Title | Focus |
|---------|-------|-------|
| DOMAIN-01 | Network Segmentation & Isolation | Network zones, lateral movement prevention |
| DOMAIN-02 | Access Control & Identity Management | MFA, credential policy |
| DOMAIN-03 | Threat Detection & Incident Response | SIEM, breach detection |
| DOMAIN-04 | Backup & Disaster Recovery | Backups, ransomware resilience |
| DOMAIN-05 | Third-Party Risk & Cloud Security | Vendor and supply chain risk |
| DOMAIN-06 | Security Operations & Monitoring | Security team, sustained posture |

### Compliance Framework Cards (11, Expansion)

| Card ID | Title | Focus |
|---------|-------|-------|
| FRAMEWORK-NIST-01 | Identify Function | Asset inventory and risk assessment |
| FRAMEWORK-NIST-02 | Protect Function | Preventive security controls |
| FRAMEWORK-NIST-03 | Detect Function | Detecting attacks as they happen |
| FRAMEWORK-NIST-04 | Respond Function | Responding to breaches/attacks |
| FRAMEWORK-NIST-05 | Recover Function | Recovery and improvement |
| FRAMEWORK-CIS-01 | Safeguards 1-6 (Foundations) | Basic security practices |
| FRAMEWORK-CIS-02 | Safeguards 7-13 (Advanced Defenses) | IR, supply chain, defense tools |
| FRAMEWORK-CIS-03 | Safeguards 14-18 (Operations & Governance) | Operational controls |
| FRAMEWORK-PCI-01 | Infrastructure Security (Requirements 1-4) | Network/system security for cardholder data |
| FRAMEWORK-PCI-02 | Access & Operations (Requirements 5-10) | Access control and operations |
| FRAMEWORK-PCI-03 | Testing & Compliance (Requirements 11-12) | Testing, monitoring, compliance management |

### Remediation Action Cards (REMEDIATION-01 – REMEDIATION-08, Expansion)

| Card ID | Title | Cost |
|---------|-------|------|
| REMEDIATION-01 | Implement MFA | 5 |
| REMEDIATION-02 | Deploy SIEM | 15 |
| REMEDIATION-03 | Implement Network Segmentation | 12 |
| REMEDIATION-04 | Backup & Disaster Recovery | 10 |
| REMEDIATION-05 | Security Training Program | 3 |
| REMEDIATION-06 | Vendor Security Assessment | 5 |
| REMEDIATION-07 | Vulnerability Management Program | 8 |
| REMEDIATION-08 | Incident Response Plan & Team | 12 |

---

## Card Count Summary

| Module | Core | Expansion | Standalone | Total |
|--------|------|-----------|------------|-------|
| Incident Response | 12 threats + 24 defenses* | 8 threats + 19 defenses | — | 63 |
| Hardening | 8 tactics (+ shared 24 defenses*) | 8 tactics | — | 16 (+24 shared) |
| Network Building | 33 | 8 | 36 | 77 |
| Disaster Recovery | 30 | 8 | — | 38 |
| Forensics | 28 | planned | — | 28 |
| Audit & Compliance | 6 | 19 | — | 25 |

\* The 24 defense cards (D-01 – D-24) are one shared deck counted once (under Incident Response) in the 247-card grand total.

---

## License & Attribution

All cards are licensed under **CC BY-NC-SA 4.0** (Creative Commons Attribution-NonCommercial-ShareAlike).

---

*Incident Zero: Card Reference Index*
*Version 2.2 - Playtest Edition*
*Generated from the card files — the card files are canonical.*
