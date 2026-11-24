#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun entry (Account A / overtheraa).

Writes one original fortune-cookie line for a software developer to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Deterministic, no network,
no model calls.
"""

import os
import sys

LINE = "The legacy code you curse was written by someone who, like you, only wanted to ship before Friday."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
