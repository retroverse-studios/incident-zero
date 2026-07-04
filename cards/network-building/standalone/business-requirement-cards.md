# Network Building Standalone: Business Requirement Cards

**Version:** 2.2 - Playtest Edition
**Last Updated:** July 2026

---

## Overview

**Business Requirement Cards** drive the Network Building standalone game. One card is revealed at the start of each turn (Phase 1) and represents what the business demands this quarter. Teams must satisfy the requirement by end of the stated deadline or take the score penalty.

- **Total Cards:** 20 (REQ-01 to REQ-20)
- **Used In:** Network Building standalone game (one drawn per turn; 5-7 turns per game)
- **Deadline:** End of the current turn unless the card says otherwise
- **Score Impact:** Penalties and bonuses are applied to the team's **final total score** (tracked on the score sheet as they occur)
- **Already satisfied counts:** If the team's existing infrastructure already meets the requirement, it is satisfied at no extra cost

---

## Business Requirement Cards

### REQ-01: New Product Launch Website
**Type:** Growth
**Requirement:** Marketing is launching a flagship product this quarter and needs a modern public website.
**Satisfied By:** Web Server (7), OR web service hosted on a Cloud Workload (4)
**Score Impact:** Missed: **-5 points** (launch flops; lost sales)

---

### REQ-02: Customer Data Acquisition
**Type:** Growth / M&A
**Requirement:** The executive team is acquiring a customer-data company. Two million customer records must land somewhere safe by end of quarter.
**Satisfied By:** Database Server (10), OR database service hosted on a Cloud Workload (4) — cloud-hosting the crown jewels is a recorded risk
**Score Impact:** Missed: **-10 points** (deal falls through)

---

### REQ-03: Work-From-Home Program
**Type:** Workforce
**Requirement:** HR is rolling out flexible work. Staff need secure remote access to internal systems.
**Satisfied By:** VPN Gateway (9)
**Score Impact:** Missed: **-3 points** (staff use risky workarounds; morale dips)

---

### REQ-04: Remote Workforce Mandate
**Type:** Workforce
**Requirement:** The board mandates support for a fully remote workforce: secure access AND central identity for every remote login.
**Satisfied By:** VPN Gateway (9) AND Domain Controller (12)
**Score Impact:** Missed: **-5 points** (shadow IT spreads across home offices)

---

### REQ-05: HIPAA Compliance Mandate
**Type:** Compliance
**Requirement:** A new healthcare client puts you in HIPAA scope. Regulators expect recoverable data and isolated sensitive systems.
**Satisfied By:** Backup Server (9) AND network segmentation (Network Segmentation Switch (10), or Segmented/Fully Isolated architecture)
**Score Impact:** Missed: **-10 points** (client walks; compliance exposure)

---

### REQ-06: PCI Scope: Cardholder Data
**Type:** Compliance
**Requirement:** You now process card payments. Cardholder data must live on a database that is walled off from the rest of the network.
**Satisfied By:** Database Server (10) or cloud-hosted database, AND a Firewall (12) or Network Segmentation Switch (10) protecting it
**Score Impact:** Missed: **-10 points** (acquirer threatens to pull card processing)

---

### REQ-07: 99.9% Uptime SLA
**Type:** Operations
**Requirement:** Your biggest customer signs a contract with a 99.9% uptime SLA on your public services. A single box is no longer good enough.
**Satisfied By:** Load Balancer (8), OR a second server duplicating any business-critical service (full price)
**Score Impact:** Missed: **-5 points** (SLA credits eat the margin)

---

### REQ-08: M&A: Integrate Acquired Network
**Type:** Growth / M&A
**Requirement:** The company you just bought needs its two core services absorbed into your infrastructure this quarter.
**Satisfied By:** Two free capacity slots across your existing servers, OR deploy any new server this turn to host them (overloading is allowed at +1 Budget per extra service)
**Score Impact:** Missed: **-10 points** (integration stalls; synergies evaporate)

---

### REQ-09: Scale Email System
**Type:** Operations
**Requirement:** Headcount doubled and the email system is groaning. Add headroom.
**Satisfied By:** Second Email Server (8), Load Balancer (8), OR email hosted on a Cloud Workload (4)
**Score Impact:** Missed: **-5 points** (mail delays; missed customer requests)

---

### REQ-10: Security Audit Ordered
**Type:** Compliance
**Requirement:** The audit committee orders an independent security audit. Auditors expect centralized visibility of security events.
**Satisfied By:** SIEM (15), OR both IDS (10) and Email Gateway (6)
**Score Impact:** Missed: **-5 points** (qualified audit opinion)

---

### REQ-11: Board Demands IR Readiness
**Type:** Security
**Requirement:** A competitor's breach is front-page news. The board demands demonstrable incident-detection capability.
**Satisfied By:** IDS (10), IPS (14), OR SIEM (15)
**Score Impact:** Missed: **-10 points** (board censure; CISO on thin ice)

---

### REQ-12: Ransomware Wave in Sector
**Type:** Security
**Requirement:** A ransomware variant is tearing through your industry. You need recoverable backups AND a way to spot the attack.
**Satisfied By:** Backup Server (9) AND at least one of IDS (10) / IPS (14) / SIEM (15)
**Score Impact:** Missed: **-20 points** (you are one bad click from catastrophe)

---

### REQ-13: New Subsidiary Office
**Type:** Growth
**Requirement:** A new regional office opens with no local infrastructure. Staff there must reach head-office systems securely.
**Satisfied By:** VPN Gateway (9)
**Score Impact:** Missed: **-5 points** (office runs on personal email and USB sticks)

---

### REQ-14: E-Commerce Expansion
**Type:** Growth
**Requirement:** Sales moves online. You need a public web presence AND protection against the web attacks that come with taking payments.
**Satisfied By:** Web Server (7) or cloud-hosted web, AND WAF (11)
**Score Impact:** Missed: **-5 points** (checkout is either absent or a breach waiting to happen)

---

### REQ-15: Developer Hiring Spree
**Type:** Workforce
**Requirement:** Engineering triples in size. Developers need somewhere to build and test that is not production.
**Satisfied By:** Development Server (5), OR dev services overloaded onto an existing server (+1 Budget per extra service — allowed)
**Score Impact:** Missed: **-3 points** (developers test in production; incidents follow)

---

### REQ-16: Records-Retention Regulation
**Type:** Compliance
**Requirement:** New regulation requires seven-year retention of business records: durable shared storage plus a recoverable copy.
**Satisfied By:** File storage (File Server (6), or hosted on another server's capacity/overload) AND Backup Server (9)
**Score Impact:** Missed: **-5 points** (regulator issues a compliance notice)

---

### REQ-17: Single Sign-On Rollout
**Type:** Operations
**Requirement:** Password chaos across a dozen apps. Leadership wants one identity for everything.
**Satisfied By:** Domain Controller (12)
**Score Impact:** Missed: **-5 points** (password reuse everywhere; helpdesk drowning)

---

### REQ-18: Cyber-Insurance Renewal
**Type:** Security
**Requirement:** Your insurer's renewal questionnaire wants proof of backups, phishing defense, and detection.
**Satisfied By:** Backup Server (9) AND Email Gateway (6) AND at least one of IDS/IPS/SIEM
**Score Impact:** Met: **+5 points** (premium drops). Missed: **-5 points** (premium spikes)

---

### REQ-19: Threat-Intel Pilot
**Type:** Security (Opportunity)
**Requirement:** Your ISAC offers to feature any member running deception technology in its quarterly report.
**Satisfied By:** Honeypot Decoy (7) or Honeypot Network (8)
**Score Impact:** Met: **+5 points** (industry kudos). Missed: **0 points** (opportunity passes; no penalty)

---

### REQ-20: Data-Center Consolidation
**Type:** Operations (Opportunity)
**Requirement:** Finance wants the server-room footprint shrunk. Show that at least one business service runs in the cloud.
**Satisfied By:** Any service hosted on a Cloud Workload (4)
**Score Impact:** Met: **+3 points** (opex savings). Missed: **-3 points** (facilities costs balloon)

---

## Requirement Card Summary

| Card | Requirement | Satisfied By | Missed | Met Bonus |
|------|-------------|--------------|--------|-----------|
| REQ-01 | Product Launch Website | Web Server or cloud web | -5 | — |
| REQ-02 | Customer Data Acquisition | Database (dedicated or cloud) | -10 | — |
| REQ-03 | Work-From-Home Program | VPN Gateway | -3 | — |
| REQ-04 | Remote Workforce Mandate | VPN Gateway + Domain Controller | -5 | — |
| REQ-05 | HIPAA Compliance | Backup + segmentation | -10 | — |
| REQ-06 | PCI Cardholder Data | Database + Firewall/Segmentation | -10 | — |
| REQ-07 | 99.9% Uptime SLA | Load Balancer or duplicate server | -5 | — |
| REQ-08 | M&A Network Integration | 2 spare slots or new server | -10 | — |
| REQ-09 | Scale Email System | 2nd Email Server / LB / cloud email | -5 | — |
| REQ-10 | Security Audit | SIEM, or IDS + Email Gateway | -5 | — |
| REQ-11 | IR Readiness | IDS, IPS, or SIEM | -10 | — |
| REQ-12 | Ransomware Wave | Backup + detection | -20 | — |
| REQ-13 | New Subsidiary Office | VPN Gateway | -5 | — |
| REQ-14 | E-Commerce Expansion | Web + WAF | -5 | — |
| REQ-15 | Developer Hiring Spree | Dev Server or overload | -3 | — |
| REQ-16 | Records Retention | File storage + Backup | -5 | — |
| REQ-17 | Single Sign-On | Domain Controller | -5 | — |
| REQ-18 | Cyber-Insurance Renewal | Backup + Email Gateway + detection | -5 | +5 |
| REQ-19 | Threat-Intel Pilot | Honeypot | 0 | +5 |
| REQ-20 | Data-Center Consolidation | Any cloud-hosted service | -3 | +3 |

---

## Gameplay Notes

### Draw Rules
- Shuffle all 20 cards at setup; draw **one per turn** face-up in Phase 1
- A 5-7 turn game uses 5-7 of the 20 cards — every game sees a different mix
- For a gentler Beginner game, the Threat Orchestrator may pre-seed the deck (remove REQ-12 and one other -10 card)

### Design Tension
Requirements are deliberately lumpy: some are satisfied by things every sane design already has (web, database), others punish narrow builds (detection, deception, redundancy). Teams that spend everything in turn 1 have no reserve when REQ-12 lands.

---

## Print Instructions

1. Print on cardstock (250 gsm minimum)
2. Color-code by type:
   - **Green (Growth/M&A):** REQ-01, REQ-02, REQ-08, REQ-13, REQ-14
   - **Blue (Workforce/Operations):** REQ-03, REQ-04, REQ-07, REQ-09, REQ-15, REQ-17, REQ-20
   - **Orange (Compliance):** REQ-05, REQ-06, REQ-10, REQ-16
   - **Red (Security):** REQ-11, REQ-12, REQ-18, REQ-19
3. Cut along dotted lines
4. Shuffle into a single face-down deck for play

---

*Network Building Standalone: Business Requirement Cards*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.2 - Playtest Edition*
