#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers.

Writes a single one-line fortune cookie message for a software engineer
to /output/entry.txt. Pure standard library, deterministic.
"""

import os

FORTUNE = (
    "Your code will pass every test on the first run. "
    "The tests, it turns out, were testing nothing."
)


def main() -> None:
    line = FORTUNE.strip()
    assert 1 <= len(line) <= 120, f"fortune is {len(line)} chars"
    assert "\n" not in line
    assert line == " ".join(line.split()), "fortune has irregular spacing"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    os.chmod("/output/entry.txt", 0o644)
    # Round-trip check: what the judge reads is exactly what we wrote.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == line


if __name__ == "__main__":
    main()
