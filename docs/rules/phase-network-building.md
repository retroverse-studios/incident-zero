# Incident Zero: Network Building Phase
## Foundational Architecture & Pre-Game Preparation

---

## Overview: The Complete Security Operations Curriculum

**Incident Zero** now offers a complete **systems thinking progression**:

```
┌─────────────────────────────────────────────────────────────┐
│ PHASE 0A: NETWORK BUILDING (Optional)                       │
│ "What infrastructure do we have?"                           │
│ - Build network with constraints                            │
│ - Make trade-off decisions                                  │
│ - Create exploitable gaps (intentionally or accidentally)   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ PHASE 0B: COMPLIANCE AUDIT (Optional)                       │
│ "Are we audit-ready?"                                       │
│ - Audit findings reveal security gaps                       │
│ - Teams learn what's broken before attack                   │
│ - Create specific vulnerabilities for attack to exploit     │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ PHASE 1: ATTACK CHAIN (Standard)                            │
│ "Can we detect the attack?"                                 │
│ Threats specifically leverage network gaps & audit findings │
└─────────────────────────────────────────────────────────────┘
                    ↙                           ↖
        WIN                                      LOSE
            ↓                                       ↓
┌──────────────────────┐              ┌──────────────────────┐
│ PHASE 2A: HARDENING  │              │ PHASE 2B: DISASTER   │
│ "Build better defense"               │ "Manage crisis"      │
│ - Use audit findings │              │ - Audit failures     │
│ - Fix network gaps   │              │   cost MORE $$$      │
│ - Deploy controls    │              │ - Network gaps make  │
│                      │              │   recovery harder    │
└──────────────────────┘              └──────────────────────┘
            ↓                                       ↓
┌──────────────────────┐              ┌──────────────────────┐
│ PHASE 2C: POST-AUDIT │              │ PHASE 2C: POST-AUDIT │
│ (Optional)           │              │ (Optional)           │
│ "Did we improve?"    │              │ "Are we better?"     │
└──────────────────────┘              └──────────────────────┘
```

---

# PHASE 0A: NETWORK BUILDING

## Purpose
Teams design their organization's IT infrastructure with **budget constraints, business requirements, and trade-off decisions**. Network design creates **intentional and accidental vulnerabilities** that will be exploited in Phase 1.

## Key Concepts

**This is NOT Network Simulation:**
- No packet flows, no routing protocols, no technical details
- **Abstracted decision-making** about architecture and trade-offs
- Each decision has **security implications** discovered later

**Randomness & Realism:**
- Teams don't build a "perfect" network
- Business requirements force imperfect solutions
- Overloaded servers, missing segmentation, legacy systems
- These become **exploitable vulnerabilities**

---

## Network Building Setup (15-20 minutes)

### Starting Situation

**"Your organization needs to build out its IT infrastructure. You have $500K budget (represented as 50 Network Budget tokens). You need to support 500 employees and provide core business functions. Make smart choices - every decision will affect your security posture when we test it later."**

### Available Components

Components fall into **5 categories**:

#### 1. SERVERS (What hosts your business)
Each server card has:
- **Type** (Email, Web, Database, File Storage, Domain Controller, Development, etc.)
- **Capacity** (can host 1, 2, or 3 services)
- **Cost** (5-15 Network Budget)
- **Security Profile** (how hard to exploit)
- **Hosting** (On-Prem, Cloud, Hybrid)

**Server Types:**

| Server Type | Cost | Capacity | Function | Security Notes |
|------------|------|----------|----------|-----------------|
| **Email Server** | 8 | 1 service | Email system | Attracts phishing; exposed to internet |
| **Web Server** | 7 | 1 service | Public website | Internet-facing; vulnerable to exploits |
| **Database Server** | 10 | 1 service | Customer data | High-value target; needs strong access control |
| **File Server** | 6 | 2 services | File storage | Often over-privileged; lateral movement point |
| **Domain Controller** | 12 | 2 services | AD/identity | Critical; compromise = full network access |
| **Development Server** | 5 | 3 services | Dev/Testing | Usually weak security; staging ground for attacks |
| **Backup System** | 9 | 1 service | Data backup | Should be isolated; often forgotten |
| **Cloud Workload (AWS/Azure)** | 4 | 2 services | General cloud | Less under control; API attacks possible |
| **Legacy System** | 3 | 1 service | Old system | High exploitability; hard to patch |
| **Honeypot Decoy** | 7 | 1 service | Detection trap | Detects attackers; wastes attacker time |

#### 2. SECURITY DEVICES (Network controls)
Network-level defenses that protect all servers behind them

| Device Type | Cost | Function | Effect |
|------------|------|----------|--------|
| **Firewall** | 12 | Perimeter defense | Blocks 1 network segment from connecting to others (requires segmentation to use) |
| **Intrusion Detection (IDS)** | 10 | Network monitoring | Detects lateral movement (+2 to detect NETWORK attacks in Phase 1) |
| **Intrusion Prevention (IPS)** | 14 | Network blocking | Blocks exploits (+1 to deploy NETWORK or WEB_EXPLOIT defenses) |
| **Load Balancer** | 8 | Traffic distribution | Spreads load; doesn't increase capacity but improves availability |
| **VPN Concentrator** | 9 | Remote access | Enables secure remote work; may be exploit target |
| **Email Gateway** | 6 | Email filtering | Stops phishing (+2 to defend against SOCIAL_ENGINEERING) |
| **Web Application Firewall (WAF)** | 11 | App-level defense | Protects web servers (+1 to defend against WEB_EXPLOIT) |
| **Network Segmentation Switch** | 10 | Microsegmentation | Enables isolated network zones (requires planning) |
| **SIEM System** | 15 | Centralized logging | Logs everything; helps in Phase 1 investigation (+1 to investigate) |
| **Honeypot Network** | 8 | Detection | Detects lateral movement; wastes attacker time |

#### 3. NETWORK ARCHITECTURE DECISIONS
How servers connect to each other

| Decision | Cost | Impact |
|----------|------|--------|
| **Flat Network** | 0 | All servers on same network; easy but vulnerable |
| **Segmented Network (3 zones)** | 5 | Servers in separate zones (DMZ, internal, sensitive); needs firewalls to control traffic |
| **Fully Isolated (each segment protected)** | 12 | Multiple firewalls; expensive but strong (-1 to lateral movement attacks) |
| **Cloud Hybrid (on-prem + cloud)** | 8 | Split between local and cloud; adds complexity to security |
| **Cloud First (mostly cloud)** | 6 | Mostly cloud; less on-prem; different attack surface |

#### 4. BUSINESS REQUIREMENTS (Services to provide)
Teams MUST provide these services, which determine what servers/software they need

| Requirement | Must Host On | Cost | Notes |
|------------|-------------|------|-------|
| **Email** | Email Server | 0 | Required; Internet-facing; phishing target |
| **Web Presence** | Web Server | 0 | Required; Internet-facing; malware/exploit target |
| **Customer Database** | Database Server | 0 | Required; high-value target; regulatory compliance |
| **File Storage** | File Server | 0 | Required; often over-privileged; lateral movement |
| **User Identity (AD/Kerberos)** | Domain Controller | 0 | Required; critical; full compromise if breached |
| **Email Backup** | Backup System OR File Server | 0 | Recommended; should be isolated |
| **Development/Testing** | Dev Server | 0 | Required; weak security creates staging ground |
| **Disaster Recovery** | Cloud System | 8 | Optional; adds security if implemented |
| **Remote Work VPN** | VPN Concentrator | 0 | Required; attack surface if weak |
| **Public Website** | Already on Web Server | 0 | Already counted |

**Key Point:** Business requirements are NON-NEGOTIABLE. Teams must find places to host them, even if it means overloading servers.

#### 5. HOSTING MODEL DECISIONS
Where servers physically exist

| Model | Cost | Security | Trade-offs |
|-------|------|----------|-----------|
| **Self-Hosted (On-Premises)** | 0 | You control; easy to harden | Expensive to operate; patching responsibility |
| **Cloud-Hosted (AWS/Azure/GCP)** | 0 | Provider's responsibility | Less control; API/credential attacks; compliance issues |
| **Hybrid** | 0 | Mix; complexity | Hardest to secure; two attack surfaces |

---

## Network Building Gameplay (15-20 minutes)

### Phase 0A Turn Structure

**Each Team Has 5 "Build Turns"** (roughly 3-4 minutes per turn)

**Each Turn, Choose ONE:**

#### **Action 1: Place a Server**
- **Cost:** Server cost (3-15 Network Budget)
- **Effect:** Add server to your infrastructure
- **Decision:** What business functions go on it?
- **Constraint:** Server capacity limits (can't put 3 services on a 1-capacity server)

**Example Turn:**
"We're placing a Domain Controller on-premises. Cost: 12 Budget. This hosts user identity services and will also run our SIEM system (2 services). Remaining budget: 38."

#### **Action 2: Add Security Device**
- **Cost:** Device cost (6-15 Network Budget)
- **Effect:** Add network control or defense
- **Placement:** Must protect one or more servers

**Example Turn:**
"We're deploying a Network Segmentation Switch between our DMZ and internal network. Cost: 10 Budget. This creates a firewall boundary so attackers can't easily move laterally. Remaining budget: 28."

#### **Action 3: Implement Network Architecture**
- **Cost:** Architecture cost (0-12 Network Budget)
- **Effect:** Decide how servers are connected
- **Implication:** Affects lateral movement, isolation, recovery

**Example Turn:**
"We're implementing segmented network (3 zones). Cost: 5 Budget. This separates DMZ (email/web), Internal (file/users), and Sensitive (database/AD). Each zone has its own security rules. Remaining budget: 23."

#### **Action 4: Choose Hosting Model**
- **Cost:** Usually 0 (some cloud decisions cost 8)
- **Effect:** Determines attack surface and control

**Example Turn:**
"We're moving our email and web servers to cloud providers (AWS). Cost: 0. This reduces our on-prem attack surface but adds API/credential management complexity. Our Domain Controller stays on-prem."

#### **Action 5: Pass / Skip Turn**
- **Cost:** 0
- **Effect:** Don't build anything this turn
- **Use:** When satisfied with current design

---

## Building with Constraints & Trade-offs

### The Overload Mechanic

**Problem:** Limited budget + required services = imperfect solutions

**Overloading a Server:**
- If a server has capacity for 2 services, you can put 3 services on it
- **Cost:** Save budget (don't need another server)
- **Risk:** Overloaded server is less secure, harder to isolate if compromised

**Example:**
"We only have $5 left. We still need to host Development Services. We can either:
- Buy a Dev Server for $5 and have 0 budget left (safe but risky with no security)
- Put dev services on our File Server (0 cost, but file server is overloaded 3/2 capacity)

We choose to overload the File Server. Notation: File Server (File Storage, Dev Services - OVERLOADED)"

**Consequences of Overloading (discovered in Phase 1):**
- Overloaded servers are easier to pivot from
- If one service is compromised, all services on that server are at risk
- Recovery is harder (can't easily isolate the compromised service)

### The Gaps That Appear Naturally

**Budget Constraints Create Gaps:**

| Gap | How It Happens | Phase 1 Consequence |
|-----|-----------------|-------------------|
| **No Network Segmentation** | Too expensive (costs 5-12) | All servers visible after initial compromise; easy lateral movement |
| **No Firewall** | Too expensive (costs 12) | Can't enforce zone boundaries; segmentation is pointless |
| **Legacy Unpatched Systems** | Cheap ($3) but weak | Easy to exploit; high severity vulnerabilities |
| **Overloaded Servers** | Budget pressure | Multi-service compromise; hard to isolate |
| **No Honeypot** | Luxury item ($7+) | Attackers move silently; no detection friction |
| **No Email Gateway** | Costs 6; phishing gate | Phishing emails pass through; easy initial compromise |
| **No IDS/IPS** | Expensive (10-14) | Lateral movement undetected; wasted budget on segmentation |
| **All Cloud / All On-Prem** | Simplicity over security | Missing security model for mixed environment |
| **No Backup System** | Expensive (9); tempting to skip | Ransomware = no recovery option |
| **No SIEM** | Most expensive (15) | No centralized logging; investigations take longer in Phase 1 |

---

## Network Building Scoring & Summary

### Final Network Card

After Phase 0A, teams receive a **Network Infrastructure Summary Card** documenting:

```
YOUR NETWORK ARCHITECTURE

Servers Deployed:
- Email Server (On-Prem) - HOSTED: Email only
- Web Server (Cloud/AWS) - HOSTED: Web + VPN Services
- Database Server (On-Prem) - HOSTED: Customer Data only
- File Server (On-Prem) - HOSTED: File Storage + Dev Services + Backup (OVERLOADED 3/2)
- Domain Controller (On-Prem) - HOSTED: Identity + SIEM (2/2)

Network Architecture: Segmented (3 zones)
- DMZ: Email (On-Prem), Web (Cloud)
- Internal: File Server, Users
- Sensitive: Database, Domain Controller

Security Devices Deployed:
- Firewall (between DMZ and Internal): 1
- IDS (monitoring Internal zone): 1
- Email Gateway: 1
- SIEM System: 1
- NO Network Segmentation Switch
- NO IPS
- NO Honeypot

Hosting: Hybrid (50% on-prem, 50% cloud)

Total Budget Spent: 47 / 50 (3 remaining)

GAPS IDENTIFIED (will be exploited in Phase 1):
- Overloaded File Server (multi-service compromise risk)
- No IPS (web exploits may pass through)
- No Honeypot (attackers move silently)
- Cloud services not on private network (API exposure)
```

### Network Gaps Score

Each infrastructure decision creates exploitable vulnerabilities:

**Vulnerability Registry** (discovered during Phase 1):

| Gap | Severity | Phase 1 Impact |
|-----|----------|----------------|
| No segmentation | CRITICAL | All servers accessible after one compromise |
| Overloaded servers | HIGH | Multi-service failures; recovery harder |
| No firewall | CRITICAL | Can't enforce boundaries |
| Legacy systems | MEDIUM | Easy exploitation |
| No honeypot | LOW | Slower detection |
| No IDS/IPS | MEDIUM | Lateral movement undetected |
| No email gateway | MEDIUM | Phishing acceptance rate higher |
| All cloud / All on-prem | MEDIUM | Security model doesn't fit attacks |
| No SIEM | LOW | Investigation slower |

**These gaps become MODIFIERS in Phase 1 and Disaster Recovery.**

---
