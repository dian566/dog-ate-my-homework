#!/usr/bin/env python3
"""Dog Ate My Homework — the funniest excuse, one line only.

A very literal dog explains what happened to the homework after it was
told the assignment had to be "turned in". The program emits a single
line into /output/entry.txt and nothing else. It stays deterministic:
identical bytes every run, no dice rolls, no wall clock involved.
"""

from pathlib import Path

EXCUSE = (
    "Your homework said it needed to be 'turned in' — so I turned it in. "
    "To my stomach. It never specified where."
)

DESTINATION = Path("/output/entry.txt")


def _check_line(line: str) -> None:
    """Guard the contract: exactly one line, under the 200-char cap."""
    assert "\n" not in line and len(line) <= 200, "entry must be one short line"


def run() -> None:
    _check_line(EXCUSE)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(EXCUSE, encoding="utf-8", newline="")


if __name__ == "__main__":
    run()
