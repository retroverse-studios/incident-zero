# Network Building Module: Architecture Cards

**Version:** 2.1 - Balanced & Refined Edition
**Last Updated:** October 2025

---

## Overview

**Architecture Cards** represent different network topology and design patterns. Each organization selects ONE architecture that determines how network segments are organized and how traffic flows between them.

- **Total Cards:** 5 (ARCH-01 to ARCH-05)
- **Usage:** Each team selects exactly ONE architecture for their network design
- **Impact:** Architecture choice affects cost, complexity, and security implications
- **Trade-offs:** Each architecture balances cost, security, complexity, and performance

---

## Architecture Options

### ARCH-01: Flat Network (Traditional)
**Cost:** 0 Budget
**Complexity:** 1/5 (very simple)
**Security Posture:** Low
**Performance:** High (no routing/switching overhead)

**Description:**
All systems connected to same network segment (same subnet, same broadcast domain). No network segmentation—everything can talk to everything. Traditional small office network.

**Network Design:**
```
Internet → Firewall → Switch
                      ├─ Email Server
                      ├─ Web Server
                      ├─ Database Server
                      ├─ File Server
                      ├─ Domain Controller
                      └─ User Workstations
```

**Characteristics:**
- All systems on same IP subnet (e.g., 192.168.1.0/24)
- Single broadcast domain
- No layer 3 routing between segments
- Firewall only at perimeter, not internal

**What This Means for Security:**
- **Advantages:** Simple to set up and manage, low cost
- **Disadvantages:** Lateral movement is trivial (attacker on user system can reach database server directly)
- **Implication:** If any system is compromised, entire network is at risk

**Who Uses This:**
- Small offices with <50 people
- Non-security-sensitive organizations
- Organizations where ease of use matters more than security

**Defenses Required:**
- Stronger endpoint protection (must protect each individual system)
- User security training (social engineering becomes primary attack vector)
- Cannot rely on network-level controls

**Against Incident Response Threats:**
- **T-04 (Lateral Movement):** Trivially successful (same network)
- **T-06 (Mimikatz):** Once DC is compromised, entire network is accessible
- **T-11 (Data Exfil):** No segmentation to stop data movement

---

### ARCH-02: Segmented 3-Zone (DMZ Model)
**Cost:** 5 Budget
**Complexity:** 2/5 (simple but requires planning)
**Security Posture:** Medium
**Performance:** Medium (slight routing overhead)

**Description:**
Network divided into three logical zones with firewall rules between them. This is the most common network architecture for medium-sized organizations.

**Network Design:**
```
Internet → Firewall → [DMZ Zone] → Firewall → [Internal Zone] → Firewall → [Admin Zone]
             (Perimeter)    ↓                       ↓                      ↓
                        Web Server            File Server            Domain Controller
                        Email Server          User Workstations      Admin Workstations
                                             Database Server         Backup Server
```

**Three Zones:**

1. **DMZ (Demilitarized Zone)** - Internet-facing systems
   - Email Server, Web Server
   - Direct internet access controlled via firewall
   - If compromised, firewall prevents spread to internal zone

2. **Internal Zone** - Business systems
   - File Server, Database Server, User Workstations
   - Can reach DMZ for legitimate purposes
   - Cannot reach Admin Zone

3. **Admin Zone** - Administrative access and privileged systems
   - Domain Controller, Backup Server
   - Only reachable from specific admin workstations
   - Contains most sensitive access

**Firewall Rules:**
- Internet → DMZ: Allowed (limited ports)
- DMZ → Internal: Blocked (one-way dependency if needed)
- Internal → Admin: Blocked (strict isolation)
- Admin → Internal: Allowed (admin management of internal systems)
- Admin → DMZ: Allowed (admin management of DMZ)

**What This Means for Security:**
- **Advantages:** Limits lateral movement (attacker on web server can't reach database server directly)
- **Disadvantages:** More complex to design and manage

**Who Uses This:**
- Most medium-sized organizations (50-500 employees)
- Organizations with some web/email presence
- Organizations that want segmentation without extreme complexity

**Against Incident Response Threats:**
- **T-04 (Lateral Movement):** Firewall rules block direct SMB access between zones; attacker must find alternate path
- **T-06 (Mimikatz):** DC is in Admin Zone, isolated from compromised internal system
- **T-11 (Data Exfil):** Must exit through firewall, can be monitored

---

### ARCH-03: Fully Isolated (Zero Trust Model)
**Cost:** 12 Budget
**Complexity:** 4/5 (complex, requires careful design)
**Security Posture:** Very High
**Performance:** Lower (strict controls add latency)

**Description:**
Network divided into many small segments, each with strict firewall rules. No implicit trust based on network location—every connection is verified. Approximates zero-trust architecture.

**Network Design:**
```
Internet → Firewall → [DMZ Segment] → Firewall → [Each Server has own segment]
                                                   + User segment
                                                   + Admin segment
                                                   + Development segment
                                                   + Backup segment
                                                   + Legacy segment

Each connection between segments requires explicit allow rule.
```

**Segment Isolation:**
- Every major system or group gets its own segment
- Database server isolated from file server
- Email server isolated from web server
- User workstations isolated from each other (per-user or small group segments)
- Development isolated from production
- Admin segment for domain controllers only
- Legacy systems isolated from modern systems

**Firewall Rules:**
- **Default deny:** Any traffic not explicitly allowed is blocked
- **Explicit allows:** Every needed connection has a specific rule
- **Unidirectional:** Rules are directional (client→server, not server→client)
- **Port specific:** Rules specify exact port, not ranges

**What This Means for Security:**
- **Advantages:** Lateral movement is nearly impossible—even if one system is compromised, firewall blocks reach to others
- **Disadvantages:** Very complex to design, expensive to implement, difficult to troubleshoot when legitimate traffic is blocked

**Who Uses This:**
- Large enterprises with security teams
- Organizations with strict compliance requirements (finance, healthcare, government)
- Organizations that assume breach and plan accordingly

**Against Incident Response Threats:**
- **T-04 (Lateral Movement):** Firewall blocks attempt immediately; attacker cannot move
- **T-06 (Mimikatz):** Even with DC credentials, accessing other systems requires approval
- **T-11 (Data Exfil):** Exfil traffic blocked by firewall rules

**Governance:** Requires change management process for any new firewall rules

---

### ARCH-04: Cloud Hybrid (Mixed On-Premises & Cloud)
**Cost:** 7 Budget
**Complexity:** 3/5 (cloud adds complexity)
**Security Posture:** Medium-High (cloud provider handles some security)
**Performance:** Medium (internet latency for cloud communication)

**Description:**
Organization has both on-premises infrastructure AND cloud resources. Some applications run on-premises, others run in cloud (AWS, Azure, GCP).

**Network Design:**
```
Internet → Firewall → On-Premises Segment
                          ├─ Email Server (on-prem)
                          ├─ File Server (on-prem)
                          ├─ Database Server (on-prem)
                          └─ VPN/Direct Connect → Cloud

                                                 ├─ Web Server (cloud)
                                                 ├─ App Server (cloud)
                                                 ├─ Cloud Storage
                                                 └─ Cloud Database
```

**Connectivity Methods:**
1. **VPN:** Encrypted tunnel over internet (slower, cheaper)
2. **Direct Connect:** Dedicated network connection (faster, more expensive)

**What This Means for Security:**
- **Advantages:** Flexibility (use right tool for each workload), scalability
- **Disadvantages:** New attack surface (cloud APIs, IAM), credential management across platforms

**Cloud-Specific Risks:**
- Misconfigured S3 buckets (public read access)
- Cloud IAM overly permissive (too much access)
- Cloud API keys in source code
- Data residency in unexpected regions

**Who Uses This:**
- Organizations transitioning to cloud (lift-and-shift)
- Organizations with variable load (burst to cloud)
- Organizations with development in cloud, production on-prem

**Against Incident Response Threats:**
- **T-04 (Lateral Movement):** Can pivot from on-prem to cloud via cloud APIs
- **T-08 (Cloud breach):** New threat class specific to cloud
- **T-13 (Misconfiguration):** Cloud-specific attack not in traditional scenarios

---

### ARCH-05: Cloud First (Cloud-Only Infrastructure)
**Cost:** 3 Budget
**Complexity:** 2/5 (cloud provider manages complexity)
**Security Posture:** Medium (cloud provider security + customer configuration)
**Performance:** Excellent (cloud provider optimization)

**Description:**
All infrastructure is cloud-based. No on-premises data center. Applications, data, and users all in cloud (AWS, Azure, GCP, or SaaS).

**Network Design:**
```
Internet → Cloud Edge
            ├─ Web Services (cloud)
            ├─ Application Services (cloud)
            ├─ Database (cloud)
            ├─ Storage (cloud)
            └─ All managed by cloud provider
```

**Deployment Models:**
1. **IaaS (Infrastructure as a Service):** You manage VMs, they manage infrastructure
2. **PaaS (Platform as a Service):** You manage app, they manage platform
3. **SaaS (Software as a Service):** Vendor manages everything (Microsoft 365, Salesforce, Slack)

**Cloud Provider Responsibilities:**
- Physical security of data centers
- Network infrastructure
- Hardware maintenance
- Some security controls (network, storage)

**Customer Responsibilities:**
- IAM configuration (who can access what)
- Network configuration (security groups, VPCs)
- Encryption keys (customer-managed or provider-managed)
- Application security

**What This Means for Security:**
- **Advantages:** Offload infrastructure security to cloud provider, auto-scaling, built-in redundancy
- **Disadvantages:** New threat landscape (cloud-specific attacks, misconfiguration)

**Cloud-Specific Risks:**
- IAM overly permissive (everyone can do everything)
- Public buckets/storage (data visible to internet)
- Unused resources (exposed services)
- Cross-account/cross-tenant misconfiguration
- Cloud API abuse (stolen credentials)

**Who Uses This:**
- Startups (no on-prem infrastructure needed)
- SaaS vendors (cloud is core offering)
- Organizations with distributed teams (no office)
- Modern organizations building on cloud-native architecture

**Against Incident Response Threats:**
- **T-08 (Cloud-specific):** Entirely new threat surface
- **T-13 (Misconfiguration):** Most common cloud vulnerability
- **T-07 (API abuse):** Cloud APIs are attack surface

---

## Architecture Comparison Table

| Aspect | Flat | 3-Zone | Fully Isolated | Cloud Hybrid | Cloud First |
|--------|------|--------|----------------|--------------|------------|
| **Cost (Budget)** | 0 | 5 | 12 | 7 | 3 |
| **Complexity** | 1/5 | 2/5 | 4/5 | 3/5 | 2/5 |
| **Lateral Movement Risk** | Very High | Medium | Very Low | Medium-High | Medium |
| **Incident Response Difficulty** | Very Easy | Medium | Hard | Hard | Hard |
| **Operational Overhead** | Low | Medium | High | High | Low (cloud manages) |
| **Best For** | Tiny orgs | Medium orgs | Large/sensitive | Hybrid migration | Cloud-native |
| **Scalability** | Poor | Good | Excellent | Excellent | Excellent |
| **Cloud Integration** | None | None | Optional | Required | Only option |

---

## Selection Guidance for Teams

### Choose Flat Network (ARCH-01) if:
- ✓ You're building a very small network (<20 people)
- ✓ You don't have sensitive data
- ✓ Your budget is extremely limited
- ✓ You want simplicity over security
- ✗ **Not recommended** for any organization with sensitive data or security requirements

### Choose 3-Zone (ARCH-02) if:
- ✓ You're a medium-sized organization (50-500 people)
- ✓ You have web/email presence exposed to internet
- ✓ You have balance security and simplicity
- ✓ You want to limit lateral movement
- ✓ **Most organizations should choose this**

### Choose Fully Isolated (ARCH-03) if:
- ✓ You're a large organization with security team
- ✓ You have strict compliance requirements (PCI-DSS, HIPAA, government)
- ✓ You assume breach and plan for containment
- ✓ You have budget for complexity
- ✓ You can maintain complex rule sets

### Choose Cloud Hybrid (ARCH-04) if:
- ✓ You're transitioning to cloud
- ✓ You have variable workloads
- ✓ You want to try cloud without full commitment
- ✓ You have both on-premises and cloud operations

### Choose Cloud First (ARCH-05) if:
- ✓ You're a new organization (no on-premises legacy)
- ✓ You want to avoid on-premises infrastructure cost
- ✓ You have a distributed, remote-first workforce
- ✓ You're building on cloud-native architecture

---

## Architecture Impact on Other Modules

### Incident Response
- **Flat Network:** Incident Response is very difficult (attacker spreads easily)
- **3-Zone:** Normal difficulty (firewall blocks some lateral movement)
- **Fully Isolated:** Incident Response is harder (firewall rules block investigation traffic)
- **Cloud Hybrid:** New threat types (cloud-specific attacks)
- **Cloud First:** Cloud-specific investigation tools needed

### Hardening
- **Flat Network:** Cannot implement segmentation defense
- **3-Zone:** Can implement segmentation defense
- **Fully Isolated:** Segmentation is core architecture
- **Cloud Hybrid:** Cloud-specific hardening needed
- **Cloud First:** Cloud-native hardening strategies needed

### Disaster Recovery
- **Flat Network:** Backup in same network, at risk
- **3-Zone:** Backup in isolated segment (safer)
- **Fully Isolated:** Backup fully isolated (safest)
- **Cloud Hybrid:** Cloud backup provides geographically separate copy
- **Cloud First:** Cloud provider manages redundancy and backup

---

## Gameplay Notes

### Budget Impact
Choosing architecture affects remaining budget for servers and security devices:
- ARCH-01 (Flat): 0 Budget cost, frees up budget for servers
- ARCH-02 (3-Zone): 5 Budget cost, medium budget remaining
- ARCH-03 (Fully Isolated): 12 Budget cost, significant budget consumed
- ARCH-04 (Cloud Hybrid): 7 Budget cost, cloud connectivity cost
- ARCH-05 (Cloud First): 3 Budget cost, low cost (cloud provider manages infrastructure)

### Firewall Rule Complexity
Higher security architectures require more firewall rules:
- ARCH-01: 0 rules needed (flat network)
- ARCH-02: 10-20 rules (3-zone model)
- ARCH-03: 50-100+ rules (fully isolated, per-system rules)
- ARCH-04: 20-30 rules (cloud connectivity + on-prem)
- ARCH-05: 10-15 rules (cloud provider manages most)

---

## Print Instructions

1. Print on cardstock (250 gsm minimum)
2. Use distinct coloring by security level:
   - **Red (Low Security):** ARCH-01
   - **Yellow (Medium Security):** ARCH-02
   - **Green (High Security):** ARCH-03
   - **Blue (Cloud Hybrid):** ARCH-04
   - **Purple (Cloud First):** ARCH-05
3. Include a visual diagram on each card showing network layout
4. Cut along dotted lines
5. Create a decision tree reference card to help teams choose architecture

---

## Decision Tree for Architecture Selection

```
Does your organization use cloud?
├─ No → Do you have >100 people?
│   ├─ No → Choose ARCH-01 (Flat) or ARCH-02 (3-Zone)
│   └─ Yes → Do you have compliance requirements?
│       ├─ No → Choose ARCH-02 (3-Zone)
│       └─ Yes → Choose ARCH-03 (Fully Isolated)
│
├─ Partially (hybrid) → Choose ARCH-04 (Cloud Hybrid)
│
└─ Yes, entirely cloud → Choose ARCH-05 (Cloud First)
```

---

*Network Building Module: Architecture Cards*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.1 - Balanced & Refined Edition*
