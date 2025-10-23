# Incident Response Module: Card Decks

This folder contains all card materials for the **Incident Response Module** - the foundation of Incident Zero where teams detect and investigate hidden attack chains.

---

## Module Overview

**Incident Response** is a single-module game where:
- 1 Threat Orchestrator creates a hidden 3-5 card attack chain
- 1+ Blue Team(s) investigate and deploy defenses to reveal cards
- Teams win by revealing all cards before budget/turns run out
- Duration: 30-45 minutes

---

## Card Decks

### Core Deck
**File:** `core-deck/threat-defense-cards.md`

Contains the essential cards needed to play Incident Response:

**Threat Cards (12 base cards):**
- T-01 to T-12: Complete attack chain examples
- Organized by attack chain step: INITIAL COMPROMISE, PIVOT & ESCALATE, PERSISTENCE, C2 & EXFIL
- 6 attack vectors: SOCIAL_ENGINEERING, WEB_EXPLOIT, CREDENTIAL_ABUSE, MALWARE, NETWORK, DATA_EXFIL

**Defense Cards (24 base cards):**
- D-01 to D-24: Security controls and countermeasures
- Organized by threat vector
- 3 tiers: BASIC (10 Budget), ADVANCED (15 Budget), ELITE (25 Budget)
- Deployment costs and descriptions included

**Total:** 36 cards

**Best for:** Standard gameplay with 3-4 card attack chains

---

### Expansion Deck
**Files:**
- `expansion-deck/advanced-threats.md` (8 additional threat cards)
- `expansion-deck/advanced-defenses.md` (8 additional defense cards)

Extends the core deck with more sophisticated attack scenarios:

**Advanced Threat Cards (8 cards):**
- Supply chain attacks
- Advanced persistence techniques
- Nation-state level attacks
- Specialized vectors (mobile, IoT, cloud-native)

**Advanced Defense Cards (8 cards):**
- Elite-tier security controls
- Advanced monitoring and detection
- Forensics and threat hunting capabilities

**Total:** 16 additional cards

**Best for:** Advanced gameplay with 5+ card chains or expert player groups

---

## How Cards Are Used

### Threat Cards
1. **Hidden by Threat Orchestrator** - Create attack chain before game starts
2. **Revealed by Blue Team** - Through successful investigations or defense deployments
3. **Cost Budget via Uncontained Threats** - Each revealed threat costs 5 Budget/turn
4. **Contains Clues** - TO reads clues to guide investigations

### Defense Cards
1. **Drawn by Blue Team** - Start with 5 cards, draw 1 per turn
2. **Deployed Against Threats** - Choose defense and roll 11+ to deploy
3. **Cost Budget** - 10/15/25 depending on tier
4. **Reveal Threats** - If defense matches threat's vector and chain step

---

## Deck Composition

### Core Deck Distribution

**Threat Cards by Vector:**
- SOCIAL_ENGINEERING: 2 cards
- WEB_EXPLOIT: 2 cards
- CREDENTIAL_ABUSE: 2 cards
- MALWARE: 2 cards
- NETWORK: 1 card
- DATA_EXFIL: 1 card
- MULTI-VECTOR: 2 cards (apply to multiple vectors)

**Threat Cards by Chain Step:**
- INITIAL COMPROMISE: 3 cards (entry point attacks)
- PIVOT & ESCALATE: 5 cards (lateral movement, privilege escalation)
- PERSISTENCE: 2 cards (maintaining access)
- C2 & EXFIL: 2 cards (command & control, data theft)

**Defense Cards by Vector:**
- SOCIAL_ENGINEERING defenses: 4 cards
- WEB_EXPLOIT defenses: 4 cards
- CREDENTIAL_ABUSE defenses: 4 cards
- MALWARE defenses: 4 cards
- NETWORK defenses: 4 cards
- DATA_EXFIL defenses: 4 cards

**Defense Cards by Tier:**
- BASIC (10 Budget): 8 cards
- ADVANCED (15 Budget): 8 cards
- ELITE (25 Budget): 8 cards

---

## Sample Attack Chains

The core deck supports these classic scenarios:

### 3-Card Chain (Beginner, 30 min)
- Phishing → Credential Dumping → Database Exfil
- Simple kill chain, teaches basics

### 4-Card Chain (Intermediate, 40 min)
- Phishing → Lateral Movement → Privilege Escalation → C2 Beaconing
- Adds complexity and lateral movement

### 5-Card Chain (Advanced, 45 min)
- Supply Chain Compromise → Lateral Movement → Persistence → Credential Theft → Exfil
- Full sophistication with multiple detection points

---

## Printing & Playing

### Physical Cards
1. Print `core-deck/threat-defense-cards.md` on cardstock
2. Cut along marked lines
3. Use for face-to-face gameplay
4. Optionally laminate for durability

### Digital Play
1. Keep cards in document
2. Reference during game
3. Mark revealed cards as you play
4. No printing needed

### Print Template
See `../print-templates/` for:
- A4 sheet layouts (multiple cards per page)
- Card template specifications
- Cutting guides
- Color recommendations

---

## Expansion Deck Strategy

### When to Use Advanced Threats
- Playing with experienced groups
- Want more sophisticated attack scenarios
- Need 5+ card chains
- Require modern threat landscape (supply chain, cloud, etc.)

### When to Use Advanced Defenses
- Teams are struggling with basic defenses
- Want more variety in control options
- Need specialized defenses (forensics, threat hunting)
- Playing with advanced rules

---

## Card Reusability

### Defense Cards Shared with Hardening Module
All 24 defense cards from the core deck are directly reusable in the **Hardening Module**.

In Hardening:
- Teams deploy same defense cards
- But Hardening adds Pentester Tactics to test them
- Creates more complex scenario

This means you only need ONE set of defense cards if playing both modules.

### Threat Cards NOT Shared
Threat cards are specific to Incident Response. Other modules don't use attack chains:
- Hardening tests defenses against tactics, not specific threat cards
- Disaster Recovery assumes attack already succeeded
- Network Building and Audit don't use threat cards

---

## Modifications & Custom Cards

### Creating Custom Threat Cards
Follow this format:
```
TITLE: [Memorable attack name]
Step: [INITIAL COMPROMISE / PIVOT & ESCALATE / PERSISTENCE / C2 & EXFIL]
Vector: [SOCIAL_ENGINEERING / WEB_EXPLOIT / CREDENTIAL_ABUSE / MALWARE / NETWORK / DATA_EXFIL]
Cost: 5 Budget (standard)

CLUE FOR TO:
[Progressive disclosure about what the attack is doing]

WHY THIS WORKS:
[Educational explanation of the attack technique]
[Real-world examples if applicable]
```

### Creating Custom Defense Cards
Follow this format:
```
TITLE: [Defense control name]
Tier: [BASIC / ADVANCED / ELITE]
Cost: [10 / 15 / 25] Budget (corresponding to tier)
Vector: [Which threat vector it counters]

DESCRIPTION:
[What the defense does and when it applies]
[Which attacks it helps protect against]
```

---

## Integration with Other Modules

### Incident Response → Hardening
- Play IR to identify threats
- Use same defense cards in Hardening
- Hardening helps you build stronger defenses

### Incident Response → Disaster Recovery
- Use IR as lead-up to DR
- Assume IR was lost (attack succeeded)
- DR manages the breach response

### Incident Response → Audit
- Play Audit first to identify network gaps
- Gaps become IR modifiers
- IR becomes harder/easier based on audit

---

## Documentation Links

For rules on how to use these cards:
- **Core Rules:** `../../docs/rules/core-rules.md`
- **Module Rules:** `../../docs/rules/module-incident-response.md`
- **Standalone Guide:** `../../docs/standalone-games/incident-response.md`
- **Card Reference:** `../CARD_REFERENCE.md` (comprehensive index)

---

## Quick Reference: Card Properties

**Threat Card Properties:**
- Title, Step, Vector, Cost, Clue, Educational Explanation

**Defense Card Properties:**
- Title, Tier, Cost, Vector, Description, Effect

**Both cards include:**
- What module they're used in
- Real-world connection
- Educational value

---

*Incident Response Module: Card Decks*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.1 - Balanced & Refined Edition*
