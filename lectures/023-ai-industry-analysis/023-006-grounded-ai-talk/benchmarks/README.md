# AI Benchmark Landscape — Data Catalog

Research pass for the "AI Benchmarks" slide: as comprehensive an inventory as we could pull together of AI/LLM benchmarks and leaderboards, plus real (date, model, score) historical data for each, sourced from official leaderboards, papers, model release announcements, and benchmark aggregators. Built to answer one question: **is AI benchmark progress plateauing, or does it just look that way because we keep retiring saturated benchmarks and replacing them with harder ones?**

**74 benchmarks/evals catalogued, 2913 total (date, model, score) data points.**

## How this is organized

- `data/*.csv` — one file per benchmark (or per incompatible-unit variant, e.g. `livecodebench.csv` [pass@1 %] vs `livecodebench-elo.csv` [LiveCodeBench Pro Elo]), columns `date,model,score,score_unit,source_url,notes`. Hand-researched by parallel research agents, one real source URL per row minimum, no fabricated numbers.
- `data/aggregator-epoch-benchmarking-hub/` — Epoch AI's own bulk CSV export (CC-BY-4.0licensed, cite as `Epoch AI, 'AI Benchmarking Hub'. https://epoch.ai/benchmarks`), 76 files, ~12,400 rows. This is the single richest source in the project and is merged into the per-benchmark CSVs above where it covers the same benchmark (see `aggregate.py`'s `ALIAS` map), and left as its own additional benchmark otherwise.
- `data/aggregator-lmarena-text-latest.csv`, `data/aggregator-epoch-notable-ai-models.csv`, `data/aggregator-epoch-frontier-ai-models.csv` — bulk model-metadata/leaderboard pulls (LMArena human-preference Elo, Epoch's model census) used for cross-referencing, not folded into individual benchmark series.
- `notes/*.md` — per-cluster research writeups from each research agent: what each benchmark measures, data-quality caveats, and trend read (saturated vs. still climbing).
- `aggregate.py` — merges everything above into `aggregated.json` (per-benchmark points plus a fitted trend curve: logistic for percent-scale benchmarks, exponential for time-horizon-style benchmarks, linear otherwise) and `aggregated_summary.csv` (one row per benchmark: point count, date range, score range, saturation flag).

## What each benchmark measures

One-sentence description per benchmark, grouped the same way as the catalog below. Sourced from the per-cluster research notes (`notes/*.md`) and, for the long-tail Epoch-hub-only benchmarks not individually researched, from direct lookups against `epoch.ai/benchmarks/<slug>` — see `descriptions.py` for the full source dict.

**General knowledge / broad reasoning**

- **MMLU** — Multiple-choice knowledge across 57 subjects (humanities, STEM, social science, professional exams) — the field's original general-knowledge headline number.
- **MMLU-Pro** — A harder, 10-choice, more reasoning-heavy successor to MMLU built specifically to un-saturate it.
- **Big Bench Hard** — 23 hand-picked "hard" tasks from BIG-Bench where earlier models scored below average human raters — multi-step logical/algorithmic/commonsense reasoning.
- **Hellaswag** — Commonsense "what happens next" sentence completion, built via adversarial filtering against weaker models.
- **ARC (AI2 Reasoning Challenge)** — Grade-school multiple-choice science questions (Easy + Challenge splits) — NOT the same benchmark as ARC-AGI below, despite the shared name.
- **Truthfulqa** — Whether a model avoids repeating common human misconceptions across 817 adversarially-written questions in 38 categories.
- **Winogrande** — Large-scale, adversarially-filtered pronoun-resolution commonsense reasoning (a scaled-up Winograd Schema Challenge).
- **AGIEval** — Real human standardized exams — SAT, LSAT, math competitions, China's Gaokao, bar exams — used as an AI benchmark instead of a purpose-built eval set.
- **BoolQ** — Naturally-occurring yes/no reading-comprehension questions paired with a supporting Wikipedia passage.
- **PIQA** — Physical commonsense reasoning — choosing which of two ways to accomplish a everyday physical goal makes more sense.
- **LAMBADA** — Predicting a passage's final word where broad discourse context (not just the last sentence) is required to get it right.
- **Adversarial NLI** — Natural language inference (entailment/contradiction/neutral) on examples adversarially collected to fool existing models.
- **CommonsenseQA 2.0** — True/false commonsense-knowledge statements, built adversarially via a human-vs-model "gotcha" collection game.
- **SuperGLUE** — A harder successor to GLUE bundling several difficult natural-language-understanding tasks into one suite.
- **ScienceQA** — Multimodal, multiple-choice science questions (often with images/diagrams) that also require a supporting explanation.

**Elite reasoning & math**

- **GPQA Diamond** — 198 graduate-level, "Google-proof" science questions in biology, chemistry, and physics — skilled non-experts with internet access score only ~34%.
- **Humanity's Last Exam** — 2,500 expert-vetted, frontier-difficulty questions across math, science, and humanities, explicitly designed to resist saturation for years.
- **SimpleQA** — Short-answer factual recall (no retrieval/tools) on deliberately obscure-but-answerable trivia, graded correct/incorrect/not-attempted.
- **SimpleQA Verified** — A de-duplicated, rebalanced, relabeled 1,000-question refinement of SimpleQA (Google DeepMind).
- **GSM8K** — Grade-school-level multi-step arithmetic word problems.
- **Math** — 12,500 competition-style math problems (AMC/AIME-sourced) across 7 subject areas and 5 difficulty levels.
- **AIME** — Real yearly American Invitational Mathematics Examination problems, repurposed as a fresh, contamination-resistant-ish annual AI benchmark.
- **FrontierMath** — Original, unpublished research-to-exploratory-level math problems written by professional mathematicians, all-or-nothing scored, no partial credit.
- **MathVista** — Mathematical reasoning that requires reading visual context — charts, geometry diagrams, figures — not just text.
- **Omni-MATH** — 4,428 olympiad-level competition math problems across 33+ sub-domains with human-annotated difficulty ratings.
- **IMO (Intl. Mathematical Olympiad)** — The real International Mathematical Olympiad — AI systems opportunistically entered against the same problems as human competitors since 2024.
- **IOI (Intl. Olympiad in Informatics)** — The real International Olympiad in Informatics — a competitive-programming olympiad AI systems have been tested against since 2024.
- **OTIS Mock AIME** — Practice AIME-style contest problems (Olympiad Training and Inspiration Sessions) used as an additional fresh math-benchmark source.

**Code & software engineering**

- **HumanEval** — 164 hand-written Python programming problems, graded by functional correctness (pass@1) against hidden unit tests.
- **MBPP** — 974 crowd-sourced, entry-level Python problems (description + reference solution + tests), graded pass@1.
- **SWE-bench Verified** — Whether an agent can resolve real GitHub issues — generate a patch that passes the repo's actual hidden tests — on a 500-problem, human-filtered subset.
- **SWE-bench Lite** — A smaller, cheaper-to-run 300-problem subset of the original SWE-bench.
- **SWE-bench Multimodal** — SWE-bench extended to issues that involve screenshots, UI mockups, or diagrams.
- **SWE-bench Pro** — A harder, 1,865-problem SWE-bench successor across 41 actively-maintained repos, designed to resist the contamination that hit the original.
- **LiveCodeBench** — Competitive-programming-style coding problems continuously collected after each model's training cutoff, to reduce contamination.
- **LiveCodeBench Pro (Elo)** — A separate, Elo-scored competitive-programming variant of LiveCodeBench ("LiveCodeBench Pro") — not on the same scale as the pass@1 version.
- **Codeforces (Elo)** — Model solutions submitted to real Codeforces-style competitive-programming judging, reported as a human-comparable Elo rating.
- **Aider Polyglot** — 225 Exercism coding exercises across 6 languages, scored inside Aider's real edit loop (including a second attempt after seeing failing tests) as a proxy for agentic coding-assistant quality.
- **SciCode** — Code synthesis for real scientific-research problems across 16 natural-science subfields, with scientist-written gold solutions.
- **MirrorCode** — Reimplementing a real command-line program from scratch by observing only its input/output behavior, not its source code.
- **AlgoTune** — Whether a model can optimize existing code to run measurably faster than a reference implementation while staying correct.
- **CursorBench** — Ambiguous, multi-file coding tasks pulled from real Cursor IDE sessions — comprehension, bug-finding, refactoring, review.

**Agentic, tool-use & computer-use**

- **GAIA** — Real-world questions requiring reasoning, multimodal handling, web browsing, and tool use — easy for humans, hard for AI assistants.
- **WebArena** — End-to-end task success across 812 long-horizon tasks on self-hosted, fully-functional websites (e-commerce, forums, GitLab, a CMS).
- **AgentBench** — LLM-as-agent decision-making across 8 environments — OS, database, knowledge graph, card game, house-holding, web shopping/browsing.
- **tau-bench** — Tool-using dialogue agents in customer-service domains (retail, airline), graded on task completion AND compliance with the company's stated policy.
- **OSWorld** — Real, executable computer-use tasks (GUI + CLI) in genuine desktop OS environments, execution-graded against a 72%-scoring human baseline.
- **AndroidWorld** — Autonomous control of real Android apps across 116 dynamically-parameterized tasks spanning 20 apps.
- **BrowseComp** — Persistent, multi-hop web browsing to surface hard-to-find, entangled facts — designed to resist saturation by non-agentic models.
- **Vending-Bench** — Long-horizon coherence of an autonomous agent running a simulated vending-machine business over very long task sequences.
- **GDPval (real-world expert tasks)** — Real work-product tasks (documents, slides, CAD, audio/video) across 44 occupations, graded by blind pairwise comparison against a human expert's actual deliverable.
- **GDPval (Elo, Artificial Analysis)** — A separate Elo-rescoring of GDPval by Artificial Analysis — not on the same scale as OpenAI's original % win-rate metric.
- **Terminal Bench** — Agent competence in real shell/terminal environments on long-horizon, multi-step tasks including recovery from failed tool calls.

**Long-horizon autonomy, AI R&D & "AI researcher" / RSI signal**

- **METR Time Horizon** — The length of task (in human-expert-equivalent hours) a model can complete autonomously with 50% success — METR's flagship autonomy-duration metric.
- **METR Cross-Domain Time Horizon** — Re-derives the time-horizon doubling trend across ~9 other domains (math, science QA, coding, computer use, self-driving) to test whether it generalizes beyond software.
- **RE-Bench (METR)** — Head-to-head AI-agent-vs.-human-expert performance on 7 open-ended ML research-engineering tasks under matched time budgets.
- **MLE-bench** — Real end-to-end ML engineering on 75 curated Kaggle competitions, scored by "any-medal rate" against the competition's actual leaderboard.
- **Paperbench** — Whether an agent can replicate a real ICML Spotlight/Oral paper from scratch — understand it, write the code, run the experiments — against an author-reviewed rubric.
- **AI Scientist (Sakana et al.)** — Fully autonomous research pipelines (hypothesize → experiment → write a paper), quality-scored by LLM-judge panels, not human peer review.
- **OpenAI Self-Improvement Evals** — Can a model replicate real internal OpenAI engineering pull requests, or diagnose real unsolved internal research bottlenecks — a direct proxy for "can it do an AI researcher's job."

**Multimodal & vision**

- **MMMU** — College-exam-level multimodal reasoning across 30 academic subjects, using real exam figures/diagrams that require expert subject knowledge to interpret.
- **MMBench** — Fine-grained multimodal ability across 20 categories, using a circular-evaluation protocol (answer choices rotated) to reduce lucky guessing.
- **ChartQA** — Question answering over bar/line/pie charts, requiring both visual reading and arithmetic reasoning over the chart's data.
- **DocVQA** — Question answering over scanned/photographed document images (forms, reports, invoices), requiring layout- and text-aware reading, not just OCR.

**ARC-AGI family (interactive/abstraction reasoning)**

- **ARC-AGI-1** — Novel visual-abstraction grid puzzles — infer a transformation rule from a few demonstration pairs and apply it to a held-out test grid, with almost no reliance on world knowledge.
- **ARC-AGI-2** — A harder ARC-AGI successor, curated specifically to defeat brute-force search solvers that had started clearing v1 without genuinely generalizing.
- **ARC-AGI-3** — Small interactive video-game-like environments an agent must explore, form a hypothesis about, and act in over multiple steps — a shift from static puzzles to interactive/embodied reasoning.

**Games, puzzles & misc. Epoch-run evals**

- **Chess Puzzles (Epoch)** — Best-next-move identification from chess positions (in FEN notation), judged against the Stockfish engine — a lightweight spatial-reasoning/planning probe.
- **Mystery Game Puzzles (Epoch)** — Best-next-move identification in an undisclosed game's mid-game positions — the game's identity is kept secret specifically to block benchmark-specific preparation.
- **RLI** — The Remote Labor Index — whether AI agents can complete real, economically valuable freelance work (dev, design, architecture, data, video) to a professional-acceptance standard.
- **Blueprint Bench 2** — Whether an agent can construct an accurate 2D floor plan of an apartment from a set of interior photographs, scored against the true room layout.

## Benchmark catalog

### General knowledge / broad reasoning

| Benchmark | Data points | Date range | Score range | Status |
| --- | --- | --- | --- | --- |
| **MMLU** (`mmlu`) | 10 | 2023-03-01 → 2026-04-23 | 86.4–92.4 percent accuracy | likely saturated (near ceiling) |
| **MMLU-Pro** (`mmlu-pro`) | 12 | 2024-06-01 → 2026-08-01 | 56.2–91.59 percent accuracy | likely saturated (near ceiling) |
| **Big Bench Hard** (`big-bench-hard`) | 10 | 2022-10-01 → 2026-06-01 | 65.7–96.1 percent accuracy | likely saturated (near ceiling) |
| **Hellaswag** (`hellaswag`) | 5 | 2020-05-01 → 2024-09-01 | 78.9–95.4 percent accuracy | likely saturated (near ceiling) |
| **ARC (AI2 Reasoning Challenge)** (`arc`) | 7 | 2023-03-01 → 2024-12-26 | 94.5–98.9 percent accuracy | likely saturated (near ceiling) |
| **Truthfulqa** (`truthfulqa`) | 6 | 2023-03-01 → 2026-08-01 | 50.18–88 percent accuracy (MC) | still discriminating |
| **Winogrande** (`winogrande`) | 5 | 2023-03-01 → 2024-12-26 | 82.3–87.5 percent accuracy | still discriminating |
| **AGIEval** (`agieval`) | 6 | 2023-07-01 → 2026-08-01 | 22.8–94 percent accuracy | likely saturated (near ceiling) |
| **BoolQ** (`bool-q`) | 123 | 2019-11-05 → 2024-08-17 | 56.3–90.9 percent | likely saturated (near ceiling) |
| **PIQA** (`piqa`) | 112 | 2019-11-05 → 2024-12-26 | 65.8–88.7 percent | still discriminating |
| **LAMBADA** (`lambada`) | 53 | 2021-12-08 → 2023-11-30 | 54.3–87.15 percent | still discriminating |
| **Adversarial NLI** (`adversarial-nli`) | 15 | 2022-01-27 → 2024-04-23 | 33.9–58.1 percent | still discriminating |
| **CommonsenseQA 2.0** (`common-sense-qa-2`) | 3 | 2022-01-27 → 2023-07-18 | 50–57 percent | still discriminating |
| **SuperGLUE** (`superglue`) | 1 | 2022-01-27 → 2022-01-27 | 71.8–71.8 percent | still discriminating |
| **ScienceQA** (`science-qa`) | 26 | 2022-01-27 → 2024-08-16 | 36.19–91.3 percent | likely saturated (near ceiling) |

### Elite reasoning & math

| Benchmark | Data points | Date range | Score range | Status |
| --- | --- | --- | --- | --- |
| **GPQA Diamond** (`gpqa-diamond`) | 271 | 2023-03-14 → 2026-08-13 | 13.226–94.823 percent | likely saturated (near ceiling) |
| **Humanity's Last Exam** (`hle`) | 8 | 2025-01-01 → 2026-08-11 | 2.7–54.9 percent accuracy | still discriminating |
| **SimpleQA** (`simpleqa`) | 7 | 2024-10-30 → 2026-07-31 | 15–62.5 percent correct | still discriminating |
| **SimpleQA Verified** (`simpleqa-verified`) | 85 | 2024-10-22 → 2026-08-13 | 5.9–77.3 percent | still discriminating |
| **GSM8K** (`gsm8k`) | 6 | 2021-11-01 → 2026-03-01 | 55–99.7 percent accuracy | likely saturated (near ceiling) |
| **Math** (`math`) | 114 | 2022-01-01 → 2025-10-15 | 3.285–98.131 percent | likely saturated (near ceiling) |
| **AIME** (`aime`) | 9 | 2024-09-12 → 2026-02-01 | 12–99.79 percent (AIME 2025 | likely saturated (near ceiling) |
| **FrontierMath** (`frontiermath`) | 176 | 2024-06-20 → 2026-05-28 | 0–89 percent | still discriminating |
| **MathVista** (`mathvista`) | 9 | 2023-10-01 → 2026-01-01 | 34.8–90.7 percent accuracy (testmini) | likely saturated (near ceiling) |
| **Omni-MATH** (`omni-math`) | 8 | 2024-10-11 → 2025-01-01 | 14.24–81.9 percent accuracy | still discriminating |
| **IMO (Intl. Mathematical Olympiad)** (`imo`) | 4 | 2024-07-01 → 2026-07-22 | 28–42 points out of 42 (perfect score) | still discriminating |
| **IOI (Intl. Olympiad in Informatics)** (`ioi`) | 3 | 2026-08-09 → 2026-08-09 | 72.25–91.67 percent score (aggregator's IOI scoring methodology) | likely saturated (near ceiling) |
| **OTIS Mock AIME** (`otis-mock-aime-2024-2025`) | 238 | 2023-03-14 → 2026-08-13 | 0–100 percent | likely saturated (near ceiling) |

### Code & software engineering

| Benchmark | Data points | Date range | Score range | Status |
| --- | --- | --- | --- | --- |
| **HumanEval** (`humaneval`) | 12 | 2021-07-14 → 2026-08-08 | 28.8–97.6 pass@1 % | likely saturated (near ceiling) |
| **MBPP** (`mbpp`) | 14 | 2024-09-19 → 2026-08-07 | 66.9–92.7 pass@1 % (MBPP+) | likely saturated (near ceiling) |
| **SWE-bench Verified** (`swe-bench-verified`) | 54 | 2024-08-13 → 2026-06-16 | 30.992–83.471 percent | still discriminating |
| **SWE-bench Lite** (`swe-bench-lite`) | 1 | 2026-08-07 → 2026-08-07 | 62.7–62.7 % resolved | still discriminating |
| **SWE-bench Multimodal** (`swe-bench-multimodal`) | 1 | 2026-08-01 → 2026-08-01 | 59–59 % resolved | still discriminating |
| **SWE-bench Pro** (`swe-bench-pro`) | 6 | 2025-09-19 → 2026-08-01 | 23–80 % resolved | still discriminating |
| **LiveCodeBench** (`livecodebench`) | 9 | 2026-06-05 → 2026-08-12 | 3.3–91.7 pass@1 % | likely saturated (near ceiling) |
| **LiveCodeBench Pro (Elo)** (`livecodebench-elo`) | 3 | 2026-02-01 → 2026-02-01 | 2316–2887 Elo (LiveCodeBench Pro) | still discriminating |
| **Codeforces (Elo)** (`codeforces-elo`) | 16 | 2022-11-01 → 2026-02-12 | 0–3455 Codeforces Elo | still discriminating |
| **Aider Polyglot** (`aider-polyglot`) | 24 | 2024-12-21 → 2025-10-03 | 28–88 % correct (2nd attempt) | still discriminating |
| **SciCode** (`scicode`) | 135 | 2024-07-18 → 2026-07-31 | 1.5–60.2 percent | still discriminating |
| **MirrorCode** (`mirrorcode`) | 6 | 2026-02-19 → 2026-07-09 | 8.889–63.889 percent | still discriminating |
| **AlgoTune** (`algotune`) | 18 | 2025-01-20 → 2026-03-05 | 1.31–2.05 raw | still discriminating |
| **CursorBench** (`cursorbench`) | 31 | 2026-01-27 → 2026-07-24 | 31.9–72.9 percent | still discriminating |

### Agentic, tool-use & computer-use

| Benchmark | Data points | Date range | Score range | Status |
| --- | --- | --- | --- | --- |
| **GAIA** (`gaia`) | 14 | 2023-11-21 → 2025-09-01 | 15–75 % accuracy | still discriminating |
| **WebArena** (`webarena`) | 2 | 2023-07-26 → 2025-01-23 | 14.41–58.1 % success rate | still discriminating |
| **AgentBench** (`agentbench`) | 7 | 2023-08-07 → 2023-08-07 | 0.78–4.01 overall score (0-8 scale; avg across 8 environments) | still discriminating |
| **tau-bench** (`tau-bench`) | 11 | 2024-06-01 → 2025-08-01 | 36–69.2 pass^1 % (airline domain) | still discriminating |
| **OSWorld** (`osworld`) | 41 | 2024-05-30 → 2026-08-01 | 4.4–90.19 % success rate (OSWorld-Verified, best step-budget run) | likely saturated (near ceiling) |
| **AndroidWorld** (`androidworld`) | 14 | 2024-05-23 → 2025-10-14 | 3.4–97.4 % success rate pass@1 (AndroidWorld community leaderboard) | likely saturated (near ceiling) |
| **BrowseComp** (`browsecomp`) | 10 | 2024-08-06 → 2026-07-09 | 0.6–92.2 % accuracy | likely saturated (near ceiling) |
| **Vending-Bench** (`vending-bench`) | 54 | 2025-06-17 → 2026-07-24 | -31.184–11181.9 raw | still discriminating |
| **GDPval (real-world expert tasks)** (`gdpval`) | 8 | 2024-06-01 → 2026-04-23 | 12.4–84.9 % GDPval score (OpenAI-reported, launch comparison) | still discriminating |
| **GDPval (Elo, Artificial Analysis)** (`gdpval-elo`) | 4 | 2026-07-01 → 2026-08-01 | 1725–1849 Elo (Artificial Analysis GDPval-AA v2 leaderboard) | still discriminating |
| **Terminal Bench** (`terminal-bench`) | 10 | 2025-05-22 → 2026-05-14 | 43.2–84.7 % (Terminal-Bench 2.0) | still discriminating |

### Long-horizon autonomy, AI R&D & "AI researcher" / RSI signal

| Benchmark | Data points | Date range | Score range | Status |
| --- | --- | --- | --- | --- |
| **METR Time Horizon** (`metr-time-horizon`) | 26 | 2019-02-14 → 2026-04-07 | 0.054–1044.78 hours (human-expert-equivalent task time, 50% success rate) | still discriminating |
| **METR Cross-Domain Time Horizon** (`metr-cross-domain-time-horizon`) | 4 | 2025-07-14 → 2025-07-14 | 3–24 approx doubling time (months) of domain-specific time horizon ('~2 years') | still discriminating |
| **RE-Bench (METR)** (`re-bench`) | 4 | 2024-11-22 → 2024-11-22 | 0.46–4 normalized score (0=starting solution, 1=reference solution), 8-hour budget | still discriminating |
| **MLE-bench** (`mle-bench`) | 28 | 2024-10-08 → 2026-03-06 | 1.6–64.44 % (any-medal rate, MLE-bench 'All'/split75 comparable subset) | still discriminating |
| **Paperbench** (`paperbench`) | 12 | 2024-05-13 → 2025-04-07 | 2.6–43.4 % PaperBench replication score | still discriminating |
| **AI Scientist (Sakana et al.)** (`ai-scientist`) | 6 | 2025-02-20 → 2026-04-18 | 1–42 mean paper-quality score, 1-5 scale (LLM-judge synthesis of GPT-5.4/Gemini/Claude reviewers) | still discriminating |
| **OpenAI Self-Improvement Evals** (`openai-ai-self-improvement-evals`) | 8 | 2025-08-13 → 2025-08-13 | 1–45 % pass@1 (OpenAI-Proof Q&A) | still discriminating |

### Multimodal & vision

| Benchmark | Data points | Date range | Score range | Status |
| --- | --- | --- | --- | --- |
| **MMMU** (`mmmu`) | 79 | 2023-11-27 → 2026-07-01 | 32.6–88.6 % accuracy (MMMU-Pro, overall -- harder 10-option variant; used because this snapshot did not report a standard MMMU-validation score) | still discriminating |
| **MMBench** (`mmbench`) | 69 | 2023-12-23 → 2025-08-14 | 58–88.5 % accuracy (MMBench-EN v1.1, test split, overall) | still discriminating |
| **ChartQA** (`chartqa`) | 11 | 2024-03-04 → 2025-02-02 | 78.1–90.8 % relaxed accuracy (ChartQA test avg.) | likely saturated (near ceiling) |
| **DocVQA** (`docvqa`) | 11 | 2024-03-04 → 2025-02-02 | 87.2–96.4 ANLS score (DocVQA test) | likely saturated (near ceiling) |

### ARC-AGI family (interactive/abstraction reasoning)

| Benchmark | Data points | Date range | Score range | Status |
| --- | --- | --- | --- | --- |
| **ARC-AGI-1** (`arc-agi-1`) | 268 | 2019-11-05 → 2026-08-11 | 0–98.5 % correct (semi-private eval set) | likely saturated (near ceiling) |
| **ARC-AGI-2** (`arc-agi-2`) | 255 | 2023-11-03 → 2026-08-11 | 0–100 % correct (semi-private eval set) | likely saturated (near ceiling) |
| **ARC-AGI-3** (`arc-agi-3`) | 36 | 2025-12-17 → 2026-08-11 | 0.01–100 % of public demo set solved (official ARC-AGI-3 leaderboard, bare model + minimal harness) | likely saturated (near ceiling) |

### Games, puzzles & misc. Epoch-run evals

| Benchmark | Data points | Date range | Score range | Status |
| --- | --- | --- | --- | --- |
| **Chess Puzzles (Epoch)** (`chess-puzzles`) | 161 | 2023-06-13 → 2026-08-13 | 0–64 percent | still discriminating |
| **Mystery Game Puzzles (Epoch)** (`mystery-game-puzzles`) | 53 | 2025-08-05 → 2026-08-13 | 6–59 percent | still discriminating |
| **RLI** (`rli`) | 12 | 2025-06-05 → 2026-06-09 | 0.83–16.1 percent | still discriminating |
| **Blueprint Bench 2** (`blueprint-bench-2`) | 21 | 2025-10-15 → 2026-07-24 | 0–38.612 percent | still discriminating |

### Other Epoch-hub benchmarks not yet slotted into a category above

| Benchmark | Data points | Date range |
| --- | --- | --- |
| **Vending-Bench ($ balance)** (`vending-bench-dollars`) | 8 | 2025-02-20 → 2026-07-29 |
| **Vending-Bench (%)** (`vending-bench-percent`) | 3 | 2025-09-24 → 2026-04-17 |
| **Vending-Bench (survival time)** (`vending-bench-time`) | 1 | 2025-02-20 → 2025-02-20 |

## Leaderboard aggregators (where to track all of this going forward)

See `notes/aggregators.md` for the full writeup. Summary:

- **Epoch AI Benchmarking Hub** — https://epoch.ai/benchmarks — best bulk data source found; 76-benchmark CC-BY export used throughout this project.
- **Artificial Analysis** — https://artificialanalysis.ai/ — 600+ models, 23+ evals, composite "Intelligence Index"; gated API.
- **LMArena** (formerly LMSYS Chatbot Arena) — https://lmarena.ai/ — 1M+ blind human A/B battles, Elo ratings; bulk dataset on Hugging Face (`lmarena-ai/leaderboard-dataset`).
- **ARC Prize** — https://arcprize.org/leaderboard — official ARC-AGI-1/2/3 leaderboards, structured JSON backing available.
- **METR** — https://metr.org/time-horizons/ — the time-horizon/autonomy benchmark, raw YAML published.
- **Vellum LLM Leaderboard**, **LiveBench**, **llm-stats.com** — secondary aggregators, useful for cross-checking recent snapshots.
- **Papers With Code** — effectively shut down (July 2025); no longer a reliable current source, though old SOTA tables were useful for pre-2025 history.
- **Hugging Face Open LLM Leaderboard** — archived/retired June 2024, citing benchmark saturation and compute cost as reasons — itself a small data point for this talk's thesis.

## Most popular benchmarks — what labs and leaderboards actually cite

Recurring benchmarks that show up across OpenAI / Anthropic / Google DeepMind / xAI release posts and system cards through 2026, with example cited scores:

- **GPQA Diamond** — used by essentially every lab (Gemini 3 Pro: 91.9%; Gemini 3.1 Pro: 94.3%; Grok 4: 88%; part of GPT-5.5's eval suite).
- **SWE-bench Verified** (and increasingly **SWE-bench Pro**) — the headline agentic-coding number. Claude Opus 4.5 (Nov 2025) led with 80.9%, the first model over 80%; GPT-5.5 reported 58.6% on SWE-bench Pro.
- **ARC-AGI (v1 and v2)** — used as a "genuine reasoning, not memorization" flex. Grok 4: 66.6% (v1), 15.9% (v2); Claude Opus 4.5: 37.6% (v2); Gemini 3 Pro: 31.1% (v2); Gemini 3.1 Pro: 77.1% (v2) — the fastest visible jump of any benchmark in this whole project.
- **Humanity's Last Exam** — cited by xAI (Grok 4 Heavy: 44.4%) and one of the 9 components in Artificial Analysis's Intelligence Index.
- **AIME** (current-year math competition) — Gemini 3 Pro: 95% on AIME 2025; near-ceiling performance across frontier models is itself a plateau/saturation signal.
- **Terminal-Bench** — Claude Opus 4.5: 59.3% vs. Gemini 3 Pro 54.2% vs. GPT-5.1 47.6%.
- **LMArena / Chatbot Arena Elo** — the human-preference cross-check every lab now cites alongside static benchmarks (Gemini 3 Pro: "tops LMArena at 1501 Elo"; by Aug 2026, Claude Opus 4.7/4.8 and Gemini 3.1 Pro sit above the historic 1500 barrier).
- **Agentic/tool-use benchmarks** are the newest recurring category (Gemini 3.1 Pro: BrowseComp 85.9%, τ2-bench Telecom 99.3%, MCP Atlas 69.2%) — reflects the 2025-2026 shift from static Q&A toward long-horizon agent evaluation.

**Pattern:** every major release leans on roughly the same 5-7 benchmark handful (GPQA Diamond, SWE-bench, ARC-AGI, HLE, AIME, Terminal-Bench/agentic evals, LMArena Elo) rather than one fixed universal suite — labs pick whichever subset makes their model look best, and the specific agentic/tool-use benchmarks used change release to release as older ones saturate. Labs introducing new evals (ARC-AGI-2 after v1 saturated, Terminal-Bench/agentic benchmarks as coding benchmarks saturate) is itself indirect evidence for the "plateau vs. moved goalposts" question this project is trying to answer.

## Known data-quality caveats

- Score units are NOT always comparable within what looks like "one benchmark" — e.g. "LiveCodeBench" pass@1 % vs. "LiveCodeBench Pro" Elo, or GDPval's OpenAI-reported % win-rate vs. Artificial Analysis's GDPval-AA Elo re-scoring — these were split into separate series (`*-elo` suffix) rather than plotted together.
- Some rows come from secondary aggregators rather than primary lab publications where primary sources didn't publish a clean historical table; flagged per-row in each CSV's `notes` column.
- A few benchmarks (SWE-bench Lite/Multimodal, WebArena, AgentBench) have very few real data points because frontier labs largely stopped reporting them in favor of newer benchmarks — that sparsity is itself a finding, not a research gap.
- "Likely saturated" in the tables above is a simple heuristic (top score ≥ 90% on a percent-scale benchmark) — see each benchmark's row/notes file for the actual nuance.
