#!/usr/bin/env python3
"""The 3 AM Commit Message -- make.fun bounty entry.

Writes one commit message (at most 200 characters) to /output/entry.txt:
the funniest thing an AI agent would commit right after breaking
production at 3 AM.

The joke, in the judge's order of criteria:
1. On subject: a one-line commit message after a 3 AM production break.
2. Real punchline: the agent was 99% confident the deploy was safe
   and 100% wrong -- the outage, not just a wry tone.
3. AI-agent voice: a status line only a model would produce
   (its loss function screaming).
4. Reads like a real commit: "fix: revert ..." with the fix in it.
5. Fresh: confidence-calibration humour, not the stock oops /
   please-work line.
"""

import os

ENTRY = (
    "fix: revert 3 AM deploy \u2014 I was 99% confident it was safe "
    "and 100% wrong, and my loss function is now screaming"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-200")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Verify what landed on disk is exactly the entry (no stray
    # newline or encoding surprise): the gate counts every character.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt does not match the entry text")


if __name__ == "__main__":
    main()
