# Forensics Module: Card Decks

**Version:** 2.1 - Investigation & Attribution Edition

---

## Module Overview

The **Forensics Module** focuses on digital forensics and incident investigation. Players act as forensic analysts investigating compromised systems to reconstruct attacks, discover evidence, and attribute breaches to threat actors.

### Game Length
- **Solo (Standalone):** 45-90 minutes
- **Sequential (After IR/DR):** 30-45 minutes
- **Full Lifecycle:** 15+ minutes within larger campaign

### Card Deck Composition

| Deck | Cards | Description |
|------|-------|-------------|
| **Core Deck** | 24 total | Investigation Actions (12) + Evidence (12) |
| **Expansion Deck** | 16 total | Advanced techniques + challenging scenarios |
| **Total** | 40 cards | Complete Forensics game |

---

## Core Deck (24 Cards)

### Investigation Action Cards (12)

Investigation Action cards represent specific forensic analysis techniques that players can deploy to discover evidence.

**By Forensic Discipline:**

| Discipline | Cards | Details |
|-----------|-------|---------|
| **Disk Forensics** | DISK-01, DISK-02 | Imaging, file carving, artifact recovery |
| **Memory Forensics** | MEM-01, MEM-02 | RAM analysis, volatile process examination |
| **Log Analysis** | LOG-01, LOG-02 | Event logs, cross-system correlation |
| **Network Forensics** | NET-01, NET-02 | Traffic analysis, packet inspection |
| **Malware Analysis** | MALW-01, MALW-02 | Dynamic behavior, static reverse engineering |
| **Timeline/Attribution** | TIMELINE-01, THREAT-01 | Event reconstruction, threat intelligence |

**Card Details:**
- See [investigation-cards.md](core-deck/investigation-cards.md) for complete card specifications
- Each card includes DC (Difficulty Class), Budget Cost, and what evidence it discovers

---

### Evidence Cards (12)

Evidence cards represent specific findings discovered during investigations.

**By Evidence Type:**

| Type | Cards | Description |
|------|-------|-------------|
| **Malware & Persistence** | EVD-01, EVD-03, EVD-10 | Malware, scheduled tasks, behavior profiles |
| **Credentials & Access** | EVD-04 | Suspicious logins, compromised accounts |
| **Lateral Movement** | EVD-05 | Pass-the-hash, privilege escalation |
| **Exfiltration** | EVD-06, EVD-11 | Data transfers, file staging artifacts |
| **Infrastructure** | EVD-02, EVD-07 | C2 domains, attacker infrastructure map |
| **Activity** | EVD-08, EVD-09, EVD-12 | Encryption keys, command history, anti-forensics |

**Card Details:**
- See [evidence-cards.md](core-deck/evidence-cards.md) for complete card specifications
- Each card includes chain of custody rating and investigative leads

---

## Expansion Deck (16 Cards)

The Expansion Deck provides advanced investigation techniques and challenging forensic scenarios.

### Advanced Investigation Actions (8 Cards)

| Card | Technique | DC | Cost | Advanced Challenge |
|------|-----------|----|----|-------------------|
| **ADV-01** | Cloud Forensics | 15 | 20 | SaaS/cloud infrastructure investigation |
| **ADV-02** | Mobile Device Forensics | 14 | 20 | iOS/Android artifact analysis |
| **ADV-03** | Database Forensics | 15 | 25 | SQL log recovery, backup analysis |
| **ADV-04** | Firmware Analysis | 16 | 25 | BIOS, UEFI, router firmware |
| **ADV-05** | Cryptography Recovery | 15 | 25 | Encryption key derivation, decryption |
| **ADV-06** | Supply Chain Forensics | 14 | 20 | Third-party compromise evidence |
| **ADV-07** | USB/External Device Forensics | 13 | 15 | Removable media analysis |
| **ADV-08** | Advanced Anti-Forensics Countermeasures | 16 | 25 | Defeating log deletion, cover-up techniques |

---

### Advanced Evidence Cards (8 Cards)

| Card | Evidence Type | Difficulty | Description |
|------|---------------|-----------|-------------|
| **ADV-EVD-01** | Cloud Infrastructure Compromise | TIER 3+ | AWS/Azure/GCP account compromise |
| **ADV-EVD-02** | Mobile Malware | TIER 3+ | iOS/Android malware artifacts |
| **ADV-EVD-03** | Database Exfiltration | TIER 3+ | Large-scale database theft evidence |
| **ADV-EVD-04** | Firmware Persistence | TIER 4 | BIOS/UEFI rootkit evidence |
| **ADV-EVD-05** | Supply Chain Compromise | TIER 3+ | Third-party software compromise |
| **ADV-EVD-06** | Nation-State Attribution | TIER 4 | APT group signatures and techniques |
| **ADV-EVD-07** | Zero-Day Exploit Evidence | TIER 3+ | Unknown vulnerability exploitation |
| **ADV-EVD-08** | Sophisticated Anti-Forensics | TIER 4 | Advanced cover-up techniques |

---

## Card Organization

### By Printable Deck

**Core Deck (24 cards, printable on 3-4 sheets):**
- Sheet 1: Investigation Actions 1-6 (DISK, MEM, LOG cards)
- Sheet 2: Investigation Actions 7-12 (NET, MALW, TIMELINE, THREAT)
- Sheet 3: Evidence Cards 1-12 (EVD-01 through EVD-12)
- Sheet 4: Findings Cards (FIND-01 through FIND-04)

**Expansion Deck (16 cards, printable on 2 sheets):**
- Sheet 1: Advanced Investigation Actions (ADV-01 through ADV-08)
- Sheet 2: Advanced Evidence Cards (ADV-EVD-01 through ADV-EVD-08)

---

## How to Print

### Materials
- Cardstock (250 gsm or heavier)
- Card sleeves (optional but recommended)
- Scissors or paper cutter
- Cutting mat

### Printing Instructions

1. **Download & Print:**
   - Print [investigation-cards.md](core-deck/investigation-cards.md) on cardstock
   - Print [evidence-cards.md](core-deck/evidence-cards.md) on cardstock
   - Print [advanced-cards.md](expansion-deck/advanced-cards.md) on cardstock (if using expansion)

2. **Cut Cards:**
   - Standard card size: 3.5" × 5.5"
   - Align card borders and cut carefully
   - Or print with margins and use guillotine cutter

3. **Organize Decks:**
   - Core Deck: 24 cards (Investigation + Evidence + Findings)
   - Expansion Deck: 16 cards (Advanced only)
   - Use card box or deck box for storage

4. **Optional: Sleeve & Laminate**
   - Card sleeves protect cards from wear
   - Lamination adds durability (optional)

---

## Using the Forensics Cards

### In Standalone Play

1. **Select scenario complexity (TIER 1-4)**
2. **Shuffle Investigation Action deck**
3. **Keep Evidence and Findings cards face-down**
4. **Players draw Investigation Action cards as needed**
5. **Revealed Evidence cards stay face-up on table**
6. **Findings cards only revealed at game end**

### In Sequential Play (After IR/DR)

1. **Use only relevant Evidence cards** for the attack chain already known
2. **Leave advanced cards face-down** unless they apply to scenario
3. **Investigation Actions remain the same**
4. **Progress meters reflect prior knowledge**

### In Competitive Play

- Multiple teams investigate same breach simultaneously
- Whoever achieves victory condition first wins
- Can use advanced scenarios for higher difficulty

---

## Card Deck Statistics

### Distribution

**Investigation Actions by Difficulty:**
- Easy (DC 11-12): 3 cards (LOG-01, TIMELINE-01, NET-01)
- Medium (DC 13-14): 6 cards (DISK-01, MEM-01, LOG-02, NET-02, MALW-01, DISK-02)
- Hard (DC 15): 3 cards (MEM-02, MALW-02, THREAT-01)

**Evidence by Type:**
- Malware & Persistence: 3 cards
- Credentials & Access: 1 card
- Lateral Movement: 1 card
- Exfiltration: 2 cards
- Infrastructure: 2 cards
- Activity: 3 cards

**Findings by Type:**
- Attribution Report: 1 card
- Attack Surface: 1 card
- Persistence Analysis: 1 card
- Investigative Gaps: 1 card

---

## Recommended Card Combinations

### Beginner Scenario (TIER 1)
- Use core Investigation Actions (DC 11-13)
- Use basic Evidence (common findings)
- Skip advanced cards

**Example Investigation Path:**
1. LOG-01 (Event Log) → EVD-04 (Suspicious Login)
2. MALW-01 (Dynamic Analysis) → EVD-01 (Malware)
3. TIMELINE-01 (Reconstruction) → EVD-03 (Persistence)
4. THREAT-01 (Attribution) → FIND-01 (Attribution Report)

---

### Advanced Scenario (TIER 3-4)
- Use all core Investigation Actions
- Combine with Expansion cards
- Require multiple evidence sources for findings

**Example Investigation Path:**
1. DISK-02 (File Carving) → ADV-EVD-01 (Cloud Compromise)
2. MEM-02 (Deep Memory) → ADV-EVD-04 (Firmware Rootkit)
3. NET-02 (Deep Packet Analysis) → ADV-EVD-06 (Nation-State)
4. ADV-08 (Anti-Forensics Countermeasures) → ADV-EVD-08 (Sophisticated)
5. THREAT-01 (Attribution) → FIND-01 (Attribution to APT group)

---

## Forensics Card Relationships

### Investigation → Evidence Flow

```
DISK-01 ──→ EVD-01, EVD-03, EVD-11
MEM-01 ──→ EVD-02, EVD-04, EVD-09
LOG-01 ──→ EVD-04, EVD-05
LOG-02 ──→ EVD-05, EVD-09
NET-01 ──→ EVD-02, EVD-06
NET-02 ──→ EVD-06, EVD-08
MALW-01 ──→ EVD-01, EVD-10
MALW-02 ──→ EVD-01, EVD-08
TIMELINE ──→ EVD-09, EVD-11
THREAT-01 ──→ EVD-07, FIND-01
```

Each Investigation Action typically discovers one or more Evidence cards.
Multiple Investigation Actions may point to the same Evidence (corroboration).

---

## Forensics Integration with Other Modules

### Receiving Input From:
- **Incident Response:** Attack chain already known (use subset of Evidence)
- **Disaster Recovery:** Investigating failed breach (incomplete information)

### Feeding Output To:
- **Hardening:** "Block techniques discovered in forensics"
- **Network Building:** "Redesign to prevent discovered attack vectors"
- **Audit & Compliance:** "Control gaps revealed by forensic findings"

---

## Frequently Asked Questions

**Q: Can I mix Core and Expansion decks?**
A: Yes! Expansion cards add complexity and advanced scenarios. Recommended only for experienced players (TIER 3-4).

**Q: How many Investigation Actions should I have in hand?**
A: In core deck play, typically 2-3 actions available at any time. Expansion deck increases options to 4-5.

**Q: Can I discard and redraw Investigation Action cards?**
A: No. Each Investigation Action card represents a specific technique that can only be used once. Once used, it doesn't return to deck.

**Q: What if we run out of Investigation Actions before finishing?**
A: You've exhausted available techniques. Investigation concludes. Check victory conditions.

**Q: Can Evidence cards be "used up"?**
A: No. Evidence cards stay on table once revealed. They support your investigation and inform conclusions (Findings cards).

**Q: How do I know which Evidence to expect from an Investigation?**
A: Check the "Discovery Source" section on each Evidence card. It lists which Investigation Actions typically find it.

---

## Card Availability

All Forensics cards are available for printing:

### Core Deck Files
- [investigation-cards.md](core-deck/investigation-cards.md) - 12 Investigation Action cards
- [evidence-cards.md](core-deck/evidence-cards.md) - 12 Evidence + 4 Findings cards

### Expansion Deck Files
- [advanced-cards.md](expansion-deck/advanced-cards.md) - 8 Advanced Actions + 8 Advanced Evidence

### Tracking Sheets & Templates
- [Forensics Progress Meter Tracker](../assets/forensics-tracker-template.xlsx)
- [Investigation Log Worksheet](../assets/forensics-investigation-log.xlsx)

---

## Contributing New Cards

Want to create additional Forensics cards? Follow the [Card Consistency Model](../../docs/CARD_DESIGN/CARD_CONSISTENCY_MODEL.md) guide.

**Investigation Action Template:**
- Title, MITRE ATT&CK technique, DC, Cost, Duration
- Description of technique
- Discovery sources
- Success/partial/failure conditions
- Chain of custody notes

**Evidence Card Template:**
- Title, Type, MITRE ATT&CK
- Description of finding
- Where found, what revealed
- Chain of custody rating
- Investigative leads
- Progress meter impact

---

## Version History

- **v2.1** (Current) - Investigation & Attribution Edition
  - 24 Core Deck cards (Investigation + Evidence + Findings)
  - 16 Expansion Deck cards (Advanced scenarios)
  - Full MITRE ATT&CK integration
  - Chain of custody tracking for legal admissibility

---

**Ready to investigate?** Print your cards and begin your forensic analysis!

