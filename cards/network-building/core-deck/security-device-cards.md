# Network Building Module: Security Device Cards

**Version:** 2.1 - Balanced & Refined Edition
**Last Updated:** October 2025

---

## Overview

**Security Device Cards** represent network security appliances and tools that control traffic, detect threats, and enforce policies between network segments.

- **Total Cards:** 10 (SEC-01 to SEC-10)
- **Used In:** Network Building module
- **Cost Range:** 6-20 Budget depending on capability and throughput
- **Placement:** Between network segments or at network perimeter

---

## Security Device Cards

### SEC-01: Firewall (Perimeter)
**Type:** Perimeter Control
**Cost:** 8 Budget
**Placement:** Network edge (between internet and internal network)
**Primary Function:** Block unauthorized inbound/outbound traffic

**Description:**
Traditional stateful firewall (Cisco ASA, Palo Alto Networks, Fortinet FortiGate) at network perimeter. Enforces allow/deny rules based on source IP, destination IP, protocol, and port. First line of defense against external attacks.

**What It Protects Against:**
- Unauthorized inbound access attempts
- Unauthorized outbound connections (C2 beaconing, data exfiltration)
- Network reconnaissance from internet
- DDoS attacks (basic flood protection)

**What It Doesn't Protect Against:**
- Application-layer attacks (SQL injection, XSS)
- Lateral movement within network (operates at L3/L4 only)
- Encrypted traffic inspection (needs deep packet inspection)
- Insider threats or authorized-but-malicious access

**Network Interactions:**
- **Required for:** Most organizations (perimeter protection is baseline)
- **Works with:** Web Server (must allow inbound HTTP/HTTPS), Email Server (SMTP/POP3/IMAP)
- **Supports:** Database (prevents inbound database connections from internet)

**Ruleset Complexity:** Medium (5-10 rules for basic setup, 50+ for mature organization)

**Performance Impact:** Minimal for small networks, can become bottleneck at scale

---

### SEC-02: Intrusion Detection System (IDS)
**Type:** Threat Detection
**Cost:** 12 Budget
**Placement:** Internal network (behind firewall, in front of critical systems)
**Primary Function:** Detect suspicious network traffic patterns

**Description:**
Network-based IDS (Snort, Zeek, Suricata) that inspects all traffic and alerts on suspicious patterns. Uses signature matching and/or behavioral analysis to identify known attacks and anomalous traffic.

**What It Protects Against:**
- Known attack patterns (exploits, vulnerability scans)
- Port scanning and reconnaissance
- Lateral movement (SMB, RDP abuse)
- Data exfiltration patterns (unusual volume, unusual destination)
- Command & Control (C2) communication

**What It Doesn't Protect Against:**
- Zero-day exploits (no signature exists)
- Encryption inspection (needs decryption)
- Insider threats (authorized users on authorized systems)
- Application-layer attacks (SQL injection, XSS still pass through)

**Network Interactions:**
- **Works with:** SIEM (IDS alerts feed into SIEM for correlation)
- **Supports:** Detection of T-04 (Lateral Movement), T-09 (C2 Beaconing) in Incident Response
- **Complements:** IPS (IDS detects, IPS blocks; often paired)

**Signature Maintenance:** High (requires weekly/daily signature updates from threat intelligence)

**Performance Impact:** Medium (packet inspection adds latency, can slow network)

---

### SEC-03: Intrusion Prevention System (IPS)
**Type:** Threat Prevention
**Cost:** 14 Budget
**Placement:** Internal network (actively blocks malicious traffic)
**Primary Function:** Block suspicious traffic in real-time

**Description:**
Network-based IPS (actively protective version of IDS). Can block traffic in addition to alerting. Inline placement allows real-time threat blocking.

**What It Protects Against:**
- Everything IDS protects against (detection + blocking)
- Exploit attempts against known vulnerabilities
- Worm propagation
- Policy violations

**What It Doesn't Protect Against:**
- Same limitations as IDS, plus:
- False positive blocking (can block legitimate traffic)
- Encrypted traffic inspection limitations
- Zero-day exploits

**Network Interactions:**
- **Works with:** WAF on web traffic (IPS for network, WAF for applications)
- **Works with:** Firewall (layered network defense)
- **Supports:** Defense against T-02 (Watering Hole), T-05 (Kernel Exploit) in Incident Response

**Tuning Complexity:** High (false positives require tuning; too aggressive = blocks legitimate traffic)

**Performance Impact:** Medium-High (real-time inspection + blocking adds latency)

**Risk:** Misconfigured IPS can block critical business traffic

---

### SEC-04: Load Balancer
**Type:** Availability & Performance
**Cost:** 6 Budget
**Placement:** In front of multiple web servers
**Primary Function:** Distribute traffic across multiple servers

**Description:**
Load balancer (F5, Citrix NetScaler, nginx, HAProxy) distributes incoming traffic across multiple backend servers. Increases availability and performance.

**What It Protects Against:**
- Single server failure (if one web server fails, traffic routes to others)
- DDoS attacks (distributes attack traffic across multiple servers)
- Overload attacks (can queue excess requests)

**What It Doesn't Protect Against:**
- Application vulnerabilities
- Malicious traffic targeting multiple backends
- Session hijacking
- Backend compromise (load balancer can't protect compromised backend)

**Network Interactions:**
- **Requires:** Web Server (needs multiple instances for load balancing to make sense)
- **Works with:** Web Server redundancy (2+ web servers behind load balancer)
- **Supports:** Web application availability in Incident Response scenarios

**Health Check Mechanism:** Monitors backend servers; removes unhealthy servers automatically

**Cost-Benefit:** Low cost (6 Budget) but high value if you have multiple web servers

---

### SEC-05: VPN Gateway
**Type:** Remote Access Control
**Cost:** 7 Budget
**Placement:** Network perimeter (between internet and internal network)
**Primary Function:** Secure remote access for employees/contractors

**Description:**
VPN concentrator (Cisco AnyConnect, Palo Alto Prisma Access, F5 BIG-IP) that creates encrypted tunnels for remote users. Allows employees to securely access internal resources from outside network.

**What It Protects Against:**
- Man-in-the-middle attacks on remote user traffic
- Credential interception (traffic encrypted)
- Unauthorized access to internal resources (authentication required)
- IP spoofing (tunnel validates source)

**What It Doesn't Protect Against:**
- Weak VPN credentials (still vulnerable to brute force)
- Compromised endpoint connecting via VPN (malware on home computer)
- Insider threats (authorized user with legitimate credentials)
- Application vulnerabilities accessed through VPN

**Network Interactions:**
- **Works with:** Domain Controller (VPN user auth)
- **Works with:** MFA (VPN should require MFA)
- **Supports:** Remote work scenarios (necessary for distributed teams)

**Authentication Complexity:** Requires MFA for security (otherwise easy brute force)

**Cost-Benefit:** Necessary for remote work, but alone insufficient (needs MFA)

---

### SEC-06: Email Gateway
**Type:** Email Security
**Cost:** 9 Budget
**Placement:** Network perimeter (filters incoming/outgoing email)
**Primary Function:** Filter spam, phishing, and malware in email

**Description:**
Email security appliance (Proofpoint, Mimecast, Cisco Email Security) that filters all incoming/outgoing email. Scans for phishing, malware, data exfiltration attempts.

**What It Protects Against:**
- Phishing emails (signature and behavior-based detection)
- Email-based malware (attachments, links)
- Spam (reduces alert fatigue)
- Data exfiltration via email (DLP for email)
- Email spoofing (validates SPF/DKIM/DMARC)

**What It Doesn't Protect Against:**
- User clicks on phishing links (user training needed)
- Advanced phishing with legitimate credentials
- Compromised internal email account sending from inside
- Zero-day malware in attachments

**Network Interactions:**
- **Works with:** Email Server (filters before reaching server)
- **Works with:** User Security Training (filters + training = defense-in-depth)
- **Supports:** Defense against T-01 (Phishing) in Incident Response

**Signature Maintenance:** Very high (email threats change daily)

**User Experience Impact:** Email delays (milliseconds) are imperceptible; false positives = missed emails

---

### SEC-07: Web Application Firewall (WAF)
**Type:** Application-Layer Protection
**Cost:** 11 Budget
**Placement:** In front of web server
**Primary Function:** Block application-layer attacks (SQL injection, XSS, etc.)

**Description:**
Web Application Firewall (ModSecurity, Cloudflare WAF, AWS WAF) that inspects HTTP traffic and blocks malicious payloads. Understands web application protocols unlike traditional firewall.

**What It Protects Against:**
- SQL injection attacks
- Cross-site scripting (XSS)
- Cross-site request forgery (CSRF)
- Remote code execution (RCE)
- Malicious file uploads
- Buffer overflows in web apps

**What It Doesn't Protect Against:**
- Logic flaws in application (WAF can't fix broken business logic)
- Authenticated attacks (user is authorized)
- Distributed attacks across many IPs (WAF can't distinguish)
- Zero-day application vulnerabilities (no rule exists)

**Network Interactions:**
- **Requires:** Web Server (only protects web traffic)
- **Works with:** IPS (network-level and application-level defense)
- **Supports:** Defense against T-02 (Watering Hole) in Incident Response

**Rule Maintenance:** Medium (OWASP rules are standardized, vendor maintains them)

**False Positive Rate:** Medium (needs tuning for specific web application)

**Performance Impact:** Medium (application inspection adds latency)

---

### SEC-08: Network Segmentation Switch
**Type:** Network Architecture Control
**Cost:** 10 Budget
**Placement:** Internal network (between segmented network zones)
**Primary Function:** Enforce network segmentation via VLANs and ACLs

**Description:**
Layer 3 switch or router configured for network segmentation. Implements VLANs (virtual LANs) and layer 3 filtering to separate network into zones (DMZ, User segment, Server segment, Admin segment).

**What It Protects Against:**
- Lateral movement via SMB and other internal protocols
- Credential dumping spread (isolated networks can't reach DCs)
- Compromised user system accessing servers directly
- Insider threats (restrictions on data access)
- Data exfiltration to external media (if USB segment is isolated)

**What It Doesn't Protect Against:**
- Attacks within same segment (switch can't prevent user↔user attacks)
- Routing around segmentation (if misconfigured)
- Physical network attacks (layer 1 problems)
- Encrypted tunneling out of segment (if firewall rule allows)

**Network Interactions:**
- **Works with:** Firewall (firewall rules enforce segmentation policies)
- **Works with:** Database Server (database in isolated segment)
- **Works with:** Zero Trust (segmentation is prerequisite for zero trust)
- **Supports:** Defense against T-04 (Lateral Movement) in Incident Response

**Configuration Complexity:** High (requires planning of segment boundaries and rules)

**Cost-Benefit:** Very high ROI (prevents lateral movement for 10 Budget)

---

### SEC-09: SIEM (Security Information & Event Management)
**Type:** Threat Monitoring & Investigation
**Cost:** 15 Budget
**Placement:** Central monitoring (logs from all devices)
**Primary Function:** Aggregate logs and detect threats via correlation

**Description:**
Enterprise SIEM (Splunk, Elastic, QRadar, ArcSight) that collects logs from all systems, correlates events, and alerts on suspicious patterns. Foundation of mature incident response program.

**What It Protects Against:**
- Multi-step attack patterns (correlation finds chains)
- Persistence mechanisms (scheduled tasks, registry changes logged)
- Credential abuse (failed login spikes)
- Insider threats (excessive file access, off-hours activity)
- Data exfiltration (unusual volume to unusual destination)

**What It Doesn't Protect Against:**
- Attacks happening faster than SIEM ingests logs
- False negatives (misconfigured rules miss attacks)
- Encrypted traffic inspection (needs decryption)
- Malware on endpoint (needs EDR, not SIEM)

**Network Interactions:**
- **Requires:** Log Centralization deployment (needs logs to analyze)
- **Works with:** IDS/IPS alerts (SIEM correlates with network alerts)
- **Supports:** Incident Response investigation (SIEM data essential for forensics)
- **Critical for:** Hardening module detection (SIEM detects Pentester Tactics)

**Data Requirements:** Massive (can be 10+ GB/day for large organizations)

**Maintenance:** Very high (tuning rules, managing data retention, responding to false positives)

**Value:** Essential for organizations that need incident detection

---

### SEC-10: Honeypot Network
**Type:** Deception & Detection
**Cost:** 8 Budget
**Placement:** Isolated segment (mimics legitimate infrastructure)
**Primary Function:** Detect lateral movement and reconnaissance

**Description:**
Network of decoy systems (not SRV-10 honeypot server, but entire segment) designed to attract attackers. Any access to honeypot network indicates active attacker.

**What It Protects Against:**
- Lateral movement (attacker triggers honeypot while exploring)
- Network reconnaissance (if honeypot is discovered)
- Ransomware spread (if honeypot is in ransomware path)
- Insider reconnaissance (any access to honeypot = red flag)

**What It Doesn't Protect Against:**
- Attacks that don't trigger honeypot (if attacker follows direct path)
- Honeypot visibility (attacker must find it to trigger it)
- False positives (must be designed to avoid accidental triggers)

**Network Interactions:**
- **Works with:** Network Segmentation (honeypot in isolated but accessible segment)
- **Works with:** SIEM (honeypot triggers feed into SIEM)
- **Supports:** Detection in Hardening module (Deception Technology defense)

**Maintenance:** Medium (must keep honeypot looking alive and attractive)

**Cost-Benefit:** Low cost (8 Budget) with high detection value (zero false positives)

---

## Security Device Summary

| Card | Device Type | Cost | Primary Vectors | Placement |
|------|-------------|------|-----------------|-----------|
| SEC-01 | Firewall (Perimeter) | 8 | NETWORK, CREDENTIAL | Perimeter |
| SEC-02 | IDS | 12 | MALWARE, NETWORK | Internal |
| SEC-03 | IPS | 14 | MALWARE, WEB, NETWORK | Internal |
| SEC-04 | Load Balancer | 6 | NETWORK (availability) | Web Tier |
| SEC-05 | VPN Gateway | 7 | CREDENTIAL, NETWORK | Perimeter |
| SEC-06 | Email Gateway | 9 | SOCIAL_ENG, MALWARE | Perimeter |
| SEC-07 | WAF | 11 | WEB, MALWARE | Web Tier |
| SEC-08 | Network Segmentation | 10 | CREDENTIAL, NETWORK | Internal |
| SEC-09 | SIEM | 15 | Multiple (detection) | Central |
| SEC-10 | Honeypot Network | 8 | NETWORK (detection) | Isolated |

---

## Cost-Benefit Analysis

### Tier 1 (Essential for Any Organization)
- SEC-01 (Firewall): 8 Budget - baseline perimeter control
- SEC-09 (SIEM): 15 Budget - essential for detection
- **Subtotal: 23 Budget** (minimum viable security monitoring)

### Tier 2 (Advanced Organizations)
- SEC-02 (IDS): 12 Budget
- SEC-03 (IPS): 14 Budget - or choose IDS+IPS combo for redundancy
- SEC-08 (Segmentation): 10 Budget - critical for limiting lateral movement
- **Subtotal: 36 Budget** (adds detection + prevention + segmentation)

### Tier 3 (Specialized Protections)
- SEC-06 (Email Gateway): 9 Budget - for email-heavy organizations
- SEC-07 (WAF): 11 Budget - if you have public web application
- SEC-05 (VPN): 7 Budget - if you have remote workers
- SEC-04 (Load Balancer): 6 Budget - if you need web app redundancy
- SEC-10 (Honeypot): 8 Budget - advanced detection tool
- **Subtotal: 41 Budget** (specialized for specific scenarios)

---

## Gameplay Strategy Notes

### Small Organization (Budget: 100)
- Firewall (8) + SIEM (15) = baseline
- Add Email Gateway (9) + Network Segmentation (10) for total 42
- Remaining 58 for servers

### Medium Organization (Budget: 120)
- Firewall (8) + SIEM (15) + Email Gateway (9) = baseline 32
- Add IDS (12) + Network Segmentation (10) + Honeypot (8) = 30 more
- Total security devices: 62
- Remaining 58 for servers

### Large Organization (Budget: 150)
- Deploy multiple devices: Firewall + IDS + IPS + WAF + Email Gateway + SIEM + Segmentation + Honeypot
- Cost all devices: ~100 Budget
- Remaining 50 for servers

---

## Print Instructions

1. Print on cardstock (250 gsm minimum)
2. Color-code by OSI layer:
   - **Red (Layer 3-4, Network):** SEC-01, SEC-02, SEC-03, SEC-08, SEC-10
   - **Orange (Layer 7, Application):** SEC-07
   - **Yellow (Specialized):** SEC-04, SEC-05, SEC-06
   - **Blue (Central):** SEC-09
3. Cut along dotted lines
4. Create a "Device Reference Card" with costs, network placement, and primary protections for quick lookup during gameplay

---

*Network Building Module: Security Device Cards*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.1 - Balanced & Refined Edition*
