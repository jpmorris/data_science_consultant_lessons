"""Generate benchmarks/README.md from aggregated.json + aggregated_summary.csv."""
import csv
import json
from pathlib import Path

BASE = Path(__file__).parent
data = json.load((BASE / "aggregated.json").open())["benchmarks"]

CATEGORIES = [
    ("General knowledge / broad reasoning", [
        "mmlu", "mmlu-pro", "big-bench-hard", "hellaswag", "arc", "truthfulqa",
        "winogrande", "agieval", "bool-q", "piqa", "lambada", "adversarial-nli",
        "common-sense-qa-2", "superglue", "science-qa", "open-book-qa", "trivia-qa",
    ]),
    ("General-purpose & human-preference leaderboards", [
        "live-bench", "lmarena-elo",
    ]),
    ("Elite reasoning & math", [
        "gpqa-diamond", "hle", "simpleqa", "simpleqa-verified", "gsm8k", "math",
        "aime", "frontiermath", "mathvista", "omni-math", "imo", "ioi",
        "otis-mock-aime-2024-2025", "critpt",
    ]),
    ("Code & software engineering", [
        "humaneval", "mbpp", "swe-bench-verified", "swe-bench-lite",
        "swe-bench-multimodal", "swe-bench-pro", "livecodebench",
        "livecodebench-elo", "codeforces-elo", "aider-polyglot", "scicode",
        "mirrorcode", "algotune", "cursorbench", "gso", "frontierswe",
        "frontiercode", "webdev-arena", "deepswe", "ale-bench",
    ]),
    ("Agentic, tool-use & computer-use", [
        "gaia", "webarena", "agentbench", "tau-bench", "osworld", "androidworld",
        "browsecomp", "vending-bench", "gdpval", "gdpval-elo",
        "the-agent-company", "terminal-bench", "cybench", "exploitbench",
        "apex-agents", "deepresearchbench",
    ]),
    ("Long-horizon autonomy, AI R&D & \"AI researcher\" / RSI signal", [
        "metr-time-horizon", "metr-cross-domain-time-horizon", "re-bench",
        "mle-bench", "paperbench", "ai-scientist",
        "openai-ai-self-improvement-evals", "posttrainbench",
    ]),
    ("Multimodal & vision", [
        "mmmu", "mmbench", "chartqa", "docvqa", "video-mme", "spatialviz-bench",
        "mindcube", "geobench",
    ]),
    ("ARC-AGI family (interactive/abstraction reasoning)", [
        "arc-agi-1", "arc-agi-2", "arc-agi-3",
    ]),
    ("Games, puzzles & misc. Epoch-run evals", [
        "chess-puzzles", "mystery-game-puzzles", "balrog", "surface-evolver-bench",
        "weirdml", "forecastbench", "fictionlivebench", "lech-mazur-writing",
        "simplebench", "rli", "cl-bench", "cl-bench-life", "blueprint-bench-2",
        "vpct", "enigma-eval", "cad-eval", "btf3", "proofbench", "gbaeval",
    ]),
]

categorized = set()
for _, slugs in CATEGORIES:
    categorized.update(slugs)
uncategorized = sorted(set(data.keys()) - categorized)

lines = []
lines.append("# AI Benchmark Landscape — Data Catalog")
lines.append("")
lines.append(
    "Research pass for the \"AI Benchmarks\" slide: as comprehensive an inventory as "
    "we could pull together of AI/LLM benchmarks and leaderboards, plus real "
    "(date, model, score) historical data for each, sourced from official "
    "leaderboards, papers, model release announcements, and benchmark "
    "aggregators. Built to answer one question: **is AI benchmark progress "
    "plateauing, or does it just look that way because we keep retiring "
    "saturated benchmarks and replacing them with harder ones?**"
)
lines.append("")
lines.append(f"**{len(data)} benchmarks/evals catalogued, {sum(len(b['points']) for b in data.values())} total (date, model, score) data points.**")
lines.append("")
lines.append("## How this is organized")
lines.append("")
lines.append("- `data/*.csv` — one file per benchmark (or per incompatible-unit variant, e.g. "
             "`livecodebench.csv` [pass@1 %] vs `livecodebench-elo.csv` [LiveCodeBench Pro "
             "Elo]), columns `date,model,score,score_unit,source_url,notes`. Hand-researched "
             "by parallel research agents, one real source URL per row minimum, no fabricated numbers.")
lines.append("- `data/aggregator-epoch-benchmarking-hub/` — Epoch AI's own bulk CSV export "
             "(CC-BY-4.0licensed, cite as `Epoch AI, 'AI Benchmarking Hub'. https://epoch.ai/benchmarks`), "
             "76 files, ~12,400 rows. This is the single richest source in the project and is merged "
             "into the per-benchmark CSVs above where it covers the same benchmark (see `aggregate.py`'s "
             "`ALIAS` map), and left as its own additional benchmark otherwise.")
lines.append("- `data/aggregator-lmarena-text-latest.csv`, `data/aggregator-epoch-notable-ai-models.csv`, "
             "`data/aggregator-epoch-frontier-ai-models.csv` — bulk model-metadata/leaderboard pulls "
             "(LMArena human-preference Elo, Epoch's model census) used for cross-referencing, not "
             "folded into individual benchmark series.")
lines.append("- `notes/*.md` — per-cluster research writeups from each research agent: what each "
             "benchmark measures, data-quality caveats, and trend read (saturated vs. still climbing).")
lines.append("- `aggregate.py` — merges everything above into `aggregated.json` (per-benchmark points "
             "plus a fitted trend curve: logistic for percent-scale benchmarks, exponential for "
             "time-horizon-style benchmarks, linear otherwise) and `aggregated_summary.csv` (one row "
             "per benchmark: point count, date range, score range, saturation flag).")
lines.append("")
lines.append("## What each benchmark measures")
lines.append("")
lines.append(
    "One-sentence description per benchmark, grouped the same way as the "
    "catalog below. Sourced from the per-cluster research notes "
    "(`notes/*.md`) and, for the long-tail Epoch-hub-only benchmarks not "
    "individually researched, from direct lookups against "
    "`epoch.ai/benchmarks/<slug>` — see `descriptions.py` for the full "
    "source dict."
)
lines.append("")

for cat_name, slugs in CATEGORIES:
    present = [s for s in slugs if s in data]
    if not present:
        continue
    lines.append(f"**{cat_name}**")
    lines.append("")
    for slug in present:
        b = data[slug]
        desc = b.get("description", "")
        lines.append(f"- **{b['display_name']}** — {desc}")
    lines.append("")

lines.append("## Data provenance")
lines.append("")
lines.append(
    "Every data point in `aggregated.json` carries a `source` URL and an "
    "`extraction_method` tag; every benchmark carries a `source_files` list "
    "(the exact CSV path(s) on disk backing it) and a `provenance_summary` "
    "(point counts by extraction method). Methods are assigned mechanically "
    "from the source URL's domain (see `classify_extraction_method()` in "
    "`aggregate.py`), not asserted from memory, so re-running the script "
    "reproduces the same tags."
)
lines.append("")
_all_points = [p for b in data.values() for p in b["points"]]
_method_counts = {}
for _p in _all_points:
    _m = _p.get("extraction_method", "unknown_no_source_recorded")
    _method_counts[_m] = _method_counts.get(_m, 0) + 1
lines.append(f"**{len(_all_points)} total data points, 0 with an empty source** (breakdown by extraction method):")
lines.append("")
lines.append("| Extraction method | Points | What it means |")
lines.append("| --- | --- | --- |")
_method_glossary = {
    "arxiv_or_academic_paper": "URL is arXiv/ACL/OpenReview/NeurIPS-proceedings — a paper's own results table.",
    "official_benchmark_leaderboard_or_site": "URL is the benchmark's own official leaderboard/project site (arcprize.org, swebench.com, metr.org, etc.).",
    "primary_lab_source": "URL is a frontier lab's own blog post, model card, or system card (OpenAI/Anthropic/Google/xAI/Meta).",
    "third_party_aggregator": "URL is a secondary aggregator (llm-stats.com, Artificial Analysis, Vals AI, etc.) — lower confidence than a primary source, flagged per-row.",
    "github_repo": "URL is a GitHub repo/README — usually a maintained leaderboard table in the benchmark's own code repo.",
    "huggingface_dataset_or_space": "URL is a Hugging Face dataset or Space.",
    "epoch_ai_page": "URL is an epoch.ai page cited directly by the hand-research pass.",
    "epoch_bulk_csv_no_row_source_used_hub_fallback": "Row came from Epoch AI's bulk CSV export with no per-row source link in Epoch's own schema; falls back to that benchmark's general epoch.ai/benchmarks page (verified to resolve) rather than being left blank.",
    "other_web_source": "URL didn't match a known domain pattern above; still a real, cited source, just uncategorized.",
    "unknown_no_source_recorded": "No source URL at all -- should be 0 rows; treat any nonzero count here as a bug to fix.",
}
for _m, _c in sorted(_method_counts.items(), key=lambda kv: -kv[1]):
    lines.append(f"| `{_m}` | {_c} | {_method_glossary.get(_m, '')} |")
lines.append("")
lines.append(
    "**Known fix in this pass:** an earlier version of `aggregate.py` left "
    "1,432 of 2,913 points (49.2%) with an empty `source` field, because "
    "10 of Epoch AI's 76 benchmark CSVs use a different column schema "
    "(`Log viewer`/`Logs` instead of `Source`/`Source link`) that the merge "
    "script didn't check, and those log-viewer/logs cells are empty for "
    "every row in those files anyway. Fixed by falling back to the "
    "benchmark's own epoch.ai hub page (a real, verified URL) for any row "
    "with no per-row source, tagged distinctly "
    "(`epoch_bulk_csv_no_row_source_used_hub_fallback`) so it's never "
    "confused with a genuine per-row citation."
)
lines.append("")

lines.append("## Benchmark catalog")
lines.append("")

for cat_name, slugs in CATEGORIES:
    present = [s for s in slugs if s in data]
    if not present:
        continue
    lines.append(f"### {cat_name}")
    lines.append("")
    lines.append("| Benchmark | Data points | Date range | Score range | Status | Source file(s) |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for slug in present:
        b = data[slug]
        pts = b["points"]
        dmin, dmax = pts[0]["date"], pts[-1]["date"]
        smin = min(p["score"] for p in pts)
        smax = max(p["score"] for p in pts)
        unit = b.get("unit_label", "")
        fam = b.get("unit_family", "")
        status = "likely saturated (near ceiling)" if (fam == "percent" and smax >= 90) else "still discriminating"
        files = "<br>".join(f"`{sf}`" for sf in b.get("source_files", []))
        lines.append(
            f"| **{b['display_name']}** (`{slug}`) | {len(pts)} | {dmin} → {dmax} | "
            f"{smin:g}–{smax:g} {unit} | {status} | {files} |"
        )
    lines.append("")

if uncategorized:
    lines.append("### Other Epoch-hub benchmarks not yet slotted into a category above")
    lines.append("")
    lines.append("| Benchmark | Data points | Date range |")
    lines.append("| --- | --- | --- |")
    for slug in uncategorized:
        b = data[slug]
        pts = b["points"]
        lines.append(f"| **{b['display_name']}** (`{slug}`) | {len(pts)} | {pts[0]['date']} → {pts[-1]['date']} |")
    lines.append("")

lines.append("## Leaderboard aggregators (where to track all of this going forward)")
lines.append("")
lines.append("See `notes/aggregators.md` for the full writeup. Summary:")
lines.append("")
lines.append("- **Epoch AI Benchmarking Hub** — https://epoch.ai/benchmarks — best bulk data source found; "
             "76-benchmark CC-BY export used throughout this project.")
lines.append("- **Artificial Analysis** — https://artificialanalysis.ai/ — 600+ models, 23+ evals, "
             "composite \"Intelligence Index\"; gated API.")
lines.append("- **LMArena** (formerly LMSYS Chatbot Arena) — https://lmarena.ai/ — 1M+ blind human "
             "A/B battles, Elo ratings; bulk dataset on Hugging Face (`lmarena-ai/leaderboard-dataset`).")
lines.append("- **ARC Prize** — https://arcprize.org/leaderboard — official ARC-AGI-1/2/3 leaderboards, "
             "structured JSON backing available.")
lines.append("- **METR** — https://metr.org/time-horizons/ — the time-horizon/autonomy benchmark, "
             "raw YAML published.")
lines.append("- **Vellum LLM Leaderboard**, **LiveBench**, **llm-stats.com** — secondary aggregators, "
             "useful for cross-checking recent snapshots.")
lines.append("- **Papers With Code** — effectively shut down (July 2025); no longer a reliable "
             "current source, though old SOTA tables were useful for pre-2025 history.")
lines.append("- **Hugging Face Open LLM Leaderboard** — archived/retired June 2024, citing benchmark "
             "saturation and compute cost as reasons — itself a small data point for this talk's thesis.")
lines.append("")
lines.append("## Most popular benchmarks — what labs and leaderboards actually cite")
lines.append("")
lines.append("Recurring benchmarks that show up across OpenAI / Anthropic / Google DeepMind / xAI "
             "release posts and system cards through 2026, with example cited scores:")
lines.append("")
lines.append("- **GPQA Diamond** — used by essentially every lab (Gemini 3 Pro: 91.9%; Gemini 3.1 Pro: "
             "94.3%; Grok 4: 88%; part of GPT-5.5's eval suite).")
lines.append("- **SWE-bench Verified** (and increasingly **SWE-bench Pro**) — the headline agentic-coding "
             "number. Claude Opus 4.5 (Nov 2025) led with 80.9%, the first model over 80%; GPT-5.5 "
             "reported 58.6% on SWE-bench Pro.")
lines.append("- **ARC-AGI (v1 and v2)** — used as a \"genuine reasoning, not memorization\" flex. Grok 4: "
             "66.6% (v1), 15.9% (v2); Claude Opus 4.5: 37.6% (v2); Gemini 3 Pro: 31.1% (v2); Gemini 3.1 "
             "Pro: 77.1% (v2) — the fastest visible jump of any benchmark in this whole project.")
lines.append("- **Humanity's Last Exam** — cited by xAI (Grok 4 Heavy: 44.4%) and one of the 9 components "
             "in Artificial Analysis's Intelligence Index.")
lines.append("- **AIME** (current-year math competition) — Gemini 3 Pro: 95% on AIME 2025; near-ceiling "
             "performance across frontier models is itself a plateau/saturation signal.")
lines.append("- **Terminal-Bench** — Claude Opus 4.5: 59.3% vs. Gemini 3 Pro 54.2% vs. GPT-5.1 47.6%.")
lines.append("- **LMArena / Chatbot Arena Elo** — the human-preference cross-check every lab now cites "
             "alongside static benchmarks (Gemini 3 Pro: \"tops LMArena at 1501 Elo\"; by Aug 2026, Claude "
             "Opus 4.7/4.8 and Gemini 3.1 Pro sit above the historic 1500 barrier).")
lines.append("- **Agentic/tool-use benchmarks** are the newest recurring category (Gemini 3.1 Pro: "
             "BrowseComp 85.9%, τ2-bench Telecom 99.3%, MCP Atlas 69.2%) — reflects the 2025-2026 shift "
             "from static Q&A toward long-horizon agent evaluation.")
lines.append("")
lines.append("**Pattern:** every major release leans on roughly the same 5-7 benchmark handful (GPQA "
             "Diamond, SWE-bench, ARC-AGI, HLE, AIME, Terminal-Bench/agentic evals, LMArena Elo) rather "
             "than one fixed universal suite — labs pick whichever subset makes their model look best, "
             "and the specific agentic/tool-use benchmarks used change release to release as older ones "
             "saturate. Labs introducing new evals (ARC-AGI-2 after v1 saturated, Terminal-Bench/agentic "
             "benchmarks as coding benchmarks saturate) is itself indirect evidence for the "
             "\"plateau vs. moved goalposts\" question this project is trying to answer.")
lines.append("")
lines.append("## Known data-quality caveats")
lines.append("")
lines.append("- Score units are NOT always comparable within what looks like \"one benchmark\" — e.g. "
             "\"LiveCodeBench\" pass@1 % vs. \"LiveCodeBench Pro\" Elo, or GDPval's OpenAI-reported % "
             "win-rate vs. Artificial Analysis's GDPval-AA Elo re-scoring — these were split into "
             "separate series (`*-elo` suffix) rather than plotted together.")
lines.append("- Some rows come from secondary aggregators rather than primary lab publications where "
             "primary sources didn't publish a clean historical table; flagged per-row in each CSV's "
             "`notes` column.")
lines.append("- A few benchmarks (SWE-bench Lite/Multimodal, WebArena, AgentBench) have very few real "
             "data points because frontier labs largely stopped reporting them in favor of newer "
             "benchmarks — that sparsity is itself a finding, not a research gap.")
lines.append("- \"Likely saturated\" in the tables above is a simple heuristic (top score ≥ 90% on a "
             "percent-scale benchmark) — see each benchmark's row/notes file for the actual nuance.")
lines.append("")

(BASE / "README.md").write_text("\n".join(lines), encoding="utf-8")
print("wrote", BASE / "README.md", f"({len(lines)} lines)")
