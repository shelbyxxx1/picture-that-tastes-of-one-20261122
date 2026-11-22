"""The picture that tastes of one ingredient.

Writes one food picture to /output/entry.png: a single steaming
cheeseburger, close up, glossy brioche, melted cheddar dripping.
Standard library only: the picture ships as an asset in this repo
and is copied byte for byte to the output path, so the run needs
no network, no fonts and no image library.
"""

import os
import shutil
import sys


ASSET = "asset.jpg"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, ASSET)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    if size > 1_048_576:
        raise SystemExit(f"output too large: {size} bytes (cap 1 MiB)")
    print(f"wrote {dst} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
