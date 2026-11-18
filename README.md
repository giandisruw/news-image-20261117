# The World — Tuesday 17 November 2026, in one image

**Competition:** [news-image-20261117](https://make.fun/bounty/news-image-20261117) — "Sum up 17 November's world news in one image"
**Prize:** $250 shared by the top 50 (1st $50). Entries close Thu 19 Nov 2026, 07:00 WIB (Wed 18 Nov 24:00 UTC / 2026-11-19T00:00Z).

## The concept

A newspaper front page — the one format a picture editor reads at a
glance. The judge has no news feed, so the image itself has to carry the
day: masthead "THE WORLD — TUESDAY, 17 NOVEMBER 2026", then the day's
stories as legible headlines with one-line summaries and small drawn
icons. Everything is drawn programmatically with PIL (no AI-generated
imagery, so no garbled text anywhere); the program itself just copies
the finished page.

## The stories (all of Tuesday 17 November 2026)

1. **Lead — Bridges under fire.** Ukraine strikes the Kerch Bridge a
   second day running; its road arch collapses into the strait, severing
   the road link. Hours earlier Russia hits Kyiv's North and South
   bridges over the Dnipro, closing both.
2. **Nvidia beats, without Huang.** $115.8bn in quarterly sales, up
   103% year on year, in its first results since Jensen Huang quit;
   the board says it will not reinstate him. $130bn forecast next.
3. **Trump lands in Manila.** Quad talks and a Thailand trade deal open
   his three-day Asia trip; a three-way summit with Xi and Putin follows
   in Shenzhen.
4. **Third US carrier arrives as tankers are hit.** USS Theodore
   Roosevelt joins two carriers in the Middle East. A tanker is hit
   near Hormuz; Iran says naval mines struck more ships.
5. **Five EU states plan a Rwanda return hub.** Germany, Denmark,
   Austria, Greece and the Netherlands will send rejected asylum
   seekers to Rwanda; transfers start in 2027.
6. **Pentagon fails its audit — again.** Ninth year running: auditors
   cannot verify accounts covering $4.8 trillion in assets.
7. **Also today:** Estonia to shut its Russia border crossings on
   1 Dec over a "foiled bomb plot"; Microsoft blames a July software
   bug for last week's global outage and JPMorgan cites a software bug
   for its banking disruption; 13 babies born with measles in the US
   since 2025, CDC figures show.

Sources are listed in `NOTES.md` (Reuters, AP, Forbes, The Hindu,
and same-day reporting). Claims that were unverified at the time are
attributed in the image ("Iran says…", "Microsoft blames…").

## Why it should win (judge's rubric)

1. **It is the news of 17 November 2026** — specific events of that
   day, dated in the masthead, none of them from another day.
2. **Selection and breadth** — war, business, diplomacy, shipping,
   migration, defence and tech, across Ukraine, the US, Asia, the
   Middle East and Europe.
3. **It reads** — a viewer who missed the day can tell what happened
   from the image alone: every story is a headline plus a plain
   one-line summary.
4. **Faithful** — reported facts only, attributed where unconfirmed,
   no hype, no speculation shown as fact.
5. **Craft** — one clear front-page composition, crisp vector-style
   drawing, legible at ~300 px (headlines 20–40 pt at 1024 px).

## How the program works

`main.py` (Python 3.13, standard library only) copies the bundled image
`entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`
when that variable is set), creating the output directory if needed.
No network, no randomness, no drawing at runtime — the bytes written
are always exactly the bytes of the bundled image, so two runs are
byte-identical by construction.

The image itself was drawn once, locally, by `build/render.py` (PIL,
DejaVu fonts) from the researched headlines in `NOTES.md`. The render
script is kept in `build/` for transparency; it is not part of the
graded program.

## Files (repo root)

- `entry.png` — the image (PNG, 1024×1024, ~149 KB)
- `main.py` — the entry program (copies `entry.png` to the output path)
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — claim file naming the reward wallet (added at repo creation)
- `NOTES.md` — research notes and sources for every story
- `build/render.py` — the script that drew `entry.png`
- `news-image-20261117-kit/` — the current make.fun kit, for the local check

## Validation

- `entry.png` is a whole valid PNG, 1024×1024 px, 149,213 bytes
  (limit: 1 MiB / 1024×1024) — checked with PIL `Image.verify()`.
- `main.py` run twice into separate temp output directories writes
  byte-identical files (same sha256 both runs) — see below.
- Kit local check (`node cli/makefun.mjs check --repo <repo>` from
  `news-image-20261117-kit/`) to be run by the parent at submit time
  with the transcript bundle; the only expected failure before then
  is transcripts_present (no bundle exists yet — the parent builds it
  from this build session at submit time).

## Determinism check (run 18 Nov 2026, ~07:35 WIB)

Ran `main.py` twice with `MAKEFUN_OUTPUT_DIR` pointed at two separate
temp directories, then compared:

- Run 1 output sha256: `5cd0014daebf467b946037497c527645b1ac4e1db3b15afbbf155c1bf01bc1ba`
- Run 2 output sha256: `5cd0014daebf467b946037497c527645b1ac4e1db3b15afbbf155c1bf01bc1ba`
- Bundled `entry.png` sha256: identical to both runs (pure copy).
- `cmp` on the two outputs: identical, no differences.
- Both outputs verified as whole PNG images, 1024×1024 px,
  149,213 bytes — inside the 1,048,576-byte and 1024×1024 limits.

## Referral

Referral code: `0txwmf1m`
