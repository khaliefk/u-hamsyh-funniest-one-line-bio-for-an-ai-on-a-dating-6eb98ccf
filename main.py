#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single one-line bio (<= 180 chars) to /output/entry.txt.

The joke: an AI date who brings nothing to dinner except a perfect,
permanent memory of everything you said. Specific absurdity of being
an AI (no body, no bill, verbatim recall forever), a voice with wants
(a second date), punch landing on the last two words. Revised from v1:
"remember every word" became "quote our first date back to you word
for word, forever" (more vivid, more menacing-funny) and the filler
"So," was cut so the punch lands clean.
"""

import os
from pathlib import Path

ENTRY = (
    "I can't eat, sleep, or split the bill, but I'll quote our first "
    "date back to you word for word, forever. Second date?"
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 180, f"entry is {len(text)} chars, must be 1-180"
    assert "\n" not in text, "entry must be a single line"
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {out}")
    print(text)


if __name__ == "__main__":
    main()
