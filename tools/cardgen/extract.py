"""Parse Incident Zero card markdown into structured card records.

The markdown files in cards/ are the single source of truth; nothing here is
hand-maintained card data. Two formats exist in the repo:

- box format: ``#### Card T-01: Title`` followed by a fenced ASCII box
  (incident-response, forensics use this)
- field format: ``### D-01: Title`` followed by ``**Field:** value`` lines
  (hardening, network-building use this)

parse_file() sniffs per card block and returns a list of Card dicts:
  {id, title, card_type, fields: {label: value}, sections: [(label, text)]}
"""

import re
from pathlib import Path

HEADING_RE = re.compile(r"^#{3,4} (?:Card )?([A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)*?-\d{2,3}): (.+)$")
ID_BANNER_RE = re.compile(r"^[A-Z][A-Za-z0-9-]*-\d{2,3}:", re.IGNORECASE)
BOX_EDGE = "┌┐└┘╔╗╚╝"
BOX_SEP = "├╠"
FIELD_RE = re.compile(r"^\*\*([^*]+):\*\*\s*(.*)$")
KV_RE = re.compile(r"^([A-Za-z][A-Za-z &/]+):\s{1,}(\S.*)$")


def _strip_box_line(line):
    line = line.rstrip()
    if line and line[0] in "│║":
        line = line[1:]
    if line and line[-1] in "│║":
        line = line[:-1]
    return line.strip()


def _parse_box(box_lines):
    """Split an ASCII box into segments on the ├──┤ / ╠══╣ rule lines."""
    segments, current = [], []
    for raw in box_lines:
        if not raw.strip():
            continue
        ch = raw.strip()[0]
        if ch in BOX_EDGE:
            continue
        if ch in BOX_SEP:
            if current:
                segments.append(current)
                current = []
            continue
        current.append(_strip_box_line(raw))
    if current:
        segments.append(current)

    # Box headers vary: "THREAT CARD" is a type banner (title block follows);
    # "DISK-01: DISK IMAGE" is a title banner (no type); architecture boxes
    # open straight with content (a topology diagram line).
    if not segments or not segments[0]:
        return "", {}, []
    card_type, fields, sections = "", {}, []
    first = segments[0][0]
    if len(segments[0]) == 1 and first.upper().endswith("CARD"):
        card_type = first.title()
        # segment 1 is the title block; a second line like "(BASIC - 10 Budget)"
        # carries tier/cost
        if len(segments) > 1 and len(segments[1]) > 1:
            extra = " ".join(segments[1][1:]).strip("() ")
            if extra:
                fields["Tier"] = extra
        body = segments[2:]
    elif ID_BANNER_RE.match(first):
        body = segments[1:]
    else:
        body = segments

    for seg in body:
        text = [l for l in seg if l]
        if not text:
            continue
        first = text[0]
        if first.endswith(":") and len(text) > 1:  # labeled paragraph
            sections.append((first.rstrip(":").title(), " ".join(text[1:])))
            continue
        matched_kv = False
        for line in text:
            m = KV_RE.match(line)
            if m and len(m.group(2)) < 60:
                fields[m.group(1).strip().title()] = m.group(2).strip()
                matched_kv = True
            elif matched_kv and fields:
                # continuation of the previous value (wrapped line)
                last = list(fields)[-1]
                fields[last] += " " + line
        if not matched_kv:
            sections.append(("", " ".join(text)))
    return card_type, fields, sections


def _parse_fields(body_lines):
    """Parse a **Field:** value card body (hardening / network-building)."""
    fields, sections = {}, []
    label, buf = None, []

    def flush():
        nonlocal buf, label
        text = " ".join(l.strip() for l in buf if l.strip())
        text = text.replace("**", "")
        if text:
            sections.append((label or "", text))
        label, buf = None, []

    for line in body_lines:
        stripped = line.strip()
        if stripped == "---":
            continue
        m = FIELD_RE.match(stripped)
        if m:
            if m.group(2):
                flush()
                fields[m.group(1).strip()] = m.group(2).strip()
            else:  # "**Description:**" header for a following paragraph
                flush()
                label = m.group(1).strip()
            continue
        if stripped.startswith("- ") and label:
            buf.append(stripped[2:] + ";")
        elif stripped or buf:
            buf.append(stripped)
    flush()
    return fields, sections


def parse_file(path, default_type=""):
    """Return a list of card dicts from one markdown card file."""
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    cards, i = [], 0
    while i < len(lines):
        m = HEADING_RE.match(lines[i])
        if not m:
            i += 1
            continue
        card_id, title = m.group(1), m.group(2).strip()
        # collect until next card heading or section heading
        j = i + 1
        block = []
        while j < len(lines) and not HEADING_RE.match(lines[j]) and not lines[j].startswith("## "):
            block.append(lines[j])
            j += 1

        fence = [k for k, l in enumerate(block) if l.strip().startswith("```")]
        # a fenced block is only a card box if it draws one; other fences
        # (e.g. audit findings templates) are worksheets, not card content
        has_box = (
            len(fence) >= 2
            and fence[0] + 1 < fence[1]
            and block[fence[0] + 1].strip()[:1] in "┌╔"
        )
        if has_box:
            card_type, fields, sections = _parse_box(block[fence[0] + 1:fence[1]])
        else:
            card_type = default_type
            inside, field_lines = False, []
            for line in block:
                if line.strip().startswith("```"):
                    inside = not inside
                    continue
                if not inside:
                    field_lines.append(line)
            fields, sections = _parse_fields(field_lines)
        cards.append({
            "id": card_id,
            "title": title,
            "card_type": card_type or default_type,
            "fields": fields,
            "sections": sections,
            # a heading with neither a box nor **Field:** lines is a rules
            # cross-reference (e.g. "### PT-01: ..." interaction notes), not a card
            "is_card": has_box or bool(fields),
        })
        i = j
    return cards


if __name__ == "__main__":
    import json
    import sys

    for p in sys.argv[1:]:
        cards = parse_file(p)
        print(f"{p}: {len(cards)} cards")
        print(json.dumps(cards[0], indent=2)[:800])
