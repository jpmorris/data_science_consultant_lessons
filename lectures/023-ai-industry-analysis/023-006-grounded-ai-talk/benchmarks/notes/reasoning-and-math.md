# Elite reasoning exams and math benchmarks

Cluster covered: GPQA/GPQA Diamond, Humanity's Last Exam, SimpleQA/SimpleQA
Verified, GSM8K, MATH/MATH Level 5, AIME, FrontierMath, MathVista, Omni-MATH,
IMO (informal AI benchmark), IOI (informal AI benchmark).

All data points below are cited to a real, fetched source URL. Where a search
aggregator (Artificial Analysis, llm-stats.com, BenchLM, pricepertoken.com,
Vals AI, etc.) was the only available source for a data point, that is noted
explicitly — treat those rows as lower-confidence than primary
lab/paper/official-leaderboard sources.

---

## GPQA / GPQA Diamond

- **Maintainer/creator:** NYU and Anthropic researchers (Rein et al., 2023).
- **Measures:** 198 graduate-level, "Google-proof" multiple-choice questions
  in biology, chemistry, physics (Diamond subset). Skilled non-experts with
  internet access score ~34%; PhD-level experts ~65-70%.
- **Scale:** 0-100% accuracy.
- **URL(s):** https://epoch.ai/benchmarks/gpqa-diamond ,
  https://artificialanalysis.ai/evaluations/gpqa-diamond
- **Data:** `data/gpqa-diamond.csv` — 8 rows, 2024-06 to 2026-02.
- **Trend:** Climbed fast: Claude 3.5 Sonnet 59.4% (Jun 2024) → o1 78.3%
  (Sep 2024) → o3 87.7% (Dec 2024) → Claude Opus 4.6 ~91.3% (early 2026) →
  Gemini 3.1 Pro ~94.1% (Feb 2026). **Approaching saturation for frontier
  models** — top scores are now well above the reported human PhD-expert
  baseline (~69.7%), so GPQA Diamond is losing discriminating power among
  the very best models even though it isn't fully maxed out.

## Humanity's Last Exam (HLE)

- **Maintainer/creator:** Center for AI Safety (CAIS) and Scale AI.
- **Measures:** 2,500 expert-vetted, frontier-difficulty questions across
  math, science, humanities — explicitly designed to be far from saturated.
- **Scale:** 0-100% accuracy (text-only/no-tools variant tracked here).
- **URL(s):** https://agi.safe.ai/ , https://labs.scale.com/leaderboard/humanitys_last_exam
- **Data:** `data/hle.csv` — 9 rows, Jan 2025 launch to Aug 2026.
- **Trend:** Still clearly climbing, not saturated. At launch (Jan 2025)
  leading models scored single digits (GPT-4o 2.7%, Claude 3.5 Sonnet 4.1%,
  o1 8.0%). By early 2026 the official CAIS/Scale leaderboard showed
  ~30-38% (Gemini 3 Pro Preview 37.5%). By Aug 2026, aggregator snapshots
  put the frontier around 50-55% (Claude Fable 5 ~55.5%). This is exactly
  the kind of "designed to stay hard" benchmark still showing steep gains.

## SimpleQA / SimpleQA Verified

- **Maintainer/creator:** Original SimpleQA — OpenAI (Oct 2024). SimpleQA
  Verified — Google DeepMind (Sep 2025), a de-duplicated/rebalanced/
  relabeled 1,000-question refinement of the original 4,326-question set.
- **Measures:** Short-answer factual recall ("parametric knowledge") without
  retrieval/tools; graded correct/incorrect/not-attempted.
- **Scale:** 0-100% (accuracy for original; F1 for Verified).
- **URL(s):** https://openai.com/index/introducing-simpleqa/ ,
  https://epoch.ai/benchmarks/simple-qa-verified ,
  https://arxiv.org/html/2509.07968v1
- **Data:** `data/simpleqa.csv` (7 rows, Oct 2024-Jul 2026) and
  `data/simpleqa-verified.csv` (8 rows, all from the Sep 2025 paper's own
  Table).
- **Trend:** Rising but nowhere near saturated — even the best model in the
  SimpleQA Verified paper (Gemini 2.5 Pro) only reached 55.6% F1, and
  GPT-4o scored just 34.9%. This benchmark measures pure parametric recall
  (deliberately answerable-but-obscure trivia), so scores well under 100%
  are expected by design; it is not intended to reach ceiling the way
  GSM8K did.

## GSM8K (grade-school math)

- **Maintainer/creator:** OpenAI (Cobbe et al., 2021).
- **Measures:** Grade-school-level multi-step arithmetic word problems.
- **Scale:** 0-100% accuracy.
- **URL(s):** https://arxiv.org/pdf/2204.02311 (PaLM paper, cites original
  Cobbe et al. results), aggregator: codesota.com
- **Data:** `data/gsm8k.csv` — 7 rows, 2021 to 2026-03.
- **Trend: SATURATED.** GPT-3+verifier reached 55% (2021), PaLM 58% (2022),
  GPT-4 92% (2023); by 2024 all frontier models (GPT-4o, Claude 3.5,
  Gemini 1.5) exceeded 90%, and by 2025-2026 aggregator-reported scores are
  at 99%+ (GPT-5 99.2%, ERNIE 5.0 99.7%). Widely regarded in the field as
  retired for frontier-model discrimination since ~2023-2024; residual gaps
  reflect noise/labeling issues more than capability differences.

## MATH (Hendrycks et al.) / MATH Level 5

- **Maintainer/creator:** Hendrycks et al. (UC Berkeley), 2021.
- **Measures:** 12,500 competition-style math problems (AMC/AIME-sourced),
  7 subject areas, 5 difficulty levels; Level 5 = hardest.
- **Scale:** 0-100% accuracy.
- **URL(s):** https://huggingface.co/datasets/hendrycks/competition_math ,
  historical figures via https://bounded-regret.ghost.io/forecasting-math-and-mmlu-in-2023/
- **Data:** `data/math.csv` — 7 rows, 2021 to 2024-09.
- **Trend: Effectively saturated for frontier general models by late 2024.**
  GPT-3 6.9% (2021) → Minerva 540B 33.6% (2022) → GPT-4 42.5% (Mar 2023) →
  GPT-4o 76.6% (2024) → o1 94.8% (Sep 2024). Because o1-era reasoning
  models cleared the ~95% mark, MATH (full set) has largely been supplanted
  by harder successors (AIME-as-benchmark, Omni-MATH, FrontierMath) for
  differentiating current frontier models — could not source recent (2025+)
  frontier scores on the original MATH set, likely because labs stopped
  reporting it once it saturated.

## AIME (as a live AI benchmark, 2024-2026 exams)

- **Maintainer/creator:** Not AI-specific — AIME is the real American
  Invitational Mathematics Examination (MAA); repurposed by AI labs as a
  contamination-resistant-ish yearly benchmark using each year's fresh
  15-problem exam.
- **Measures:** Competition-level pre-olympiad math (integer-answer
  problems), reported as % of problems solved (pass@1, sometimes with
  test-time-compute variants).
- **Scale:** 0-100% (or problems solved out of 15).
- **URL(s):** model release blogs/system cards (OpenAI, Anthropic, Google
  DeepMind); aggregated at https://lifearchitect.ai/o3/
- **Data:** `data/aime.csv` — 9 rows, Sep 2024 to Feb 2026.
- **Trend:** Rapid, still-visible climb through 2024-2025 (GPT-4o baseline
  ~12% → o1 74.4% → o3 96.7% on AIME 2024; Gemini 2.5 Pro 92.0%/86.7% on
  2024/2025 sets; GPT-5 94.6% on AIME 2025), but **now showing saturation
  signs at the very top** — Claude Opus 4.6 reports 99.79% on AIME 2025,
  which Anthropic's own system card flags as a possible contamination risk
  since AIME problems and solutions are public. AIME is likely to be
  retired/rotated (new year's exam swapped in) as a discriminating
  benchmark the way GSM8K and MATH were.

## FrontierMath (Epoch AI)

- **Maintainer/creator:** Epoch AI, with problems written by professional
  mathematicians (some IMO gold medalists, Fields Medal-adjacent reviewers).
  Launched Nov 2024; v2 (error-corrected) released 2026-06-12; Tier 4
  (hardest, research-level) added as an expansion set.
- **Measures:** Original, unpublished research-to-exploratory-level math
  problems, all-or-nothing scoring (no partial credit).
- **Scale:** 0-100% problems solved, reported per tier (Tiers 1-3 vs Tier 4).
- **URL(s):** https://epoch.ai/frontiermath/tiers-1-4 ,
  https://arxiv.org/pdf/2411.04872 , https://ourworldindata.org/grapher/ai-frontiermath-over-time
- **Data:** `data/frontiermath.csv` — 7 rows, Nov 2024 to 2026.
- **Trend: Explicitly designed to be very hard, and still climbing fast —
  not saturated.** At launch (Nov 2024) no tested model (GPT-4o, Claude
  3.5 Sonnet, Gemini 1.5 Pro, o1-preview, Grok 2) exceeded 2%. OpenAI's o3
  was claimed at >25% internally (Dec 2024) but Epoch AI's independent
  re-test of the public release found only ~10% (Apr 2025) — a notable
  case of a lab's internal claim not replicating externally. By late 2025,
  Gemini 3 Pro reached 38% (Tiers 1-3) / 19% (Tier 4). Tier 4 in particular
  remains far from ceiling and is the benchmark this cluster's data most
  clearly supports as "still climbing, likely to keep discriminating
  frontier models for a while."

## MathVista

- **Maintainer/creator:** Lu et al. (UCLA/Washington/Microsoft et al.),
  ICLR 2024.
- **Measures:** Mathematical reasoning in visual contexts (charts, geometry
  diagrams, figures) — 6,141 examples, "testmini" 1,000-example subset used
  for leaderboard comparisons.
- **Scale:** 0-100% accuracy.
- **URL(s):** https://mathvista.github.io/ , https://github.com/lupantech/MathVista
- **Data:** `data/mathvista.csv` — 9 rows, Oct 2023 to 2026.
- **Trend:** Fast climb through 2024 (Multimodal Bard 34.8% → GPT-4V 49.9%
  → GPT-4o 63.8%, first to beat the reported 60.3% human average → o1
  73.9% by Sep 2024), continuing into 2026 (Seed 2.1 Pro ~90.7% per a 2026
  aggregator snapshot). Approaching saturation at the top but the official
  GitHub leaderboard did not show much confirmed 2025 primary-source data
  in this search — worth a follow-up pass against the live leaderboard.

## Omni-MATH

- **Maintainer/creator:** KbsdJames et al. (STAR Lab / academic
  collaboration), published Oct 2024.
- **Measures:** 4,428 olympiad-level competition math problems, 33+
  sub-domains, human-annotated difficulty ratings 1-10.
- **Scale:** 0-100% accuracy (GPT-4o- or Omni-Judge-graded).
- **URL(s):** https://arxiv.org/pdf/2410.07985 , https://omni-math.github.io/ ,
  https://llm-stats.com/benchmarks/omnimath
- **Data:** `data/omni-math.csv` — 8 rows, Oct 2024 to 2025.
- **Trend:** Explicitly built to be hard and was **not** saturated at
  launch: best "vanilla" model (Qwen2.5-MATH-72B) only reached 36.2%; the
  best test-time-compute model, o1-mini, reached 60.54% (and dropped to
  48.56% on problems above difficulty 5/10). By a later aggregator snapshot
  in 2025, reported top scores (e.g., Phi-4-reasoning-plus ~81.9%) show
  continued fast progress, though the gap between the original paper's
  ~60% ceiling and this later ~82% figure is large enough that it's worth
  double-checking methodology consistency before using both numbers in the
  same chart.

## International Mathematical Olympiad (IMO) — informal AI benchmark

- **Not a maintained ML benchmark** — this is the real human IMO
  competition; AI labs have opportunistically tested/entered systems
  against the same problems since 2024.
- **Scale:** Points out of 42 (6 problems x 7 points); ~29 = silver
  threshold, ~35 = gold threshold in 2024/2025 (varies slightly by year).
- **Data:** `data/imo.csv` — 4 rows, 2024-2026.
- **Trend / key results:**
  - **IMO 2024:** Google DeepMind's AlphaProof + AlphaGeometry 2 scored
    28/42 (silver-medal standard), solving 4 of 6 problems — a
    Lean-formalized system, not end-to-end natural language, and the first
    AI ever to reach medal-equivalent IMO performance.
  - **IMO 2025:** Both Google DeepMind (Gemini Deep Think, 35/42,
    **IMO-coordinator-certified**) and OpenAI (an experimental
    general-purpose reasoning model, 35/42, **self-graded, not
    IMO-certified**) reached gold-medal-level scores, working end-to-end in
    natural language within the standard 4.5-hour limit. OpenAI announced
    first; DeepMind's was the official, certified result.
  - **IMO 2026:** RedNote's (Xiaohongshu) `dots-note-3.0` model reportedly
    achieved a **perfect 42/42**, solving all 6 problems — the first
    perfect AI score at the IMO, per SCMP. Model was described as still
    in beta / the lightest model in RedNote's dots3 family.
  - This progression (silver → gold → perfect, 2024→2025→2026) is one of
    the clearest "still climbing, not remotely plateaued" signals in this
    entire cluster, though note the certification-status differences
    (DeepMind IMO-certified vs. OpenAI/RedNote self-reported) matter for
    how rigorously each claim should be trusted.

## International Olympiad in Informatics (IOI) — informal AI benchmark

- **Not a maintained ML benchmark** — real human competitive-programming
  olympiad; separate from IMO. AI labs/aggregators have tested systems
  against IOI problem sets since 2024.
- **Scale:** Percentile/rank among human contestants, or aggregator-defined
  percent score against IOI problem sets.
- **URL(s):** https://stats.ioinformatics.org/results/2025 ,
  https://www.vals.ai/benchmarks/ioi ,
  https://the-decoder.com/openais-ai-system-wins-a-gold-medal-level-score-at-the-international-olympiad-in-informatics-2025/
- **Data:** `data/ioi.csv` — 5 rows, 2024 to Aug 2026.
- **Trend:** Sharp jump for OpenAI between 2024 and 2025 — narrowly missed
  bronze (49th percentile) in 2024, then reached **gold-medal level, 6th of
  330 (98th percentile)** in 2025, notably using a lighter-weight
  general-purpose scaffold rather than IOI-specific fine-tuning. A later
  (Aug 2026) Vals AI leaderboard shows continued strong scores for frontier
  models (Claude Opus 5 ~91.7%) but also flags **large year-to-year
  variance within the same model** (e.g., one model scoring 100% on 2024
  problems but only 44.5% on 2025 problems), suggesting IOI scores should
  be read cautiously — they may reflect contamination/familiarity with
  older problem sets more than a stable capability trend.

---

## Saturated vs. still-climbing summary

| Benchmark | Status |
|---|---|
| GSM8K | **Saturated** (~99%+ by 2025-2026; retired as a frontier discriminator since ~2023-2024) |
| MATH (full set) | **Effectively saturated** for frontier general models (~95%+ by late 2024); labs largely stopped reporting it |
| GPQA Diamond | **Approaching saturation** at the top (mid-90s% by 2026), though still used actively |
| AIME | **Showing saturation signs** at the very top (Claude Opus 4.6 ~99.8% on AIME 2025, flagged for possible contamination) |
| MathVista | **Approaching saturation** (~90%+ by 2026 aggregator data) |
| SimpleQA / SimpleQA Verified | Rising, **not saturated** — best model still only ~55% F1 (Verified) |
| Omni-MATH | Rising fast, **not saturated** (best ~60-82% depending on snapshot, on a benchmark designed to stay hard) |
| Humanity's Last Exam | Rising fast, **clearly not saturated** (frontier ~50-55% by Aug 2026, designed to resist saturation) |
| FrontierMath (esp. Tier 4) | **Not saturated** — Tier 4 still in the 10-20% range as of late 2025; the clearest "still climbing" case in this cluster |
| IMO (informal) | **Not saturated / still improving** — silver (2024) → gold (2025) → perfect score claimed (2026) |
| IOI (informal) | Improving but **noisy/inconsistent** year-to-year — treat trend with caution |

## Notable caveats found during research

- Several 2026-dated figures in this cluster come only from third-party
  aggregator sites (Artificial Analysis, llm-stats.com, BenchLM,
  pricepertoken.com, Vals AI, lifearchitect.ai) rather than primary lab
  publications, because the aggregators were the only sources this search
  surfaced for that specific model/date. These are flagged in each CSV's
  `notes` column and should be treated as lower-confidence than
  official system cards/model cards/papers.
- The OpenAI o3 FrontierMath episode (internal >25% claim vs. independently
  verified ~10%) is a good illustrative example for a "beware benchmark
  marketing" slide.
- IMO 2025 has a real certification-status asymmetry worth calling out on
  slides: DeepMind's gold was IMO-coordinator-certified; OpenAI's gold was
  self-graded and announced first, before DeepMind's official result.
