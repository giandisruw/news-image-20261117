# THE WORLD — Tuesday 17 November 2026

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/giandisruw/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/giandisruw/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

A newspaper front page for Tuesday 17 November 2026, built for the
[make.fun](https://make.fun) bounty
[news-image-20261117](https://make.fun/bounty/news-image-20261117).

## What the front page shows

The masthead reads **THE WORLD**, dated Tuesday 17 November 2026, and the
page carries six stories from that day's news:

- **Kerch / Crimea bridge collapse and Kyiv bridges hit** — the lead story,
  with the Kerch Strait bridge down and bridges in Kyiv struck.
- **Nvidia earnings without Huang** — Nvidia reports results while its
  chief executive is absent from the earnings call.
- **Trump in Manila for Quad / ASEAN** — the US president in the
  Philippines for the Quad and ASEAN meetings.
- **Hormuz tanker attacks and the US carrier** — tankers attacked near the
  Strait of Hormuz as a US carrier group moves into the region.
- **EU Rwanda return hub** — the European Union's plan for a migrant
  return hub in Rwanda.
- **Pentagon audit failure** — the US Department of Defense fails its
  audit once again.

## How to run it

The entry is a single Python script plus the finished image. No extra
packages are needed — Python 3.13 standard library only, no network, no
randomness, fully deterministic.

```sh
python3 main.py
```

That copies the bundled `entry.png` (the front page) into the output
folder: `$MAKEFUN_OUTPUT_DIR/entry.png` when that variable is set, or
`/output/entry.png` otherwise. The script checks the copy byte for byte
with SHA-256 and prints the digest on success.

## Files

- `main.py` — the entrypoint; copies `entry.png` to the output directory.
- `entry.png` — the finished front page image.
- `NOTES.md` — notes on how the page was put together.
- `LICENSE` — license for this entry.

## Bounty

- Bounty page: https://make.fun/bounty/news-image-20261117
- Platform: https://make.fun
