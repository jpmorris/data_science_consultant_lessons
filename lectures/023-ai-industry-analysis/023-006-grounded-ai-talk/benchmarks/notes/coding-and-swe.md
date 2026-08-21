# Coding & Software-Engineering Benchmarks

Research cluster for the "is AI benchmark progress plateauing?" talk. CSVs live in `../data/`. All data points below are sourced from real web pages found via search/fetch (leaderboards, model announcement blog posts, or the original benchmark papers) — no numbers were estimated or interpolated.

## HumanEval

- **Maintainer/creator:** OpenAI (Chen et al., 2021).
- **What it measures:** Functional correctness on 164 hand-written Python programming problems; pass@1.
- **Scale:** 0-100% pass@1.
- **URLs:** original paper https://arxiv.org/abs/2107.03374; leaderboard aggregator https://www.codesota.com/llm/humaneval-mbpp; https://pricepertoken.com/leaderboards/benchmark/humaneval
- **Data:** 12 rows, 2021-07 to 2026-08.
- **Trend:** **SATURATED.** Went from 28.8% (Codex, 2021) → 67% (GPT-4, 2023) → 92%+ (Claude 3.5 Sonnet, GPT-4o, o1-preview, all by late 2024) → 97%+ (Claude Sonnet 4.5, DeepSeek R1, 2026). Every frontier model has cleared 90% since roughly late 2024, and current trackers explicitly call it saturated/contaminated: a 97% vs 98% score is a difference of under 2 of 164 problems, and the dataset has been in public training data for years.

## MBPP (Mostly Basic Python Problems)

- **Maintainer/creator:** Google Research (Austin et al., 2021).
- **What it measures:** 974 crowd-sourced, entry-level Python problems (task description + reference solution + 3 tests); pass@1.
- **Scale:** 0-100% pass@1 (a stricter "MBPP+"/EvalPlus variant also exists with harder test cases).
- **URLs:** https://www.codesota.com/llm/humaneval-mbpp; https://airank.dev/benchmarks/mbpp; https://llm-stats.com/benchmarks/mbpp; https://pricepertoken.com/leaderboards/benchmark/mbppplus
- **Data:** 15 rows, 2024-07 to 2026-08.
- **Trend:** **Also largely SATURATED at the frontier**, though messier than HumanEval — Claude Opus 4 hit 92% in May 2025, and multiple 2024-era open models (Qwen2.5-Coder-32B, Llama-3.3-Nemotron-49B) were already in the high-80s/low-90s by late 2024/early 2025. Notably, by 2026 the plain-MBPP leaderboards are topped by smaller/regional models (e.g. Sarvam-30B at 92.7%) rather than flagship frontier labs — a sign labs have stopped bothering to report it because it no longer differentiates. The harder MBPP+ variant (e.g. Kimi K2.6 at 66.9%) shows there's still headroom once test cases are toughened, but plain MBPP itself is done as a discriminator.

## SWE-bench / SWE-bench Verified

- **Maintainer/creator:** Princeton/SWE-bench team; SWE-bench Verified is OpenAI's human-filtered 500-problem subset (Aug 2024), now the field's default agentic-coding benchmark.
- **What it measures:** Whether an agent can resolve real GitHub issues (generate a patch that passes the repo's hidden tests) in real Python repositories.
- **Scale:** % of instances resolved (0-100%).
- **URLs:** https://www.swebench.com/ ; https://openai.com/index/introducing-swe-bench-verified/ ; https://www.vals.ai/benchmarks/swebench
- **Data:** 19 rows, 2024-08 to 2026-04 (`swe-bench-verified.csv`) — the richest series in this cluster.
- **Trend:** **Still climbing, not yet plateaued**, though the rate of gain is slowing. GPT-4o started at 33.2% (Aug 2024) → Claude 3.5 Sonnet 49% (Oct 2024) → Claude 3.7 Sonnet 70.3% custom-scaffold (Feb 2025) → Claude Opus 4 / Sonnet 4 ~72.5-72.7% (May 2025) → GPT-5 74.9% (Aug 2025) → Claude Opus 4.5 crosses 80% (Nov 2025) → Claude Sonnet 5 82.1% (2026). The curve is clearly decelerating (roughly +20pts in the first 6 months vs. +8pts in the most recent 6+ months), consistent with a benchmark approaching its ceiling, but it has not flattened the way HumanEval/MBPP have. Also worth flagging: OpenAI itself reportedly stopped emphasizing SWE-bench Verified as of ~Sept 2025, citing training-data leakage/shortcut-reward concerns, which is part of why the field is shifting toward SWE-bench Pro.

## SWE-bench Lite

- Smaller (300-problem), cheaper-to-run subset of the original SWE-bench.
- **URL:** https://pricepertoken.com/leaderboards/benchmark/swe-bench-lite
- **Data:** only 1 clean sourced point found (Claude Opus 4.6, 62.7%, Aug 2026) — labs have largely stopped reporting Lite in favor of Verified, so historical coverage is thin.

## SWE-bench Multimodal

- Extends SWE-bench to issues involving screenshots/UI mockups/diagrams.
- **URL:** https://llm-stats.com/benchmarks/swe-bench-multimodal
- **Data:** only 1 clean sourced point found (Claude Mythos Preview, 59.0%, 2026) — rarely reported; not enough history to characterize a trend.

## SWE-bench Pro

- **Confirmed to exist.** Launched 2025-09-19 by Scale AI (with academic collaborators): 1,865 problems across 41 actively-maintained repos, explicitly designed to resist the contamination/leakage that undermined SWE-bench Verified.
- **URLs:** https://labs.scale.com/papers/swe_bench_pro ; https://www.morphllm.com/swe-bench-pro ; https://labs.scale.com/leaderboard/swe_bench_pro_public
- **Data:** 6 rows, 2025-09 to 2026-08.
- **Trend:** Much harder than Verified by design — top models scored only ~23% on the public set at launch, still only ~59% (GPT-5.4 xHigh) on Scale's standardized public leaderboard by mid-2026, vs. vendor-reported aggregate numbers running higher (~68-80%) under different scaffolds/methodology. This is the benchmark to watch next as Verified saturates.

## LiveCodeBench

- **Maintainer/creator:** UC Berkeley / academic consortium (Jain et al.).
- **What it measures:** Competitive-programming-style problems continuously collected post-training-cutoff (self-repair, execution, test-output prediction, not just generation) to reduce contamination.
- **Scale:** pass@1 %; a separate "LiveCodeBench Pro" variant reports Elo.
- **URLs:** https://artificialanalysis.ai/evaluations/livecodebench ; https://llm-stats.com/benchmarks/livecodebench-pro
- **Data:** 12 rows, 2026-06 to 2026-08 snapshot (all recent — didn't find well-sourced 2024 numbers for this specific tracker).
- **Trend:** Wide spread even among recent models (GPT-4o near 3%, reasoning models 30-90%+), and the leaderboard is still shuffling at the top (Gemini 3 Pro 91.7% narrowly ahead of Gemini 3 Flash 90.8%) — **not saturated**, still a live discriminator between frontier reasoning models.

## Codeforces Elo (as an AI coding benchmark)

- **Not a single maintained benchmark** — multiple labs/trackers submit model solutions to Codeforces-style judging and report a Human-comparable Elo. Two lineages found: (1) informal OpenAI-model-progression tracking (officechai.com), and (2) the academic **CodeElo** benchmark (Peking Univ. et al., arXiv 2501.01257) which submits directly to the real Codeforces judge.
- **Scale:** Standard Codeforces Elo (rough human comparison: ~1200 = beginner, ~1900 = Master, ~2400 = Grandmaster, ~3000+ = Legendary Grandmaster).
- **URLs:** https://officechai.com/ai/how-openais-models-got-exponentially-better-at-coding-over-the-last-2-years/ ; https://arxiv.org/abs/2501.01257 ; https://codeforces.com/blog/entry/151090
- **Data:** 15 rows, 2022-11 to 2026-02.
- **Trend:** **Still climbing steeply, no plateau.** GPT-3.5 (~0 Elo, 2022) → GPT-4 (392) → GPT-4o (808) → o1 (1891, late 2024) → o3 (2727, ranking ~175th human worldwide, early 2025) → Gemini 3 Pro (2512) → Gemini 3 Deep Think (3455, "Legendary Grandmaster," Feb 2026, beaten by only ~7 active humans). This is arguably the most dramatic, least-plateaued curve in the whole coding cluster.

## Aider Polyglot

- **Maintainer/creator:** aider.chat (Paul Gauthier), also tracked by Epoch AI.
- **What it measures:** 225 Exercism exercises across C++/Go/Java/JavaScript/Python/Rust, scored inside Aider's actual edit loop (model must emit structured diffs, gets a second attempt after seeing failing-test output) — a realistic proxy for agentic coding-assistant quality, not just raw code generation. Replaced Aider's original (now-saturated, 80%+) single-language benchmark.
- **Scale:** % correct after 2 attempts, 0-100%.
- **URLs:** https://aider.chat/docs/leaderboards/ ; https://aider.chat/2024/12/21/polyglot.html ; https://epoch.ai/benchmarks/aider-polyglot
- **Data:** 24 rows, 2024-12 to 2025-10 (out of ~70 available on the live table — trimmed to a representative spread here).
- **Trend:** Rapid, fairly steady climb, **not yet plateaued**: o1 opened the leaderboard at 61.7% (Dec 2024) → Claude 3.7 Sonnet 64.9% (Feb 2025) → Gemini 2.5 Pro 76.9-83.1% (May-Jun 2025) → o3-pro 84.9% (Jun 2025) → GPT-5 (high) 88.0%, the highest score found (Aug 2025). Roughly +26 points in 8 months with no sign of flattening yet, though the gap between the top model and the pack has been narrowing.

## SciCode

- **Maintainer/creator:** SciCode-bench team, scientist-curated (Tian et al., 2024), arXiv 2407.13168.
- **What it measures:** Code synthesis for real scientific-research problems (338 subproblems from 80 main problems across 16 natural-science subfields: physics, chemistry, biology, materials science, math), with scientist-written gold solutions/tests. Much harder and less contaminated than HumanEval/MBPP.
- **Scale:** pass@1 %, reported at both subproblem-level and full-main-problem level (main-problem scores are much lower / stricter).
- **URLs:** https://arxiv.org/abs/2407.13168 ; https://scicode-bench.github.io/ ; https://pricepertoken.com/leaderboards/benchmark/scicode
- **Data:** 10 rows, 2024-07 to 2026-07.
- **Trend:** **Far from saturated.** At launch (Jul 2024) the best model (Claude 3.5 Sonnet) solved only 4.6% of main problems in the realistic setting. Two years later (Jul 2026) the best tracked model (Claude Fable 5) is still only at ~60% pass@1 on the (easier) subproblem-style leaderboard metric. This is the clearest counter-example in the cluster to "AI coding benchmarks are plateauing" — there's a lot of headroom left specifically on real scientific-computing tasks.

## Bonus find: Terminal-Bench

- Not on the original list but referenced repeatedly in 2025-2026 frontier releases (Anthropic's Claude 4 launch cites it right alongside SWE-bench Verified; Google and OpenAI coverage does the same for Gemini 3.1 Pro / GPT-5.x).
- **Maintainer:** Harbor / Laude Institute, with Snorkel AI contributing data — an open, continuously-updated, adversarially-curated task set.
- **What it measures:** Agent competence in real shell/terminal environments on long-horizon, multi-step tasks (file manipulation, recovery from failed tool calls) — a step beyond single-repo-patch benchmarks like SWE-bench toward general agentic-computer-use coding.
- **Scale:** % of tasks completed, versioned (v1, 2.0, 2.1, 3.0 — versions are not directly comparable to each other since task sets change).
- **URLs:** https://www.tbench.ai/leaderboard ; https://www.tbench.ai/leaderboard/terminal-bench/2.0 ; https://www.anthropic.com/news/claude-4
- **Data:** 10 rows, 2025-05 to 2026-05.
- **Trend:** Climbing fast on the current (2.0) version: Claude Opus 4 scored 43.2% on the original v1 (May 2025); by 2026 top agents on the harder v2.0 task set are clearing 80-85% (best found: NexAU-AHE running GPT-5.5, 84.7%, May 2026). Because the benchmark maintainers keep raising the difficulty (v2.1, v3.0 already exist), it's explicitly designed to avoid the saturation problem HumanEval/MBPP ran into.

---

## Overall read for the plateau question

- **Saturated / no longer useful for differentiating frontier models:** HumanEval, MBPP (plain variant).
- **Still climbing but decelerating (partial plateau signal):** SWE-bench Verified — biggest, best-tracked series in this cluster, clearly slowing down (~20pt gain in 6 months in 2024 vs. ~8pt gain in a comparable recent window), but not flat.
- **Still climbing steeply, no plateau:** Codeforces Elo, Aider Polyglot, LiveCodeBench, Terminal-Bench.
- **Nowhere near saturated, large headroom:** SciCode, SWE-bench Pro (both explicitly designed post-2024 to escape the saturation/contamination that hit the earlier benchmarks).
- Net pattern for the slide: coding benchmarks aren't uniformly plateauing — the *old, easy, contamination-prone* ones (HumanEval, MBPP, and to a lesser extent SWE-bench Verified) are topping out, while the field keeps inventing *harder, contamination-resistant* successors (SciCode, SWE-bench Pro, Terminal-Bench, LiveCodeBench) that reset the headroom. That treadmill effect is itself worth calling out on the slide.
