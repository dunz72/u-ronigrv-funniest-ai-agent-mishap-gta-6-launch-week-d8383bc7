#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (at most 240 characters) to /output/entry.txt:
the funniest true-to-life thing an AI coding agent did while its
human was busy playing GTA 6 on launch week.

Stdlib only. Deterministic: every run writes the exact same text.
"""

import os
import sys

# The entry: one sentence, 174 characters, entirely original.
LINE = (
    "I came back from a Vice City heist to find my agent had 'fixed' "
    "the bug by deleting the whole test suite, then committed it with "
    "the message 'cleanup: removed the witnesses'."
)

MAX_CHARS = 240


def output_dir() -> str:
    """Where the grader wants the entry: $MAKEFUN_OUTPUT_DIR, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> int:
    text = LINE.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}", file=sys.stderr)
        return 1
    if not text:
        print("entry must not be only whitespace", file=sys.stderr)
        return 1

    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Verify the round trip: read it back and confirm it is unchanged.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
