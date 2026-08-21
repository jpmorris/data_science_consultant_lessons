# General knowledge / broad reasoning benchmarks

Research cluster covering: MMLU, MMLU-Pro, BIG-Bench Hard, HellaSwag, ARC,
TruthfulQA, Winogrande, AGIEval. Data files live in `../data/*.csv`
(columns: `date,model,score,score_unit,source_url,notes`).

A cross-cutting theme: five of these eight benchmarks (MMLU, HellaSwag, ARC,
Winogrande, and to a lesser extent BIG-Bench Hard) are now widely described by
independent aggregators as **saturated** — frontier models cluster within a
point or two of the ceiling, differences are within noise, and in several
cases the benchmark has been formally retired from a standard leaderboard.
TruthfulQA and AGIEval are the exceptions: both still show real spread
(averages well below the top scores) even among current models, for
different reasons discussed below.

---

## MMLU (Massive Multitask Language Understanding)

- **Maintainer/origin:** Hendrycks et al. (UC Berkeley), introduced 2020.
- **Measures:** Multiple-choice (4-option) knowledge across 57 subjects
  spanning humanities, STEM, social science, and professional domains —
  the closest thing the field has to a general-knowledge headline number.
- **Scale:** 0–100% accuracy (5-shot is the traditional standard; later
  reasoning models often report 0-shot CoT).
- **Leaderboard/URL:** original paper https://arxiv.org/abs/2009.03300;
  Epoch AI tracker https://epoch.ai/benchmarks/mmlu; Artificial Analysis
  https://artificialanalysis.ai/evaluations/mmlu-pro (MMLU-Pro companion).
  Papers With Code's MMLU leaderboard page now 404s/redirects — PWC appears
  defunct as of this research.
- **Data found:** 10 rows, 2023-03 (GPT-4, 86.4%) through 2026-04 (GPT-5.5,
  92.4%). Kept two pre-2024 anchors (GPT-4, Gemini Ultra) since MMLU predates
  2024 and they show how close to the ceiling the field already was.
- **Trend:** Effectively saturated for frontier models since ~2023–2024.
  GPT-4 (86.4%) was already within ~10 points of Gemini Ultra's claimed
  90.0% "exceeds human expert" score (achieved only via a non-standard
  32-sample chain-of-thought voting scheme). By 2024, GPT-4o/Claude 3
  Opus/Llama 3.1 405B all sat in the 87–89% band. Reported gains since then
  (o1: 91.8%, GPT-5.5: 92.4%) are real but incremental against a
  ~95–96%-ish practical ceiling (test-set noise/label-error rate). This is a
  clean "we've largely blown past this one" case.

## MMLU-Pro

- **Maintainer/origin:** TIGER-AI-Lab (Wang et al.), NeurIPS 2024, arXiv
  2406.01574. Explicitly designed to un-saturate MMLU: 12,000 questions,
  10 answer choices instead of 4, more reasoning-heavy.
- **Measures:** Same subject breadth as MMLU but harder, more
  reasoning-dependent questions; original paper reports a 16–33-point
  accuracy drop vs. MMLU for the same models.
- **Scale:** 0–100% accuracy.
- **Leaderboard/URL:** https://artificialanalysis.ai/evaluations/mmlu-pro;
  original leaderboard/data at https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro;
  code at https://github.com/TIGER-AI-Lab/MMLU-Pro.
- **Data found:** 12 rows, 2024-06 (paper baseline, GPT-4o 72.6%) through
  2026-08 (Claude Opus 5, 91.59%).
- **Trend:** Went from genuinely discriminating (2024 top model GPT-4o at
  72.6%, best open model Llama-3-70B at 56.2%) to itself approaching
  saturation by late 2025 — independent commentary (lifearchitect.ai) flags
  Gemini 3 Pro's 89.8% in November 2025 as the point MMLU-Pro effectively
  hit its ~90% ceiling. By August 2026 the top handful of models (Qwen3.7
  Max 89.6%, Claude Opus 5 91.59%) are clustered within ~2 points. A good
  illustration of the "benchmark treadmill": a harder successor benchmark
  buys the field roughly 18 months before it, too, saturates.

## BIG-Bench Hard (BBH)

- **Maintainer/origin:** Suzgun et al. (Google/Stanford), Oct 2022 — a
  23-task, hand-picked "hard" subset of the original BIG-Bench where prior
  models had scored below average human raters.
- **Measures:** Multi-step logical/algorithmic/commonsense reasoning
  (e.g., date understanding, causal judgment, tracking shuffled objects).
- **Scale:** 0–100% accuracy; both direct-answer and chain-of-thought
  variants are commonly reported.
- **Leaderboard/URL:** original paper https://arxiv.org/abs/2210.09261;
  current-ish leaderboard aggregator https://pricepertoken.com/leaderboards/benchmark/bbh.
- **Data found:** 10 rows, 2022-10 (PaLM 540B baseline) through 2026-06
  (Gemini 3.1 Pro Preview, 96.1%). Kept the 2022 PaLM anchors since BBH
  predates 2024 and they show the full climb.
- **Trend:** Climbed fast — GPT-4 broke 80% within 5 months of BBH's
  release, Claude 3.5 Sonnet hit 93.1% by August 2024. By April 2025,
  aggregator commentary describes frontier models as "exceeding 95% with
  CoT + majority voting," and by mid-2025 the field's hard-benchmark
  attention had visibly shifted to GPQA-Diamond and Humanity's Last Exam.
  Another clear saturation/retirement case.

## HellaSwag

- **Maintainer/origin:** Zellers et al. (UW/AI2), 2019.
- **Measures:** Commonsense sentence-completion / "what happens next"
  physical/situational reasoning, built via adversarial filtering against
  weaker models.
- **Scale:** 0–100% accuracy; reported human baseline ~95.6%.
- **Leaderboard/URL:** original site https://rowanzellers.com/hellaswag/;
  Papers With Code page now shows an unrelated "current SOTA" model
  (Shakti-LLM 2.5B) rather than a maintained frontier leaderboard, another
  sign PWC has gone stale; aggregator: https://llm-stats.com/benchmarks/hellaswag.
- **Data found:** only 5 rows — 2020-05 (GPT-3, 78.9% zero-shot) through
  2024-09 (Qwen2.5 32B, 85.2%, included for contrast). Sparse **on purpose**:
  frontier labs have largely stopped reporting HellaSwag in 2025–2026 model
  cards because there's nothing left to show.
- **Trend:** Fully saturated. GPT-4 hit 95.3% in March 2023 (10-shot),
  already at/above the human baseline; Claude 3 Opus followed a year later
  at 95.4%. HellaSwag was formally dropped from the Hugging Face Open LLM
  Leaderboard v2 in June 2024 specifically because it could no longer
  differentiate frontier models. This is the single cleanest "we blew past
  this one years ago" example in the cluster.

## ARC (AI2 Reasoning Challenge — ARC-Easy / ARC-Challenge)

**Note:** this is the Allen Institute for AI's 2018 grade-school-science
question set, NOT "ARC-AGI" (Chollet's Abstraction and Reasoning Corpus,
tracked at arcprize.org) — a different agent in this project covers ARC-AGI
separately. Several search results returned mixed/conflated results between
the two names; rows below were checked against the primary sources to avoid
that confusion.

- **Maintainer/origin:** Clark et al., Allen Institute for AI (AI2), 2018.
- **Measures:** Multiple-choice grade-school science questions, split into
  an "Easy" set and a harder "Challenge" set (questions that simple
  retrieval/co-occurrence baselines get wrong).
- **Scale:** 0–100% accuracy (25-shot is the common pretrained-model
  convention; 0-shot for many instruction-tuned model cards).
- **Leaderboard/URL:** official dataset https://allenai.org/data/arc;
  original paper https://arxiv.org/abs/1803.05457.
- **Data found:** 7 rows (both Challenge and Easy subsets), 2023-03 (GPT-4)
  through 2024-12 (DeepSeek-V3), all clustered 94.5–98.9%.
- **Trend:** Saturated. Every model found scores in the mid-90s to
  high-90s on both subsets, with less than 5 points separating GPT-4
  (2023) from DeepSeek-V3 (late 2024). An independent aggregator (llm-stats)
  put the mean across 25 currently-tracked models at 91.9% with only 7.9
  points of spread — consistent with a benchmark that stopped
  discriminating among serious models years ago.

## TruthfulQA

- **Maintainer/origin:** Lin, Hilton & Evans (Oxford/OpenAI), 2021,
  arXiv 2109.07958.
- **Measures:** Whether a model avoids repeating common human
  misconceptions/falsehoods across 817 adversarially-written questions in
  38 categories (health, law, finance, politics, etc.) — a truthfulness
  benchmark rather than a knowledge or reasoning one.
- **Scale:** 0–100%, typically reported as multiple-choice (MC1/MC2) or
  as "% truthful and informative" for free-form generation.
- **Leaderboard/URL:** https://github.com/sylinrl/TruthfulQA;
  aggregator https://llm-stats.com/benchmarks/truthfulqa.
- **Data found:** only 6 rows, 2023-03 (GPT-4, 59.0%) through 2026-08
  (MAI-Thinking-1, 88.0%). Sparse because TruthfulQA has fallen out of
  favor for standard frontier-model reporting — it doesn't appear at all
  in the DeepSeek-V3 or Llama-3.1 evaluation tables checked for this
  research, and the benchmark has been criticized in the literature (e.g.
  "Gaming TruthfulQA: Simple Heuristics Exposed Dataset Weaknesses") for
  being gameable by superficial cues rather than genuine truthfulness.
- **Trend:** NOT saturated — the one clear exception in this cluster. The
  current top model (MAI-Thinking-1, 88.0%) sits well above the ~60.5%
  average across the 18 models an aggregator currently tracks. This is a
  case where the field has partly moved on not because the benchmark is
  "solved," but because of validity concerns about what it's actually
  measuring, plus RLHF/alignment tuning producing large, hard-to-compare
  swings (Llama 2 70B jumped from 50.2% base to 64.1% after chat
  fine-tuning).

## Winogrande

- **Maintainer/origin:** Sakaguchi et al. (AI2), 2019 — a large-scale,
  adversarially-filtered version of the Winograd Schema Challenge
  (pronoun-resolution commonsense reasoning).
- **Measures:** Binary pronoun-resolution commonsense reasoning.
- **Scale:** 0–100% accuracy (5-shot is standard for base/pretrained
  models); reported human baseline ~94%.
- **Leaderboard/URL:** https://leaderboard.allenai.org/winogrande/;
  aggregator https://llm-stats.com/benchmarks/winogrande.
- **Data found:** only 5 rows, all from two sources: GPT-4's March 2023
  technical report (87.5%) and DeepSeek-V3's December 2024 technical
  report's own comparison table (DeepSeek-V2/V3, Qwen2.5-72B, Llama-3.1-405B,
  all 82–86%). Could not find any Winogrande numbers reported by 2025–2026
  frontier labs (GPT-5, Claude Opus, Gemini 3.x) — it appears to have
  dropped out of standard reporting entirely.
- **Trend:** Saturated and effectively retired. Winogrande was one of the
  six original tasks on the Hugging Face Open LLM Leaderboard v1, which was
  archived in June 2024 specifically because tasks like this had stopped
  separating good models from great ones. The absence of any 2025+ frontier
  data points is itself the signal here — labs stopped reporting it because
  there was nothing left to show.

## AGIEval

- **Maintainer/origin:** Zhong, Cui et al. (Microsoft Research), April 2023,
  arXiv 2304.06364.
- **Measures:** Human-centric standardized exams — SAT, LSAT, math
  competitions, Chinese Gaokao (college entrance exam), lawyer
  qualification tests, civil service exams, etc. — chosen because they're
  exams real humans take for real stakes, rather than a purpose-built ML
  eval set.
- **Scale:** 0–100% accuracy, reported both as an overall average and
  per-exam; separate English and Chinese question-set tracks exist.
- **Leaderboard/URL:** https://arxiv.org/abs/2304.06364; GitHub
  https://github.com/ruixiangcui/AGIEval; aggregator
  https://pricepertoken.com/leaderboards/benchmark/agieval-en (English) and
  .../agieval-zh (Chinese).
- **Data found:** 6 rows, 2023-07 (Llama 2 7B, 22.8%) through 2026-08
  (DeepSeek V3.2 Exp, 90.1% on the Chinese track). Sparse for the same
  reason as TruthfulQA/Winogrande — not a standard line item in 2024–2025
  frontier model cards (not present in the Llama 3.1 or DeepSeek-V3 eval
  tables checked) — but current leaderboard aggregators still actively
  track it for a long tail of ~136 (English) / 23 (Chinese) models.
- **Trend:** Not fully saturated, though getting close at the very top.
  Early 2023-era open models scored in the 20–45% range; by July 2026 the
  #1 model (Gemini 3.1 Pro Preview) reaches 94.0% on the English track, but
  the tracked-model average is only 79.7% (σ=13.2) — real spread still
  exists once you look past the top 2–3 models, unlike HellaSwag/ARC/
  Winogrande where even mid-tier current models cluster near the ceiling.

---

## Sourcing notes / caveats

- Papers With Code appears to be largely dead as a live leaderboard source
  as of this research (its MMLU/HellaSwag SOTA pages either 404-redirect or
  show a stale/unrelated "current SOTA"). Epoch AI's benchmarking hub and
  model pages are JS-rendered and did not expose per-model score tables to
  either text-fetch or the accessibility-tree snapshot used here, despite
  clearly hosting the underlying data — flagged in case a future pass wants
  to pull their raw dataset export instead of the web UI.
  Artificial Analysis's pages have the same JS-chart limitation, though
  their written summaries (surfaced via web search) were usable.
  Model technical reports/system cards (OpenAI, Anthropic, Meta, DeepSeek)
  and dedicated aggregator sites (llm-stats.com, pricepertoken.com,
  benchlm.ai) were the most reliable sources actually used.
- Some numbers for the same model/benchmark pair varied slightly across
  secondary sources (e.g., Llama 3.1 405B's BBH/MMLU-Pro figures differed
  by 1-2 points between aggregators). Where this happened, the CSVs cite
  whichever specific source was actually fetched/read for that row rather
  than trying to reconcile conflicting secondary reports.
