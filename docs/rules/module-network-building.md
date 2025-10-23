# Network Building Module: Rules & Mechanics

**Version:** 2.1 - Balanced & Refined Edition
**Last Updated:** October 2025

---

## Module Overview

The **Network Building Module** teaches players how to design IT infrastructure under budget constraints, business requirements, and trade-off decisions. This is a *pre-game* module designed to create the network context for other modules (particularly Incident Response, Hardening, and Disaster Recovery).

**Key Concept:** Architecture decisions create vulnerabilities that are discovered during investigations and audits. Bad decisions made here cost more money later.

**Module Teaches:**
- **Primary:** Network architecture, infrastructure design, security trade-offs
- **Secondary:** Budget prioritization, business vs. security balance, intentional/accidental vulnerabilities

**Integration Point:**
- Network Building can be played standalone OR as setup for Incident Response/Hardening/Disaster Recovery modules
- When combined with other modules, the network design created here becomes the context for those modules (see [module-combinations.md](../module-combinations.md))

---

## Module Setup (15-20 minutes)

### 1. Choose Difficulty Level

| Difficulty | Budget | Recommended Use |
|------------|--------|-----------------|
| **Beginner** | 40 | Learning networks, constrained decisions |
| **Standard** | 50 | Balanced play, typical scenario |
| **Advanced** | 60 | Strategic depth, more options |

**Budget represents:** Time, money, and resources for infrastructure design

### 2. Starting Scenario

**Narrative Framing:**

> "Your organization is building or rebuilding its IT infrastructure. You have limited budget and must support 500 employees with core business functions. Every decision will affect your security posture when this network is tested. Make smart trade-offs."

**Key Point:** Teams don't know yet which decisions will matter most. Some budget is "wasted" on nice-to-haves, some on security that (hopefully) won't be needed.

### 3. Available Network Components

Components fall into **5 categories**:

#### Category 1: Server Types

| Server Type | Cost | Capacity | Function | Security Notes |
|------------|------|----------|----------|-----------------|
| **Email Server** | 8 | 1 | Email system | Internet-facing; phishing target |
| **Web Server** | 7 | 1 | Public website | Internet-facing; exploit target |
| **Database Server** | 10 | 1 | Customer data | High-value target; access control critical |
| **File Server** | 6 | 2 | File storage | Often over-privileged; lateral movement point |
| **Domain Controller** | 12 | 2 | User identity (AD/Kerberos) | Critical; full compromise if breached |
| **Development Server** | 5 | 3 | Dev/testing environment | Weak security; staging ground for attacks |
| **Backup System** | 9 | 1 | Data backup | Should be isolated; ransomware recovery |
| **Cloud Workload** | 4 | 2 | General cloud compute | Less control; API/credential exposure |
| **Legacy System** | 3 | 1 | Old/unmaintained system | High exploitability; hard to patch |
| **Honeypot Decoy** | 7 | 1 | Detection trap | Detects attackers; wastes attacker time |

**Capacity Rules:**
- Each server can host a certain number of services (shown in Capacity column)
- Services = business functions (email, web, database, identity, file storage, etc.)
- Can OVERLOAD a server (put more services than capacity allows) to save budget, but creates risk

#### Category 2: Security Devices

| Device Type | Cost | Function | Gameplay Effect |
|------------|------|----------|-----------------|
| **Firewall** | 12 | Perimeter defense | Blocks traffic between network zones |
| **Intrusion Detection (IDS)** | 10 | Network monitoring | Detects lateral movement (+1 investigation modifier in IR) |
| **Intrusion Prevention (IPS)** | 14 | Network blocking | Blocks exploits passively |
| **Load Balancer** | 8 | Traffic distribution | Improves availability without extra capacity |
| **VPN Concentrator** | 9 | Remote access | Enables secure remote work; attack surface if weak |
| **Email Gateway** | 6 | Email filtering | Stops phishing; reduces SOCIAL_ENGINEERING risk |
| **Web Application Firewall (WAF)** | 11 | App-level defense | Protects web servers from app attacks |
| **Network Segmentation Switch** | 10 | Microsegmentation | Creates isolated network zones |
| **SIEM System** | 15 | Centralized logging | Logs everything; helps IR investigations (+1 to Investigate in IR module) |
| **Honeypot Network** | 8 | Detection | Detects lateral movement; wastes attacker time |

#### Category 3: Network Architecture Decisions

How servers are logically organized and connected:

| Decision | Cost | Security Impact | Notes |
|----------|------|-----------------|-------|
| **Flat Network** | 0 | No segmentation | All servers on same network; vulnerable but simple |
| **Segmented Network (3 zones)** | 5 | Basic isolation | Separate DMZ, Internal, Sensitive zones |
| **Fully Isolated (multiple firewalls)** | 12 | Strong isolation | Each zone protected; expensive but resilient |
| **Cloud Hybrid (on-prem + cloud)** | 8 | Complex | Adds cloud security considerations |
| **Cloud First (mostly cloud)** | 6 | Different attack surface | Less on-prem; more cloud API risk |

**Architecture decisions are NON-NEGOTIABLE** - teams must pick one to organize their network.

#### Category 4: Business Requirements

Teams MUST provide these services (cannot skip):

| Requirement | Must Host On | Cost | Business Impact |
|------------|-------------|------|-----------------|
| **Email** | Email Server | 0 | Required; non-negotiable |
| **Web Presence** | Web Server | 0 | Required; online business |
| **Customer Database** | Database Server | 0 | Required; core data |
| **File Storage** | File Server | 0 | Required; document sharing |
| **User Identity (AD/Kerberos)** | Domain Controller | 0 | Required; access control |
| **Email Backup** | Backup System OR File Server | 0 | Recommended; recovery option |
| **Development/Testing** | Dev Server | 0 | Required; software development |
| **Disaster Recovery** | Cloud or isolated system | 8 (if cloud) | Optional; recovery plan |
| **Remote Work VPN** | VPN Concentrator | 0 | Required; modern workforce |

**Key Rule:** Business requirements are fixed. Teams must find places to host them, even if it means overloading servers or making difficult trade-offs.

#### Category 5: Hosting Model

Physical location of infrastructure:

| Model | Cost | Notes |
|-------|------|-------|
| **Self-Hosted (On-Premises)** | 0 | Team controls; responsibility for patching |
| **Cloud-Hosted (AWS/Azure/GCP)** | 0 | Provider controls; less direct control |
| **Hybrid** | 0 | Mix of on-prem and cloud; complex |

---

## Gameplay Loop (15-20 minutes)

### Turn Structure

**Teams take 5 "Build Turns"** (~3-4 minutes each to discuss and decide)

**Each turn, teams choose ONE action:**

### Action 1: Place a Server

**Cost:** Server cost (3-15 Budget)
**Effect:** Add server to infrastructure

**How It Works:**
1. Choose a server card
2. Decide which business services it will host
3. Pay the cost
4. Track remaining budget

**Example Turn:**
"We're placing a Domain Controller on-premises (12 Budget). It will host user identity and our SIEM system. Remaining budget: 38."

**Constraints:**
- Can't place a server type twice unless you have the budget for both
- Can't host a required service on a server that doesn't exist
- Can OVERLOAD servers (see Overload Mechanic below)

---

### Action 2: Add Security Device

**Cost:** Device cost (6-15 Budget)
**Effect:** Add network defense or monitoring

**How It Works:**
1. Choose a security device card
2. Describe which servers/zones it protects
3. Pay the cost
4. Track placement on network diagram

**Example Turn:**
"We're deploying a Firewall between our DMZ and Internal network (12 Budget). This blocks unauthorized traffic between zones. Remaining budget: 28."

---

### Action 3: Implement Network Architecture

**Cost:** Architecture cost (0-12 Budget)
**Effect:** Determine how servers logically connect

**How It Works:**
1. Choose one architecture type (only ONE per game)
2. Describe zone organization
3. Pay the cost
4. Document on network diagram

**Example Turn:**
"We're implementing a Segmented Network with 3 zones (5 Budget):
- DMZ: Email and Web servers (internet-facing)
- Internal: File servers and user workstations
- Sensitive: Database and Domain Controller
Remaining budget: 23."

---

### Action 4: Choose Hosting Model

**Cost:** Usually 0 (some cloud strategies cost money)
**Effect:** Determines where infrastructure physically lives

**How It Works:**
1. Decide on hosting strategy
2. Apply to appropriate servers
3. Document on infrastructure card
4. Pay if cloud-specific (usually free)

**Example Turn:**
"We're hosting our email and web servers on AWS (0 cost). Domain Controller stays on-premises. This reduces on-prem complexity but adds cloud management responsibility."

---

### Action 5: Pass / Skip Turn

**Cost:** 0
**Effect:** No action; preserve budget

**Use When:** Satisfied with current design or running low on budget

---

## The Overload Mechanic

### Strategic Tradeoff: Cost vs. Risk

**Problem:** Limited budget + mandatory services = imperfect solutions

**Solution:** Overload servers (put more services on one server than intended)

**How It Works:**
- If a server has capacity for 2 services, you can put 3+ on it
- **Benefit:** Save 3-15 Budget (don't need another server)
- **Risk:** Overloaded server is harder to isolate; compromise affects multiple services

**Example Scenario:**
"Budget remaining: 5. Still need to host Development Services.

Option A: Buy Dev Server for 5 (leaves 0 budget)
Option B: Put Dev on File Server (0 cost, overload by 1)

We choose B: File Server becomes (File Storage, Dev Services - OVERLOADED)"

**Consequences (Discovered Later):**
- Overloaded servers are easier to pivot from (when other modules investigate)
- If one service is compromised, ALL services on that server are at risk
- Recovery is harder (can't isolate just the compromised service)

---

## Vulnerability Gaps (Intentional and Accidental)

### How Budget Constraints Create Gaps

Teams inevitably leave security gaps:

| Gap Type | How It Happens | Cost Saved | Later Consequence |
|----------|-----------------|-----------|-------------------|
| **No Segmentation** | Too expensive (5-12) | 5-12 | All servers accessible after initial compromise |
| **No Firewall** | Too expensive (12) | 12 | Can't enforce zone boundaries |
| **Legacy Systems** | Cheap (3) | 7+ | Easy to exploit; unpatched vulnerabilities |
| **Overloaded Servers** | Budget pressure | 3-15 | Multi-service compromise; hard to isolate |
| **No Detection** (no IDS/SIEM) | Expensive (10-15) | 10-15 | Attacks undetected; investigations harder |
| **No Email Gateway** | Phishing defense (6) | 6 | Phishing easier in IR module |
| **No Honeypot** | Luxury item (7) | 7 | Attackers move silently |
| **All Cloud or All On-Prem** | Simplicity | 0 | Security model doesn't fit actual architecture |
| **No Backup System** | Expensive (9) | 9 | Ransomware = no recovery |
| **No SIEM** | Most expensive (15) | 15 | Investigation takes longer |

**Key Insight:** These gaps are discovered when other modules test the network (Audit, Incident Response, Disaster Recovery).

---

## Final Infrastructure Summary

### After Building Complete

Teams create an **Infrastructure Summary Card**:

```
YOUR NETWORK ARCHITECTURE

SERVERS DEPLOYED:
- Email Server (On-Prem) - Hosts: Email only
- Web Server (Cloud/AWS) - Hosts: Web + VPN
- Database Server (On-Prem) - Hosts: Customer Database
- File Server (On-Prem) - Hosts: File Storage, Dev Services (OVERLOADED 3/2)
- Domain Controller (On-Prem) - Hosts: Identity, SIEM (2/2)

ARCHITECTURE: Segmented (3 zones)
- DMZ: Email (On-Prem), Web (Cloud)
- Internal: File Server, Users
- Sensitive: Database, Domain Controller

SECURITY DEVICES:
- Firewall (DMZ ↔ Internal)
- IDS (Internal network)
- Email Gateway (incoming mail)
- SIEM (logging, investigation)
- NO IPS, NO Honeypot, NO Segmentation Switch

HOSTING: Hybrid (50% on-prem, 50% cloud)

BUDGET SPENT: 47/50 (3 remaining)

IDENTIFIED GAPS (for other modules):
- Overloaded File Server (multi-service risk)
- No IPS (web exploits pass through)
- No Honeypot (attackers move silently)
- Cloud servers not on private network
```

---

## Scoring & Network Assessment

### Infrastructure Quality Score

After building, teams receive a score reflecting their design choices:

| Metric | Score |
|--------|-------|
| **Budget Efficiency** | Budget Remaining / Starting Budget × 10 points |
| **Redundancy** | Multiple backup paths = +5 points |
| **Segmentation** | Implemented segmentation = +10 points |
| **Detection** | Deployed IDS/SIEM = +5 points |
| **Recovery** | Deployed backup system = +5 points |

**Example Scoring:**
- Budget remaining: 3/50 = 0.6 points
- Segmentation implemented: +10 points
- IDS + SIEM deployed: +5 points
- Backup system: +5 points
- **Total: ~20 points**

**Interpretation Tiers:**
- **30-40 points:** Enterprise-grade design; comprehensive protection
- **20-29 points:** Good design; most critical gaps covered
- **10-19 points:** Adequate design; some gaps remain
- **Below 10 points:** High risk; many gaps; future modules will be challenging

### Gap Registry

For use in Incident Response and Audit modules:
- List all identified gaps
- Note severity (CRITICAL, HIGH, MEDIUM, LOW)
- These gaps become modifiers when other modules test the network

---

## Integration with Other Modules

### Using Network Building as Context

When Network Building leads to other modules:

**→ Incident Response Module:**
- Network design determines which attacks are possible
- Overloaded servers make lateral movement easier
- Missing IDS/SIEM makes investigation harder

**→ Hardening Module:**
- Teams can see which network gaps they should fix
- Fixing a gap they identified = +2 bonus to that defense

**→ Disaster Recovery Module:**
- Network gaps increase crisis budget costs
- Overloaded servers = more data compromised
- No backup = no recovery option

**→ Audit & Compliance Module:**
- Pre-built network is audited against NIST/CIS
- Audit findings highlight network gaps
- Findings become modifiers in Incident Response

---

## Tips for Threat Orchestrators

### Before the Game

1. **Clarify business requirements** - Teams must provide email, web, database, file storage, identity, dev
2. **Show budget constraints** - 50 Budget is tight; teams will make difficult choices
3. **Emphasize consequences** - Choices made here affect all future modules
4. **Prepare Infrastructure Card template** - For documenting final network

### During Gameplay

1. **Ask clarifying questions** - "Why are you putting those two services together?"
2. **Point out overloads** - Track when servers exceed capacity
3. **Keep budget visible** - Announce remaining budget after each action
4. **Suggest trade-offs** - Help teams think through cost-benefit decisions

### After Building Complete

1. **Document gaps** - List all identified vulnerabilities
2. **Score the network** - Tell them how good/risky their design is
3. **Prepare for next module** - If continuing to Audit or IR, this network is the context
4. **Celebrate trade-offs** - "You saved budget on IPS, but web exploits will be riskier"

---

## Sample Scenarios

### Scenario 1: "Startup Network" (Beginner, 40 Budget)

**Constraint:** Very limited budget; must make hard choices

**Starting Narrative:**
"You're a startup with limited funding. You need to build infrastructure but can't afford everything. Choose wisely."

**Likely Outcome:**
- Flat network (save 5)
- Few security devices
- Multiple overloaded servers
- High vulnerability; good learning about consequences

---

### Scenario 2: "Mid-Market Expansion" (Standard, 50 Budget)

**Constraint:** Moderate budget; can afford some security

**Starting Narrative:**
"Your organization is growing. You have some budget for infrastructure but not unlimited. Balance growth with security."

**Likely Outcome:**
- Segmented network
- Basic security devices (firewall, email gateway, IDS or SIEM)
- Some overloading but manageable
- Moderate vulnerability; balanced design

---

### Scenario 3: "Enterprise Hardening" (Advanced, 60 Budget)

**Constraint:** Good budget; comprehensive design possible

**Starting Narrative:**
"You're rebuilding infrastructure with sufficient budget. Design for security AND resilience."

**Likely Outcome:**
- Segmented or isolated network
- Multiple security devices
- Minimal overloading
- Good security posture; few gaps

---

## Extensions & Variations

### Variation 1: Regulatory Compliance

Add compliance requirements:
- NIST CSF, CIS Controls, PCI-DSS, HIPAA
- Teams must choose devices that satisfy compliance
- Some devices count toward multiple requirements

---

### Variation 2: Business Department Negotiation

Assign roles:
- Finance wants cheap solutions
- Operations wants reliability
- Security wants defense-in-depth
- Teams must negotiate trade-offs

---

### Variation 3: Network Redesign

After Incident Response or Disaster Recovery:
- Teams rebuild network based on lessons learned
- Compare new design to original
- Measure improvement

---

## Quick Reference: Component Costs

| Component | Cost | Notes |
|-----------|------|-------|
| **Servers** | 3-12 | Higher cost = more capacity |
| **Devices** | 6-15 | Higher cost = more capability |
| **Architecture** | 0-12 | One per game; segmented is best balance |
| **Hosting** | 0-8 | Usually free; some cloud options cost |

---

## Need Help?

- **Questions about universal rules?** See [Core Rules](core-rules.md)
- **Want to combine modules?** See [Module Combinations](../module-combinations.md)
- **How does this integrate with Incident Response?** See [module-incident-response.md](module-incident-response.md)
- **How does this integrate with Audit & Compliance?** See [module-audit-compliance.md](module-audit-compliance.md)
- **Standalone play guide?** See [Standalone Play Guide](../standalone-games/network-building.md)

---

*Network Building Module - Rules & Mechanics*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.1 - Balanced & Refined Edition*
