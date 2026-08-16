# Benchmark leaderboard aggregators — source catalog

Meta-sources for tracking AI/LLM benchmark progress over time. Researched
2026-08-16. Where a bulk dataset was actually retrieved, the local file is
noted (see `benchmarks/data/`).

---

## 1. Epoch AI — Benchmarking Hub

- **URL:** https://epoch.ai/benchmarks (dashboard) / https://epoch.ai/data (all datasets) / https://epoch.ai/benchmarks/use-this-data (docs for this dataset specifically)
- **Coverage:** Interactive hub covering benchmarks across math, software engineering, agentic tasks, games, world knowledge, science, multimodal, long-context, and writing (FrontierMath, SWE-bench Verified, GPQA Diamond, MATH level 5, OTIS Mock AIME, METR time-horizon, ARC-AGI, MMLU, and dozens more — 76 distinct benchmark CSVs in the bulk export as of this pull). Sourced from both Epoch's own evaluations and external benchmark creators/labs.
- **Bulk dataset — YES, and it's excellent.** Direct zip download at `https://epoch.ai/data/benchmark_data.zip` contains one CSV per benchmark (76 files, ~12,400 rows total) with columns: model version, mean score, best score, **release date**, organization, country, training compute (FLOP), stderr, and an eval-log id/timestamp. This is essentially ready-made "benchmark score vs. time, labeled by model/org" data — exactly the shape needed for a plateau/progress chart.
- **Also has a separate "AI Models" database** (not benchmark scores, but model metadata): downloadable as `all_ai_models.csv` (~21,000 models), `notable_ai_models.csv` (~8,300 "notable" models), `frontier_ai_models.csv` (~1,600 frontier-at-the-time models), `large_scale_ai_models.csv` (~3,600). Columns include publication date, org, country, training compute, parameters, accessibility, "Frontier model" flag — very useful for compute/timeline framing independent of benchmark scores.
- **Also offers a Python client** (`pip install epochai`) hitting an Airtable-backed API that preserves entity relationships better than the flat CSVs (per their docs).
- **License:** CC-BY 4.0 — free to reuse with attribution.
- **Saved locally:**
  - `benchmarks/data/aggregator-epoch-benchmarking-hub/` — full unzipped 76-file benchmark export (README + one CSV per benchmark, e.g. `gpqa_diamond.csv`, `swe_bench_verified.csv`, `frontiermath.csv`, `metr_time_horizons_external.csv`, `arc_agi_external.csv`, `live_bench_external.csv`, etc.)
  - `benchmarks/data/aggregator-epoch-notable-ai-models.csv` (~8,300 rows, full model metadata)
  - `benchmarks/data/aggregator-epoch-frontier-ai-models.csv` (~1,600 rows, frontier-model subset)
- **Verdict:** This is the best single source in the whole project. It's the only aggregator that hands you clean, dated, per-model, per-benchmark CSV rows in bulk with no scraping required — use it as the backbone for any "benchmark score over time" chart.

---

## 2. Artificial Analysis

- **URL:** https://artificialanalysis.ai/
- **Coverage:** 608 language models tracked (varies by leaderboard view) across 23+ independent evaluations, plus separate leaderboards for coding agents (59 models), image models (149), speech models (91), video generation, and API-provider endpoint-accuracy testing. Runs its own standardized evals rather than only aggregating labs' self-reported numbers.
- **"Intelligence Index" (currently v4.1.1):** composite of 9 evaluations — GDPval-AA v2, τ³-Banking, Terminal-Bench v2.1, SciCode, Humanity's Last Exam, GPQA Diamond, CritPt, AA-Omniscience, and AA-LCR. Also publishes sub-indices (Coding Index, Agentic Index, Math Index, Openness Index, Multilingual Index).
- **Bulk dataset — yes, via paid/attributed API.** `https://artificialanalysis.ai/data-api` (docs at `/data-api/docs`) — a proper API returning benchmark, pricing, and performance data for every tracked model, including all the individual index scores. Attribution to Artificial Analysis is required whenever the data is displayed/shared. Did not pull a sample (looked gated/requiring signup for API keys); the web leaderboard itself has no plain CSV export button.
- **Verdict:** Probably the second-best source after Epoch — broadest model coverage and a real API — but the API is not fully open/anonymous like Epoch's CSV zips, so it wasn't sampled here. Worth flagging to the user as a candidate for a follow-up API-key pull if the talk wants Artificial Analysis-specific numbers (e.g., the Intelligence Index trend line).

---

## 3. LMSYS Chatbot Arena / LMArena (now rebranded "Arena")

- **URL:** https://lmarena.ai/ now **301-redirects to https://arena.ai/** — the project rebranded from "LMArena" to "Arena" in 2026.
- **Coverage:** Human-preference Elo (Bradley-Terry since Jan 2024, still called "Elo" publicly) leaderboard from blind pairwise battles. Now spans many arena types beyond plain text chat: Vision, Search, Document, WebDev/Code, Agent, Text-to-Image, Image/Text-to-Video, Video-editing. Agent Arena is new as of June 4, 2026.
- **Bulk dataset — YES, and it's real.** Hugging Face dataset **`lmarena-ai/leaderboard-dataset`** (https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset), Parquet format, 22 subsets (one per arena/category), 2,171,642 rows total, 107 MB, license CC-BY-4.0. Each subset has a `full` split (every historical leaderboard snapshot) and a `latest` split (current standings only). Columns for the text/vision arenas: model_name, organization, license, rating, rating_lower/upper (confidence interval), variance, vote_count, rank, category, leaderboard_publish_date. Data goes back to Jan 2024 for text; newer arenas start later (Search/WebDev Aug/Nov 2025, Agent June 2026).
  - Separately, LMSYS also published raw **conversation-level** datasets on HF from the original 2023 era: `lmsys/chatbot_arena_conversations` (33K conversations w/ pairwise votes, Apr–Jun 2023) and `lmsys/lmsys-chat-1m` (1M conversations, Apr–Aug 2023) — these are conversation transcripts, not current leaderboard standings, and are now quite old.
- **Saved locally:** `benchmarks/data/aggregator-lmarena-text-latest.csv` — 10,262 rows pulled from the `text` / `latest` split of the HF dataset (current Elo standings for every text model ever ranked, one row per model+category combo as of the 2026-08-12 snapshot; top rows: `claude-opus-5-max` 1507.8, `claude-opus-5-high` 1505.3, `claude-opus-4-6-high` 1502.8). The `full` split (52.6 MB, complete historical Elo trajectory since Jan 2024) was located but not downloaded here — flagging it as available if the talk wants an Elo-over-time chart; `pd.read_parquet` on `text/full-00000-of-00001.parquet` via the HF resolve URL would pull it.
- **Verdict:** Second genuinely bulk-exportable dataset found. Excellent for an Elo leaderboard chart; the full historical split would support an Elo-over-time plateau/progress chart similar to Epoch's.

---

## 4. Vellum LLM Leaderboard

- **URL:** https://www.vellum.ai/llm-leaderboard
- **Coverage:** Aggregates "latest public benchmark performance for SOTA LLM model versions" from official releases and independent evals, covering Anthropic, OpenAI, Google, Meta, DeepSeek, and others. Sections for overall capability (Humanity's Last Exam), reasoning (GPQA Diamond), coding (SWE-bench), computer/browser/terminal use (OSWorld, AutoBench), plus separate operational tables (throughput, latency, price/M tokens). Model directory lists 60+ models with context window, pricing, knowledge cutoff.
- **Bulk dataset:** None found — plain HTML tables, no export/API mentioned on the page. Vellum does publish good narrative "X benchmarks explained" blog posts per major model release (used those as sources for the release-benchmark findings below).
- **Verdict:** Useful as a human-readable cross-check and for its per-model-release blog writeups, but not a data source — no export capability.

---

## 5. LiveBench

- **URL:** https://livebench.ai/ ; GitHub: https://github.com/LiveBench/LiveBench
- **Coverage:** Contamination-resistant benchmark suite explicitly designed to avoid the "benchmark saturates because labs train on the test set" problem. New questions released monthly (about 1/6 of the dataset rotated each month, full refresh every ~6 months); question sources include recent arXiv papers, news articles, IMDb synopses, and other very-recent material so training-data contamination is structurally limited. All questions have objective, verifiable ground-truth answers — scored without an LLM judge.
- **Bulk dataset:** The live site is JS-rendered so it couldn't be scraped directly here, but the **GitHub repo is the actual source of truth** — it contains the evaluation code and (per repo structure) the underlying results data used to generate the site's tables, since the site is generated from that repo's outputs. Not pulled in this pass; recommend a follow-up `git clone`/browse of `github.com/LiveBench/LiveBench` if per-question or per-model historical LiveBench scores are wanted.
- **Verdict:** Directly relevant to the "plateau" narrative of the talk — it's the aggregator explicitly built to distinguish real capability plateaus from contamination-driven benchmark inflation. Good to cite conceptually even without a data pull.

---

## 6. Papers With Code

- **URL:** paperswithcode.com
- **Status as of 2026: SHUT DOWN.** Papers With Code ceased operating in **July 2025**. The domain now redirects toward Hugging Face's "Trending Papers" feed; the original 1,500+ leaderboards and 18,000+ papers are no longer live/maintained, though the underlying data was released openly (CC-BY-SA) and lives on in frozen archives (e.g., a `paperswithcode-data` archive referenced by successor sites).
- **Successors filling the gap:** CodeSOTA (codesota.com) — live SOTA pages for coding/vision benchmarks, explicitly built as a PWC replacement, plus access to the frozen PWC archive for historical JSON; Hugging Face's Trending Papers section.
- **Bulk dataset:** The frozen archive exists but wasn't pulled in this pass (out of scope — PWC itself is dead, not an active aggregator).
- **Verdict:** No longer usable as a live source — mention its shutdown as a data point in itself (another data-tracking casualty as the field's benchmark culture shifted to labs/independent evaluators), but don't rely on it for current-day trend lines.

---

## 7. Hugging Face Open LLM Leaderboard

- **URL:** https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard
- **Status as of 2026: RETIRED/ARCHIVED**, static snapshot only. It was archived starting June 2024 and is not a live, continuously-updated board. HF's own stated reasoning: benchmark saturation, ballooning compute cost of continuously evaluating every new open-weight release, and the field's shift toward human-preference evaluation (i.e., arenas) as the more trustworthy signal. Its former role — ranking open-weight models — has effectively been absorbed by Artificial Analysis's Intelligence Index and by arena-style leaderboards.
- **Bulk dataset:** The historical results are still archived as HF datasets (e.g., `open-llm-leaderboard-old/results`) — a frozen snapshot, not actively growing.
- **Verdict:** Historically important, now a dead end for anything current — useful only as a "here's a benchmark-tracking project that itself became obsolete" illustration of the plateau/saturation theme, similar to Papers With Code.

---

## 8. llm-stats.com

- **URL:** https://llm-stats.com/
- **Coverage:** Self-described "Compare & Rank 300+ Top AI Models by Intelligence, Speed & Price" — an intelligence/speed/price comparison site. Page was gated behind a bot-check (CAPTCHA) during this research pass, limiting what could be confirmed about specific benchmarks used, methodology, or data freshness.
- **Bulk dataset:** Not confirmed either way — could not get past the CAPTCHA wall in this pass to check for an export/API page.
- **Verdict:** Lowest-confidence entry in this catalog; treat as a minor/secondary aggregator unless a follow-up manual visit turns up more (e.g., via a headed browser rather than plain fetch).

---

## 9. Most commonly cited benchmarks in frontier model release announcements

Recurring benchmarks that show up across OpenAI / Anthropic / Google DeepMind / xAI release posts and system cards through 2026:

- **GPQA Diamond** — graduate-level science Q&A; used by essentially every lab (Gemini 3 Pro: 91.9%; Gemini 3.1 Pro: 94.3%; Grok 4: 88%; GPT-5.5 system card includes it as part of its eval suite).
- **SWE-bench Verified** (and increasingly **SWE-bench Pro**) — software engineering / agentic coding. Claude Opus 4.5 (Nov 2025) led with 80.9%, the first model over 80%, explicitly framed as the headline coding number in Anthropic's announcement; GPT-5.5 reported 58.6% on SWE-bench Pro.
- **ARC-AGI (v1 and v2)** — abstraction/generalization, used as a "genuine reasoning, not memorization" flex. Grok 4: 66.6% (v1), 15.9% (v2); Claude Opus 4.5: 37.6% (v2, "more than double GPT-5.1"); Gemini 3 Pro: 31.1% (v2); Gemini 3.1 Pro: 77.1% (v2) — this benchmark saw the fastest visible jump of any in this set, worth highlighting for the "plateau vs. breakthrough" framing.
- **Humanity's Last Exam (HLE)** — broad frontier-knowledge stress test, cited by xAI (Grok 4 Heavy: 44.4%) and used as one of the 9 components in Artificial Analysis's Intelligence Index.
- **AIME (current-year math competition)** — Gemini 3 Pro: 95% on AIME 2025; near-ceiling performance across frontier models is itself a plateau signal.
- **Terminal-Bench** — autonomous/agentic terminal-use tasks; Claude Opus 4.5: 59.3% vs. Gemini 3 Pro 54.2% vs. GPT-5.1 47.6%.
- **LMArena / Chatbot Arena Elo** — the human-preference cross-check every lab now cites alongside static benchmarks (Gemini 3 Pro: "tops LMArena at 1501 Elo"; as of Aug 2026, Claude Opus 4.7/4.8 and Gemini 3.1 Pro sit above the historic 1500 barrier).
- **Agentic/tool-use benchmarks** are the newest recurring category (Gemini 3.1 Pro: BrowseComp 85.9%, τ2-bench Telecom 99.3%, MCP Atlas 69.2%) — reflects the field's 2025–2026 shift from static Q&A toward long-horizon agent evaluation, echoed in Epoch's METR "time horizon" benchmark and Artificial Analysis's Agentic Index.

**Pattern for the talk:** every major release leans on roughly the same 5–7 benchmark handful (GPQA Diamond, SWE-bench, ARC-AGI, HLE, AIME, Terminal-Bench/agentic evals, LMArena Elo) rather than a fixed universal suite — labs pick whichever subset makes their model look best, and the specific agentic/tool-use benchmarks used change release to release as older ones saturate. This selection behavior is itself worth a slide bullet: it's indirect evidence of benchmark saturation/plateau driving labs to keep introducing new evals (ARC-AGI-2 after v1 saturated, Terminal-Bench/agentic benchmarks as coding benchmarks saturate, etc.).
