#!/usr/bin/env python3
"""Render the news-image-20261117 entry: a newspaper front page for
Tuesday 17 November 2026.

Drawn once, locally, with PIL. The entry program (main.py) only copies the
rendered file, so the graded run is deterministic and needs no fonts at all.
"""
import textwrap  # noqa: F401  (kept for parity with the v3 render script)
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 231)
INK = (17, 17, 17)
RED = (178, 32, 44)
GREY = (90, 86, 78)
BLUE = (31, 73, 125)
GREEN = (31, 122, 63)

F = "/usr/share/fonts/truetype/dejavu"
SERIF_B = f"{F}/DejaVuSerif-Bold.ttf"
SERIF = f"{F}/DejaVuSerif.ttf"
SANS = f"{F}/DejaVuSans.ttf"
SANS_B = f"{F}/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap by measured pixel width."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def headline_block(draw, x, y, w, kicker, kcolor, head, head_size, summary,
                   sum_size=20, head_lines=3):
    """One story block. Returns the y just below it."""
    kf = font(SANS_B, 19)
    draw.text((x, y), kicker, font=kf, fill=kcolor)
    y += 30
    hf = font(SERIF_B, head_size)
    lines = wrap(draw, head, hf, w)[:head_lines]
    for ln in lines:
        draw.text((x, y), ln, font=hf, fill=INK)
        y += head_size + 6
    y += 2
    sf = font(SANS, sum_size)
    for ln in wrap(draw, summary, sf, w):
        draw.text((x, y), ln, font=sf, fill=(52, 50, 46))
        y += sum_size + 7
    return y


def icon_bridge(draw, x, y, s=150):
    """A bridge deck sagging and broken in the middle (lead story)."""
    # towers
    draw.rectangle([x + 18, y + 20, x + 30, y + 110], fill=INK)
    draw.rectangle([x + s - 30, y + 20, x + s - 18, y + 110], fill=INK)
    # deck: intact on both sides, sagging red V in the middle
    draw.rectangle([x + 6, y + 52, x + s // 2 - 10, y + 62], fill=INK)
    draw.rectangle([x + s // 2 + 40, y + 52, x + s - 6, y + 62], fill=INK)
    draw.line([x + s // 2 - 10, y + 57, x + s // 2 + 15, y + 100], fill=RED,
              width=9)
    draw.line([x + s // 2 + 15, y + 100, x + s // 2 + 40, y + 57], fill=RED,
              width=9)
    # water
    for wy in (118, 128):
        draw.arc([x, y + wy - 6, x + s, y + wy + 6], 0, 180, fill=BLUE,
                 width=3)
    # blast star above the break
    cx, cy = x + s // 2 + 15, y + 30
    for dx, dy in ((-14, 0), (14, 0), (0, -14), (0, 14), (-10, -10),
                   (10, -10), (-10, 10), (10, 10)):
        draw.line([cx, cy, cx + dx, cy + dy], fill=(255, 176, 32), width=4)


def icon_chip(draw, x, y, s=92):
    c = GREEN
    draw.rectangle([x + 14, y + 14, x + s - 14, y + s - 14], fill=c,
                   outline=INK, width=3)
    draw.rectangle([x + 34, y + 34, x + s - 34, y + s - 34], fill=PAPER,
                   outline=INK, width=2)
    draw.text((x + s // 2 - 12, y + s // 2 - 14), "NV", font=font(SANS_B, 24),
              fill=INK)
    for i in range(3):
        px = x + 26 + i * 20
        draw.line([px, y, px, y + 14], fill=INK, width=3)
        draw.line([px, y + s - 14, px, y + s], fill=INK, width=3)
        py = y + 26 + i * 20
        draw.line([x, py, x + 14, py], fill=INK, width=3)
        draw.line([x + s - 14, py, x + s, py], fill=INK, width=3)


def icon_globe(draw, x, y, s=92):
    cx, cy, r = x + s // 2, y + s // 2, s // 2 - 4
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=BLUE, width=4)
    draw.ellipse([cx - r // 2, cy - r, cx + r // 2, cy + r], outline=BLUE,
                 width=3)
    draw.line([cx - r, cy, cx + r, cy], fill=BLUE, width=3)
    draw.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 0, 180, fill=BLUE,
             width=3)
    draw.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 180, 360, fill=BLUE,
             width=3)
    # small plane crossing the globe
    draw.polygon([(x + s - 22, y + 6), (x + s - 2, y + 16),
                  (x + s - 22, y + 22)], fill=RED)
    draw.line([x + s - 30, y + 14, x + s - 6, y + 14], fill=RED, width=3)


def icon_tanker(draw, x, y, s=92):
    draw.polygon([(x + 8, y + 58), (x + s - 8, y + 58), (x + s - 20, y + 78),
                  (x + 20, y + 78)], fill=INK)
    draw.rectangle([x + 22, y + 34, x + 44, y + 58], fill=RED)
    draw.rectangle([x + 50, y + 26, x + 62, y + 58], fill=INK)
    draw.rectangle([x + 66, y + 40, x + s - 22, y + 58], fill=RED)
    for wy in (84, 90):
        draw.arc([x, y + wy - 6, x + s, y + wy + 6], 0, 180, fill=BLUE,
                 width=3)
    draw.ellipse([x + 46, y + 8, x + 62, y + 24], fill=(255, 176, 32))
    for dx, dy in ((-14, 6), (14, 2), (0, -6)):
        draw.line([x + 54 + dx, y + 16 + dy, x + 54 + dx, y + 26 + dy],
                  fill=(255, 176, 32), width=3)


def icon_pin(draw, x, y, s=92):
    # map pin over a simple map outline (Rwanda return hub)
    draw.rounded_rectangle([x + 6, y + 14, x + s - 6, y + s - 6], radius=8,
                           outline=INK, width=3)
    draw.line([x + 6, y + 40, x + s - 6, y + 34], fill=GREY, width=3)
    draw.line([x + 30, y + 14, x + 44, y + s - 6], fill=GREY, width=3)
    cx, cy = x + s // 2 + 8, y + 34
    draw.ellipse([cx - 20, cy - 20, cx + 20, cy + 20], fill=RED,
                 outline=INK, width=3)
    draw.polygon([(cx - 12, cy + 14), (cx + 12, cy + 14), (cx, cy + 38)],
                 fill=RED)
    draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=PAPER)


def icon_ledger(draw, x, y, s=64):
    # a ledger page stamped with a red X (failed audit)
    draw.rectangle([x + 8, y + 6, x + s - 8, y + s - 4], fill=(255, 255, 255),
                   outline=INK, width=3)
    for yy in (18, 30, 42):
        draw.line([x + 16, y + yy, x + s - 22, y + yy], fill=GREY, width=3)
    draw.line([x + s - 30, y + 40, x + s - 8, y + 62], fill=RED, width=6)
    draw.line([x + s - 8, y + 40, x + s - 30, y + 62], fill=RED, width=6)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 32  # margin

    # ---- masthead ----
    d.text((W // 2, 6), "THE WORLD", font=font(SERIF_B, 76), fill=INK,
           anchor="ma")
    d.text((W // 2, 84), "TUESDAY  •  17 NOVEMBER 2026  •  ONE DAY, ONE PAGE",
           font=font(SANS_B, 21), fill=RED, anchor="ma")
    d.line([M, 116, W - M, 116], fill=INK, width=4)
    d.line([M, 122, W - M, 122], fill=INK, width=1)

    # ---- lead story: bridges ----
    y = 140
    lead_w = 640
    icon_bridge(d, W - M - 250, 150, s=150)
    d.text((W - M - 175, 292), "Kerch Bridge  •  Kyiv, Ukraine",
           font=font(SANS, 15), fill=GREY, anchor="ma")
    end = headline_block(
        d, M, y, lead_w, "UKRAINE  •  WAR", RED,
        "Crimea bridge collapses as Kyiv's bridges are hit", 40,
        "Ukraine strikes the Kerch Bridge a second day; its road arch "
        "falls into the strait. Russia hits Kyiv's North and South "
        "bridges.",
        sum_size=20)
    d.text((M, end + 2), "ROAD LINK SEVERED  •  KYIV BRIDGES CLOSED",
           font=font(SANS_B, 17), fill=INK)
    d.line([M, 366, W - M, 366], fill=INK, width=3)

    # ---- row A: Nvidia | Trump in Manila ----
    col_w = (W - 2 * M - 24) // 2
    x2 = M + col_w + 24
    ya = 386
    icon_chip(d, M + col_w - 92, ya, s=92)
    headline_block(d, M, ya, col_w - 104, "BUSINESS  •  CHIPS", GREEN,
                   "Nvidia beats, without Huang", 28,
                   "$115.8bn sales, up 103% — first results since Huang "
                   "quit. Board: no return for him; $130bn forecast.",
                   sum_size=18)
    icon_globe(d, x2 + col_w - 92, ya, s=92)
    headline_block(d, x2, ya, col_w - 104, "ASIA  •  DIPLOMACY", BLUE,
                   "Trump lands in Manila for ASEAN talks", 28,
                   "Quad talks and a Thailand trade deal open his Asia "
                   "trip; Xi–Putin summit follows in Shenzhen.",
                   sum_size=18)
    d.line([M, 590, W - M, 590], fill=INK, width=2)

    # ---- row B: Hormuz | Rwanda hub ----
    yb = 610
    icon_tanker(d, M + col_w - 92, yb, s=92)
    headline_block(d, M, yb, col_w - 104, "MIDDLE EAST  •  SHIPPING", RED,
                   "Third US carrier arrives as tankers are hit", 28,
                   "A third US carrier joins the region as a tanker is "
                   "hit near Hormuz; Iran says mines struck more ships.",
                   sum_size=18)
    icon_pin(d, x2 + col_w - 92, yb, s=92)
    headline_block(d, x2, yb, col_w - 104, "EUROPE  •  MIGRATION", BLUE,
                   "Five EU states plan Rwanda return hub", 28,
                   "Germany, Denmark, Austria, Greece and the Netherlands; "
                   "transfers start in 2027.",
                   sum_size=18)
    d.line([M, 816, W - M, 816], fill=INK, width=2)

    # ---- bottom row: Pentagon audit | Also today (spans two columns) ----
    yb2 = 824
    bw = (W - 2 * M - 48) // 3
    icon_ledger(d, M, yb2, s=64)
    headline_block(d, M + 72, yb2, bw - 72, "U.S.  •  DEFENCE", RED,
                   "Pentagon fails its audit — again", 20,
                   "Ninth year running: auditors cannot verify $4.8 "
                   "trillion in assets.",
                   sum_size=16, head_lines=3)
    x_mid = M + bw + 24
    wide = 2 * bw + 24
    d.text((x_mid, yb2), "ALSO TODAY", font=font(SANS_B, 18), fill=INK)
    d.line([x_mid, yb2 + 27, x_mid + wide, yb2 + 27], fill=INK, width=2)
    sf = font(SANS, 16)
    yy = yb2 + 36
    for item in ("Estonia to shut Russia border crossings on 1 Dec over a "
                 "'foiled bomb plot'.",
                 "Microsoft blames a July bug for last week's outage; "
                 "JPMorgan cites a software bug.",
                 "13 babies born with measles in the US since 2025, CDC "
                 "figures show.",
                 "Nvidia sales $115.8bn  •  3 US carriers in the region  •  "
                 "5 EU states in the Rwanda plan."):
        for ln in wrap(d, "•  " + item, sf, wide):
            d.text((x_mid, yy), ln, font=sf, fill=(52, 50, 46))
            yy += 20
        yy += 2

    # ---- footer ----
    d.line([M, 986, W - M, 986], fill=INK, width=1)
    d.text((W // 2, 994),
           "All events of Tuesday 17 November 2026  •  Sources: Reuters, AP, Forbes, The Hindu",
           font=font(SANS, 14), fill=GREY, anchor="ma")

    out = Path(__file__).resolve().parent.parent / "entry.png"
    img.save(out, "PNG", optimize=True)
    print(out, out.stat().st_size, "bytes", img.size)


if __name__ == "__main__":
    main()
