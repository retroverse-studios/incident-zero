"""Compose the hero banner: generated pixel-noir scene + title overlay.

Input:  assets/art/hero-raw.png (limn output, 16:9)
Output: assets/art/hero-banner.png — 1280x640, GitHub social-preview size.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
W, H = 1280, 640
GLOW = "#3DDC6A"
BOLD = "/System/Library/Fonts/Supplemental/Courier New Bold.ttf"
MONO = "/System/Library/Fonts/Menlo.ttc"


def main():
    art = Image.open(ROOT / "assets" / "art" / "hero-raw.png").convert("RGB")
    # crop-fit to 2:1
    w, h = art.size
    if w / h > W / H:
        nw = int(h * W / H)
        art = art.crop(((w - nw) // 2, 0, (w + nw) // 2, h))
    else:
        nh = int(w * H / W)
        art = art.crop((0, (h - nh) // 2, w, (h + nh) // 2))
    img = art.resize((W, H), Image.LANCZOS)

    # darken the lower-left for the title block
    overlay = Image.new("L", (W, H), 0)
    od = ImageDraw.Draw(overlay)
    for i in range(H):
        od.line([0, i, W, i], fill=int(30 + 150 * (i / H) ** 2))
    img = Image.composite(Image.new("RGB", (W, H), "#050705"), img, overlay)

    d = ImageDraw.Draw(img)
    title = ImageFont.truetype(BOLD, 104)
    tag = ImageFont.truetype(BOLD, 34)
    sub = ImageFont.truetype(MONO, 22)

    x, y = 56, H - 250
    d.text((x + 3, y + 3), "INCIDENT ZERO", font=title, fill="#031007")
    d.text((x, y), "INCIDENT ZERO", font=title, fill=GLOW)
    d.text((x + 6, y + 122), "THE ATTACKER IS ALREADY INSIDE.", font=tag, fill="#E8E8E4")
    d.text((x + 6, y + 172),
           "A print-and-play cybersecurity board game · six modules · one d20",
           font=sub, fill="#9AA59C")
    d.rectangle([0, 0, W - 1, H - 1], outline="#1A1F1B", width=2)

    out = ROOT / "assets" / "art" / "hero-banner.png"
    img.save(out)
    print(f"hero banner -> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
