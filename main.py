"""Write the one-sentence entry to <MAKEFUN_OUTPUT_DIR or /output>/entry.txt.

Standard library only, no network, no randomness, no clock reads.
"""

import os
import sys

TEXT = "Imagine every printing press on earth joined by one invisible thread: a page printed at dawn is read that hour in every town, and any reader may answer back along it.\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        print(f"could not create output directory {out_dir!r}: {exc}", file=sys.stderr)
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
