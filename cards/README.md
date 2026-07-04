# Incident Zero: Card Decks

This folder contains all card materials for the Incident Zero modular cybersecurity board game. Cards are organized by module, with core (starter) decks and expansion (advanced) decks for each.

---

## Folder Structure

```
cards/
├── README.md (this file)
├── CARD_REFERENCE.md (comprehensive card index)
├── print-templates/ (card printing templates and guides)
│   ├── a4-layout-guide.md (A4 print layouts and instructions)
│   └── tracker-sheets.md (printable game tracker sheets)
│
├── incident-response/
│   ├── core-deck/
│   │   └── threat-defense-cards.md (12 threat cards + 24 defense cards)
│   └── expansion-deck/
│       ├── advanced-threats.md (8 additional threat cards, T-13 to T-20)
│       └── advanced-defenses.md (19 additional defense cards, D-25 to D-43)
│
├── hardening/
│   ├── core-deck/
│   │   ├── defense-cards.md (the same 24 defense cards, shared with IR)
│   │   └── pentester-tactic-cards.md (8 tactic cards, PT-01 to PT-08)
│   └── expansion-deck/
│       └── advanced-tactics.md (8 advanced tactic cards, PT-09 to PT-16)
│
├── disaster-recovery/
│   ├── core-deck/
│   │   ├── crisis-action-cards.md (13 crisis action cards)
│   │   ├── event-cards.md (12 timeline events: 6 scheduled + 6 triggered)
│   │   └── stakeholder-cards.md (5 stakeholder trust cards)
│   └── expansion-deck/
│       └── advanced-scenarios.md (8 complex crisis scenarios)
│
├── network-building/
│   ├── core-deck/
│   │   ├── server-cards.md (10 server types)
│   │   ├── security-device-cards.md (10 security devices)
│   │   ├── architecture-cards.md (5 network architecture options)
│   │   └── asset-cards.md (8 business requirement assets)
│   ├── expansion-deck/
│   │   ├── legacy-systems.md (4 legacy/old systems)
│   │   └── cloud-variants.md (4 advanced cloud deployment options)
│   └── standalone/
│       ├── business-requirement-cards.md (20 requirement cards, REQ-01 to REQ-20)
│       └── operational-event-cards.md (16 event cards, EVT-01 to EVT-16)
│
├── forensics/
│   └── core-deck/
│       ├── investigation-cards.md (12 investigation action cards)
│       └── evidence-cards.md (12 evidence cards + 4 findings cards)
│
└── audit-compliance/
    ├── core-deck/
    │   └── audit-domain-cards.md (6 audit domain assessment cards)
    └── expansion-deck/
        └── compliance-frameworks.md (11 framework cards: NIST, CIS, PCI-DSS
                                       + 8 remediation action cards)
```

**Note:** The 24-card Defense deck is shared between Incident Response and Hardening. Rather than a separate `shared/` folder, the same deck appears in both module folders (`incident-response/core-deck/threat-defense-cards.md` and `hardening/core-deck/defense-cards.md`) — print one physical set and use it in both modules.

---

## Module Card Decks

### Incident Response Module
**Purpose:** Detect and investigate hidden attack chains

**Core Deck:**
- 12 Threat Cards (organized by attack chain step)
- 24 Defense Cards (organized by threat vector; shared with Hardening)

**Expansion Deck:**
- 8 Advanced Threat Cards (supply chain, insider, IoT, cloud, DNS, physical)
- 19 Advanced Defense Cards (whitelisting, analytics, container/cloud, playbooks, backup/DR)

**Total:** 63 cards (12 + 24 + 8 + 19; the 24 defenses are shared with Hardening)

**Best for:** 3-5 card attack chains, ~30-45 minute gameplay

---

### Hardening Module
**Purpose:** Build defense-in-depth and test defenses

**Core Deck:**
- 24 Defense Cards (same shared deck as IR core, reusable)
- 8 Pentester Tactic Cards (PT-01 to PT-08, DC 12-15)

**Expansion Deck:**
- 8 Advanced Pentester Tactic Cards (PT-09 to PT-16, DC 14-16)

**Total:** 16 tactic cards + the shared 24-card defense deck

**Best for:** 7 turn hardening, ~30-45 minute gameplay

---

### Disaster Recovery Module
**Purpose:** Manage breach response under crisis pressure

**Core Deck:**
- 13 Crisis Action Cards (investigation, remediation, communication, ransom decision)
- 12 Event Timeline Cards (6 scheduled + 6 triggered deadlines and escalations)
- 5 Stakeholder Cards (customers, regulators, media, board, executives)

**Expansion Deck:**
- 8 Advanced Scenario Cards (complex crisis situations)

**Total:** 38 cards (30 core + 8 expansion)

**Best for:** 8 turn crisis management, ~30-45 minute gameplay

---

### Network Building Module
**Purpose:** Design IT infrastructure with trade-offs

**Core Deck (33 cards):**
- 10 Server Cards (Email, Web, Database, File, DC, Dev, Backup, Cloud, Legacy, Honeypot)
- 10 Security Device Cards (Firewall, IDS, IPS, Load Balancer, VPN, Email Gateway, WAF, Segmentation, SIEM, Honeypot Network)
- 5 Architecture Cards (Flat, Segmented 3-zone, Fully Isolated, Cloud Hybrid, Cloud First)
- 8 Asset Cards (email, web, database, file storage, identity, dev, DR, VPN)

**Expansion Deck (8 cards):**
- 4 Legacy System Cards (mainframe, custom app, ICS, obsolete OS)
- 4 Cloud Variant Cards (microservices, serverless, managed DB, CDN)

**Standalone Decks (36 cards):**
- 20 Business Requirement Cards (REQ-01 to REQ-20)
- 16 Operational Event Cards (EVT-01 to EVT-16)

**Total:** 77 cards (33 core + 8 expansion + 36 standalone)

**Best for:** 5 turn network design, ~30-45 minute gameplay

---

### Forensics Module
**Purpose:** Investigate a breach, collect evidence, and attribute the attack

**Core Deck (28 cards):**
- 12 Investigation Action Cards (DISK-01/02, MEM-01/02, LOG-01/02, NET-01/02, MALW-01/02, TIMELINE-01, THREAT-01)
- 12 Evidence Cards (EVD-01 to EVD-12)
- 4 Findings Cards (FIND-01 to FIND-04)

**Expansion Deck:**
- PLANNED — not yet available (design notes live in the module README; no card file exists yet)

**Total:** 28 cards

**Best for:** 4-7 turn investigations, ~30-45 minute gameplay

---

### Audit & Compliance Module
**Purpose:** Assess security controls using compliance frameworks

**Core Deck:**
- 6 Audit Domain Assessment Cards (segmentation, identity, detection, backup, vendor/cloud, operations)

**Expansion Deck (19 cards, all in compliance-frameworks.md):**
- 5 NIST CSF Function Cards
- 3 CIS Controls Cards
- 3 PCI-DSS Cards
- 8 Remediation Action Cards (REMEDIATION-01 to REMEDIATION-08)

**Total:** 25 cards (6 core + 19 expansion)

**Best for:** quick assessments, ~30-45 minute gameplay (also combines well with IR/DR)

---

## Card Format

All cards are provided in markdown format with:
- **Card Name/Title**
- **Card Type** (Threat, Defense, Tactic, etc.)
- **Module** (which module uses this card)
- **Card Properties** (cost, tier, vector, step, DC, etc.)
- **Description/Effect** (what the card does)
- **Special Rules** (if applicable)

Cards can be:
1. **Printed directly** - Print markdown as-is for reference
2. **Printed on cardstock** - Use the A4 layout guide for printable sheets
3. **Used digitally** - Reference markdown during gameplay

---

## Card Use by Module

### Incident Response
- Uses: Threat Cards, Defense Cards
- From which decks: IR core-deck + IR expansion-deck

### Hardening
- Uses: Defense Cards, Pentester Tactic Cards
- From which decks: shared defense deck (in both IR and Hardening core-decks), Hardening core-deck (tactics), optional expansion

### Disaster Recovery
- Uses: Crisis Action Cards, Event Cards, Stakeholder Cards
- From which decks: DR core-deck + DR expansion-deck
- May reference: Audit findings (if audit was played)

### Network Building
- Uses: Server Cards, Security Device Cards, Architecture Cards, Asset Cards
- From which decks: NB core-deck + NB expansion-deck
- Standalone play adds: Business Requirement Cards + Operational Event Cards (NB standalone decks)

### Forensics
- Uses: Investigation Action Cards, Evidence Cards, Findings Cards
- From which decks: Forensics core-deck (expansion is planned, not yet available)
- Feeds findings into: Hardening, Network Building, and Audit modules

### Audit & Compliance
- Uses: Audit Domain Cards, Framework Cards, Remediation Cards
- From which decks: Audit core-deck + Audit expansion-deck (one file: compliance-frameworks.md)

---

## Shared Cards

Some cards are used across multiple modules:

**Defense Cards** (the 24-card deck shared between IR and Hardening):
- Email Authentication Setup (SOCIAL_ENGINEERING)
- Multi-Factor Authentication (CREDENTIAL_ABUSE)
- EDR Deployment (MALWARE)
- Network Segmentation (NETWORK)
- DLP (DATA_EXFIL)
- And others...

The shared defense deck is documented in **both** module folders — `incident-response/core-deck/threat-defense-cards.md` (printable layouts) and `hardening/core-deck/defense-cards.md` (compact reference). They are the same 24 cards; print once, use in both modules.

**Asset/Server Cards** (referenced across modules):
- Email Server, Web Server, Database Server, etc.
- Used in Network Building (component selection)
- Referenced in Incident Response (asset names in clues)
- May be used in Disaster Recovery (what was affected)

---

## Reusability Notes

### Cards Shared Between IR and Hardening
- Defense Cards: the 24-card deck (D-01 to D-24) is directly reusable in Hardening
- Both modules use the same 6 threat vectors (SOCIAL_ENGINEERING, WEB_EXPLOIT, CREDENTIAL_ABUSE, MALWARE, NETWORK, DATA_EXFIL)
- Hardening adds Pentester Tactic cards to test defenses

### Cards NOT Shared (Module-Specific)
- **Threat Cards:** Only for Incident Response (other modules don't need attack chains)
- **Pentester Tactic Cards:** Only for Hardening (simulated red team attacks)
- **Crisis Action / Event / Stakeholder Cards:** Only for Disaster Recovery
- **Server/Device/Architecture Cards:** Only for Network Building (physical infrastructure)
- **Investigation/Evidence/Findings Cards:** Only for Forensics (though Findings feed other modules)
- **Audit Domain Cards:** Only for Audit & Compliance (assessment framework)

---

## Printing Cards

### Print Templates
See `print-templates/` folder for:
- **a4-layout-guide.md** - A4 sheet layouts and detailed printing instructions
- **tracker-sheets.md** - Printable tracker sheets for gameplay

### Quick Print Tips
1. Print on cardstock (240-300 gsm) for durability
2. Use color printing for better visual distinction
3. Cut along dotted lines
4. Consider laminating for reusability
5. A4 sheets: Print multiple cards per sheet for efficiency

---

## Card Reference Index

See **CARD_REFERENCE.md** for:
- Complete index of all cards in all six modules
- Card properties quick lookup (tier, DC, cost, vector)
- Deck file locations and card ID ranges
- Card count summary per module

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
*v2.2 - Playtest Edition*
