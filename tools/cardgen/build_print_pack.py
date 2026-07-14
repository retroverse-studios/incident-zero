"""Build printable A4 card-sheet PDFs from the markdown card files.

Usage:
    python3 tools/cardgen/build_print_pack.py [deck ...]   # default: all decks

Output: downloads/print-pack/<deck>.pdf — pages alternate fronts / backs so
duplex printing (flip on long edge) produces double-sided cards. Print odd
pages only for fronts-only sheets. 3x3 cards per A4 page, cut on the marks.
"""

import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract import parse_file
from render import CARD_H, CARD_W, back_for, render_face

ROOT = Path(__file__).resolve().parents[2]
A4_W, A4_H = 2480, 3508  # A4 at 300 DPI
COLS, ROWS = 3, 3
GUTTER = 36
GRID_W = COLS * CARD_W + (COLS - 1) * GUTTER
GRID_H = ROWS * CARD_H + (ROWS - 1) * GUTTER
OFF_X, OFF_Y = (A4_W - GRID_W) // 2, (A4_H - GRID_H) // 2

DECKS = {
    "ir-core": {
        "module": "Incident Response",
        "sources": [("cards/incident-response/core-deck/threat-defense-cards.md", "")],
    },
    "ir-expansion": {
        "module": "Incident Response",
        "sources": [
            ("cards/incident-response/expansion-deck/advanced-threats.md", "Threat Card"),
            ("cards/incident-response/expansion-deck/advanced-defenses.md", "Defense Card"),
        ],
    },
}


def cell_origin(idx, mirrored=False):
    row, col = divmod(idx, COLS)
    if mirrored:  # back sheet: mirror columns for long-edge duplex alignment
        col = COLS - 1 - col
    return OFF_X + col * (CARD_W + GUTTER), OFF_Y + row * (CARD_H + GUTTER)


def new_page():
    page = Image.new("RGB", (A4_W, A4_H), "white")
    draw = ImageDraw.Draw(page)
    # cut marks: hairlines across the full page at every card edge
    xs, ys = set(), set()
    for c in range(COLS):
        x0 = OFF_X + c * (CARD_W + GUTTER)
        xs.update([x0, x0 + CARD_W])
    for r in range(ROWS):
        y0 = OFF_Y + r * (CARD_H + GUTTER)
        ys.update([y0, y0 + CARD_H])
    for x in xs:
        draw.line([x, 40, x, OFF_Y - 20], fill="#999999", width=2)
        draw.line([x, OFF_Y + GRID_H + 20, x, A4_H - 40], fill="#999999", width=2)
    for y in ys:
        draw.line([40, y, OFF_X - 20, y], fill="#999999", width=2)
        draw.line([OFF_X + GRID_W + 20, y, A4_W - 40, y], fill="#999999", width=2)
    return page


def build_deck(name, spec):
    cards = []
    for src, default_type in spec["sources"]:
        for card in parse_file(ROOT / src, default_type):
            if card["is_card"]:
                cards.append(card)
            else:
                print(f"  skipped cross-reference heading: {card['id']} {card['title']}")
    if not cards:
        raise SystemExit(f"{name}: no cards parsed")

    back_cache = {}
    pages = []
    for start in range(0, len(cards), COLS * ROWS):
        chunk = cards[start:start + COLS * ROWS]
        front, back = new_page(), new_page()
        for i, card in enumerate(chunk):
            front.paste(render_face(card, spec["module"]), cell_origin(i))
            bt = card["card_type"]
            if bt not in back_cache:
                back_cache[bt] = back_for(bt)
            back.paste(back_cache[bt], cell_origin(i, mirrored=True))
        pages.extend([front, back])

    out_dir = ROOT / "downloads" / "print-pack"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{name}.pdf"
    pages[0].save(out, save_all=True, append_images=pages[1:], resolution=300.0)
    print(f"{name}: {len(cards)} cards -> {out.relative_to(ROOT)} ({len(pages)} pages)")


if __name__ == "__main__":
    targets = sys.argv[1:] or list(DECKS)
    for name in targets:
        build_deck(name, DECKS[name])
