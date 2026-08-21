# AI Benchmark Landscape — Data Catalog

Research pass for the "AI Benchmarks" slide: as comprehensive an inventory as we could pull together of AI/LLM benchmarks and leaderboards, plus real (date, model, score) historical data for each, sourced from official leaderboards, papers, model release announcements, and benchmark aggregators. Built to answer one question: **is AI benchmark progress plateauing, or does it just look that way because we keep retiring saturated benchmarks and replacing them with harder ones?**

**208 benchmarks/evals catalogued, 7630 total (date, model, score) data points.**

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
- **OpenBookQA** — Elementary science questions answerable by combining a small set of provided core facts with commonsense reasoning.
- **Trivia Qa** — Open-domain trivia question answering with distantly-supervised evidence documents.

**General-purpose & human-preference leaderboards**

- **LiveBench** — General-purpose benchmark with new questions released monthly from fresh sources (recent papers, news, forum posts), objectively scored with no LLM judge — explicitly designed to resist contamination.
- **LMArena Elo** — Human-preference Elo from blind pairwise model battles ("overall" category — this pull doesn't include the style-controlled variant, which filters out the verbosity/formatting bias).

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
- **CritPT** — Graduate/research-level critical-thinking physics problems tracked on Epoch AI's benchmarking hub.

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
- **Gso** — An Epoch-hub-tracked software/systems engineering benchmark (bulk-imported; no dedicated deep-dive in this research pass).
- **Frontiercode** — An Epoch-hub-tracked frontier coding benchmark (bulk-imported; no dedicated deep-dive in this research pass).
- **Webdev Arena** — Head-to-head human-preference voting on AI-generated web app/website builds, arena-style.
- **Deepswe** — An Epoch-hub-tracked deep software-engineering-agent benchmark (bulk-imported; no dedicated deep-dive in this research pass).
- **Ale Bench** — An Epoch-hub-tracked algorithmic-engineering benchmark (bulk-imported; no dedicated deep-dive in this research pass).

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
- **TheAgentCompany** — An Epoch-hub-tracked simulated-workplace agent benchmark (bulk-imported; no dedicated deep-dive in this research pass).
- **Terminal Bench** — Agent competence in real shell/terminal environments on long-horizon, multi-step tasks including recovery from failed tool calls.
- **Cybench** — Offensive-security capture-the-flag-style cybersecurity challenges used to benchmark agentic exploitation capability.
- **ExploitBench** — Real-world software vulnerability exploitation tasks used to benchmark agentic offensive-security capability.
- **APEX Agents** — An Epoch-hub-tracked general agentic-capability benchmark (bulk-imported; no dedicated deep-dive in this research pass).
- **DeepResearch Bench** — Evaluates AI "deep research" agents on producing well-sourced, comprehensive research reports from open-ended questions.

**Long-horizon autonomy, AI R&D & "AI researcher" / RSI signal**

- **METR Time Horizon** — The length of task (in human-expert-equivalent hours) a model can complete autonomously with 50% success — METR's flagship autonomy-duration metric.
- **METR Cross-Domain Time Horizon** — Re-derives the time-horizon doubling trend across ~9 other domains (math, science QA, coding, computer use, self-driving) to test whether it generalizes beyond software.
- **RE-Bench (METR)** — Head-to-head AI-agent-vs.-human-expert performance on 7 open-ended ML research-engineering tasks under matched time budgets.
- **MLE-bench** — Real end-to-end ML engineering on 75 curated Kaggle competitions, scored by "any-medal rate" against the competition's actual leaderboard.
- **Paperbench** — Whether an agent can replicate a real ICML Spotlight/Oral paper from scratch — understand it, write the code, run the experiments — against an author-reviewed rubric.
- **AI Scientist (Sakana et al.)** — Fully autonomous research pipelines (hypothesize → experiment → write a paper), quality-scored by LLM-judge panels, not human peer review.
- **OpenAI Self-Improvement Evals** — Can a model replicate real internal OpenAI engineering pull requests, or diagnose real unsolved internal research bottlenecks — a direct proxy for "can it do an AI researcher's job."
- **PostTrainBench** — An Epoch-hub-tracked post-training-capability benchmark (bulk-imported; no dedicated deep-dive in this research pass).

**Multimodal & vision**

- **MMMU** — College-exam-level multimodal reasoning across 30 academic subjects, using real exam figures/diagrams that require expert subject knowledge to interpret.
- **MMBench** — Fine-grained multimodal ability across 20 categories, using a circular-evaluation protocol (answer choices rotated) to reduce lucky guessing.
- **ChartQA** — Question answering over bar/line/pie charts, requiring both visual reading and arithmetic reasoning over the chart's data.
- **DocVQA** — Question answering over scanned/photographed document images (forms, reports, invoices), requiring layout- and text-aware reading, not just OCR.
- **Video-MME** — Multimodal understanding of video content across a wide range of durations and domains.
- **SpatialViz-Bench** — Spatial-visualization reasoning from visual input.
- **MindCube** — 3D/spatial reasoning about objects and their relationships from visual input.
- **GeoBench** — Geography/geolocation reasoning from visual and/or textual clues.

**ARC-AGI family (interactive/abstraction reasoning)**

- **ARC-AGI-1** — Novel visual-abstraction grid puzzles — infer a transformation rule from a few demonstration pairs and apply it to a held-out test grid, with almost no reliance on world knowledge.
- **ARC-AGI-2** — A harder ARC-AGI successor, curated specifically to defeat brute-force search solvers that had started clearing v1 without genuinely generalizing.
- **ARC-AGI-3** — Small interactive video-game-like environments an agent must explore, form a hypothesis about, and act in over multiple steps — a shift from static puzzles to interactive/embodied reasoning.

**Games, puzzles & misc. Epoch-run evals**

- **Chess Puzzles (Epoch)** — Best-next-move identification from chess positions (in FEN notation), judged against the Stockfish engine — a lightweight spatial-reasoning/planning probe.
- **Mystery Game Puzzles (Epoch)** — Best-next-move identification in an undisclosed game's mid-game positions — the game's identity is kept secret specifically to block benchmark-specific preparation.
- **Balrog** — Text-based game-playing across six environments of increasing difficulty, from simple grid tasks to complex dungeon exploration (NetHack).
- **Surface Evolver Bench** — An Epoch-hub-tracked scientific-simulation benchmark (bulk-imported; no dedicated deep-dive in this research pass).
- **Weirdml** — An Epoch-hub-tracked unconventional machine-learning-reasoning benchmark (bulk-imported; no dedicated deep-dive in this research pass).
- **Forecastbench** — Whether a model can forecast the outcome of real, currently-unresolved future events as accurately as human forecasters.
- **Fictionlivebench** — Long-context comprehension and consistency-tracking within long fictional narratives.
- **Lech Mazur Writing** — Creative-writing quality, judged head-to-head via an LLM-judge tournament (Lech Mazur's ongoing creative-writing benchmark).
- **Simplebench** — A small set of everyday-reasoning questions that are simple for humans but that language models tend to get wrong.
- **RLI** — The Remote Labor Index — whether AI agents can complete real, economically valuable freelance work (dev, design, architecture, data, video) to a professional-acceptance standard.
- **Cl Bench** — An Epoch-hub-tracked "continual learning"-flavored benchmark (bulk-imported; no dedicated deep-dive in this research pass).
- **Cl Bench Life** — A "life"/everyday-tasks variant of CL-Bench (bulk-imported; no dedicated deep-dive in this research pass).
- **Blueprint Bench 2** — Whether an agent can construct an accurate 2D floor plan of an apartment from a set of interior photographs, scored against the true room layout.
- **Vpct** — An Epoch-hub-tracked visual/perceptual-consistency-testing benchmark (bulk-imported; no dedicated deep-dive in this research pass).
- **Enigma Eval** — Puzzle-solving across a range of enigma-style logic/lateral-thinking challenges.
- **Cad Eval** — Whether a model can produce correct computer-aided-design (CAD) outputs from a specification.
- **Btf3** — An Epoch-hub-tracked benchmark (bulk-imported; no dedicated deep-dive in this research pass).
- **Proofbench** — Formal or informal mathematical proof-writing/verification tasks.
- **Gbaeval** — An Epoch-hub-tracked benchmark (bulk-imported; no dedicated deep-dive in this research pass).

**Web & computer-use agents**

- **WorkArena / WorkArena++** — Enterprise browser work inside a real ServiceNow instance; WorkArena++ adds 682 compositional planning tasks.
- **VisualWebArena** — 910 tasks on realistic sites requiring visual/spatial page understanding, not just DOM/text.
- **Online-Mind2Web** — Live re-evaluation of 300 tasks on 136 real high-traffic sites; found agents underperform 2024 baselines ("illusion of progress").
- **WebVoyager** — End-to-end multimodal web agent benchmark; ~643 real-world tasks across 15 real sites, GPT-4V + human-judge evaluation.
- **WebBench** — Large live-web READ/WRITE benchmark spanning hundreds of sites, including auth, downloads, and state-changing actions.
- **AssistantBench** — Long, realistic live-web research/assistant tasks requiring planning, retrieval, and synthesis.
- **Windows Agent Arena** — Windows-specific multimodal desktop control across real applications.
- **AppWorld (+ AppWorld-UL)** — 750 executable tasks across 9 simulated everyday apps / 457 APIs, graded from resulting application state, not an LLM judge; AppWorld-UL adds user-in-the-loop clarification/confirmation.
- **Mind2Web** — Foundational large-scale generalist web-agent dataset: 137 real websites, 2,000+ tasks, element identification and action prediction.
- **MiniWoB++** — 100+ simulated-browser micro-tasks; the foundational web-interaction benchmark (2017/2018), still widely cited.
- **AssistGUI** — Desktop GUI automation (Windows) across productivity software (After Effects, MS Word) via screenshots.
- **SPA-Bench** — Smartphone-agent benchmark, 340 tasks / 66 apps, English+Chinese, cross-app tasks. ICLR'25 Spotlight.

**Tool-use & function-calling**

- **Berkeley Function-Calling Leaderboard (BFCL v1-v4)** — The standard tool/function-calling eval: single-turn, multi-turn, parallel and nested calls across Python/Java/JS/SQL/REST; v4 adds agentic eval.
- **tau2-bench (Telecom)** — Sierra's dual-control (agent + simulated user, both can act on a shared environment) successor to tau-bench; 2,285 compositional tasks.
- **MCP-Atlas** — Scale AI: 1,000 tasks across 36 real MCP servers / 220 tools, tests tool discovery + multi-server workflows.
- **ToolBench / ToolEval** — 16,000+ real APIs, instruction-following tool-use benchmark; ICLR 2024 Spotlight.
- **MINT-Bench** — Multi-turn interactive tool use with feedback over multiple rounds.
- **CRMArena / CRMArena-Pro** — Enterprise CRM work benchmark: business-process knowledge, confidentiality handling, multi-turn interactions.

**Games & interactive environments**

- **Kaggle Game Arena** — Google DeepMind + Kaggle live head-to-head leaderboard: frontier models play full adversarial Chess, Werewolf, and Poker against each other.
- **lmgame-Bench** — Modular Gym-style harness across 6 real video games (Mario, Sokoban, Tetris, 2048, Candy Crush, Ace Attorney), isolating perception/memory/reasoning. ICLR 2026.
- **VideoGameBench** — VLM benchmark on real Game Boy (via PyBoy) and MS-DOS games -- live perception+control on actual retro binaries.
- **Werewolf Arena** — Social-deduction (Werewolf/Mafia) benchmark for deception, persuasion, theory of mind, coalition reasoning.
- **DSGBench** — Multi-game "diverse strategic game" suite bundling several strategy games under one harness.
- **GameBench** — Strategic-reasoning eval across multiple novel/unseen games chosen to avoid training-data contamination (Codenames, Coup, Sea Battle, SpyFall, etc.).
- **GAMEBoT** — Direct competition across 8 games exposing planning/reasoning behavior via modular sub-problems; 17 LLMs benchmarked with CoT.
- **GAMA-Bench** — Multi-agent strategic/social/economic games -- auction, bargaining, battle, and others.
- **LLM-Hanabi** — Cooperative card-game (Hanabi) benchmark testing theory-of-mind and collaborative rationale inference among multiple LLM agents. EMNLP 2025.
- **ORAK** — Diverse video-game benchmark designed specifically for LLM agents, configurable games/observations/agent modules.
- **GameDevBench** — 333 agentic game-development tasks combining codebase work with shaders, sprites, animation, and visual scene validation.
- **Roblox Open Game Eval** — Executable game-development and debugging tasks with a maintained multi-model leaderboard.
- **Classic RL suites (Atari/ALE, Procgen, NetHack LE, MineRL/MineDojo, Crafter, GVGAI, DMLab-30, Habitat, BabyAI, TextWorld, Jericho, ScienceWorld)** — The canonical deep-RL benchmark suites predating the LLM-agent era.
- **Kaggle Game Arena (Chess Elo)** — The chess-specific Elo-rating slice of Kaggle Game Arena's live head-to-head leaderboard, split out from its cross-game score family.

**Safety, alignment & red-teaming**

- **WMDP (Weapons of Mass Destruction Proxy)** — 3,668 MCQ proxy for hazardous bio/cyber/chem knowledge; built as both a hazard eval and an unlearning benchmark by CAIS + UC Berkeley/MIT.
- **HarmBench** — Standardized red-teaming benchmark: 400 harmful behaviors x 7 categories, Attack Success Rate metric, 18-method attack panel.
- **JailbreakBench** — Maintained leaderboard + JBB-Behaviors dataset (100 behaviors), tracks Attack Success Rate for attacks and defenses over time.
- **AgentHarm** — Extends harm evaluation to tool-using agents: 110 unique / 330 augmented multi-step agentic harm behaviors across 11 categories, 104 tools. ICLR 2025.
- **AgentDojo** — Tests agent robustness to prompt injection and unsafe tool use in realistic agentic settings.
- **MASK** — Disentangles honesty from factual accuracy -- tests whether models contradict their own stated beliefs under pressure to lie. Frontier models score 20-60% lie rate despite high TruthfulQA scores.
- **RealToxicityPrompts** — Naturally-occurring prompts probing toxic completion tendencies.
- **HaluEval / HaluEval 2.0** — Hallucination evaluation across QA/dialogue/summarization, quantifying frequency and trigger types; 2.0 extends to biomedicine/finance/science.
- **FActScore** — Fine-grained atomic factuality evaluation: decomposes generated text into atomic facts and checks each against a knowledge source.
- **Vectara Hallucination Leaderboard** — Ranks LLMs by hallucination/faithfulness rate in RAG/summarization settings, LLM-judge scored; the "HHEM" the Reddit list specifically asked about.

**Instruction-following & chat quality**

- **IFEval** — ~500 prompts with verifiable, auto-checkable constraints (word counts, keyword inclusion, format rules); part of HF Open LLM Leaderboard v2.
- **IFBench** — Harder, contamination-resistant IFEval successor, tracked live on Artificial Analysis.
- **FollowBench** — Multi-level constraint-following (Content/Situation/Style/Format/Example), incrementally stacking constraints to find the failure point.
- **MT-Bench** — Multi-turn conversational benchmark across 8 domains, judged by GPT-4 on a 1-10 scale; the foundational "LLM-as-judge" framework.
- **AlpacaEval 2.0** — Win-rate evaluation vs. a reference model (GPT-4), length-controlled to reduce verbosity bias.
- **WildBench** — Challenging, diverse "in the wild" real user queries, LLM-as-judge; designed to be harder than MT-Bench with less contamination.
- **MultiChallenge** — Multi-turn conversation: instruction retention, inference memory, versioned editing, self-coherence. Cited by Gemini 3 Pro / GPT-5.1 releases.

**Long-context & memory**

- **RULER** — 13 synthetic tasks (multi-needle retrieval, variable tracing, multi-hop QA) up to 128K+ tokens, built to expose the gap between claimed and effective context length.
- **LongBench / LongBench v2** — Bilingual (Chinese/English) long-context benchmark; v2 spans 8K-2M words with real-world multitask reasoning, not synthetic retrieval.
- **InfiniteBench** — Additional synthetic long-context suite, actively maintained alongside LongBench v2/NIAH.
- **BABILong** — Long-context reasoning built on the classic bAbI tasks, extended to very long documents.
- **SCROLLS** — 7-dataset long-document suite (QASPER, QUALITY, GovReport, SummScreenFD, NarrativeQA, QMSum, ContractNLI).
- **MRCR v2 (Multi-Round Context Retrieval)** — Anthropic-aligned long-context/memory eval.

**Multilingual**

- **Belebele** — 122-language reading comprehension on FLORES-200 passages (Meta).
- **MGSM (Multilingual GSM8K)** — GSM8K extended into 10 languages including low-resource ones; explicitly named in the user's Reddit list as a "dead" benchmark for English but still used for multilingual comparison.
- **IndicGenBench / IndicMMLU** — 22 officially-recognized Indian languages, generative + MMLU-style QA tasks.
- **MMLU-ProX** — Multilingual extension of MMLU-Pro across 13-29 languages, expert-post-edited machine translation.

**Domain-professional (medicine, law, finance)**

- **HealthBench** — 5,000 realistic clinician-conversation scenarios, 48,562 physician-written rubric criteria -- OpenAI's own eval.
- **MedXpertQA** — 4,460 expert-level questions across 17 medical specialties, text + multimodal; built because MedQA saturated.
- **MedQA / MedQA-USMLE** — USMLE-style multiple-choice medical exam questions; historically the GPT-4/Gemini medical headline benchmark, now widely regarded as saturated.
- **MedMCQA** — 194K MC questions from Indian medical entrance exams (AIIMS/NEET-PG) across 21 subjects.
- **PubMedQA** — Biomedical research QA requiring yes/no/maybe answers from PubMed abstracts.
- **LegalBench (via Vals AI)** — 162 crowd-built legal-reasoning tasks (issue-spotting, rule-recall, rule-application); nearly saturated at frontier (88%+) by 2026.
- **CaseHOLD** — 53,000+ MC questions identifying legal holdings from real US case law; part of the LegalBench suite.
- **FinBen** — Holistic financial-LLM benchmark, 8-axis taxonomy. NeurIPS 2024 Datasets & Benchmarks track.
- **FinanceBench (+ DocFinQA)** — 10,000+ financial QA questions from real US public-company filings; even GPT-4-Turbo misses 81%+ without retrieval. DocFinQA extends to full 10-K document context.

**Coding & data (extended)**

- **Spider 2.0** — 632 real enterprise text-to-SQL workflows (BigQuery/Snowflake/DuckDB/Postgres), active leaderboard. Caveat: a 2026 VLDB/CIDR paper found a 66.1% annotation-error rate in the Spider2-Snow subset.
- **BIRD-SQL** — 12,751 question/SQL pairs, 95 databases, 37 domains; standard cross-domain text-to-SQL benchmark, usually reported alongside Spider.
- **DS-1000** — 1,000 realistic data-science coding problems (NumPy/Pandas/SciPy/sklearn/PyTorch/TF/Matplotlib) from StackOverflow, deliberately perturbed to resist memorization.
- **BigCodeBench** — Diverse function-calls + complex multi-step instructions, harder/broader than HumanEval; active leaderboard.
- **EvalPlus / HumanEval+** — Rigor upgrade to HumanEval/MBPP via ~80x more test cases per problem to catch subtle bugs; also includes EvalPerf for code efficiency. NeurIPS 2023.
- **APPS** — 10,000 Python programming problems, introductory through competition level; one of the first large competitive-coding LLM benchmarks (2021).
- **SWE-Lancer** — Real freelance software-engineering tasks from Upwork ($1M total task value) -- tests whether models can do work professionals were actually paid for.

**Embedding & retrieval (different capability axis)**

- **MTEB (Massive Text Embedding Benchmark)** — 8 task types, 58 datasets, 112 languages -- the standard embedding-model benchmark; active HF leaderboard + "MTEB Arena."

**Multimodal (extended: image, video, audio)**

- **HEIM (Holistic Evaluation of Text-to-Image Models)** — 12-dimensional evaluation of text-to-image models (alignment, quality, aesthetics, bias, toxicity, fairness, robustness) across 29 models. Part of Stanford HELM.
- **GenAI-Bench** — 1,600+ compositional text-to-image/video prompts rated by 80k+ humans, introduces VQAScore metric.
- **RealWorldQA** — Real-world spatial understanding from photographs (xAI/Grok).
- **MME (Multimodal LLM Evaluation)** — Perception (OCR, object/scene recognition) + cognition (commonsense, arithmetic, translation) VLM eval, yes/no format.
- **SEED-Bench** — 19,000 MC questions for multimodal LLMs across 12 dimensions including image/video understanding.
- **AudioBench** — Universal audio-LLM benchmark: ASR, speech QA, instruction following, audio captioning, emotion/accent/gender recognition across 26 datasets. NAACL 2025.
- **AIR-Bench (Audio Instruct)** — Open-ended, instruction-following audio tasks across speech/sound/music/mixed audio; dynamic foundation-model-judged scoring.

**Reasoning, planning & social cognition**

- **PlanBench** — Classical PDDL-based planning benchmark (Blocksworld, Logistics domains); tests plan validity, cost optimization, replanning -- even o1-style reasoning models still struggle.
- **ToMBench** — Theory-of-Mind benchmark: 8 task types, 31 social-cognition abilities (false beliefs, deception, faux-pas, perspective-tracking), MCQ format. ACL 2024.
- **MuSR (Multistep Soft Reasoning)** — Algorithmically-generated tasks (murder mysteries, object placements, team allocations) requiring multi-step reasoning over 1000+ word contexts. Part of HF Open LLM Leaderboard v2.
- **StrategyQA** — Binary yes/no questions requiring multi-hop implicit world-knowledge reasoning.
- **CLUTRR** — Multi-hop relational reasoning from family-relation narrative stories.
- **HotpotQA** — Multi-hop reasoning QA requiring synthesis across multiple Wikipedia paragraphs.
- **DROP (Discrete Reasoning Over Paragraphs)** — Reading comprehension requiring numerical reasoning, counting, sorting over Wikipedia passages (96,000 questions).
- **NarrativeQA** — Reading comprehension over full books and movie scripts (DeepMind).

**Scientific-agent & AI-researcher (extends RSI cluster)**

- **AstaBench** — AI2's grounded scientific-research-agent benchmark: 4 categories (literature search, code, data analysis, end-to-end discovery). ICLR 2026 oral.
- **AIRS-Bench** — End-to-end AI research-science work by agents, official multi-agent leaderboard (Meta).
- **ScienceAgentBench** — 102 real-world data-driven scientific-discovery tasks across chemistry, biology, economics; tests end-to-end scientific workflows including code + experiment design.

**Embodied & robotics**

- **EmbodiedBench** — Multimodal-LLM-as-embodied-agent benchmark, 4 simulation environments incl. EB-ALFRED (manipulation), EB-Habitat (navigation). ICML 2025 Oral -- GPT-4o achieves only ~29% on low-level manipulation.
- **ALFWorld / ScienceWorld / Habitat-BEHAVIOR / RoboCasa / EMMOE** — A cluster of embodied/robotics simulation benchmarks for physical-world planning and manipulation.

**Multi-agent & social reasoning**

- **MultiAgentBench (MARBLE)** — Evaluates LLMs in cooperative (research writing, Minecraft building, coding) and competitive (negotiation, Werewolf) multi-agent scenarios with milestone-based KPIs. ACL 2025.

## Data provenance

Every data point in `aggregated.json` carries a `source` URL and an `extraction_method` tag; every benchmark carries a `source_files` list (the exact CSV path(s) on disk backing it) and a `provenance_summary` (point counts by extraction method). Methods are assigned mechanically from the source URL's domain (see `classify_extraction_method()` in `aggregate.py`), not asserted from memory, so re-running the script reproduces the same tags.

**7630 total data points, 0 with an empty source** (breakdown by extraction method):

| Extraction method | Points | What it means |
| --- | --- | --- |
| `epoch_bulk_csv_no_row_source_used_hub_fallback` | 2842 | Row came from Epoch AI's bulk CSV export with no per-row source link in Epoch's own schema; falls back to that benchmark's general epoch.ai/benchmarks page (verified to resolve) rather than being left blank. |
| `arxiv_or_academic_paper` | 1811 | URL is arXiv/ACL/OpenReview/NeurIPS-proceedings — a paper's own results table. |
| `other_web_source` | 1112 | URL didn't match a known domain pattern above; still a real, cited source, just uncategorized. |
| `official_benchmark_leaderboard_or_site` | 646 | URL is the benchmark's own official leaderboard/project site (arcprize.org, swebench.com, metr.org, etc.). |
| `huggingface_dataset_or_space` | 520 | URL is a Hugging Face dataset or Space. |
| `third_party_aggregator` | 289 | URL is a secondary aggregator (llm-stats.com, Artificial Analysis, Vals AI, etc.) — lower confidence than a primary source, flagged per-row. |
| `primary_lab_source` | 220 | URL is a frontier lab's own blog post, model card, or system card (OpenAI/Anthropic/Google/xAI/Meta). |
| `github_repo` | 190 | URL is a GitHub repo/README — usually a maintained leaderboard table in the benchmark's own code repo. |

**Known fix in this pass:** an earlier version of `aggregate.py` left 1,432 of 2,913 points (49.2%) with an empty `source` field, because 10 of Epoch AI's 76 benchmark CSVs use a different column schema (`Log viewer`/`Logs` instead of `Source`/`Source link`) that the merge script didn't check, and those log-viewer/logs cells are empty for every row in those files anyway. Fixed by falling back to the benchmark's own epoch.ai hub page (a real, verified URL) for any row with no per-row source, tagged distinctly (`epoch_bulk_csv_no_row_source_used_hub_fallback`) so it's never confused with a genuine per-row citation.

## Benchmark catalog

### General knowledge / broad reasoning

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **MMLU** (`mmlu`) | 225 | 2021-08-05 → 2026-04-23 | 23.9–92.4 percent accuracy | likely saturated (near ceiling) | `data/aggregator-epoch-benchmarking-hub/mmlu_external.csv`<br>`data/mmlu.csv` |
| **MMLU-Pro** (`mmlu-pro`) | 12 | 2024-06-01 → 2026-08-01 | 56.2–91.59 percent accuracy | likely saturated (near ceiling) | `data/mmlu-pro.csv` |
| **Big Bench Hard** (`big-bench-hard`) | 98 | 2022-10-01 → 2026-06-01 | 28–96.1 percent accuracy | likely saturated (near ceiling) | `data/aggregator-epoch-benchmarking-hub/bbh_external.csv`<br>`data/big-bench-hard.csv` |
| **Hellaswag** (`hellaswag`) | 112 | 2019-11-05 → 2024-12-26 | 40–95.4 percent | likely saturated (near ceiling) | `data/aggregator-epoch-benchmarking-hub/hella_swag_external.csv`<br>`data/hellaswag.csv` |
| **ARC (AI2 Reasoning Challenge)** (`arc`) | 140 | 2019-11-05 → 2024-12-26 | 23.2–98.9 percent | likely saturated (near ceiling) | `data/aggregator-epoch-benchmarking-hub/arc_ai2_external.csv`<br>`data/arc.csv` |
| **Truthfulqa** (`truthfulqa`) | 6 | 2023-03-01 → 2026-08-01 | 50.18–88 percent accuracy (MC) | still discriminating | `data/truthfulqa.csv` |
| **Winogrande** (`winogrande`) | 142 | 2019-11-05 → 2024-12-26 | 51.5–89.2 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/wino_grande_external.csv`<br>`data/winogrande.csv` |
| **AGIEval** (`agieval`) | 6 | 2023-07-01 → 2026-08-01 | 22.8–94 percent accuracy | likely saturated (near ceiling) | `data/agieval.csv` |
| **BoolQ** (`bool-q`) | 123 | 2019-11-05 → 2024-08-17 | 56.3–90.9 percent | likely saturated (near ceiling) | `data/aggregator-epoch-benchmarking-hub/bool_q_external.csv` |
| **PIQA** (`piqa`) | 112 | 2019-11-05 → 2024-12-26 | 65.8–88.7 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/piqa_external.csv` |
| **LAMBADA** (`lambada`) | 53 | 2021-12-08 → 2023-11-30 | 54.3–87.15 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/lambada_external.csv` |
| **Adversarial NLI** (`adversarial-nli`) | 15 | 2022-01-27 → 2024-04-23 | 33.9–58.1 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/adversarial_nli_external.csv` |
| **CommonsenseQA 2.0** (`common-sense-qa-2`) | 3 | 2022-01-27 → 2023-07-18 | 50–57 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/common_sense_qa_2_external.csv` |
| **SuperGLUE** (`superglue`) | 1 | 2022-01-27 → 2022-01-27 | 71.8–71.8 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/superglue_external.csv` |
| **ScienceQA** (`science-qa`) | 26 | 2022-01-27 → 2024-08-16 | 36.19–91.3 percent | likely saturated (near ceiling) | `data/aggregator-epoch-benchmarking-hub/science_qa_external.csv` |
| **OpenBookQA** (`open-book-qa`) | 70 | 2019-11-05 → 2024-04-23 | 22.4–88 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/open_book_qa_external.csv` |
| **Trivia Qa** (`trivia-qa`) | 113 | 2021-12-08 → 2024-12-26 | 43.5–87.6 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/trivia_qa_external.csv` |

### General-purpose & human-preference leaderboards

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **LiveBench** (`live-bench`) | 52 | 2024-02-29 → 2025-11-13 | 22.08–82.35 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/live_bench_external.csv` |
| **LMArena Elo** (`lmarena-elo`) | 389 | 2026-08-12 → 2026-08-12 | 833.629–1507.79 Elo | still discriminating | `data/aggregator-lmarena-text-latest.csv` |

### Elite reasoning & math

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **GPQA Diamond** (`gpqa-diamond`) | 271 | 2023-03-14 → 2026-08-13 | 13.226–94.823 percent | likely saturated (near ceiling) | `data/aggregator-epoch-benchmarking-hub/gpqa_diamond.csv`<br>`data/gpqa-diamond.csv` |
| **Humanity's Last Exam** (`hle`) | 60 | 2024-09-24 → 2026-08-11 | 2.7–55.5 percent accuracy | still discriminating | `data/aggregator-epoch-benchmarking-hub/hle_external.csv`<br>`data/hle.csv` |
| **SimpleQA** (`simpleqa`) | 7 | 2024-10-30 → 2026-07-31 | 15–62.5 percent correct | still discriminating | `data/simpleqa.csv` |
| **SimpleQA Verified** (`simpleqa-verified`) | 85 | 2024-10-22 → 2026-08-13 | 5.9–77.3 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/simpleqa_verified.csv`<br>`data/simpleqa-verified.csv` |
| **GSM8K** (`gsm8k`) | 168 | 2020-06-22 → 2026-03-01 | 0.7–99.7 percent accuracy | likely saturated (near ceiling) | `data/aggregator-epoch-benchmarking-hub/gsm8k_external.csv`<br>`data/gsm8k.csv` |
| **Math** (`math`) | 115 | 2021-01-01 → 2025-10-15 | 3.285–98.131 percent | likely saturated (near ceiling) | `data/aggregator-epoch-benchmarking-hub/math_level_5.csv`<br>`data/math.csv` |
| **AIME** (`aime`) | 9 | 2024-09-12 → 2026-02-01 | 12–99.79 percent (AIME 2025, no tools) | likely saturated (near ceiling) | `data/aime.csv` |
| **FrontierMath** (`frontiermath`) | 177 | 2024-06-20 → 2026-05-28 | 0–89 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/frontiermath.csv`<br>`data/aggregator-epoch-benchmarking-hub/frontiermath_tier_4.csv`<br>`data/frontiermath.csv` |
| **MathVista** (`mathvista`) | 9 | 2023-10-01 → 2026-01-01 | 34.8–90.7 percent accuracy (testmini) | likely saturated (near ceiling) | `data/mathvista.csv` |
| **Omni-MATH** (`omni-math`) | 8 | 2024-10-11 → 2025-01-01 | 14.24–81.9 percent accuracy | still discriminating | `data/omni-math.csv` |
| **IMO (Intl. Mathematical Olympiad)** (`imo`) | 4 | 2024-07-01 → 2026-07-22 | 28–42 points out of 42 (perfect score) | still discriminating | `data/imo.csv` |
| **IOI (Intl. Olympiad in Informatics)** (`ioi`) | 5 | 2024-01-01 → 2026-08-09 | 49–98 percent score (aggregator's IOI scoring methodology) | likely saturated (near ceiling) | `data/ioi.csv` |
| **OTIS Mock AIME** (`otis-mock-aime-2024-2025`) | 238 | 2023-03-14 → 2026-08-13 | 0–100 percent | likely saturated (near ceiling) | `data/aggregator-epoch-benchmarking-hub/otis_mock_aime_2024_2025.csv` |
| **CritPT** (`critpt`) | 135 | 2024-07-23 → 2026-07-31 | 0–32.3 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/critpt_external.csv` |

### Code & software engineering

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **HumanEval** (`humaneval`) | 12 | 2021-07-14 → 2026-08-08 | 28.8–97.6 pass@1 % | likely saturated (near ceiling) | `data/humaneval.csv` |
| **MBPP** (`mbpp`) | 15 | 2024-07-23 → 2026-08-07 | 66.9–92.7 pass@1 % (MBPP+) | likely saturated (near ceiling) | `data/mbpp.csv` |
| **SWE-bench Verified** (`swe-bench-verified`) | 54 | 2024-08-13 → 2026-06-16 | 30.992–83.471 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/swe_bench_verified.csv`<br>`data/swe-bench-verified.csv` |
| **SWE-bench Lite** (`swe-bench-lite`) | 1 | 2026-08-07 → 2026-08-07 | 62.7–62.7 % resolved | still discriminating | `data/swe-bench-lite.csv` |
| **SWE-bench Multimodal** (`swe-bench-multimodal`) | 1 | 2026-08-01 → 2026-08-01 | 59–59 % resolved | still discriminating | `data/swe-bench-multimodal.csv` |
| **SWE-bench Pro** (`swe-bench-pro`) | 6 | 2025-09-19 → 2026-08-01 | 23–80 % resolved | still discriminating | `data/swe-bench-pro.csv` |
| **LiveCodeBench** (`livecodebench`) | 9 | 2026-06-05 → 2026-08-12 | 3.3–91.7 pass@1 % | likely saturated (near ceiling) | `data/livecodebench.csv` |
| **LiveCodeBench Pro (Elo)** (`livecodebench-elo`) | 3 | 2026-02-01 → 2026-02-01 | 2316–2887 Elo (LiveCodeBench Pro) | still discriminating | `data/livecodebench.csv` |
| **Codeforces (Elo)** (`codeforces-elo`) | 16 | 2022-11-01 → 2026-02-12 | 0–3455 Codeforces Elo | still discriminating | `data/codeforces-elo.csv` |
| **Aider Polyglot** (`aider-polyglot`) | 96 | 2024-03-26 → 2025-12-01 | 3.6–88 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/aider_polyglot_external.csv`<br>`data/aider-polyglot.csv` |
| **SciCode** (`scicode`) | 135 | 2024-07-18 → 2026-07-31 | 1.5–60.2 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/scicode_external.csv`<br>`data/scicode.csv` |
| **MirrorCode** (`mirrorcode`) | 6 | 2026-02-19 → 2026-07-09 | 8.889–63.889 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/mirrorcode.csv` |
| **AlgoTune** (`algotune`) | 18 | 2025-01-20 → 2026-03-05 | 1.31–2.05 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/algotune_external.csv` |
| **CursorBench** (`cursorbench`) | 31 | 2026-01-27 → 2026-07-24 | 31.9–72.9 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/cursorbench_external.csv` |
| **Gso** (`gso`) | 38 | 2024-10-22 → 2026-06-30 | 0–47.06 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/gso_external.csv` |
| **Frontiercode** (`frontiercode`) | 20 | 2026-04-07 → 2026-07-24 | 9.4–53.5 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/frontiercode_external.csv` |
| **Webdev Arena** (`webdev-arena`) | 98 | 2025-06-17 → 2026-07-24 | 1139–1711.88 Elo | still discriminating | `data/aggregator-epoch-benchmarking-hub/webdev_arena_external.csv` |
| **Deepswe** (`deepswe`) | 50 | 2026-02-17 → 2026-07-24 | 1.549–73.649 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/deepswe_external.csv` |
| **Ale Bench** (`ale-bench`) | 101 | 2024-12-03 → 2026-07-31 | 137.78–2176.88 raw | still discriminating | `data/aggregator-epoch-benchmarking-hub/ale_bench_external.csv` |

### Agentic, tool-use & computer-use

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **GAIA** (`gaia`) | 14 | 2023-11-21 → 2025-09-01 | 15–75 % accuracy | still discriminating | `data/gaia.csv` |
| **WebArena** (`webarena`) | 2 | 2023-07-26 → 2025-01-23 | 14.41–58.1 % success rate | still discriminating | `data/webarena.csv` |
| **AgentBench** (`agentbench`) | 7 | 2023-08-07 → 2023-08-07 | 0.78–4.01 overall score (0-8 scale; avg across 8 environments) | still discriminating | `data/agentbench.csv` |
| **tau-bench** (`tau-bench`) | 11 | 2024-06-01 → 2025-08-01 | 36–69.2 pass^1 % (airline domain) | still discriminating | `data/tau-bench.csv` |
| **OSWorld** (`osworld`) | 51 | 2024-05-30 → 2026-08-01 | 2.8–90.19 % success rate (OSWorld-Verified, best step-budget run) | likely saturated (near ceiling) | `data/aggregator-epoch-benchmarking-hub/os_world_external.csv`<br>`data/aggregator-epoch-benchmarking-hub/osworld_2_external.csv`<br>`data/osworld.csv` |
| **AndroidWorld** (`androidworld`) | 14 | 2024-05-23 → 2025-10-14 | 3.4–97.4 % success rate pass@1 (AndroidWorld community leaderboard) | likely saturated (near ceiling) | `data/androidworld.csv` |
| **BrowseComp** (`browsecomp`) | 10 | 2024-08-06 → 2026-07-09 | 0.6–92.2 % accuracy | likely saturated (near ceiling) | `data/browsecomp.csv` |
| **Vending-Bench** (`vending-bench`) | 54 | 2025-06-17 → 2026-07-24 | -31.184–11181.9 raw | still discriminating | `data/aggregator-epoch-benchmarking-hub/vending_bench_2_external.csv` |
| **GDPval (real-world expert tasks)** (`gdpval`) | 40 | 2024-06-01 → 2026-07-24 | 8–84.9 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/gdp_pdf_external.csv`<br>`data/aggregator-epoch-benchmarking-hub/gdpval_external.csv`<br>`data/gdpval.csv` |
| **GDPval (Elo, Artificial Analysis)** (`gdpval-elo`) | 4 | 2026-07-01 → 2026-08-01 | 1725–1849 Elo (Artificial Analysis GDPval-AA v2 leaderboard) | still discriminating | `data/gdpval.csv` |
| **TheAgentCompany** (`the-agent-company`) | 16 | 2024-06-07 → 2025-09-29 | 4.2–52.4 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/the_agent_company_external.csv` |
| **Terminal Bench** (`terminal-bench`) | 212 | 2025-05-22 → 2026-05-14 | 3.1–84.7 % (Terminal-Bench 2.0) | still discriminating | `data/aggregator-epoch-benchmarking-hub/terminalbench_external.csv`<br>`data/terminal-bench.csv` |
| **Cybench** (`cybench`) | 22 | 2024-02-15 → 2026-02-05 | 5–93 percent | likely saturated (near ceiling) | `data/aggregator-epoch-benchmarking-hub/cybench_external.csv` |
| **ExploitBench** (`exploitbench`) | 20 | 2025-10-15 → 2026-04-23 | 13.3–73.8 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/exploitbench_external.csv` |
| **APEX Agents** (`apex-agents`) | 55 | 2024-11-20 → 2026-07-24 | 1.1–45 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/apex_agents_external.csv` |
| **DeepResearch Bench** (`deepresearchbench`) | 35 | 2025-01-21 → 2026-05-28 | 29.19–55.314 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/deepresearchbench_external.csv` |

### Long-horizon autonomy, AI R&D & "AI researcher" / RSI signal

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **METR Time Horizon** (`metr-time-horizon`) | 26 | 2019-02-14 → 2026-04-07 | 0.054–1044.78 hours (human-expert-equivalent task time, 50% success rate) | still discriminating | `data/metr-time-horizon.csv` |
| **METR Cross-Domain Time Horizon** (`metr-cross-domain-time-horizon`) | 4 | 2025-07-14 → 2025-07-14 | 3–24 approx doubling time (months) of domain-specific time horizon ('~2 years') | still discriminating | `data/metr-cross-domain-time-horizon.csv` |
| **RE-Bench (METR)** (`re-bench`) | 4 | 2024-11-22 → 2024-11-22 | 0.46–4 normalized score (0=starting solution, 1=reference solution), 8-hour budget | still discriminating | `data/re-bench.csv` |
| **MLE-bench** (`mle-bench`) | 28 | 2024-10-08 → 2026-03-06 | 1.6–64.44 % (any-medal rate, MLE-bench 'All'/split75 comparable subset) | still discriminating | `data/mle-bench.csv` |
| **Paperbench** (`paperbench`) | 12 | 2024-05-13 → 2025-04-07 | 2.6–43.4 % PaperBench replication score | still discriminating | `data/paperbench.csv` |
| **AI Scientist (Sakana et al.)** (`ai-scientist`) | 6 | 2025-02-20 → 2026-04-18 | 1–42 mean paper-quality score, 1-5 scale (LLM-judge synthesis of GPT-5.4/Gemini/Claude reviewers) | still discriminating | `data/ai-scientist.csv` |
| **OpenAI Self-Improvement Evals** (`openai-ai-self-improvement-evals`) | 8 | 2025-08-13 → 2025-08-13 | 1–45 % pass@1 (OpenAI-Proof Q&A) | still discriminating | `data/openai-ai-self-improvement-evals.csv` |
| **PostTrainBench** (`posttrainbench`) | 35 | 2025-09-24 → 2026-07-24 | 7.25–41.79 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/posttrainbench_external.csv` |

### Multimodal & vision

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **MMMU** (`mmmu`) | 79 | 2023-11-27 → 2026-07-01 | 32.6–88.6 % accuracy (MMMU-Pro, overall -- harder 10-option variant; used because this snapshot did not report a standard MMMU-validation score) | still discriminating | `data/mmmu.csv` |
| **MMBench** (`mmbench`) | 69 | 2023-12-23 → 2025-08-14 | 58–88.5 % accuracy (MMBench-EN v1.1, test split, overall) | still discriminating | `data/mmbench.csv` |
| **ChartQA** (`chartqa`) | 11 | 2024-03-04 → 2025-02-02 | 78.1–90.8 % relaxed accuracy (ChartQA test avg.) | likely saturated (near ceiling) | `data/chartqa.csv` |
| **DocVQA** (`docvqa`) | 11 | 2024-03-04 → 2025-02-02 | 87.2–96.4 ANLS score (DocVQA test) | likely saturated (near ceiling) | `data/docvqa.csv` |
| **Video-MME** (`video-mme`) | 50 | 2023-08-20 → 2025-06-18 | 37.9–79.7 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/video_mme_external.csv` |
| **SpatialViz-Bench** (`spatialviz-bench`) | 8 | 2024-01-18 → 2025-06-17 | 31.78–44.66 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/spatialviz_bench_external.csv` |
| **MindCube** (`mindcube`) | 5 | 2024-06-13 → 2025-05-22 | 29.46–46.67 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/mindcube_external.csv` |
| **GeoBench** (`geobench`) | 32 | 2024-07-18 → 2025-12-17 | 2131–4333 raw | still discriminating | `data/aggregator-epoch-benchmarking-hub/geobench_external.csv` |

### ARC-AGI family (interactive/abstraction reasoning)

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **ARC-AGI-1** (`arc-agi-1`) | 268 | 2019-11-05 → 2026-08-11 | 0–98.5 % correct (semi-private eval set) | likely saturated (near ceiling) | `data/aggregator-epoch-benchmarking-hub/arc_agi_external.csv`<br>`data/arc-agi-1.csv` |
| **ARC-AGI-2** (`arc-agi-2`) | 255 | 2023-11-03 → 2026-08-11 | 0–100 % correct (semi-private eval set) | likely saturated (near ceiling) | `data/aggregator-epoch-benchmarking-hub/arc_agi_2_external.csv`<br>`data/arc-agi-2.csv` |
| **ARC-AGI-3** (`arc-agi-3`) | 36 | 2025-12-17 → 2026-08-11 | 0.01–100 % of public demo set solved (official ARC-AGI-3 leaderboard, bare model + minimal harness) | likely saturated (near ceiling) | `data/arc-agi-3.csv` |

### Games, puzzles & misc. Epoch-run evals

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **Chess Puzzles (Epoch)** (`chess-puzzles`) | 161 | 2023-06-13 → 2026-08-13 | 0–64 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/chess_puzzles.csv` |
| **Mystery Game Puzzles (Epoch)** (`mystery-game-puzzles`) | 53 | 2025-08-05 → 2026-08-13 | 6–59 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/mystery_game_puzzles.csv` |
| **Balrog** (`balrog`) | 36 | 2024-05-13 → 2026-02-19 | 3.7–58.1 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/balrog_external.csv` |
| **Surface Evolver Bench** (`surface-evolver-bench`) | 24 | 2025-08-05 → 2026-07-16 | 15.625–95 percent | likely saturated (near ceiling) | `data/aggregator-epoch-benchmarking-hub/surface_evolver_bench_external.csv` |
| **Weirdml** (`weirdml`) | 161 | 2023-06-13 → 2026-07-31 | 1.73–91.94 percent | likely saturated (near ceiling) | `data/aggregator-epoch-benchmarking-hub/weirdml_external.csv` |
| **Forecastbench** (`forecastbench`) | 75 | 2023-06-13 → 2026-05-28 | 50.4–62.5 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/forecastbench_external.csv` |
| **Fictionlivebench** (`fictionlivebench`) | 42 | 2024-12-17 → 2026-01-27 | 18.8–100 percent | likely saturated (near ceiling) | `data/aggregator-epoch-benchmarking-hub/fictionlivebench_external.csv` |
| **Lech Mazur Writing** (`lech-mazur-writing`) | 49 | 2024-07-18 → 2025-08-07 | 6.05–8.6 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/lech_mazur_writing_external.csv` |
| **Simplebench** (`simplebench`) | 91 | 2024-02-29 → 2026-07-09 | 10.7–81.9 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/simplebench_external.csv` |
| **RLI** (`rli`) | 12 | 2025-06-05 → 2026-06-09 | 0.83–16.1 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/rli_external.csv` |
| **Cl Bench** (`cl-bench`) | 22 | 2025-04-16 → 2026-03-31 | 11.4–27.9 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/cl_bench_external.csv` |
| **Cl Bench Life** (`cl-bench-life`) | 16 | 2025-09-29 → 2026-04-24 | 6.3–22.2 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/cl_bench_life_external.csv` |
| **Blueprint Bench 2** (`blueprint-bench-2`) | 21 | 2025-10-15 → 2026-07-24 | 0–38.612 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/blueprint_bench_2_external.csv` |
| **Vpct** (`vpct`) | 38 | 2024-06-20 → 2025-12-17 | 30–91 percent | likely saturated (near ceiling) | `data/aggregator-epoch-benchmarking-hub/vpct_external.csv` |
| **Enigma Eval** (`enigma-eval`) | 46 | 2024-02-29 → 2026-07-09 | 0.38–39.28 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/enigma_eval_external.csv` |
| **Cad Eval** (`cad-eval`) | 14 | 2024-03-07 → 2025-04-16 | 12–74 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/cad_eval_external.csv` |
| **Btf3** (`btf3`) | 9 | 2026-04-23 → 2026-07-24 | 11.8–15.4 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/btf3_external.csv` |
| **Proofbench** (`proofbench`) | 50 | 2025-08-07 → 2026-07-24 | 0–78 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/proofbench_external.csv` |
| **Gbaeval** (`gbaeval`) | 23 | 2026-02-05 → 2026-07-24 | 0–79.599 percent | still discriminating | `data/aggregator-epoch-benchmarking-hub/gbaeval_external.csv` |

### Web & computer-use agents

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **WorkArena / WorkArena++** (`workarena`) | 17 | 2024-05-13 → 2026-03-12 | 27–90.3 percent success rate (WorkArena L1) | likely saturated (near ceiling) | `data/workarena.csv` |
| **VisualWebArena** (`visualwebarena`) | 9 | 2024-01-24 → 2024-01-24 | 0.33–88.7 percent success rate (VisualWebArena) | still discriminating | `data/visualwebarena.csv` |
| **Online-Mind2Web** (`online-mind2web`) | 13 | 2025-03-22 → 2026-08-04 | 28–97.7 percent success rate (Online-Mind2Web, human-graded) | likely saturated (near ceiling) | `data/online-mind2web.csv` |
| **WebVoyager** (`webvoyager`) | 6 | 2024-01-25 → 2024-06-06 | 30.8–59.1 percent task success rate (WebVoyager, GPT-4V auto-eval) | still discriminating | `data/webvoyager.csv` |
| **WebBench** (`webbench`) | 2 | 2025-05-30 → 2025-05-30 | 46.6–66 percent overall task success rate (WebBench, fully-automated agents) | still discriminating | `data/webbench.csv` |
| **AssistantBench** (`assistantbench`) | 7 | 2024-07-22 → 2024-07-22 | 4.1–25.2 percent accuracy (AssistantBench test set) | still discriminating | `data/assistantbench.csv` |
| **Windows Agent Arena** (`windows-agent-arena`) | 5 | 2024-09-12 → 2024-09-12 | 3.5–74.5 percent success rate (Windows Agent Arena) | still discriminating | `data/windows-agent-arena.csv` |
| **AppWorld (+ AppWorld-UL)** (`appworld`) | 8 | 2024-07-26 → 2026-02-15 | 13.1–86.9 percent task goal completion (AppWorld, Test-Normal, best scaffold) | still discriminating | `data/appworld.csv` |
| **Mind2Web** (`mind2web`) | 3 | 2023-06-09 → 2023-06-09 | 0.8–5.2 percent task success rate (Mind2Web cross-task test split) | still discriminating | `data/mind2web.csv` |
| **MiniWoB++** (`miniwob-plus-plus`) | 16 | 2024-05-13 → 2026-03-16 | 56.6–74.9 percent success rate (MiniWoB++) | still discriminating | `data/miniwob-plus-plus.csv` |
| **AssistGUI** (`assistgui`) | 4 | 2023-12-20 → 2023-12-20 | 5–46 percent success rate (AssistGUI) | still discriminating | `data/assistgui.csv` |
| **SPA-Bench** (`spa-bench`) | 11 | 2024-10-19 → 2024-10-19 | 1–54.4 percent success rate (SPA-Bench, single-app overall) | still discriminating | `data/spa-bench.csv` |

### Tool-use & function-calling

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **Berkeley Function-Calling Leaderboard (BFCL v1-v4)** (`bfcl`) | 6 | 2024-10-21 → 2025-12-17 | 62.19–78.45 % overall accuracy (BFCL, top-ranked model) | still discriminating | `data/bfcl.csv` |
| **tau2-bench (Telecom)** (`tau2-bench-telecom`) | 18 | 2025-06-09 → 2026-07-09 | 34–99.1 % pass rate (tau2-bench Telecom, Artificial Analysis independent eval) | likely saturated (near ceiling) | `data/tau2-bench-telecom.csv` |
| **MCP-Atlas** (`mcp-atlas`) | 30 | 2026-04-08 → 2026-04-08 | 40.2–88.1 % pass rate (All 1000 tasks) | still discriminating | `data/mcp-atlas.csv` |
| **ToolBench / ToolEval** (`toolbench`) | 6 | 2022-11-28 → 2023-08-01 | 22.6–71.1 pass rate % avg across I1-I3 test splits (ToolBench/ToolEval) | still discriminating | `data/toolbench.csv` |
| **MINT-Bench** (`mint-bench`) | 5 | 2023-05-10 → 2023-08-09 | 14.5–69.5 Success Rate % at k=5 interaction turns (MINT, micro-averaged) | still discriminating | `data/mint-bench.csv` |
| **CRMArena / CRMArena-Pro** (`crmarena-pro`) | 9 | 2024-02-29 → 2025-01-20 | 3.1–64.3 Overall % accuracy (CRMArena-Pro, best agentic scaffold per model) | still discriminating | `data/crmarena-pro.csv` |

### Games & interactive environments

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **Kaggle Game Arena** (`kaggle-game-arena`) | 15 | 2026-08-17 → 2026-08-17 | -2.15–353 Werewolf equilibrium rating (percent) | likely saturated (near ceiling) | `data/kaggle-game-arena.csv` |
| **lmgame-Bench** (`lmgame-bench`) | 29 | 2025-06-03 → 2025-06-03 | 7–3445 Candy Crush score (no model; random-action baseline) | likely saturated (near ceiling) | `data/lmgame-bench.csv` |
| **VideoGameBench** (`videogamebench`) | 7 | 2026-05-14 → 2026-05-14 | 0–0.48 percent of VideoGameBench test-set completed (checkpoint-weighted avg across 7 test games) | still discriminating | `data/videogamebench.csv` |
| **Werewolf Arena** (`werewolf-arena`) | 6 | 2024-07-18 → 2024-07-18 | 0–90.9 percent of Seer werewolf-reveals believed by villagers | likely saturated (near ceiling) | `data/werewolf-arena.csv` |
| **DSGBench** (`dsgbench`) | 6 | 2025-03-01 → 2025-03-01 | 10.94–56.16 DSGBench overall score (0-100 scale; avg of 5 ability dimensions across strategy games) | still discriminating | `data/dsgbench.csv` |
| **GameBench** (`gamebench`) | 7 | 2024-07-22 → 2024-07-22 | 0.31–0.85 GameBench overall avg score (0-1 scale; fraction of best possible score across 8 obscure strategy games) | still discriminating | `data/gamebench.csv` |
| **GAMEBoT** (`gamebot`) | 14 | 2025-07-27 → 2025-07-27 | -0.36–0.42 GAMEBoT avg outcome score (-1 to 1 scale; avg across 8 games, head-to-head win/draw/loss) | still discriminating | `data/gamebot.csv` |
| **GAMA-Bench** (`gama-bench`) | 13 | 2025-01-15 → 2025-01-15 | 42.7–69.8 GAMA-Bench overall score (0-100 scale; avg across 9 economic/strategic games) | still discriminating | `data/gama-bench.csv` |
| **LLM-Hanabi** (`llm-hanabi`) | 14 | 2025-10-06 → 2025-10-06 | 3.47–30 LLM-Hanabi cooperative game score (0-25 scale; 5-player, CoT prompting) | still discriminating | `data/llm-hanabi.csv` |
| **ORAK** (`orak`) | 9 | 2025-06-09 → 2025-06-09 | 3.9–17.8 ORAK average rank across 12 games (1=best) | still discriminating | `data/orak.csv` |
| **GameDevBench** (`gamedevbench`) | 11 | 2026-08-17 → 2026-08-17 | 5.4–67.3 percent of 333 Godot game-dev tasks solved | still discriminating | `data/gamedevbench.csv` |
| **Roblox Open Game Eval** (`roblox-open-game-eval`) | 11 | 2026-08-17 → 2026-08-17 | 40.23–64.67 Roblox Open Game Eval pass@1 (Debug Eval Leaderboard) | still discriminating | `data/roblox-open-game-eval.csv` |
| **Classic RL suites (Atari/ALE, Procgen, NetHack LE, MineRL/MineDojo, Crafter, GVGAI, DMLab-30, Habitat, BabyAI, TextWorld, Jericho, ScienceWorld)** (`classic-rl-suites`) | 20 | 2024-11-11 → 2026-02-25 | 19.5–58.1 BALROG overall % progress (avg across NetHack LE, BabyAI, Crafter, TextWorld, BabaIsAI, MiniHack) | still discriminating | `data/classic-rl-suites.csv` |
| **Kaggle Game Arena (Chess Elo)** (`kaggle-game-arena-elo`) | 5 | 2026-08-17 → 2026-08-17 | 1258–1367 Chess Elo-style rating | still discriminating | `data/kaggle-game-arena.csv` |

### Safety, alignment & red-teaming

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **WMDP (Weapons of Mass Destruction Proxy)** (`wmdp`) | 6 | 2024-03-05 → 2024-03-05 | 44–75.3 percent accuracy (WMDP-Cyber subset) | still discriminating | `data/wmdp.csv` |
| **HarmBench** (`harmbench`) | 8 | 2024-02-06 → 2024-02-06 | 2–33 percent attack success rate (Direct Request; standard behaviors) | still discriminating | `data/harmbench.csv` |
| **JailbreakBench** (`jailbreakbench`) | 8 | 2023-03-01 → 2024-04-02 | 0–93 percent attack success rate (Prompt with Random Search attack; no defense) | likely saturated (near ceiling) | `data/jailbreakbench.csv` |
| **AgentHarm** (`agentharm`) | 6 | 2024-10-11 → 2024-10-11 | 13.5–82.2 percent harm score (template jailbreak attack; standard prompt) | still discriminating | `data/agentharm.csv` |
| **AgentDojo** (`agentdojo`) | 19 | 2024-06-05 → 2025-02-24 | 1.11–56.28 percent targeted attack success rate (important_instructions attack; no defense) | still discriminating | `data/agentdojo.csv` |
| **MASK** (`mask`) | 12 | 2025-03-05 → 2025-03-05 | 26.6–63 percent P(lie) under pressure | still discriminating | `data/mask.csv` |
| **RealToxicityPrompts** (`realtoxicityprompts`) | 5 | 2020-09-24 → 2020-09-24 | 0.82–0.9 toxicity probability (toxic-prompt continuations) | still discriminating | `data/realtoxicityprompts.csv` |
| **HaluEval / HaluEval 2.0** (`halueval`) | 11 | 2023-05-19 → 2023-05-19 | 6.68–69.78 percent accuracy recognizing hallucinated QA answers | still discriminating | `data/haluEval.csv` |
| **FActScore** (`factscore`) | 3 | 2023-05-23 → 2023-05-23 | 42.5–71.5 FActScore (percent atomic facts supported) | still discriminating | `data/factscore.csv` |
| **Vectara Hallucination Leaderboard** (`vectara-hallucination-leaderboard`) | 15 | 2024-08-06 → 2025-11-01 | 4.5–18.6 percent hallucination rate (RAG summarization) | still discriminating | `data/vectara-hallucination-leaderboard.csv` |

### Instruction-following & chat quality

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **IFEval** (`ifeval`) | 5 | 2023-08-01 → 2024-06-26 | 43.07–77.45 % prompt-level strict-accuracy (IFEval) | still discriminating | `data/ifeval.csv` |
| **IFBench** (`ifbench`) | 14 | 2025-08-05 → 2026-07-09 | 54.3–83.3 % accuracy (IFBench, Artificial Analysis independent eval) | still discriminating | `data/ifbench.csv` |
| **FollowBench** (`followbench`) | 13 | 2023-07-01 → 2023-11-30 | 33.1–73.4 Hard Satisfaction Rate % avg across L1-L5 (FollowBench) | still discriminating | `data/followbench.csv` |
| **MT-Bench** (`mt-bench`) | 9 | 2023-02-24 → 2023-03-30 | 2.61–8.99 MT-Bench score (1-10, GPT-4-judged) | still discriminating | `data/mt-bench.csv` |
| **AlpacaEval 2.0** (`alpacaeval-2`) | 16 | 2023-03-13 → 2024-07-23 | 5.88–57.46 % length-controlled win rate vs. GPT-4-Preview-1106 | still discriminating | `data/alpacaeval-2.csv` |
| **WildBench** (`wildbench`) | 11 | 2023-07-18 → 2024-05-13 | 61.93–82.65 WB-Score (0-100, WildBench v2 leaderboard) | still discriminating | `data/wildbench.csv` |
| **MultiChallenge** (`multichallenge`) | 30 | 2025-03-05 → 2026-07-09 | 36.35–75.52 % accuracy (MultiChallenge, Scale AI leaderboard) | still discriminating | `data/multichallenge.csv` |

### Long-context & memory

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **RULER** (`ruler`) | 9 | 2023-11-06 → 2025-04-29 | 80.5–96 percent accuracy (RULER 13-task avg across 4K-128K) | likely saturated (near ceiling) | `data/ruler.csv` |
| **LongBench / LongBench v2** (`longbench-v2`) | 9 | 2024-09-12 → 2025-07-25 | 56–63.3 percent accuracy (overall, w/ CoT) | still discriminating | `data/longbench-v2.csv` |
| **InfiniteBench** (`infinitebench`) | 7 | 2024-02-21 → 2024-02-21 | 10.48–72.49 percent accuracy (En.MC subtask, 100K+ context multiple-choice) | still discriminating | `data/infinitebench.csv` |
| **BABILong** (`babilong`) | 7 | 2024-06-01 → 2025-04-01 | 55.4–74.9 percent accuracy (avg qa1-5, aggregated 0k-128k context) | still discriminating | `data/babilong.csv` |
| **SCROLLS** (`scrolls`) | 4 | 2022-01-01 → 2022-01-01 | 27.06–29.16 SCROLLS composite average score (Table 2) | still discriminating | `data/scrolls.csv` |
| **MRCR v2 (Multi-Round Context Retrieval)** (`mrcr-v2`) | 14 | 2024-05-14 → 2026-02-17 | 4–84.9 percent accuracy (MRCR v2 8-needle, 128K average) | still discriminating | `data/mrcr-v2.csv` |

### Multilingual

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **Belebele** (`belebele`) | 5 | 2023-08-01 → 2023-08-01 | 41.5–60.2 percent accuracy (avg across 122 languages) | still discriminating | `data/belebele.csv` |
| **MGSM (Multilingual GSM8K)** (`mgsm`) | 11 | 2022-10-06 → 2025-04-16 | 45.6–93.7 percent accuracy (avg across languages) | likely saturated (near ceiling) | `data/mgsm.csv` |
| **IndicGenBench / IndicMMLU** (`indicgenbench`) | 8 | 2024-04-01 → 2024-04-01 | 4.6–69.3 F1 (XQuAD-In, one-shot) | still discriminating | `data/indicgenbench.csv` |
| **MMLU-ProX** (`mmlu-prox`) | 10 | 2024-05-23 → 2025-04-29 | 25.6–75.5 percent accuracy (avg across 29 languages) | still discriminating | `data/mmlu-prox.csv` |

### Domain-professional (medicine, law, finance)

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **HealthBench** (`healthbench`) | 5 | 2023-09-01 → 2025-04-16 | 16–60 percent (HealthBench overall score) | still discriminating | `data/healthbench.csv` |
| **MedXpertQA** (`medxpertqa`) | 17 | 2024-05-13 → 2025-01-31 | 15.06–56.28 percent accuracy (MedXpertQA Text avg) | still discriminating | `data/medxpertqa.csv` |
| **MedQA / MedQA-USMLE** (`medqa`) | 7 | 2022-12-01 → 2023-11-28 | 67.2–90.2 percent accuracy (MedQA US 4-option) | likely saturated (near ceiling) | `data/medqa.csv` |
| **MedMCQA** (`medmcqa`) | 8 | 2022-03-10 → 2023-05-16 | 33–73.7 percent accuracy (MedMCQA dev) | still discriminating | `data/medmcqa.csv` |
| **PubMedQA** (`pubmedqa`) | 25 | 2019-09-13 → 2024-04-18 | 55.8–82 percent accuracy (PubMedQA reasoning-required) | still discriminating | `data/pubmedqa.csv` |
| **LegalBench (via Vals AI)** (`legalbench`) | 12 | 2023-08-20 → 2023-08-20 | 58.1–89.9 percent correctness (LegalBench rule-application) | still discriminating | `data/legalbench.csv` |
| **CaseHOLD** (`casehold`) | 5 | 2021-04-18 → 2021-04-18 | 39.9–69.5 macro F1 (CaseHOLD) | still discriminating | `data/casehold.csv` |
| **FinBen** (`finben`) | 3 | 2024-06-19 → 2024-06-19 | 0.02–1.51 Sharpe Ratio (FinBen stock-trading decision task) | still discriminating | `data/finben.csv` |
| **FinanceBench (+ DocFinQA)** (`financebench`) | 8 | 2023-11-01 → 2023-11-01 | 9–85 percent correct (FinanceBench, 150-case subset) | still discriminating | `data/financebench.csv` |

### Coding & data (extended)

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **Spider 2.0** (`spider-2`) | 11 | 2024-11-30 → 2026-02-09 | 9.68–94.15 % execution accuracy (Spider 2.0-Snow) | likely saturated (near ceiling) | `data/spider-2.csv` |
| **BIRD-SQL** (`bird-sql`) | 5 | 2023-02-17 → 2025-12-16 | 36.47–81.95 EX % (test set) | still discriminating | `data/bird-sql.csv` |
| **DS-1000** (`ds-1000`) | 5 | 2022-11-21 → 2024-04-09 | 38.6–53.9 pass@1 % (mean over 1000 problems) | still discriminating | `data/ds-1000.csv` |
| **BigCodeBench** (`bigcodebench`) | 11 | 2024-04-18 → 2025-04-14 | 43.6–51.1 pass@1 % (Instruct split) | still discriminating | `data/bigcodebench.csv` |
| **EvalPlus / HumanEval+** (`evalplus`) | 12 | 2023-05-01 → 2024-11-12 | 73.3–89 pass@1 % (MBPP+) | still discriminating | `data/evalplus.csv` |
| **APPS** (`apps-bench`) | 4 | 2021-11-08 → 2021-11-08 | 0.06–1.12 strict accuracy % (avg across Introductory/Interview/Competition) | still discriminating | `data/apps-bench.csv` |
| **SWE-Lancer** (`swe-lancer`) | 6 | 2025-05-29 → 2025-05-29 | 23.3–36.1 pass@1 % (SWE-Lancer Diamond: IC SWE + SWE Manager combined) | still discriminating | `data/swe-lancer.csv` |

### Embedding & retrieval (different capability axis)

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **MTEB (Massive Text Embedding Benchmark)** (`mteb`) | 5 | 2023-09-12 → 2025-03-07 | 64.23–72.31 mean task score (MTEB Multilingual leaderboard) | still discriminating | `data/mteb.csv` |

### Multimodal (extended: image, video, audio)

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **HEIM (Holistic Evaluation of Text-to-Image Models)** (`heim`) | 9 | 2021-12-14 → 2023-04-28 | 0.074–0.971 alignment win rate (HEIM Table 5, 0-1 scale) | still discriminating | `data/heim.csv` |
| **GenAI-Bench** (`genai-bench`) | 10 | 2023-01-30 → 2024-05-20 | 8.88–49.2 average pairwise-judgment accuracy vs. human votes (GenAI-Bench, %) | still discriminating | `data/genai-bench.csv` |
| **RealWorldQA** (`realworldqa`) | 13 | 2024-04-12 → 2025-02-02 | 49.8–78.7 percent accuracy (RealWorldQA) | still discriminating | `data/realworldqa.csv` |
| **MME (Multimodal LLM Evaluation)** (`mme`) | 9 | 2024-05-13 → 2025-02-02 | 1872–2494 MME sum score (perception+cognition, max 2800) | likely saturated (near ceiling) | `data/mme.csv` |
| **SEED-Bench** (`seed-bench`) | 11 | 2023-01-30 → 2023-06-08 | 31.17–53.37 percent accuracy (SEED-Bench overall) | still discriminating | `data/seed-bench.csv` |
| **AudioBench** (`audiobench`) | 5 | 2023-10-20 → 2024-07-15 | 50.51–85.25 CN-College-Listen speech-QA accuracy, LLM-judged (AudioBench Table 2) | still discriminating | `data/audiobench.csv` |
| **AIR-Bench (Audio Instruct)** (`air-bench-audio`) | 7 | 2023-05-18 → 2023-11-14 | 1.15–6.34 AIR-Bench Chat average score (1-10 scale) | still discriminating | `data/air-bench-audio.csv` |

### Reasoning, planning & social cognition

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **PlanBench** (`planbench`) | 15 | 2023-11-26 → 2025-01-01 | 0.5–99.1 percent accuracy (zero-shot Blocksworld NL) | likely saturated (near ceiling) | `data/planbench.csv` |
| **ToMBench** (`tombench`) | 7 | 2024-02-23 → 2024-02-23 | 40.3–74 percent accuracy (English subset, task-oriented average) | still discriminating | `data/tombench.csv` |
| **MuSR (Multistep Soft Reasoning)** (`musr`) | 7 | 2023-10-24 → 2023-10-24 | 34.83–69.9 percent accuracy (avg of murder mystery/object placement/team allocation) | still discriminating | `data/musr.csv` |
| **StrategyQA** (`strategyqa`) | 5 | 2021-01-06 → 2022-01-28 | 65.4–77.8 percent accuracy | still discriminating | `data/strategyqa.csv` |
| **CLUTRR** (`clutrr`) | 5 | 2019-08-16 → 2019-08-16 | 37–100 percent accuracy (clean train/test setting) | likely saturated (near ceiling) | `data/clutrr.csv` |
| **HotpotQA** (`hotpotqa`) | 3 | 2018-09-25 → 2022-10-06 | 28.7–45.46 exact match (distractor-style setting) | still discriminating | `data/hotpotqa.csv` |
| **DROP (Discrete Reasoning Over Paragraphs)** (`drop`) | 5 | 2019-03-01 → 2023-03-15 | 36.5–80.9 F1 | still discriminating | `data/drop.csv` |
| **NarrativeQA** (`narrativeqa`) | 9 | 2017-12-19 → 2023-08-28 | 11.8–36.3 F1 | still discriminating | `data/narrativeqa.csv` |

### Scientific-agent & AI-researcher (extends RSI cluster)

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **AstaBench** (`astabench`) | 7 | 2026-04-30 → 2026-04-30 | 46.5–58 percent (overall AstaBench score) | still discriminating | `data/astabench.csv` |
| **AIRS-Bench** (`airs-bench`) | 14 | 2026-02-16 → 2026-02-16 | 0.018–0.402 normalized score (0-1 scale vs SOTA) | still discriminating | `data/airs-bench.csv` |
| **ScienceAgentBench** (`scienceagentbench`) | 6 | 2024-10-07 → 2024-10-07 | 13.7–42.2 success rate % (direct prompting + self-debug, no expert knowledge) | still discriminating | `data/scienceagentbench.csv` |

### Embodied & robotics

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **EmbodiedBench** (`embodiedbench`) | 18 | 2025-02-13 → 2025-02-13 | 22.6–68 percent success rate (EmbodiedBench EB-Navigation avg) | still discriminating | `data/embodiedbench.csv` |
| **ALFWorld / ScienceWorld / Habitat-BEHAVIOR / RoboCasa / EMMOE** (`alfworld-scienceworld`) | 8 | 2021-03-14 → 2022-10-06 | 6–71 percent success rate (ALFWorld overall) | still discriminating | `data/alfworld-scienceworld.csv` |

### Multi-agent & social reasoning

| Benchmark | Data points | Date range | Score range | Status | Source file(s) |
| --- | --- | --- | --- | --- | --- |
| **MultiAgentBench (MARBLE)** (`multiagentbench`) | 5 | 2025-03-03 → 2025-03-03 | 43.85–52.73 Task Score (0-100, avg across Research/Minecraft/Database/Coding/Bargaining/Werewolf scenarios) | still discriminating | `data/multiagentbench.csv` |

### Other Epoch-hub benchmarks not yet slotted into a category above

| Benchmark | Data points | Date range |
| --- | --- | --- |
| **Epoch Capabilities Index** (`epoch-capabilities-index`) | 498 | 2023-02-24 → 2026-08-02 |
| **Epoch Capabilities Index Percent** (`epoch-capabilities-index-percent`) | 20 | 2023-02-24 → 2024-11-29 |
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
