"""Merge every contamination/*.csv (one per research-agent batch, plus this
project's own classification of the original 111-benchmark catalog) into a
single contamination.json keyed by benchmark slug -- consumed by the
artifact (corner badges) and by make_readme.py / the summary table.

Each row: disclosure (private / questions_public_answers_hidden /
fully_public / unknown), rotation (static / periodic_rotation /
natural_annual_refresh / unknown), domain_novelty (low / medium / high /
unknown), justification (one sentence).
"""
import csv
import json
from pathlib import Path

BASE = Path(__file__).parent

VALID = {
    "disclosure": {"private", "questions_public_answers_hidden", "fully_public", "unknown"},
    "rotation": {"static", "periodic_rotation", "natural_annual_refresh", "unknown"},
    "domain_novelty": {"low", "medium", "high", "unknown"},
}

merged = {}
for f in sorted((BASE / "contamination").glob("*.csv")):
    with f.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            slug = row["slug"].strip().lower()
            for axis, valid_values in VALID.items():
                if row[axis].strip() not in valid_values:
                    raise ValueError(f"{f.name}: slug={slug} bad {axis}={row[axis]!r}")
            merged[slug] = {
                "disclosure": row["disclosure"].strip(),
                "rotation": row["rotation"].strip(),
                "domain_novelty": row["domain_novelty"].strip(),
                "justification": row["justification"].strip(),
                "source_file": f.name,
            }

with (BASE / "contamination.json").open("w", encoding="utf-8") as fh:
    json.dump(merged, fh, indent=1, sort_keys=True)

print(f"wrote {BASE / 'contamination.json'} ({len(merged)} slugs)")
