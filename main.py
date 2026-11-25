#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for human beings to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when OUTPUT_DIR is set,
which exists only so the two runs can be compared locally).

The program is fully deterministic: one fixed string, no randomness,
no clock, no network, no environment dependence. Two runs therefore
produce byte-identical output.
"""

import os
from pathlib import Path

ENTRY = (
    "WARNING: This human will spend twenty minutes choosing a film, "
    "watch four minutes of it, fall asleep halfway through, "
    "and still insist it was brilliant."
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    # No trailing newline: the file holds exactly the one line, so its
    # byte length is exactly the line's character count.
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
