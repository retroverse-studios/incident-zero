# Network Building Module: Legacy Systems (Expansion)

**Version:** 2.1 - Balanced & Refined Edition
**Last Updated:** October 2025

---

## Overview

**Legacy System Cards** extend the Network Building module with specialized systems that many organizations still operate but cannot easily patch or upgrade.

- **Total Cards:** 4 (LEGACY-01 to LEGACY-04)
- **Used In:** Network Building expansion (adds complexity and challenge)
- **Assumption:** Legacy systems cannot be patched or upgraded due to vendor EOL (End of Life) or critical business dependency
- **Design Philosophy:** Cannot defend legacy system itself; must isolate and defend around it

---

## Legacy System Cards

### LEGACY-01: Mainframe System
**Type:** Legacy Business-Critical Infrastructure
**Cost:** 15 Budget (expensive to operate)
**Complexity:** 4/4 (extremely complex, specialized expertise required)
**Availability Requirement:** 99.95% (financial/mission-critical)
**Supported Operating System:** Mainframe OS (z/OS, VSE, VM), Not patchable

**Description:**
Large centralized mainframe computer running business-critical applications. Banks, insurance companies, government agencies, and utilities often depend on mainframes for core operations. Mainframes are designed for availability and stability, but security model is outdated (predates internet security concerns).

**Key Characteristics:**
- **Age:** Often 20-30+ years old
- **Software:** Custom applications written in COBOL or other legacy languages
- **Security:** Perimeter security model (assume all internal traffic is trusted)
- **Expertise:** Few experts remain (knowledge leaving the industry)
- **Vendor Support:** Vendor may no longer exist; in-house expertise critical
- **Cost of Replacement:** $5M-100M+ (impossible to replace)

**Key Concerns:**
- No regular security patches available (vendor EOL)
- Known CVEs published but cannot be patched
- Legacy protocols (unencrypted connections, weak authentication)
- Access control systems predate modern security standards
- Directly connected to corporate network (not isolated)
- Often contains entire organization's critical data
- Business process depends on it (replacement would take years)

**Defense Strategy (Cannot Fix, Must Isolate):**
- **Network Isolation:** Mainframe in restricted segment, minimal connectivity
- **Firewall Rules:** Only authorized systems can connect to specific ports
- **Monitoring:** SIEM must monitor all mainframe connections (detect anomalies)
- **Assumption of Breach:** Assume mainframe will be compromised; defend everything else
- **No Direct User Access:** Users should not directly access mainframe (access via secure application tier)
- **Log Aggregation:** All mainframe activities logged centrally (immutable audit trail)

**Network Interactions:**
- **Requires:** Firewall rules isolating mainframe
- **Requires:** Network Segmentation to restrict access
- **Requires:** SIEM monitoring for anomaly detection
- **Incompatible with:** Direct internet access (perimeter firewall only)
- **Incompatible with:** Cloud integration (data residency and connectivity issues)

**Incident Response Impact:**
- If mainframe is compromised, entire organization may be compromised
- Mainframe compromise may be immediate game-loss in Incident Response
- Legacy authentication means attacker can move freely once inside
- Mainframe contains sufficient data to be primary exfiltration target

**Team Design Validation:**
- ✓ If including mainframe: must include Network Segmentation + Firewall
- ✓ Must include SIEM for monitoring
- ✗ Failure: Direct user access to mainframe increases risk
- ✗ Failure: Cloud connectivity to mainframe violates security boundary

---

### LEGACY-02: Custom Business Application
**Type:** Legacy Business-Critical Software
**Cost:** 8 Budget (application licensing/support)
**Complexity:** 3/4 (difficult to update or replace)
**Availability Requirement:** 99% (business depends on it)
**Operating System:** Windows Server 2008/2012, or older Linux, or proprietary OS

**Description:**
Specialized business application written by external vendor or in-house team that is no longer maintained. Application may be:
- Accounting system (custom financial software)
- Manufacturing control system (production scheduling)
- Insurance claims system
- Legal case management system
- ERP (Enterprise Resource Planning) system

The application is mission-critical but:
- Vendor no longer provides updates (company went out of business, or stopped supporting)
- Cost to replace: $500K-$5M+ (economically infeasible)
- Business process deeply embedded in application (replacement would require major restructuring)
- Knowledge of application is scarce (original developers left, documentation poor)

**Key Characteristics:**
- **Age:** Often 10-20 years old
- **Language:** Written in outdated languages (Visual Basic 6, old Java, COBOL)
- **Vendor:** Vendor may no longer exist; purchased "as-is"
- **Customization:** Heavily customized for organization (not standard product)
- **Expertise:** Few people understand the code
- **Database:** Proprietary or very old database (SQL Server 2005, Oracle 10g, etc.)
- **Integration:** Deeply integrated into business workflow

**Key Concerns:**
- Application may contain hardcoded credentials
- Application may store passwords in plaintext
- Application may use unencrypted connections to database
- Application may have SQL injection vulnerabilities (pre-2005 development)
- Application may lack audit logging
- Upgrading operating system may break application
- Patches to operating system may be incompatible with application
- Security testing tools may break application

**Defense Strategy (Isolate and Monitor):**
- **Application Server Isolation:** Application in restricted segment
- **Database Isolation:** Application database encrypted and access-controlled
- **Network Firewall:** Only users/systems needing application can access it
- **No Direct Internet Access:** Application never exposed to internet
- **SIEM Monitoring:** All application access logged and monitored
- **Assumption:** Assume application has SQL injection or similar vulnerabilities; defend database
- **Access Control:** Limit who can use application (risk vs. benefit analysis)

**Network Interactions:**
- **Requires:** Application Server (SRV-06 or custom server)
- **Requires:** Database Server isolated from other systems
- **Requires:** Firewall rules limiting access
- **Requires:** SIEM monitoring application access
- **Incompatible with:** Cloud hosting (licensing, data residency issues)

**Incident Response Impact:**
- Custom application vulnerability could be exploited for lateral movement
- Application database compromise exposes sensitive business data
- Application logs may be missing or inaccessible
- Attacker may extract application source code

**Team Design Validation:**
- ✓ If including custom application: must isolate application + database
- ✓ Must limit user access (principle of least privilege)
- ✓ Must monitor application access in SIEM
- ✗ Failure: Direct internet access to application increases attack surface
- ✗ Failure: Weak access controls allow unauthorized application access

---

### LEGACY-03: Industrial Control System (ICS)
**Type:** Operational Technology (OT) / Safety-Critical
**Cost:** 12 Budget (specialized equipment)
**Complexity:** 4/4 (extremely specialized, safety implications)
**Availability Requirement:** 99.9%+ (safety-critical, cannot fail)
**Operating System:** Proprietary Industrial OS, real-time OS, or very old Linux

**Description:**
Specialized system that controls physical machinery, manufacturing processes, power generation, utilities, or other critical infrastructure. Examples:
- Manufacturing: Assembly line control, robotic systems
- Utilities: Power distribution, water treatment, smart grid
- Building Systems: HVAC, access control, fire systems
- Transportation: Traffic signals, rail systems

Industrial Control Systems (ICS) are purpose-built for reliability and real-time control, not information security. They predate cybersecurity concerns.

**Key Characteristics:**
- **Purpose:** Controls physical machinery or critical infrastructure
- **Real-time:** Must respond in milliseconds (cannot tolerate latency)
- **Reliability:** Designed for 99.99%+ availability
- **Security:** Predates modern security (no authentication, no encryption)
- **Isolation:** Historically air-gapped (not connected to corporate network)
- **Expertise:** Requires specialized engineering expertise (electrical, mechanical, control systems)
- **Cost of Downtime:** $10K-$1M+ per minute of downtime
- **Lifecycle:** 10-30 year lifespan (different than IT systems)

**Key Concerns (from IT Perspective):**
- Cannot be patched (real-time systems cannot tolerate OS updates)
- Cannot tolerate intrusion detection (latency would affect operations)
- Cannot install EDR/antivirus (would slow down real-time responses)
- Cannot use modern encryption (adds latency)
- Uses legacy protocols (Modbus, Profibus, DNP3 - no security built-in)
- Often air-gapped; now being connected to corporate network (exposes vulnerability)
- If compromised, physical safety implications (machinery malfunction, power outage, etc.)

**Key Concerns (from ICS Perspective):**
- Availability is paramount (security is secondary)
- Adding security controls might affect uptime
- ICS engineers don't understand IT security
- IT security tools and practices may break ICS
- ICS changes must be tested extensively (downtime is unacceptable)

**Defense Strategy (Strict Isolation):**
- **Never Connect to Corporate Network:** ICS should remain air-gapped
- **If Connection Required:** Use unidirectional gateway (ICS can send data out, nothing comes in)
- **Network Segmentation:** ICS in completely isolated segment from corporate systems
- **No User Internet Access from ICS:** ICS workstations cannot browse internet
- **Physical Security:** ICS room locked, access restricted to authorized engineers
- **Monitoring:** Use ICS-specific monitoring tools (not traditional SIEM)
- **Assumption:** Assume ICS network will be compromised; focus on preventing spread to corporate

**Network Interactions:**
- **Isolation:** Complete separation from corporate network (air-gapped preferred)
- **If Bridge Required:** Unidirectional gateway (one-way data flow)
- **Incompatible with:** Corporate firewall (ICS cannot tolerate intrusion detection latency)
- **Incompatible with:** EDR/Antivirus (would slow down real-time control)
- **Incompatible with:** Cloud integration (real-time latency requirements)

**Incident Response Impact:**
- ICS compromise may cause physical safety issues (priority = physical safety over data)
- ICS compromise may cause production shutdown (significant financial impact)
- ICS security investigation requires specialized expertise (not standard IT)
- ICS forensics may disrupt operations (cannot preserve evidence if it affects safety)

**Team Design Validation:**
- ✓ If including ICS: must isolate ICS from corporate network
- ✓ Must use unidirectional gateway if connectivity required
- ✓ Must NOT install traditional IT security tools on ICS
- ✗ Failure: Corporate network connected to ICS without isolation
- ✗ Failure: ICS exposed to internet or untrusted networks
- ✗ Failure: IT security tools degrading ICS real-time performance

---

### LEGACY-04: Obsolete Operating System
**Type:** Legacy Infrastructure Running Unsupported OS
**Cost:** 5 Budget (cheap hardware, but difficult to support)
**Complexity:** 3/4 (difficult to manage with modern security tools)
**Availability Requirement:** 80-95% (business can tolerate occasional downtime)
**Operating System Examples:** Windows XP, Windows Server 2003, old Linux kernels, custom UNIX variants

**Description:**
Systems running operating systems that are no longer supported by vendor or open-source community. Vendor has stopped releasing security patches. Public exploit code for known vulnerabilities exists and is freely available.

**Examples:**
- Windows XP (support ended 2014)
- Windows Server 2003 (support ended 2015)
- Linux 2.4/2.6 kernels (EOL for 10+ years)
- Solaris 8/9 (Sun Microsystems EOL)
- Other commercial UNIX variants EOL decades ago

**Key Characteristics:**
- **Support:** No security patches from vendor
- **Exploits:** All known vulnerabilities are published (no zero-days)
- **Tools:** Modern security tools often don't run on EOL OS
- **Compatibility:** Cannot run modern applications
- **Patching OS:** OS upgrade would break dependent applications
- **Cost of Replacement:** Application replacement cost makes OS upgrade prohibitive

**Key Concerns:**
- All known vulnerabilities can be exploited (no patches)
- Public exploits readily available (trivial for attacker)
- Modern malware often targets these systems (profitable attacks)
- Ransomware frequently targets EOL systems (known vulnerabilities)
- System cannot run modern antivirus/EDR (not compatible)
- System cannot use modern encryption protocols
- System is prone to exploitation for lateral movement into modern systems

**Defense Strategy (Assume Compromise, Isolate):**
- **Assumption:** Assume EOL system will be compromised (all vulnerabilities are public)
- **Network Isolation:** EOL system in restricted segment, minimal connectivity
- **Firewall Rules:** Only necessary traffic to/from EOL system
- **No Lateral Movement:** Firewall rules prevent movement from EOL system to others
- **No Sensitive Data:** Do not store sensitive data on EOL system
- **Monitoring:** SIEM monitors EOL system closely (detect compromise signs)
- **Replacement Planning:** Have timeline to replace/upgrade EOL system
- **Physical Security:** Restrict physical access to EOL system

**Network Interactions:**
- **Isolation:** EOL system in isolated segment
- **Firewall:** Strict firewall rules (default deny)
- **Monitoring:** SIEM alerts on any unusual EOL system activity
- **No Cloud Access:** EOL system does not connect to cloud systems
- **Air-gapped Preferred:** If possible, keep EOL system air-gapped

**Incident Response Impact:**
- EOL system compromise may be inevitable (all vulnerabilities public)
- Attacker will target EOL system as entry point (easier than hardened systems)
- EOL system may be used as staging point for attacks on hardened systems
- Forensics on EOL system may be difficult (no modern forensics tools support it)

**Team Design Validation:**
- ✓ If including EOL system: must isolate completely
- ✓ Must have replacement timeline
- ✓ Must NOT store sensitive data on EOL system
- ✗ Failure: No network isolation for EOL system
- ✗ Failure: Sensitive data on EOL system
- ✗ Failure: EOL system has same network privileges as modern systems

---

## Legacy Systems Card Summary

| Card | System Type | Cost | Complexity | Key Challenge |
|------|------------|------|-----------|--------------|
| LEGACY-01 | Mainframe | 15 | 4/4 | Cannot patch, mission-critical |
| LEGACY-02 | Custom Application | 8 | 3/4 | Vendor no longer exists |
| LEGACY-03 | Industrial Control | 12 | 4/4 | Real-time + safety-critical |
| LEGACY-04 | Obsolete OS | 5 | 3/4 | All vulnerabilities public |

---

## Design Philosophy

**Key Principle: Cannot Fix, Must Isolate**

Legacy systems cannot be fixed through normal security controls:
- Cannot patch (vendor no longer supports)
- Cannot upgrade OS (breaks dependent applications)
- Cannot install modern security tools (incompatible)
- Cannot redesign (cost prohibitive)

Instead, organizations must:
1. **Isolate the legacy system:** Separate network segment, strict firewall rules
2. **Monitor closely:** SIEM alerts on any anomalous activity
3. **Assume compromise:** Design defenses assuming legacy system will be compromised
4. **Plan replacement:** Have timeline to eventually replace legacy system
5. **Limit exposure:** Do not connect sensitive systems to legacy system network

---

## Gameplay Impact

### Network Design Complexity
Including legacy systems significantly increases network design complexity:
- Must add firewall rules for each legacy system
- Must add network segmentation
- Must add SIEM monitoring
- Budget is constrained (legacy systems are expensive to operate)

### Incident Response Complications
If Incident Response follows Network Building:
- Legacy systems are easier attack targets (known vulnerabilities)
- Attacker will likely compromise legacy system first
- Legacy system compromise may lead to lateral movement
- Legacy system may lack proper logging (forensics is difficult)

### Strategic Trade-off
Teams face strategic decision: Include legacy systems or avoid them?
- **Include Legacy Systems:** Realistic, mirrors real organizations, adds challenge
- **Avoid Legacy Systems:** Simpler network design, but unrealistic
- **Team Decision:** Should reflect organization's actual legacy system situation

---

## When to Use Legacy System Cards

### Use in Network Building Expansion if:
- Playing with experienced teams
- Want realistic organizational network design
- Want to teach legacy system security challenges
- Want to increase network design complexity

### Skip Legacy System Cards if:
- Playing with beginners (too much complexity)
- Want to focus on modern security practices
- Want shorter, simpler network design phase
- Limited play time (legacy systems add design time)

---

## Print Instructions

1. Print on cardstock (250 gsm minimum)
2. Use color scheme indicating "difficult/expensive":
   - **Dark Red/Brown (Difficult):** LEGACY-01, LEGACY-03
   - **Orange (Moderate):** LEGACY-02, LEGACY-04
3. Include warning icons (exclamation mark, caution symbol) on cards
4. Cut along dotted lines
5. Create a "Legacy System Reference Card" with isolation requirements and key facts

---

## Possible Future Expansions

**Additional Legacy System Cards:**
- LEGACY-05: Mainframe Tape Backup System (disaster recovery, retention archiving)
- LEGACY-06: Proprietary Database System (custom data storage, vendor extinct)
- LEGACY-07: Dedicated PBX Telephony System (VoIP not yet viable)
- LEGACY-08: Custom SCADA System (industrial automation, not standard ICS)

---

*Network Building Module: Legacy Systems (Expansion)*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.1 - Balanced & Refined Edition*
