# Multimodal/Vision Benchmarks and the ARC-AGI Family

Research pass covering: MMMU, MMBench, ChartQA, DocVQA (Part 1) and ARC-AGI-1 /
ARC-AGI-2 / ARC-AGI-3 (Part 2, priority). CSVs live in `../data/*.csv`, one row
per `(date, model)` data point, columns `date,model,score,score_unit,source_url,notes`.

A note on naming before anything else: **ARC-AGI is not the same benchmark as
"ARC"** (the AI2 Reasoning Challenge, ARC-Easy/ARC-Challenge — grade-school
multiple-choice science questions, covered by a different research agent in
`arc.csv`). ARC-AGI (Abstraction and Reasoning Corpus for Artificial General
Intelligence) is François Chollet's grid-puzzle benchmark from the ARC Prize
Foundation. The shared "ARC" name is a genuine, frequent source of confusion in
both benchmark writeups and casual conversation — the two measure completely
different things (retrieved factual/scientific knowledge vs. novel
few-shot visual abstraction), and neither is a variant of the other.

---

## MMMU (Massive Multi-discipline Multimodal Understanding)

- **Maintainer:** MMMU team (multi-institution academic collaboration:
  IN.AI / University of Waterloo / OSU and collaborators); ongoing leaderboard at
  [mmmu-benchmark.github.io](https://mmmu-benchmark.github.io/)
- **What it measures:** College-exam-level multimodal reasoning across 30
  academic subjects (art, business, science, health/medicine, humanities,
  tech/engineering) using real exam figures, diagrams, charts, and images —
  answering requires expert-level subject knowledge, not just "read the image."
- **Scale:** 11.5K questions across 6 broad disciplines / 30 subjects / 183
  subfields, drawn from college textbooks, exams, and quizzes.
- **URL:** https://mmmu-benchmark.github.io/ (leaderboard JSON at
  `mmmu-benchmark.github.io/leaderboard_data.json`)
- **Data pulled:** 79 rows in `mmmu.csv`, spanning 2023-11-27 (GPT-4V, 56.8%)
  through 2026-07-01, plus the human-expert baseline tiers (98.6% for a "human
  expert, high" panel; 88.6% is the more commonly cited "expert" benchmark).
- **Trend:** MMMU climbed from ~50-60% (GPT-4V/Gemini Ultra era, late 2023)
  through the high-70s/low-80s by mid-2025 (o3, GPT-5) and has been sitting in
  the high-80s/~90% band since Claude Opus 5 (2026), essentially at or just
  above the ~88.6% human-expert baseline. Recent frontier snapshots increasingly
  report **MMMU-Pro** (a harder 10-option variant introduced because the
  original validation set was saturating) instead of standard MMMU — flagged
  per-row in the CSV notes where that substitution happens. This is itself a
  small-scale echo of the ARC-AGI goalpost-moving pattern below.

## MMBench

- **Maintainer:** OpenCompass / Shanghai AI Laboratory;
  [mmbench.opencompass.org.cn](https://mmbench.opencompass.org.cn/leaderboard)
- **What it measures:** Fine-grained multimodal ability across 20 leaf
  categories (logical reasoning, attribute/relation reasoning, coarse- and
  fine-grained perception) using a circular-evaluation protocol (each question
  asked with answer choices rotated) to reduce lucky-guess noise relative to
  single-pass multiple choice.
- **Scale:** MMBench-EN v1.1 test split, ~3K questions.
- **URL:** https://mmbench.opencompass.org.cn/leaderboard (backing data at
  `cdn.opencompass.org.cn/assets/mmbench/mmbench-data.json`)
- **Data pulled:** 69 rows in `mmbench.csv`, from GPT-4V (Nov 2023, 75.3%)
  through GPT-5 (Aug 2025, 86.8%), including the Claude 3/3.5/3.7, Gemini
  1.0/1.5/2.0/2.5, Qwen2-VL/Qwen2.5-VL, and InternVL2/2.5/3 families.
- **Trend:** Fast climb from the mid-60s/70s (2023-2024) into the mid-80s to
  high-80s by 2025, with open-weight models (Qwen2.5-VL-72B, InternVL3-78B,
  Gemini 2.5 Pro) pulling slightly ahead of the closed frontier leaders on this
  particular test in 2025 — score gains visibly compress (roughly 83→88 across
  all of 2025) compared to the 2023→2024 jump (75→86), consistent with
  saturation pressure on the older v1.1 test split.

## ChartQA

- **Maintainer:** Originally academic (Masry et al., ACL 2022 Findings);
  no single actively-updated public leaderboard survives Papers With Code's
  2025 shutdown, so this file is built from cross-lab technical-report tables
  rather than one canonical leaderboard.
- **What it measures:** Question answering over bar/line/pie charts requiring
  both visual reading and arithmetic/logical reasoning over the chart's data
  (e.g., "what's the difference between the two tallest bars").
- **Scale:** ~9.6K human-written + ~23.1K machine-generated questions over
  real-world charts; scored with "relaxed accuracy" (numeric answers within 5%
  tolerance).
- **URL:** original paper https://arxiv.org/abs/2203.10244; data points sourced
  from Anthropic's Claude 3.5 Sonnet Model Card Addendum and the Qwen2.5-VL
  Technical Report (both linked per-row).
- **Data pulled:** 11 rows in `chartqa.csv`, from Claude 3 Opus/Sonnet and
  GPT-4 Turbo (~78-81%, March-April 2024) through Qwen2.5-VL-72B (89.5%,
  February 2025). Includes a deliberate same-model, two-lab comparison
  (GPT-4o scored 85.7% by Anthropic vs. 86.7% by the Qwen team) to illustrate
  that a couple of points of benchmark movement can just be eval-harness noise.
- **Trend:** Moved from high-70s/low-80s to high-80s/~90% across 2024, i.e.
  approaching but not yet at ceiling; Papers With Code's shutdown makes it
  harder to track this one continuously going into 2026 (no single
  actively-maintained public leaderboard was located for this pass).

## DocVQA

- **Maintainer:** Originally CVC-UAB / Robust Reading Competition (Mathew et
  al., WACV 2021); like ChartQA, tracked here via cross-lab technical-report
  tables rather than one continuously-updated leaderboard.
- **What it measures:** Question answering over scanned/photographed document
  images (forms, reports, invoices) requiring layout- and text-aware reading,
  not just OCR.
- **Scale:** ~50K questions over ~12K document images; scored with ANLS
  (Average Normalized Levenshtein Similarity), which gives partial credit for
  near-miss text extraction.
- **URL:** original paper via https://rrc.cvc.uab.es/?ch=17; data points
  sourced from the same two cross-lab tables as ChartQA.
- **Data pulled:** 11 rows in `docvqa.csv`, from Claude 3 Opus/Sonnet and
  GPT-4 Turbo (~87-90% ANLS, March-April 2024) through Qwen2.5-VL-72B (96.4%,
  February 2025).
- **Trend:** This benchmark is essentially saturated — every frontier model
  checked here scores 87%+ ANLS, and the 2024-2025 top-of-leaderboard movement
  is only ~4 points (92.8% → 96.4%), a much flatter curve than ChartQA,
  MMMU, or MMBench over the same window. It's a good example of a multimodal
  benchmark that plateaued because the task genuinely got solved, not because
  of an evaluation artifact.

---

## The ARC-AGI family (priority section)

ARC-AGI is explicitly designed to resist the kind of memorization/pattern-match
saturation that hits benchmarks like DocVQA: each puzzle is a small number of
input/output grid examples illustrating a novel rule, and the model must infer
the rule and apply it to a new test grid, with fresh, human-generated puzzle
sets kept partly private specifically to block training-set leakage. This
makes the ARC-AGI trajectory an unusually clean natural experiment for the
talk's "is progress plateauing" question, precisely because the benchmark's
authors have repeatedly demonstrated that when models *do* start saturating
a version, that is treated as a benchmark-design problem to be fixed by
releasing a harder version, not as evidence that reasoning has been solved.

**Data sources used:** the official ARC Prize leaderboard's backing JSON
(`arcprize.org/media/data/{models,evaluations,datasets,providers}.json` and
`arcprize.org/media/data/leaderboard/v3.json`, discovered via the rendered
page's network requests — these are the same numbers arcprize.org's own charts
plot, just pulled as structured data instead of screen-scraped); the community
agent-harness leaderboard at
[github.com/arcprize/ARC-AGI-Community-Leaderboard](https://github.com/arcprize/ARC-AGI-Community-Leaderboard)
(structured YAML submissions, several cross-checked against their live
`arcprize.org/scorecards/<uuid>` pages for exact levels-completed counts); and
the OpenAI/ARC Prize blog post on the o3 breakthrough for the two headline
December 2024 numbers.

### ARC-AGI-1

- **Maintainer:** ARC Prize Foundation (François Chollet et al.)
- **What it measures:** Novel visual-abstraction puzzles (small colored grids)
  — infer a transformation rule from 2-5 demonstration pairs, apply it to a
  held-out test input. No natural-language or world knowledge is needed; the
  task is designed to require little-to-no training-data-driven solving.
- **Scale / splits:** ~400 training + 400 evaluation public tasks, plus
  semi-private and private evaluation sets used for leaderboard scoring so
  systems can't just memorize published answers.
- **URL:** https://arcprize.org/arc-agi/1/ ; leaderboard https://arcprize.org/leaderboard
- **Data pulled:** 80 rows in `arc-agi-1.csv`, from Icecuber's 2023 Kaggle
  solution (17%, pre-LLM symbolic search) through Nov-2019 human-panel
  baseline (98%) and up to Grok 4.6 / GPT-5.6 / Claude-family runs in
  Aug 2026 scoring in the high-80s to high-90s. Includes the two December
  2024 o3-preview headline numbers as a dedicated pair of rows: **75.7%** at
  low compute ($2,680 total / $26 per task — qualified for the public
  leaderboard under ARC-AGI-Pub's <$10k rule) and **87.5%** at high compute
  ($456,000 total / $4,560 per task, 172x the compute — publicized as a
  research result but disqualified from the cost-capped leaderboard).
- **Trend:** This is the headline "did AI break through a wall" moment for the
  whole ARC-AGI story — scores sat near 0-20% through GPT-4/GPT-4o-era models
  (2023 to late 2024), then jumped sharply with o3 in December 2024, and by
  2026 multiple frontier models (Claude Opus/Fable, GPT-5.x, Gemini 3.x) are
  clearing 90-98%, essentially matching the human baseline. ARC-AGI-1 is
  now close to saturated at the frontier — which is exactly why ARC-AGI-2
  exists.

### ARC-AGI-2

- **Maintainer:** ARC Prize Foundation, launched March 2025
- **What it measures:** Same puzzle format as ARC-AGI-1, but tasks were
  specifically curated to defeat "brute-force" search/program-synthesis
  solvers that had started to do well on ARC-AGI-1 without generalizing —
  ARC-AGI-2 tasks require more compositional, multi-step, and symbolic
  reasoning per puzzle, and every task was verified solvable by at least 2 of
  a panel of humans in under 2 attempts (to guarantee it's a fair, solvable
  test and not just "harder for the sake of harder").
- **Scale:** New training/evaluation task sets, same public/semi-private/
  private split structure as v1.
- **URL:** https://arcprize.org/arc-agi/2/ ; leaderboard https://arcprize.org/leaderboard
- **Data pulled:** 83 rows in `arc-agi-2.csv`, from o3-preview-low (4.0%,
  Dec 2024 — evaluated retroactively against the not-yet-released v2 set) and
  near-0% scores for GPT-4o/Claude 3.x-era models, through Claude Opus 5 (Max)
  at **90.4%** in July 2026. Note: several 2023-2024-dated rows (Icecuber,
  NVARC, ARChitects, GPT-4o) reflect *retroactive* evaluation of pre-existing
  models/solutions against the ARC-AGI-2 set after its March 2025 release, not
  contemporaneous ARC-AGI-2 scores — the model's original release date is kept
  in the `date` column for consistency with the rest of the file, but this is
  flagged here since it could otherwise look like ARC-AGI-2 existed a year
  earlier than it did.
- **Trend:** This is the clearest "moved goalposts" case in the dataset.
  ARC-AGI-2 launched specifically because ARC-AGI-1 was saturating, and it
  reset the frontier back to near-zero (o3, the very model that had just
  scored 87.5% on v1, could only manage ~4-6.5% on v2 at launch). From there
  it followed almost the identical S-curve shape as v1 — near-0% through most
  of 2025, breaking 30-50% by late 2025/early 2026 (Gemini 3 Pro, GPT-5.2),
  and reaching ~90% by mid-2026. The whole cycle from "new benchmark, ~0%" to
  "~90%, arguably saturating again" took roughly 16 months.

### ARC-AGI-3

- **Maintainer:** ARC Prize Foundation, competition launched 2025, ongoing
  through 2026
- **What it measures:** A deliberate format change from the first two
  versions — instead of static grid-transformation puzzles, ARC-AGI-3 is a
  set of small interactive video-game-like environments the agent must
  explore, form a hypothesis about the rules of, and act in over multiple
  steps to win levels. This targets a different capability gap: novel-skill
  acquisition and interactive/embodied reasoning rather than one-shot visual
  pattern completion, explicitly because static-grid puzzles were judged too
  narrow a test of "general" reasoning as v1/v2 scores climbed.
- **Scale:** 25 hand-built environments / 183 total levels in the current
  public demo set (per the scorecards pulled for this pass); a larger private
  set is used for the "official" ARC Prize competition track.
- **URL:** https://arcprize.org/arc-agi/3/ ; leaderboards
  https://arcprize.org/leaderboard/3 (bare-model baseline) and
  https://github.com/arcprize/ARC-AGI-Community-Leaderboard (custom agent
  harnesses)
- **Data pulled:** 36 rows in `arc-agi-3.csv`, split into two genuinely
  different populations that should not be averaged together:
  - **27 rows** from the official bare-model leaderboard (a frontier LLM
    given the raw game state with a minimal harness, no custom scaffolding):
    scores are almost all under 5%, with Claude Opus 5 (High) as a striking
    outlier at **30.2%** (July 2026) — otherwise this track looks nowhere
    near solved.
  - **9 rows** from the community leaderboard, where teams build custom
    agent harnesses (persistent memory files, executable world-model
    construction, multi-agent setups, etc.) on top of the same underlying
    models: scores here range from RGB-Agent's 82.4% (March 2026, Claude
    Opus 4.6 + a read/grep/bash tool harness) up to **two independent teams
    reaching a full 100% clear of the public demo set** — SingularityNET's
    `baseline1` (GPT-5.6-sol, July 15 2026) and Tycho (Claude Opus 5, July 29
    2026) — each at a few-thousand-dollar total run cost.
- **Trend:** ARC-AGI-3 is the sharpest illustration in this whole dataset of
  why "is the benchmark plateauing" and "is AI progress plateauing" are
  different questions. The *bare-model* score is barely off the floor 8
  months into the competition (which reads as "AI still can't do this"), while
  *harness-equipped* versions of essentially the same underlying models
  cleared the public set within about 4-5 months of the benchmark's public
  demo going live (which reads as "this is already basically solved, just not
  by the model alone"). Whether ARC-AGI-3 is "hard" depends entirely on
  which of those two leaderboards you're looking at — and the ARC Prize
  Foundation's own site keeps them as visibly separate tracks for exactly
  this reason.

### What the ARC-AGI arc implies for the "plateauing" thesis

Every version of ARC-AGI has followed the same shape: launch near 0%,
climb an S-curve to 80-100% at the frontier within roughly a year and a half,
then get replaced by a harder version before it can be called "solved" for
more than a few months. Read naively, each individual version's asymptote
could be mistaken for AI progress slowing down — scores compress into the
high-80s/90s and month-over-month gains shrink, which is what a plateauing
chart looks like. But the *family's* history shows the opposite: the
benchmark-makers are the ones moving the goalposts, on purpose, precisely
*because* frontier models keep clearing whatever bar was set 12-18 months
earlier. ARC-AGI-1's saturation triggered ARC-AGI-2; ARC-AGI-2 visibly
saturating in the last few months of this dataset (Claude Opus 5 at 90%+) is
plausibly what's driving the ARC Prize Foundation's heavier promotion of
ARC-AGI-3 in 2026. For a talk on whether AI progress is plateauing, the
honest framing is: individual benchmark curves plateau constantly, almost by
design, because that's the signal benchmark designers use to know it's time
to write a harder test — so a flattening curve on any one ARC-AGI version is
much weaker evidence of a real capability slowdown than it looks like at
first glance. The ARC-AGI-3 harness-vs-bare-model split adds a second wrinkle
on top of that: even within one benchmark, "saturated" can just mean
"saturated by systems with enough scaffolding," which is a moving target in
its own right as agent-harness engineering keeps improving independent of
the underlying model.
