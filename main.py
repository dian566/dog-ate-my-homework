#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

A dog, caught red-pawed, explains why the homework got eaten.
The program writes exactly one line to /output/entry.txt.
The output is byte-identical on every run: no randomness, no clock.
"""

import os

ENTRY = "Your homework said it needed to be 'turned in' — so I turned it in. To my stomach. It never specified where."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
