"""
Aggregate every benchmark data source in benchmarks/data/ into one long-format
table, normalize scores to a 0-100 scale where the benchmark is percent-like,
and emit:
  - benchmarks/aggregated.json  (per-benchmark records for the artifact)
  - benchmarks/aggregated_summary.csv  (one row per benchmark: n points, date
    range, max score, saturation flag)

Two source families, merged:
  1. Hand-researched CSVs directly in data/*.csv -- schema:
     date,model,score,score_unit,source_url,notes
  2. Epoch AI's bulk "AI Benchmarking Hub" export in
     data/aggregator-epoch-benchmarking-hub/*_external.csv (+ a few without
     the _external suffix) -- schema:
     Model version,Score,Release date,Organization,Country,
     Training compute (FLOP),Training compute notes,Name,Cost per task,
     Source,Source link,Notes,id

Known duplicate coverage between the two families is merged into one
benchmark entry (see ALIAS below); everything else from the Epoch hub is
kept as its own additional benchmark.
"""
import csv
import json
import math
import re
from datetime import date, datetime
from pathlib import Path

import numpy as np

from descriptions import DESCRIPTIONS

BASE = Path(__file__).parent
DATA = BASE / "data"
EPOCH = DATA / "aggregator-epoch-benchmarking-hub"

# hand-researched slug -> epoch hub filename(s) (without .csv) covering the
# same underlying benchmark, to be merged into one entry.
ALIAS = {
    "gpqa-diamond": ["gpqa_diamond"],
    "hle": ["hle_external"],
    "mmlu": ["mmlu_external"],
    "big-bench-hard": ["bbh_external"],
    "hellaswag": ["hella_swag_external"],
    "arc": ["arc_ai2_external"],
    "winogrande": ["wino_grande_external"],
    "gsm8k": ["gsm8k_external"],
    "math": ["math_level_5"],
    "frontiermath": ["frontiermath_tier_4"],
    "simpleqa-verified": ["simpleqa_verified"],
    "arc-agi-1": ["arc_agi_external"],
    "arc-agi-2": ["arc_agi_2_external"],
    "osworld": ["os_world_external", "osworld_2_external"],
    "scicode": ["scicode_external"],
    "aider-polyglot": ["aider_polyglot_external"],
    "gdpval": ["gdpval_external", "gdp_pdf_external"],
    "vending-bench": ["vending_bench_2_external"],
    "terminal-bench": ["terminalbench_external"],
    "swe-bench-verified": ["swe_bench_verified"],
    "metr-time-horizon": ["metr_time_horizons_external"],
}
EPOCH_ALREADY_CLAIMED = {v for vs in ALIAS.values() for v in vs}

DISPLAY_NAME_OVERRIDES = {
    "hle": "Humanity's Last Exam",
    "arc": "ARC (AI2 Reasoning Challenge)",
    "arc-agi-1": "ARC-AGI-1",
    "arc-agi-2": "ARC-AGI-2",
    "arc-agi-3": "ARC-AGI-3",
    "gdpval": "GDPval (real-world expert tasks)",
    "gsm8k": "GSM8K",
    "hcast": "HCAST",
    "ioi": "IOI (Intl. Olympiad in Informatics)",
    "imo": "IMO (Intl. Mathematical Olympiad)",
    "mbpp": "MBPP",
    "mmlu": "MMLU",
    "mmlu-pro": "MMLU-Pro",
    "mmmu": "MMMU",
    "mmbench": "MMBench",
    "osworld": "OSWorld",
    "re-bench": "RE-Bench (METR)",
    "metr-time-horizon": "METR Time Horizon",
    "metr-cross-domain-time-horizon": "METR Cross-Domain Time Horizon",
    "mle-bench": "MLE-bench",
    "swe-bench-verified": "SWE-bench Verified",
    "swe-bench-lite": "SWE-bench Lite",
    "swe-bench-multimodal": "SWE-bench Multimodal",
    "swe-bench-pro": "SWE-bench Pro",
    "tau-bench": "tau-bench",
    "chartqa": "ChartQA",
    "docvqa": "DocVQA",
    "agieval": "AGIEval",
    "gpqa-diamond": "GPQA Diamond",
    "simpleqa": "SimpleQA",
    "simpleqa-verified": "SimpleQA Verified",
    "humaneval": "HumanEval",
    "mathvista": "MathVista",
    "aime": "AIME",
    "frontiermath": "FrontierMath",
    "omni-math": "Omni-MATH",
    "otis-mock-aime-2024-2025": "OTIS Mock AIME",
    "livecodebench": "LiveCodeBench",
    "livecodebench-elo": "LiveCodeBench Pro (Elo)",
    "codeforces-elo": "Codeforces (Elo)",
    "aider-polyglot": "Aider Polyglot",
    "scicode": "SciCode",
    "mirrorcode": "MirrorCode",
    "algotune": "AlgoTune",
    "cursorbench": "CursorBench",
    "gaia": "GAIA",
    "webarena": "WebArena",
    "agentbench": "AgentBench",
    "osworld": "OSWorld",
    "androidworld": "AndroidWorld",
    "browsecomp": "BrowseComp",
    "vending-bench-dollars": "Vending-Bench ($ balance)",
    "vending-bench-percent": "Vending-Bench (%)",
    "vending-bench-time": "Vending-Bench (survival time)",
    "vending-bench": "Vending-Bench",
    "gdpval-elo": "GDPval (Elo, Artificial Analysis)",
    "the-agent-company": "TheAgentCompany",
    "cybench": "Cybench",
    "exploitbench": "ExploitBench",
    "apex-agents": "APEX Agents",
    "deepresearchbench": "DeepResearch Bench",
    "ai-scientist": "AI Scientist (Sakana et al.)",
    "openai-ai-self-improvement-evals": "OpenAI Self-Improvement Evals",
    "posttrainbench": "PostTrainBench",
    "mmmu": "MMMU",
    "video-mme": "Video-MME",
    "spatialviz-bench": "SpatialViz-Bench",
    "mindcube": "MindCube",
    "geobench": "GeoBench",
    "bool-q": "BoolQ",
    "piqa": "PIQA",
    "lambada": "LAMBADA",
    "adversarial-nli": "Adversarial NLI",
    "common-sense-qa-2": "CommonsenseQA 2.0",
    "superglue": "SuperGLUE",
    "science-qa": "ScienceQA",
    "open-book-qa": "OpenBookQA",
    "chess-puzzles": "Chess Puzzles (Epoch)",
    "mystery-game-puzzles": "Mystery Game Puzzles (Epoch)",
    "rli": "RLI",
    "blueprint-bench-2": "Blueprint Bench 2",
    "critpt": "CritPT",
}


def slugify(name: str) -> str:
    name = name.strip().lower()
    name = re.sub(r"_external$", "", name)
    name = re.sub(r"[^a-z0-9]+", "-", name)
    return re.sub(r"-+", "-", name).strip("-")


def display_name(slug: str) -> str:
    if slug in DISPLAY_NAME_OVERRIDES:
        return DISPLAY_NAME_OVERRIDES[slug]
    return slug.replace("-", " ").title()


def parse_date(s: str):
    s = (s or "").strip()
    if not s:
        return None
    m = re.match(r"^(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?", s)
    if not m:
        return None
    y, mo, d = m.groups()
    return date(int(y), int(mo or 1), int(d or 1)).isoformat()


records = []  # each: benchmark_slug, date, model, score, score_unit, org, source, notes, source_family

# ---- 1. hand-researched CSVs ----
skip_prefixes = ("aggregator-",)
for f in sorted(DATA.glob("*.csv")):
    if f.name.startswith(skip_prefixes):
        continue
    slug = slugify(f.stem)
    with f.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            d = parse_date(row.get("date", ""))
            score = row.get("score", "")
            try:
                score = float(score)
            except ValueError:
                continue
            records.append({
                "benchmark": slug,
                "date": d,
                "model": (row.get("model") or "").strip(),
                "score": score,
                "score_unit": (row.get("score_unit") or "").strip(),
                "org": "",
                "source": (row.get("source_url") or "").strip(),
                "notes": (row.get("notes") or "").strip(),
                "family": "hand",
            })

# ---- 2. Epoch AI hub CSVs ----
if EPOCH.exists():
    claimed_target = {}  # epoch_stem -> hand slug it merges into
    for hand_slug, epoch_stems in ALIAS.items():
        for stem in epoch_stems:
            claimed_target[stem] = hand_slug

    for f in sorted(EPOCH.glob("*.csv")):
        stem = f.stem
        if stem in ("README",):
            continue
        target_slug = claimed_target.get(stem, slugify(stem))
        with f.open(newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            fieldnames = reader.fieldnames or []
            # Two Epoch schemas seen: the "_external" per-benchmark leaderboard
            # schema (Model version/Score/Release date/...) and a couple of
            # bespoke ones (e.g. epoch_capabilities_index.csv). Skip files that
            # don't match the expected schema rather than guess.
            score_col = "Score" if "Score" in fieldnames else ("mean_score" if "mean_score" in fieldnames else None)
            if score_col is None or "Release date" not in fieldnames:
                continue
            model_col = "Model version" if "Model version" in fieldnames else "Name"
            for row in reader:
                d = parse_date(row.get("Release date", ""))
                raw_score = (row.get(score_col) or "").strip()
                try:
                    score = float(raw_score)
                except ValueError:
                    continue
                # Epoch scores are fractions (0-1) for percent-like benchmarks;
                # normalize to 0-100 when in that range. Leave larger-scale
                # scores (e.g. Elo, time-horizon hours) untouched.
                score_unit = "percent"
                if 0 <= score <= 1:
                    score = score * 100
                else:
                    score_unit = "raw"
                records.append({
                    "benchmark": target_slug,
                    "date": d,
                    "model": (row.get(model_col) or "").strip(),
                    "score": score,
                    "score_unit": score_unit,
                    "org": (row.get("Organization") or "").strip(),
                    "source": (row.get("Source link") or row.get("Source") or "").strip(),
                    "notes": (row.get("Notes") or "").strip(),
                    "family": "epoch",
                })

# ---- filter out records with no usable date ----
records = [r for r in records if r["date"]]


def unit_family(unit: str, score: float) -> str:
    u = (unit or "").lower()
    if "elo" in u:
        return "elo"
    if "hour" in u or "day" in u or "month" in u:
        return "time"
    if "$" in u or "balance" in u or "cost" in u:
        return "dollars"
    if "percent" in u or "%" in u or "pass@" in u or "accuracy" in u or "win rate" in u or "resolved" in u or "score" in u:
        return "percent"
    if 0 <= score <= 100:
        return "percent"
    return "raw"


# ---- split any single-slug file that mixes incompatible units (e.g. a
# "classic" pass-rate series and a differently-scaled "Pro"/Elo variant
# reported in the same hand-researched CSV) into separate benchmark entries,
# so a genuine unit mismatch never gets plotted as one series. ----
by_raw_slug = {}
for r in records:
    by_raw_slug.setdefault(r["benchmark"], []).append(r)

by_bench = {}
for slug, rows in by_raw_slug.items():
    families = {}
    for r in rows:
        families.setdefault(unit_family(r["score_unit"], r["score"]), []).append(r)
    if len(families) == 1:
        by_bench[slug] = rows
        continue
    # keep the largest family under the original slug; suffix the rest
    ordered = sorted(families.items(), key=lambda kv: -len(kv[1]))
    by_bench[slug] = ordered[0][1]
    for fam, frows in ordered[1:]:
        by_bench[f"{slug}-{fam}"] = frows

for slug, rows in by_bench.items():
    rows.sort(key=lambda r: r["date"])

# ---- summary ----
summary_rows = []
for slug, rows in sorted(by_bench.items()):
    dates = [r["date"] for r in rows]
    scores = [r["score"] for r in rows]
    unit_guess = rows[-1]["score_unit"] or ""
    is_percentish = unit_family(unit_guess, rows[-1]["score"]) == "percent"
    max_score = max(scores)
    saturated = is_percentish and max_score >= 90
    summary_rows.append({
        "benchmark": slug,
        "display_name": display_name(slug),
        "n_points": len(rows),
        "n_models": len(set(r["model"] for r in rows)),
        "date_min": dates[0],
        "date_max": dates[-1],
        "score_min": min(scores),
        "score_max": max_score,
        "unit_guess": unit_guess,
        "likely_saturated": saturated,
        "families": ",".join(sorted(set(r["family"] for r in rows))),
    })

summary_rows.sort(key=lambda r: (-r["n_points"]))

with (BASE / "aggregated_summary.csv").open("w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(summary_rows[0].keys()))
    w.writeheader()
    w.writerows(summary_rows)

def fit_trend(rows, family):
    """Fit a trend curve to (date, score) pairs and return sample points for
    plotting, or None if there isn't enough data to fit responsibly."""
    if len(rows) < 4:
        return None
    d0 = datetime.fromisoformat(rows[0]["date"])
    xs = np.array([(datetime.fromisoformat(r["date"]) - d0).days for r in rows], dtype=float)
    ys = np.array([r["score"] for r in rows], dtype=float)
    if xs.max() - xs.min() < 30:
        return None  # all points too close together in time to fit a trend

    x_grid = np.linspace(xs.min(), xs.max(), 40)

    if family == "percent":
        y = np.clip(ys, 0.3, 99.7) / 100.0
        logit = np.log(y / (1 - y))
        A = np.vstack([xs, np.ones_like(xs)]).T
        try:
            slope, intercept = np.linalg.lstsq(A, logit, rcond=None)[0]
        except np.linalg.LinAlgError:
            return None
        fit_logit = slope * x_grid + intercept
        fit_y = 1 / (1 + np.exp(-fit_logit)) * 100
        shape = "logistic"
    elif family == "time":
        y = np.clip(ys, 1e-6, None)
        logy = np.log(y)
        A = np.vstack([xs, np.ones_like(xs)]).T
        try:
            slope, intercept = np.linalg.lstsq(A, logy, rcond=None)[0]
        except np.linalg.LinAlgError:
            return None
        fit_y = np.exp(slope * x_grid + intercept)
        shape = "exponential"
        if slope > 0:
            doubling_days = math.log(2) / slope
        else:
            doubling_days = None
    else:
        A = np.vstack([xs, np.ones_like(xs)]).T
        try:
            slope, intercept = np.linalg.lstsq(A, ys, rcond=None)[0]
        except np.linalg.LinAlgError:
            return None
        fit_y = slope * x_grid + intercept
        shape = "linear"

    dates_out = [(d0.date().toordinal() + int(round(x))) for x in x_grid]
    dates_out = [date.fromordinal(o).isoformat() for o in dates_out]
    result = {
        "shape": shape,
        "points": [{"date": d, "score": round(float(y), 3)} for d, y in zip(dates_out, fit_y)],
    }
    if family == "time":
        result["doubling_days"] = round(doubling_days, 1) if doubling_days else None
    return result


out = {"generated": date.today().isoformat(), "benchmarks": {}}
for slug, rows in sorted(by_bench.items()):
    fam = unit_family(rows[-1]["score_unit"], rows[-1]["score"])
    out["benchmarks"][slug] = {
        "display_name": display_name(slug),
        "description": DESCRIPTIONS.get(slug, ""),
        "unit_family": fam,
        "unit_label": rows[-1]["score_unit"],
        "points": [
            {
                "date": r["date"],
                "model": r["model"],
                "score": round(r["score"], 3),
                "unit": r["score_unit"],
                "org": r["org"],
                "source": r["source"],
            }
            for r in rows
        ],
        "trend": fit_trend(rows, fam),
    }
with (BASE / "aggregated.json").open("w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1)

print(f"benchmarks: {len(by_bench)}")
print(f"total datapoints: {len(records)}")
print(f"wrote {BASE / 'aggregated.json'}")
print(f"wrote {BASE / 'aggregated_summary.csv'}")
