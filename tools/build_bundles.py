#!/usr/bin/env python3
"""Build self-contained print-and-play HTML bundles for Incident Zero.

Each bundle concatenates the markdown docs a table actually needs into one
styled, printer-friendly HTML file under downloads/. Re-run after editing
any rules or cards:  python3 tools/build_bundles.py
"""

import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "downloads"

COMMON = [
    "docs/HOW_TO_PLAY.md",
    "docs/TO_GUIDE.md",
    "docs/rules/core-rules.md",
]
TRACKERS = ["cards/print-templates/tracker-sheets.md"]

MODULES = {
    "network-building": {
        "title": "Network Building",
        "files": [
            "docs/rules/module-network-building.md",
            "docs/standalone-games/network-building.md",
            "cards/network-building/core-deck/server-cards.md",
            "cards/network-building/core-deck/security-device-cards.md",
            "cards/network-building/core-deck/architecture-cards.md",
            "cards/network-building/core-deck/asset-cards.md",
            "cards/network-building/standalone/business-requirement-cards.md",
            "cards/network-building/standalone/operational-event-cards.md",
            "cards/network-building/expansion-deck/legacy-systems.md",
            "cards/network-building/expansion-deck/cloud-variants.md",
        ],
    },
    "hardening": {
        "title": "Hardening",
        "files": [
            "docs/rules/module-hardening.md",
            "docs/standalone-games/hardening.md",
            "cards/hardening/core-deck/defense-cards.md",
            "cards/hardening/core-deck/pentester-tactic-cards.md",
            "cards/hardening/expansion-deck/advanced-tactics.md",
        ],
    },
    "incident-response": {
        "title": "Incident Response",
        "files": [
            "docs/rules/module-incident-response.md",
            "docs/standalone-games/incident-response.md",
            "cards/incident-response/core-deck/threat-defense-cards.md",
            "cards/incident-response/expansion-deck/advanced-threats.md",
            "cards/incident-response/expansion-deck/advanced-defenses.md",
        ],
    },
    "disaster-recovery": {
        "title": "Disaster Recovery",
        "files": [
            "docs/rules/module-disaster-recovery.md",
            "docs/standalone-games/disaster-recovery.md",
            "cards/disaster-recovery/core-deck/crisis-action-cards.md",
            "cards/disaster-recovery/core-deck/event-cards.md",
            "cards/disaster-recovery/core-deck/stakeholder-cards.md",
            "cards/disaster-recovery/expansion-deck/advanced-scenarios.md",
        ],
    },
    "forensics": {
        "title": "Forensics",
        "files": [
            "docs/rules/module-forensics.md",
            "docs/standalone-games/forensics.md",
            "cards/forensics/core-deck/investigation-cards.md",
            "cards/forensics/core-deck/evidence-cards.md",
        ],
    },
    "audit-compliance": {
        "title": "Audit & Compliance",
        "files": [
            "docs/rules/module-audit-compliance.md",
            "docs/standalone-games/audit-compliance.md",
            "cards/audit-compliance/core-deck/audit-domain-cards.md",
            "cards/audit-compliance/expansion-deck/compliance-frameworks.md",
        ],
    },
}

COMPLETE_EXTRAS = [
    "docs/FRAMEWORK.md",
    "docs/module-combinations.md",
    "docs/VARIABLE_GAME_LENGTH_SYSTEM.md",
    "cards/CARD_REFERENCE.md",
]

CSS = """
:root { color-scheme: light; }
* { box-sizing: border-box; }
body { font-family: Georgia, 'Times New Roman', serif; line-height: 1.5;
       max-width: 52rem; margin: 0 auto; padding: 2rem 1.25rem; color: #1a1a1a; }
h1, h2, h3, h4 { font-family: 'Helvetica Neue', Arial, sans-serif; line-height: 1.25; }
h1 { border-bottom: 3px solid #1a1a1a; padding-bottom: .3rem; }
h2 { border-bottom: 1px solid #999; padding-bottom: .2rem; margin-top: 2.2rem; }
pre, code { font-family: 'Courier New', monospace; font-size: .85em; }
pre { background: #f4f4f4; border: 1px solid #ddd; padding: .8rem;
      overflow-x: auto; white-space: pre; }
table { border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: .92em; }
th, td { border: 1px solid #888; padding: .35rem .55rem; text-align: left; vertical-align: top; }
th { background: #eee; }
blockquote { border-left: 4px solid #888; margin-left: 0; padding-left: 1rem; color: #444; }
hr { border: none; border-top: 1px solid #bbb; margin: 2rem 0; }
a { color: #0b5394; }
.doc-break { page-break-before: always; break-before: page; border-top: 6px double #1a1a1a;
             margin-top: 3rem; padding-top: 1rem; }
.doc-src { font-family: 'Courier New', monospace; font-size: .75rem; color: #777;
           text-transform: uppercase; letter-spacing: .08em; }
.bundle-cover { text-align: center; padding: 4rem 0 2rem; page-break-after: always; }
.bundle-cover h1 { border: none; font-size: 2.6rem; }
.bundle-cover .toc { text-align: left; display: inline-block; margin-top: 2rem; }
@media print {
  body { max-width: none; padding: 0; font-size: 11pt; }
  a { color: inherit; text-decoration: none; }
  pre { white-space: pre-wrap; }
}
"""

MD = markdown.Markdown(extensions=["tables", "fenced_code"], tab_length=4)


def render(md_path: Path) -> str:
    text = md_path.read_text(encoding="utf-8")
    # Strip relative markdown links (targets don't exist inside a bundle) but keep the label.
    text = re.sub(r"\[([^\]]+)\]\((?!https?://|#)[^)]+\)", r"\1", text)
    MD.reset()
    return MD.convert(text)


def build(name: str, title: str, files: list[str]) -> None:
    parts, toc = [], []
    for i, rel in enumerate(files):
        p = ROOT / rel
        if not p.exists():
            raise SystemExit(f"missing file in bundle '{name}': {rel}")
        cls = "doc-break" if i else ""
        toc.append(f"<li>{rel}</li>")
        parts.append(
            f'<section class="{cls}"><p class="doc-src">{rel}</p>{render(p)}</section>'
        )
    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Incident Zero — {title} (Print &amp; Play)</title>
<style>{CSS}</style></head><body>
<div class="bundle-cover">
  <h1>INCIDENT ZERO</h1>
  <p><strong>{title}</strong> — Print &amp; Play Bundle · v2.2 Playtest Edition</p>
  <p>A cybersecurity board game by RetroVerse Studios · CC BY-NC-SA 4.0</p>
  <p>Print this file (Ctrl/Cmd+P) or read on screen. Card pages print best on cardstock.</p>
  <div class="toc"><strong>Contents:</strong><ol>{''.join(toc)}</ol></div>
</div>
{''.join(parts)}
</body></html>"""
    out = OUT / f"incident-zero-{name}.html"
    out.write_text(html, encoding="utf-8")
    print(f"built {out.relative_to(ROOT)}  ({out.stat().st_size // 1024} KB)")


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for name, spec in MODULES.items():
        build(name, spec["title"], COMMON + spec["files"] + TRACKERS)
    all_files = COMMON + COMPLETE_EXTRAS[:3]
    for spec in MODULES.values():
        all_files += spec["files"]
    all_files += TRACKERS + [COMPLETE_EXTRAS[3]]
    build("complete", "Complete Game (All 6 Modules)", all_files)


if __name__ == "__main__":
    main()
