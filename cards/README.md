# Incident Zero: Card Decks

This folder contains all card materials for the Incident Zero modular cybersecurity board game. Cards are organized by module, with core (starter) decks and expansion (advanced) decks for each.

---

## Folder Structure

```
cards/
├── README.md (this file)
├── CARD_REFERENCE.md (comprehensive card index)
├── print-templates/ (card printing templates and guides)
│
├── incident-response/
│   ├── core-deck/
│   │   └── threat-defense-cards.md (12 threat cards + 24 defense cards)
│   └── expansion-deck/
│       ├── advanced-threats.md (8 additional threat cards)
│       └── advanced-defenses.md (8 additional defense cards)
│
├── hardening/
│   ├── core-deck/
│   │   ├── defense-cards.md (core defense cards for hardening)
│   │   └── pentester-tactic-cards.md (8 tactic cards)
│   └── expansion-deck/
│       └── advanced-tactics.md (additional tactic variations)
│
├── disaster-recovery/
│   ├── core-deck/
│   │   ├── crisis-action-cards.md (stakeholder notification cards)
│   │   └── event-cards.md (timeline events and escalations)
│   └── expansion-deck/
│       └── advanced-scenarios.md (complex crisis scenarios)
│
├── network-building/
│   ├── core-deck/
│   │   ├── server-cards.md (10 server types)
│   │   ├── security-device-cards.md (10 security devices)
│   │   ├── architecture-cards.md (5 network architecture options)
│   │   └── asset-cards.md (business requirement assets)
│   └── expansion-deck/
│       ├── legacy-systems.md (additional legacy/old systems)
│       └── cloud-variants.md (advanced cloud deployment options)
│
├── audit-compliance/
│   ├── core-deck/
│   │   └── audit-domain-cards.md (6 audit domain assessment cards)
│   └── expansion-deck/
│       ├── compliance-frameworks.md (NIST, CIS, PCI-DSS, HIPAA)
│       └── remediation-cards.md (remediation action cards)
│
└── shared/
    ├── asset-cards.md (cards used across multiple modules)
    └── generic-defense-cards.md (defenses applicable to multiple modules)
```

---

## Module Card Decks

### Incident Response Module
**Purpose:** Detect and investigate hidden attack chains

**Core Deck:**
- 12 Threat Cards (organized by attack chain step)
- 24 Defense Cards (organized by threat vector)

**Expansion Deck:**
- 8 Advanced Threat Cards (sophisticated attack scenarios)
- 8 Advanced Defense Cards (elite-tier controls)

**Total:** 52 cards

**Best for:** 3-5 card attack chains, ~30-45 minute gameplay

---

### Hardening Module
**Purpose:** Build defense-in-depth and test defenses

**Core Deck:**
- 24 Defense Cards (same as IR core, reusable)
- 8 Pentester Tactic Cards (attack simulation tactics)

**Expansion Deck:**
- Advanced Pentester Tactic variations
- Additional defense cards for depth

**Total:** 32+ cards

**Best for:** 5-7 turn hardening, ~30-45 minute gameplay

---

### Disaster Recovery Module
**Purpose:** Manage breach response under crisis pressure

**Core Deck:**
- Stakeholder Notification Cards (customers, regulators, media, board)
- Event Timeline Cards (deadlines and escalations)
- Crisis Action Cards (investigation, remediation, communication)

**Expansion Deck:**
- Advanced scenario cards
- Complex crisis situations

**Total:** 20+ cards

**Best for:** 7 turn crisis management, ~30-45 minute gameplay

---

### Network Building Module
**Purpose:** Design IT infrastructure with trade-offs

**Core Deck:**
- 10 Server Cards (Email, Web, Database, File, DC, Dev, Backup, Cloud, Legacy, Honeypot)
- 10 Security Device Cards (Firewall, IDS, IPS, Load Balancer, VPN, Email Gateway, WAF, Segmentation, SIEM, Honeypot Network)
- 5 Architecture Cards (Flat, Segmented 3-zone, Fully Isolated, Cloud Hybrid, Cloud First)
- 8 Asset/Business Requirement Cards (email, web, database, file storage, identity, dev, DR, VPN)

**Expansion Deck:**
- Additional legacy systems
- Advanced cloud deployment options
- Specialized security appliances

**Total:** 33+ cards

**Best for:** 5 turn network design, ~15-20 minute gameplay

---

### Audit & Compliance Module
**Purpose:** Assess security controls using compliance frameworks

**Core Deck:**
- 6 Audit Domain Assessment Cards (segmentation, identity, detection, backup, cloud, operations)
- Scoring/Finding reference cards

**Expansion Deck:**
- NIST CSF variant cards
- CIS Controls variant cards
- PCI-DSS specific cards
- HIPAA specific cards
- Remediation action cards

**Total:** 15+ cards

**Best for:** 10 minute assessment, ~30-45 minute gameplay when combined with IR/DR

---

## Card Format

All cards are provided in markdown format with:
- **Card Name/Title**
- **Card Type** (Threat, Defense, Tactic, etc.)
- **Module** (which module uses this card)
- **Card Properties** (cost, tier, vector, step, etc.)
- **Description/Effect** (what the card does)
- **Special Rules** (if applicable)

Cards can be:
1. **Printed directly** - Print markdown as-is for reference
2. **Printed on cardstock** - Use card templates to generate printable PDFs
3. **Used digitally** - Reference markdown during gameplay

---

## Card Use by Module

### Incident Response
- Uses: Threat Cards, Defense Cards
- From which decks: IR core-deck + IR expansion-deck

### Hardening
- Uses: Defense Cards, Pentester Tactic Cards
- From which decks: IR core-deck (defense cards), Hardening core-deck (tactics), optional expansions

### Disaster Recovery
- Uses: Crisis Action Cards, Event Cards, Stakeholder Cards
- From which decks: DR core-deck + DR expansion-deck
- May reference: Audit findings (if audit was played)

### Network Building
- Uses: Server Cards, Security Device Cards, Architecture Cards, Asset Cards
- From which decks: NB core-deck + NB expansion-deck

### Audit & Compliance
- Uses: Audit Domain Cards, Finding Cards
- From which decks: Audit core-deck + Audit expansion-deck

---

## Shared Cards

Some cards are used across multiple modules:

**Defense Cards** (shared between IR and Hardening):
- Email Authentication Setup (SOCIAL_ENGINEERING)
- Multi-Factor Authentication (CREDENTIAL_ABUSE)
- EDR Deployment (MALWARE)
- Network Segmentation (NETWORK)
- DLP (DATA_EXFIL)
- And others...

**Asset Cards** (shared between modules):
- Email Server, Web Server, Database Server, etc.
- Used in Network Building (component selection)
- Referenced in Incident Response (asset names in clues)
- May be used in Disaster Recovery (what was affected)

These cards are documented in `shared/` folder to avoid duplication.

---

## Reusability Notes

### Cards Shared Between IR and Hardening
- Defense Cards: 24 cards from IR core-deck are directly reusable in Hardening
- Both modules use the same 6 threat vectors (SOCIAL_ENGINEERING, WEB_EXPLOIT, CREDENTIAL_ABUSE, MALWARE, NETWORK, DATA_EXFIL)
- Hardening adds Pentester Tactic cards to test defenses

### Cards NOT Shared (Module-Specific)
- **Threat Cards:** Only for Incident Response (other modules don't need attack chains)
- **Pentester Tactic Cards:** Only for Hardening (simulated red team attacks)
- **Crisis Action Cards:** Only for Disaster Recovery (not used in other modules)
- **Server/Device Cards:** Only for Network Building (physical infrastructure)
- **Audit Domain Cards:** Only for Audit & Compliance (assessment framework)

---

## Printing Cards

### Print Templates
See `print-templates/` folder for:
- **card-template-standard.html** - Standard card template for all modules
- **card-template-a4.html** - A4 sheet layout (multiple cards per page)
- **print-guide.md** - Detailed printing instructions
- **cutting-guide.md** - Guidelines for cutting cards

### Quick Print Tips
1. Print on cardstock (240-300 gsm) for durability
2. Use color printing for better visual distinction
3. Cut along dotted lines
4. Consider laminating for reusability
5. A4 sheets: Print multiple cards per sheet for efficiency

---

## Card Reference Index

See **CARD_REFERENCE.md** for:
- Complete alphabetical index of all cards
- Card properties quick lookup
- Which cards work together
- Attack vector cross-reference
- Budget cost reference

---

## Contributing New Cards

When adding cards to any module:

1. **Follow existing format** - Match the structure of existing cards
2. **Specify module** - Clearly mark which module(s) use this card
3. **Include properties** - Cost, tier, vector, step, etc.
4. **Add educational value** - Explain why the card works (teaching point)
5. **Test in gameplay** - Ensure card is balanced
6. **Update CARD_REFERENCE.md** - Add to the index

---

## Download Guides

### For Teachers Running Single Module
- Download only the module's folder
- Core-deck for standard play
- Add expansion-deck for advanced play

### For Teachers Running Multiple Modules
- Download all module folders
- Use combination guide in `../docs/module-combinations.md`
- Cross-reference shared cards

### For Online Play
- Use markdown files directly
- Print on demand
- No physical cards needed

---

## License

All card materials are licensed under **CC BY-NC-SA 4.0** (Creative Commons Attribution-NonCommercial-ShareAlike).

You may:
- ✓ Use cards for educational purposes
- ✓ Modify cards for your classroom
- ✓ Share modified versions (with attribution)

You may not:
- ✗ Use cards for commercial purposes without permission
- ✗ Remove attribution

---

## Related Documentation

For game rules and how to use cards, see:
- **Core Rules:** `../docs/rules/core-rules.md`
- **Module Rules:** `../docs/rules/module-*.md`
- **Module Combinations:** `../docs/module-combinations.md`
- **Standalone Guides:** `../docs/standalone-games/`

---

*Incident Zero: Card Decks*
*Modular cybersecurity board game*
*v2.1 - Balanced & Refined Edition*
