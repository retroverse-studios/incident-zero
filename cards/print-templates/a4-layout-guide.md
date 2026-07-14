# A4 Print & Layout Guide

**Version:** 2.2 - Playtest Edition

How to turn the card files in `cards/` into a physical deck.

---

## What You Need

- **Printer:** Any home/office printer (color recommended, mono works)
- **Paper:** 200-250 gsm cardstock for cards; plain 80 gsm for tracker sheets
- **Tools:** Paper cutter or scissors, ruler, optionally 63.5 × 88 mm card sleeves
- **Optional:** Corner rounder, laminator for tracker sheets (reuse with dry-erase markers)

---

## Card Format

All Incident Zero cards use **poker size (63.5 × 88 mm / 2.5" × 3.5")**.
That gives a **3 × 3 grid of 9 cards per A4 sheet** with comfortable margins and cutting gutters.

### A4 Sheet Layout (9 cards)

```
A4 portrait: 210 × 297 mm
Margins: 10 mm all sides
Card grid: 3 columns × 3 rows
Card size: 63.5 × 88 mm
Gutters: ~3 mm between cards (cut lines)
```

If your printer needs more margin, drop to a **2 × 4 grid (8 cards per sheet)** and scale cards to fit.

---

## Ready-Made PDF Print Pack (all modules)

`downloads/print-pack/` has ready-to-print PDFs (3 × 3 cards per A4 page,
fronts and pixel-noir backs on alternating pages):

| PDF | Contents |
|-----|----------|
| `ir-core.pdf` | 12 Threats + 24 Defenses |
| `ir-expansion.pdf` | 8 advanced Threats + 19 advanced Defenses |
| `hardening-core.pdf` | 8 Pentester Tactics + the 24 shared Defenses |
| `hardening-expansion.pdf` | 8 advanced Tactics |
| `forensics-core.pdf` | 12 Investigations + 16 Evidence |
| `disaster-recovery-core.pdf` | 13 Crisis Actions + 12 Events + 5 Stakeholders |
| `disaster-recovery-expansion.pdf` | 8 advanced Scenarios |
| `network-building-core.pdf` | 10 Servers + 10 Devices + 8 Assets + 5 Architectures |
| `network-building-expansion.pdf` | 4 Cloud variants + 4 Legacy systems |
| `network-building-standalone.pdf` | 20 Business Requirements + 16 Operational Events |
| `audit-core.pdf` | 6 Audit Domains |
| `audit-expansion.pdf` | 19 Framework cards |
| `play-mats.pdf` | Universal tracker + Forensics/DR/Audit/Network module mats (A4 landscape) |
| `network-zone-tiles.pdf` | 5 zone tiles that butt together into the network board |

**Duplex printer:** print double-sided, flip on long edge — backs land behind
their fronts. **Single-sided:** print odd pages only for face-up cards, or all
pages and glue front/back sheets together. Cut along the edge marks.

**Play mats:** print on plain A4 (landscape), laminate + dry-erase or use coins
as track markers. They replace the ASCII tracker sheets below.

**Zone tiles (Network Building):** lay the five tiles in a row —
Internet Edge → DMZ → Internal Network → Data Center, Cloud beside the edge —
and place Server/Device cards sideways on the printed slots. In follow-on
modules, threat tokens sit on the compromised zone.

Regenerate after any card edit (markdown stays the single source of truth):

```
python3 tools/cardgen/build_print_pack.py   # card decks
python3 tools/cardgen/build_mats.py         # play mats
python3 tools/cardgen/build_tiles.py        # network zone tiles
```

## Making Cards From the Markdown Files

Manual fallback options if you can't print the PDFs:

### Option 1: Table-fold cards (fastest)
1. Open the card file (e.g., `cards/incident-response/core-deck/threat-defense-cards.md`)
2. Copy each card's title + key fields into a 9-cell table in any word processor
3. Print on cardstock, cut on the gridlines

### Option 2: Print the reference pages
1. Print the card file directly from the docs site (Ctrl+P in your browser)
2. Keep the pages as a face-up reference "menu" instead of a shuffled deck
3. Works well for decks that are menus rather than hidden draws
   (Defense cards, Crisis Action cards, Investigation cards, Audit domains)

### Option 3: Index cards (zero printing)
Hand-write card titles + costs/DCs on index cards; keep the markdown open as the rules text. Fine for a first playtest.

> **Which decks must be hidden/shuffled?** Only the Threat deck (Threat Orchestrator's hidden attack chain), Pentester Tactic deck, and Event deck benefit from being physical face-down cards. Everything else can be an open menu.

---

## Color Coding by Card Type

| Card Type | Color | Modules |
|-----------|-------|---------|
| Threat | Red | Incident Response |
| Defense | Blue | IR / Hardening |
| Pentester Tactic | Dark red | Hardening |
| Server / Device / Architecture | Green | Network Building |
| Crisis Action | Orange | Disaster Recovery |
| Event | Purple | Disaster Recovery |
| Stakeholder | Yellow | Disaster Recovery |
| Investigation | Teal | Forensics |
| Evidence / Findings | Grey | Forensics |
| Audit Domain / Framework | Brown | Audit & Compliance |

Mono printers: print the card-type name in a header band instead.

**Accessibility note:** never rely on color alone — every card carries its type in text. (Colorblind-safe icons are planned; see FUTURE_WORK.md.)

---

## Cutting & Finishing

1. Cut columns first, then rows (fewer long cuts = straighter edges)
2. Round corners if you have a corner punch (cards shuffle better)
3. Sleeve if the deck will be shuffled a lot (Threat, Tactic, Event decks)

## Tracker Sheets

Print `tracker-sheets.md` (this folder) on plain paper — one universal sheet per table plus the module sheet for the module you're playing. Laminate + dry-erase marker for repeated use.
