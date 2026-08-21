# Long-horizon autonomy, AI R&D, and "AI researcher" benchmarks

Cluster covering: METR Task-Completion Time Horizon, HCAST, RE-Bench, MLE-bench,
PaperBench, autonomous "AI Scientist" paper-generation evals, and METR's
cross-domain time-horizon follow-up. This is the cluster most directly relevant
to recursive self-improvement (RSI): it asks not "can the model answer a hard
question" but "can the model stand in for a human AI researcher/engineer over
increasingly long, open-ended stretches of unsupervised work."

---

## 1. METR Task-Completion Time Horizon ("50% time horizon")

- **Maintainer:** METR (Model Evaluation and Threat Research), an independent
  nonprofit that partners with OpenAI/Anthropic/Google DeepMind for pre-deployment
  autonomy evaluations.
- **What it measures:** For a given model, the length of task (measured in
  *human-expert-equivalent completion time*) at which the model succeeds 50% of
  the time, estimated by fitting a logistic curve (probability of success vs.
  log of human task-completion time) across hundreds of tasks drawn from HCAST,
  RE-Bench, and SWAA (Software Atomic Actions).
- **Scale/units: TIME, not percent.** Reported in hours of human-equivalent
  task duration (this file's `metr-time-horizon.csv` stores raw hours; sub-hour
  values like GPT-2's 0.054h ≈ 3.2 minutes). This is the one benchmark in the
  whole project where the y-axis unit is a duration, not an accuracy score —
  flag this explicitly when combining with other benchmarks in the final chart
  (log-scale duration axis, not 0-100%).
- **URLs:** https://metr.org/time-horizons/ (live leaderboard) ·
  https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
  (original paper, arXiv:2503.14499) · raw data:
  https://metr.org/assets/benchmark_results_1_1.yaml · analysis code:
  https://github.com/METR/eval-analysis-public
- **Data:** `data/metr-time-horizon.csv` — **26 real data points**, one per
  model, pulled directly from METR's own published `benchmark_results_1_1.yaml`
  (their "METR-Horizon-v1.1" dataset), with 95% CIs preserved in the notes
  column. Date range: **2019-02-14 (GPT-2) to 2026-04-07 (Claude Mythos Preview,
  early)**. Models span GPT-2 → GPT-3 (davinci-002) → GPT-3.5 → GPT-4 family →
  Claude 3/3.5/3.7/4/4.1/Opus-4.5/4.6 → o1-preview/o1/o3 → GPT-5.x → Gemini
  3/3.1 Pro. This is real primary-source data, not chart-eyeballing.
- **Trend:** Time horizon has grown from ~3 minutes (GPT-2, 2019) to over
  **1,000 hours (~43 days)** for the most recent 2026 model, a roughly
  4-order-of-magnitude increase in under 7 years. METR's own fit gives an
  all-time doubling period of **~188 days**; restricting to the post-2023
  frontier-lab era, the doubling time is faster, **~129 days (95% CI
  104-158 days)**, i.e. progress has been *accelerating*, not plateauing, through
  early 2026 by METR's own numbers. Caveat stated directly on METR's site:
  "measurements above 16 hrs are unreliable with our current task suite" — so
  the newest, largest values (Claude Opus 4.6 at ~719h, Claude Mythos Preview at
  ~1,045h) carry wide confidence intervals (e.g. Opus 4.6: 95% CI 317-3,634
  hours) and should be shown with error bars, not as clean point estimates.

## 2. HCAST (Human-Calibrated Autonomy Software Tasks)

- **Maintainer:** METR. **What it measures:** the underlying 189-task suite
  (ML engineering, cybersecurity, general software engineering, reasoning) with
  563 human baseline attempts (1,500+ hours), each task hand-timed against
  skilled humans; this is the software backbone that feeds directly into the
  Time Horizon metric above (together with RE-Bench and SWAA).
- **URLs:** https://arxiv.org/abs/2503.17354 · code:
  https://github.com/METR/hcast-public
- **No standalone CSV produced.** HCAST does not publish an independent
  numeric "score per model" leaderboard separate from the time-horizon curve —
  it's the substrate, not a separate scoreboard. The paper reports success rate
  stratified by task-length bucket in figures only (e.g. "current agents
  succeed 70-80% of the time on tasks under 1 hour, <20% on tasks over 4
  hours"), not as an extractable table of exact per-model numbers. Rather than
  eyeball chart pixels, this cluster treats `metr-time-horizon.csv` as HCAST's
  quantitative face for charting purposes.

## 3. RE-Bench (Research Engineering Benchmark)

- **Maintainer:** METR. **What it measures:** head-to-head AI-agent vs.
  human-expert performance on 7 open-ended ML research engineering
  environments (kernel optimization, embedding recovery, RL fine-tuning,
  scaling-law experiments, etc.), scored 0 (starting point) to 1 (strong
  reference solution), under matched time budgets.
- **URLs:** https://arxiv.org/abs/2411.15114 ·
  https://metr.org/AI_R_D_Evaluation_Report.pdf · tasks:
  https://github.com/METR/RE-Bench
- **Data:** `data/re-bench.csv` — **4 real data points**, all from the single
  Nov 2024 paper (updated May 2025), since RE-Bench has no ongoing public
  leaderboard the way MLE-bench does. Cannot be extended to a longitudinal
  series without a maintained data table; the underlying figures (agent-vs-time
  score curves) are published only as chart images, not machine-readable data.
- **Trend (as of the one snapshot available):** at a **2-hour** budget, the
  best AI agents (Claude 3.5 Sonnet / o1-preview) scored **4x higher** than
  human experts; by an **8-hour** budget humans had narrowly overtaken agents;
  by a **32-hour** budget (best-of-k) humans scored **2x** the best agent. The
  qualitative shape — agents front-load progress fast, then plateau, while
  humans are slow to start but keep improving — is the opposite curve shape
  from the time-horizon chart's steady exponential, and is itself informative:
  it's a snapshot showing 2024-era models were "fast but shallow" researchers,
  not "fast and deep" ones. No public 2025/2026 refresh of this exact
  comparison was found.

## 4. MLE-bench (OpenAI)

- **Maintainer:** OpenAI. **What it measures:** agent ability to do real
  end-to-end ML engineering — 75 curated Kaggle competitions (worth $1.9M in
  historical prize value); primary metric is "any-medal rate" (bronze/silver/
  gold vs. the competition's real leaderboard).
- **URLs:** https://github.com/openai/mle-bench (actively-updated public
  leaderboard) · paper https://arxiv.org/abs/2410.07095
- **Data:** `data/mle-bench.csv` — **28 real data points**, pulled directly
  from the live GitHub README leaderboard table, spanning **2024-10-08
  (original paper baselines: AIDE+GPT-4o at 8.6%, MLAB+GPT-4o at 1.6%) through
  2026-03-06 (AIBuildAI + Claude Opus 4.6 at 63.1%)**. Score column uses the
  "All (%)" comparable split (any-medal rate across the full complexity
  range). **Caveat:** unlike the time-horizon table, each row here mixes a
  *scaffold/agent-framework* (AIDE, R&D-Agent, Famou-Agent, MARS, etc.) with an
  underlying *LLM* — so score gains reflect both model capability improvement
  and a maturing agent-harness ecosystem, not model capability in isolation.
  As of April 2026 the repo maintainers paused new leaderboard submissions
  pending a fairness/comparability review, so the series is provisionally
  frozen at that point.
- **Trend:** roughly **8x improvement** in any-medal rate from the original
  Oct 2024 baseline (best model then: 17.1%, o1-preview+AIDE) to the most
  recent frontier entries (~63-64%), with no visible plateau through early
  2026 — a top "Disarray" ensemble submission (flagged as not directly
  comparable due to test-set feedback) reports 77.8%.

## 5. PaperBench (OpenAI)

- **Maintainer:** OpenAI. **What it measures:** can an agent replicate a
  real ICML 2024 Spotlight/Oral paper from scratch (understand the
  contribution, write the codebase, run the experiments), graded against
  8,316 fine-grained, paper-author-reviewed rubric items across 20 papers.
- **URLs:** https://arxiv.org/abs/2504.01848 ·
  https://openai.com/index/paperbench/
- **Data:** `data/paperbench.csv` — **12 real data points** from the original
  paper's results tables (BasicAgent and IterativeAgent scaffolds), spanning
  model release dates **2024-05-13 (GPT-4o, 4.1%) through 2025-01-31
  (o3-mini-high, 2.6-8.5% depending on scaffold)**, plus the human ML-PhD
  baseline (41.4%, best-of-3 over 48 hours, on a 3-paper subset). Best model
  score in the original paper: Claude 3.5 Sonnet (New) BasicAgent at 21.0%, or
  o1-high IterativeAgent at 24.4-26.0% with an extended 36-hour budget.
  OpenAI's later GPT-5 system card (Aug 2025) states gpt-5-thinking became "the
  highest scoring model" on PaperBench and cites a **22%→24%** improvement
  figure in third-party summaries, but the system card itself presents this
  only as a bar-chart image without an accompanying numeric table, so it was
  **not** added as a CSV row (would require reading pixel values off a chart,
  which this project avoids).
- **Trend:** models still sit well below the 41.4% human baseline as of the
  most recent verifiable numbers (early-to-mid 2025); later 2025-2026 system
  cards suggest continued but not yet human-parity progress.

## 6. Autonomous "AI Scientist" / paper-generation systems

- **What's covered:** Sakana AI's "AI Scientist" (v1, v2), plus
  CycleResearcher, Data-to-Paper, and "FARS" (Fully Automated Research
  System) — systems that attempt the full pipeline (hypothesize → run
  experiments → write a paper) autonomously.
- **URLs:** independent evaluation of Sakana v1:
  https://arxiv.org/abs/2502.14297 · comparative benchmarking study (FARS):
  https://arxiv.org/abs/2607.28631
- **Data:** `data/ai-scientist.csv` — **6 real data points**. Feb 2025
  independent audit of Sakana AI Scientist v1 found **42% of its generated
  experiments failed from coding errors**, median 5 citations per paper (only
  5/34 from 2020+), papers costing $6-15 and ~3.5 human-hours each to
  produce — quality assessed as comparable to "an unmotivated undergraduate
  rushing a deadline." An April 2026 comparative study (FARS paper) scored five
  such systems on a 1-5 scale via three-LLM-judge automated peer review: FARS
  scored highest (synthesis 2.27; per-judge 2.14/2.47/2.47), while Sakana v1/
  v2, CycleResearcher, and Data-to-Paper all clustered near the 1.0 floor
  (near-uniform "poor" ratings from 2 of 3 judges).
- **Caveat — no benchmark here is peer-validated in the traditional sense.**
  Scores come from LLM-judge panels, not human peer review, and no comparison
  points to human PhD baseline quality on the same scale. There is not yet a
  standardized, longitudinally-tracked "AI Scientist" benchmark comparable in
  rigor to MLE-bench or the METR time horizon — this remains the least mature
  of the six benchmark families in this cluster.

## 7. METR cross-domain time horizon (follow-up study)

- **Maintainer:** METR. **What it measures:** whether the ~7-month doubling
  trend generalizes beyond the software/HCAST domain — re-derives time-horizon
  curves for ~9 other domains (math, scientific QA, competitive programming,
  agentic computer use, self-driving, video understanding) using existing
  public leaderboards (LiveCodeBench, GPQA Diamond, Mock AIME, OSWorld,
  WebArena, VideoMME, Tesla FSD disengagement data, etc.).
- **URLs:** https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains/
  · code: https://github.com/METR/cross-domain-horizon
- **Data:** `data/metr-cross-domain-time-horizon.csv` — **4 real data
  points** (doubling times in months, not model scores): METR-HRS/software
  ~4 months, Mock AIME/math ~3 months, Tesla FSD/self-driving ~20 months,
  OSWorld/agentic computer use ~24 months (~2 years). Several other domains
  the study covers (SWE-bench Verified, MATH, GPQA Diamond, LiveCodeBench,
  WebArena, VideoMME) were mentioned but without an explicit stated doubling
  time extractable from available text, so they were excluded rather than
  guessed.
- **Trend:** the study's headline finding — "in no domain examined is
  progress clearly sub-exponential" — held as of July 2025. Self-driving and
  agentic computer use double 5-8x slower than software/math, i.e. embodied
  and long-tail-UI domains lag pure cognitive/coding domains by a wide margin,
  which matters for RSI: an "AI researcher" bottlenecked on writing code and
  proving math lemmas would be progressing fast; one that also needs to
  operate real lab equipment or unfamiliar software would not be.

---

## What would plateau vs. continued-exponential actually mean here

This cluster is the most direct empirical proxy available for "is AI
capability now compounding its own improvement" — more so than any static
knowledge/reasoning benchmark, because time-horizon, RE-Bench, MLE-bench, and
PaperBench specifically test *substituting for an AI researcher/engineer* over
progressively longer stretches of autonomous work, which is the mechanism a
literal RSI loop would run on.

- **If the METR time-horizon doubling trend held or accelerated through
  2026** (it did, per the raw data here — post-2023 doubling of ~129 days vs.
  ~188 days all-time), the load-bearing question is whether that translates
  into genuine end-to-end research uplift, or just longer *coding-task*
  endurance. RE-Bench's one snapshot (Nov 2024) already showed models are
  "fast starters, slow finishers" relative to humans on genuinely open-ended
  research work — a very different shape than the smooth time-horizon curve —
  and no newer RE-Bench data exists to say whether that gap has closed.
- **MLE-bench's ~8x medal-rate improvement (2024→2026)** is real and
  encouraging for the "capability is compounding" story, but every top entry
  is a hand-engineered agent scaffold layered over a frontier LLM — so part of
  the gain is *tooling* maturity (better agent harnesses), which is a
  human-researcher-driven process, not evidence of the model self-improving
  unassisted.
- **PaperBench and the AI Scientist evaluations are the most sobering data
  points in this cluster.** Models were still well under the human PhD
  baseline (41.4% vs. best model ~21-26%) as of the most recent verifiable
  numbers, and independent audits of autonomous paper-writing systems found
  high failure rates, thin/outdated literature grounding, and quality akin to
  a rushed undergraduate — a genuine ceiling, not merely slow progress. A
  system that cannot yet reliably replicate an *existing* published result
  end-to-end is a long way from productively generating *novel* research that
  accelerates the next model generation.
- **Net read:** the pure "can it work autonomously for longer" axis (time
  horizon) shows no plateau — if anything it accelerated into 2026. But the
  "can it do genuinely novel, judgment-heavy R&D work as well as a human
  expert" axis (RE-Bench's long-budget comparison, PaperBench, AI Scientist)
  shows a real, currently-unclosed gap with only sparse longitudinal data to
  say whether *that* gap is closing quickly. For an RSI-specific claim, the
  second axis is the one that actually matters, and it is also the axis with
  the thinnest, least-refreshed public data — worth flagging explicitly on
  the slide rather than let the dramatic time-horizon chart imply more than
  it supports.
