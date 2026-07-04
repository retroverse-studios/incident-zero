# Network Building Module: Card Decks

This folder contains all card materials for the **Network Building Module** - where teams design IT infrastructure with trade-offs between cost, complexity, and security.

---

## Module Overview

**Network Building** is a module where:
- 1+ Team(s) design network infrastructure from scratch
- Each component (servers, devices, architecture) has cost/benefit trade-offs
- Teams win by meeting business requirements within budget constraints
- Duration: 30-45 minutes (standalone, including setup and scoring)

---

## Card Decks

### Core Deck
**Files:** `core-deck/server-cards.md`, `core-deck/security-device-cards.md`, `core-deck/architecture-cards.md`, `core-deck/asset-cards.md`

**Server Cards (10 cards):**
- Email Server, Web Server, Database Server, File Server
- Domain Controller, Development Server, Backup Server
- Cloud Workload, Legacy System, Honeypot Decoy
- Each with cost, complexity, and security properties

**Security Device Cards (10 cards):**
- Firewall, IDS/IPS, Load Balancer, VPN Gateway
- Email Gateway, Web Application Firewall (WAF)
- Network Segmentation Switch, SIEM, Honeypot Network
- Each with cost, effectiveness, and deployment considerations

**Architecture Cards (5 cards):**
- Flat Network (cheap, simple, risky)
- Segmented 3-Zone (balanced cost/security)
- Fully Isolated (expensive, very secure)
- Cloud Hybrid (mix of on-prem and cloud)
- Cloud First (modern, low overhead)

**Asset/Business Requirement Cards (8 cards):**
- Email, Web Presence, Database, File Storage
- Identity/Authentication, Development, Disaster Recovery, VPN Access
- Each represents a business requirement that must be met

**Total:** 33 cards

**Best for:** Network design with 5 build turns (any number of placements per turn), ~30-45 minute session

---

### Standalone Deck (v2.2)
**Files:** `standalone/business-requirement-cards.md`, `standalone/operational-event-cards.md`

Drives the competitive standalone game (one of each drawn per turn):

**Business Requirement Cards (20 cards, REQ-01 to REQ-20):**
- Random quarterly business needs (product launches, M&A integration, PCI/HIPAA scope, uptime SLAs, remote workforce, ransomware readiness...)
- Each names the requirement, what satisfies it, and the score impact

**Operational Event Cards (16 cards, EVT-01 to EVT-16):**
- Random incidents and windfalls (outages, traffic spikes, phishing waves, vendor outages, budget cuts and grants...)
- Each states its effect and which designs mitigate it

**Total:** 36 cards

**Best for:** The standalone infrastructure design competition (see `../../docs/standalone-games/network-building.md`)

---

### Expansion Deck
**Files:** `expansion-deck/legacy-systems.md`, `expansion-deck/cloud-variants.md`

Extends core deck with specialized systems:

**Legacy System Cards (4 cards, LEGACY-01 to LEGACY-04):**
- Mainframe System
- Custom Business Application (vendor extinct)
- Industrial Control System (ICS)
- Obsolete Operating System

**Cloud Variant Cards (4 cards, CLOUD-01 to CLOUD-04):**
- Containerized Microservices (Kubernetes-style orchestration)
- Serverless / Function-as-a-Service
- Database-as-a-Service (managed database)
- Content Delivery Network (CDN)

**Total:** 8 additional cards

**Best for:** Complex scenarios with legacy infrastructure or cloud-native deployments

---

## How Cards Are Used

### Server Cards
1. **Selected by Team** - Choose which servers to deploy
2. **Cost Varies** - Each has different Budget cost
3. **Meets Business Requirements** - Must include servers needed for each Asset Card
4. **Creates Complexity** - More servers = more to defend/manage

### Security Device Cards
1. **Added to Network** - Placed between network segments
2. **Increases Cost** - Each device has Budget cost
3. **Reduces Vulnerabilities** - Devices protect against specific attack vectors
4. **Increases Complexity** - Must monitor and maintain

### Architecture Cards
1. **One Selected** - Team chooses ONE architecture pattern
2. **Shapes Network Layout** - Determines server placement and communication
3. **Sets Budget Constraints** - Architecture determines available Budget
4. **Affects Subsequent Modules** - Network design impacts Incident Response difficulty

### Asset Cards
1. **Requirements to Meet** - Represent business needs
2. **Must Be Satisfied** - Team must provide servers/services for each
3. **Drive Design** - Architects network around business assets

---

## Reusability Notes

### Asset Cards May Be Shared
Asset Cards (Email, Database, Web Server, etc.) may be referenced in:
- Network Building (component selection)
- Incident Response (asset names in clues)
- Disaster Recovery (what was affected)

### Server/Device Cards NOT Shared
Server and Security Device cards are specific to Network Building. Other modules don't use physical infrastructure selection.

---

## Integration with Other Modules

### Network Building → Incident Response
- Built network becomes the "target" in IR
- Poor network design makes IR harder (more attack surface)
- Good network design with segmentation makes IR easier to contain

### Network Building → Hardening
- Designed network is baseline for hardening
- Teams deploy defenses ON the built infrastructure
- Affects which defenses are available

### Network Building → Audit
- Built network is audited for compliance
- Poor design may have audit findings that apply to IR/DR

---

## Documentation Links

For rules on how to use these cards:
- **Module Rules:** `../../docs/rules/module-network-building.md`
- **Standalone Guide:** `../../docs/standalone-games/network-building.md`
- **Card Reference:** `../CARD_REFERENCE.md` (comprehensive index)

---

*Network Building Module: Card Decks*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.2 - Playtest Edition*
