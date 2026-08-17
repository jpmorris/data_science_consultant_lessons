"""Build the embedded JSON blobs the artifact (benchmark-tracker.html) needs
and patch them into the four <script id="..." type="application/json">
tags in place:

  - bench-data           trimmed aggregated.json (per-point keys shortened)
  - candidates-data       candidates.json as-is (still-unplotted candidates)
  - contamination-data    slug -> {dis, rot, nov, why} for the corner badges
  - summary-data          one row per benchmark (has_data True or False) for
                           the bottom summary table: benchmark, popular,
                           category, saturated, has_data, what_measures,
                           disclosure, rotation, domain_novelty

Run this after aggregate.py / make_candidates_json.py / merge_contamination.py
any time the underlying data changes, then re-publish the artifact file.
"""
import csv
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).parent
ARTIFACT = Path(
    "/tmp/claude-1000/-mnt-bebop-jmorris-code-data-science-consultant-lessons-visual-3"
    "/017fd929-0d0a-47c8-89f5-927b895a899d/scratchpad/benchmark-tracker.html"
)

sys.path.insert(0, str(BASE))
from candidates import CANDIDATES  # noqa: E402
from make_readme import CATEGORIES as README_CATEGORIES  # noqa: E402

aggregated = json.load((BASE / "aggregated.json").open())
benchmarks = aggregated["benchmarks"]
contamination = json.load((BASE / "contamination.json").open())
candidates_data = json.load((BASE / "candidates.json").open())

summary_rows = {}
with (BASE / "aggregated_summary.csv").open(newline="", encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        summary_rows[row["benchmark"]] = row

# ---- slug -> category, covering all 208 tracked + 21 still-unplotted ----
slug_category = {}
for cat, slugs in README_CATEGORIES:
    for s in slugs:
        slug_category[s] = cat
for c in CANDIDATES:
    slug_category.setdefault(c["slug"].lower(), c["category"])

POPULAR_SLUGS = {
    "gpqa-diamond", "swe-bench-verified", "swe-bench-pro", "arc-agi-1",
    "arc-agi-2", "hle", "aime", "terminal-bench", "lmarena-elo",
    "browsecomp", "tau2-bench-telecom", "mcp-atlas",
}

# ---- 1. bench-data: trimmed aggregated.json ----
trimmed_benchmarks = {}
for slug, b in benchmarks.items():
    trimmed_benchmarks[slug] = {
        "display_name": b["display_name"],
        "description": b["description"],
        "unit_family": b["unit_family"],
        "unit_label": b["unit_label"],
        "source_files": b["source_files"],
        "provenance_summary": b["provenance_summary"],
        "points": [
            {
                "s": p.get("source", ""),
                "em": p.get("extraction_method", ""),
                "m": p.get("model", ""),
                "d": p.get("date", ""),
                "v": p.get("score"),
            }
            for p in b["points"]
        ],
        "trend": b.get("trend"),
    }
bench_data_json = json.dumps(
    {"generated": aggregated["generated"], "benchmarks": trimmed_benchmarks},
    separators=(",", ":"),
)

# ---- 2. candidates-data: as-is ----
candidates_data_json = json.dumps(candidates_data, separators=(",", ":"))

# ---- 3. contamination-data: trimmed ----
trimmed_contamination = {
    slug: {"dis": v["disclosure"], "rot": v["rotation"], "nov": v["domain_novelty"], "why": v["justification"]}
    for slug, v in contamination.items()
}
contamination_data_json = json.dumps(trimmed_contamination, separators=(",", ":"))

# ---- 4. summary-data: one row per benchmark (has_data or not) ----
summary = []
for slug, b in benchmarks.items():
    sr = summary_rows.get(slug, {})
    c = contamination.get(slug, {})
    summary.append({
        "slug": slug,
        "name": b["display_name"],
        "popular": slug in POPULAR_SLUGS,
        "category": slug_category.get(slug, "Uncategorized"),
        "saturated": sr.get("saturated", "").strip().lower() == "true",
        "has_data": True,
        "what": b["description"],
        "dis": c.get("disclosure", "unknown"),
        "rot": c.get("rotation", "unknown"),
        "nov": c.get("domain_novelty", "unknown"),
    })
for cand in candidates_data["candidates"]:
    slug = cand["slug"].lower()
    c = contamination.get(slug, {})
    summary.append({
        "slug": slug,
        "name": cand["name"],
        "popular": slug in POPULAR_SLUGS,
        "category": cand["category"],
        "saturated": False,
        "has_data": False,
        "what": cand["description"],
        "dis": c.get("disclosure", "unknown"),
        "rot": c.get("rotation", "unknown"),
        "nov": c.get("domain_novelty", "unknown"),
    })
summary.sort(key=lambda r: r["name"].lower())
summary_data_json = json.dumps({"rows": summary}, separators=(",", ":"))

# ---- patch into the artifact HTML ----
html = ARTIFACT.read_text(encoding="utf-8")


def replace_script(html: str, script_id: str, new_json: str) -> str:
    pattern = re.compile(
        r'(<script id="' + re.escape(script_id) + r'" type="application/json">)(.*?)(</script>)',
        re.DOTALL,
    )
    new_html, n = pattern.subn(lambda m: m.group(1) + new_json + m.group(3), html, count=1)
    if n != 1:
        raise RuntimeError(f"expected exactly 1 match for script#{script_id}, got {n}")
    return new_html


html = replace_script(html, "bench-data", bench_data_json)
html = replace_script(html, "candidates-data", candidates_data_json)

if 'id="contamination-data"' in html:
    html = replace_script(html, "contamination-data", contamination_data_json)
else:
    # insert right after the candidates-data script tag
    marker = re.search(r'<script id="candidates-data" type="application/json">.*?</script>', html, re.DOTALL)
    assert marker
    insert_at = marker.end()
    html = (
        html[:insert_at]
        + f'\n<script id="contamination-data" type="application/json">{contamination_data_json}</script>'
        + html[insert_at:]
    )

if 'id="summary-data"' in html:
    html = replace_script(html, "summary-data", summary_data_json)
else:
    marker = re.search(r'<script id="contamination-data" type="application/json">.*?</script>', html, re.DOTALL)
    assert marker
    insert_at = marker.end()
    html = (
        html[:insert_at]
        + f'\n<script id="summary-data" type="application/json">{summary_data_json}</script>'
        + html[insert_at:]
    )

ARTIFACT.write_text(html, encoding="utf-8")
print(f"bench-data: {len(bench_data_json):,} bytes, {len(trimmed_benchmarks)} benchmarks")
print(f"candidates-data: {len(candidates_data_json):,} bytes, {len(candidates_data['candidates'])} candidates")
print(f"contamination-data: {len(contamination_data_json):,} bytes, {len(trimmed_contamination)} slugs")
print(f"summary-data: {len(summary_data_json):,} bytes, {len(summary)} rows")
print(f"wrote {ARTIFACT} ({len(html):,} bytes total)")
