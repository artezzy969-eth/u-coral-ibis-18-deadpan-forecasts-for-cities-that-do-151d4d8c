"""Deadpan forecast for Tarnwick.

Writes a single forecast line to the output file. Standard library only,
no network access, deterministic: the same line every run.
"""

import os
from pathlib import Path

FORECAST = (
    "In Tarnwick, Thursday's 41-knot headwind will return the 8:15 ferry "
    "to its berth, so the council has ruled the crossing complete, "
    "refunds in vouchers."
)


def main() -> None:
    if not 1 <= len(FORECAST) <= 160:
        raise ValueError("forecast must be 1-160 code points")
    if "\n" in FORECAST or not FORECAST.strip():
        raise ValueError("forecast must be a single non-blank line")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(FORECAST + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
