"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast line about a smart fridge to entry.txt.

The roast: a fridge so smart it can run a full self-diagnostic and push
its own firmware update, yet the only repair it can offer is rebooting
the owner's expectations. The gadget is brilliant at everything except
the one job that matters.
"""

import os
import pathlib

LINE = (
    "My smart fridge ran a full diagnostic, updated its firmware, "
    "then concluded the only thing that needs rebooting is my expectations."
)


def main() -> None:
    out_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character, and the entry
    # must be exactly one line.
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
