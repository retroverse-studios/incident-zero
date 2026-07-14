"""Render the Network Building zone tiles: A4 pages that butt together into
a network board. Players place Server / Device / Asset cards onto the printed
card slots, so the module's hand-drawn network diagram becomes a physical
board — and IR/Forensics threat tokens can sit on the compromised zone.

Output: downloads/print-pack/network-zone-tiles.pdf (A4 landscape @300 DPI).
"""

from pathlib import Path

from PIL import Image, ImageDraw

from build_mats import F, BOLD, MONO, INK, PAPER, MUTED, GLOW
from render import CARD_W, CARD_H

ROOT = Path(__file__).resolve().parents[2]
W, H = 3508, 2480
M = 110

ZONES = [
    ("INTERNET EDGE", "Untrusted outside world — ISP link, public traffic arrives here.",
     "Firewall / gateway devices sit on the border to the DMZ →"),
    ("DMZ", "Semi-trusted segment for external-facing services (web, email, VPN).",
     "← border to Internet Edge · border to Internal Network →"),
    ("INTERNAL NETWORK", "Trusted user LAN — workstations, print, internal apps.",
     "← border to DMZ · border to Data Center →"),
    ("DATA CENTER", "Most protected segment — databases, file servers, backups.",
     "← border to Internal Network"),
    ("CLOUD", "Provider-hosted services — attaches to the Internet Edge tile.",
     "↑ place beside Internet Edge"),
]


def dashed_rect(d, box, dash=28, gap=18, width=4, fill=MUTED):
    x0, y0, x1, y1 = box
    for (ax, ay, bx, by, horiz) in [(x0, y0, x1, y0, True), (x0, y1, x1, y1, True),
                                    (x0, y0, x0, y1, False), (x1, y0, x1, y1, False)]:
        pos = ax if horiz else ay
        end = bx if horiz else by
        while pos < end:
            seg = min(pos + dash, end)
            if horiz:
                d.line([pos, ay, seg, ay], fill=fill, width=width)
            else:
                d.line([ax, pos, ax, seg], fill=fill, width=width)
            pos = seg + gap


def chevrons(d, x, y, direction=1, color=GLOW):
    for i in range(3):
        cx = x + i * 46 * direction
        d.line([cx, y - 40, cx + 40 * direction, y], fill=color, width=10)
        d.line([cx + 40 * direction, y, cx, y + 40], fill=color, width=10)


def zone_tile(name, desc, links):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 240], fill=INK)
    for y in range(8, 240, 14):
        d.line([0, y, W, y], fill="#262626", width=3)
    d.text((M, 60), name, font=F(BOLD, 96), fill=GLOW)
    d.text((M, 175), desc, font=F(MONO, 34), fill="#B9B9B9")
    d.rectangle([0, 240, W, 256], fill=GLOW)

    # connector chevrons on the side edges so tiles read as joinable
    chevrons(d, 40, H / 2, 1)
    chevrons(d, W - 40, H / 2, -1)
    d.text((M, H - 90), f"NETWORK ZONE TILE · {links}", font=F(MONO, 32), fill=MUTED)
    brand = "INCIDENT ZERO"
    d.text((W - M - d.textlength(brand, font=F(BOLD, 34)), H - 92), brand,
           font=F(BOLD, 34), fill=MUTED)

    # 3 x 2 true-size card slots (landscape: cards lie sideways on the board)
    slot_w, slot_h = CARD_H, CARD_W
    gap_x = (W - 2 * (M + 130) - 3 * slot_w) / 2
    gap_y = 110
    top = 400
    for r in range(2):
        for c in range(3):
            x0 = M + 130 + c * (slot_w + gap_x)
            y0 = top + r * (slot_h + gap_y)
            dashed_rect(d, (x0, y0, x0 + slot_w, y0 + slot_h))
            hint = "PLACE CARD"
            d.text((x0 + (slot_w - d.textlength(hint, font=F(BOLD, 36))) / 2,
                    y0 + slot_h / 2 - 20), hint, font=F(BOLD, 36), fill="#D8D8D4")
    return img


def main():
    pages = [zone_tile(*z) for z in ZONES]
    out_dir = ROOT / "downloads" / "print-pack"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "network-zone-tiles.pdf"
    pages[0].save(out, save_all=True, append_images=pages[1:], resolution=300.0)
    print(f"zone tiles -> {out.relative_to(ROOT)} ({len(pages)} pages)")


if __name__ == "__main__":
    main()
