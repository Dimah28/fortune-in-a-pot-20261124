#!/usr/bin/env python3
"""Fortune in a Pot — make.fun bounty u-golden-heron-44-fortune-in-a-pot-ded981e9.

Writes one kind, funny fortune for a houseplant to /output/entry.txt.
Deterministic: the fortune is a fixed string, stdlib only, no randomness,
no network, no clock. The output directory honours MAKEFUN_OUTPUT_DIR
when set (for local testing); otherwise it writes to /output.
"""

import os
import sys

ENTRY = (
    "You will outgrow this pot, win over the cat, "
    "and become the plant every guest asks about by name."
)

MAX_CHARS = 120
FINAL_PUNCTUATION = (".", "!", "?")


def check_fortune(text: str) -> None:
    """Fail hard if the fortune breaks any gate rule."""
    if not isinstance(text, str):
        raise TypeError("fortune must be a string")
    if not text.strip():
        raise ValueError("fortune must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"fortune is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    if text != text.strip():
        raise ValueError("fortune must not start or end with whitespace")
    if not text.endswith(FINAL_PUNCTUATION):
        raise ValueError("fortune must end with sentence-final punctuation")


def main() -> int:
    check_fortune(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    # Read-back verification: what landed on disk must be exactly the
    # validated fortune, byte for byte.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != ENTRY:
        raise ValueError("read-back mismatch: entry.txt differs from ENTRY")
    check_fortune(written)
    return 0


if __name__ == "__main__":
    sys.exit(main())
