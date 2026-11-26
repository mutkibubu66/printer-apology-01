#!/usr/bin/env python3
"""The Printer Apology.

One line, at most 120 characters: an apology note from an office printer
to the people who keep jamming it, feeding it cheap paper and swearing
at it. The printer owns up to the jam on page 47, then turns the apology
around on its humans: cheapest paper, constant swearing, and still they
expect miracles. Pure standard library.
"""

# PART1 — the entry line (96 characters, one line).
LINE = (
    "Sorry I jammed page 47 \u2014 you feed me the cheapest paper, "
    "swear at me, and still expect miracles."
)


# PART2 — gate validation (1-120 chars, single line, not only whitespace).
def validate(line: str) -> None:
    assert line.strip(), "line must not be only white space"
    assert "\n" not in line, "line must be a single line"
    assert 1 <= len(line) <= 120, f"line is {len(line)} chars, gate is 1-120"


# PART3 — write the line to /output/entry.txt, no trailing newline.
import os


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()


