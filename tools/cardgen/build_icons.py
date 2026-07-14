"""Process raw generated icons into clean glyph masks.

Input:  assets/art/icons/raw/<name>.png — white glyph on black (limn output)
Output: assets/art/icons/<name>.png — 256x256 RGBA, black glyph on
        transparent, cropped and centered. render.py tints these at draw time.
"""

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "assets" / "art" / "icons" / "raw"
OUT = ROOT / "assets" / "art" / "icons"
SIZE = 256
THRESHOLD = 110


def process(path):
    g = Image.open(path).convert("L")
    mask = g.point(lambda p: 255 if p > THRESHOLD else 0)
    bbox = mask.getbbox()
    if not bbox:
        print(f"  WARNING: {path.name} produced an empty glyph")
        return
    mask = mask.crop(bbox)
    # square-pad, keep aspect
    side = max(mask.size)
    sq = Image.new("L", (side, side), 0)
    sq.paste(mask, ((side - mask.width) // 2, (side - mask.height) // 2))
    sq = sq.resize((SIZE - 24, SIZE - 24), Image.LANCZOS)
    final_mask = Image.new("L", (SIZE, SIZE), 0)
    final_mask.paste(sq, (12, 12))
    glyph = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    black = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 255))
    glyph.paste(black, (0, 0), final_mask)
    glyph.save(OUT / path.name)
    print(f"  {path.name}: ok")


def main():
    for p in sorted(RAW.glob("*.png")):
        if p.name.startswith("._"):  # macOS AppleDouble sidecars on exFAT
            continue
        process(p)


if __name__ == "__main__":
    main()
