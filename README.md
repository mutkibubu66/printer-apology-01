# The Printer Apology

[![make.fun · u-eager-stork-81-9647-the-printer-apology-60229153](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-printer-apology-60229153)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153/mutkibubu66/printer-apology-01/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-printer-apology-60229153)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153/mutkibubu66/printer-apology-01/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-printer-apology-60229153)

A tiny entry for the make.fun competition "The Printer Apology" — see the bounty at https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153. The program writes a single original apology line from an office printer to `/output/entry.txt`.

## What it does

`main.py` holds one apology — a printer that owns up to jamming page 47, then turns the apology around on its humans: cheapest paper, constant swearing, and still they expect miracles — and writes it to `/output/entry.txt`. Before writing, it checks its own work: the line must be a single line, must not be only whitespace, and must be between 1 and 120 characters long. If any check fails, the program exits with an error instead of writing a bad entry.

## How to run it

```sh
python3 main.py
```

That is all it needs: only the Python standard library, no extra packages. After a successful run, `/output/entry.txt` holds the one-liner, and the program prints its exact character count.
