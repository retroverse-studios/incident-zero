# Audit & Compliance Module: Compliance Frameworks & Remediation (Expansion)

**Version:** 2.1 - Balanced & Refined Edition
**Last Updated:** October 2025

---

## Overview

**Compliance Framework Cards** extend the Audit & Compliance module with industry-specific and regulation-specific assessment frameworks beyond the generic 6-domain audit.

- **Total Cards:** 16 (8 framework variants + 8 remediation action cards)
- **Used In:** Audit & Compliance expansion (specialized assessments)
- **Prerequisite:** Complete generic audit with 6 domains
- **Purpose:** Deep-dive assessment using specific compliance frameworks

---

## Compliance Framework Variants

Organizations must often comply with specific regulatory frameworks. Each framework has slightly different focuses and requirements.

---

## NIST Cybersecurity Framework (5 cards)
**Relevance:** US Federal government, critical infrastructure, government contractors
**Key Standard:** NIST CSF (Cybersecurity Framework) 5 functions

### FRAMEWORK-NIST-01: Identify Function
**Framework:** NIST CSF
**Function:** Identify (AM - Asset Management, RM - Risk Management)
**Focus:** Knowing what systems/data you have and what risks they face

**Assessment Criteria:**
- Asset inventory (what systems exist?)
- Data classification (what data is sensitive?)
- Risk assessment (what could go wrong?)
- Threat intelligence (what are realistic threats?)

**Scoring (1-5 stars):**
- ⭐ (1): No asset inventory, no risk assessment
- ⭐⭐ (2): Partial inventory, informal risk assessment
- ⭐⭐⭐ (3): Complete inventory, documented risk assessment
- ⭐⭐⭐⭐ (4): Inventory regularly updated, risk assessment reviewed annually
- ⭐⭐⭐⭐⭐ (5): Real-time asset visibility, continuous risk assessment

**Typical Findings:**
- Unknown systems (shadow IT)
- Unclassified data (don't know what's sensitive)
- Missing risk assessment
- Risk assessment not updated

**Remediation:**
- Discovery tools (find all systems)
- Data classification policy
- Annual risk assessment
- Asset management system

---

### FRAMEWORK-NIST-02: Protect Function
**Framework:** NIST CSF
**Function:** Protect (AC - Access Control, AT - Awareness, DE - Data Security, IR - Info Protection, SC - Security Continuity)
**Focus:** Building security controls to prevent/slow attacks

**Assessment Criteria:**
- Access controls (only authorized users)
- Employee training (security awareness)
- Data protection (encryption, classification)
- Information protection (DLP, data loss prevention)
- Business continuity (backup, disaster recovery)

**Scoring (1-5 stars):**
- ⭐ (1): No controls
- ⭐⭐ (2): Basic controls (passwords)
- ⭐⭐⭐ (3): Good controls (MFA, encryption)
- ⭐⭐⭐⭐ (4): Strong controls (defense-in-depth)
- ⭐⭐⭐⭐⭐ (5): Excellent controls (comprehensive, tested)

**Typical Findings:**
- Weak authentication (no MFA)
- Poor training (phishing success rate >10%)
- Unencrypted data
- No backup strategy
- Defense gaps

**Remediation:**
- MFA deployment
- Security training program
- Encryption implementation
- Backup/DR strategy
- Penetration testing

---

### FRAMEWORK-NIST-03: Detect Function
**Framework:** NIST CSF
**Function:** Detect (AE - Anomalies & Events, CM - Continuous Monitoring)
**Focus:** Detecting attacks as they happen

**Assessment Criteria:**
- Log monitoring (are suspicious activities logged?)
- Anomaly detection (is suspicious behavior caught?)
- Continuous monitoring (24/7 surveillance)
- Alert procedures (who responds to alerts?)
- Threat intelligence integration (using threat data)

**Scoring (1-5 stars):**
- ⭐ (1): No logging, no monitoring
- ⭐⭐ (2): Logging exists, limited monitoring
- ⭐⭐⭐ (3): SIEM deployed, some alerts
- ⭐⭐⭐⭐ (4): SIEM with good rules, 24/7 monitoring
- ⭐⭐⭐⭐⭐ (5): Mature SOC, threat intelligence integrated

**Typical Findings:**
- No SIEM deployed
- Alerts not reviewed
- No 24/7 monitoring
- Response time too slow
- Threat intel not integrated

**Remediation:**
- SIEM deployment
- Alert rule tuning
- SOC staffing (24/7 coverage)
- Response procedures
- Threat intel integration

---

### FRAMEWORK-NIST-04: Respond Function
**Framework:** NIST CSF
**Function:** Respond (RP - Response Planning, CM - Communications Management)
**Focus:** Responding to breaches/attacks

**Assessment Criteria:**
- Incident response plan (documented procedures)
- Response team (trained, staffed)
- Communication plan (who gets told when)
- Investigation procedures (forensics)
- Post-incident review (lessons learned)

**Scoring (1-5 stars):**
- ⭐ (1): No incident response plan
- ⭐⭐ (2): Plan exists, not tested
- ⭐⭐⭐ (3): Plan exists, annual testing
- ⭐⭐⭐⭐ (4): Plan regularly tested, team trained
- ⭐⭐⭐⭐⭐ (5): Mature response, regular exercises, continuous improvement

**Typical Findings:**
- No incident response plan
- Response team not trained
- No communication plan
- Investigation procedures unclear
- No post-incident reviews

**Remediation:**
- Incident response plan development
- Team training
- Communication procedures
- Tabletop exercises
- Post-incident review process

---

### FRAMEWORK-NIST-05: Recover Function
**Framework:** NIST CSF
**Function:** Recover (RC - Recovery Planning, IM - Improvements)
**Focus:** Recovering from breaches and improving for next time

**Assessment Criteria:**
- Recovery plan (how to restore systems)
- Recovery time objectives (RTO - how fast?)
- Recovery point objectives (RPO - how much data loss?)
- Backup verification (can you actually restore?)
- Lessons learned process (improve after incident)

**Scoring (1-5 stars):**
- ⭐ (1): No recovery plan, no backups
- ⭐⭐ (2): Backup exists, recovery not tested
- ⭐⭐⭐ (3): Recovery plan exists, tested annually
- ⭐⭐⭐⭐ (4): Recovery plan regularly tested, RPO/RTO defined
- ⭐⭐⭐⭐⭐ (5): Mature recovery, tested regularly, continuous improvement

**Typical Findings:**
- No recovery plan
- Backups untested (may not restore)
- RTO/RPO not defined
- Recovery team not trained
- No lessons learned process

**Remediation:**
- Recovery plan development
- Backup testing (quarterly)
- RTO/RPO definition
- Recovery team training
- Lessons learned process

---

## CIS Controls (4 cards)
**Relevance:** General US/Canada, healthcare, financial, government
**Key Standard:** CIS Controls (18 prioritized security controls)

### FRAMEWORK-CIS-01: Safeguards 1-6 (Foundations)
**Focus:** Basic security practices (asset management, access control, data protection, secure configuration)

**Assessment Criteria:**
- Asset management (know what you have)
- Access control (least privilege)
- Data protection (encryption)
- Secure configuration (harden systems)
- Detection tools (SIEM, antivirus)
- Training (security awareness)

---

### FRAMEWORK-CIS-02: Safeguards 7-13 (Advanced Defenses)
**Focus:** Advanced controls (incident response, supply chain, defense tools)

**Assessment Criteria:**
- Incident response plan
- Supply chain risk
- Vulnerability management
- Application security
- Remote services security
- Testing & monitoring
- Network segmentation

---

### FRAMEWORK-CIS-03: Safeguards 14-18 (Operations & Governance)
**Focus:** Operational controls (reporting, awareness, training, testing)

**Assessment Criteria:**
- Security awareness training
- Incident reporting
- Third-party risk management
- Penetration testing
- Secure development practices

---

## PCI-DSS (3 cards)
**Relevance:** Any organization handling payment cards
**Key Standard:** PCI-DSS (Payment Card Industry Data Security Standard)

### FRAMEWORK-PCI-01: Infrastructure Security (Requirements 1-4)
**Focus:** Network and system security for cardholder data

**Assessment Criteria:**
- Firewall configuration
- No default credentials
- Cardholder data protection
- Vulnerability scanning

---

### FRAMEWORK-PCI-02: Access & Operations (Requirements 5-10)
**Focus:** Access control and operational procedures

**Assessment Criteria:**
- Antivirus/malware protection
- Secure system updates
- Access control & authentication
- Audit trails & logging

---

### FRAMEWORK-PCI-03: Testing & Compliance (Requirements 11-12)
**Focus:** Testing, monitoring, and compliance management

**Assessment Criteria:**
- Security testing (penetration testing, vulnerability scanning)
- Monthly scanning
- Annual penetration testing
- Security policies
- Training
- Incident response procedures

---

## Remediation Action Cards (8 cards)

**Remediation Cards** represent specific actions to address compliance findings. These can be used after an audit to remediate identified gaps.

### REMEDIATION-01: Implement MFA
**Cost:** 5 Budget
**Timeline:** 2-4 weeks
**Difficulty:** Low-Medium

**What it does:**
- Deploy multi-factor authentication for all user access
- Implement MFA for VPN, remote access, email, admin access
- Select authentication method (authenticator app, hardware token, SMS)

**Prerequisites:**
- Identity management system (Domain Controller, Azure AD)
- User device (phone or security key)
- Application/system support for MFA

**Prerequisites:**
- Reduces DOMAIN-02 (Access Control) findings
- Makes credential attacks (T-03, T-06) harder
- Improves Incident Response and Disaster Recovery modifiers

---

### REMEDIATION-02: Deploy SIEM
**Cost:** 15 Budget
**Timeline:** 4-8 weeks
**Difficulty:** Medium

**What it does:**
- Deploy Security Information & Event Management (SIEM)
- Configure log collection from all systems
- Create alert rules for suspicious activity
- Implement 24/7 monitoring

**Prerequisites:**
- Centralized logging infrastructure
- SIEM software/service (Splunk, ELK, QRadar, Azure Sentinel)
- Security personnel to manage SIEM

**Impact:**
- Reduces DOMAIN-03 (Threat Detection) findings
- Enables early breach detection
- Improves Incident Response investigation
- Provides audit trail for compliance

---

### REMEDIATION-03: Implement Network Segmentation
**Cost:** 12 Budget
**Timeline:** 4-6 weeks
**Difficulty:** Medium-High

**What it does:**
- Divide network into security zones (DMZ, internal, admin)
- Deploy firewalls between zones
- Configure firewall rules for inter-zone traffic
- Implement VLANs and network isolation

**Prerequisites:**
- Network switches/routers capable of VLAN support
- Firewall(s) for inter-zone traffic
- Network diagram and access requirements

**Impact:**
- Reduces DOMAIN-01 (Network Segmentation) findings
- Prevents lateral movement (T-04 becomes harder)
- Improves Disaster Recovery (limits blast radius)
- Foundational for zero-trust architecture

---

### REMEDIATION-04: Backup & Disaster Recovery
**Cost:** 10 Budget
**Timeline:** 2-4 weeks
**Difficulty:** Low-Medium

**What it does:**
- Implement 3-2-1 backup strategy (3 copies, 2 media, 1 offsite)
- Configure automated backups
- Test backup restoration (quarterly)
- Document recovery procedures

**Prerequisites:**
- Backup software/service
- Off-site storage location
- Testing schedule

**Impact:**
- Reduces DOMAIN-04 (Backup & DR) findings
- Enables ransomware recovery
- Improves Disaster Recovery (reduces costs)
- Supports compliance requirements

---

### REMEDIATION-05: Security Training Program
**Cost:** 3 Budget
**Timeline:** 1-2 weeks (ongoing)
**Difficulty:** Low

**What it does:**
- Develop security awareness training curriculum
- Conduct initial training for all employees
- Implement phishing simulations
- Quarterly refresher training

**Prerequisites:**
- Training development (internal or vendor)
- Management buy-in (release time for employees)

**Impact:**
- Reduces DOMAIN-06 (Security Ops) findings
- Reduces phishing success rate
- Improves overall security culture
- Compliance requirement (most frameworks)

---

### REMEDIATION-06: Vendor Security Assessment
**Cost:** 5 Budget
**Timeline:** 2-4 weeks
**Difficulty:** Low-Medium

**What it does:**
- Develop vendor security questionnaire
- Send questionnaires to key vendors
- Review vendor security controls
- Document vendor risk assessment
- Establish SLAs with security requirements

**Prerequisites:**
- Vendor list and criticality assessment
- Security questionnaire template
- Document review process

**Impact:**
- Reduces DOMAIN-05 (Third-Party Risk) findings
- Identifies supply chain risks
- Prevents SCENARIO-03 (Supply Chain Compromise)
- Compliance requirement (GDPR, etc.)

---

### REMEDIATION-07: Vulnerability Management Program
**Cost:** 8 Budget
**Timeline:** 3-4 weeks
**Difficulty:** Medium

**What it does:**
- Deploy vulnerability scanning tools
- Establish patching procedures
- Configure patch management automation
- Document vulnerability remediation process

**Prerequisites:**
- Vulnerability scanner (Nessus, Qualys, OpenVAS)
- Patch management tools or procedures
- Prioritization process (critical vs. non-critical)

**Impact:**
- Reduces multiple audit findings
- Prevents PT-05 (Privilege Escalation via unpatched kernel)
- Improves overall security posture

---

### REMEDIATION-08: Incident Response Plan & Team
**Cost:** 12 Budget
**Timeline:** 4-6 weeks (plus ongoing)
**Difficulty:** Medium-High

**What it does:**
- Develop incident response plan (procedures, contacts, escalation)
- Establish incident response team
- Conduct tabletop exercises
- Implement communication procedures

**Prerequisites:**
- Team designation (CISO, security analysts, IT, legal, PR)
- Plan documentation
- Training and exercises

**Impact:**
- Reduces DOMAIN-03 (Threat Detection) and DOMAIN-06 (Security Ops) findings
- Enables faster response to Incident Response module
- Improves Disaster Recovery effectiveness
- Compliance requirement (nearly universal)

---

## Using Compliance Frameworks in Gameplay

### Standalone Compliance Assessment
1. Choose one framework (e.g., NIST CSF, CIS Controls, PCI-DSS)
2. Assess each requirement
3. Score and document findings
4. Develop remediation roadmap
5. **Game ends:** Compliance report delivered

### Framework-Specific Play
- **NIST:** For government/critical infrastructure players
- **CIS:** For general security posture assessment
- **PCI:** For organizations handling payment cards
- **HIPAA:** For healthcare (expansion deck)

### Remediation Roadmap
1. After audit, teams identify high-priority findings
2. Allocate budget to remediation actions
3. Spend Budget to fix findings
4. Re-assess after remediation
5. Track compliance journey

---

## Print Instructions

1. Print on cardstock (250 gsm minimum)
2. Framework color-coding:
   - **Blue (NIST):** FRAMEWORK-NIST-01 to FRAMEWORK-NIST-05
   - **Orange (CIS):** FRAMEWORK-CIS-01 to FRAMEWORK-CIS-03
   - **Red (PCI):** FRAMEWORK-PCI-01 to FRAMEWORK-PCI-03
   - **Green (Remediation):** REMEDIATION-01 to REMEDIATION-08
3. Include assessment rubric (1-5 stars) on each framework card
4. Include cost/timeline/difficulty on remediation cards
5. Cut along dotted lines

---

## Possible Expansion: Additional Frameworks

- **HIPAA:** Healthcare specific (Privacy Rule, Security Rule, Breach Notification)
- **GDPR:** European Union data protection (7 principles, 99 articles)
- **ISO 27001:** International standard (14 control categories)
- **SOC 2:** Service organization controls (trust principles)
- **COBIT:** IT governance (governance & management objectives)

---

*Audit & Compliance Module: Compliance Frameworks & Remediation (Expansion)*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.1 - Balanced & Refined Edition*
