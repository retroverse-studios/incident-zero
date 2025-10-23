# Network Building Module: Asset Cards

**Version:** 2.1 - Balanced & Refined Edition
**Last Updated:** October 2025

---

## Overview

**Asset Cards** represent business requirements or critical functions that the network must support. Each asset card describes a business need, and teams must ensure their network design includes appropriate servers/services to satisfy each requirement.

- **Total Cards:** 8 (ASSET-01 to ASSET-08)
- **Used In:** Network Building (to validate network design meets requirements)
- **Also Used In:** Incident Response (scenario context), Disaster Recovery (impact assessment)
- **Purpose:** Ensures network design addresses real business needs, not just security checkbox items

---

## Asset Cards

### ASSET-01: Email
**Business Function:** Internal and external email communication
**Criticality:** High (nearly universal requirement)
**Impact if Down:** Significant (communication stops, customer requests missed)
**Compliance Requirements:** Email retention (SOX, GDPR), encryption (HIPAA, PCI-DSS)

**Description:**
Organization needs reliable email system for internal communication and external customer contact. Email is both critical infrastructure and significant security risk (phishing, credential attacks, data exfiltration).

**Network Requirements:**
- **Server:** Email Server (SRV-01)
- **Protection:** Email Gateway (SEC-06) for phishing/malware filtering
- **Optional:** Load Balancer if email server needs redundancy

**Security Considerations:**
- Email is primary phishing attack vector (T-01 in Incident Response)
- Email contains sensitive information (must be encrypted and access-controlled)
- Email forwarding rules can be abused for data exfiltration
- Email archive must be protected and retained per compliance requirements

**Dependencies:**
- Requires Domain Controller for user authentication
- Requires backup for email archive recovery
- Integrates with SIEM for email security event logging

**Team Design Validation:**
✓ **Must Include:** Email Server or equivalent email service (cloud-based OK)
✓ **Should Include:** Email Gateway for threat filtering
✗ **Failure Condition:** No email capability = cannot satisfy Asset requirement

---

### ASSET-02: Web
**Business Function:** Public-facing web application or website
**Criticality:** Medium (business depends on it but alternatives exist)
**Impact if Down:** Moderate (customers cannot access services, lost sales/engagement)
**Compliance Requirements:** PCI-DSS (if payments), WCAG accessibility

**Description:**
Organization has public web presence—either corporate website, e-commerce site, or customer portal. Web server is exposed to internet and primary target for web exploits (SQL injection, RCE, DDoS).

**Network Requirements:**
- **Server:** Web Server (SRV-02) in DMZ
- **Protection:** WAF (SEC-07) for application-layer attack prevention
- **Optional:** Load Balancer (SEC-04) for redundancy and DDoS protection

**Security Considerations:**
- Web servers have highest internet attack surface
- Vulnerable to web exploits (T-02 Watering Hole, T-05 Kernel Exploit in Incident Response)
- DDoS attacks can take down web server
- Code injection can compromise entire application
- Requires patching and web application security testing

**Dependencies:**
- Often connects to Database (for dynamic content)
- May require load balancer for redundancy
- Requires SIEM monitoring for web security events

**Team Design Validation:**
✓ **Must Include:** Web Server (SRV-02) or cloud-hosted web service
✓ **Should Include:** WAF for attack protection
✓ **Should Include:** Load Balancer if redundancy needed
✗ **Failure Condition:** No web server = Asset unsatisfied

---

### ASSET-03: Database
**Business Function:** Data storage and retrieval for critical business data
**Criticality:** Very High (most sensitive business data)
**Impact if Down:** Severe (business cannot operate, financial/customer impact)
**Compliance Requirements:** PCI-DSS, HIPAA, GDPR, SOX (depending on data type)

**Description:**
Centralized database for customer data, financial records, operational data. Database is most valuable attack target—contains the "crown jewels." Database compromise often defines loss condition in Incident Response.

**Network Requirements:**
- **Server:** Database Server (SRV-03) in restricted/admin segment
- **Protection:** Network Segmentation (SEC-08) to limit access
- **Optional:** Backup Server (SRV-07) for recovery capability

**Security Considerations:**
- Database is primary exfiltration target (T-10, T-11 in Incident Response)
- SQL injection attacks compromise database
- Credential abuse allows unauthorized access to sensitive data
- Data exfiltration is often attack goal (customer PII, financial data)
- Database compromise may be game-loss condition
- Must have immutable backups for recovery from ransomware

**Dependencies:**
- Requires strong authentication (MFA, password vault)
- Requires Data Loss Prevention (DLP) to prevent exfiltration
- Requires encryption at rest and in transit
- Requires database activity monitoring (DAM) for audit

**Team Design Validation:**
✓ **Must Include:** Database Server or equivalent data store
✓ **Should Include:** Network Segmentation to isolate database access
✓ **Should Include:** Backup Server for disaster recovery
✓ **Should Include:** DLP for sensitive data protection
✗ **Failure Condition:** No database = Asset unsatisfied OR unsecured database access = audit finding

---

### ASSET-04: File Storage
**Business Function:** Shared file storage for documents, projects, compliance records
**Criticality:** High (business relies on shared documents)
**Impact if Down:** Moderate-High (work stops, cannot access needed files)
**Compliance Requirements:** Data retention (GDPR), data classification (HIPAA, PCI-DSS)

**Description:**
Shared network file storage for collaborative work. File servers often contain mixed-sensitivity data (company policy next to customer PII next to trade secrets). Poorly secured file storage is source of data exfiltration and lateral movement.

**Network Requirements:**
- **Server:** File Server (SRV-04) in protected segment
- **Protection:** Network Segmentation (SEC-08) to limit file access
- **Optional:** DLP (in Hardening module) to prevent sensitive file exfiltration

**Security Considerations:**
- File servers are lateral movement target (T-04 in Incident Response)
- SMB protocol allows attacker to enumerate shares and attempt access
- Over-permissive file permissions = data exfiltration vector
- Ransomware frequently targets file servers (T-11 in Incident Response)
- File permissions audit is critical for compliance

**Dependencies:**
- Requires Domain Controller for user authentication
- Requires Network Segmentation to limit SMB access
- Requires backup strategy (especially for ransomware recovery)
- Requires file permission auditing

**Team Design Validation:**
✓ **Must Include:** File Server or cloud file storage (OneDrive, SharePoint, Google Drive)
✓ **Should Include:** Network Segmentation to restrict access
✓ **Should Include:** Backup for ransomware recovery
✗ **Failure Condition:** No file storage = Asset unsatisfied

---

### ASSET-05: Identity
**Business Function:** User identity and access management
**Criticality:** Very High (foundational to all access control)
**Impact if Down:** Severe (cannot authenticate users, cannot operate)
**Compliance Requirements:** MFA (various standards), audit logging (GDPR, SOX)

**Description:**
Centralized identity system (Active Directory, Azure AD, Okta) that authenticates users and grants access to resources. Identity compromise is game-over scenario—attacker with access to identity system can impersonate any user.

**Network Requirements:**
- **Server:** Domain Controller (SRV-05) in admin segment
- **Protection:** Credential Guard for LSASS protection
- **Optional:** Backup Domain Controller for redundancy

**Security Considerations:**
- Domain Controller is most sensitive system (compromise = total infrastructure access)
- Credential dumping attacks target DC (T-06 Mimikatz in Incident Response)
- Compromised DC allows attacker to create backdoor accounts
- Pass-the-hash attacks replay credentials from DC compromise
- DC must be in isolated segment with strict access control

**Dependencies:**
- Requires strong authentication (MFA for all DC access)
- Requires privileged access workstation (PAW) for admin access
- Requires immutable backup DC in separate location
- Requires audit logging of all DC changes

**Team Design Validation:**
✓ **Must Include:** Domain Controller (on-premises or Azure AD)
✓ **Should Include:** MFA for administrative access
✓ **Should Include:** Backup Domain Controller
✗ **Failure Condition:** No identity system = cannot manage users/access = game loss

---

### ASSET-06: Development
**Business Function:** Software development and testing environment
**Criticality:** Medium (important but not production-critical)
**Impact if Down:** Low-Medium (development delays, but not immediate business impact)
**Compliance Requirements:** Secrets management (API keys not hardcoded), code scanning

**Description:**
Development and testing infrastructure where software developers build and test applications. Development environment is often overlooked security risk because developers prioritize speed over security.

**Network Requirements:**
- **Server:** Development Server (SRV-06) in isolated development segment
- **Protection:** Firewall rules prevent dev→prod lateral movement
- **Optional:** Code repository (Git, GitHub) for version control

**Security Considerations:**
- Development servers often contain production-like data (compliance violation)
- Developers have broad access (weak access controls)
- Test credentials and API keys in source code
- Outdated/unpatched tools (developer tools not security tools)
- Development system as lateral movement springboard to production
- Source code repository is high-value target (intellectual property)

**Dependencies:**
- Requires separate database from production (never use production data in dev)
- Requires code review and secrets scanning
- Requires firewall rules isolating dev from production
- Requires MFA for code repository access

**Team Design Validation:**
✓ **Should Include:** Development Server for software development
✓ **Should Isolate:** Dev network from production network
✓ **Should Scan:** Code for hardcoded secrets
✗ **Failure Condition:** Using production database in dev = data exposure/compliance violation

---

### ASSET-07: Disaster Recovery
**Business Function:** Recovery capability for business continuity
**Criticality:** Very High (determines if business survives major attack/disaster)
**Impact if Down:** Catastrophic (cannot recover from major incident)
**Compliance Requirements:** Backup retention, recovery SLA (RTO/RPO)

**Description:**
Backup and disaster recovery capability. Organization needs ability to recover from data loss, ransomware, or disaster. Backup/recovery capability is often neglected until it's needed.

**Network Requirements:**
- **Server:** Backup Server (SRV-07) with off-site backups
- **Protection:** Immutable backups (WORM storage)
- **3-2-1 Strategy:** 3 copies, 2 media types, 1 off-site

**Security Considerations:**
- Ransomware attacks target backup systems (T-11 in Incident Response)
- Backup must be immutable (attacker cannot modify backups)
- Backup must be off-site (local backup lost if data center destroyed)
- Backup testing must be regular (quarterly minimum)
- Backup credentials must be separate from domain (attacker cannot delete backups)

**Dependencies:**
- Requires off-site backup location (geographically separated)
- Requires immutable storage (WORM or cloud versioning)
- Requires regular backup restore testing
- Requires separate backup credentials

**Team Design Validation:**
✓ **Must Include:** Backup Server with off-site capability
✓ **Must Test:** Recovery procedures (quarterly)
✓ **Must Implement:** 3-2-1 strategy
✗ **Failure Condition:** No backup = cannot recover from ransomware = game loss in DR module

---

### ASSET-08: VPN/Remote Access
**Business Function:** Secure remote access for employees and contractors
**Criticality:** Medium (became High during COVID pandemic)
**Impact if Down:** Moderate (remote workers cannot work)
**Compliance Requirements:** MFA (various standards), encryption, audit logging

**Description:**
VPN or similar remote access solution for employees working from home, traveling, or off-site. Remote access expands attack surface but is necessary for modern workforce.

**Network Requirements:**
- **Device:** VPN Gateway (SEC-05) at network perimeter
- **Protection:** MFA required for all VPN access
- **Optional:** Conditional access policies (restrict access by device/location)

**Security Considerations:**
- VPN is attractive attack target (Credential Abuse)
- Weak VPN credentials easily brute-forced (must use MFA)
- Compromised home computer connecting via VPN = internal network at risk
- VPN traffic must be encrypted
- VPN access must be logged and audited

**Dependencies:**
- Requires Domain Controller for user authentication
- Requires MFA (cannot rely on password alone)
- Requires endpoint security on remote devices
- Requires SIEM monitoring of VPN access

**Team Design Validation:**
✓ **Should Include:** VPN Gateway for remote access
✓ **Must Implement:** MFA for VPN access
✓ **Should Monitor:** VPN access logs in SIEM
✗ **Failure Condition:** Weak VPN security (no MFA) = credential attack vector

---

## Asset Card Summary

| Asset | Business Function | Criticality | Server | Key Defense |
|-------|------------------|-------------|--------|------------|
| ASSET-01 | Email | High | SRV-01 | Email Gateway |
| ASSET-02 | Web | Medium | SRV-02 | WAF |
| ASSET-03 | Database | Very High | SRV-03 | Network Segmentation |
| ASSET-04 | File Storage | High | SRV-04 | Network Segmentation |
| ASSET-05 | Identity | Very High | SRV-05 | Credential Guard |
| ASSET-06 | Development | Medium | SRV-06 | Network Isolation |
| ASSET-07 | Disaster Recovery | Very High | SRV-07 | Immutable Backups |
| ASSET-08 | VPN/Remote Access | Medium | SEC-05 | MFA |

---

## Gameplay Integration

### Network Building Module
Asset Cards drive network design decisions:
1. Display all 8 Asset Cards face-up on the table
2. Team designs network to satisfy each Asset
3. For each Asset, team must include appropriate Server and Defenses
4. Team validates: "Does our network design satisfy this Asset?"

### Incident Response Module
Asset Cards provide scenario context:
- Threat Orchestrator refers to Assets when describing scenarios
- "Customer database is being exfiltrated" = reference ASSET-03
- "Email is compromised" = reference ASSET-01
- Assets help Blue Team understand what they're protecting

### Disaster Recovery Module
Asset Cards determine impact assessment:
- "How many critical systems are down?" = count "Very High" Assets affected
- Recovery priority = order by Asset criticality
- RTO (Recovery Time Objective) depends on which Assets must recover first

---

## Expansion Notes

### Asset Card Variants (for specific industries)

**Financial Services Assets:**
- Trading System (real-time market data)
- Payment Processing (external integrations)
- Audit Trail (regulatory requirement)

**Healthcare Assets:**
- Electronic Health Records (HIPAA-critical)
- Prescription Management (pharmacy integration)
- Patient Portal (external access)

**Manufacturing Assets:**
- Industrial Control Systems (safety-critical)
- Supply Chain Integration (vendor systems)
- Engineering Data (intellectual property)

**Retail Assets:**
- Point of Sale (transaction processing)
- Inventory Management (supplier integration)
- Customer Loyalty (marketing data)

---

## Print Instructions

1. Print on cardstock (250 gsm minimum)
2. Color-code by criticality:
   - **Red (Very High):** ASSET-03, ASSET-05, ASSET-07
   - **Orange (High):** ASSET-01, ASSET-04
   - **Yellow (Medium):** ASSET-02, ASSET-06, ASSET-08
3. Include icons representing each asset:
   - Email: Envelope icon
   - Web: Globe icon
   - Database: Cylinder/drum icon
   - File: Folder icon
   - Identity: ID card / Shield icon
   - Development: Code brackets icon
   - Disaster Recovery: Backup/Archive icon
   - VPN: Lock/tunnel icon
4. Cut along dotted lines
5. Create a "Business Requirement Validation Card" that teams use to check off satisfied requirements

---

## Team Validation Checklist

**After team completes network design, verify each Asset is satisfied:**

- [ ] ASSET-01 (Email) - Email Server + Email Gateway
- [ ] ASSET-02 (Web) - Web Server + WAF + Load Balancer (optional)
- [ ] ASSET-03 (Database) - Database Server + Network Segmentation + DLP
- [ ] ASSET-04 (File Storage) - File Server + Network Segmentation
- [ ] ASSET-05 (Identity) - Domain Controller + Credential Guard + Backup DC
- [ ] ASSET-06 (Development) - Development Server + Network Isolation
- [ ] ASSET-07 (Disaster Recovery) - Backup Server + Off-site + Immutable
- [ ] ASSET-08 (VPN) - VPN Gateway + MFA

**If any Asset is unsatisfied or under-defended:**
- Network design is incomplete
- That Asset becomes a vulnerability in Incident Response
- That Asset affects recovery time in Disaster Recovery

---

*Network Building Module: Asset Cards*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.1 - Balanced & Refined Edition*
