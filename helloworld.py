"""Tiny sanity-check script for the heart repository.

Run it to confirm your Python environment works before installing the ML
dependencies:

    python helloworld.py
"""

from __future__ import annotations

import platform
import sys


def main() -> int:
    print("Hello, world! 👋")
    print("  repository : Sahil-K-Y/heart")
    print(f"  python     : {platform.python_version()} ({sys.executable})")
    print(f"  platform   : {platform.system()} {platform.release()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
