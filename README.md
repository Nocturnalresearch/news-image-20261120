# WORLD NEWS — Friday, 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Nocturnalresearch/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Nocturnalresearch/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A newspaper front page for **Friday, 20 November 2026**, drawn entirely in
code (PIL, no AI-generated image). It sums up the day's world news in four
stories, one per quadrant, each with a small drawn illustration, a region
tag, a bold headline and a one-line subhead. The masthead names the day.

## The four stories

1. **SUMMIT · SHENZHEN — "THREE POWERS SIGN 'PEACE DECLARATION'"**
   Trump, Xi and Putin held the first-ever trilateral summit in Shenzhen on
   Thursday 19 November. Their joint "Peace Declaration" says "a nuclear war
   cannot be won and must never be fought", with dialogue on reducing nuclear
   risks — but no arms-control treaty, no timetable, and no mention of
   Ukraine or the Iran war.
   *Sources: USA Today, Algemeiner (Reuters photo), Seoul Economic Daily,
   19 Nov 2026.*

2. **JUSTICE · THE HAGUE — "MYANMAR GUILTY OF GENOCIDE"**
   The International Court of Justice ruled on Thursday 19 November that
   Myanmar committed genocide against the Rohingya in the 2017 "clearance
   operations" — the first time in the court's 80-year history a state has
   been found responsible for genocide (9–6 vote). Reparations were ordered,
   including the safe return of refugees.
   *Sources: CNN, Le Monde, Amnesty International, OHCHR, 19 Nov 2026.*

3. **WAR · BLACK SEA — "KERCH BRIDGE HIT AGAIN"**
   Ukrainian strikes on 16–17 November collapsed the Kerch Bridge road arch
   into the strait; a third strike overnight on 18–19 November halted rail
   traffic. Road closed, rail suspended, no casualties reported.
   *Sources: Euronews, ISW assessments 16–17 Nov, AP, 19 Nov 2026.*

4. **WEATHER · INDIA — "CYCLONE AKVAN HITS ODISHA"**
   Severe Cyclonic Storm Akvan makes landfall near Gopalpur, Odisha, around
   noon on Friday 20 November, with winds of 90–100 km/h gusting to 110.
   Odisha evacuated 1,05,304 people to 1,224 shelters; red alert for
   11 districts; schools shut.
   *Sources: IMD bulletins via India Today / NewsXphere / JagranJosh,
   19 Nov 2026.*

## How to run

```sh
python3 draw_news.py   # redraws entry.png (1024x1024, deterministic)
python3 main.py        # copies entry.png to /output/entry.png
```

`main.py` is standard library only. `draw_news.py` needs Pillow and the
DejaVu/Liberation fonts under `/usr/share/fonts/truetype/`; it draws the
page from scratch, so the PNG is reproducible byte-for-byte.

## make.fun

Entry for [news-image-20261120](https://make.fun/c/news-image-20261120)
($250, top 50 paid, AI judge pairwise). The program runs twice with no
network and both runs must write the same bytes — `main.py` copies the
same `entry.png` each time.
