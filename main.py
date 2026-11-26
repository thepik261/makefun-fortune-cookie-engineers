#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers.

Writes a single one-line fortune cookie message for a software engineer
to /output/entry.txt. Pure standard library, deterministic.
"""

import os

FORTUNE = (
    "You will fix the bug in five minutes. "
    "You will spend four hours explaining why it was never a bug."
)


def main() -> None:
    line = FORTUNE.strip()
    assert 1 <= len(line) <= 120, f"fortune is {len(line)} chars"
    assert "\n" not in line
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
