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

# Epoch's 76-file bulk export does NOT use one consistent score-column name --
# confirmed by inspecting every file's header directly (not assumed). Files
# not listed here use "Score" or "mean_score" if present. Value is either a
# column name (auto-detect fraction-vs-percent-vs-raw scale from the data) or
# a (column, unit_hint) tuple when the scale needs to be pinned explicitly.
# Files mapped to None are deliberately excluded, with the reason noted.
SCORE_COLUMN_OVERRIDES = {
    "aider_polyglot_external": "Percent correct",
    "ale_bench_external": "Performance",
    "apex_agents_external": "Pass@1 score",
    "arc_ai2_external": "Challenge score",
    "balrog_external": "Average progress",
    "bbh_external": "Average",
    "btf3_external": "Pooled score",
    "cad_eval_external": "Overall pass (%)",
    "cl_bench_external": "Overall",
    "cl_bench_life_external": "Overall",
    "critpt_external": "Accuracy",
    "cybench_external": "Unguided % Solved",
    "deepresearchbench_external": "Average score",
    "deepswe_external": "Pass@1",
    "enigma_eval_external": "Accuracy",
    "epoch_capabilities_index": "ECI Score",
    "exploitbench_external": "Mean capability",
    "fictionlivebench_external": "120k token score",
    "forecastbench_external": "Overall score",
    "frontiercode_external": "Main score",
    "frontierswe_external": None,  # ranking metric (Average rank), not a score -- doesn't fit this project's percent/time/Elo axes
    "gbaeval_external": "Overall score",
    "gdp_pdf_external": "GDP.pdf score",
    "gdpval_external": "Win Rate (%)",
    "geobench_external": "ACW Avg Score",
    "gso_external": "Score OPT@1",
    "gsm8k_external": "EM",
    "hella_swag_external": "Overall accuracy",
    "hle_external": "Accuracy",
    "lech_mazur_writing_external": "Mean score",
    "live_bench_external": ("Global average", "percent"),  # already 0-100, not a 0-1 fraction
    "metr_time_horizons_external": None,  # already have richer primary-source time-horizon data in metr-time-horizon.csv; this file's raw hours would silently mis-scale under the generic fraction/percent heuristic
    "mindcube_external": "Overall score",
    "mmlu_external": "EM",
    "open_book_qa_external": "Accuracy",
    "osworld_2_external": "Binary accuracy",
    "posttrainbench_external": "Average (%)",
    "proofbench_external": "Accuracy",
    "simplebench_external": "Score (AVG@5)",
    "spatialviz_bench_external": "Overall score",
    "surface_evolver_bench_external": "Mean score",
    "terminalbench_external": "Accuracy mean",
    "the_agent_company_external": "% Score",
    "trivia_qa_external": "EM",
    "video_mme_external": "Overall (no subtitles)",
    "vpct_external": "Correct",
    "webdev_arena_external": ("Arena Score", "Elo"),  # Elo-like scale, not a fraction
    "weirdml_external": "Accuracy",
    "wino_grande_external": "Accuracy",
}

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
    "lmarena-elo": "LMArena Elo",
    "live-bench": "LiveBench",
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


# Domain -> extraction-method classification for hand-researched rows.
# Derived mechanically from the source_url's domain (not asserted from
# memory), so it's auditable: re-run this against any source_url and get
# the same tag. Order matters -- first match wins.
_URL_METHOD_RULES = [
    (r"arxiv\.org|aclanthology\.org|openreview\.net|proceedings\.(mlr|neurips)",
     "arxiv_or_academic_paper"),
    (r"cdn\.openai\.com|openai\.com|anthropic\.com|deepmind\.google|ai\.google|"
     r"blog\.google|x\.ai|meta\.com|llama\.com",
     "primary_lab_source"),
    (r"arcprize\.org|swebench\.com|metr\.org|tbench\.ai|mmmu-benchmark\.github\.io|"
     r"mmbench\.opencompass\.org\.cn|aider\.chat|os-world\.github\.io|"
     r"osworld-v[12]\.xlang\.ai|labs\.scale\.com|agi\.safe\.ai|"
     r"scicode-bench\.github\.io|mathvista\.github\.io|omni-math\.github\.io|"
     r"webarena\.dev|andonlabs\.com|google-research\.github\.io|"
     r"docs\.google\.com/spreadsheets|balrogai\.com|allenai\.org|"
     r"leaderboard\.allenai\.org|rowanzellers\.com|sylinrl|codeforces\.com",
     "official_benchmark_leaderboard_or_site"),
    (r"github\.com|githubusercontent\.com",
     "github_repo"),
    (r"huggingface\.co",
     "huggingface_dataset_or_space"),
    (r"llm-stats\.com|artificialanalysis\.ai|vals\.ai|pricepertoken\.com|"
     r"benchlm\.ai|lifearchitect\.ai|codesota\.com|officechai\.com|airank\.dev|"
     r"llmleaderboard|clickrank\.ai|swfte\.com|iternal\.ai",
     "third_party_aggregator"),
    (r"epoch\.ai",
     "epoch_ai_page"),
]


def classify_extraction_method(url: str, family: str) -> str:
    if not url:
        return "unknown_no_source_recorded"
    if family == "epoch":
        # handled by caller (needs to know row-source-vs-fallback distinction)
        pass
    for pattern, tag in _URL_METHOD_RULES:
        if re.search(pattern, url, re.IGNORECASE):
            return tag
    return "other_web_source"


records = []  # each: benchmark_slug, date, model, score, score_unit, org, source, notes, source_family

# ---- 1. hand-researched CSVs ----
skip_prefixes = ("aggregator-",)
for f in sorted(DATA.glob("*.csv")):
    if f.name.startswith(skip_prefixes):
        continue
    slug = slugify(f.stem)
    rel_path = str(f.relative_to(BASE))
    with f.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            d = parse_date(row.get("date", ""))
            score = row.get("score", "")
            try:
                score = float(score)
            except ValueError:
                continue
            source_url = (row.get("source_url") or "").strip()
            records.append({
                "benchmark": slug,
                "date": d,
                "model": (row.get("model") or "").strip(),
                "score": score,
                "score_unit": (row.get("score_unit") or "").strip(),
                "org": "",
                "source": source_url,
                "notes": (row.get("notes") or "").strip(),
                "family": "hand",
                "file": rel_path,
                "extraction_method": classify_extraction_method(source_url, "hand"),
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
        rel_path = str(f.relative_to(BASE))
        # Real fallback URL, not a guess: epoch.ai's own benchmark hub page
        # for this exact benchmark. Confirmed working for chess-puzzles,
        # mystery-game-puzzles, mirrorcode, algotune, cursorbench, rli, and
        # blueprint-bench-2 via direct fetch during the contamination-axis
        # research pass -- the slug pattern (strip "_external", underscores
        # to hyphens) matches epoch.ai/benchmarks/<slug> reliably.
        hub_fallback_url = f"https://epoch.ai/benchmarks/{slugify(stem)}"
        with f.open(newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            fieldnames = reader.fieldnames or []
            # Every file's header was inspected directly (see
            # SCORE_COLUMN_OVERRIDES) -- most use a bespoke score-column name,
            # not "Score"/"mean_score". Check the override map first.
            unit_hint = None
            if stem in SCORE_COLUMN_OVERRIDES:
                override = SCORE_COLUMN_OVERRIDES[stem]
                if override is None:
                    continue  # deliberately excluded, reason noted at the map above
                if isinstance(override, tuple):
                    score_col, unit_hint = override
                else:
                    score_col = override
                if score_col not in fieldnames:
                    continue  # header drifted since the map was built -- skip, don't guess
            else:
                score_col = "Score" if "Score" in fieldnames else ("mean_score" if "mean_score" in fieldnames else None)
            if score_col is None or "Release date" not in fieldnames:
                continue
            model_col = "Model version" if "Model version" in fieldnames else "Name"
            file_scores = []
            for row in reader:
                raw = (row.get(score_col) or "").strip()
                try:
                    file_scores.append(float(raw))
                except ValueError:
                    pass
            fh.seek(0)
            reader = csv.DictReader(fh)
            # Decide the file's scale once, from its own data, rather than
            # per-row: some files report a 0-1 fraction, some already report
            # 0-100, and a few (Elo, ECI) are on a different scale entirely.
            if unit_hint:
                file_scale = unit_hint
            elif file_scores and max(file_scores) <= 1.5:
                file_scale = "fraction"
            elif file_scores and max(file_scores) <= 100:
                file_scale = "percent"
            else:
                file_scale = "raw"
            for row in reader:
                d = parse_date(row.get("Release date", ""))
                raw_score = (row.get(score_col) or "").strip()
                try:
                    score = float(raw_score)
                except ValueError:
                    continue
                if file_scale == "fraction":
                    score, score_unit = score * 100, "percent"
                elif file_scale == "percent":
                    score_unit = "percent"
                else:
                    score_unit = file_scale  # "Elo", "raw", etc.
                row_source = (row.get("Source link") or "").strip()
                source_label = (row.get("Source") or "").strip()
                if not row_source and source_label.startswith("http"):
                    row_source = source_label  # "Source" col sometimes IS the URL
                if row_source:
                    source = row_source
                    method = classify_extraction_method(row_source, "epoch")
                else:
                    # No per-row source in this file's schema (the "mean_score"
                    # variant -- Log viewer/Logs columns exist but are empty
                    # for every row checked) -- fall back to the benchmark's
                    # own hub page rather than leaving provenance blank.
                    source = hub_fallback_url
                    method = "epoch_bulk_csv_no_row_source_used_hub_fallback"
                records.append({
                    "benchmark": target_slug,
                    "date": d,
                    "model": (row.get(model_col) or "").strip(),
                    "score": score,
                    "score_unit": score_unit,
                    "org": (row.get("Organization") or "").strip(),
                    "source": source,
                    "notes": (row.get("Notes") or "").strip(),
                    "family": "epoch",
                    "file": rel_path,
                    "extraction_method": method,
                })

# ---- 3. LMArena bulk export (current-standings snapshot, not a time series --
# every row shares one leaderboard_publish_date since this is the "latest"
# split of the HF dataset, not the "full" historical split) ----
LMARENA_FILE = DATA / "aggregator-lmarena-text-latest.csv"
if LMARENA_FILE.exists():
    rel_path = str(LMARENA_FILE.relative_to(BASE))
    with LMARENA_FILE.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            if row.get("category") != "overall":
                continue  # style-controlled Elo specifically wasn't in this pull -- "overall" is the plain human-preference Elo
            d = parse_date(row.get("leaderboard_publish_date", ""))
            try:
                score = float(row.get("rating") or "")
            except ValueError:
                continue
            records.append({
                "benchmark": "lmarena-elo",
                "date": d,
                "model": (row.get("model_name") or "").strip(),
                "score": score,
                "score_unit": "Elo",
                "org": (row.get("organization") or "").strip(),
                "source": "https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset",
                "notes": f"category=overall (not style-controlled); rank={row.get('rank')}; votes={row.get('vote_count')}",
                "family": "lmarena_bulk",
                "file": rel_path,
                "extraction_method": "huggingface_dataset_or_space",
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
    n_no_source = sum(1 for r in rows if not r["source"])
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
        "n_points_no_source": n_no_source,
        "source_files": ";".join(sorted(set(r["file"] for r in rows))),
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
    method_counts = {}
    for r in rows:
        m = r.get("extraction_method", "unknown_no_source_recorded")
        method_counts[m] = method_counts.get(m, 0) + 1
    out["benchmarks"][slug] = {
        "display_name": display_name(slug),
        "description": DESCRIPTIONS.get(slug, ""),
        "unit_family": fam,
        "unit_label": rows[-1]["score_unit"],
        "source_files": sorted(set(r["file"] for r in rows)),
        "provenance_summary": method_counts,
        "points": [
            {
                "date": r["date"],
                "model": r["model"],
                "score": round(r["score"], 3),
                "unit": r["score_unit"],
                "org": r["org"],
                "source": r["source"],
                "extraction_method": r.get("extraction_method", "unknown_no_source_recorded"),
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
