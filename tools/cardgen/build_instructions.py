"""Render the one-page print instructions sheet.

Output: downloads/print-pack/print-instructions.pdf (A4 portrait @300 DPI).
Covers the two things that actually break duplex alignment — page scaling
and flip direction — plus cutting and finishing.
"""

from pathlib import Path

from PIL import Image, ImageDraw

from build_mats import F, BOLD, MONO, INK, PAPER, MUTED, GLOW

ROOT = Path(__file__).resolve().parents[2]
W, H = 2480, 3508  # A4 portrait
M = 150

STEPS = [
    ("1 · PRINT AT ACTUAL SIZE", [
        'In the print dialog set scaling to "Actual size" / "100%" — never',
        '"Fit to page". Fit-to-page shrinks fronts and backs by different',
        "amounts on some drivers, which is the #1 cause of misaligned backs.",
    ]),
    ("2 · CARD DECKS: DUPLEX, FLIP ON LONG EDGE", [
        "Deck PDFs alternate pages: fronts, then their backs (mirrored).",
        'Print double-sided with "Flip on long edge" and backs land behind',
        "their fronts automatically.",
        "",
        "TEST FIRST: print only pages 1-2 of one deck on plain paper. Hold",
        "the sheet up to the light — card frames should sit within ~2 mm.",
        "The symmetric back frame forgives small offsets; sleeves hide them",
        "entirely. If your printer cannot duplex: print odd pages (fronts),",
        "re-feed the stack, print even pages — or print odd pages only and",
        "play with face-up decks (only Threat, Pentester Tactic and Event",
        "decks truly need hidden backs).",
    ]),
    ("3 · PAPER", [
        "Cards: 200-250 gsm cardstock (or plain paper into 63.5 x 88 mm",
        "sleeves — sleeves also fix any duplex offset).",
        "Play mats & zone tiles: plain 80 gsm is fine; laminate the mats and",
        "use a dry-erase marker, or move coins along the tracks.",
    ]),
    ("4 · CUT", [
        "Cut along the edge marks on the FRONT side (marks sit outside the",
        "card area, so they disappear with the offcuts). A guillotine or",
        "rotary cutter beats scissors; a corner rounder is a nice finish.",
    ]),
    ("5 · BUILD THE TABLE", [
        "Universal mat + your module's mat in the middle. Network Building:",
        "lay the five zone tiles in a row (Internet Edge > DMZ > Internal >",
        "Data Center, Cloud beside the edge) and place cards on the slots.",
    ]),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 260], fill=INK)
    for y in range(8, 260, 14):
        d.line([0, y, W, y], fill="#262626", width=3)
    d.text((M, 70), "PRINT INSTRUCTIONS", font=F(BOLD, 86), fill=GLOW)
    d.text((M, 185), "Incident Zero print-and-play pack · poker-size cards, A4 sheets",
           font=F(MONO, 34), fill="#B9B9B9")
    d.rectangle([0, 260, W, 276], fill=GLOW)

    y = 360
    for title, lines in STEPS:
        d.text((M, y), title, font=F(BOLD, 52), fill=INK)
        y += 84
        for line in lines:
            if line:
                d.text((M + 10, y), line, font=F(MONO, 36), fill="#333333")
            y += 56
        y += 46

    d.line([M, H - 170, W - M, H - 170], fill="#CCCCCC", width=3)
    d.text((M, H - 130), "incidentzero.retroverse.studio · github.com/retroverse-studios/incident-zero",
           font=F(MONO, 32), fill=MUTED)

    out = ROOT / "downloads" / "print-pack" / "print-instructions.pdf"
    img.save(out, resolution=300.0)
    print(f"instructions -> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
