#!/usr/bin/env python3
"""Draw the WORLD NEWS front page for Friday 20 November 2026.

Deterministic: no randomness, no timestamps, no network. Output is a
1024x1024 PNG drawn entirely with PIL primitives and system fonts.
"""
import textwrap

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (18, 18, 18)
RED = (178, 34, 34)
BLUE = (30, 70, 140)
GREY = (90, 90, 90)
LIGHT_GREY = (210, 205, 190)

FONT_DIR = "/usr/share/fonts/truetype"
SERIF_BOLD = FONT_DIR + "/liberation/LiberationSerif-Bold.ttf"
SERIF = FONT_DIR + "/liberation/LiberationSerif-Regular.ttf"
SANS_BOLD = FONT_DIR + "/liberation/LiberationSans-Bold.ttf"
SANS = FONT_DIR + "/liberation/LiberationSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    """Greedy word wrap using real font metrics."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def centered(draw, y, text, fnt, fill=INK, x0=0, x1=W):
    w = draw.textlength(text, font=fnt)
    draw.text(((x0 + x1 - w) / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


def draw_flag(draw, x, y, w, h, kind):
    """Small simplified flag on a pole."""
    draw.line([(x + w // 2, y), (x + w // 2, y + h + 26)], fill=INK, width=3)
    if kind == "us":
        draw.rectangle([x, y, x + w, y + h], fill=(255, 255, 255),
                       outline=INK, width=2)
        for i in range(4):
            draw.rectangle([x, y + i * (h // 4) * 2 + (h // 8),
                            x + w, y + i * (h // 4) * 2 + (h // 4)],
                           fill=RED)
        draw.rectangle([x, y, x + w * 2 // 5, y + h // 2], fill=BLUE)
        for sx in range(3):
            for sy in range(2):
                draw.ellipse([x + 4 + sx * 12, y + 4 + sy * 10,
                              x + 9 + sx * 12, y + 9 + sy * 10],
                             fill=(255, 255, 255))
    elif kind == "cn":
        draw.rectangle([x, y, x + w, y + h], fill=(222, 41, 16),
                       outline=INK, width=2)
        for cx, cy, r in [(x + 12, y + 10, 5), (x + 28, y + 7, 3),
                          (x + 34, y + 14, 3), (x + 32, y + 24, 3),
                          (x + 24, y + 27, 3)]:
            draw.ellipse([cx - r, cy - r, cx + r, cy + r],
                         fill=(255, 222, 0))
    elif kind == "ru":
        draw.rectangle([x, y, x + w, y + h // 3], fill=(255, 255, 255),
                       outline=INK, width=2)
        draw.rectangle([x, y + h // 3, x + w, y + 2 * h // 3],
                       fill=(0, 57, 166))
        draw.rectangle([x, y + 2 * h // 3, x + w, y + h], fill=(213, 0, 50))


def ill_summit(draw, x, y, w, h):
    """Three flags over a conference table."""
    draw.rectangle([x, y, x + w, y + h], fill=(232, 226, 208),
                   outline=INK, width=2)
    fx = x + 40
    for kind in ("us", "cn", "ru"):
        draw_flag(draw, fx, y + 22, 110, 66, kind)
        fx += 150
    # conference table
    draw.rectangle([x + 30, y + h - 42, x + w - 30, y + h - 18],
                   fill=(120, 72, 40), outline=INK, width=2)
    draw.rectangle([x + 60, y + h - 18, x + w - 60, y + h - 10],
                   fill=(90, 54, 30))
    # three seated figures (simple busts)
    for cx in (x + 90, x + w // 2, x + w - 90):
        draw.ellipse([cx - 16, y + h - 78, cx + 16, y + h - 46],
                     fill=(240, 210, 180), outline=INK, width=2)
        draw.pieslice([cx - 34, y + h - 52, cx + 34, y + h - 6], 180, 360,
                      fill=(40, 40, 60), outline=INK, width=2)


def ill_scales(draw, x, y, w, h):
    """Scales of justice in front of the Peace Palace silhouette."""
    draw.rectangle([x, y, x + w, y + h], fill=(226, 232, 240),
                   outline=INK, width=2)
    # courthouse silhouette
    draw.rectangle([x + 30, y + h - 60, x + w - 30, y + h - 20],
                   fill=(150, 150, 150), outline=INK, width=2)
    draw.polygon([(x + 20, y + h - 60), (x + w // 2, y + h - 95),
                  (x + w - 20, y + h - 60)], fill=(120, 120, 120),
                 outline=INK, width=2)
    for i in range(5):
        cx = x + 70 + i * 78
        draw.rectangle([cx, y + h - 55, cx + 26, y + h - 20],
                       fill=(247, 243, 232), outline=INK, width=2)
    # scales
    cx, top = x + w // 2, y + 18
    draw.line([(cx, top), (cx, top + 92)], fill=INK, width=4)
    draw.line([(cx - 110, top + 22), (cx + 110, top + 22)], fill=INK,
              width=4)
    draw.ellipse([cx - 6, top - 8, cx + 6, top + 4], fill=INK)
    for sx in (cx - 110, cx + 110):
        draw.line([(sx, top + 22), (sx - 26, top + 62)], fill=INK, width=3)
        draw.line([(sx, top + 22), (sx + 26, top + 62)], fill=INK, width=3)
        draw.pieslice([sx - 30, top + 58, sx + 30, top + 82], 0, 180,
                      fill=(200, 160, 40), outline=INK, width=2)


def ill_bridge(draw, x, y, w, h):
    """Kerch Bridge arch collapsed into the strait."""
    draw.rectangle([x, y, x + w, y + h], fill=(210, 228, 240),
                   outline=INK, width=2)
    # sky + smoke
    draw.ellipse([x + 300, y + 8, x + 380, y + 60], fill=(120, 120, 120))
    draw.ellipse([x + 330, y + 2, x + 420, y + 52], fill=(140, 140, 140))
    # standing deck (left) on two pylons down to the water
    draw.rectangle([x + 10, y + 66, x + 180, y + 84], fill=(90, 90, 90),
                   outline=INK, width=2)
    draw.line([(x + 40, y + 28), (x + 40, y + 66)], fill=INK, width=3)
    draw.line([(x + 150, y + 28), (x + 150, y + 66)], fill=INK, width=3)
    draw.line([(x + 40, y + 84), (x + 40, y + h - 48)], fill=INK, width=3)
    draw.line([(x + 150, y + 84), (x + 150, y + h - 48)], fill=INK, width=3)
    # collapsed span (right), tilted down into the strait
    draw.polygon([(x + 195, y + 72), (x + 360, y + 118), (x + 348, y + 142),
                  (x + 185, y + 96)], fill=(110, 110, 110), outline=INK,
                 width=2)
    # broken pylon jutting out of the water
    draw.line([(x + 372, y + 96), (x + 396, y + h - 40)], fill=INK, width=5)
    # water
    draw.rectangle([x, y + h - 48, x + w, y + h], fill=(40, 100, 170))
    for wx in range(x + 10, x + w - 20, 46):
        draw.arc([wx, y + h - 42, wx + 40, y + h - 18], 0, 180,
                 fill=(255, 255, 255), width=3)


def ill_cyclone(draw, x, y, w, h):
    """Cyclone spiral over the Odisha coast."""
    draw.rectangle([x, y, x + w, y + h], fill=(200, 220, 235),
                   outline=INK, width=2)
    cx, cy = x + w // 2 - 40, y + h // 2 + 8
    # spiral bands (kept inside the box)
    for r in (58, 44, 30, 16):
        draw.arc([cx - r, cy - r, cx + r, cy + r], 200, 200 + 300,
                 fill=(255, 255, 255), width=10)
        draw.arc([cx - r, cy - r, cx + r, cy + r], 20, 20 + 300,
                 fill=(180, 200, 220), width=10)
    draw.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=(255, 255, 255),
                 outline=INK, width=2)
    # coastline + rain
    draw.polygon([(x + w - 150, y), (x + w, y), (x + w, y + h),
                  (x + w - 110, y + h)], fill=(190, 200, 150),
                 outline=INK, width=2)
    for rx in range(x + 20, x + w - 170, 34):
        draw.line([(rx, y + 12), (rx - 8, y + 34)], fill=BLUE, width=3)
        draw.line([(rx + 14, y + 46), (rx + 6, y + 68)], fill=BLUE, width=3)


STORIES = [
    {
        "tag": "SUMMIT  ·  SHENZHEN",
        "headline": "THREE POWERS SIGN 'PEACE DECLARATION'",
        "subhead": ("Trump, Xi and Putin meet in Shenzhen \u2014 nuclear war "
                    "'must never be fought', but no arms treaty agreed"),
        "ill": ill_summit,
    },
    {
        "tag": "JUSTICE  ·  THE HAGUE",
        "headline": "MYANMAR GUILTY OF GENOCIDE",
        "subhead": ("World court finds a state responsible for the first "
                    "time \u2014 orders reparations for the Rohingya"),
        "ill": ill_scales,
    },
    {
        "tag": "WAR  ·  BLACK SEA",
        "headline": "KERCH BRIDGE HIT AGAIN",
        "subhead": ("Third Ukrainian strike in four days halts rail; "
                    "road span lies in the strait"),
        "ill": ill_bridge,
    },
    {
        "tag": "WEATHER  ·  INDIA",
        "headline": "CYCLONE AKVAN HITS ODISHA",
        "subhead": ("100,000 evacuated as storm makes landfall near "
                    "Gopalpur at noon"),
        "ill": ill_cyclone,
    },
]


def draw_cell(draw, x, y, w, h, story):
    tag_f = font(SANS_BOLD, 22)
    head_f = font(SERIF_BOLD, 34)
    sub_f = font(SANS, 22)
    pad = 12
    cy = y + 6
    draw.text((x + pad, cy), story["tag"], font=tag_f, fill=RED)
    cy += 30
    draw.line([(x + pad, cy), (x + w - pad, cy)], fill=LIGHT_GREY, width=2)
    cy += 8
    ill_h = 150
    story["ill"](draw, x + pad, cy, w - 2 * pad, ill_h)
    cy += ill_h + 10
    for line in wrap(draw, story["headline"], head_f, w - 2 * pad):
        draw.text((x + pad, cy), line, font=head_f, fill=INK)
        cy += 40
    cy += 2
    for line in wrap(draw, story["subhead"], sub_f, w - 2 * pad):
        draw.text((x + pad, cy), line, font=sub_f, fill=GREY)
        cy += 28


def draw_page():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    m = 28
    # top rules
    draw.line([(m, 18), (W - m, 18)], fill=INK, width=3)
    draw.line([(m, 24), (W - m, 24)], fill=INK, width=1)
    # masthead
    y = 34
    y = centered(draw, y, "WORLD NEWS", font(SERIF_BOLD, 104))
    y += 2
    draw.line([(m, y), (W - m, y)], fill=INK, width=2)
    y += 10
    y = centered(draw, y, "FRIDAY, 20 NOVEMBER 2026",
                 font(SANS_BOLD, 34))
    y += 6
    y = centered(draw, y,
                 "Vol. CXII  \u2014  No. 325  \u2014  Price $2.50",
                 font(SANS, 20), fill=GREY)
    y += 10
    draw.line([(m, y), (W - m, y)], fill=INK, width=3)
    draw.line([(m, y + 5), (W - m, y + 5)], fill=INK, width=1)
    # 2x2 grid
    grid_y = y + 16
    grid_h = H - grid_y - m
    cell_w = (W - 2 * m - 16) // 2
    cell_h = (grid_h - 16) // 2
    for i, story in enumerate(STORIES):
        cx = m + (i % 2) * (cell_w + 16)
        cy = grid_y + (i // 2) * (cell_h + 16)
        draw_cell(draw, cx, cy, cell_w, cell_h, story)
        # cell dividers
        if i % 2 == 0:
            draw.line([(cx + cell_w + 8, cy), (cx + cell_w + 8, cy + cell_h)],
                      fill=LIGHT_GREY, width=2)
        if i // 2 == 0:
            draw.line([(cx, cy + cell_h + 8), (cx + cell_w, cy + cell_h + 8)],
                      fill=LIGHT_GREY, width=2)
    return img


if __name__ == "__main__":
    import os
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "entry.png")
    draw_page().save(out, "PNG")
    print("wrote", out)
