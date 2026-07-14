"""Render the play mats: designed A4 replacements for the ASCII tracker sheets.

Content mirrors cards/print-templates/tracker-sheets.md (the source of truth
for track values and thresholds). Output: downloads/print-pack/play-mats.pdf,
A4 landscape @300 DPI, one mat per page. Laminate + dry-erase, or use tokens.
"""

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
W, H = 3508, 2480  # A4 landscape at 300 DPI
M = 130            # page margin
INK, PAPER, MUTED, GLOW = "#161616", "#FFFFFF", "#5A5A5A", "#2E9E4F"

BOLD = "/System/Library/Fonts/Supplemental/Courier New Bold.ttf"
MONO = "/System/Library/Fonts/Menlo.ttc"


def F(path, size):
    return ImageFont.truetype(path, size)


FT_TITLE = F(BOLD, 76)
FT_BRAND = F(BOLD, 34)
FT_SECTION = F(BOLD, 46)
FT_CELL = F(MONO, 34)
FT_NOTE = F(MONO, 32)
FT_SMALL = F(MONO, 28)


def new_mat(title, accent):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # header: black band, scanline texture, green title, accent underline
    d.rectangle([0, 0, W, 210], fill=INK)
    for y in range(8, 210, 14):
        d.line([0, y, W, y], fill="#262626", width=3)
    d.text((M, 62), title.upper(), font=FT_TITLE, fill=GLOW)
    brand = "INCIDENT ZERO"
    d.text((W - M - d.textlength(brand, font=FT_BRAND), 88), brand, font=FT_BRAND, fill="#8A8A8A")
    d.rectangle([0, 210, W, 226], fill=accent)
    return img, d


def section(d, x, y, text):
    d.text((x, y), text.upper(), font=FT_SECTION, fill=INK)
    return y + 78


def note(d, x, y, text, fill=MUTED, font=FT_NOTE):
    d.text((x, y), text, font=font, fill=fill)
    return y + 52


def track(d, x, y, width, labels, cell_h=90, boxes=False, marks=()):
    """A row of cells. labels above each cell; boxes=True draws tick squares.
    marks: label values that get a solid victory marker."""
    n = len(labels)
    gap = 10
    cw = (width - gap * (n - 1)) / n
    for i, lab in enumerate(labels):
        cx = x + i * (cw + gap)
        d.text((cx + (cw - d.textlength(str(lab), font=FT_CELL)) / 2, y), str(lab),
               font=FT_CELL, fill=INK if str(lab) not in map(str, marks) else GLOW)
        top = y + 52
        is_mark = str(lab) in map(str, marks)
        color, weight = (GLOW, 8) if is_mark else (INK, 4)
        if boxes:
            side = min(cell_h, cw * 0.7)
            bx = cx + (cw - side) / 2
            d.rectangle([bx, top, bx + side, top + side], outline=color, width=weight)
        else:
            d.rectangle([cx, top, cx + cw, top + cell_h], outline=color, width=weight)
    return y + 52 + cell_h + 46


def table(d, x, y, col_widths, headers, rows, row_h=88):
    """Simple grid; rows is a list of tuples (prefilled strings, '' = blank)."""
    total_w = sum(col_widths)
    # header row
    d.rectangle([x, y, x + total_w, y + row_h], fill="#EDEDE9", outline=INK, width=4)
    cx = x
    for wd, htext in zip(col_widths, headers):
        d.text((cx + 24, y + (row_h - 40) / 2), htext, font=F(BOLD, 36), fill=INK)
        cx += wd
    y += row_h
    for row in rows:
        cx = x
        for wd, cell in zip(col_widths, row):
            d.rectangle([cx, y, cx + wd, y + row_h], outline=INK, width=3)
            if cell:
                d.text((cx + 24, y + (row_h - 36) / 2), cell, font=FT_NOTE, fill=INK)
            cx += wd
        y += row_h
    return y + 40


def blank_line(d, x, y, label, width):
    d.text((x, y), label, font=FT_NOTE, fill=INK)
    lx = x + d.textlength(label, font=FT_NOTE) + 20
    d.line([lx, y + 40, x + width, y + 40], fill=INK, width=3)
    return y + 76


def mat_universal():
    img, d = new_mat("Universal Tracker", INK)
    x, width = M, W - 2 * M
    y = 300
    y = section(d, x, y, "Turn track — cross off each turn; circle your limit")
    y = track(d, x, y, width, list(range(1, 17)), boxes=True)
    y = section(d, x, y, "Budget track — tick down in 5s")
    y = track(d, x, y, width, list(range(150, 70, -5)))
    y = track(d, x, y, width, list(range(70, -1, -5)))
    y = note(d, x, y, "Starting budgets — Network Building 40-60 · Disaster Recovery 50 · "
                      "Forensics 75 · Incident Response 100 · Audit 100 · Hardening 150")
    y += 20
    y = section(d, x, y, "Reputation / score (0-100)")
    y = track(d, x, y, width, list(range(100, -1, -5)))
    y = section(d, x, y, "Uncontained threats (Incident Response)")
    y = track(d, x, y, width * 0.45, list(range(0, 6)), boxes=True)
    d.text((x + width * 0.5, y - 130), "Penalty at start of turn: -5 Budget each",
           font=FT_NOTE, fill=MUTED)
    y = section(d, x, y, "Table notes")
    d.rectangle([x, y, x + width, H - 110], outline=INK, width=4)
    return img


def meter(d, x, y, width, name, mark=None):
    d.text((x, y + 56), name, font=F(BOLD, 38), fill=INK)
    return track(d, x + 620, y, width - 620, list(range(0, 101, 10)),
                 cell_h=80, marks=(mark,) if mark else ())


def mat_forensics():
    img, d = new_mat("Forensics — Progress Meters", "#1E6E6C")
    x, width = M, W - 2 * M
    y = 290
    y = note(d, x, y, "Advance each meter per card effects. ▲ marks the victory threshold.")
    y += 10
    for name, mark in [("ATTRIBUTION", 90), ("TIMELINE", 80),
                       ("ATTACK CHAIN", 80), ("CHAIN OF CUSTODY", 70)]:
        y = meter(d, x, y, width, name, mark)
    y = section(d, x, y, "Victory check (end of game)")
    y = note(d, x, y, "V1 Full Attribution: Attribution ≥90 AND Timeline ≥80", INK)
    y = note(d, x, y, "V2 Solid Case: Timeline ≥80 AND Attack Chain ≥80 AND Chain of Custody ≥70", INK)
    y = note(d, x, y, "V3 Partial Findings: any two meters ≥70", INK)
    y += 14
    y = blank_line(d, x, y, "Investigation in flight:", width * 0.55)
    d.text((x + width * 0.6, y - 76), "results arrive Turn ____", font=FT_NOTE, fill=INK)
    y = section(d, x, y, "Evidence collected (one Analyze per card)")
    table(d, x, y, [int(width * 0.5), int(width * 0.25), int(width * 0.25)],
          ["Evidence card", "Documented? (+5% CoC)", "Analyzed?"],
          [("", "", "")] * 5, row_h=82)
    return img


def mat_disaster_recovery():
    img, d = new_mat("Disaster Recovery — Crisis Tracks", "#C06515")
    x, width = M, W - 2 * M
    y = 290
    for name in ("INVESTIGATION", "REMEDIATION", "COMMUNICATION"):
        y = meter(d, x, y, width, name)
    y = section(d, x, y, "Stakeholder trust (any stakeholder at 0% = company collapses)")
    cw = [int(width * 0.3)] + [int(width * 0.7 / 6)] * 6
    y = table(d, x, y, cw,
              ["Stakeholder", "100", "80", "60", "40", "20 CRIT", "0 LOSS"],
              [(s, "", "", "", "", "", "") for s in
               ("Customers", "Employees", "Regulators", "Board / Investors", "Media / Public")],
              row_h=80)
    y = section(d, x, y, "Deadline timeline (mark scheduled events at setup)")
    cw = [int(width * 0.16)] + [int(width * 0.84 / 8)] * 8
    y = table(d, x, y, cw,
              ["Turn", "1", "2", "3", "4", "5", "6", "7", "8"],
              [("Event", "", "", "", "", "", "", "", ""),
               ("Deadline", "", "", "", "", "Notify customers", "Reg. penalties", "", "GDPR 72h")],
              row_h=80)
    blank_line(d, x, y, "Multi-turn action in flight:", width * 0.55)
    d.text((x + width * 0.6, y + 4), "completes Turn ____", font=FT_NOTE, fill=INK)
    return img


def mat_audit():
    img, d = new_mat("Audit & Compliance — Scoring", "#6E4A2B")
    x, width = M, W - 2 * M
    y = 300
    cw = [int(width * 0.05), int(width * 0.3), int(width * 0.14),
          int(width * 0.19), int(width * 0.32)]
    y = table(d, x, y, cw,
              ["#", "Domain", "Stars (1-5)", "PASS (3+) / FAIL", "Key gap found"],
              [(str(i), dom, "", "", "") for i, dom in enumerate(
                  ("Network Segmentation", "Identity & Access", "Detection & Monitoring",
                   "Backup & Recovery", "Cloud Security", "Security Operations"), 1)],
              row_h=110)
    y = blank_line(d, x, y, "Result:", 460)
    d.text((x + 520, y - 76), "/ 6 PASS — gap penalties for follow-on modules capped at -30",
           font=FT_NOTE, fill=MUTED)
    y += 20
    y = section(d, x, y, "Finding worksheet (one per FAIL domain)")
    for lab in ("FINDING:", "SEVERITY (Critical / Major / Minor):",
                "RECOMMENDATION:", "EFFORT (weeks) / COST:"):
        y = blank_line(d, x, y, lab, width)
    return img


def mat_network():
    img, d = new_mat("Network Building — Score Sheet", "#2E7D46")
    x, width = M, W - 2 * M
    y = 290
    half = int(width * 0.47)
    y0 = section(d, x, y, "Scoring")
    table(d, x, y0, [int(half * 0.42), int(half * 0.18), int(half * 0.4)],
          ["Category", "Points", "Notes"],
          [("Requirements met", "", ""), ("Security coverage", "", ""),
           ("Capability coverage", "", ""), ("Budget management", "", ""),
           ("TOTAL", "", "")], row_h=96)
    x2 = x + half + int(width * 0.06)
    y0 = section(d, x2, y, "Components placed")
    y0 = table(d, x2, y0, [int(half * 0.5), int(half * 0.2), int(half * 0.3)],
               ["Component", "Cost", "Capacity used/total"],
               [("", "", "")] * 10, row_h=96)
    blank_line(d, x2, y0, "Budget remaining:", half * 0.6)
    d.text((x2 + half * 0.66, y0 + 4), "/ starting ____", font=FT_NOTE, fill=INK)
    return img


def main():
    mats = [mat_universal(), mat_forensics(), mat_disaster_recovery(),
            mat_audit(), mat_network()]
    out_dir = ROOT / "downloads" / "print-pack"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "play-mats.pdf"
    mats[0].save(out, save_all=True, append_images=mats[1:], resolution=300.0)
    print(f"play mats -> {out.relative_to(ROOT)} ({len(mats)} pages)")
    if "--png" in sys.argv:  # debug previews
        for i, m in enumerate(mats):
            m.resize((1170, 827)).save(out_dir / f"_mat{i}.png")


if __name__ == "__main__":
    main()
