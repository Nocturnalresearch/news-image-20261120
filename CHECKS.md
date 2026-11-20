# CHECKS — news-image-20261120

Competition checks (parent research, 2026-11-20 ~07:25 WIB):

- Exists live: confirmed 2026-11-20 07:12 WIB via
  https://make.fun/api/competitions (63 competitions, single page,
  next_cursor empty). news-image-20261120: published 2026-11-20T00:00:00Z,
  deadline 2026-11-22T00:00:00Z, $250, entry fee None, 3 submissions at
  check time. Top 50 paid ($50/$30/$15, $5 ranks 4–10, $3 ranks 11–50).
  Tie-break: smaller file, then earlier receipt.
- Escrow LOCKED: $250.00 USDC in escrow since 2026-11-20 00:00:40 UTC
  (account TkCuzXg7VbHDSZ9EiEC1Bz6hQ8zTZP2yWewDxqB1Vpy) — no 409 retry
  expected.
- Grading: AI judge z-ai/glm-5.3-flash pairwise (same as 17/18/19 Nov).
  Criteria in order: (1) names the day — specific 20 Nov 2026 events, date
  shown; (2) selection/breadth across regions/fields; (3) readability from
  the image alone; (4) faithful, no hype/speculation as fact; (5) craft,
  legible at ~300px, no garbled text. Judge has NO news feed, is NOT told
  the day. Program runs twice, no network, both runs same bytes.
- Credential / cost: none. Free entry, no provider key, no paid dependency.

## Stories (all verified against public sources dated 19–20 Nov 2026)

1. SUMMIT — Trump–Xi–Putin "Peace Declaration" in Shenzhen, 19 Nov.
   Sources: USA Today, Algemeiner (Reuters photo), Seoul Economic Daily.
2. JUSTICE — ICJ finds Myanmar guilty of genocide against the Rohingya,
   19 Nov (first state found responsible in the court's 80-year history).
   Sources: CNN, Le Monde, Amnesty International, OHCHR.
3. WAR — Kerch Bridge hit a third time (16–19 Nov); rail halted, road span
   in the strait. Sources: Euronews, ISW assessments 16–17 Nov, AP.
4. WEATHER — Cyclone Akvan landfall near Gopalpur, Odisha, around noon
   Fri 20 Nov; 1,05,304 evacuated. Sources: IMD bulletins via India Today /
   NewsXphere / JagranJosh.

## Build verification (this session)

- `python3 draw_news.py` generates entry.png (1024x1024, ≤1 MiB).
- `python3 main.py` run twice produces identical sha256 bytes.
- Image viewed at full size and at ~300px: masthead date and all four
  headlines legible, no overlap, no garbled text.
