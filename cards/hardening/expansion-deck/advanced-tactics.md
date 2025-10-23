# Hardening Module: Advanced Pentester Tactics (Expansion)

**Version:** 2.1 - Balanced & Refined Edition
**Last Updated:** October 2025

---

## Overview

**Advanced Pentester Tactic Cards** extend the core Hardening module with 8 sophisticated attack scenarios for experienced players and complex threat environments.

- **Total Cards:** 8 (PT-09 to PT-16)
- **Difficulty Range:** ADVANCED to EXPERT+
- **Best For:** Experienced teams, advanced threat scenarios, specialized environments
- **Prerequisite:** Familiarity with core Pentester Tactics (PT-01 to PT-08)

---

## Advanced Pentester Tactics

### PT-09: Multi-Vector Attack - Coordinated Campaign
**Tactic Type:** Advanced Persistence / Multi-Stage
**Target Vectors:** MALWARE, CREDENTIAL_ABUSE, NETWORK, DATA_EXFIL
**Difficulty:** ADVANCED (defeat DC 14)

**Description:**
A pentester orchestrates a coordinated multi-vector attack that combines multiple tactics simultaneously: social engineering + malware + lateral movement + data exfiltration. Each phase is dependent on the previous one, and success in one area opens opportunities in others. Can your defenses coordinate to stop the full attack chain?

**Attack Details:**
- Phase 1: Phishing delivers initial malware
- Phase 2: Malware establishes persistence
- Phase 3: Lateral movement to file server
- Phase 4: Credential harvesting and exfiltration
- Targets: Defense coordination, integrated threat response
- Blue Team must roll separately for EACH phase

**Defending Defenses:**
- **Phase 1 (Social Engineering):** D-02 (+2), D-23 (+2) reduce success by +2 on this roll
- **Phase 2 (Malware):** D-06 (+1), D-08 (+3), D-13 (+2), D-17 (+2) for this phase
- **Phase 3 (Lateral Movement):** D-04 (+1), D-09 (+3), D-10 (+2), D-15 (+2) for this phase
- **Phase 4 (Data Exfil):** D-11 (+4), D-22 (+2), D-24 (+1) for this phase
- **Synergy Bonus:** If Blue Team deployed defenses covering all 4 vectors, +1 additional bonus to final roll

**Outcome:**
- **Blue Team Succeeds (DC 14 on FINAL phase roll):** Comprehensive defense stops the attack chain
- **Blue Team Fails ANY phase:** Attack progresses; Blue Team loses 1d4 security score points per failed phase and must deploy emergency response

**Teaching Point:** Modern attacks are sophisticated and multi-faceted. No single defense can stop them. Comprehensive defense-in-depth with coordinated response is essential. Defense teams must practice responding to coordinated attacks.

---

### PT-10: Zero-Day Exploitation - Unknown Vulnerability
**Tactic Type:** Initial Access / Execution
**Target Vectors:** MALWARE, WEB_EXPLOIT
**Difficulty:** ADVANCED (defeat DC 15)

**Description:**
A pentester exploits a previously unknown vulnerability (zero-day) in a critical business application. Traditional defenses (patching, signature-based detection, vulnerability scanning) cannot help because the vulnerability isn't public. Only behavioral detection or proactive hunting can identify this attack. Can your advanced monitoring catch what signature-based tools cannot?

**Attack Details:**
- Targets: Signature-based defenses, unknown vulnerability management
- Attack Vector: Unpatched but pristine application
- Success indicates: Blind spots in behavioral detection
- Blue Team rolls 1d20 to detect before exploitation succeeds

**Defending Defenses:**
- **D-03 (Patching):** +0 bonus (zero-day by definition isn't in patches)
- **D-06 (Antivirus):** +0 bonus (signatures don't exist for zero-day)
- **D-08 (EDR):** +3 bonus (behavioral analytics detect anomalous post-exploitation)
- **D-13 (Threat Hunting):** +3 bonus (proactive hunting finds zero-day activity)
- **D-17 (Sandbox):** +2 bonus (detonates malicious payloads in sandbox before deployment)
- **D-18 (IPS):** +1 bonus only (cannot stop unknown exploits)
- **D-21 (Container Security):** +2 bonus (isolates exploited application)

**Outcome:**
- **Blue Team Succeeds (14+):** EDR or threat hunting detects post-exploitation activity before damage
- **Blue Team Fails:** Zero-day achieves initial access; Blue Team suffers -1 penalty to all rolls for remainder of game (blind spot in defenses)

**Special Rule:** If Blue Team has NOT deployed at least 2 of {D-08, D-13, D-17}, they cannot succeed at this challenge (add clause: "You must have behavioral detection to stop unknown exploits").

**Teaching Point:** Signature-based defenses have inherent limitations. Behavioral detection and threat hunting are essential for detecting novel attacks. Zero-day preparedness requires assumption-of-breach mindset.

---

### PT-11: Ransomware Deployment & Encryption
**Tactic Type:** Impact / Extortion
**Target Vectors:** MALWARE, DATA_EXFIL, NETWORK
**Difficulty:** ADVANCED (defeat DC 15)

**Description:**
A pentester deploys ransomware that encrypts critical business data and demands payment for decryption keys. The attack combines malware execution, persistence, and data exfiltration (to threaten public disclosure if ransom not paid). This is the culmination of a successful attack chain. Can your defenses prevent data encryption, and can your backup strategy save you?

**Attack Details:**
- Targets: Data availability, backup resilience, recovery procedures
- Success indicates: Lack of backup redundancy or immutable backup protection
- Blue Team rolls 1d20 to either: (A) prevent ransomware deployment, OR (B) recover from backup

**Defending Defenses:**
- **Option A: Prevent Deployment**
  - D-08 (EDR): +3 bonus (detects ransomware execution)
  - D-13 (Threat Hunting): +2 bonus (proactive hunting finds ransomware)
  - D-14 (Memory Forensics): +1 bonus (detects encryption process)
  - D-17 (Sandbox): +2 bonus (detonates before reaching production)
  - D-21 (Container Security): +2 bonus (prevents spread in containerized environments)

- **Option B: Recover from Backup (if prevention fails)**
  - D-19 (Backup & Disaster Recovery): +4 bonus (3-2-1 backup strategy enables recovery)
  - D-21 (Container Security): +1 bonus (containerized backups easier to restore)
  - DC becomes 12 (easier to recover than prevent)

**Outcome:**
- **Blue Team Succeeds (13+):** Ransomware prevented or successfully recovered from backup
- **Blue Team Fails:** Data encrypted; immediate loss of 25% of remaining Budget, and all data-dependent operations suffer -2 penalty for remainder of game

**Special Rule - Immutable Backup Check:** If Blue Team deployed D-19, they also need verification that backups are immutable and tested. If backup testing procedures weren't mentioned in D-19 deployment, the bonus only applies if they roll 15+.

**Teaching Point:** Ransomware is now the #1 cybersecurity threat. Prevention through detection is important, but backup resilience is the ultimate defense. Immutable backups that survive ransomware attacks are essential business continuity strategy. Regular restore testing is critical.

---

### PT-12: APT Campaign - Multi-Turn Persistent Threat
**Tactic Type:** Advanced Persistent Threat / Long-term Compromise
**Target Vectors:** CREDENTIAL_ABUSE, MALWARE, NETWORK, DATA_EXFIL
**Difficulty:** EXPERT (defeat DC 16)

**Description:**
A pentester simulates an Advanced Persistent Threat (APT) campaign that maintains presence across multiple turns. Each turn, the APT performs new reconnaissance, persistence, lateral movement, or data exfiltration activities. The Blue Team must detect and eradicate the APT before it achieves critical objectives. This is a multi-turn challenge that escalates difficulty.

**Attack Details:**
- Multi-turn challenge (lasts 2-3 turns of main game)
- Targets: Long-term detection, threat hunting, incident response procedures
- Each turn the APT performs an action; Blue Team must detect and respond
- If APT achieves 3 objectives (e.g., 3 successful data exfils), game is lost

**Turn-by-Turn APT Actions:**
- **Turn 1:** Reconnaissance (scan network, enumerate users, identify critical assets)
- **Turn 2:** Lateral movement (move to file server, domain controller)
- **Turn 3:** Persistence establishment (add backdoor, create hidden user account)
- **Turn 4 (if still active):** Data exfiltration (steal customer database)
- **Turn 5+ (if still active):** Destruction phase (delete logs, trigger ransomware)

**Defending Against APT:**

Each turn, Blue Team must roll 1d20 to detect the APT activity:

- **Detection Phase:**
  - D-05 (Log Centralization): +1 bonus (detects suspicious activity in centralized logs)
  - D-10 (SIEM Correlation): +2 bonus (correlates multi-step APT behavior)
  - D-13 (Threat Hunting): +3 bonus (proactive hunting finds APT indicators)
  - D-22 (SIEM Enterprise): +3 bonus (advanced correlation detects APT patterns)
  - D-23 (IR Playbooks): +1 bonus (clear detection procedures in playbooks)
  - D-24 (Threat Intelligence): +2 bonus (known APT indicators in threat feeds)

- **Eradication Phase (if detected):**
  - D-09 (Network Segmentation): +1 bonus (isolates compromised systems)
  - D-15 (Honeypots): +2 bonus (APT triggers honeypot canaries)
  - D-20 (Zero Trust): +2 bonus (APT cannot spread even with stolen credentials)

**Outcome:**
- **Blue Team Succeeds (15+ each turn):** APT detected and eradicated before achieving 3 objectives
- **Blue Team Fails (any turn < 15):** APT progresses to next action; if 3 objectives achieved, game is lost

**Special Rule - Escalating Difficulty:** Each turn the APT remains undetected, DC increases by 1 (Turn 1: DC 15, Turn 2: DC 16, Turn 3: DC 17, etc.)

**Teaching Point:** APTs are sophisticated, well-resourced, and patient. They expect to remain undetected for months or years. Early detection is critical. Continuous monitoring, threat intelligence integration, and advanced hunting are essential for APT detection.

---

### PT-13: Cloud-Specific Attack - Misconfigured Cloud Resources
**Tactic Type:** Cloud Security / Privilege Escalation
**Target Vectors:** MALWARE, CREDENTIAL_ABUSE, NETWORK, DATA_EXFIL
**Difficulty:** ADVANCED (defeat DC 14)

**Description:**
A pentester discovers misconfigured cloud resources (S3 bucket, Azure storage, GCP database) that are accessible without authentication. They pivot from compromised workstation to cloud infrastructure, exfiltrating sensitive data stored in cloud. Can your cloud security controls catch this lateral movement into cloud?

**Attack Details:**
- Targets: Cloud security posture management, identity & access management in cloud
- Assumes: Blue Team has cloud infrastructure in their network design
- Success indicates: Misconfigured cloud resources, weak cloud IAM policies
- Blue Team rolls 1d20 to detect and remediate

**Defending Defenses:**
- **D-04 (Firewall Rules):** +1 bonus (limits cloud connectivity from compromised systems)
- **D-20 (Zero Trust Access):** +2 bonus (requires proper identity & authorization for cloud access)
- **D-21 (Container Security):** +2 bonus (blocks cloud API abuse if containerized)
- **D-22 (SIEM Enterprise):** +2 bonus (detects unusual cloud API calls)
- **D-24 (Threat Intelligence):** +1 bonus (known misconfigured bucket signatures)
- **New Special Defense - Cloud Posture Mgmt:** +3 bonus (automatically detects and remediates misconfigurations)

**Special Cloud Defense:** If Blue Team deployed cloud-specific hardening (e.g., cloud security posture management tools, cloud-native IAM), add +2 bonus.

**Outcome:**
- **Blue Team Succeeds (13+):** Misconfiguration detected and remediated before exfiltration
- **Blue Team Fails:** Cloud data is exfiltrated; -1 penalty to all rolls for remainder of game, plus immediate 15 Budget cost for cloud forensics

**Teaching Point:** Cloud security is fundamentally different from on-premises. Shared responsibility model requires organizations to actively manage cloud configuration. Cloud misconfigurations are the #1 cloud vulnerability. Continuous posture scanning is essential.

---

### PT-14: IoT/OT Compromise - Industrial Network Attack
**Tactic Type:** Operational Technology Attack / Physical Safety Impact
**Target Vectors:** NETWORK, MALWARE
**Difficulty:** ADVANCED (defeat DC 14)

**Description:**
A pentester compromises IoT or Operational Technology (OT) devices (industrial control systems, HVAC, building management, manufacturing systems) that are connected to the corporate network. Unlike IT systems (computers, servers), OT systems prioritize availability and cannot be patched frequently. Can your network architecture prevent OT compromise, and can you detect it before physical systems are affected?

**Attack Details:**
- Targets: Network segmentation between IT and OT, OT-specific monitoring
- Assumes: Blue Team has IoT/OT devices in their network design
- Success indicates: Lack of network segmentation or OT-specific monitoring
- Blue Team rolls 1d20 to detect and isolate

**Defending Defenses:**
- **D-04 (Firewall Rules):** +1 bonus (separates IT from OT traffic)
- **D-09 (Network Segmentation):** +3 bonus (dedicated OT segment with restricted access)
- **D-10 (SIEM Correlation):** +1 bonus (detects OT anomalies if properly tuned)
- **D-22 (SIEM Enterprise):** +2 bonus (advanced OT monitoring and correlation)
- **New Special Defense - OT Monitoring:** +3 bonus (specialized tools detect OT compromise)

**Special OT Defense:** If Blue Team has deployed OT-specific monitoring and segmentation, add +2 bonus.

**Outcome:**
- **Blue Team Succeeds (13+):** OT compromise detected and isolated before impact
- **Blue Team Fails:** OT systems compromised; physical operations affected, -2 penalty to all rolls for remainder of game, plus potential safety/liability consequences (narrative impact)

**Teaching Point:** OT security is distinct from IT security. OT systems cannot be patched like IT systems. Network segmentation is the primary defense. OT-specific monitoring and threat hunting are essential. Organizations with manufacturing, utilities, or building management need specialized OT security strategies.

---

### PT-15: Firmware/BIOS Attack - Bootloader Compromise
**Tactic Type:** Persistence / Hardware-Level Attack
**Target Vectors:** MALWARE, NETWORK
**Difficulty:** EXPERT (defeat DC 15)

**Description:**
A pentester with physical or remote access targets system firmware (BIOS/UEFI) or bootloader, establishing persistence at the hardware level below the operating system. This attack survives OS reinstalls and even hardware replacement (if firmware is deployed via supply chain). Can your controls detect and prevent firmware-level attacks?

**Attack Details:**
- Targets: Firmware integrity, secure boot verification, hardware attestation
- Success indicates: Lack of UEFI Secure Boot, no firmware validation, no TPM
- Blue Team rolls 1d20 to detect firmware tampering

**Defending Defenses:**
- **D-16 (Credential Guard & Secure Boot):** +3 bonus (UEFI Secure Boot prevents unauthorized firmware)
- **D-17 (Malware Sandbox):** +1 bonus only (doesn't catch firmware-level attacks)
- **D-13 (Threat Hunting):** +2 bonus (advanced hunting detects firmware persistence)
- **New Special Defense - Hardware Attestation:** +3 bonus (TPM verification detects firmware changes)
- **New Special Defense - Supply Chain Verification:** +2 bonus (validates firmware integrity from trusted source)

**Special Firmware Defense:** If Blue Team deployed secure boot, TPM attestation, and hardware validation, add +2 additional bonus.

**Outcome:**
- **Blue Team Succeeds (14+):** Firmware tampering detected and system reimaged
- **Blue Team Fails:** Firmware-level persistence established; -2 penalty to all rolls for remainder of game, Blue Team loses control of compromised system

**Teaching Point:** Firmware attacks are extremely sophisticated but increasingly common in APT campaigns. Secure Boot and TPM are standard defenses but must be enabled and properly configured. Firmware supply chain security is critical. Organizations should consider firmware integrity verification in procurement.

---

### PT-16: Privilege Escalation - Containerized Environment Escape
**Tactic Type:** Privilege Escalation / Container Escape
**Target Vectors:** MALWARE, NETWORK
**Difficulty:** EXPERT (defeat DC 15)

**Description:**
A pentester, operating from within a compromised container, exploits a container runtime vulnerability (like CVE-2019-5736 runc exploit) to escape the container and gain access to the underlying host system. From there, lateral movement to other containers and host systems becomes possible. Can your container security and patching strategies prevent container escape?

**Attack Details:**
- Targets: Container runtime patching, container isolation, runtime security
- Assumes: Blue Team has containerized workloads (Docker, Kubernetes, etc.)
- Success indicates: Unpatched container runtime or lack of runtime monitoring
- Blue Team rolls 1d20 to prevent or detect escape

**Defending Defenses:**
- **D-03 (Patching):** +2 bonus (ensures container runtime is patched)
- **D-08 (EDR):** +2 bonus (detects suspicious syscalls attempting escape)
- **D-13 (Threat Hunting):** +2 bonus (hunting for container escape indicators)
- **D-21 (Container Security):** +4 bonus (runtime security detects and blocks escape attempts)
- **New Special Defense - Kubernetes Security Policies:** +2 bonus (network policies and pod security policies restrict escape)

**Special Container Defense:** If Blue Team has deployed comprehensive container security (runtime monitoring + pod security policies + network policies), add +2 additional bonus.

**Outcome:**
- **Blue Team Succeeds (14+):** Container escape prevented or detected before host compromise
- **Blue Team Fails:** Attacker escapes container to host; immediate +1 for all subsequent attacks, gains ability to compromise other containers

**Teaching Point:** Container security is distinct from traditional OS security. Container runtimes have historically had significant vulnerabilities. Runtime security monitoring is essential. Kubernetes network policies and pod security standards are critical controls. Organizations using containers must keep runtimes patched and actively monitor for escape attempts.

---

## Advanced Tactics Summary

| Card | Tactic | Vectors | Difficulty | Primary Defense |
|------|--------|---------|------------|-----------------|
| PT-09 | Multi-Vector Attack | Multiple | ADVANCED (DC 14) | Integrated Response |
| PT-10 | Zero-Day Exploitation | MALWARE, WEB | ADVANCED (DC 15) | Behavioral Detection |
| PT-11 | Ransomware Deployment | MALWARE, EXFIL | ADVANCED (DC 15) | Backup & DR |
| PT-12 | APT Campaign | Multiple | EXPERT (DC 16) | Threat Hunting |
| PT-13 | Cloud Misconfiguration | MALWARE, CA, EXFIL | ADVANCED (DC 14) | Cloud Posture |
| PT-14 | IoT/OT Compromise | NETWORK, MALWARE | ADVANCED (DC 14) | OT Segmentation |
| PT-15 | Firmware Attack | MALWARE, NETWORK | EXPERT (DC 15) | Hardware Attestation |
| PT-16 | Container Escape | MALWARE, NETWORK | EXPERT (DC 15) | Runtime Security |

---

## Gameplay Recommendations

### When to Use Advanced Tactics

1. **Experienced Teams:** Players familiar with core tactics (PT-01 to PT-08)
2. **Longer Games:** Extend Hardening gameplay to 7-10 turns instead of 5-7
3. **Specialized Environments:** Organizations with cloud, IoT, or containerized infrastructure
4. **Challenge Play:** Teams want more difficulty and realism

### Suggested Advanced Scenarios

**Scenario A: Cloud-Native Hardening (6 turns)**
- Turn 1-3: Deploy cloud-specific defenses + container security
- Turn 4: PT-13 (Cloud Misconfiguration) challenge
- Turn 5: PT-16 (Container Escape) challenge
- Turn 6: Final defense evaluation

**Scenario B: APT Defense (8 turns)**
- Turns 1-4: Deploy enterprise-grade defenses (SIEM, threat hunting, forensics)
- Turns 5-7: PT-12 (APT Campaign) multi-turn challenge
- Turn 8: Eradication and recovery

**Scenario C: Zero-Day & Ransomware (7 turns)**
- Turns 1-3: Deploy behavioral detection + backup systems
- Turn 4: PT-10 (Zero-Day) challenge
- Turn 5: PT-11 (Ransomware) challenge
- Turns 6-7: Recovery and hardening improvements

---

## Design Philosophy

**Each Advanced Tactic represents modern, sophisticated threat scenarios** that:

1. **Are realistic** - Based on actual APT campaigns, zero-day vulnerabilities, ransomware attacks
2. **Require advanced defenses** - Cannot be defeated by basic controls alone
3. **Teach emerging threats** - Cloud security, containerization, firmware, OT compromise
4. **Encourage specialization** - Teams must choose focus areas (cloud, OT, containers) and accept vulnerability elsewhere
5. **Create strategic dilemmas** - Limited budget forces difficult prioritization choices

---

## Print Instructions

1. Print on cardstock (250 gsm minimum)
2. Use distinct color scheme from core tactics (suggest: **DARK RED background** to indicate "advanced threat")
3. Core tactics have lighter red; advanced tactics have darker red (visual difficulty progression)
4. Cut along dotted lines
5. Keep separate from core Pentester Tactic Cards until players are ready for advanced challenges

---

## Special Rules for Advanced Tactics

### Difficulty Escalation
Advanced tactics can be introduced gradually:
- Start with PT-09 (Multi-Vector) and PT-10 (Zero-Day)
- Once mastered, add PT-11 (Ransomware) and PT-13 (Cloud)
- Save PT-12 (APT), PT-14 (OT), PT-15 (Firmware), PT-16 (Container) for expert play

### Synergy with Core Tactics
Advanced tactics build on concepts from core tactics:
- PT-09 (Multi-Vector) combines concepts from PT-01 to PT-08
- PT-10 (Zero-Day) extends PT-05 (Priv Esc) concepts
- PT-12 (APT) extends PT-02 (Malware Evasion) concepts

### Future Expansion
Possible additional advanced tactics:
- **PT-17:** Machine Learning Model Poisoning
- **PT-18:** Quantum-Resistant Cryptography Breaking
- **PT-19:** Supply Chain Compromise (Deep Dive)
- **PT-20:** Geopolitical Nation-State Attack Simulation

---

*Hardening Module: Advanced Pentester Tactics*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.1 - Balanced & Refined Edition*
