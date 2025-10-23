# Network Building Module: Server Cards

**Version:** 2.1 - Balanced & Refined Edition
**Last Updated:** October 2025

---

## Overview

**Server Cards** represent the core computational systems that run your business. Each server has cost (Budget), complexity, and security properties that affect network design.

- **Total Cards:** 10 (SRV-01 to SRV-10)
- **Used In:** Network Building module
- **Cost Range:** 3-25 Budget depending on type and complexity
- **Complexity Range:** 1-4 (affects maintenance overhead, represented narratively)

---

## Server Cards

### SRV-01: Email Server
**Type:** Business Critical
**Cost:** 8 Budget
**Complexity:** 2/4
**Availability Requirement:** 99.9% (almost always needed)

**Description:**
Central email system (Exchange, Postfix, or cloud-based like Office 365). Handles all organizational communication. Commonly targeted by phishing and credential attacks. Must support spam filtering, encryption, and audit logging.

**Key Concerns:**
- Email spoofing and phishing vectors
- Credential compromise (email = access to password resets)
- Data exfiltration via email attachments and forwarding
- High user impact if unavailable

**Defense Considerations:**
- Requires Email Authentication (DMARC/SPF/DKIM)
- Benefits from DLP for sensitive email attachments
- Gateway filtering for phishing and malware
- MFA required for administrative access

**Network Placement:** DMZ or protected segment (external access required)

**Interactions:**
- Used with Asset Card "Email"
- References in Incident Response scenarios (T-01 Phishing, T-11 Browser Extension)
- Part of Disaster Recovery "critical services" list

---

### SRV-02: Web Server
**Type:** Business Critical
**Cost:** 6 Budget
**Complexity:** 2/4
**Availability Requirement:** 99.5% (critical during business hours)

**Description:**
Public-facing web application server (Apache, Nginx, IIS). Hosts corporate website, customer portal, or SaaS application. Primary attack surface for web exploits (SQL injection, XSS, remote code execution).

**Key Concerns:**
- Web application vulnerabilities (OWASP Top 10)
- Unpatched framework or library exploits
- DDoS attacks targeting availability
- Code injection and remote execution
- Data exposure via web interface

**Defense Considerations:**
- Requires WAF (Web Application Firewall) for SQL injection/XSS prevention
- IPS for exploit signature detection
- Regular patching and vulnerability scanning
- Load balancer for availability
- TLS/SSL for data in transit

**Network Placement:** DMZ (external access required, isolated from internal systems)

**Interactions:**
- Used with Asset Card "Web"
- References in Incident Response scenarios (T-02 Watering Hole, T-05 Kernel Exploit)
- Load balancer reduces single point of failure

---

### SRV-03: Database Server
**Type:** Business Critical
**Cost:** 12 Budget
**Complexity:** 3/4
**Availability Requirement:** 99.9% (critical for business operations)

**Description:**
Relational or NoSQL database (SQL Server, PostgreSQL, MongoDB, Oracle). Stores customer data, financial records, operational data. Highest value target after compromise—contains the "crown jewels."

**Key Concerns:**
- SQL injection attacks
- Credential abuse (weak database admin passwords)
- Lateral movement target (pivot point)
- Unencrypted data at rest
- Unencrypted data in transit
- Unauthorized data access and exfiltration

**Defense Considerations:**
- Requires Network Segmentation to limit access
- Credential Guard and strong authentication
- Database activity monitoring (DAM)
- TLS for all connections
- Data encryption at rest
- Regular backups with immutability
- Connection string in vault (not hardcoded)

**Network Placement:** Restricted segment (only authorized systems can connect)

**Interactions:**
- Used with Asset Card "Database"
- References in Incident Response scenarios (T-04 Lateral Movement, T-10 SQL Exfiltration, T-11 Browser Extension)
- Critical for Disaster Recovery backup and recovery

---

### SRV-04: File Server
**Type:** Business Critical
**Cost:** 7 Budget
**Complexity:** 2/4
**Availability Requirement:** 99% (needed during business hours)

**Description:**
File storage and sharing system (SMB/CIFS, NFS, or cloud file sharing). Stores shared documents, project files, compliance records. Often contains both sensitive and non-sensitive data mixed together.

**Key Concerns:**
- SMB lateral movement attacks
- Excessive file permissions (everyone can read everything)
- Ransomware encryption of shares
- Unauthorized file access and data theft
- Compliance violations (PII, PHI, PCI data stored unencrypted)
- Uncontrolled data growth and backup challenges

**Defense Considerations:**
- Network Segmentation to limit SMB access
- File permissions auditing and hardening
- DLP for sensitive file detection
- Immutable snapshots for ransomware recovery
- Encryption at rest
- Access logging and monitoring

**Network Placement:** Protected segment (limited internal access only)

**Interactions:**
- Used with Asset Card "File Storage"
- Target of T-04 Lateral Movement in Incident Response
- Critical dependency for Disaster Recovery

---

### SRV-05: Domain Controller
**Type:** Business Critical
**Cost:** 10 Budget
**Complexity:** 3/4
**Availability Requirement:** 99.5% (core infrastructure dependency)

**Description:**
Active Directory or LDAP domain controller. Master repository of all user identities, credentials, and group memberships. Most powerful target in the organization—compromise of DC gives attacker control of entire directory.

**Key Concerns:**
- Credential dumping (Mimikatz targets LSASS on DC)
- Pass-the-hash attacks
- Unauthorized privilege escalation
- DC compromise = organization is fundamentally compromised
- Backup DC synchronization complications
- Can be both on-premises and cloud (Azure AD)

**Defense Considerations:**
- Credential Guard to protect LSASS
- Privileged Access Workstation (PAW) for DC admin access
- Strong authentication (MFA) for all DC access
- Network Segmentation (DC in restricted tier)
- Backup DC in geographically separate location
- Regular backup and recovery testing

**Network Placement:** Restricted segment (admin-only access)

**Interactions:**
- Used with Asset Card "Identity"
- Central to Incident Response investigation (T-06 Mimikatz, T-04 Lateral Movement)
- DC compromise immediately loses the game (organizational control lost)
- Critical for Disaster Recovery restore procedures

---

### SRV-06: Development Server
**Type:** Business Important
**Cost:** 5 Budget
**Complexity:** 2/4
**Availability Requirement:** 80% (nice to have, can work around)

**Description:**
Development and testing environment for software development. Lower security requirements than production but often contains production-like data (for testing). Developers need broad access for testing purposes.

**Key Concerns:**
- Overly permissive developer access
- Production data in dev (compliance violations)
- Outdated/unpatched tools (focus on development, not security)
- Lateral movement springboard to production
- Code repository contains source code (intellectual property)
- Test credentials and API keys hardcoded

**Defense Considerations:**
- Separate dev database from production database (never use prod data)
- Firewall rules to prevent dev→prod lateral movement
- Code repository security (secrets scanning, access control)
- Regular cleanup of test data
- MFA for dev server access
- Audit logging of developer activities

**Network Placement:** Development segment (isolated from production)

**Interactions:**
- Used with Asset Card "Development"
- Often overlooked security risk (compliance gap in Audit module)
- Lateral movement target (attacker compromise dev to move to prod)

---

### SRV-07: Backup Server
**Type:** Business Critical (Different Tier)
**Cost:** 9 Budget
**Complexity:** 2/4
**Availability Requirement:** 95% (needed for recovery scenarios)

**Description:**
Backup and archival storage system (dedicated appliance, NAS, or cloud backup like Veeam, Commvault, or Backblaze). Stores point-in-time copies of all critical systems. The ultimate recovery mechanism for ransomware, disasters, and destructive attacks.

**Key Concerns:**
- Backup corruption or compromise (renders backups useless)
- Ransomware targeting backup systems
- Backup media not separated from primary systems
- Backups not regularly tested (recovery fails when needed)
- Immutability not enforced (backups can be modified)
- Access control: who can restore? Who can delete?

**Defense Considerations:**
- **CRITICAL:** 3-2-1 backup strategy: 3 copies, 2 media types, 1 offsite
- Immutable backups (WORM - Write Once Read Many)
- Encryption at rest and in transit
- Backup testing schedule (quarterly minimum)
- Separate backup credentials (not domain-linked)
- Offsite backup location (geographically separated)
- Backup media inventory and audit log

**Network Placement:** Restricted segment + offsite (separate from primary network)

**Interactions:**
- Used with Asset Card "Disaster Recovery"
- Critical for Disaster Recovery module (backup resilience determines recovery speed)
- If backup is compromised, cannot recover from ransomware (immediately lose game)
- Incident Response mentions backup verification in defenses

---

### SRV-08: Cloud Workload
**Type:** Increasingly Business Critical
**Cost:** 4 Budget
**Complexity:** 2/4 (but different concerns than on-premises)
**Availability Requirement:** 99% (vendor manages SLA)

**Description:**
Cloud-hosted application or service (AWS EC2, Azure VM, GCP Compute Engine, or fully managed service like Lambda, Cloud Run). Shifts some infrastructure management to cloud provider but introduces new security concerns.

**Key Concerns:**
- Misconfigured security groups/network ACLs (open to internet)
- Cloud credentials compromise (AWS IAM keys stolen)
- Instance metadata service attacks (AWS IMDS exploitation)
- Cross-account or cross-tenant access (shared infrastructure)
- Cloud-specific vulnerabilities (API, permissions models)
- Data residency and compliance (where is data stored?)

**Defense Considerations:**
- Cloud-native security tools (AWS Security Hub, Azure Security Center)
- Proper IAM configuration (least privilege for cloud roles)
- Network security groups with default-deny
- Cloud workload protection (container runtime security)
- VPC and subnet isolation
- Encryption of cloud data

**Network Placement:** Cloud provider network (separate from on-premises, connected via VPN)

**Interactions:**
- Used with Asset Card (varies—Email in cloud, Web in cloud, etc.)
- Network design must include cloud connectivity (VPN or Direct Connect)
- Audit module assesses cloud security posture
- Cloud-specific Incident Response and Hardening challenges

---

### SRV-09: Legacy System
**Type:** Business Important (Legacy)
**Cost:** 3 Budget
**Complexity:** 3/4 (difficult to maintain, patch, or secure)
**Availability Requirement:** 90% (supported but aging)

**Description:**
Aging system running outdated OS (Windows XP, older Linux, proprietary systems) or custom applications. Cannot be easily patched due to compatibility issues, vendor no longer supporting, or critical business process depends on it.

**Key Concerns:**
- Cannot patch due to vendor EOL (End of Life)
- Incompatible with modern security tools (EDR won't run)
- No TLS support (unencrypted traffic)
- Known, publicly disclosed vulnerabilities with no fix
- Business relies on it despite security risk
- Migration cost exceeds security benefit (economically trapped)

**Defense Considerations:**
- **CRITICAL:** Network Segmentation isolates legacy system
- Firewall rules restrict legacy system traffic
- Assume compromise and defend the segmented network (not the legacy system itself)
- Monitor legacy system for suspicious activity (can't detect on system, detect on network)
- Immutable backups to restore if compromised
- Plan legacy system retirement

**Network Placement:** Isolated segment (strict firewall rules, minimal connectivity)

**Interactions:**
- Used if organization has legacy infrastructure
- Audit module finds legacy systems as critical findings
- Network design: "assume legacy is compromised, defend around it"
- Expansion deck explores legacy system challenges

---

### SRV-10: Honeypot Decoy
**Type:** Security Tool (Non-Business)
**Cost:** 2 Budget
**Complexity:** 1/4 (purposefully simple and unmonitored-looking)
**Availability Requirement:** N/A (false resource)

**Description:**
Deliberately exposed fake server or user account designed to detect compromise and lateral movement. Appears to be a real business resource but is actually a trap. Any access to honeypot indicates active attacker activity (zero false positives).

**Key Concerns:**
- Placement visibility (attacker must discover it to trigger it)
- Believability (must look like real system worth attacking)
- Monitoring (honeypot access must be logged securely)
- Honeypot maintenance (must not appear unmaintained)
- Response procedures (what do we do when honeypot is triggered?)

**Defense Considerations:**
- Canary tokens (watermarked documents, fake credentials)
- Fake administrative account (admin account that isn't really admin)
- Fake file server with sensitive-looking shares
- Fake VIP email addresses on mailing lists
- Alerting on any access to honeypot (immediate incident response)

**Network Placement:** Among legitimate resources (cannot appear isolated)

**Interactions:**
- Used with Deception Technology defense card in Hardening
- Network design: "place honeypots where attackers will likely look"
- Zero false positives: any honeypot access = real attack
- Expansion deck discusses advanced honeypot strategies

---

## Server Card Summary

| Card | Server Type | Cost | Complexity | Availability | Key Risk |
|------|-------------|------|-----------|--------------|----------|
| SRV-01 | Email Server | 8 | 2/4 | 99.9% | Phishing, Credential Abuse |
| SRV-02 | Web Server | 6 | 2/4 | 99.5% | Web Exploits, RCE |
| SRV-03 | Database Server | 12 | 3/4 | 99.9% | SQL Injection, Data Exfil |
| SRV-04 | File Server | 7 | 2/4 | 99% | SMB Laterals, Ransomware |
| SRV-05 | Domain Controller | 10 | 3/4 | 99.5% | Mimikatz, Complete Compromise |
| SRV-06 | Development | 5 | 2/4 | 80% | Lateral Movement, Data Leak |
| SRV-07 | Backup Server | 9 | 2/4 | 95% | Ransomware, Recovery Failure |
| SRV-08 | Cloud Workload | 4 | 2/4 | 99% | Misconfiguration, IAM Abuse |
| SRV-09 | Legacy System | 3 | 3/4 | 90% | Known Vulns, Cannot Patch |
| SRV-10 | Honeypot | 2 | 1/4 | N/A | Detection, Early Warning |

---

## Gameplay Notes

### Budget Considerations
- **Cheapest:** Honeypot (2), Cloud Workload (4), Development (5)
- **Mid-range:** Web Server (6), File Server (7), Email Server (8), Backup Server (9)
- **Most Expensive:** Domain Controller (10), Database Server (12)
- **Total budget:** 76 for all servers (teams must prioritize)

### Complexity Considerations
- High complexity servers (DC, Database, Legacy) require more operational overhead
- Teams with strong Ops team can handle complexity better
- Low complexity servers (Web, Email) are easier to manage

### Business Requirement Mapping
Each server fulfills one or more Asset Card requirements:
- SRV-01 → Asset "Email"
- SRV-02 → Asset "Web"
- SRV-03 → Asset "Database"
- SRV-04 → Asset "File Storage"
- SRV-05 → Asset "Identity"
- SRV-06 → Asset "Development"
- SRV-07 → Asset "Disaster Recovery"
- SRV-08 → Asset (varies—could be Email, Web, Database in cloud)
- SRV-09 → Asset (legacy system supporting specific business function)
- SRV-10 → Security monitoring (not a business requirement)

---

## Print Instructions

1. Print on cardstock (250 gsm minimum)
2. Color-code by business criticality:
   - **Red:** SRV-03, SRV-05, SRV-07 (Business Critical - cannot lose)
   - **Yellow:** SRV-01, SRV-02, SRV-04 (Important - high impact if down)
   - **Blue:** SRV-06, SRV-08, SRV-09 (Business Important - can work around)
   - **Green:** SRV-10 (Security Tool - special purpose)
3. Cut along dotted lines
4. Consider creating a separate "Server Reference Card" with costs and complexity for quick lookup

---

*Network Building Module: Server Cards*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.1 - Balanced & Refined Edition*
