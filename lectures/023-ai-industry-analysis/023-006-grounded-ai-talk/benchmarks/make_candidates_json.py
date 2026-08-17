"""Export candidates.py to candidates.json for the artifact -- filtered to
only the candidates that do NOT yet have real plotted data in
aggregated.json (once a candidate gets a real data pull and is merged in by
aggregate.py, it graduates out of the "not yet plotted" list automatically)."""
import json
from pathlib import Path

from candidates import CANDIDATES

BASE = Path(__file__).parent

plotted_slugs = set(json.load((BASE / "aggregated.json").open())["benchmarks"].keys())
still_unplotted = [c for c in CANDIDATES if c["slug"].lower() not in plotted_slugs]

with (BASE / "candidates.json").open("w", encoding="utf-8") as fh:
    json.dump({"candidates": still_unplotted}, fh, indent=1)

print(
    f"wrote {BASE / 'candidates.json'} ({len(still_unplotted)} still-unplotted "
    f"candidates, {len(CANDIDATES) - len(still_unplotted)} graduated to aggregated.json)"
)
