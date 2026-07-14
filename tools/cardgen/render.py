"""Render card faces and backs as poker-size images (63.5 x 88 mm @ 300 DPI).

Faces are text-first (the game is playable text-only); the pixel-noir art
lives on the backs (assets/art/backs/), with the deck name overlaid here so
the source art stays text-free.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

CARD_W, CARD_H = 750, 1040  # 63.5 x 88 mm at 300 DPI
MARGIN = 46

# Color coding from cards/print-templates/a4-layout-guide.md
TYPE_COLORS = {
    "Threat Card": "#A63028",
    "Defense Card": "#2456A6",
    "Pentester Tactic": "#701C1C",
    "Server Card": "#2E7D46",
    "Device Card": "#2E7D46",
    "Architecture Card": "#2E7D46",
    "Crisis Action": "#C06515",
    "Event Card": "#5F3B93",
    "Stakeholder Card": "#B8922A",
    "Investigation Card": "#1E6E6C",
    "Evidence Card": "#5C6570",
    "Audit Domain": "#6E4A2B",
}
FALLBACK_COLOR = "#333333"
INK = "#161616"
PAPER = "#FFFFFF"
MUTED = "#5A5A5A"
GLOW = "#2E9E4F"  # phosphor green accent, matches the back art

_FONT_DIRS = [
    "/System/Library/Fonts/Supplemental/Courier New Bold.ttf",
    "/System/Library/Fonts/Supplemental/Courier New.ttf",
    "/System/Library/Fonts/Menlo.ttc",
]


def _font(path, size):
    return ImageFont.truetype(path, size)


def fonts(scale=1.0):
    s = lambda px: max(12, round(px * scale))
    return {
        "type": _font(_FONT_DIRS[0], s(30)),
        "title": _font(_FONT_DIRS[0], s(44)),
        "label": _font(_FONT_DIRS[0], s(24)),
        "field": _font(_FONT_DIRS[1], s(26)),
        "body": _font(_FONT_DIRS[2], s(26)),
        "footer": _font(_FONT_DIRS[1], s(20)),
    }


def wrap(draw, text, font, max_w):
    lines, line = [], ""
    for word in text.split():
        probe = f"{line} {word}".strip()
        if draw.textlength(probe, font=font) <= max_w:
            line = probe
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def _layout_height(draw, card, f, max_w):
    """Total content height below the header band at a given font scale."""
    h = 0
    title_lines = wrap(draw, card["title"].upper(), f["title"], max_w)
    h += len(title_lines) * round(f["title"].size * 1.15) + 26
    h += len(card["fields"]) * round(f["field"].size * 1.5) + 20
    for label, text in card["sections"]:
        if label:
            h += round(f["label"].size * 1.6)
        h += len(wrap(draw, text, f["body"], max_w)) * round(f["body"].size * 1.32)
        h += 26
    return h


def render_face(card, module=""):
    img = Image.new("RGB", (CARD_W, CARD_H), PAPER)
    draw = ImageDraw.Draw(img)
    color = TYPE_COLORS.get(card["card_type"], FALLBACK_COLOR)
    max_w = CARD_W - 2 * MARGIN

    # shrink type until the card fits above the footer
    scale = 1.0
    while scale > 0.62:
        f = fonts(scale)
        band_h = 96
        avail = CARD_H - band_h - 30 - 70  # header, padding, footer
        if _layout_height(draw, card, f, max_w) <= avail:
            break
        scale -= 0.05
    f = fonts(scale)

    # frame + header band
    draw.rectangle([10, 10, CARD_W - 11, CARD_H - 11], outline=INK, width=3)
    draw.rectangle([10, 10, CARD_W - 11, 106], fill=color)
    draw.text((MARGIN, 40), card["card_type"].upper(), font=f["type"], fill=PAPER)
    id_w = draw.textlength(card["id"], font=f["type"])
    draw.text((CARD_W - MARGIN - id_w, 40), card["id"], font=f["type"], fill=PAPER)

    y = 136
    for line in wrap(draw, card["title"].upper(), f["title"], max_w):
        draw.text((MARGIN, y), line, font=f["title"], fill=INK)
        y += round(f["title"].size * 1.15)
    y += 10
    draw.line([MARGIN, y, CARD_W - MARGIN, y], fill=color, width=4)
    y += 16

    for label, value in card["fields"].items():
        draw.text((MARGIN, y), f"{label.upper()}: ", font=f["label"], fill=MUTED)
        x = MARGIN + draw.textlength(f"{label.upper()}: ", font=f["label"])
        draw.text((x, y), value, font=f["field"], fill=INK)
        y += round(f["field"].size * 1.5)
    if card["fields"]:
        y += 20

    for label, text in card["sections"]:
        if label:
            draw.text((MARGIN, y), label.upper(), font=f["label"], fill=color)
            y += round(f["label"].size * 1.6)
        for line in wrap(draw, text, f["body"], max_w):
            draw.text((MARGIN, y), line, font=f["body"], fill=INK)
            y += round(f["body"].size * 1.32)
        y += 26

    footer = f"INCIDENT ZERO{' · ' + module.upper() if module else ''}"
    fw = draw.textlength(footer, font=f["footer"])
    draw.line([MARGIN, CARD_H - 64, CARD_W - MARGIN, CARD_H - 64], fill="#CCCCCC", width=2)
    draw.text(((CARD_W - fw) / 2, CARD_H - 52), footer, font=f["footer"], fill=MUTED)
    return img


def render_back(art_path, deck_name):
    art = Image.open(art_path).convert("RGB")
    # crop-fit to card aspect
    target = CARD_W / CARD_H
    w, h = art.size
    if w / h > target:
        new_w = int(h * target)
        art = art.crop(((w - new_w) // 2, 0, (w + new_w) // 2, h))
    else:
        new_h = int(w / target)
        art = art.crop((0, (h - new_h) // 2, w, (h + new_h) // 2))
    art = art.resize((CARD_W, CARD_H), Image.LANCZOS)

    draw = ImageDraw.Draw(art, "RGBA")
    label_font = _font(_FONT_DIRS[0], 46)
    text = " ".join(deck_name.upper())  # letterspacing via literal spaces
    tw = draw.textlength(text, font=label_font)
    band_y = CARD_H - 172
    draw.rectangle([56, band_y, CARD_W - 56, band_y + 84], fill=(0, 0, 0, 215))
    draw.rectangle([56, band_y, CARD_W - 56, band_y + 84], outline=GLOW, width=2)
    draw.text(((CARD_W - tw) / 2, band_y + 18), text, font=label_font, fill=GLOW)
    return art


BACKS_DIR = Path(__file__).resolve().parents[2] / "assets" / "art" / "backs"

BACK_FOR_TYPE = {
    "Threat Card": ("threat.png", "Threat"),
    "Defense Card": ("defense.png", "Defense"),
    "Pentester Tactic": ("pentester.png", "Pentester"),
    "Event Card": ("event.png", "Event"),
    "Crisis Action": ("crisis-action.png", "Crisis"),
    "Stakeholder Card": ("stakeholder.png", "Stakeholder"),
    "Investigation Card": ("investigation.png", "Investigate"),
    "Evidence Card": ("evidence.png", "Evidence"),
    "Server Card": ("network.png", "Network"),
    "Device Card": ("network.png", "Network"),
    "Architecture Card": ("network.png", "Network"),
    "Audit Domain": ("audit.png", "Audit"),
}


def back_for(card_type):
    fname, label = BACK_FOR_TYPE.get(card_type, ("threat.png", "Incident Zero"))
    return render_back(BACKS_DIR / fname, label)
