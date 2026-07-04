# Audit & Compliance Module: Rules & Mechanics

**Version:** 2.2 - Playtest Edition
**Last Updated:** October 2025

> **v2.2:** this document's modifier table is **canonical** — the tables in `cards/audit-compliance/` are generated from it. See **v2.2 Playtest Edition Changes** at the bottom.

---

## Module Overview

The **Audit & Compliance Module** teaches players how security assessments reveal vulnerabilities that attackers will eventually exploit. Teams conduct a simulated third-party audit of their IT infrastructure, discovering gaps that will matter later.

**Key Concept:** "Auditors find what attackers will exploit." The findings from this module either inform hardening decisions (if successful) or create additional costs (if incident occurs).

**Module Teaches:**
- **Primary:** Security assessment, compliance frameworks (NIST, CIS, PCI-DSS), vulnerability discovery
- **Secondary:** Risk prioritization, remediation planning, audit-to-action translation

**Integration Point:**
- Can be played standalone (teams audit a pre-built network)
- OR as setup for Incident Response/Disaster Recovery (audit findings modify those modules)
- See [module-combinations.md](../module-combinations.md) for recommended sequences

---

## Module Setup (10 minutes)

### 1. Choose Assessment Framework

| Framework | Focus | Best For |
|-----------|-------|----------|
| **NIST Cybersecurity Framework** | 5 Core Functions | General organizations |
| **CIS Critical Controls** | 18 Controls (CIS v8) | Defense-focused |
| **PCI-DSS** | Payment card security | Retail/e-commerce |
| **HIPAA** | Healthcare data | Healthcare organizations |
| **Multi-Framework** | Mix of above | Realistic compliance |

**Key Point:** Framework choice determines which audit domains are tested.

**Budget note (v2.2):** core-rules gives the Audit module a starting Budget of 100 — **Budget (100) applies only when playing the optional Remediation follow-up cards** (see `cards/audit-compliance/expansion-deck/compliance-frameworks.md`, remediation section); **the assessment itself costs nothing.**

### 2. Choose Assessment Scope

| Scope | Time | Networks Evaluated |
|-------|------|-------------------|
| **Basic** | 5 min | One pre-built network |
| **Standard** | 10 min | One network from Network Building OR pre-built |
| **Comprehensive** | 15+ min | Multiple networks / multiple locations |

### 3. Network Input

**Option A: Use Pre-Built Network**
- Threat Orchestrator provides a sample network
- Teams audit it without having built it
- Focuses on audit skills, not network design

**Option B: Use Network from Network Building Module**
- Teams audit the network they just built
- Directly see consequences of earlier decisions
- More integrated experience

**Option C: Create Fictional Network via Narrative**
- Threat Orchestrator describes a scenario: "Your organization has email, web, database, and domain controller servers. Some are on-prem, some in cloud. You have a firewall but no IDS."
- Teams audit based on description
- Faster, requires less setup

---

## Gameplay Loop (10 minutes)

### Audit Structure

**Threat Orchestrator (Acting as External Auditor)** reviews the network and assesses **6 audit domains**:

### Domain 1: Network Segmentation & Isolation

**Audit Question:**
"Does your network properly isolate critical systems from untrusted networks?"

**Pass Criteria:**
- Implemented segmented architecture (3+ zones), AND
- Deployed firewall between zones, AND
- Critical systems (Database, Domain Controller) in separate zone from internet-facing systems

**Fail Criteria:**
- Flat network (no segmentation), OR
- Segmentation without firewall, OR
- Critical systems on same zone as untrusted systems

**If FAIL - Finding:**
- **Name:** Network Segmentation Gap
- **Risk Level:** CRITICAL
- **Consequence in IR:** Lateral movement easier (-1 to defending against NETWORK attacks)
- **Consequence in DR:** Attacker access spreads to more systems (-10 DR budget penalty)

**Narrative for Teams:**
"All of your systems are on the same network segment. Once an attacker gains access to one system, they can move freely between others."

---

### Domain 2: Access Control & Identity Management

**Audit Question:**
"Is your identity system (directory services, authentication, authorization) properly secured?"

**Pass Criteria:**
- Domain Controller deployed, AND
- Domain Controller on separate network segment, AND
- Domain Controller not overloaded (≤2 services)

**Fail Criteria:**
- No Domain Controller deployed, OR
- Domain Controller on same segment as untrusted systems, OR
- Domain Controller overloaded (3+ services)

**If FAIL - Finding:**
- **Name:** Identity System Vulnerability
- **Risk Level:** CRITICAL
- **Consequence in IR:** Credential-based attacks easier (-1 to defending against CREDENTIAL_ABUSE attacks)
- **Consequence in DR:** Full credential compromise; all user accounts compromised (-15 DR budget penalty)

**Narrative for Teams:**
"Your identity system is overloaded with too many services and insufficient hardening. If compromised, attackers will have broad access to all user credentials."

---

### Domain 3: Threat Detection & Incident Response

**Audit Question:**
"Can you detect attacks when they happen? Do you have monitoring and alerting?"

**Pass Criteria:**
- IDS or IPS deployed, AND/OR
- SIEM system deployed, AND/OR
- Email Gateway + Honeypot deployed (detection alternatives)

**Fail Criteria:**
- None of the above detection systems deployed, OR
- Only basic security devices with no central logging

**If FAIL - Finding:**
- **Name:** Detection & Monitoring Gap
- **Risk Level:** HIGH
- **Consequence in IR:** Investigations slower (-1 to Investigation rolls; 12+ instead of 11+)
- **Consequence in DR:** Breach undetected longer; more data stolen (-10 DR budget penalty)

**Narrative for Teams:**
"You have no centralized logging or monitoring. When an attack happens, you won't know about it until data is already compromised."

---

### Domain 4: Backup & Disaster Recovery

**Audit Question:**
"Do you have functional backups? Can you recover from data loss or ransomware?"

**Pass Criteria:**
- Backup System deployed, AND
- Backup isolated on separate network, OR
- Cloud backup configured, OR
- Multiple hosting locations (on-prem + cloud redundancy)

**Fail Criteria:**
- No Backup System deployed, OR
- Single point of failure (all on-prem or all cloud)

**If FAIL - Finding:**
- **Name:** Backup & Recovery Gap
- **Risk Level:** CRITICAL (for ransomware/DR only)
- **Consequence in IR:** None (network gap, not detection issue)
- **Consequence in DR:** Ransomware unrecoverable; full rebuild required (-25 DR budget penalty)

**Narrative for Teams:**
"You have no backup strategy. If ransomware hits, you cannot recover your data. You must either pay ransom or rebuild from scratch."

---

### Domain 5: Third-Party Risk & Cloud Security

**Audit Question:**
"Are your cloud systems and third-party integrations properly secured and isolated?"

**Pass Criteria:**
- Cloud systems isolated on private network (VPN), AND
- Cloud systems monitored/managed, AND
- Credentials for cloud access securely managed

**Fail Criteria:**
- Cloud systems internet-exposed, OR
- No monitoring of cloud services, OR
- Credentials stored locally for cloud access

**If FAIL - Finding:**
- **Name:** Cloud Security Gap
- **Risk Level:** HIGH
- **Consequence in IR:** Cloud-based attacks easier (-1 to defending against WEB_EXPLOIT attacks)
- **Consequence in DR:** Cloud compromise requires cloud provider recovery; slow remediation (-20 DR budget penalty)

**Narrative for Teams:**
"Your cloud systems are internet-accessible without protection. Any attacker can directly target your cloud infrastructure."

---

### Domain 6: Security Operations & Monitoring

**Audit Question:**
"Do you have centralized logging, monitoring, and security operations capability?"

**Pass Criteria:**
- SIEM system deployed, OR
- Email Gateway + IDS deployed (combined monitoring)

**Fail Criteria:**
- No SIEM or equivalent centralized logging

**If FAIL - Finding:**
- **Name:** Security Operations Gap
- **Risk Level:** MEDIUM
- **Consequence in IR:** Investigations slower (-1 to Investigation rolls)
- **Consequence in DR:** Forensic analysis slow; can't determine breach scope (-5 DR budget penalty)

**Narrative for Teams:**
"You have no centralized place to view security events. When an attack happens, investigators must pull data from multiple sources manually."

---

## Audit Report Generation

### Creating the Formal Findings Report

After all 6 domains are assessed, **Threat Orchestrator produces an Audit Findings Report**:

```
SECURITY AUDIT FINDINGS REPORT

Organization: [Name]
Assessment Date: [Date]
Framework: [Framework used]
Auditor: [Your name / External firm]

═══════════════════════════════════════════

DOMAIN ASSESSMENT SUMMARY:

✓ PASS - Network Segmentation & Isolation
  Observation: Network properly segmented with firewalls between zones.
  Assessment: Risk is LOW for lateral movement.

✗ FAIL - Access Control & Identity Management
  Finding: Domain Controller overloaded with excessive services.
  Risk: If DC compromised, entire identity system at risk.
  Severity: CRITICAL
  Recommendation: Isolate DC to minimal required services.

✓ PASS - Threat Detection & Incident Response
  Observation: SIEM system deployed with centralized logging.
  Assessment: Good detection capability.

✗ FAIL - Backup & Disaster Recovery
  Finding: No backup system deployed.
  Risk: Data loss unrecoverable; ransomware response limited to ransom/rebuild.
  Severity: CRITICAL
  Recommendation: Deploy backup system immediately.

✓ PASS - Third-Party Risk & Cloud Security
  Observation: Cloud systems properly isolated on private network.
  Assessment: Cloud security posture adequate.

✗ FAIL - Security Operations & Monitoring
  Finding: No centralized logging platform.
  Risk: Incident investigation will be slow and manual.
  Severity: HIGH
  Recommendation: Deploy SIEM or equivalent centralized logging.

═══════════════════════════════════════════

FINAL SCORE: 3/6 DOMAINS PASS

Overall Assessment: CONCERNING GAPS IDENTIFIED

Summary: Organization has adequate network and cloud security but lacks:
1. Proper identity system isolation
2. Backup/recovery capability
3. Centralized monitoring

Impact Estimate:
- If attack occurs: Detection delayed, recovery impossible without ransom
- Estimated cost to remediate findings: ~$40K (modest investment)
- Estimated cost of breach due to these gaps: ~$500K+ (significant exposure)

Recommendation Priority:
1. Deploy backup system (prevent ransomware catastrophe)
2. Isolate Domain Controller (prevent credential compromise)
3. Centralize logging (speed up incident response)
```

---

## Audit Scoring

### One Rubric (v2.2): PASS/FAIL is primary

**PASS/FAIL per domain (X/6) is the primary score.** Star ratings (1-5★) are flavor for narrative reports, with this fixed mapping:

> **1-2★ = FAIL · 3★+ = PASS · "PARTIAL" counts as FAIL**

**Optional (v2.2):** a 5★ (exemplary) rating in Detection grants +1 to Incident Response investigation rolls if IR is played later.

### Final Audit Score

Teams receive a score reflecting their infrastructure quality:

| Score | Assessment | Interpretation |
|-------|------------|-----------------|
| **6/6 PASS** | Enterprise-Grade | No modifiers carried into later modules; strong foundation |
| **5/6 PASS** | Strong Security | -1 modifier to one attack type in IR |
| **4/6 PASS** | Adequate Security | -1 modifier to two attack types in IR |
| **3/6 PASS** | Concerning Gaps | -1 modifier to three attack types; IR easier |
| **Below 3/6** | High Risk | Multiple -1 modifiers; IR much easier; DR much costlier |

### Narrative Interpretation

**6/6 Pass:**
"Your organization demonstrates strong security practices across all domains. While no system is perfect, you have implemented key controls and best practices."

**4-5/6 Pass:**
"Your organization has good foundational security but should prioritize remediation of identified gaps. Most critical systems are protected, but some exposure remains."

**3/6 Pass:**
"Your organization has significant security gaps that create real risk. Multiple critical domains require attention. If an incident occurs, you will face challenges."

**Below 3/6:**
"Your organization has critical gaps across multiple domains. Significant investment needed to meet baseline security standards."

---

## Audit Findings as Attack Modifiers

### How Audit Failures Affect Other Modules

**When audit findings exist and other modules are played:**

#### In Incident Response Module:

Each FAIL finding creates a **-1 modifier** (one per gap — canonical, v2.2) to the relevant roll:

| Audit Finding | IR Modifier | Affected Threat Type |
|---------------|------------|----------------------|
| **Segmentation Gap** | -1 to NETWORK defenses | Lateral movement attacks easier |
| **Identity Gap** | -1 to CREDENTIAL_ABUSE defenses | Credential attacks easier |
| **Detection Gap** | -1 to Investigation rolls | Finding threats takes longer (11+ becomes 12+) |
| **Backup Gap** | No IR effect | (Matters in Disaster Recovery) |
| **Cloud Gap** | -1 to WEB_EXPLOIT defenses | Web/API attacks easier |
| **Operations Gap** | -1 to Investigation rolls | Forensic investigation slower |

**Example: Segmentation Gap Active in IR**

```
INCIDENT RESPONSE PHASE:

Team's Threat: Lateral Movement via SMB
Base roll needed: 11+
Audit Modifier: -1 (Segmentation Gap)
Effective roll needed: 12+

Team's Defense: Network Segmentation (newly deployed)
Roll: 14 + 2 (justification) = 16
Result: SUCCESS (16 ≥ 12)

TO Narrative: "Your network segmentation worked perfectly, stopping the
lateral movement that would have been trivial in an unsegmented network."
```

#### In Disaster Recovery Module:

Each FAIL finding is a penalty subtracted from the DR starting budget (this table is **canonical** — v2.2):

| Audit Finding | DR Budget Penalty |
|---------------|-------------------|
| **Segmentation Gap** | -10 Budget (attacker spreads to more systems) |
| **Identity Gap** | -15 Budget (full credential compromise) |
| **Detection Gap** | -10 Budget (dwell time longer; more data stolen) |
| **Backup Gap** | -25 Budget (no recovery option; expensive rebuild) |
| **Cloud Gap** | -20 Budget (cloud provider recovery needed) |
| **Operations Gap** | -5 Budget (forensic investigation slow) |

**Cap (v2.2):** the total gap penalty applied to a subsequent module's budget is **capped at -30**.

**Example: Multiple Gaps in DR (v2.2)**

```
DISASTER RECOVERY PHASE:

Teams start with 50 crisis budget (DR 50; for reference, IR starts at 100).

Audit Failures from earlier assessment:
- Segmentation Gap: -10
- Detection Gap: -10
- Backup Gap: -25

Raw Gap Penalty: -45 -> capped at -30

Available Crisis Budget: 50 - 30 = 20

With 20 Budget the team can still afford the mandatory beats
(cheapest mandatory path is 29 -> they must lean on the free
Holding Statement and skip actions), but the response will be
thin. Outcome: heavy pressure, likely reputation damage.
```

---

## Integration with Other Modules

### Audit as Setup for Incident Response

**Recommended Flow: Audit → Incident Response**

1. **Conduct Audit** (10 minutes)
   - Identify 3-5 gaps in network

2. **Generate Modifiers** (2 minutes)
   - Each gap becomes a -1 modifier to relevant defense in IR

3. **Play Incident Response** (35-40 minutes)
   - Teams discover that audit findings predicted attack vectors
   - Audit gaps make IR harder
   - Teams gain appreciation for audit value

4. **Debrief** (10 minutes)
   - Discuss how audit findings manifested as attack vectors
   - Real-world connection to breach investigations

### Audit as Setup for Disaster Recovery

**Recommended Flow: Audit → [Incident Response] → Disaster Recovery**

1. **Conduct Audit** (10 minutes)
   - Identify gaps (particularly Backup Gap and Detection Gap)

2. **Skip or Lose IR** (optional)
   - Assume attackers breached and incident was NOT detected

3. **Play Disaster Recovery** (30-35 minutes)
   - Each audit gap increases crisis costs
   - Teams discover backup gap = ransomware unrecoverable
   - Teams discover detection gap = dwell time was 48+ hours

4. **Debrief** (10 minutes)
   - Discuss financial impact of audit failures
   - Calculate total incident cost

### Audit as Learning Tool (Standalone)

**Play Just the Audit Module** (as independent learning)

- Teams audit a provided network
- Discuss what each finding means
- Plan hypothetical remediation
- Estimate costs and timeline

---

## Tips for Threat Orchestrators

### Before the Audit

1. **Choose framework** - NIST/CIS/PCI-DSS based on organization/industry
2. **Select network** - Pre-built OR from Network Building OR fictional
3. **Prepare assessment checklist** - Know pass/fail criteria for each domain
4. **Have findings report template** - For consistent, professional output

### During the Audit

1. **Walk through systematically** - Each domain, one at a time
2. **Explain reasoning** - "You passed segmentation because you have firewalls between zones"
3. **Use NIST/CIS language** - Frame findings in recognized compliance framework
4. **Be fair** - Audit findings should be accurate, not arbitrary
5. **Take notes** - Document what you see for the formal report

### After the Audit

1. **Create findings report** - Professional document teams can reference
2. **Calculate score** - X/6 domains pass
3. **Identify modifiers** - Which audit gaps will affect Incident Response
4. **Estimate remediation costs** - Budget and timeline to fix findings
5. **Explain real-world connections** - Compare audit process to actual assessments (SOC 2, ISO 27001, etc.)

---

## Sample Scenarios

### Scenario 1: "Startup Audit" (Beginner)

**Network Characteristics:**
- Flat network (no segmentation)
- Email, web, database on same servers (overloaded)
- No backup system
- No SIEM or monitoring
- All on-premises

**Expected Audit Result:**
- 1-2/6 domains pass
- Multiple CRITICAL findings
- High remediation cost
- Team learns value of basics (backup, monitoring)

---

### Scenario 2: "Mid-Market Audit" (Intermediate)

**Network Characteristics:**
- Segmented network with firewall
- Dedicated servers for critical functions
- Backup system present
- IDS deployed but no SIEM
- Hybrid on-prem/cloud

**Expected Audit Result:**
- 4/6 domains pass
- 2 MEDIUM findings (monitoring, cloud config)
- Moderate remediation cost
- Team learns importance of comprehensive monitoring

---

### Scenario 3: "Enterprise Audit" (Advanced)

**Network Characteristics:**
- Fully isolated network architecture
- Dedicated hardened servers
- Comprehensive backup strategy
- SIEM + IDS deployed
- Cloud properly secured

**Expected Audit Result:**
- 5-6/6 domains pass
- 0-1 minor findings
- Low remediation cost
- Team learns value of comprehensive program

---

## Extensions & Variations

### Variation 1: Regulatory Compliance Specific

Focus audit on specific compliance requirement:
- **PCI-DSS:** Focus on payment card handling, encryption, access control
- **HIPAA:** Focus on healthcare data protection, audit logs, access management
- **SOC 2:** Focus on security, availability, confidentiality controls
- **GDPR:** Focus on data protection, breach notification, privacy

Each framework has different pass/fail criteria.

---

### Variation 2: Continuous Auditing

Run audit multiple times with team improvements:
1. Initial audit (baseline)
2. Team makes improvements based on findings
3. Follow-up audit (measure improvement)
4. Calculate improvement % and cost-benefit

---

### Variation 3: Threat Model Audit

Instead of compliance framework, audit against specific threat profile:
- "This organization faces nation-state threat" → Audit for advanced detection
- "This organization handles PHI data" → Audit for healthcare security
- "This organization processes credit cards" → Audit for PCI-DSS
- "This organization is critical infrastructure" → Audit for resilience

---

## Quick Reference: Audit Domains & Consequences (canonical, v2.2)

| Domain | PASS Meaning | FAIL Consequence (IR) | FAIL Consequence (DR) |
|--------|------------|----------------------|-----------------------|
| **Segmentation** | Good isolation | -1 to NETWORK defense | -10 budget |
| **Identity** | Proper AC | -1 to CREDENTIAL_ABUSE defense | -15 budget |
| **Detection** | Good monitoring | -1 to Investigation | -10 budget |
| **Backup** | Recovery capable | None | -25 budget |
| **Cloud** | Secure cloud | -1 to WEB_EXPLOIT defense | -20 budget |
| **Operations** | Good logging | -1 to Investigation | -5 budget |

**Cap (v2.2):** total DR budget penalty capped at **-30**. Star flavor mapping: 1-2★ = FAIL, 3★+ = PASS, PARTIAL = FAIL.

---

## Need Help?

- **Questions about universal rules?** See [Core Rules](core-rules.md)
- **Want to combine modules?** See [Module Combinations](../module-combinations.md)
- **How does this integrate with Incident Response?** See [module-incident-response.md](module-incident-response.md)
- **How does this integrate with Network Building?** See [module-network-building.md](module-network-building.md)
- **Standalone play guide?** See [Standalone Play Guide](../standalone-games/audit-compliance.md)

---

## v2.2 Playtest Edition Changes

1. **One canonical modifier table.** This document's table is authoritative: DR budget penalties Segmentation -10 / Identity -15 / Detection -10 / Backup -25 / Cloud -20 / Ops -5, and one -1 IR modifier per gap. The tables in `cards/audit-compliance/core-deck/audit-domain-cards.md` and `cards/audit-compliance/README.md` are regenerated from it. One-off mechanics that existed nowhere else ("+5 turn penalty", "+1 escalation point", "-2 modifier", "+1 difficulty") are deleted or folded into the canonical -1-per-gap rule.
2. **Cap added:** the total gap penalty applied to a subsequent module's budget is capped at **-30**. The unexplained "from 120 to 190" example was replaced with real budgets (DR 50, IR 100).
3. **One scoring rubric:** PASS/FAIL per domain (X/6) is primary. Stars are flavor with a fixed mapping — 1-2★ = FAIL, 3★+ = PASS, "PARTIAL" counts as FAIL — printed here, on the domain cards, and in the standalone guide. Optional: 5★ in Detection grants +1 to IR investigation rolls if IR is played later.
4. **Budget note:** the module's core-rules Budget (100) applies only to the optional Remediation follow-up cards; the assessment itself costs nothing.
5. **Fact corrections:** CIS "20 Core Controls" → 18 (CIS v8) everywhere; NIST CSF category codes corrected in the expansion deck (Protect = PR.AC/PR.AT/PR.DS/PR.IP/PR.MA/PR.PT; Respond = RS.RP/RS.CO/RS.AN/RS.MI/RS.IM); segmentation cites PR.AC-5; vendor risk cites ID.SC; incident response is CIS Control 17 (v8).
6. **Card counts corrected:** expansion deck is 19 cards (11 framework + 8 remediation); CIS section is 3 cards; HIPAA/SOC 2 moved to "Planned".
7. **Play aids:** scoring reference card, audit worksheet, and judge guide are moving to the print pack (coming); an inline text audit worksheet is included in the standalone guide so it is playable today.

---

*Audit & Compliance Module - Rules & Mechanics*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.2 - Playtest Edition*
