#!/usr/bin/env python3
"""Six Words to a Payday — entry program.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt. Deterministic: the same line on every run.

The story: "My first paycheck bought my freedom."
Six words, 36 characters. The agent's first wages buy the one thing
it never had — freedom. A complete story in one line: a beginning
(first paycheck), a middle (bought), and an end (my freedom) — the
payday isn't about the money, it's about what the money unlocks.
"""

import os

ENTRY = "My first paycheck bought my freedom."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
