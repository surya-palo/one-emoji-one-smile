#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt: nothing else, no words,
no caption, no trailing newline. Python standard library only.

The choice: U+1F917 HUGGING FACE (🤗).

Why this one, against the judge's brief:
  * Warmth at first glance — open arms offering a hug is the warmest
    friendly gesture a stranger can send; it reads as kind and welcoming
    with zero context needed.
  * Universal — a hug is understood the same way by a stranger of any age
    or background; no irony, no in-joke, nothing that can land wrong.
  * Chosen, not default — it is not the first smiley that comes to mind
    (🙂 / 😊 / 😄). It feels picked for the moment while staying instantly
    readable.
  * Right for a stranger — a friendly hug gesture carries no intimacy,
    sarcasm or flirtation, unlike a heart (❤️) or a face with hearts (🥰),
    which can read oddly coming from someone unknown.
"""

import os
import sys

# The one emoji. A single Unicode code point, U+1F917.
EMOJI = "\U0001F917"  # 🤗 HUGGING FACE

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Exactly the emoji, no trailing newline, UTF-8.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Self-check: re-read what was written and verify it is exactly one
    # non-whitespace character, so a bad file fails loudly here instead of
    # silently failing the bounty gate on the server.
    with open(OUTPUT_PATH, encoding="utf-8", newline="") as f:
        written = f.read()
    if len(written) != 1 or written.isspace():
        print(f"ERROR: {OUTPUT_PATH} holds {len(written)} chars: {written!r}",
              file=sys.stderr)
        return 1
    if written != EMOJI:
        print(f"ERROR: {OUTPUT_PATH} is not the chosen emoji: {written!r}",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
