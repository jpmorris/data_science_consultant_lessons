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
        "common-sense-qa-2", "superglue", "science-qa", "open-book-qa",
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
        "frontiercode", "webdev-arena", "deepswe",
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
lines.append("## Benchmark catalog")
lines.append("")

for cat_name, slugs in CATEGORIES:
    present = [s for s in slugs if s in data]
    if not present:
        continue
    lines.append(f"### {cat_name}")
    lines.append("")
    lines.append("| Benchmark | Data points | Date range | Score range | Status |")
    lines.append("| --- | --- | --- | --- | --- |")
    for slug in present:
        b = data[slug]
        pts = b["points"]
        dmin, dmax = pts[0]["date"], pts[-1]["date"]
        smin = min(p["score"] for p in pts)
        smax = max(p["score"] for p in pts)
        unit = b.get("unit_label", "")
        fam = b.get("unit_family", "")
        status = "likely saturated (near ceiling)" if (fam == "percent" and smax >= 90) else "still discriminating"
        lines.append(
            f"| **{b['display_name']}** (`{slug}`) | {len(pts)} | {dmin} → {dmax} | "
            f"{smin:g}–{smax:g} {unit} | {status} |"
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
lines.append("## Benchmarks most commonly cited in 2025-2026 frontier model releases")
lines.append("")
lines.append("Per the aggregator research pass: GPQA Diamond, SWE-bench Verified/Pro, ARC-AGI-1/2, "
             "Humanity's Last Exam, AIME, Terminal-Bench, and LMArena Elo recur across GPT-5.x, Claude "
             "Opus 4.x/5, Gemini 3/3.1 Pro, and Grok 4/4.x release announcements. Labs report against a "
             "shifting subset of ~5-7 benchmarks rather than one fixed suite, introducing new ones "
             "(ARC-AGI-2, agentic/tool-use evals) as older ones saturate — itself indirect evidence for "
             "the \"plateau vs. moved goalposts\" question this project is trying to answer.")
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
