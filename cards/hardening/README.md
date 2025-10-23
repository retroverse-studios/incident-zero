# Hardening Module: Card Decks

This folder contains all card materials for the **Hardening Module** - where teams build defense-in-depth and test defenses against simulated attacks.

---

## Module Overview

**Hardening** is a module where:
- 1 Blue Team designs and deploys security controls
- 1 Pentester (or Red Team) challenges those defenses
- Teams win by building layered, resilient defenses
- Duration: 20-45 minutes

---

## Card Decks

### Core Deck
**Files:** `core-deck/defense-cards.md`, `core-deck/pentester-tactic-cards.md`

**Defense Cards (24 cards - reused from Incident Response):**
- D-01 to D-24: Same security controls from IR module
- 3 tiers: BASIC (10 Budget), ADVANCED (15 Budget), ELITE (25 Budget)
- 6 threat vectors: SOCIAL_ENGINEERING, WEB_EXPLOIT, CREDENTIAL_ABUSE, MALWARE, NETWORK, DATA_EXFIL

**Pentester Tactic Cards (8 cards):**
- PT-01 to PT-08: Simulated red team attack tactics
- Attack vectors and evasion techniques
- Challenge defense deployments

**Total:** 32 cards

**Best for:** Defense-in-depth gameplay with 5-7 turn hardening phase

---

### Expansion Deck
**File:** `expansion-deck/advanced-tactics.md`

Extends core deck with advanced pentester tactics:

**Advanced Tactic Cards (8 cards):**
- Supply chain attack simulations
- Advanced persistence techniques
- Detection evasion tactics
- Zero-day exploitation scenarios

**Total:** 8 additional cards

**Best for:** Advanced gameplay with experienced blue teams

---

## How Cards Are Used

### Defense Cards
1. **Drawn by Blue Team** - Start with 5 cards, draw 1 per turn
2. **Deployed Against Threat Vectors** - Choose defense and place on board
3. **Cost Budget** - 10/15/25 depending on tier
4. **Provide Security Score** - 5 points per defense deployed

### Pentester Tactic Cards
1. **Drawn by Pentester/Red Team** - Mid-game challenges
2. **Challenge Deployed Defenses** - Team rolls to test if defenses hold
3. **Create Learning Moments** - When defenses fail, discuss why and how to improve
4. **Drive Iteration** - Teams may re-deploy or upgrade defenses in response

---

## Reusability Notes

### Defense Cards Shared with Incident Response
All 24 defense cards from the Incident Response core-deck are **directly reusable** in Hardening Module.

In Hardening:
- Same defense cards
- But Pentester Tactics test them in action
- Creates comprehensive defense-in-depth scenario

This means you only need ONE set of defense cards if playing both IR and Hardening.

### Pentester Tactic Cards NOT Shared
Tactic cards are specific to Hardening Module. Other modules don't use simulated red team attacks.

---

## Integration with Other Modules

### Incident Response → Hardening
- Play IR to identify threats
- Use same defense cards in Hardening
- Hardening helps build stronger defenses against discovered attacks

### Hardening → Disaster Recovery
- Use hardened network as baseline
- If hardening was successful, DR becomes easier
- If hardening was incomplete, DR becomes harder

---

## Documentation Links

For rules on how to use these cards:
- **Module Rules:** `../../docs/rules/module-hardening.md`
- **Standalone Guide:** `../../docs/standalone-games/hardening.md`
- **Card Reference:** `../CARD_REFERENCE.md` (comprehensive index)

---

*Hardening Module: Card Decks*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.1 - Balanced & Refined Edition*
