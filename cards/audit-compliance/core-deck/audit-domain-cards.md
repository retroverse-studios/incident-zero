# Audit & Compliance Module: Audit Domain Assessment Cards

**Version:** 2.1 - Balanced & Refined Edition
**Last Updated:** October 2025

---

## Overview

**Audit Domain Assessment Cards** represent six critical security domains that an organization must have controls for. Each domain is assessed independently, with findings recorded on a standard audit report.

- **Total Cards:** 6 (DOMAIN-01 to DOMAIN-06)
- **Used In:** Audit & Compliance module (primary gameplay)
- **Assessment Method:** Auditor reviews evidence, scores domain (1-5 stars)
- **Purpose:** Identify gaps that become modifiers in other modules

---

## Assessment Methodology

### The Audit Process

1. **Assessment:** Auditor reviews domain for evidence of controls
2. **Scoring:** Rate domain 1-5 stars based on maturity
   - ⭐ (1 star): No controls, critical findings
   - ⭐⭐ (2 stars): Minimal controls, major findings
   - ⭐⭐⭐ (3 stars): Adequate controls, minor findings
   - ⭐⭐⭐⭐ (4 stars): Strong controls, few findings
   - ⭐⭐⭐⭐⭐ (5 stars): Excellent controls, no findings
3. **Findings:** Record specific gaps (vulnerabilities, non-compliance)
4. **Remediation:** Recommend actions to address findings
5. **Report:** Compile audit findings and recommendations

### Scoring Impact

**Domain Score determines:**
- Audit Grade (1-5 stars)
- Findings Severity (critical/major/minor)
- Modifiers for other modules (IR, DR get harder if audit failed)
- Compliance Status (pass/fail/remediation needed)

---

## Audit Domain Cards

### DOMAIN-01: Network Segmentation & Isolation
**Focus:** How well is network divided into protected segments?
**Critical For:** Preventing lateral movement
**Regulatory References:** PCI-DSS (network segmentation), NIST (zero trust)

**What's Assessed:**
- Is network flat (1 segment) or segmented (multiple segments)?
- Are sensitive systems isolated (DMZ, database segment, admin segment)?
- Are firewall rules enforced between segments?
- Is network architecture documented?
- Are VLANs/subnets properly configured?

**Typical Findings:**
- **Critical (1-2 star):** Flat network, no segmentation, everything can talk to everything
- **Major (2-3 star):** Basic segmentation exists, but enforcement is weak
- **Minor (3-4 star):** Segmentation exists, few rule violations
- **Compliant (4-5 star):** Strong segmentation, zero-trust architecture

**Real-World Question:**
"If one system is compromised, how far can the attacker spread?"
- Flat network: Entire organization immediately
- 3-zone network: Blocked by firewalls
- Zero-trust: Individual systems isolated

**Audit Evidence:**
- Network diagram (shows segments)
- Firewall rule documentation
- Network ACL lists
- Proof of implementation (switch configs)
- Test results (can systems cross segments? No)

**Compliance Standards:**
- PCI-DSS Requirement 1: Network segmentation for cardholder data
- NIST CSF: PR.AC-4 (Access control restricted by segmentation)
- CIS Control 12: Boundary Defense

**Findings Template:**
```
FINDING: Network segmentation inadequate
SEVERITY: [Critical/Major/Minor]
DESCRIPTION: The network is [flat/minimally segmented], allowing [lateral movement/unauthorized access]
RECOMMENDATION: Implement [VLAN/firewall rules/zero-trust] to segment [database/admin/sensitive systems]
EFFORT: [1-5] weeks
COST: [Moderate/High/Very High]
```

**Remediation Actions:**
- ✓ Implement network segmentation (ARCH-02, ARCH-03 in Network Building)
- ✓ Deploy firewall with segmentation rules (SEC-08)
- ✓ Implement zero-trust architecture (ARCH-03)
- ✓ Test segmentation enforcement

**Impact if Failed (1-2 stars):**
- T-04 (Lateral Movement) becomes trivial for attackers
- Incident Response becomes much harder (-2 modifier to investigate/contain)
- Disaster Recovery is harder (attacker spreads widely)

---

### DOMAIN-02: Access Control & Identity Management
**Focus:** How are user identities managed and access controlled?
**Critical For:** Preventing unauthorized access
**Regulatory References:** HIPAA (access controls), GDPR (access management)

**What's Assessed:**
- Is there centralized identity management (Domain Controller/Azure AD)?
- Is multi-factor authentication (MFA) enabled for sensitive access?
- Are access permissions based on least privilege?
- Are access reviews performed (verify who has access)?
- Are privileged accounts managed (admin accounts, service accounts)?

**Typical Findings:**
- **Critical (1-2 star):** No centralized identity, weak passwords, no MFA
- **Major (2-3 star):** Some identity management, MFA not universal
- **Minor (3-4 star):** Good identity management, minor gaps
- **Compliant (4-5 star):** Strong identity, MFA everywhere, privilege management

**Real-World Question:**
"How easily can an attacker use stolen credentials?"
- Weak: No MFA, can use stolen password immediately
- Medium: MFA only for some systems
- Strong: MFA everywhere, weak credentials are useless

**Audit Evidence:**
- AD/directory configuration
- MFA enrollment status
- Access policy documentation
- Privileged account audit (who has admin?)
- Account review records (periodic access verification)

**Compliance Standards:**
- PCI-DSS Requirement 8: User identification and authentication
- HIPAA Rule 164.308(a)(4): Unique user identification
- NIST CSF: PR.AC-1 (Physical & logical access controls)

**Findings Template:**
```
FINDING: Multi-factor authentication not universally enforced
SEVERITY: [Critical/Major/Minor]
DESCRIPTION: MFA is [not implemented/optional] for [VPN/email/admin access]
RECOMMENDATION: Deploy [MFA solution] to [affected systems]
EFFORT: [2-4] weeks
COST: [Low/Moderate/High]
```

**Remediation Actions:**
- ✓ Deploy MFA (D-07 in Hardening)
- ✓ Implement password vault (D-12)
- ✓ Credential Guard for privileged access (D-16)
- ✓ Access reviews quarterly

**Impact if Failed (1-2 stars):**
- T-03 (Compromised Credentials), T-06 (Mimikatz) become likely
- Incident Response harder (attacker has valid credentials)
- Disaster Recovery harder (attacker can restore themselves with stolen creds)
- -2 modifier to Incident Response defense against credential-based attacks

---

### DOMAIN-03: Threat Detection & Incident Response
**Focus:** Can the organization detect and respond to attacks?
**Critical For:** Finding breaches quickly
**Regulatory References:** GDPR (breach detection), HIPAA (log monitoring)

**What's Assessed:**
- Are logs being collected centrally (SIEM or similar)?
- Is there 24/7 monitoring of critical systems?
- Are alerts configured to detect suspicious activity?
- Is there incident response plan documented?
- Are incident responders trained?

**Typical Findings:**
- **Critical (1-2 star):** No logging, no monitoring, no incident response plan
- **Major (2-3 star):** Some logging, limited monitoring
- **Minor (3-4 star):** Good logging, some gaps in alerting
- **Compliant (4-5 star):** Comprehensive logging, active monitoring, trained team

**Real-World Question:**
"How quickly will you detect an active attacker?"
- Poor: Days/weeks (after data is already stolen)
- Medium: Hours (after attacker has spread)
- Strong: Minutes (catch attacker early)

**Audit Evidence:**
- SIEM/logging configuration
- Alert rules documentation
- Incident response plan
- Training records (who's trained?)
- Incident history (how did you detect past incidents?)

**Compliance Standards:**
- GDPR Article 33: Breach notification timing (72 hours)
- HIPAA Rule 164.308(a)(6): Incident response procedures
- NIST CSF: DE.AE-3 (Event detection processes)

**Findings Template:**
```
FINDING: Insufficient threat detection and monitoring
SEVERITY: [Critical/Major/Minor]
DESCRIPTION: [SIEM/monitoring] is [not deployed/inadequately configured]
RECOMMENDATION: Deploy [SIEM] with [alert rules] to detect [attack patterns]
EFFORT: [4-8] weeks
COST: [Moderate/High]
```

**Remediation Actions:**
- ✓ Deploy SIEM (D-09, D-22)
- ✓ Configure log centralization (D-05)
- ✓ Create SIEM correlation rules (D-10)
- ✓ Threat hunting program (D-13)

**Impact if Failed (1-2 stars):**
- Breach detection is late (attacker has time to steal data)
- Incident Response starts late (investigates old attacks)
- Dwell time increases (attacker has more time)
- +5 turn penalty in Incident Response (late detection)

---

### DOMAIN-04: Backup & Disaster Recovery
**Focus:** Can the organization recover from attacks/disasters?
**Critical For:** Ransomware resilience
**Regulatory References:** Most breach laws mention recovery

**What's Assessed:**
- Is there a documented backup strategy (frequency, retention)?
- Are backups tested regularly (restore actually works)?
- Is backup storage off-site (geographically separated)?
- Are backups immutable (cannot be deleted/encrypted)?
- Is recovery time objective (RTO) documented for each system?

**Typical Findings:**
- **Critical (1-2 star):** No backups or untested backups (may not restore)
- **Major (2-3 star):** Backups exist but not properly tested
- **Minor (3-4 star):** Backups exist and tested, gaps in immutability
- **Compliant (4-5 star):** 3-2-1 strategy, tested, immutable, offsite

**Real-World Question:**
"Can you recover from ransomware?"
- Poor: No (backups are encrypted too)
- Medium: Yes but slowly (days to recover)
- Strong: Yes quickly (hours to recover, immutable backups)

**Audit Evidence:**
- Backup schedule/documentation
- Backup test results (prove restore works)
- Off-site backup location documentation
- Immutable backup configuration
- Recovery time estimates

**Compliance Standards:**
- Most breach laws assume backups exist (no recovery = massive damage)
- HIPAA Rule 164.308(a)(7): Data backup procedures
- NIST CSF: PR.IP-4 (Resilience practices documented)

**Findings Template:**
```
FINDING: Backup and recovery procedures inadequate
SEVERITY: [Critical/Major/Minor]
DESCRIPTION: Backups are [not tested/not off-site/not immutable]
RECOMMENDATION: Implement [3-2-1 strategy] with [immutable storage]
EFFORT: [2-4] weeks
COST: [Moderate]
```

**Remediation Actions:**
- ✓ Implement 3-2-1 backup strategy (D-19)
- ✓ Test backups quarterly (prove restore works)
- ✓ Immutable storage (WORM, cloud versioning)
- ✓ Off-site backup location

**Impact if Failed (1-2 stars):**
- Ransomware attacks cannot be recovered from
- Disaster Recovery becomes much harder (+25 Budget cost)
- Business interruption is long (days vs hours)
- May result in game loss (cannot recover)

---

### DOMAIN-05: Third-Party Risk & Cloud Security
**Focus:** How well are vendors and cloud services managed?
**Critical For:** Managing supply chain risk
**Regulatory References:** GDPR (processor accountability), PCI-DSS (vendor security)

**What's Assessed:**
- Is there a vendor management program?
- Are vendors required to meet security standards?
- Are vendor assessments conducted (security questionnaires, audits)?
- Are cloud configurations secured (IAM, encryption, monitoring)?
- Is data residency managed (where is customer data stored)?

**Typical Findings:**
- **Critical (1-2 star):** No vendor management, cloud misconfigured
- **Major (2-3 star):** Basic vendor management, cloud gaps
- **Minor (3-4 star):** Vendor management exists, minor gaps
- **Compliant (4-5 star):** Strong vendor program, cloud security

**Real-World Question:**
"Is your vendor secure?"
- Poor: No idea (never asked them)
- Medium: They said they're secure (took their word)
- Strong: Assessed and monitored (ongoing verification)

**Audit Evidence:**
- Vendor management policy
- Vendor security questionnaires
- Cloud configuration documentation
- IAM policies for cloud access
- Data residency mapping

**Compliance Standards:**
- GDPR Article 28: Processor agreements (vendor security required)
- PCI-DSS Requirement 12.8: Service provider agreements
- NIST CSF: PR.AT-2 (Vendor risk management)

**Findings Template:**
```
FINDING: Vendor and cloud security assessment inadequate
SEVERITY: [Critical/Major/Minor]
DESCRIPTION: [Vendor/Cloud] security is [not assessed/misconfigured]
RECOMMENDATION: Implement [vendor assessment process/cloud security hardening]
EFFORT: [3-6] weeks
COST: [Low/Moderate]
```

**Remediation Actions:**
- ✓ Vendor management program (SLAs, security requirements)
- ✓ Cloud security posture management (CSPM tools)
- ✓ Cloud IAM hardening (least privilege)
- ✓ Regular vendor assessments

**Impact if Failed (1-2 stars):**
- SCENARIO-03 (Supply Chain Compromise) becomes likely in Disaster Recovery
- Vendor breach affects your customers
- Liability disputes (who's responsible?)
- +15 Budget cost in Disaster Recovery

---

### DOMAIN-06: Security Operations & Monitoring
**Focus:** How is security operationalized (day-to-day)?
**Critical For:** Sustained security posture
**Regulatory References:** Most frameworks mention continuous monitoring

**What's Assessed:**
- Is there a dedicated security team (CISO, analysts)?
- Are security meetings held regularly?
- Is vulnerability scanning done regularly?
- Are patches applied timely?
- Is security training conducted?

**Typical Findings:**
- **Critical (1-2 star):** No security team, no updates, no training
- **Major (2-3 star):** Small security team, infrequent patching
- **Minor (3-4 star):** Security team exists, good operations
- **Compliant (4-5 star):** Mature security operations, continuous improvement

**Real-World Question:**
"Is security a priority for the organization?"
- Poor: No dedicated resources
- Medium: Part-time effort
- Strong: Dedicated team, empowered leadership

**Audit Evidence:**
- Org chart (is CISO position filled?)
- Security meeting minutes
- Vulnerability scan reports
- Patch management records
- Training records

**Compliance Standards:**
- Most frameworks require security leadership
- NIST CSF: PR.IP-1 (Security policy established & communicated)
- CIS Controls 19: Incident response planning & exercises

**Findings Template:**
```
FINDING: Security operations maturity inadequate
SEVERITY: [Critical/Major/Minor]
DESCRIPTION: [Security team/training/patching] is [insufficient]
RECOMMENDATION: [Hire/train/increase resources] for [security function]
EFFORT: [Ongoing]
COST: [Varies]
```

**Remediation Actions:**
- ✓ Hire CISO (if missing)
- ✓ Establish security team
- ✓ Regular vulnerability scanning
- ✓ Patch management program
- ✓ Security awareness training

**Impact if Failed (1-2 stars):**
- Security functions are reactive (not proactive)
- Incident Response is harder (-1 modifier)
- Vulnerabilities accumulate (PT-10 Zero-Day risk increases)
- Overall security posture degrades

---

## Audit Domain Summary

| Domain | Focus | Critical Finding | Remediation Effort | Compliance Impact |
|--------|-------|------------------|-------------------|------------------|
| DOMAIN-01 | Network Segmentation | Flat network | Moderate (2-4 wk) | Lateral movement prevented |
| DOMAIN-02 | Access Control | No MFA | Low (2-4 wk) | Credential attacks harder |
| DOMAIN-03 | Threat Detection | No SIEM | High (4-8 wk) | Breach detection enabled |
| DOMAIN-04 | Backup & DR | No backups | Moderate (2-4 wk) | Ransomware resilience |
| DOMAIN-05 | Vendor Risk | No assessment | Low (3-6 wk) | Supply chain risk managed |
| DOMAIN-06 | Security Ops | No security team | High (ongoing) | Sustained security posture |

---

## Audit Scoring & Findings

### Standard Audit Report Format

```
AUDIT REPORT - [Organization Name]
Audit Date: [Date]
Domains Assessed: 6
Overall Score: [X/6 stars]

DOMAIN SCORES:
1. Network Segmentation: ⭐⭐ (2 stars) - NEEDS WORK
2. Access Control: ⭐⭐⭐ (3 stars) - ADEQUATE
3. Threat Detection: ⭐ (1 star) - CRITICAL
4. Backup & DR: ⭐⭐ (2 stars) - NEEDS WORK
5. Vendor Risk: ⭐⭐ (2 stars) - NEEDS WORK
6. Security Ops: ⭐⭐⭐⭐ (4 stars) - STRONG

CRITICAL FINDINGS (must fix immediately):
- No SIEM or threat monitoring
- Network is completely flat (no segmentation)

MAJOR FINDINGS (fix within 30 days):
- No backup strategy
- Vendor security not assessed
- MFA not implemented

MINOR FINDINGS (fix within 90 days):
- Security training curriculum needs update

RECOMMENDATIONS:
1. Deploy SIEM immediately (critical)
2. Implement network segmentation
3. Establish backup program
4. Implement MFA
5. Develop vendor management program
```

---

## Modifiers for Other Modules

### Incident Response Modifiers

**For each failed domain (1-2 stars):**
- Network Segmentation failed: -1 modifier to contain lateral movement
- Access Control failed: Attackers have easy credential path (+1 difficulty)
- Threat Detection failed: +5 turns to investigate (late detection)
- Backup failed: No offline backup available (complicates recovery)
- Vendor Risk failed: Supply chain may be compromised (+1 threat to track)
- Security Ops failed: -1 to all investigation rolls (weak team)

**Example:** If 3 domains fail, IR gets -2 to -5 modifiers (making it harder)

### Disaster Recovery Modifiers

**For each failed domain (1-2 stars):**
- Network Segmentation failed: +10 Budget cost (attacker spread more, costs more)
- Access Control failed: +5 Budget (credential reset costs more)
- Threat Detection failed: +5 Budget (investigation slower, costs more)
- Backup failed: +25 Budget cost (cannot recover from backup, full rebuild)
- Vendor Risk failed: +15 Budget (vendor negotiation, replacement costs)
- Security Ops failed: +10 Budget (team less effective, need consultants)

**Example:** If all 6 domains fail, DR gets +70 Budget cost increase (from 120 to 190)

---

## Gameplay Notes

### Playing Audit Standalone
1. Assess all 6 domains
2. Score each domain (1-5 stars)
3. Record findings
4. Compile audit report
5. **Game ends:** Audit complete, recommendations provided

### Playing Audit as Module Lead-In
1. Play Audit first (establish baseline)
2. Get audit report with findings
3. Play Incident Response (audit failures become modifiers)
4. Play Disaster Recovery (audit failures increase costs)
5. **Narrative:** Poor audit = harder subsequent modules

### Audit Remediation Follow-Up (Optional)
1. After audit report, teams can remediate findings
2. Spend Budget to fix findings
3. Re-assess domain (did remediation work?)
4. Update modifiers for downstream modules

---

## Print Instructions

1. Print on cardstock (250 gsm minimum)
2. Color-code by domain function:
   - **Blue (Infrastructure):** DOMAIN-01 (Segmentation)
   - **Purple (Access):** DOMAIN-02 (Identity)
   - **Red (Detection):** DOMAIN-03 (Detection)
   - **Green (Resilience):** DOMAIN-04 (Backup)
   - **Orange (Supply Chain):** DOMAIN-05 (Vendor)
   - **Yellow (Operations):** DOMAIN-06 (Ops)
3. Include assessment rubric (1-5 star descriptions)
4. Include finding templates on back of card
5. Cut along dotted lines
6. Create "Audit Scoring Reference Card" for scoring guidance

---

*Audit & Compliance Module: Audit Domain Assessment Cards*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.1 - Balanced & Refined Edition*
