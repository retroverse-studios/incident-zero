"""Render the landing-page component previews from the real pipeline output.

Output (assets/site/):
  components-fan.png  — five real cards fanned like a table shot
  mat-preview.png     — forensics play mat thumbnail
  tile-preview.png    — DMZ zone tile thumbnail
Rerun after visual changes to cards/mats/tiles so the site never shows
stale components.
"""

import sys
from pathlib import Path

from PIL import Image, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract import parse_file
from render import back_for, render_face
import build_mats
import build_tiles

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "assets" / "site"


def with_shadow(img, angle):
    img = img.convert("RGBA").rotate(angle, expand=True, resample=Image.BICUBIC)
    shadow = Image.new("RGBA", (img.width + 40, img.height + 40), (0, 0, 0, 0))
    sil = Image.new("RGBA", img.size, (0, 0, 0, 160))
    sil.putalpha(img.getchannel("A").point(lambda a: a * 160 // 255))
    shadow.paste(sil, (24, 28), sil)
    shadow = shadow.filter(ImageFilter.GaussianBlur(10))
    shadow.paste(img, (20, 20), img)
    return shadow


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    ir = parse_file(ROOT / "cards/incident-response/core-deck/threat-defense-cards.md")
    inv = [c for c in parse_file(ROOT / "cards/forensics/core-deck/investigation-cards.md",
                                 "Investigation Card") if c["is_card"]]
    evt = [c for c in parse_file(ROOT / "cards/network-building/standalone/operational-event-cards.md",
                                 "Event Card") if c["is_card"]]
    cards = [
        back_for("Threat Card"),
        render_face(ir[0], "Incident Response"),          # T-01, red
        render_face(ir[12], "Incident Response"),         # D-01, blue
        render_face(evt[4], "Network Building"),          # EVT-05, purple + art
        render_face(inv[0], "Forensics"),                 # DISK-01, teal
    ]
    angles = [-11, -5.5, 0, 5.5, 11]
    scale_w = 330
    fan = Image.new("RGBA", (1460, 620), (0, 0, 0, 0))
    x = 0
    for card, ang in zip(cards, angles):
        c = card.resize((scale_w, int(scale_w * card.height / card.width)), Image.LANCZOS)
        s = with_shadow(c, ang)
        fan.alpha_composite(s, (x, 30 + abs(int(ang * 6))))
        x += 222
    fan = fan.crop(fan.getbbox())
    fan.save(OUT / "components-fan.png", optimize=True)

    build_mats.mat_forensics().resize((820, 580), Image.LANCZOS).save(
        OUT / "mat-preview.png", optimize=True)
    build_tiles.zone_tile(*build_tiles.ZONES[1]).resize((820, 580), Image.LANCZOS).save(
        OUT / "tile-preview.png", optimize=True)
    for f in ("components-fan.png", "mat-preview.png", "tile-preview.png"):
        print(f, (OUT / f).stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()
