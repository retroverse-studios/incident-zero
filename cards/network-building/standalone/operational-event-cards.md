# Network Building Standalone: Operational Event Cards

**Version:** 2.2 - Playtest Edition
**Last Updated:** July 2026

---

## Overview

**Operational Event Cards** are the random incidents, windfalls, and headaches of running infrastructure. One card is revealed each turn (Phase 2) of the Network Building standalone game, right after the Business Requirement.

- **Total Cards:** 16 (EVT-01 to EVT-16)
- **Used In:** Network Building standalone game (one drawn per turn; 5-7 turns per game)
- **Effect Timing:** Resolve immediately unless the card says otherwise
- **Score Impact:** Point penalties/bonuses apply to the team's **final total score**; Budget changes apply to the budget tracker immediately (Budget can never go below 0)
- **Mitigation:** Each card lists which designs shrug it off — good architecture turns bad events into non-events

---

## Operational Event Cards

### EVT-01: Email Server Failure
**Type:** Outage
**Effect:** Your email server dies mid-quarter. Choose one:
- **Repair:** Pay 5 Budget (emergency callout)
- **Ignore:** **-10 points** (email down all quarter; users furious)
**Mitigated By:** A second Email Server, or email hosted on a Cloud Workload — the redundant/cloud service carries the load: no cost, no penalty
**No email service at all?** Nothing to break — but you already have bigger problems (see Capability scoring)

---

### EVT-02: Traffic Spike
**Type:** Load
**Effect:** Your product goes viral overnight. Public services are hammered.
- **Prepared** (Load Balancer, CDN, or a duplicated web service): **+5 points** (you rode the wave; sales boom)
- **Unprepared:** **-5 points** (site down during your biggest day)
**Mitigated By:** Load Balancer (8), CDN (expansion CLOUD-04), or redundant web hosting

---

### EVT-03: Phishing Wave
**Type:** Attack
**Effect:** A targeted phishing campaign hits every inbox in the company.
- **Email Gateway deployed:** **+5 points** (campaign filtered; nice catch)
- **No Email Gateway:** **-10 points** (three credential sets stolen)
**Mitigated By:** Email Gateway (6)

---

### EVT-04: Cloud Vendor Outage
**Type:** Outage
**Effect:** Your cloud provider has a region-wide outage this quarter.
- If any **required business service runs only in the cloud**: **-5 points** (service dark; SLA breached)
- Cloud services with an on-prem twin, or no cloud usage: no effect
**Mitigated By:** On-prem redundancy for cloud-hosted services, or an all-on-prem design
**Lesson:** Cloud is cheap, but concentration risk is real

---

### EVT-05: Budget Cut
**Type:** Finance
**Effect:** Fiscal crisis. **Lose 5 Budget immediately** (to a minimum of 0).
**Mitigated By:** Nothing — but teams holding a contingency reserve absorb it without changing plans

---

### EVT-06: Emergency Funds
**Type:** Finance
**Effect:** A surprise rebate lands. **Gain +10 Budget** (one time).
**Mitigated By:** N/A (enjoy it)

---

### EVT-07: Security Grant
**Type:** Finance
**Effect:** A government cyber-resilience grant is available to organizations with recoverable backups.
- **Backup Server deployed:** **Gain +5 Budget**
- **No Backup Server:** Nothing (you don't qualify)
**Mitigated By:** N/A — this one rewards good hygiene

---

### EVT-08: File Server Filling Up
**Type:** Capacity
**Effect:** Shared storage hits 98% full. Choose one this turn:
- **Add capacity:** Deploy any server to host file storage, or overload an existing server (+1 Budget per extra service)
- **Ignore:** **-5 points** (service degradation; work grinds)
**Mitigated By:** Spare capacity anywhere in your design (assign file storage to it at no cost)
**No file storage service at all?** No effect — and no file-storage capability either

---

### EVT-09: Honeypot Triggers
**Type:** Attack (Detected?)
**Effect:** Someone has been quietly probing your network.
- **Honeypot Decoy or Honeypot Network deployed:** **+5 points** (intruder caught red-handed in the decoy; access cut)
- **No honeypot:** Nothing visible happens. Nothing visible *ever* happens. (No penalty — this time)
**Mitigated By:** N/A — this is deception's payday

---

### EVT-10: Insider Snooping
**Type:** Attack
**Effect:** An employee is browsing systems far outside their role.
- **SIEM deployed OR network segmentation in place:** **+5 points** (caught early / blocked at the zone boundary)
- **Neither:** **-5 points** (months of quiet data access before anyone notices)
**Mitigated By:** SIEM (15) or Network Segmentation Switch (10) / segmented architecture

---

### EVT-11: Ransomware Strikes
**Type:** Attack (Severe)
**Effect:** Ransomware detonates on an internal system.
- **Backup Server deployed:** Pay 3 Budget for restore effort; if you also have detection (IDS/IPS/SIEM), you contained it fast: **+5 points**
- **No Backup Server:** **-20 points** (pay the ransom or lose the data — either way it's ugly)
**Mitigated By:** Backup Server (9); detection reduces blast radius

---

### EVT-12: IT Staff Burnout
**Type:** Operations
**Effect:** The ops team is running on fumes. **This turn you may deploy at most ONE component.** (Handling the turn's Business Requirement with an already-deployed component is fine.)
**Mitigated By:** Designs that are already complete — teams who front-loaded their build barely notice

---

### EVT-13: Vendor Promotion
**Type:** Opportunity
**Effect:** A security vendor is clearing stock. **The next security device you deploy this turn costs 2 less** (minimum cost 1).
**Mitigated By:** N/A — pure opportunity; skip it if nothing on the list fits your design

---

### EVT-14: New Hire Needs Remote Access
**Type:** Workforce
**Effect:** A key new hire works from another city and starts Monday.
- **VPN Gateway deployed:** No effect (onboarding is routine)
- **No VPN Gateway:** **-3 points** (they quit in week two, or worse: they improvise)
**Mitigated By:** VPN Gateway (9)

---

### EVT-15: Hardware Recall
**Type:** Outage
**Effect:** A vendor recalls a faulty component. Pick one of your on-prem servers (Threat Orchestrator picks if you won't):
- **Pay 3 Budget** for expedited replacement, OR
- That server is **offline this quarter** — any requirement it alone satisfies counts as unmet this turn
**Mitigated By:** Redundant servers or cloud-hosted twins (the twin covers the outage: no cost, no penalty). All-cloud designs are unaffected

---

### EVT-16: Quiet Quarter
**Type:** Respite
**Effect:** Nothing breaks. Nobody attacks. Finance leaves you alone. Use the breathing room to review your gaps.
**Mitigated By:** N/A

---

## Event Card Summary

| Card | Event | Effect (Unmitigated) | Mitigated By |
|------|-------|----------------------|--------------|
| EVT-01 | Email Server Failure | Pay 5 or -10 pts | Redundant/cloud email |
| EVT-02 | Traffic Spike | -5 pts (or +5 if ready) | LB / CDN / redundant web |
| EVT-03 | Phishing Wave | -10 pts (or +5 if ready) | Email Gateway |
| EVT-04 | Cloud Vendor Outage | -5 pts if cloud-only service | On-prem redundancy |
| EVT-05 | Budget Cut | -5 Budget | Contingency reserve |
| EVT-06 | Emergency Funds | +10 Budget | — |
| EVT-07 | Security Grant | +5 Budget if Backup | — |
| EVT-08 | File Server Filling Up | Buy capacity or -5 pts | Spare capacity |
| EVT-09 | Honeypot Triggers | +5 pts if honeypot | — |
| EVT-10 | Insider Snooping | -5 pts (or +5 if ready) | SIEM / segmentation |
| EVT-11 | Ransomware Strikes | -20 pts | Backup (+ detection: +5) |
| EVT-12 | IT Staff Burnout | Max 1 deploy this turn | Completed builds |
| EVT-13 | Vendor Promotion | Next device -2 cost | — |
| EVT-14 | New Hire Remote Access | -3 pts | VPN Gateway |
| EVT-15 | Hardware Recall | Pay 3 or server offline | Redundancy / cloud |
| EVT-16 | Quiet Quarter | Nothing | — |

---

## Gameplay Notes

### Draw Rules
- Shuffle all 16 cards at setup; draw **one per turn** face-up in Phase 2
- A 5-7 turn game uses 5-7 of the 16 cards
- **Advanced difficulty option:** remove EVT-06, EVT-07, and EVT-16 before shuffling (fewer breaks; matches the "disasters more frequent" rule)
- **Beginner difficulty option:** remove EVT-11 before shuffling

### Design Tension
Events reward the same things the scoring rewards — redundancy, detection, backups, and a contingency reserve — so mitigation is never wasted spend. The nastiest cards (EVT-11) are exactly why hoarding zero-reserve builds and backup-free builds both hurt.

---

## Print Instructions

1. Print on cardstock (250 gsm minimum)
2. Color-code by type:
   - **Red (Attack):** EVT-03, EVT-09, EVT-10, EVT-11
   - **Orange (Outage/Capacity):** EVT-01, EVT-04, EVT-08, EVT-15
   - **Blue (Finance/Operations):** EVT-05, EVT-06, EVT-07, EVT-12
   - **Green (Opportunity/Respite):** EVT-02, EVT-13, EVT-14, EVT-16
3. Cut along dotted lines
4. Shuffle into a single face-down deck for play

---

*Network Building Standalone: Operational Event Cards*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.2 - Playtest Edition*
