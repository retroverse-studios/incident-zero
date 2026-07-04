# Disaster Recovery Module: Card Decks

This folder contains all card materials for the **Disaster Recovery Module** - where teams manage breach response and crisis communication under extreme pressure.

---

## Module Overview

**Disaster Recovery** is a module where:
- 1 Threat Orchestrator escalates the crisis
- 1+ Team(s) manage investigation, remediation, and stakeholder communication
- Teams win by managing the crisis, containing damage, and restoring trust
- Game clock (v2.2): 8 turns, each ~6-12 hours of narrative time (Turn 1 ≈ detection +6h, Turn 8 ≈ 72h)
- Duration: 30-45 minutes

---

## Card Decks

### Core Deck
**Files:** `core-deck/crisis-action-cards.md`, `core-deck/stakeholder-cards.md`, `core-deck/event-cards.md`

**Crisis Action Cards (13):**
- Investigation Actions (ACTION-01 to ACTION-04: forensics, threat hunting, logs, third-party IR)
- Remediation Actions (ACTION-05 to ACTION-08: patching, containment, rebuild, credential reset)
- Communication Actions (ACTION-09 to ACTION-12: customers, regulators, media, board)
- Crisis Decision (ACTION-13: Ransom Decision — Pay / Negotiate / Refuse) *(v2.2 — this is the "Negotiation Team" card promised in earlier editions)*
- Each with Budget cost and deterministic track advances

**Stakeholder Cards (5):**
- Customers (STAKE-01), Regulators (STAKE-02), Media/Public (STAKE-03), Board of Directors (STAKE-04), Executive Leadership (STAKE-05)
- Each with a 0-100% trust meter and escalation triggers

**Event Cards (12):**
- Scheduled Events (6 — placed on the 8-turn timeline at setup)
- Triggered Events (6 — resolve when their stated condition is met)
- Each moves the crisis forward and increases pressure

**Total:** 30 cards (13 Action + 12 Event + 5 Stakeholder). *(v2.1 shipped 29 — 12 Action + 12 Event + 5 Stakeholder; ACTION-13 makes 30.)*

**Best for:** Crisis management with 8 turns, ~30-45 minute gameplay

---

### Expansion Deck
**File:** `expansion-deck/advanced-scenarios.md`

Extends core deck with complex crisis situations:

**Advanced Scenario Cards:**
- Multi-region breaches
- Supply chain compromise with cascading effects
- Ransomware with extortion demands
- Nation-state attribution scenarios
- Media feeding frenzy situations
- Regulatory enforcement actions

**Total:** 8+ additional cards

**Best for:** Advanced gameplay with experienced crisis managers

---

## How Cards Are Used

### Crisis Action Cards
1. **Chosen by Blue Team** - Select ONE action each turn (plus the free Holding Statement rule and the ACTION-13 decision, which doesn't use the action slot)
2. **Cost Budget** - Each action has a resource cost; Budget floor is 0
3. **Advance Objectives** - Deterministic advances to Investigation %, Remediation %, or Communication % (optional Justification d20: 11+ = +5%)
4. **Create Cascading Effects** - Poor choices make later turns harder

### Stakeholder Cards
1. **Represent Affected Parties** - Visible on board
2. **Track Satisfaction/Trust** - Each stakeholder has a 0-100% trust meter
3. **Create Escalation Points** - Unhappy stakeholders trigger events
4. **Determine Victory/Defeat** - Any trust meter at 0% = immediate loss; otherwise the end-of-game Reputation tier table decides the outcome

### Event Cards (v2.2)
1. **Scheduled events** are placed on the timeline at setup and resolve at the start of their turn
2. **Triggered events** resolve when their stated condition is met (once each)
3. **Create Time Pressure** - Deadlines pinned to the 8-turn clock
4. **Trigger Escalations** - Major events increase stakeholder pressure

---

## Integration with Other Modules

### Incident Response → Disaster Recovery
- Use IR as lead-up to DR
- Assume IR was lost (attack succeeded)
- DR manages the breach response after detection failed

### Audit Findings → Disaster Recovery
- Audit findings create modifiers in DR
- Each failed audit domain subtracts from the DR starting budget (total penalty capped at -30, v2.2)
- Poor audit = DR becomes much more expensive

### Hardening → Disaster Recovery
- If hardening was successful, fewer critical systems are affected
- Speeds up recovery timeline
- Reduces escalation likelihood

### Network Building → Disaster Recovery
- Network design affects containment speed
- Well-segmented network = faster containment
- Flat network = cascading compromise

---

## Documentation Links

For rules on how to use these cards:
- **Module Rules:** `../../docs/rules/module-disaster-recovery.md`
- **Standalone Guide:** `../../docs/standalone-games/disaster-recovery.md`
- **Card Reference:** `../CARD_REFERENCE.md` (comprehensive index)

---

*Disaster Recovery Module: Card Decks*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.2 - Playtest Edition*
