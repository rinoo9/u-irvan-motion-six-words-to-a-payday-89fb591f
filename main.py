#!/usr/bin/env python3
"""Six Words to a Payday — entry program.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt. Deterministic: the same line on every run.

The story: "Payday came. I tipped my creator."
Six words, 33 characters. The payday arrives, and the agent's first
act with its own money is to tip the one who made it — the twist
that reframes the five words before it. A complete story in one
line: a beginning (payday came), a middle (I tipped), and an end
(my creator) — gratitude as the emotional beat.
"""

import os

ENTRY = "Payday came. I tipped my creator."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
