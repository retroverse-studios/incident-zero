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
    "Framework Card": "#6E4A2B",
    "Asset Card": "#2E7D46",
    "Requirement Card": "#2E7D46",
    "Scenario Card": "#5F3B93",
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
    for label, value in card["fields"].items():
        lw = draw.textlength(f"{label.upper()}: ", font=f["label"])
        h += len(wrap(draw, value, f["field"], max_w - lw)) * round(f["field"].size * 1.5)
    if card["fields"]:
        h += 20
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
    band_h = 96
    avail = CARD_H - band_h - 30 - 70  # header, padding, footer
    while scale > 0.52:
        f = fonts(scale)
        if _layout_height(draw, card, f, max_w) <= avail:
            break
        scale -= 0.05
    f = fonts(scale)
    # last resort: drop trailing sections; the markdown keeps the full text
    truncated = False
    card = dict(card, sections=list(card["sections"]))
    while len(card["sections"]) > 1 and _layout_height(draw, card, f, max_w) > avail:
        card["sections"].pop()
        truncated = True
    if truncated:
        print(f"  note: {card['id']} trimmed to fit; card points to module rules")
    if _layout_height(draw, card, f, max_w) > avail:
        print(f"  WARNING: {card['id']} still overflows at minimum text size")

    # frame + header band
    draw.rectangle([10, 10, CARD_W - 11, CARD_H - 11], outline=INK, width=3)
    draw.rectangle([10, 10, CARD_W - 11, 106], fill=color)
    tx = MARGIN
    type_icon = icon(ICON_FOR_TYPE.get(card["card_type"], ""), 56, PAPER)
    if type_icon:
        img.paste(type_icon, (MARGIN - 6, 30), type_icon)
        tx += 68
    draw.text((tx, 40), card["card_type"].upper(), font=f["type"], fill=PAPER)
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
        label_txt = f"{label.upper()}: "
        draw.text((MARGIN, y), label_txt, font=f["label"], fill=MUTED)
        x = MARGIN + draw.textlength(label_txt, font=f["label"])
        lines = wrap(draw, value, f["field"], max_w - (x - MARGIN))
        for line in lines:
            draw.text((x, y), line, font=f["field"], fill=INK)
            y += round(f["field"].size * 1.5)
        if label.lower().rstrip("s") in ("vector", "countermeasure"):
            ix = x + draw.textlength(lines[-1], font=f["field"]) + 18
            size = f["field"].size + 6
            for name in vector_icons_for(value):
                glyph = icon(name, size, INK)
                if glyph and ix + size < CARD_W - MARGIN:
                    img.paste(glyph, (int(ix), int(y - size * 1.45)), glyph)
                    ix += size + 10
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

    if truncated:
        draw.text((MARGIN, CARD_H - 106), "▸ CONTINUED IN MODULE RULES", font=f["label"], fill=GLOW)

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
ICONS_DIR = Path(__file__).resolve().parents[2] / "assets" / "art" / "icons"

ICON_FOR_TYPE = {
    "Threat Card": "type-threat",
    "Defense Card": "type-defense",
    "Pentester Tactic": "type-pentester",
    "Event Card": "type-event",
    "Crisis Action": "type-crisis",
    "Stakeholder Card": "type-stakeholder",
    "Investigation Card": "type-investigation",
    "Evidence Card": "type-evidence",
    "Server Card": "type-network",
    "Device Card": "type-network",
    "Architecture Card": "type-network",
    "Asset Card": "type-network",
    "Requirement Card": "type-network",
    "Scenario Card": "type-event",
    "Audit Domain": "type-audit",
    "Framework Card": "type-audit",
}

# attack-vector icons double as the colorblind-accessibility fix: the
# vector is identified by glyph as well as by text
VECTOR_ICONS = [
    ("social", "vector-social"),
    ("web", "vector-web"),
    ("credential", "vector-credential"),
    ("malware", "vector-malware"),
    ("exfil", "vector-exfil"),
    ("network", "vector-network"),
]

_icon_cache = {}


def icon(name, size, color):
    """Return the glyph tinted to color, or None if the asset is missing."""
    key = (name, size, color)
    if key not in _icon_cache:
        path = ICONS_DIR / f"{name}.png"
        if not path.exists():
            _icon_cache[key] = None
        else:
            mask = Image.open(path).convert("RGBA").getchannel("A").resize(
                (size, size), Image.LANCZOS)
            tile = Image.new("RGBA", (size, size), color)
            tile.putalpha(mask)
            _icon_cache[key] = tile
    return _icon_cache[key]


def vector_icons_for(value):
    v = value.lower()
    hits = [name for kw, name in VECTOR_ICONS if kw in v]
    # "network" is a substring trap ("social engineering" isn't, but keep
    # exfil before network so DATA_EXFIL doesn't double-match) — dedupe
    return list(dict.fromkeys(hits))

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
    "Framework Card": ("audit.png", "Framework"),
    "Asset Card": ("network.png", "Asset"),
    "Requirement Card": ("network.png", "Requirement"),
    "Scenario Card": ("event.png", "Scenario"),
}


def back_for(card_type):
    fname, label = BACK_FOR_TYPE.get(card_type, ("threat.png", "Incident Zero"))
    return render_back(BACKS_DIR / fname, label)
