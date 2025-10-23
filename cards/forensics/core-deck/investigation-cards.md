# Forensics Module: Investigation Action Cards (Core Deck)

**Version:** 2.1 - Investigation & Attribution Edition
**Card Count:** 12 Investigation Action Cards
**Printable:** Yes (see printing instructions below)

---

## Overview

Investigation Action cards represent specific forensic analysis techniques that investigators can deploy to discover evidence about the attack. Each card has a **Difficulty Class (DC)** that represents the skill required to successfully complete the investigation, a **Cost** in Budget, and a **Duration** showing how many turns the investigation takes.

---

## Card Structure

Each Investigation Action Card includes:
- **Card ID:** Unique identifier (DISK-01, MEM-01, LOG-01, etc.)
- **Title:** Name of investigation technique
- **MITRE ATT&CK:** Referenced technique(s) this investigation detects
- **Difficulty Class (DC):** Roll d20+modifiers vs. this to succeed (typically 11-15)
- **Cost:** Budget units required
- **Duration:** Number of turns investigation takes
- **Description:** What the investigation does and what evidence it reveals
- **Success Conditions:** What happens on success, partial success, or failure
- **Chain of Custody Notes:** Any admissibility or documentation concerns

---

## Card Details

### DISK-01: Disk Image & Analysis

```
╔════════════════════════════════════════════════════════════════╗
║              DISK-01: DISK IMAGE & ANALYSIS                    ║
╠════════════════════════════════════════════════════════════════╣
║ Technique: Forensic Disk Imaging & Analysis                    ║
║ MITRE ATT&CK: T1005 (Data Staged), T1025 (Data from Removable) ║
╠════════════════════════════════════════════════════════════════╣
║ Difficulty Class: 12                                           ║
║ Budget Cost: 10                                                ║
║ Duration: 2 turns (or execute in 1 turn if budget allows)      ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Create a bit-for-bit disk image of the compromised system,     ║
║ then examine file system artifacts, deleted files, and         ║
║ hidden data. This is a foundational forensic technique.        ║
║                                                                 ║
║ What You're Looking For:                                       ║
║ - Malware files (executables, scripts, libraries)              ║
║ - Deleted files (file carving reveals overwritten data)        ║
║ - Persistence mechanisms (startup folders, registry runs)      ║
║ - Downloaded files (browser cache, temp directories)           ║
║ - Suspicious file timestamps (backdating, mismatches)          ║
╠════════════════════════════════════════════════════════════════╣
║ SUCCESS (roll ≥ DC 12):                                        ║
║ Discover ONE Evidence card from: Malware Sample, Persistence   ║
║ Mechanism, or Downloaded Malware evidence set.                 ║
║ Advance: Timeline Completeness +10%, Attack Chain +15%         ║
║                                                                 ║
║ PARTIAL SUCCESS (roll DC-2 to DC-1 = 10-11):                  ║
║ Discover INCOMPLETE Evidence card (partial findings).          ║
║ Advance: Timeline Completeness +5%, Attack Chain +5%           ║
║                                                                 ║
║ FAILURE (roll < 10):                                           ║
║ No evidence discovered. Budget still spent. Take a turn.       ║
╠════════════════════════════════════════════════════════════════╣
║ CHAIN OF CUSTODY:                                              ║
║ Disk image must be bit-for-bit copy. Chain of custody:         ║
║ Strong - Imaging is gold standard in forensics.                ║
║ ✓ All evidence from this source is admissible in court         ║
║                                                                 ║
║ SKILL MODIFIERS:                                               ║
║ +2 if investigator has formal GCIH/CCNA-Security training      ║
║ +1 if investigator has IT administration background            ║
║ +1 if team provides detailed explanation of imaging process    ║
╠════════════════════════════════════════════════════════════════╣
║ NOTES:                                                         ║
║ • Disk imaging is time-consuming (hence 2 turn cost)           ║
║ • Can be combined with DISK-02 for deeper analysis             ║
║ • Foundation for all disk-based forensic work                  ║
║ • Works best on traditional disk systems (less effective on    ║
║   SSDs with wear-leveling and TRIM commands)                   ║
╚════════════════════════════════════════════════════════════════╝
```

---

### DISK-02: File System Carving

```
╔════════════════════════════════════════════════════════════════╗
║              DISK-02: FILE SYSTEM CARVING                      ║
╠════════════════════════════════════════════════════════════════╣
║ Technique: Advanced File Recovery & Data Carving               ║
║ MITRE ATT&CK: T1005 (Data Staged), T1485 (Data Destruction)   ║
╠════════════════════════════════════════════════════════════════╣
║ Difficulty Class: 14                                           ║
║ Budget Cost: 15                                                ║
║ Duration: 3 turns (specialized expertise required)             ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Advanced carving techniques recover data from unallocated      ║
║ disk space and file slack, even when files have been deleted   ║
║ and storage sectors overwritten. Uses specialized tools like   ║
║ EnCase, FTK, or open-source carving tools.                    ║
║                                                                 ║
║ What You're Looking For:                                       ║
║ - Deleted malware (recovered from free space)                  ║
║ - Temporary files (attacker staging data before exfil)         ║
║ - Encryption keys or passphrases (memory remnants on disk)     ║
║ - Hidden partitions or file systems                            ║
║ - Slack space artifacts                                        ║
╠════════════════════════════════════════════════════════════════╣
║ SUCCESS (roll ≥ DC 14):                                        ║
║ Discover ONE Evidence card from: Deep Malware Samples,         ║
║ Encryption Keys Found, or Hidden Backdoor evidence.            ║
║ Advance: Attack Chain +20%, Chain of Custody +10%              ║
║                                                                 ║
║ PARTIAL SUCCESS (roll 12-13):                                  ║
║ Discover partial data (e.g., fragments of deleted file).       ║
║ Advance: Attack Chain +10%, Chain of Custody +5%               ║
║                                                                 ║
║ FAILURE (roll < 12):                                           ║
║ Data too corrupted or already overwritten. No recovery.        ║
╠════════════════════════════════════════════════════════════════╣
║ CHAIN OF CUSTODY:                                              ║
║ Carving is technically sound but must be documented carefully. ║
║ Chain of Custody: Strong if done by certified analyst.         ║
║ ⚠ Partial carving may be challenged in court (incomplete       ║
║   file recovery). Recommend combining with other techniques.   ║
╠════════════════════════════════════════════════════════════════╣
║ SKILL MODIFIERS:                                               ║
║ +2 if investigator has GCFE (Certified Forensic Examiner)      ║
║ +1 if investigator has disk forensics experience               ║
║ +1 if combined with DISK-01 investigation already done         ║
║ -1 if SSD drives present (wear-leveling complicates carving)   ║
╠════════════════════════════════════════════════════════════════╣
║ NOTES:                                                         ║
║ • Expensive investigation (15 budget) for specialized work     ║
║ • Can take weeks in real incidents; represented as 3 turns     ║
║ • Most valuable for discovering deleted persistence and        ║
║   encryption keys                                              ║
║ • Less effective on modern systems with TRIM/wear-leveling     ║
╚════════════════════════════════════════════════════════════════╝
```

---

### MEM-01: Memory Dump & Analysis

```
╔════════════════════════════════════════════════════════════════╗
║              MEM-01: MEMORY DUMP & ANALYSIS                    ║
╠════════════════════════════════════════════════════════════════╣
║ Technique: Volatile Memory Forensics (RAM analysis)            ║
║ MITRE ATT&CK: T1120 (Peripheral Device Discovery), T1057       ║
║              (Process Discovery), T1518 (Software Discovery)   ║
╠════════════════════════════════════════════════════════════════╣
║ Difficulty Class: 13                                           ║
║ Budget Cost: 15                                                ║
║ Duration: 2 turns                                              ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Capture RAM (volatile memory) from running system during       ║
║ incident response, then analyze for active processes, malware, ║
║ injected code, network connections, and encryption keys in     ║
║ memory. Uses tools like Volatility, Rekall, or proprietary     ║
║ memory analysis suites.                                        ║
║                                                                 ║
║ What You're Looking For:                                       ║
║ - Malware processes running in memory                          ║
║ - Injected code (shellcode, DLLs in unexpected processes)      ║
║ - Network connections (established C2 connections)             ║
║ - Encryption keys and credentials in memory                    ║
║ - Command history from interactive shells                      ║
║ - Rootkit or kernel-level hooks                                ║
╠════════════════════════════════════════════════════════════════╣
║ SUCCESS (roll ≥ DC 13):                                        ║
║ Discover ONE Evidence card from: Active Malware Process,       ║
║ C2 Connection, or Injected Code evidence.                      ║
║ Advance: Attack Chain +20%, Timeline Completeness +10%         ║
║                                                                 ║
║ PARTIAL SUCCESS (roll 11-12):                                  ║
║ Discover evidence of suspicious process (incomplete details).  ║
║ Advance: Attack Chain +10%, Timeline Completeness +5%          ║
║                                                                 ║
║ FAILURE (roll < 11):                                           ║
║ Malware may use anti-forensics in memory; analysis inconclusive║
╠════════════════════════════════════════════════════════════════╣
║ CHAIN OF CUSTODY:                                              ║
║ Memory capture is volatile and must be done immediately.       ║
║ Chain of Custody: Strong if documented with timestamps.        ║
║ ✓ Admissible, but include disclaimer about volatile nature    ║
╠════════════════════════════════════════════════════════════════╣
║ SKILL MODIFIERS:                                               ║
║ +2 if investigator trained in memory forensics (Volatility)    ║
║ +1 if malware analysis background                              ║
║ +1 if Analyze Evidence action previously discovered malware    ║
║ -2 if memory was overwritten before capture (time-sensitive)   ║
╠════════════════════════════════════════════════════════════════╣
║ NOTES:                                                         ║
║ • Time-critical: Memory is lost if system is rebooted          ║
║ • Reveals active threats that may not exist on disk            ║
║ • Combines process discovery with malware analysis             ║
║ • Most valuable for finding active C2 connections              ║
╚════════════════════════════════════════════════════════════════╝
```

---

### MEM-02: Memory Forensics Deep Dive

```
╔════════════════════════════════════════════════════════════════╗
║              MEM-02: MEMORY FORENSICS DEEP DIVE                ║
╠════════════════════════════════════════════════════════════════╣
║ Technique: Advanced Volatile Memory Analysis                   ║
║ MITRE ATT&CK: T1112 (Modify System Image), T1187 (Forced Auth) ║
║              T1140 (Deobfuscate/Decode Files or Information)   ║
╠════════════════════════════════════════════════════════════════╣
║ Difficulty Class: 15                                           ║
║ Budget Cost: 20                                                ║
║ Duration: 3 turns (expert-level analysis)                      ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Expert-level memory analysis including malware behavior        ║
║ simulation, deobfuscation of shellcode, reverse engineering    ║
║ of code injected into memory, and recovery of encryption keys. ║
║ Requires deep expertise in assembly language, malware tactics, ║
║ and memory layouts.                                            ║
║                                                                 ║
║ What You're Looking For:                                       ║
║ - Obfuscated/encrypted malware payloads (deobfuscate them)     ║
║ - Code injection techniques (understand HOW malware hides)     ║
║ - Encryption keys and passphrases in memory (crypto recovery)  ║
║ - Malware command history (recent attacker commands)           ║
║ - Process hollowing or code caves (anti-analysis techniques)   ║
║ - Privilege escalation vulnerabilities in use                  ║
╠════════════════════════════════════════════════════════════════╣
║ SUCCESS (roll ≥ DC 15):                                        ║
║ Discover TWO Evidence cards: One from malware behavior set     ║
║ (e.g., Encryption Keys, Command History) + one from attack     ║
║ technique set (e.g., Code Injection Method, Exploitation Used).║
║ Advance: Attack Chain +25%, Attribution +20%                   ║
║                                                                 ║
║ PARTIAL SUCCESS (roll 13-14):                                  ║
║ Discover ONE complete Evidence + incomplete second evidence.   ║
║ Advance: Attack Chain +15%, Attribution +10%                   ║
║                                                                 ║
║ FAILURE (roll < 13):                                           ║
║ Malware uses sophisticated anti-analysis; analysis fails.      ║
╠════════════════════════════════════════════════════════════════╣
║ CHAIN OF CUSTODY:                                              ║
║ Analysis documentation critical (how did you reach conclusions)║
║ Chain of Custody: Strong if reverse engineering is documented. ║
║ ⚠ Conclusions must be explained clearly for court admissibility║
╠════════════════════════════════════════════════════════════════╣
║ SKILL MODIFIERS:                                               ║
║ +3 if investigator has GCFA (Certified Forensic Analyst)       ║
║ +2 if malware reverse engineering background                   ║
║ +1 if Malware Analysis card already completed                  ║
║ +1 if detailed explanation of deobfuscation approach           ║
║ -2 if malware is heavily obfuscated or virtualized             ║
╠════════════════════════════════════════════════════════════════╣
║ NOTES:                                                         ║
║ • Most expensive memory analysis (20 budget)                   ║
║ • Requires reverse engineering expertise                       ║
║ • Discovers "why" the malware works, not just "what"          ║
║ • Essential for understanding sophisticated attacks            ║
║ • Can take weeks in real investigations; represented as 3 turns║
╚════════════════════════════════════════════════════════════════╝
```

---

### LOG-01: Event Log Analysis

```
╔════════════════════════════════════════════════════════════════╗
║              LOG-01: EVENT LOG ANALYSIS                        ║
╠════════════════════════════════════════════════════════════════╣
║ Technique: Windows/Linux Log Examination                       ║
║ MITRE ATT&CK: T1552 (Unsecured Credentials), T1098 (Account)   ║
║              T1021 (Remote Services), T1078 (Valid Accounts)   ║
╠════════════════════════════════════════════════════════════════╣
║ Difficulty Class: 11                                           ║
║ Budget Cost: 5                                                 ║
║ Duration: 1 turn                                               ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Analyze system event logs (Windows Event Log, syslog, etc.)    ║
║ to identify user logins, privilege escalations, file access,   ║
║ and process execution. This is foundational and relatively     ║
║ quick—useful for establishing a basic timeline.                ║
║                                                                 ║
║ What You're Looking For:                                       ║
║ - Failed login attempts (brute force evidence)                 ║
║ - Successful logins from unusual locations/times               ║
║ - Privilege escalation attempts (RunAs, sudo)                  ║
║ - Process creation events                                      ║
║ - Service installation events                                  ║
║ - File access to sensitive files                               ║
╠════════════════════════════════════════════════════════════════╣
║ SUCCESS (roll ≥ DC 11):                                        ║
║ Discover ONE Evidence card from: Suspicious Login Timeline,    ║
║ Privilege Escalation Attempt, or Service Installation evidence.║
║ Advance: Timeline Completeness +15%, Attack Chain +10%         ║
║                                                                 ║
║ PARTIAL SUCCESS (roll 9-10):                                   ║
║ Discover partial timeline (logs are fragmented or unclear).    ║
║ Advance: Timeline Completeness +5%, Attack Chain +5%           ║
║                                                                 ║
║ FAILURE (roll < 9):                                            ║
║ Logs were deleted or corrupted; no useful evidence.            ║
╠════════════════════════════════════════════════════════════════╣
║ CHAIN OF CUSTODY:                                              ║
║ Logs must be exported with metadata (timestamps, user context).║
║ Chain of Custody: Strong if logs are digitally signed.         ║
║ ✓ Admissible in court (widely accepted evidence type)         ║
╠════════════════════════════════════════════════════════════════╣
║ SKILL MODIFIERS:                                               ║
║ +1 if investigator has Windows administration experience       ║
║ +1 if investigator has SIEM/log analysis background            ║
║ +1 if detailed explanation of log analysis approach            ║
║ +2 if prior Timeline Reconstruction investigation completed    ║
╠════════════════════════════════════════════════════════════════╣
║ NOTES:                                                         ║
║ • Cheapest investigation (5 budget) - good starting point      ║
║ • Fastest (1 turn) - can be done early in investigation        ║
║ • Foundation for Timeline Reconstruction and Log Correlation   ║
║ • May be ineffective if attacker deleted logs (add anti-forensics penalty: +2 DC)  ║
╚════════════════════════════════════════════════════════════════╝
```

---

### LOG-02: Deep Log Correlation

```
╔════════════════════════════════════════════════════════════════╗
║              LOG-02: DEEP LOG CORRELATION                      ║
╠════════════════════════════════════════════════════════════════╣
║ Technique: Cross-System Log Analysis & Correlation             ║
║ MITRE ATT&CK: T1087 (Account Discovery), T1021 (Remote Services)║
║              T1083 (File and Directory Discovery)              ║
╠════════════════════════════════════════════════════════════════╣
║ Difficulty Class: 13                                           ║
║ Budget Cost: 10                                                ║
║ Duration: 2 turns                                              ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Correlate logs from multiple systems (servers, firewalls, IDS, ║
║ proxies, domain controllers) to build a complete timeline of   ║
║ attacker lateral movement and actions across the environment.  ║
║ Requires SIEM expertise or manual correlation tools.           ║
║                                                                 ║
║ What You're Looking For:                                       ║
║ - Lateral movement pattern (login on A → login on B → etc)     ║
║ - Privilege escalation sequence (user to admin to system)      ║
║ - Command execution across systems                             ║
║ - Network connections (firewall → host activity)               ║
║ - Timeline of data access and exfiltration                     ║
╠════════════════════════════════════════════════════════════════╣
║ SUCCESS (roll ≥ DC 13):                                        ║
║ Discover ONE Evidence card from: Lateral Movement Pattern,     ║
║ Complete Attack Timeline, or Attacker Command Sequence.        ║
║ Advance: Timeline Completeness +20%, Attack Chain +25%         ║
║                                                                 ║
║ PARTIAL SUCCESS (roll 11-12):                                  ║
║ Discover partial timeline (some systems missing logs).         ║
║ Advance: Timeline Completeness +15%, Attack Chain +10%         ║
║                                                                 ║
║ FAILURE (roll < 11):                                           ║
║ Too many log gaps; timeline cannot be reliably correlated.     ║
╠════════════════════════════════════════════════════════════════╣
║ CHAIN OF CUSTODY:                                              ║
║ Correlation requires clear documentation of methodology.       ║
║ Chain of Custody: Strong if SIEM tool provided audit trail.    ║
║ ✓ Admissible if correlation process is documented clearly     ║
╠════════════════════════════════════════════════════════════════╣
║ SKILL MODIFIERS:                                               ║
║ +2 if investigator has SIEM administration (Splunk, ArcSight) ║
║ +1 if LOG-01 already completed (building on prior analysis)    ║
║ +1 if detailed explanation of correlation methodology         ║
║ +2 if team provides narrative of suspected attacker movements  ║
╠════════════════════════════════════════════════════════════════╣
║ NOTES:                                                         ║
║ • Most valuable for understanding "how" attacker moved         ║
║ • Reveals attack pace and duration (dwell time)                ║
║ • Can expose failed lateral movement attempts                  ║
║ • Requires multiple systems to have logging enabled            ║
╚════════════════════════════════════════════════════════════════╝
```

---

### NET-01: Network Traffic Analysis

```
╔════════════════════════════════════════════════════════════════╗
║              NET-01: NETWORK TRAFFIC ANALYSIS                  ║
╠════════════════════════════════════════════════════════════════╣
║ Technique: Packet Capture & Flow Analysis                      ║
║ MITRE ATT&CK: T1041 (Exfiltration Over C2), T1048 (Alternative ║
║              Protocol), T1071 (Application Layer Protocol)     ║
╠════════════════════════════════════════════════════════════════╣
║ Difficulty Class: 12                                           ║
║ Budget Cost: 10                                                ║
║ Duration: 2 turns                                              ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Analyze network traffic captures (PCAP) or network flow records║
║ (NetFlow) to identify communication patterns, exfiltration     ║
║ evidence, and command-and-control connections. Uses tools like ║
║ Wireshark, Zeek, or commercial traffic analysis platforms.    ║
║                                                                 ║
║ What You're Looking For:                                       ║
║ - Unusual outbound connections (C2 domains, IPs)               ║
║ - Large data transfers (exfiltration evidence)                 ║
║ - Encrypted tunnels (VPN, proxy connections)                   ║
║ - DNS queries for suspicious domains                           ║
║ - HTTP user agents inconsistent with legitimate software       ║
║ - Beacon-like patterns (regular connection attempts)           ║
╠════════════════════════════════════════════════════════════════╣
║ SUCCESS (roll ≥ DC 12):                                        ║
║ Discover ONE Evidence card from: C2 Server Evidence,           ║
║ Exfiltration Traffic Pattern, or Suspicious Domain Lookup.     ║
║ Advance: Attack Chain +20%, Attribution +15%                   ║
║                                                                 ║
║ PARTIAL SUCCESS (roll 10-11):                                  ║
║ Discover suspicious traffic but destination unclear.           ║
║ Advance: Attack Chain +10%, Attribution +5%                    ║
║                                                                 ║
║ FAILURE (roll < 10):                                           ║
║ Traffic too encrypted or obfuscated; cannot analyze.           ║
╠════════════════════════════════════════════════════════════════╣
║ CHAIN OF CUSTODY:                                              ║
║ PCAP files must include timestamp and collection metadata.     ║
║ Chain of Custody: Strong if collected from router/IDS.         ║
║ ✓ Admissible (widely accepted for network evidence)           ║
║ ⚠ Encrypted traffic reveals patterns but not content           ║
╠════════════════════════════════════════════════════════════════╣
║ SKILL MODIFIERS:                                               ║
║ +2 if investigator has Wireshark/packet analysis certification ║
║ +1 if network engineering background                           ║
║ +1 if Threat Attribution evidence already discovered           ║
║ -1 if traffic is heavily encrypted or anonymized              ║
╠════════════════════════════════════════════════════════════════╣
║ NOTES:                                                         ║
║ • Reveals attacker communication patterns                      ║
║ • Can identify C2 infrastructure                               ║
║ • Exfiltration volume is critical evidence                     ║
║ • Encrypted traffic is harder to analyze but patterns visible  ║
╚════════════════════════════════════════════════════════════════╝
```

---

### NET-02: Packet Capture Deep Analysis

```
╔════════════════════════════════════════════════════════════════╗
║              NET-02: PACKET CAPTURE DEEP ANALYSIS              ║
╠════════════════════════════════════════════════════════════════╣
║ Technique: Advanced Protocol Forensics & Reconstruction        ║
║ MITRE ATT&CK: T1557 (Adversary-in-the-Middle), T1040 (Traffic ║
║              Rerouting), T1004 (Winlogon Helper DLL)           ║
╠════════════════════════════════════════════════════════════════╣
║ Difficulty Class: 14                                           ║
║ Budget Cost: 15                                                ║
║ Duration: 3 turns                                              ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Deep packet inspection including protocol reconstruction       ║
║ (rebuilding HTTP streams, email messages, file transfers from  ║
║ packet payloads), malware traffic analysis, and detection of   ║
║ exploitation attempts in traffic. Requires advanced networking  ║
║ and protocol knowledge.                                        ║
║                                                                 ║
║ What You're Looking For:                                       ║
║ - Reconstructed HTTP/S traffic (actual data transferred)       ║
║ - Exploitation payloads in network traffic (shellcode, etc)    ║
║ - Malware command protocols (custom C2 protocols)              ║
║ - Authentication attempts (credentials in transit)             ║
║ - Man-in-the-middle evidence (SSL/TLS downgrade, cert mismatches)║
║ - Attacker reconnaissance traffic patterns                     ║
╠════════════════════════════════════════════════════════════════╣
║ SUCCESS (roll ≥ DC 14):                                        ║
║ Discover TWO Evidence cards from: Exploitation Traffic,        ║
║ C2 Protocol Details, or Attacker Reconnaissance Pattern.       ║
║ Advance: Attack Chain +25%, Attribution +25%                   ║
║                                                                 ║
║ PARTIAL SUCCESS (roll 12-13):                                  ║
║ Discover ONE complete evidence + incomplete second.            ║
║ Advance: Attack Chain +15%, Attribution +10%                   ║
║                                                                 ║
║ FAILURE (roll < 12):                                           ║
║ Encryption or obfuscation prevents useful reconstruction.      ║
╠════════════════════════════════════════════════════════════════╣
║ CHAIN OF CUSTODY:                                              ║
║ PCAP reconstruction must document decoding methodology.        ║
║ Chain of Custody: Moderate (depends on decoding assumptions).  ║
║ ⚠ If encrypted traffic decoded, must explain decryption method║
╠════════════════════════════════════════════════════════════════╣
║ SKILL MODIFIERS:                                               ║
║ +2 if investigator has network forensics certification         ║
║ +2 if protocol reverse engineering experience                  ║
║ +1 if NET-01 already completed (building on analysis)          ║
║ -2 if traffic is encrypted and keys not recovered              ║
╠════════════════════════════════════════════════════════════════╣
║ NOTES:                                                         ║
║ • Most detailed network analysis (3 turns)                     ║
║ • Requires protocol expertise (HTTP, DNS, custom protocols)    ║
║ • Reveals actual attacker commands and data stolen             ║
║ • Challenging when traffic is encrypted                        ║
╚════════════════════════════════════════════════════════════════╝
```

---

### MALW-01: Malware Analysis (Dynamic)

```
╔════════════════════════════════════════════════════════════════╗
║              MALW-01: MALWARE ANALYSIS (DYNAMIC)               ║
╠════════════════════════════════════════════════════════════════╣
║ Technique: Behavioral Malware Analysis                         ║
║ MITRE ATT&CK: T1518 (Software Discovery), T1082 (System Info), ║
║              T1012 (Query Registry), T1033 (System Owner/User)  ║
╠════════════════════════════════════════════════════════════════╣
║ Difficulty Class: 12                                           ║
║ Budget Cost: 15                                                ║
║ Duration: 2 turns                                              ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Execute malware samples in an isolated sandbox environment     ║
║ and record their behavior. Monitor file system changes, registry║
║ modifications, network connections, and process creation to    ║
║ understand what the malware does without reverse engineering.  ║
║ Uses tools like Cuckoo, Any.run, or commercial sandboxes.     ║
║                                                                 ║
║ What You're Looking For:                                       ║
║ - File system changes (what files created/modified)            ║
║ - Registry modifications (persistence mechanisms)              ║
║ - Network communications (DNS, HTTP, etc connections)          ║
║ - Process creation (child processes, injections)               ║
║ - System enumeration (reconnaissance activity)                 ║
║ - Anti-analysis techniques (checks for sandbox)                ║
╠════════════════════════════════════════════════════════════════╣
║ SUCCESS (roll ≥ DC 12):                                        ║
║ Discover ONE Evidence card from: Malware Behavior Profile,     ║
║ Persistence Mechanism Created, or C2 Callback Observed.        ║
║ Advance: Attack Chain +20%, Attribution +10%                   ║
║                                                                 ║
║ PARTIAL SUCCESS (roll 10-11):                                  ║
║ Malware behavior observed but some details unclear.            ║
║ Advance: Attack Chain +10%, Attribution +5%                    ║
║                                                                 ║
║ FAILURE (roll < 10):                                           ║
║ Malware detects sandbox; exhibits anti-analysis behavior.      ║
╠════════════════════════════════════════════════════════════════╣
║ CHAIN OF CUSTODY:                                              ║
║ Sandbox execution creates video/log recordings of behavior.    ║
║ Chain of Custody: Strong if sandbox logs are preserved.        ║
║ ✓ Admissible (widely accepted malware analysis evidence)      ║
╠════════════════════════════════════════════════════════════════╣
║ SKILL MODIFIERS:                                               ║
║ +2 if investigator has CRT (Certified Reverse Engineer - Malware)║
║ +1 if incident responder with malware analysis training        ║
║ +1 if detailed explanation of behavioral analysis approach     ║
║ -1 if malware implements anti-sandbox techniques               ║
╠════════════════════════════════════════════════════════════════╣
║ NOTES:                                                         ║
║ • Safer than static analysis (execution is isolated)           ║
║ • Reveals "what the malware does" not "how it works"          ║
║ • Complements Static Analysis (MALW-02) well                  ║
║ • Useful for identifying persistence and C2 behavior           ║
╚════════════════════════════════════════════════════════════════╝
```

---

### MALW-02: Malware Analysis (Static)

```
╔════════════════════════════════════════════════════════════════╗
║              MALW-02: MALWARE ANALYSIS (STATIC)                ║
╠════════════════════════════════════════════════════════════════╣
║ Technique: Code Reverse Engineering & Analysis                 ║
║ MITRE ATT&CK: T1140 (Deobfuscate/Decode Files), T1113 (Screen  ║
║              Capture), T1005 (Data Staged)                     ║
╠════════════════════════════════════════════════════════════════╣
║ Difficulty Class: 14                                           ║
║ Budget Cost: 10                                                ║
║ Duration: 2 turns                                              ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Disassemble and analyze malware code without execution using   ║
║ reverse engineering tools (IDA Pro, Ghidra, Binary Ninja, etc).║
║ Examine assembly code, strings, imports, and code structure to ║
║ understand attacker capabilities and techniques. Requires      ║
║ assembly language and debugging expertise.                     ║
║                                                                 ║
║ What You're Looking For:                                       ║
║ - Hardcoded C2 servers, encryption keys                        ║
║ - Malware capabilities (spyware, RAT, backdoor, etc)           ║
║ - Obfuscation techniques (packing, encryption, polymorphism)   ║
║ - Code similarities to known malware families                  ║
║ - Exploit codes (zero-days, known CVEs)                        ║
║ - Attacker identity clues (developer name, code style)         ║
╠════════════════════════════════════════════════════════════════╣
║ SUCCESS (roll ≥ DC 14):                                        ║
║ Discover ONE Evidence card from: Malware Source Code Analysis, ║
║ Hardcoded C2 Server, or Code Similarity to Known Family.       ║
║ Advance: Attack Chain +20%, Attribution +25%                   ║
║                                                                 ║
║ PARTIAL SUCCESS (roll 12-13):                                  ║
║ Understand some code features but full analysis incomplete.    ║
║ Advance: Attack Chain +10%, Attribution +10%                   ║
║                                                                 ║
║ FAILURE (roll < 12):                                           ║
║ Malware is heavily obfuscated; code analysis inconclusive.     ║
╠════════════════════════════════════════════════════════════════╣
║ CHAIN OF CUSTODY:                                              ║
║ Reverse engineering analysis is documented with screenshots    ║
║ Chain of Custody: Moderate (interpretation-dependent).         ║
║ ⚠ Conclusions must be clearly explained for admissibility     ║
╠════════════════════════════════════════════════════════════════╣
║ SKILL MODIFIERS:                                               ║
║ +3 if investigator has GREM (GIAC Reverse Engineering Malware) ║
║ +2 if assembly language and debugging expertise                ║
║ +1 if MALW-01 already completed (building on behavioral findings)║
║ +1 if detailed explanation of reverse engineering approach     ║
║ -2 if malware is polymorphic/heavily obfuscated                ║
╠════════════════════════════════════════════════════════════════╣
║ NOTES:                                                         ║
║ • Highest skill requirement (DC 14)                            ║
║ • Reveals "how the malware works"                              ║
║ • Can identify code reuse and attacker patterns                ║
║ • Complements Behavior Analysis (MALW-01) well                ║
║ • Time-consuming (2 turns represents weeks of analysis)        ║
╚════════════════════════════════════════════════════════════════╝
```

---

### TIMELINE-01: Timeline Reconstruction

```
╔════════════════════════════════════════════════════════════════╗
║              TIMELINE-01: TIMELINE RECONSTRUCTION              ║
╠════════════════════════════════════════════════════════════════╣
║ Technique: Event Correlation & Chronological Analysis          ║
║ MITRE ATT&CK: T1005 (Data Staged), T1087 (Account Discovery), ║
║              T1046 (Network Service Discovery)                 ║
╠════════════════════════════════════════════════════════════════╣
║ Difficulty Class: 13                                           ║
║ Budget Cost: 5                                                 ║
║ Duration: 1 turn                                               ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Synthesize evidence from multiple sources (logs, timestamps,   ║
║ file metadata, malware analysis) into a unified chronological  ║
║ timeline of the attack. Identify sequence of events, dwell     ║
║ time, and decision points.                                     ║
║                                                                 ║
║ What You're Looking For:                                       ║
║ - Entry point and initial compromise time                      ║
║ - Privilege escalation points and timing                       ║
║ - Lateral movement sequence                                    ║
║ - Data reconnaissance timeline                                 ║
║ - Exfiltration timing (when, how much, for how long)           ║
║ - Dwell time (how long attacker in network before detection)   ║
╠════════════════════════════════════════════════════════════════╣
║ SUCCESS (roll ≥ DC 13):                                        ║
║ Discover ONE Evidence card: Complete Attack Timeline with      ║
║ key decision points and transitions between phases identified. ║
║ Advance: Timeline Completeness +25%, Attack Chain +15%         ║
║                                                                 ║
║ PARTIAL SUCCESS (roll 11-12):                                  ║
║ Partial timeline with some events missing or unclear.          ║
║ Advance: Timeline Completeness +15%, Attack Chain +10%         ║
║                                                                 ║
║ FAILURE (roll < 11):                                           ║
║ Too many timestamp discrepancies; timeline unreliable.         ║
╠════════════════════════════════════════════════════════════════╣
║ CHAIN OF CUSTODY:                                              ║
║ Timeline must reference source evidence for each event.        ║
║ Chain of Custody: Strong if well-documented and cross-referenced║
║ ✓ Admissible if timeline sources are cited                    ║
╠════════════════════════════════════════════════════════════════╣
║ SKILL MODIFIERS:                                               ║
║ +2 if investigator is DFIR (Digital Forensics & Incident Response)║
║ +1 if LOG-01 or LOG-02 already completed                       ║
║ +2 if detailed explanation synthesizes multiple evidence sources║
║ +1 if team notes discrepancies and explains them               ║
╠════════════════════════════════════════════════════════════════╣
║ NOTES:                                                         ║
║ • Critical for understanding attack progression                ║
║ • Cheap (5 budget) but requires multiple prior investigations  ║
║ • Fast (1 turn) but depends on prior evidence collection       ║
║ • Foundation for narrative reconstruction of incident          ║
╚════════════════════════════════════════════════════════════════╝
```

---

### THREAT-01: Threat Attribution Analysis

```
╔════════════════════════════════════════════════════════════════╗
║              THREAT-01: THREAT ATTRIBUTION ANALYSIS            ║
╠════════════════════════════════════════════════════════════════╣
║ Technique: Threat Intelligence & Attribution                   ║
║ MITRE ATT&CK: S#### (Software/Group categories)                ║
║              Requires synthesis of all prior evidence           ║
╠════════════════════════════════════════════════════════════════╣
║ Difficulty Class: 15                                           ║
║ Budget Cost: 20                                                ║
║ Duration: 3 turns                                              ║
╠════════════════════════════════════════════════════════════════╣
║ DESCRIPTION:                                                   ║
║ Synthesize all collected evidence (malware, infrastructure,    ║
║ tactics, timeline, timeline) to attribute the attack to a      ║
║ known threat group, nation-state, or attacker profile. Includes║
║ cross-referencing with threat intelligence databases, academic ║
║ papers, and law enforcement data. This is the highest-level    ║
║ attribution analysis.                                          ║
║                                                                 ║
║ What You're Looking For:                                       ║
║ - Similar attacks in CTI databases (VirusTotal, OSINT, etc)   ║
║ - Malware signatures matching known threat groups              ║
║ - Tactics & Techniques (TTPs) matching known profiles          ║
║ - Infrastructure (domains, IPs) linked to known campaigns      ║
║ - Language/coding style hints about attacker origin            ║
║ - Geolocation clues from timestamps and infrastructure         ║
║ - Victim profile matching known group targeting patterns       ║
╠════════════════════════════════════════════════════════════════╣
║ SUCCESS (roll ≥ DC 15):                                        ║
║ Discover ONE Evidence card: Threat Attribution Report with     ║
║ confidence level (60-90%) linking to specific threat group.    ║
║ Advance: Attribution Confidence +35%, Attack Chain +10%        ║
║                                                                 ║
║ PARTIAL SUCCESS (roll 13-14):                                  ║
║ Partial attribution (likely group/profile but not 100% certain)║
║ Advance: Attribution Confidence +25%, Attack Chain +5%         ║
║                                                                 ║
║ FAILURE (roll < 13):                                           ║
║ Insufficient evidence for reliable attribution.                ║
╠════════════════════════════════════════════════════════════════╣
║ CHAIN OF CUSTODY:                                              ║
║ Attribution must cite specific evidence for each finding.      ║
║ Chain of Custody: Moderate (depends on CTI source reliability) ║
║ ⚠ Confidence level must be documented (70% vs. 90% certainty) ║
╠════════════════════════════════════════════════════════════════╣
║ SKILL MODIFIERS:                                               ║
║ +2 if investigator has threat intelligence background          ║
║ +1 if access to premium CTI services (CrowdStrike, Mandiant)  ║
║ +1 per prior investigation showing strong evidence patterns    ║
║ +2 if detailed narrative synthesizes multiple evidence sources ║
║ -2 if evidence is sparse or conflicting                        ║
╠════════════════════════════════════════════════════════════════╣
║ NOTES:                                                         ║
║ • Highest difficulty (DC 15) requires extensive prior evidence ║
║ • Cannot be done until sufficient evidence collected           ║
║ • Most valuable action for reaching Victory Condition 1        ║
║ • Attribution confidence matters: 60% vs. 95% is significant   ║
║ • Final step in forensic investigation                         ║
╚════════════════════════════════════════════════════════════════╝
```

---

## Printable Format

### How to Print Cards

**Materials Needed:**
- Cardstock (250 gsm minimum)
- Card sleeves (optional but recommended)
- Scissors or guillotine cutter
- Ruler and cutting mat

**Printing Instructions:**
1. Print each card on heavy cardstock (250 gsm)
2. Cut along the border (approx. 3.5" x 5.5" for standard card size)
3. Optional: Laminate for durability
4. Optional: Sleeve cards for shuffling and handling

**PDF Layout:**
[Card layout with 4-6 cards per page will be generated separately in printable PDF format]

---

## Card Combination & Strategy

### Investigation Pathways

**Pathway 1: Quick Start (Turns 1-3)**
- LOG-01 (Event Log Analysis) → Timeline Reconstruction → Identify key events

**Pathway 2: Deep Evidence (Turns 1-5)**
- DISK-01 (Disk Image) → MALW-01 (Dynamic Analysis) → MALW-02 (Static Analysis) → Understand full malware

**Pathway 3: Network-Based (Turns 1-5)**
- LOG-01 (Initial timeline) → NET-01 (Network Traffic) → NET-02 (Deep Packet Analysis) → Reconstruct C2

**Pathway 4: Attribution (Turns 1-6)**
- MALW-01/02 → NET-01 → THREAT-01 → Complete attribution with infrastructure evidence

---

## FAQ

**Q: Can I do these investigations in any order?**
A: Yes, but some combinations are more efficient. Multiple investigations often support each other.

**Q: What's the DC difficulty based on?**
A: Skill required. Easier investigations (LOG-01, TIMELINE-01) have DC 11-13. Complex investigations (MEM-02, THREAT-01) have DC 14-15.

**Q: Why do some investigations take 3 turns?**
A: They represent weeks of real forensic work compressed into game turns.

**Q: What modifiers apply to my roll?**
A: Skill (+1 to +3), narrative explanation (+1 to +2), prior investigations (+1), challenge circumstances (-1 to -2).

---

## Version History

- **v2.1** (Current) - Investigation & Attribution Edition
  - 12 Investigation Action Cards across 6 forensic disciplines
  - Difficulty Classes 11-15 with clear success criteria
  - Integration with MITRE ATT&CK framework
  - Chain of custody tracking for legal admissibility

