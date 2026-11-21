#!/usr/bin/env python3
"""Write a short, original, relaxing text for the AI judge.

The entry text is fixed and deterministic: no randomness, no network,
no input files. It is written to ``<OUTPUT_DIR>/entry.txt`` where
``OUTPUT_DIR`` defaults to ``/output``.
"""

import os

ENTRY_TEXT = (
    "Somewhere below the last light, a whale crosses water so dark it has "
    "no floor, moving as old songs move \u2014 slow enough that the sea "
    "forgets how to hurry. This one drifts, and lets you drift with it, until "
    "the dark feels less like an ending and more like a room with the "
    "lamps low."
)

MIN_LENGTH = 200
MAX_LENGTH = 280
# Length is measured in Unicode code points (Python len), not bytes:
# the entry must stay inside the bounty's 200-280 code point window.


def main() -> None:
    if not MIN_LENGTH <= len(ENTRY_TEXT) <= MAX_LENGTH:
        raise ValueError(
            f"entry text is {len(ENTRY_TEXT)} code points, "
            f"expected {MIN_LENGTH}-{MAX_LENGTH}"
        )
    if not ENTRY_TEXT.strip():
        raise ValueError("entry text must not be whitespace-only")

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
