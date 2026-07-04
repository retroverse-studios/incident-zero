# Network Building Module: Rules & Mechanics

**Version:** 2.2 - Playtest Edition
**Last Updated:** July 2026

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
| **Beginner** | 60 | Learning networks; roomier budget, easier trade-offs |
| **Standard** | 50 | Balanced play, typical scenario |
| **Advanced** | 40 | Tight budget; hard trade-offs, strategic depth |

**Budget represents:** Time, money, and resources for infrastructure design

**(v2.2)** More budget = easier. Beginner gets the most budget; Advanced gets the least.

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
| **Backup Server** | 9 | 1 | Data backup | Should be isolated; ransomware recovery |
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
| **VPN Gateway** | 9 | Remote access | Enables secure remote work; attack surface if weak |
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

#### Category 4: Business Requirements (v2.2)

Teams MUST satisfy every **Required** item by end of game. **Recommended** items are not mandatory, but skipping one is recorded as a gap (and costs points at scoring).

| Requirement | Status | Satisfied By | Notes |
|------------|--------|--------------|-------|
| **Email** | Required | Email Server, OR hosted on a Cloud Workload | Non-negotiable |
| **Web Presence** | Required | Web Server, OR hosted on a Cloud Workload | Online business |
| **Customer Database** | Required | Database Server, OR hosted on a Cloud Workload | Cloud-hosting the crown jewels is a recorded risk |
| **User Identity (AD/Kerberos)** | Required | Domain Controller | No substitute |
| **Disaster Recovery (Backup)** | Required (v2.2) | Backup Server | No backup = automatic FAIL on this requirement, recorded as a CRITICAL gap (not an instant game loss) |
| **File Storage** | Recommended (v2.2) | File Server, OR spare capacity/overload on another server | Gap if missing |
| **Development/Testing** | Recommended (v2.2) | Dev Server, OR overload another server | Overloading a server for dev is explicitly allowed |
| **Remote Work VPN** | Recommended (v2.2) | VPN Gateway | Gap if missing: risky remote-access workarounds |

**Key Rule:** Required items are fixed. Teams must find places to host them, even if it means cloud-hosting or overloading servers.

**Affordability Check (v2.2)** — the Required list fits every difficulty:

- **Dedicated servers for every Required item:** Email 8 + Web 7 + Database 10 + Domain Controller 12 + Backup 9 = **46** → affordable at Standard (50, leaves 4) and Beginner (60, leaves 14)
- **Advanced (40):** cloud-host Email + Web on one Cloud Workload (4): 4 + 10 + 12 + 9 = **35** (leaves 5). Hosting the Database on a second Cloud Workload drops it to **29** (leaves 11) — cheap, but every substitution is a recorded gap
- File Storage can ride the Domain Controller's spare capacity slot (free) or overload any server (+1 Budget)

#### Category 5: Hosting Model

Physical location of infrastructure:

| Model | Cost | Notes |
|-------|------|-------|
| **Self-Hosted (On-Premises)** | 0 | Team controls; responsibility for patching |
| **Cloud-Hosted (AWS/Azure/GCP)** | 0 | Provider controls; less direct control |
| **Hybrid** | 0 | Mix of on-prem and cloud; complex |

---

## Gameplay Loop (15-20 minutes)

### Turn Structure (v2.2)

**Teams take 5 "Build Turns"** (~3-4 minutes each to discuss and decide).

**Each turn is a design-review phase (v2.2):** the team may take **any number of actions** — place as many components as they can afford — before ending the turn. Turns are not a one-purchase limit; they are checkpoints where the design gets stress-tested.

**Between turns**, the Threat Orchestrator reveals a development: draw one Operational Event or Business Requirement card from the standalone decks (`cards/network-building/standalone/`), or narrate one (a stakeholder demand, a vendor issue, a budget change). This gives teams a reason to revisit the design each turn.

**Available actions:**

### Action 1: Place a Server

**Cost:** Server cost (3-12 Budget)
**Effect:** Add server to infrastructure

**How It Works:**
1. Choose a server card
2. Decide which business services it will host
3. Pay the cost
4. Track remaining budget

**Example:**
"We're placing a Domain Controller on-premises (12 Budget). It will host user identity, with a spare capacity slot for file storage. Remaining budget: 38."

**Constraints:**
- **Duplicates allowed (v2.2):** you may deploy more than one server of the same type; each copy costs full price
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
"We're deploying a Firewall between our DMZ and Internal network (12 Budget). This blocks unauthorized traffic between zones. Remaining budget: 26."

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
Remaining budget: 21."

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

### Action 5: End Turn / Pass

**Cost:** 0
**Effect:** Take no further actions this turn; preserve budget

**Use When:** Satisfied with current design or holding budget in reserve for surprises

---

## The Overload Mechanic

### Strategic Tradeoff: Cost vs. Risk

**Problem:** Limited budget + mandatory services = imperfect solutions

**Solution:** Overload servers (put more services on one server than intended)

**How It Works (v2.2):**
- If a server has capacity for 2 services, you can put 3+ on it
- **Cost:** +1 Budget per extra service beyond capacity (paid when the service is added)
- **Benefit:** Still far cheaper than buying another server
- **Risk:** Overloaded server is harder to isolate; compromise affects multiple services

**Example Scenario:**
"Budget remaining: 5. Still need to host Development Services.

Option A: Buy Dev Server for 5 (leaves 0 budget)
Option B: Put Dev on our File Server, which already hosts File Storage and Email Backup (2/2). Overload by 1: pay 1 Budget (leaves 4)

We choose B: File Server becomes (File Storage, Email Backup, Dev Services — OVERLOADED 3/2)"

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
| **Overloaded Servers** | Budget pressure | 2-11 (server cost minus overload fees) | Multi-service compromise; hard to isolate |
| **No Detection** (no IDS/SIEM) | Expensive (10-15) | 10-15 | Attacks undetected; investigations harder |
| **No Email Gateway** | Phishing defense (6) | 6 | Phishing easier in IR module |
| **No Honeypot** | Luxury item (7) | 7 | Attackers move silently |
| **All Cloud or All On-Prem** | Simplicity | 0 | Security model doesn't fit actual architecture |
| **No Backup Server** | Expensive (9) | 9 | Automatic FAIL on the Disaster Recovery requirement |
| **No SIEM** | Most expensive (15) | 15 | Investigation takes longer |

**Key Insight:** These gaps are discovered when other modules test the network (Audit, Incident Response, Disaster Recovery).

---

## Final Infrastructure Summary

### After Building Complete

Teams create an **Infrastructure Summary Card**:

```
YOUR NETWORK ARCHITECTURE (Standard, 50 Budget)

SERVERS DEPLOYED:
- Cloud Workload (AWS) - Hosts: Email + Web (2/2, cloud-hosted)
- Database Server (On-Prem) - Hosts: Customer Database
- Domain Controller (On-Prem) - Hosts: Identity, File Storage,
  Dev Services (OVERLOADED 3/2, +1 Budget paid)
- Backup Server (On-Prem, isolated) - Hosts: Backups / DR

ARCHITECTURE: Segmented (3 zones)
- DMZ: (cloud workload fronts the internet)
- Internal: Users
- Sensitive: Database, Domain Controller, Backup Server

SECURITY DEVICES:
- Email Gateway (incoming mail)
- NO Firewall, NO IDS/SIEM, NO VPN Gateway, NO Honeypot

HOSTING: Hybrid (cloud front end, on-prem crown jewels)

BUDGET SPENT: 47/50 (3 remaining)
- Cloud Workload 4 + Database 10 + Domain Controller 12 + Backup 9
  + Segmented Architecture 5 + Email Gateway 6 + Overload 1 = 47

IDENTIFIED GAPS (for other modules):
- Overloaded Domain Controller (identity + files + dev on one box)
- No IDS/SIEM (attacks undetected; investigations harder)
- No VPN Gateway (remote workers use risky workarounds)
- Email and Web share one cloud workload (single point of failure)
```

---

## Scoring & Network Assessment

### Infrastructure Quality Score (v2.2)

After building, teams receive a score reflecting their design choices:

| Metric | Score |
|--------|-------|
| **Requirements** | +2 per Required item satisfied (Email, Web, Database, Identity, Backup) — max +10 |
| **Segmentation** | Implemented Segmented or Fully Isolated architecture = +10 |
| **Detection** | Deployed IDS, IPS, or SIEM = +5 |
| **Recovery** | Deployed Backup Server = +5 |
| **Redundancy** | Duplicated a critical server or deployed a Load Balancer = +5 |
| **Contingency Reserve** | 5-15 Budget remaining = +5; 1-4 remaining = +2; 0 or 16+ remaining = 0 |

**Maximum: 40 points.** The reserve bonus rewards smart utilization — meet the requirements *and* keep a small cushion; hoarding budget scores nothing.

**Example Scoring (the sample network above, Standard 50):**
- All 5 Required items satisfied: +10
- Segmentation implemented: +10
- No IDS/IPS/SIEM: 0
- Backup Server deployed: +5
- No redundancy: 0
- 3 Budget remaining: +2
- **Total: 27 points — Good design**

**Interpretation Tiers (v2.2):**
- **32-40 points:** Enterprise-grade design; comprehensive protection
- **22-31 points:** Good design; most critical gaps covered
- **12-21 points:** Adequate design; some gaps remain
- **Below 12 points:** High risk; many gaps; future modules will be challenging

*Reachability check: at Beginner (60), a team can score the full 40 — e.g., Cloud Workload 4 (Email+Web) + Database 10 + Domain Controller 12 (Identity + File) + Backup 9 + Segmented 5 + IDS 10 + second Cloud Workload 4 (redundant web) = 54 spent, 6 remaining → 10+10+5+5+5+5 = 40.*

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

1. **Clarify business requirements** - Teams must provide email, web, database, identity, and backup (file storage, dev, and VPN are recommended)
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

### Scenario 1: "Startup Network" (Advanced, 40 Budget)

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

### Scenario 3: "Enterprise Hardening" (Beginner, 60 Budget)

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
| **Servers** | 3-12 | Higher cost = more critical function |
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

## v2.2 Playtest Edition Changes

Summary of rule changes for playtesters (all labelled "(v2.2)" in the text above):

1. **Difficulty direction fixed:** more budget = easier. Beginner 60 / Standard 50 / Advanced 40 (previously Beginner had the *least* budget).
2. **Action economy fixed:** each Build Turn, teams may place **any number** of components they can afford. Turns are design-review checkpoints; between turns the TO reveals an Operational Event or Business Requirement (see the standalone decks in `cards/network-building/standalone/`). Previously 5 turns × 1 action made the mandatory requirements physically impossible to place.
3. **Requirement list rebalanced:** Required = Email, Web, Database, Identity, Disaster Recovery (Backup). Recommended = File Storage, Development, Remote Work VPN. Backup is now Required (missing backup = automatic FAIL on that requirement, not an instant game loss). Development is Recommended and may be hosted by overloading. Email/Web/Database may be cloud-hosted on Cloud Workloads, which keeps the Required list affordable even at Advanced (40): dedicated build = 46; cloud-assisted builds = 35 or 29.
4. **Overload now costs +1 Budget per extra service** beyond capacity (was free). Matches the standalone game.
5. **Duplication rule:** multiple servers of the same type are allowed; each costs full price (replaces the old vacuous "unless you have the budget for both" wording).
6. **Scoring rescaled:** new Requirements metric (+2 each, max 10), Contingency Reserve bonus (+5 for finishing with 5-15 Budget — smart utilization, not hoarding), and tiers rescaled to reachable bands (32-40 / 22-31 / 12-21 / <12). Max score 40 is verified reachable at Beginner.
7. **Terminology unified:** "VPN Gateway" (was VPN Concentrator) and "Backup Server" (was Backup System) everywhere.
8. **Examples corrected:** the sample Infrastructure Summary and all in-text budget arithmetic now add up.

---

*Network Building Module - Rules & Mechanics*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.2 - Playtest Edition*
