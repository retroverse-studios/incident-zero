# Incident Zero — Art Assets

**Style decision (2026-07-14, FUTURE_WORK #18):** all generated art uses the
locked **pixel noir** identity. Every prompt starts with this canonical prefix:

```
pixel art film noir, high contrast black and white 8-bit pixel art,
dramatic chiaroscuro, venetian blind shadows, single green phosphor glow
as the only color, dark moody retro computing aesthetic, no text, no
letters, no words
```

Card backs additionally append:
`ornate playing card back composition with symmetrical border frame, central emblem: <deck motif>`

## Regenerating

Images were generated with [limn](https://github.com/) → Gemini/Imagen 4
(`limn -p gemini -s 768x1024 -M -o <name>.png "<prefix>, central emblem: <motif>"`).
Each `.png.json` sidecar records the exact prompt and parameters — regenerate
any asset from its sidecar, or re-render the whole set with the
`pixel-art-xl` LoRA on SwarmUI once its backend is up
(`--lora pixel-art-xl:1.0`, trigger word `pixelbuildings128`).

## backs/

One back per card type (deck motifs, all face-down decks get uniform backs):

| File | Deck / card type |
|------|------------------|
| threat.png | Threat (IR) — hooded figure at terminal |
| defense.png | Defense (IR / Hardening) — vault door |
| pentester.png | Pentester Tactic (Hardening) — lockpick |
| event.png | Event (DR) — noir street scene |
| crisis-action.png | Crisis Action (DR) — emergency telephone |
| stakeholder.png | Stakeholder (DR) — boardroom |
| investigation.png | Investigation (Forensics) — magnifier over CRT |
| evidence.png | Evidence / Findings (Forensics) — case file |
| network.png | Server / Device / Architecture (Network Building) — isometric racks |
| audit.png | Audit Domain / Framework (Audit & Compliance) — stamp & ledger |

The deck name is overlaid at render time by `tools/cardgen/render.py` —
the source art stays text-free.

## icons/

16 one-bit pixel glyphs: 10 card-type icons (header band of every card face)
and 6 attack-vector icons (drawn beside Vector/Countermeasure fields). The
vector icons are the colorblind-accessibility fix from FUTURE_WORK #10 —
vectors are identified by glyph as well as text, never by color alone.

Raw limn output lives in `icons/raw/` (with `.png.json` prompt sidecars);
`tools/cardgen/build_icons.py` thresholds them into centered 256px RGBA
glyph masks that `render.py` tints at draw time.

## Hero banner

`hero-banner.png` (1280×640) — README top, docsify coverpage, and sized for
the GitHub social preview (upload it under repo Settings → Social preview).
Rebuild with `tools/cardgen/build_hero.py` (composites the title over
`hero-raw.png`; regenerate the scene from `hero-raw.png.json`).
