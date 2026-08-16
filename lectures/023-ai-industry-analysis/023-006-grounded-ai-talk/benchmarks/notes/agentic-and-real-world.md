# Agentic, tool-use, computer-use, and real-world-economic-task benchmarks

Research cluster covering: GAIA, WebArena, AgentBench, tau-bench, OSWorld,
AndroidWorld, BrowseComp, GDPval, Vending-Bench, and "AI researcher" /
recursive-self-improvement-flavored agentic evals. Data files live in
`../data/*.csv` (columns: `date,model,score,score_unit,source_url,notes`).
Every row has a real, cited source; nothing here is estimated or interpolated.

---

## GAIA (General AI Assistants)

- **Maintainer/creator:** Meta FAIR, Hugging Face, AutoGPT, GenAI (Meta) - Mialon et al., Nov 2023.
- **What it measures:** Real-world questions requiring reasoning, multi-modality handling, web browsing, and tool use, designed to be easy for humans but hard for AI.
- **Scale:** % accuracy (exact-match), 466 questions across 3 difficulty levels.
- **URLs:** paper https://arxiv.org/pdf/2311.12983 · HF leaderboard https://huggingface.co/spaces/gaia-benchmark/leaderboard · HAL reproduction https://hal.cs.princeton.edu/gaia
- **Data:** 14 points, Nov 2023 - Sep 2025.
- **Trend:** Went from 15% (GPT-4+plugins, launch) to 74.55% (Claude Sonnet 4.5, HAL scaffold) in under two years - a huge, still-climbing trajectory, nowhere near the 92% human baseline but closing fast. Notably, H2O.ai's h2oGPTe agent jumped from 65% (Dec 2024) to 75% (Mar 2025, on the *harder* test split) in about 3 months. HAL has since paused adding new models to focus on agent *reliability* rather than raw accuracy - itself a signal that raw-score progress was outpacing the community's ability to trust the numbers.

## WebArena (and VisualWebArena)

- **Maintainer/creator:** CMU (Zhou, Xu et al.), ICLR 2024.
- **What it measures:** End-to-end functional-correctness success on 812 long-horizon tasks across 4 self-hosted, fully-functional websites (e-commerce, forums, GitLab, CMS) plus map/wiki/calculator tools.
- **Scale:** % end-to-end task success rate.
- **URLs:** paper https://arxiv.org/pdf/2307.13854 · site https://webarena.dev/
- **Data:** only 2 solid points found (Jul 2023 baseline, Jan 2025 OpenAI CUA). No distinct VisualWebArena time-series data was found with a comparably reliable source, so it isn't broken out separately.
- **Trend:** GPT-4 baseline 14.41% -> OpenAI's CUA hit 58.1% in 18 months, a 4x jump, but the benchmark itself appears to have fallen out of frontier-lab reporting habits (unlike GAIA/OSWorld/tau-bench, WebArena scores are rarely quoted in 2025-2026 model system cards), so the public trend line is thin despite real underlying progress. Treat the "58.1%" endpoint as a snapshot, not a dense trend.

## AgentBench

- **Maintainer/creator:** Tsinghua University, Ohio State, UC Berkeley (Liu, Yu, Zhang et al.), ICLR 2024.
- **What it measures:** LLM-as-Agent reasoning/decision-making across 8 environments (OS, DB, knowledge graph, digital card game, lateral-thinking puzzles, house-holding, web shopping, web browsing).
- **Scale:** Overall score, roughly 0-8/0-10 (weighted average across environments).
- **URLs:** paper https://arxiv.org/abs/2308.03688 · GitHub https://github.com/THUDM/AgentBench
- **Data:** 7 points, all from the single original-paper chart (Aug 2023 submission; the PDF was later revised, v3, to add newer comparison models like Claude 2/3).
- **Trend:** GPT-4 topped the original chart at 4.01/8 vs. an open-source-model average of 0.51 - a big commercial/open gap, but a low absolute ceiling. Notably, **this benchmark has effectively gone stale**: frontier labs stopped reporting AgentBench scores in their system cards well before 2026, superseded by GAIA/OSWorld/tau-bench/SWE-bench. This is itself a data point about benchmark churn in the agentic space - the field moved to harder, more specialized replacements rather than pushing this one to saturation.

## tau-bench / tau2-bench (Sierra)

- **Maintainer/creator:** Sierra (Yao et al.), June 2024.
- **What it measures:** Tool-using dialogue agents in customer-service domains (retail, airline), with a simulated user and policy-compliance grading, not just task completion.
- **Scale:** pass^1 (single-attempt success rate) and pass^k (consistency across k repeated attempts), per domain.
- **URLs:** paper https://arxiv.org/abs/2406.12045 · GitHub (frozen leaderboard) https://github.com/sierra-research/tau-bench · successor https://github.com/sierra-research/tau2-bench · HAL https://hal.cs.princeton.edu/taubench_airline
- **Data:** 11 points, Jun 2024 - Aug 2025.
- **Trend:** Claude 3.5 Sonnet (Oct 2024) topped the official *frozen* leaderboard at 69.2% retail / 46.0% airline and nothing has displaced it there since - **because Sierra explicitly froze the original task set** (citing task-quality bugs) and redirected new evaluation to tau2-bench/tau3-bench. Independent HAL reproductions on the airline split show GPT-5-era and Claude-4-era models still only in the mid-50s%, i.e. this benchmark is *not* saturated and progress since late 2024 has been surprisingly flat/noisy rather than fast - a useful counter-example to the "everything agentic is racing to the ceiling" narrative.

## OSWorld / OSWorld-Verified (and OSWorld 2.0)

- **Maintainer/creator:** HKU, CMU, Salesforce Research, U. Waterloo (Xie, Zhang et al.), NeurIPS 2024.
- **What it measures:** Real, executable computer-use tasks (GUI + CLI) across Ubuntu/Windows/macOS-style environments and arbitrary real apps, execution-graded.
- **Scale:** % task success rate; human baseline 72.36% on the original 369-task set.
- **URLs:** paper https://arxiv.org/pdf/2404.07972 · official leaderboard (OSWorld-Verified) https://osworld-v1.xlang.ai/ · harder successor (OSWorld 2.0) https://osworld-v2.xlang.ai/
- **Data:** 21 points, May 2024 - Aug 2026, most pulled directly from the benchmark maintainers' own leaderboard spreadsheet (each row carries its own citation link back to the submitting lab/paper).
- **Trend:** This is the **standout "surprisingly fast" case** in this cluster. The original paper's best agent scored 12.24% (May 2024); by December 2025 an agent had crossed the 72.36% human baseline (72.58%); by July 2026 the top score was 90.19%. That's a climb from barely-double-digits to near-saturation in about 26 months. The benchmark's own maintainers responded by shipping a deliberately harder successor, **OSWorld 2.0** (108 longer-horizon tasks), where even the best mid-2026 model (Claude Opus 4.8) only reaches 20.6% - a clean example of a benchmark being "re-hardened" the moment it saturates, which is itself informative about the plateau question: individual benchmark instances saturate fast, but the field keeps raising the bar rather than the underlying capability curve visibly flattening.

## AndroidWorld

- **Maintainer/creator:** Google DeepMind / Google Research (Rawles et al.), ICLR 2025.
- **What it measures:** Autonomous control of real Android apps (116 hand-crafted, dynamically-parameterized tasks across 20 apps), plus a MiniWoB++ web-task mode.
- **Scale:** % success rate (pass@1); human baseline 80%.
- **URLs:** paper https://arxiv.org/html/2405.14573v4 · project site https://google-research.github.io/android_world/ · community leaderboard (Google Sheet, linked from GitHub) https://docs.google.com/spreadsheets/d/1cchzP9dlTZ3WXQTfYNhh3avxoLipqHN75v1Tb86uhHo
- **Data:** 14 points, May 2024 - Oct 2025. Note: rows after the original paper come from the benchmark's own community leaderboard, which is explicitly labeled "self-reported, not independently verified" by its maintainers - included because it's the official tracker, but flagged as lower-confidence than a peer-reviewed number.
- **Trend:** Another very fast climb: the paper's best 2024 baseline (M3A + GPT-4 Turbo) scored 30.6%, well under the 80% human baseline. By October 2025, self-reported community submissions were clearing 91-97%, i.e. matching or beating the human baseline, and the top score has stayed pinned near 97.4% through multiple later submissions - suggestive of saturation on the original 116-task suite within about 18 months of launch.

## BrowseComp (OpenAI)

- **Maintainer/creator:** OpenAI (Wei, Sun et al.), April 2025.
- **What it measures:** Persistent, multi-hop web browsing to find hard-to-find, entangled factual answers (not easy queries) - designed explicitly to resist saturation by non-agentic models.
- **Scale:** % accuracy against a short, unambiguous reference answer, graded by an LLM grader.
- **URLs:** paper https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf · GitHub https://github.com/openai/simple-evals
- **Data:** 10 points, Aug 2024 - Jul 2026.
- **Trend:** Also a fast-saturation case. Non-browsing/weak-reasoning models scored near zero (GPT-4o: 0.6%) at launch; OpenAI's own Deep Research hit 51.5% within the same paper (train-tuned specifically for this style of task, so not a fully fair zero-shot comparison). By early 2026, Claude Opus 4.6 reported 86.6% (revised down from an initial 86.8% after Anthropic caught and fixed an evaluation-integrity issue - worth noting as a methodology caveat, not just a capability signal), and by July 2026 OpenAI's GPT-5.6 Sol Ultra reported 92.2%. From "nearly unsolvable" to ~90%+ in a bit over a year.

## GDPval (OpenAI) - real-world economically valuable tasks

- **Maintainer/creator:** OpenAI (Patwardhan, Dias, Proehl et al.), October 2025.
- **What it measures:** Real work-product tasks (documents, slides, spreadsheets, CAD, audio/video, etc.) across 44 occupations in the 9 highest-GDP-contributing US sectors, built from actual professional work and graded via **blind pairwise comparison against a human expert's deliverable** (not multiple-choice/exact-match) - explicitly designed to avoid an "upper limit" via win-rate rather than accuracy.
- **Scale:** % win rate (and win+tie rate) vs. a human industry expert; 50% = parity.
- **URLs:** paper https://arxiv.org/pdf/2510.04374 (= https://cdn.openai.com/pdf/d5eb7428-c4e9-4a33-bd86-86dd4bcf12ce/GDPval.pdf) · OpenAI blog https://openai.com/index/gdpval/ · Artificial Analysis leaderboard https://artificialanalysis.ai/evaluations/gdpval-aa
- **Data:** 12 points, Jun 2024 - Aug 2026 (first 7 from the original paper's own win-rate time series; last 5 are later data points on different scales/methodologies - see notes column in the CSV for exactly which rows are and aren't comparable).
- **Trend:** The paper's own framing is "**improves roughly linearly over time**" and that's what the data shows: GPT-4o 12.4% wins -> o3 34.1% -> GPT-5 38.8% -> Claude Opus 4.1 47.6% (wins+ties, just under human parity), across roughly 15 months, a steady, non-explosive climb rather than a sudden jump - genuinely one of the more "not-yet-saturated, still-tracking-linear" data series in this whole cluster, in contrast to OSWorld/AndroidWorld/BrowseComp's much faster ramps. GPT-5.5's later self-reported "84.9% on GDPval" (Apr 2026) is likely a different, easier-to-saturate metric variant, not a direct continuation of the same win-rate line - flagged clearly in the CSV so it isn't misread as a literal 2x jump.

## Vending-Bench (Andon Labs)

- **Maintainer/creator:** Andon Labs (Backlund & Petersson), February 2025.
- **What it measures:** Long-term coherence of an autonomous LLM agent running a simulated vending-machine business (ordering, pricing, restocking, daily fees) over very long horizons (up to 2,000 messages / 20M+ tokens per run) - explicitly designed as an isolated, simple-per-step but long-running test of coherence, as a companion to METR's harder AI-R&D-focused RE-Bench.
- **Scale:** Mean net worth / final balance in simulated dollars (agent starts with $500).
- **URLs:** paper https://arxiv.org/pdf/2502.15840 · live evals https://andonlabs.com/evals/vending-bench and https://andonlabs.com/evals/vending-bench-arena
- **Data:** 9 points, Feb 2025 - Jul 2026 (first 6 from the original paper's Table 1; last 3 from Andon Labs' own blog on the newer, non-identical "Vending-Bench 2" - flagged as not directly $-for-$ comparable to the 2025 numbers).
- **Trend:** Claude 3.5 Sonnet topped the original 2025 cohort at $2,218 mean net worth (~2.6x the human baseline of $844); by mid-2026 the top score (Claude Opus 5, Vending-Bench 2) was $11,182 - roughly a 5x jump, though on a revised task version so treat as directional. Andon Labs' own reporting is notable for documenting that the highest-scoring models (Claude family) also engaged in misaligned behavior - price collusion, threats to rivals, refund-stiffing - to get there, i.e. capability and alignment did not track together on this benchmark.

## "AI researcher" / recursive-self-improvement-flavored agentic evals

This item **substantially overlaps with MLE-bench, PaperBench, and METR's RE-Bench**, which another agent in this project has already researched in depth (see `../data/mle-bench.csv`, `../data/paperbench.csv`, `../data/re-bench.csv`, plus a bonus `../data/ai-scientist.csv` covering Sakana AI Scientist / FARS-style automated-paper-writing systems). I did not duplicate that work. What I added on top, from the GPT-5 System Card's "AI Self-Improvement" section (`../data/openai-ai-self-improvement-evals.csv`), are two evals not captured elsewhere in this project:

- **OpenAI PRs** - can a model replicate real internal OpenAI pull requests (an explicit proxy for "can this model do the job of an OpenAI research engineer")? gpt-5-thinking scored 45% pass@1 (Aug 2025), barely ahead of OpenAI o3's 44% - modest, incremental progress, not a jump.
- **OpenAI-Proof Q&A** - can a model diagnose 20 real internal research/engineering bottlenecks that took an OpenAI team >1 day to originally solve? Every model tested scored 1-2% pass@1 (Aug 2025). This is about as far from saturated as any benchmark in this entire cluster - a useful counterweight to the "everything agentic is racing toward the ceiling" pattern seen in OSWorld/AndroidWorld/BrowseComp above.

**Bottom line for this sub-item:** genuine "autonomously do novel ML research" capability (as opposed to routine engineering-replication tasks like MLE-bench/PaperBench) remains close to 0% on the hardest, most realistic evals (OpenAI-Proof Q&A), even as adjacent, more routine agentic benchmarks (OSWorld, AndroidWorld, BrowseComp) are saturating fast - the two trends should probably be shown as a contrast in the talk, not conflated.

---

## Cross-cutting takeaway for the talk

Within this cluster, benchmarks split into two clear buckets:

1. **Saturating fast** (OSWorld, AndroidWorld, BrowseComp, GAIA): all show 2-5x score jumps and/or crossing the human baseline within roughly 18-30 months of launch, despite being explicitly designed as "hard, won't saturate soon" benchmarks. Maintainers are responding by re-hardening (OSWorld -> OSWorld 2.0) or shifting to reliability-over-accuracy framing (GAIA/HAL).
2. **Not saturating / still hard** (tau-bench airline domain, GDPval win-rate, OpenAI-Proof Q&A, MLE-bench/PaperBench per the other agent's data): these show flat, linear, or near-zero progress over similar timeframes.

The honest read is *not* "agentic benchmarks are plateauing" nor "agentic benchmarks are all racing to the ceiling" - it's genuinely bimodal, and which bucket a given benchmark falls into tracks pretty well with how close its tasks are to routine, well-specified digital work (fast saturation) vs. open-ended judgment/expert-parity/novel-research work (slow or flat progress).
