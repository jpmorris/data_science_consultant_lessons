"""Export candidates.py to candidates.json for the artifact + a summary table for README.md."""
import json
from pathlib import Path

from candidates import CANDIDATES

BASE = Path(__file__).parent

with (BASE / "candidates.json").open("w", encoding="utf-8") as fh:
    json.dump({"candidates": CANDIDATES}, fh, indent=1)

print(f"wrote {BASE / 'candidates.json'} ({len(CANDIDATES)} candidates)")
