# Forensics Module: Evidence & Findings Cards (Core Deck)

**Version:** 2.1 - Investigation & Attribution Edition
**Card Count:** 12 Evidence Cards + 4 Findings Cards = 16 Total
**Printable:** Yes

---

## Overview

**Evidence Cards** represent specific findings discovered during forensic investigations. They document what was found, how it was found, and what investigative leads it provides.

**Findings Cards** represent conclusions drawn from the evidence—these feed recommendations into Hardening, Network Building, and Audit modules.

---

## Evidence Card Structure

Each Evidence Card includes:
- **Card ID:** Unique identifier (EVD-01 through EVD-12)
- **Type:** Category of evidence (Malware, Credentials, Movement, Exfiltration, Infrastructure, Timeline)
- **Title:** Specific finding name
- **MITRE ATT&CK:** Technique this evidence relates to
- **Description:** What was found and where
- **Discovery Source:** Which Investigation Action cards typically find this evidence
- **Chain of Custody:** Admissibility rating (Strong/Moderate/Weak)
- **Investigative Lead:** What the team can do next with this finding
- **Connection to Attack:** Links to threat cards and attack phases

---

## Evidence Cards (12 Total)

### EVD-01: Credential Dumper Malware

```
╔════════════════════════════════════════════════════════════════╗
║              EVD-01: CREDENTIAL DUMPER MALWARE                 ║
╠════════════════════════════════════════════════════════════════╣
║ Type: Malware & Persistence                                    ║
║ MITRE ATT&CK: T1003 (OS Credential Dumping), T1556 (Modify Auth)║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Malware sample recovered from compromised system that dumps    ║
║ user credentials (SAM file, LSASS process, password hashes,    ║
║ or Kerberos tickets). Examples: Mimikatz, PwDump, LaZagne.     ║
║                                                                 ║
║ Where It Was Found:                                            ║
║ - In System32 directory (hidden with attributes)               ║
║ - In %Temp% directory (temporary staging)                      ║
║ - In admin user AppData (stealth installation)                 ║
║                                                                 ║
║ What It Reveals:                                               ║
║ - Attacker objective: Privilege escalation                     ║
║ - Persistence vector: Credential harvesting                    ║
║ - Attack phase: Privilege escalation → lateral movement        ║
╠════════════════════════════════════════════════════════════════╣
║ Chain of Custody: STRONG ✓                                     ║
║ - Binary file can be hashed (MD5, SHA-1, SHA-256)             ║
║ - File timestamps document creation/modification               ║
║ - Admissible in court with hash validation                     ║
╠════════════════════════════════════════════════════════════════╣
║ Discovery Source:                                              ║
║ - DISK-01/DISK-02: Found as file artifact                      ║
║ - MEM-01/MEM-02: Found as running process in memory            ║
║ - MALW-01: Behavior shows credential dumping actions           ║
║ - MALW-02: Code analysis identifies dumping capabilities       ║
╠════════════════════════════════════════════════════════════════╣
║ Investigative Lead:                                            ║
║ "We found a credential dumper. Let's analyze its behavior      ║
║ (MALW-01) to understand exactly what credentials were captured.║
║ Then we can assume those accounts are compromised."            ║
╠════════════════════════════════════════════════════════════════╣
║ Impact on Progress Meters:                                     ║
║ - Attack Chain: +15% (shows escalation phase)                  ║
║ - Attribution: +10% (dumper choice shows attacker sophistication)║
║ - Timeline: +10% (timestamp shows when escalation occurred)    ║
╠════════════════════════════════════════════════════════════════╣
║ Feeds Into Modules:                                            ║
║ → HARDENING: "Implement credential guard to prevent dumping"   ║
║ → NETWORK BUILDING: "Isolate admin credentials in PAW"         ║
║ → AUDIT: "Verify controls around credential access logging"    ║
╚════════════════════════════════════════════════════════════════╝
```

---

### EVD-02: Command-and-Control Callback Domain

```
╔════════════════════════════════════════════════════════════════╗
║              EVD-02: C2 CALLBACK DOMAIN                        ║
╠════════════════════════════════════════════════════════════════╣
║ Type: Attack Infrastructure                                    ║
║ MITRE ATT&CK: T1071 (Application Layer Protocol), T1573 (Encrypted║
║              Channel), T1008 (Fallback Channels)               ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Domain name or IP address that malware communicates with for   ║
║ command and control. Examples:                                 ║
║ - checkupdate.ru (looks legitimate but is attacker-controlled) ║
║ - 192.0.2.45 (direct IP address)                              ║
║                                                                 ║
║ Where It Was Found:                                            ║
║ - In malware strings (hardcoded in binary)                     ║
║ - In network traffic (outbound connections)                    ║
║ - In memory (communication buffers)                            ║
║ - In DNS logs (DNS queries)                                    ║
║                                                                 ║
║ What It Reveals:                                               ║
║ - Attacker still has access (if domain still active)           ║
║ - C2 infrastructure operator (may be reused for other campaigns)║
║ - Attack sophistication (legitimate-looking domain = higher skill║
╠════════════════════════════════════════════════════════════════╣
║ Chain of Custody: STRONG ✓                                     ║
║ - Network logs document domain/IP communication                ║
║ - PCAP files timestamp the traffic                             ║
║ - DNS logs show query history                                  ║
║ - Admissible with supporting traffic analysis                  ║
╠════════════════════════════════════════════════════════════════╣
║ Discovery Source:                                              ║
║ - MALW-01: Dynamic analysis shows C2 connections               ║
║ - MALW-02: Static analysis finds hardcoded domains             ║
║ - NET-01: Network traffic analysis identifies unusual domains  ║
║ - NET-02: Deep packet inspection reconstructs C2 commands      ║
╠════════════════════════════════════════════════════════════════╣
║ Investigative Lead:                                            ║
║ "We found the C2 domain. Let's do THREAT-01 analysis to:       ║
║ - WHOIS lookup (registrant info)                               ║
║ - Historical DNS records (see past resolutions)                ║
║ - Infrastructure mapping (what else is hosted on this IP?)     ║
║ - Passive DNS (VirusTotal, Shodan, etc)"                       ║
╠════════════════════════════════════════════════════════════════╣
║ Impact on Progress Meters:                                     ║
║ - Attack Chain: +15% (confirms persistence vector)             ║
║ - Attribution: +25% (infrastructure links to threat group)     ║
║ - Timeline: +5% (timestamps when C2 was active)                ║
╠════════════════════════════════════════════════════════════════╣
║ Feeds Into Modules:                                            ║
║ → HARDENING: "Block C2 domain via firewall, DNS sinkhole"      ║
║ → NETWORK BUILDING: "Implement egress filtering to C2 ranges"  ║
║ → AUDIT: "Review firewall rules for C2 domain blocking"        ║
║                                                                 ║
║ THREAT INTEL:                                                  ║
║ Can be shared with ISP/CISA for coordinated takedown/blocking. ║
╚════════════════════════════════════════════════════════════════╝
```

---

### EVD-03: Persistence Mechanism (Scheduled Task)

```
╔════════════════════════════════════════════════════════════════╗
║              EVD-03: PERSISTENCE MECHANISM (SCHEDULED TASK)    ║
╠════════════════════════════════════════════════════════════════╣
║ Type: Malware & Persistence                                    ║
║ MITRE ATT&CK: T1053 (Scheduled Task/Job), T1543 (Create/Modify ║
║              System Process)                                   ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Scheduled task or cron job configured to execute malware at    ║
║ regular intervals (hourly, daily, on system startup). Ensures  ║
║ malware runs even if process is killed or system reboots.      ║
║                                                                 ║
║ Example:                                                       ║
║ - Task: "Windows_Update_Service" (disguised name)              ║
║ - Runs: System startup + every 4 hours                         ║
║ - Executes: C:\Windows\System32\msupd.exe (hidden location)    ║
║                                                                 ║
║ What It Reveals:                                               ║
║ - Attacker skill level (simple but effective)                  ║
║ - Intent: Long-term access/persistence                         ║
║ - Sophistication: Low-to-medium (persistence is basic)         ║
╠════════════════════════════════════════════════════════════════╣
║ Chain of Custody: STRONG ✓                                     ║
║ - Task definition stored in XML (Windows registry/filesystem)  ║
║ - Can be exported and hashed                                   ║
║ - Creation/modification timestamps available                   ║
║ - Fully admissible in court                                    ║
╠════════════════════════════════════════════════════════════════╣
║ Discovery Source:                                              ║
║ - DISK-01: Task files in Windows registry/filesystem           ║
║ - LOG-01: Task execution appears in logs                       ║
║ - MEM-01: Task execution visible in running processes          ║
║ - MALW-01: Dynamic analysis shows task creation               ║
╠════════════════════════════════════════════════════════════════╣
║ Investigative Lead:                                            ║
║ "We found a scheduled task executing malware. Key questions:   ║
║ - When was this task created? (timestamp analysis)             ║
║ - What executable does it run? (acquire and analyze - MALW-01) ║
║ - Is the executable still present? (filesystem search)         ║
║ - Is the task still active? (persistence threat)"              ║
╠════════════════════════════════════════════════════════════════╣
║ Impact on Progress Meters:                                     ║
║ - Attack Chain: +20% (clearly shows persistence phase)         ║
║ - Timeline: +15% (task timestamps show when persistence installed)║
║ - Attribution: +5% (persistence technique is common)           ║
╠════════════════════════════════════════════════════════════════╣
║ Feeds Into Modules:                                            ║
║ → HARDENING: "Implement AppLocker/code signing for scheduled   ║
║              task executables"                                 ║
║ → NETWORK BUILDING: "Enable scheduled task logging and analysis"║
║ → AUDIT: "Verify controls on scheduled task creation"          ║
╚════════════════════════════════════════════════════════════════╝
```

---

### EVD-04: Suspicious Admin Login (Timeline)

```
╔════════════════════════════════════════════════════════════════╗
║              EVD-04: SUSPICIOUS ADMIN LOGIN (TIMELINE)         ║
╠════════════════════════════════════════════════════════════════╣
║ Type: Credentials & Access                                     ║
║ MITRE ATT&CK: T1078 (Valid Accounts), T1021 (Remote Services), ║
║              T1550 (Use Alternate Authentication Material)     ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Administrator account login with suspicious characteristics:   ║
║ - Unusual time (3 AM instead of business hours)                ║
║ - Unusual location (different country/VPN)                     ║
║ - Unusual source (remote desktop instead of VPN)               ║
║ - Batch processing (multiple logins in seconds)                ║
║                                                                 ║
║ Example Log Entry:                                             ║
║ 2024-10-15 03:22:15 - User: Administrator                      ║
║ Source: 192.0.2.100 (Russia)                                   ║
║ Protocol: RDP / SSH                                            ║
║ Success: Yes                                                   ║
║                                                                 ║
║ What It Reveals:                                               ║
║ - Credential compromise (credentials being used by attacker)   ║
║ - Privilege level compromised (admin account)                  ║
║ - Lateral movement likely (attacker on network now)            ║
╠════════════════════════════════════════════════════════════════╣
║ Chain of Custody: STRONG ✓                                     ║
║ - Log entry with timestamp and source                          ║
║ - digitally signed event log                                   ║
║ - Corroborated by other log sources                            ║
║ - Fully admissible in court                                    ║
╠════════════════════════════════════════════════════════════════╣
║ Discovery Source:                                              ║
║ - LOG-01: Event Log Analysis shows unusual logon event         ║
║ - LOG-02: Correlation across multiple systems                  ║
║ - TIMELINE-01: Used to establish attack progression            ║
╠════════════════════════════════════════════════════════════════╣
║ Investigative Lead:                                            ║
║ "Admin account was compromised. Questions to answer:           ║
║ - When was the password changed? (before or after login?)      ║
║ - What other logins occurred after this? (lateral movement)    ║
║ - Was there any password reset? (attacker covering tracks)     ║
║ - What systems did this account access? (scope of compromise)" ║
╠════════════════════════════════════════════════════════════════╣
║ Impact on Progress Meters:                                     ║
║ - Attack Chain: +20% (clear escalation point)                  ║
║ - Timeline: +25% (login timestamp anchors timeline)            ║
║ - Attribution: +10% (geolocation may hint at attacker origin)  ║
╠════════════════════════════════════════════════════════════════╣
║ Feeds Into Modules:                                            ║
║ → HARDENING: "Implement MFA on admin accounts"                 ║
║ → NETWORK BUILDING: "Isolate admin access to PAW"              ║
║ → AUDIT: "Review admin account access controls and logging"    ║
╚════════════════════════════════════════════════════════════════╝
```

---

### EVD-05: Lateral Movement Evidence (Pass-the-Hash)

```
╔════════════════════════════════════════════════════════════════╗
║              EVD-05: LATERAL MOVEMENT (PASS-THE-HASH)          ║
╠════════════════════════════════════════════════════════════════╣
║ Type: Lateral Movement                                         ║
║ MITRE ATT&CK: T1550 (Use Alternate Authentication Material),   ║
║              T1110 (Brute Force), T1021 (Remote Services)      ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Evidence that attacker used stolen password hashes to access   ║
║ other systems without knowing the plaintext password.          ║
║ NTLM hash reuse across systems allows lateral movement.        ║
║                                                                 ║
║ What It Shows:                                                 ║
║ - Compromised account: admin-user (hash: A1B2C3D4E5F6...)      ║
║ - Lateral targets: File server, database server, backup server ║
║ - Movement pattern: Sequential access across infrastructure    ║
║                                                                 ║
║ What It Reveals:                                               ║
║ - Attack sophistication (understanding Windows auth)           ║
║ - Network enumeration (attacker knew what systems exist)       ║
║ - Scope of compromise (multiple systems accessed)              ║
╠════════════════════════════════════════════════════════════════╣
║ Chain of Custody: MODERATE ⚠                                   ║
║ - Hash captured from memory/SAM file                           ║
║ - Corroborated by network logs (successful auth events)        ║
║ - Can be cryptographically validated                           ║
║ - Admissible with supporting evidence (network logs)           ║
╠════════════════════════════════════════════════════════════════╣
║ Discovery Source:                                              ║
║ - LOG-02: Cross-system log correlation shows pattern           ║
║ - NET-01: Network traffic shows auth attempts                  ║
║ - MEM-01/MEM-02: Hash visible in memory                        ║
║ - DISK-01/DISK-02: SAM file contains hashes                    ║
╠════════════════════════════════════════════════════════════════╣
║ Investigative Lead:                                            ║
║ "Attacker used pass-the-hash technique. Next steps:            ║
║ - Determine all systems accessed with this hash                ║
║ - Check what actions were taken on each system                 ║
║ - Look for privilege escalation or data access on each system" ║
╠════════════════════════════════════════════════════════════════╣
║ Impact on Progress Meters:                                     ║
║ - Attack Chain: +25% (shows sophisticated lateral movement)    ║
║ - Timeline: +15% (timestamps show movement sequence)           ║
║ - Attribution: +15% (technique sophistication shows skill)     ║
╠════════════════════════════════════════════════════════════════╣
║ Feeds Into Modules:                                            ║
║ → HARDENING: "Implement Credential Guard, Mimikatz mitigations"║
║ → NETWORK BUILDING: "Network segmentation to limit lateral move"║
║ → AUDIT: "Verify Controls on credential reuse prevention"      ║
╚════════════════════════════════════════════════════════════════╝
```

---

### EVD-06: Data Exfiltration Evidence

```
╔════════════════════════════════════════════════════════════════╗
║              EVD-06: DATA EXFILTRATION EVIDENCE                ║
╠════════════════════════════════════════════════════════════════╣
║ Type: Exfiltration                                             ║
║ MITRE ATT&CK: T1020 (Automated Exfiltration), T1030 (Data      ║
║              Transfer Size Limits), T1048 (Exfil Over Alt      ║
║              Protocol)                                         ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Evidence of large data transfer from internal network to       ║
║ external attacker-controlled destination.                      ║
║                                                                 ║
║ Characteristics:                                               ║
║ - Volume: 100+ GB transferred in 6-hour window                 ║
║ - Timing: During non-business hours (3-8 AM)                   ║
║ - Destination: External IP/domain (attacker server)            ║
║ - Protocol: HTTPS, FTP, or custom protocol                     ║
║ - Pattern: Consistent data rate (not bandwidth-throttled)      ║
║                                                                 ║
║ What It Reveals:                                               ║
║ - Scope of compromise (what was accessed)                      ║
║ - Attacker objective (data theft vs. ransomware)               ║
║ - Attack timeline (when exfiltration occurred)                 ║
║ - Attacker infrastructure (location of receiving server)       ║
╠════════════════════════════════════════════════════════════════╣
║ Chain of Custody: STRONG ✓                                     ║
║ - Network flow logs (NetFlow, sFlow, or IDS logs)              ║
║ - PCAP files with packet timestamps                            ║
║ - Firewall logs documenting outbound connections               ║
║ - Cryptographic hashes of transferred data                     ║
║ - Fully admissible in court                                    ║
╠════════════════════════════════════════════════════════════════╣
║ Discovery Source:                                              ║
║ - NET-01: Network traffic analysis shows volume anomalies      ║
║ - NET-02: Packet inspection shows data being transferred       ║
║ - LOG-02: Firewall/proxy logs show external connections        ║
║ - MALW-01: Dynamic analysis shows file staging before exfil   ║
╠════════════════════════════════════════════════════════════════╣
║ Investigative Lead:                                            ║
║ "Massive data exfiltration detected. Critical questions:       ║
║ - Exactly which files/databases were exfiltrated?              ║
║ - How many customer records are affected?                      ║
║ - Can we identify specific data types stolen?                  ║
║ - Is the data still being transferred (ongoing threat)?"       ║
╠════════════════════════════════════════════════════════════════╣
║ Impact on Progress Meters:                                     ║
║ - Attack Chain: +20% (confirms attacker objectives)            ║
║ - Timeline: +20% (exfil duration/timing)                       ║
║ - Attribution: +10% (exfil infrastructure may be reused)       ║
╠════════════════════════════════════════════════════════════════╣
║ Feeds Into Modules:                                            ║
║ → HARDENING: "Data loss prevention (DLP) controls"             ║
║ → NETWORK BUILDING: "Egress filtering, traffic inspection"     ║
║ → DISASTER RECOVERY: "Breach notification scope (data volume)" ║
║ → AUDIT: "Data protection controls and encryption review"      ║
╚════════════════════════════════════════════════════════════════╝
```

---

### EVD-07: Attacker Infrastructure Map

```
╔════════════════════════════════════════════════════════════════╗
║              EVD-07: ATTACKER INFRASTRUCTURE MAP               ║
╠════════════════════════════════════════════════════════════════╣
║ Type: Attack Infrastructure                                    ║
║ MITRE ATT&CK: Related to C2 infrastructure and command channels║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Connected map of attacker-controlled infrastructure including  ║
║ multiple domains, IP addresses, registrars, and services.      ║
║                                                                 ║
║ Example Infrastructure Web:                                    ║
║ - Primary C2: checkupdate.ru (IP: 192.0.2.45)                 ║
║ - Alternate C2: update-service.xyz (IP: 192.0.2.46)            ║
║ - Malware hosting: files.example.net (IP: 192.0.2.47)          ║
║ - Registrant: All registered via registrar.ru                  ║
║ - ASN: AS64512 (Ukrainian ISP network)                         ║
║                                                                 ║
║ What It Reveals:                                               ║
║ - Attacker operational security (multiple infrastructure) ■    ║
║ - Attacker resources (ISP relationships, hosting account)      ║
║ - Attacker location hints (registrar, ASN, geolocation)        ║
║ - Attack history (domains registered months/years earlier)     ║
║ - Other campaigns (infrastructure reused for other attacks)    ║
╠════════════════════════════════════════════════════════════════╣
║ Chain of Custody: MODERATE ⚠                                   ║
║ - WHOIS records are public but can be modified                 ║
║ - Historical DNS data from passive DNS services                ║
║ - Correlations need cross-referencing                          ║
║ - Admissible with supporting evidence (traffic logs)           ║
╠════════════════════════════════════════════════════════════════╣
║ Discovery Source:                                              ║
║ - THREAT-01: Threat attribution analysis connects domains      ║
║ - MALW-02: Static analysis finds hardcoded backup domains      ║
║ - NET-01: Network traffic shows multiple C2 attempts           ║
║ - CTI research: VirusTotal, Shodan, Passive DNS services      ║
╠════════════════════════════════════════════════════════════════╣
║ Investigative Lead:                                            ║
║ "We've mapped attacker infrastructure. Next steps:             ║
║ - Search threat intelligence databases for this infrastructure ║
║ - Look for connections to known threat groups                  ║
║ - Check if infrastructure used in other campaigns              ║
║ - Contact registrar and hosting for takedown                   ║
║ - Report to ISP for blocking/monitoring"                       ║
╠════════════════════════════════════════════════════════════════╣
║ Impact on Progress Meters:                                     ║
║ - Attribution: +30% (infrastructure often linked to groups)    ║
║ - Attack Chain: +15% (understanding attacker preparation)      ║
║ - Timeline: +10% (infrastructure registration dates)           ║
╠════════════════════════════════════════════════════════════════╣
║ Feeds Into Modules:                                            ║
║ → HARDENING: "Block all known C2 infrastructure via firewall"  ║
║ → AUDIT: "Threat intelligence integration for blocking"        ║
║ → THREAT INTEL: Shareable with industry, law enforcement       ║
╚════════════════════════════════════════════════════════════════╝
```

---

### EVD-08: Encryption Keys Recovered

```
╔════════════════════════════════════════════════════════════════╗
║              EVD-08: ENCRYPTION KEYS RECOVERED                 ║
╠════════════════════════════════════════════════════════════════╣
║ Type: Malware & Persistence                                    ║
║ MITRE ATT&CK: T1140 (Deobfuscate/Decode), T1552 (Unsecured    ║
║              Credentials), T1005 (Data Staged)                 ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Encryption keys recovered from memory, disk, or malware code   ║
║ that allow decryption of:                                      ║
║ - Malware traffic (C2 communications)                          ║
║ - Stolen data archives (what was exfiltrated)                  ║
║ - Attacker staging servers (accessing their infrastructure)    ║
║ - Backdoor communications (understanding commands)             ║
║                                                                 ║
║ Examples:                                                      ║
║ - AES-256 key found in malware binary                          ║
║ - RC4 key in process memory (used for C2)                      ║
║ - TLS certificates for backdoor listener                       ║
║ - Steganography keys (hidden messages in files)                ║
║                                                                 ║
║ What It Reveals:                                               ║
║ - Encryption strength (military-grade vs. basic obfuscation)   ║
║ - Attacker sophistication (poor key management = careless)     ║
║ - What data can be decrypted (scope of analysis)               ║
║ - Backdoor capabilities (understanding command set)            ║
╠════════════════════════════════════════════════════════════════╣
║ Chain of Custody: MODERATE ⚠                                   ║
║ - Keys extracted from memory/binary must be documented         ║
║ - Extraction methodology must be explained                     ║
║ - Cross-referencing with code/behavior confirms validity       ║
║ - Admissible with supporting analysis documentation            ║
╠════════════════════════════════════════════════════════════════╣
║ Discovery Source:                                              ║
║ - MEM-02: Deep memory analysis finds encryption keys           ║
║ - DISK-02: File carving recovers keys from slack space         ║
║ - MALW-02: Static analysis finds hardcoded keys                ║
║ - MALW-01: Dynamic analysis reveals keys generated at runtime  ║
╠════════════════════════════════════════════════════════════════╣
║ Investigative Lead:                                            ║
║ "We recovered encryption keys! This is huge because:           ║
║ - We can decrypt C2 communications (see commands sent)          ║
║ - We can decrypt malware archives (understand what was stolen) ║
║ - We can access attacker staging servers (more evidence)       ║
║ - We can build stronger attribution (command content)"         ║
╠════════════════════════════════════════════════════════════════╣
║ Impact on Progress Meters:                                     ║
║ - Attack Chain: +25% (understand full communication)           ║
║ - Attribution: +20% (commands reveal attacker objectives)      ║
║ - Timeline: +15% (command history shows action sequence)       ║
║ - Chain of Custody: +15% (encryption is strong evidence)       ║
╠════════════════════════════════════════════════════════════════╣
║ Feeds Into Modules:                                            ║
║ → HARDENING: "Secure key management practices"                 ║
║ → AUDIT: "Encryption and key management controls"              ║
║ → THREAT INTEL: Keys shared with law enforcement               ║
╚════════════════════════════════════════════════════════════════╝
```

---

### EVD-09: Attacker Command History

```
╔════════════════════════════════════════════════════════════════╗
║              EVD-09: ATTACKER COMMAND HISTORY                  ║
╠════════════════════════════════════════════════════════════════╣
║ Type: Attack Activity                                          ║
║ MITRE ATT&CK: T1059 (Command & Scripting Interpreter), T1086   ║
║              (PowerShell)                                      ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Recovered history of commands executed by attacker on          ║
║ compromised systems. Shows attacker's actions, objectives,     ║
║ and decision-making process.                                   ║
║                                                                 ║
║ Examples:                                                      ║
║ - PowerShell: Get-AdUser -Filter * | Export-CSV C:\temp\ad.csv ║
║ - CMD: dir \\backup-server\share                               ║
║ - Bash: find / -name "*.sql" -o -name "*.db" 2>/dev/null       ║
║                                                                 ║
║ What It Reveals:                                               ║
║ - Attacker objectives (looking for what? ad users? databases?) ║
║ - Attacker knowledge (familiar with Windows/Linux/networks)    ║
║ - Attack sophistication (script-kiddie vs. skilled operator)   ║
║ - Targeting specificity (random exploration vs. targeted search║
║ - Timeline of activities (sequence of commands shows progression)║
╠════════════════════════════════════════════════════════════════╣
║ Chain of Custody: STRONG ✓                                     ║
║ - Command history from shell/terminal logs                     ║
║ - PowerShell transcript logs (if enabled)                      ║
║ - Memory forensics shows running command buffer                ║
║ - Timestamps document command execution order                  ║
║ - Fully admissible in court                                    ║
╠════════════════════════════════════════════════════════════════╣
║ Discovery Source:                                              ║
║ - MEM-02: Memory forensics finds recent command buffer         ║
║ - LOG-02: Command execution logging (PowerShell, bash history) ║
║ - DISK-01: Shell history files (.bash_history, PowerShell logs)║
║ - MALW-01: Dynamic analysis shows commands sent to shell       ║
╠════════════════════════════════════════════════════════════════╣
║ Investigative Lead:                                            ║
║ "We have the attacker's command history! This shows us:        ║
║ - What systems they were looking for                           ║
║ - What data they searched for                                  ║
║ - How much time they spent on each system                      ║
║ - When they pivoted to new systems                             ║
║ - When they started exfiltration                               ║
║ - If they set up backdoors or persistence"                     ║
╠════════════════════════════════════════════════════════════════╣
║ Impact on Progress Meters:                                     ║
║ - Timeline: +25% (command timing shows exact sequence)         ║
║ - Attack Chain: +25% (command progression shows phases)        ║
║ - Attribution: +15% (command style/language hints)             ║
║ - Chain of Custody: +10% (strong admissible evidence)          ║
╠════════════════════════════════════════════════════════════════╣
║ Feeds Into Modules:                                            ║
║ → HARDENING: "PowerShell transcript logging, command audit"    ║
║ → AUDIT: "Verify logging of command execution"                 ║
║ → TRAINING: "Identify what commands should have triggered alerts"║
╚════════════════════════════════════════════════════════════════╝
```

---

### EVD-10: Malware Behavior Profile

```
╔════════════════════════════════════════════════════════════════╗
║              EVD-10: MALWARE BEHAVIOR PROFILE                  ║
╠════════════════════════════════════════════════════════════════╣
║ Type: Malware & Persistence                                    ║
║ MITRE ATT&CK: Multiple TTPs based on observed behavior         ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Complete profile of malware capabilities and behavior based    ║
║ on dynamic analysis in sandbox environment.                    ║
║                                                                 ║
║ Profile Contents:                                              ║
║ - File system interactions (creates, modifies, deletes)        ║
║ - Registry modifications (persistence mechanisms)              ║
║ - Process creation (parent-child relationships)                ║
║ - Network communications (DNS queries, HTTP requests, IPs)     ║
║ - API calls (Windows/Linux API usage)                          ║
║ - Anti-analysis techniques (sandbox evasion)                   ║
║                                                                 ║
║ Example Output:                                                ║
║ - Name: conhost.exe (masquerading as Windows process)          ║
║ - Creates files: C:\Users\*\AppData\Local\Temp\app.exe         ║
║ - Registry: HKLM\Software\Microsoft\Windows\Run (persistence)  ║
║ - Network: Connects to update.badsite.ru:443 every 15 minutes  ║
║ - Capabilities: Credential harvesting, File encryption, C2    ║
║                                                                 ║
║ What It Reveals:                                               ║
║ - Complete malware capabilities                                ║
║ - Attacker operational techniques                              ║
║ - Threat level (spyware vs. ransomware vs. trojan)              ║
║ - Indicators of Compromise (IOCs)                              ║
╠════════════════════════════════════════════════════════════════╣
║ Chain of Custody: STRONG ✓                                     ║
║ - Sandbox execution video/logs document behavior               ║
║ - Timestamps and sequence recorded                             ║
║ - Reproducible analysis methodology                            ║
║ - Widely accepted malware analysis evidence                    ║
╠════════════════════════════════════════════════════════════════╣
║ Discovery Source:                                              ║
║ - MALW-01: Dynamic sandbox analysis produces full profile      ║
║ - MALW-02: Static analysis validates observed behaviors        ║
║ - Combined: Behavior validated against code confirms accuracy  ║
╠════════════════════════════════════════════════════════════════╣
║ Investigative Lead:                                            ║
║ "We have the complete malware profile. Now we can:             ║
║ - Search for all instances of this malware                     ║
║ - Hunt for C2 communications on network                        ║
║ - Search for created files and artifacts                       ║
║ - Link to other malware families (code similarities)"          ║
╠════════════════════════════════════════════════════════════════╣
║ Impact on Progress Meters:                                     ║
║ - Attack Chain: +20% (understand capabilities = understand threat)║
║ - Attribution: +15% (malware signatures match known families)  ║
║ - Timeline: +10% (behavior timing shows operation phase)       ║
║ - Chain of Custody: +10% (sandbox logs are strong evidence)    ║
╠════════════════════════════════════════════════════════════════╣
║ Feeds Into Modules:                                            ║
║ → HARDENING: "Controls to prevent malware execution"           ║
║ → NETWORK BUILDING: "Detection of malware C2 behaviors"        ║
║ → AUDIT: "EDR/SIEM coverage for malware detection"             ║
╚════════════════════════════════════════════════════════════════╝
```

---

### EVD-11: File Staging Artifacts

```
╔════════════════════════════════════════════════════════════════╗
║              EVD-11: FILE STAGING ARTIFACTS                    ║
╠════════════════════════════════════════════════════════════════╣
║ Type: Attack Activity                                          ║
║ MITRE ATT&CK: T1005 (Data Staged), T1074 (Data Staged)         ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Evidence of attacker staging files before exfiltration. Files  ║
║ are collected in a temporary location, compressed, encrypted,  ║
║ then transferred to attacker server.                           ║
║                                                                 ║
║ Artifacts Found:                                               ║
║ - Compressed archives (RAR, 7z, ZIP files)                     ║
║ - Partially deleted files (overwrite artifacts)                ║
║ - File lists (text files naming what to steal)                 ║
║ - Batch scripts (automated collection scripts)                 ║
║ - Temporary directories with suspicious contents               ║
║                                                                 ║
║ Example:                                                       ║
║ - C:\Staging\data_backup.7z (500 MB)                           ║
║ - C:\Staging\files_to_get.txt (list of target files)           ║
║ - C:\Staging\collect.bat (automated collection script)         ║
║                                                                 ║
║ What It Reveals:                                               ║
║ - Data that was targeted (from .txt lists)                     ║
║ - Volume of exfiltration (archive size)                        ║
║ - Compression ratio (how much data actually stolen)            ║
║ - Attacker knowledge (knew where sensitive data was)           ║
╠════════════════════════════════════════════════════════════════╣
║ Chain of Custody: STRONG ✓                                     ║
║ - File hashes document the staging                             ║
║ - File timestamps show staging timeline                        ║
║ - File content confirms what was staged                        ║
║ - Fully admissible in court                                    ║
╠════════════════════════════════════════════════════════════════╣
║ Discovery Source:                                              ║
║ - DISK-01/DISK-02: Staging artifacts on disk                   ║
║ - LOG-02: Batch script execution in logs                       ║
║ - MALW-01: Dynamic analysis shows staging process              ║
║ - NET-01: File transfer evidence (connection to staging dir)   ║
╠════════════════════════════════════════════════════════════════╣
║ Investigative Lead:                                            ║
║ "Attacker staged specific files. This shows:                   ║
║ - Exact data that was targeted (from staging lists)            ║
║ - Attack planning (targeted vs. random)                        ║
║ - Data sensitivity (what did they prioritize)                  ║
║ - Precision of attack (narrow vs. broad data grab)"            ║
╠════════════════════════════════════════════════════════════════╣
║ Impact on Progress Meters:                                     ║
║ - Attack Chain: +15% (staging phase evidence)                  ║
║ - Timeline: +20% (staging timestamps show prep phase)          ║
║ - Attribution: +10% (precision shows targeting sophistication) ║
║ - Chain of Custody: +10% (file evidence is strong)             ║
╠════════════════════════════════════════════════════════════════╣
║ Feeds Into Modules:                                            ║
║ → HARDENING: "Data identification and protection (DLP)"        ║
║ → AUDIT: "Data classification and access controls"             ║
║ → NOTIFICATION: "Specific data breach notification"            ║
╚════════════════════════════════════════════════════════════════╝
```

---

### EVD-12: Anti-Forensics Evidence

```
╔════════════════════════════════════════════════════════════════╗
║              EVD-12: ANTI-FORENSICS EVIDENCE                   ║
╠════════════════════════════════════════════════════════════════╣
║ Type: Attack Activity                                          ║
║ MITRE ATT&CK: T1070 (Indicator Removal), T1485 (Data Destruction║
║              ), T1551 (Modify Authentication Process)          ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Evidence that attacker actively tried to cover their tracks    ║
║ using anti-forensics techniques.                               ║
║                                                                 ║
║ Anti-Forensics Found:                                          ║
║ - Event log deletion (Clear-EventLog PowerShell)               ║
║ - File timestamp manipulation (TimeStomp)                      ║
║ - Log overwriting (dd commands filling logs)                   ║
║ - File shredding (secure deletion of evidence)                 ║
║ - Registry clearing (CleanMgr, CCleaner, etc)                  ║
║ - Malware self-deletion after execution                        ║
║                                                                 ║
║ What It Reveals:                                               ║
║ - Sophistication (advanced attackers use anti-forensics)       ║
║ - Awareness (attacker knew forensics would be used)            ║
║ - Intent (intentional cover-up vs. accidental trail)           ║
║ - What they're hiding (deleted logs = they knew activities     ║
║   would be suspicious)                                         ║
║ - Attack planning (anti-forensics in playbook = pre-planned)   ║
╠════════════════════════════════════════════════════════════════╣
║ Chain of Custody: MODERATE ⚠                                   ║
║ - Evidence is lack of evidence (absences are hard to prove)    ║
║ - Comparison with known baselines shows anomalies              ║
║ - Log deletion tools detected and documented                   ║
║ - Admissible with supporting context (other evidence)          ║
╠════════════════════════════════════════════════════════════════╣
║ Discovery Source:                                              ║
║ - LOG-01/LOG-02: Gaps in logs (suspicious absences)            ║
║ - DISK-01/DISK-02: Deleted log files, anti-forensic tools     ║
║ - MEM-01/MEM-02: Anti-forensic process running in memory       ║
║ - MALW-01: Dynamic analysis shows self-deletion               ║
║ - MALW-02: Code analysis finds anti-forensic capabilities      ║
╠════════════════════════════════════════════════════════════════╣
║ Investigative Lead:                                            ║
║ "Attacker used anti-forensics. This actually helps because:    ║
║ - Proves attacker sophistication (means skilled opponent)      ║
║ - Indicates intentional harm (not accidental)                  ║
║ - Suggests what they're hiding (what logs were deleted?)       ║
║ - Helps attribution (anti-forensics technique is signature)    ║
║ - Can reconstruct from other sources (memory, network logs)"   ║
╠════════════════════════════════════════════════════════════════╣
║ Impact on Progress Meters:                                     ║
║ - Attribution: +20% (anti-forensic technique is signature)     ║
║ - Attack Chain: +10% (shows post-attack phase)                 ║
║ - Timeline: -10% (anti-forensics makes timeline harder)        ║
║ - Chain of Custody: +5% (proves intentional cover-up)          ║
╠════════════════════════════════════════════════════════════════╣
║ Feeds Into Modules:                                            ║
║ → HARDENING: "Immutable logging (cloud, WORM storage)"         ║
║ → NETWORK BUILDING: "Centralized log aggregation"              ║
║ → AUDIT: "Log integrity and anti-tampering controls"           ║
╚════════════════════════════════════════════════════════════════╝
```

---

## Findings Cards (4 Total)

These are synthesis cards representing conclusions from forensic findings:

### FIND-01: Threat Attribution Report

```
╔════════════════════════════════════════════════════════════════╗
║              FIND-01: THREAT ATTRIBUTION REPORT                ║
╠════════════════════════════════════════════════════════════════╣
║ Type: Findings/Conclusions                                     ║
║ Triggered When: Attribution Confidence ≥ 70%                   ║
╠════════════════════════════════════════════════════════════════╣
║ FINDING:                                                       ║
║ Attack attributed to [Threat Group Name]                       ║
║ Confidence Level: [60-90% based on evidence]                   ║
║ Associated Techniques: [MITRE ATT&CK TTPs]                     ║
║ Previous Targets: [Industries/organizations previously targeted]║
║ Likely Motivation: [Financial gain, espionage, etc]            ║
║                                                                 ║
║ RECOMMENDATIONS:                                               ║
║ 1. Notify law enforcement (FBI, Interpol if international)     ║
║ 2. Share intelligence with industry ISACs                      ║
║ 3. Monitor for indicators of re-engagement                     ║
║ 4. Implement defenses targeting group's known TTPs             ║
║                                                                 ║
║ FEEDS INTO MODULES:                                            ║
║ → HARDENING: "Defense-in-depth against attributed group"       ║
║ → AUDIT & COMPLIANCE: "Threat model update with attributed group"║
║ → INCIDENT RESPONSE: "Playbook for future incidents from group"║
╚════════════════════════════════════════════════════════════════╝
```

---

### FIND-02: Attack Surface Analysis

```
╔════════════════════════════════════════════════════════════════╗
║              FIND-02: ATTACK SURFACE ANALYSIS                  ║
╠════════════════════════════════════════════════════════════════╣
║ Type: Findings/Conclusions                                     ║
║ Triggered When: Attack Chain ≥ 75%                             ║
╠════════════════════════════════════════════════════════════════╣
║ FINDING:                                                       ║
║ Entry Point: [Method used for initial compromise]              ║
║ Exploited Vulnerability: [CVE, weak auth, configuration gap]   ║
║ Escalation Point: [Where privilege escalation occurred]        ║
║ Lateral Movement Paths: [Systems accessed after pivot]         ║
║                                                                 ║
║ ROOT CAUSE:                                                    ║
║ - [Patch missing, configuration weakness, process gap]         ║
║                                                                 ║
║ RECOMMENDATIONS:                                               ║
║ 1. Patch entry-point vulnerability immediately                ║
║ 2. Implement detection for exploitation attempts               ║
║ 3. Restrict lateral movement (network segmentation)            ║
║ 4. Update architecture to prevent this attack path             ║
║                                                                 ║
║ FEEDS INTO MODULES:                                            ║
║ → HARDENING: "Specific technical hardening measures"           ║
║ → NETWORK BUILDING: "Architecture redesign to block attack path"║
║ → AUDIT: "Control gap remediation"                             ║
╚════════════════════════════════════════════════════════════════╝
```

---

### FIND-03: Persistence Mechanisms Discovered

```
╔════════════════════════════════════════════════════════════════╗
║              FIND-03: PERSISTENCE MECHANISMS DISCOVERED        ║
╠════════════════════════════════════════════════════════════════╣
║ Type: Findings/Conclusions                                     ║
║ Triggered When: Multiple persistence artifacts found           ║
╠════════════════════════════════════════════════════════════════╣
║ FINDING:                                                       ║
║ Primary Persistence: [Scheduled task, registry run, etc]       ║
║ Backup Persistence: [Redundant persistence methods]            ║
║ Dormancy: [How long could malware remain active undetected]    ║
║                                                                 ║
║ THREAT:                                                        ║
║ Attacker likely still has access (persistence remains active)  ║
║ - Malware calls home regularly (C2 connections)                ║
║ - Can re-establish access if initial access closed             ║
║ - May deploy additional payloads over time                     ║
║                                                                 ║
║ IMMEDIATE ACTIONS:                                             ║
║ 1. Fully remediate all discovered persistence mechanisms       ║
║ 2. Search for backup persistence (often multiple methods)      ║
║ 3. Monitor for re-establishment of access                      ║
║ 4. Assume attacker may have staged additional backdoors        ║
║                                                                 ║
║ FEEDS INTO MODULES:                                            ║
║ → HARDENING: "Persistence prevention and detection"            ║
║ → DISASTER RECOVERY: "Scope of remediation (how deep?)"        ║
║ → AUDIT: "Endpoint protection review"                          ║
╚════════════════════════════════════════════════════════════════╝
```

---

### FIND-04: Investigative Gaps & Recommendations

```
╔════════════════════════════════════════════════════════════════╗
║              FIND-04: INVESTIGATIVE GAPS & RECOMMENDATIONS     ║
╠════════════════════════════════════════════════════════════════╣
║ Type: Findings/Conclusions                                     ║
║ Triggered When: Investigation completes (Victory or Failure)   ║
╠════════════════════════════════════════════════════════════════╣
║ FINDING:                                                       ║
║ Key Questions Answered:                                        ║
║ - [ ] Attack entry point identified?                           ║
║ - [ ] Attacker motivation understood?                          ║
║ - [ ] Threat actor identified (attribution)?                   ║
║ - [ ] Data compromised: volume and sensitivity?                ║
║ - [ ] Current access status: eliminated or ongoing?            ║
║ - [ ] Persistence mechanisms: removed or active?               ║
║                                                                 ║
║ Remaining Questions:                                           ║
║ - [List specific unknowns from the investigation]              ║
║ - [What evidence gaps prevent complete understanding]          ║
║ - [What would close these gaps (more investigation, experts)]  ║
║                                                                 ║
║ NEXT STEPS:                                                    ║
║ 1. [If gaps remain: External forensics firm for deep analysis] ║
║ 2. [Law enforcement involvement for attribution/prosecution]   ║
║ 3. [Threat intelligence: share findings with industry]         ║
║ 4. [Lessons learned: update hardening/network architecture]    ║
║                                                                 ║
║ FEEDS INTO MODULES:                                            ║
║ → AUDIT & COMPLIANCE: "Post-incident review and control updates"║
║ → TRAINING: "Lessons learned session with all teams"           ║
║ → STRATEGIC: "Investment in detection/response capabilities"   ║
╚════════════════════════════════════════════════════════════════╝
```

---

## Evidence Card Combinations

### Fast Track (Quick Investigation - 3 Turns)
- EVD-04: Suspicious Admin Login → identifies credential compromise
- EVD-03: Persistence Mechanism → shows attacker goal (staying in)
- EVD-02: C2 Domain → identifies attacker infrastructure

**Result:** Quick understanding of attack progression without full attribution

---

### Complete Investigation (5-6 Turns)
- EVD-04 + EVD-05: Login → Lateral Movement (attack progression)
- EVD-01 + EVD-03: Malware + Persistence (attacker capabilities)
- EVD-02 + EVD-07: C2 + Infrastructure (attacker identity)
- EVD-06: Exfiltration (damage assessment)
- EVD-09: Command History (full understanding)

**Result:** Complete attack narrative with attribution

---

### Advanced Investigation (7+ Turns)
- All evidence cards above, PLUS:
- EVD-08: Encryption Keys (decrypt C2 communications)
- EVD-10: Behavior Profile (detailed malware analysis)
- EVD-11: File Staging (understand what was stolen)
- EVD-12: Anti-Forensics (proves intentional harm)

**Result:** Expert-level forensic analysis, actionable threat intelligence

---

## FAQ

**Q: Can I discover the same Evidence card twice?**
A: No. Each Evidence card represents a unique finding. Multiple investigations may point to the same finding (confirming it), but you only gain progress once.

**Q: What if I fail an investigation?**
A: No Evidence discovered, but you've used a turn and Budget. You can retry next turn (costs full Budget again), or move to different investigation.

**Q: How do I use Evidence Cards to support my narrative?**
A: Reference specific Evidence cards when describing findings to Threat Orchestrator or in debrief. Chain of Custody rating shows admissibility in court.

---

## Version History

- **v2.1** (Current) - Investigation & Attribution Edition
  - 12 Evidence Cards across 6 categories
  - 4 Findings Cards for conclusions
  - Integration with Investigation Action Cards
  - Chain of Custody tracking for legal admissibility

