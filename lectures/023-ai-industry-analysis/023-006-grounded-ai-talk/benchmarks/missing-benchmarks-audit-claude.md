# Missing-benchmarks audit

Research pass (2026-08-17) checking the 111-benchmark catalog in `README.md` against the wider AI-benchmark landscape: web search across game-playing/interactive environments, browser/computer-use/tool-use agents, safety/alignment/risk evals, instruction-following/long-context/coding, and domain-professional/organizational leaderboards. Five parallel research passes, one per category below.

Each entry: **name** — description — why it's distinct from what's already catalogued — source(s). Confidence/notability ranked within each category (real public leaderboard or frontier-lab citation > single-paper proposal).

## Structural findings

The existing catalog has zero representation in three entire categories that frontier labs actually publish and cite against:

- **Safety / alignment / catastrophic-risk** — the closest things catalogued are Cybench and ExploitBench, which are offensive-security *capability* evals, not safety/alignment evals.
- **Instruction-following** — nothing tests literal constraint-compliance (word counts, format rules, keyword inclusion).
- **Multilingual** — nothing outside English-centric benchmarks, despite Gemini's own technical report leaning on multilingual evals.

Also: the README's own "most popular benchmarks" section cites scores on **τ²-bench Telecom** and **MCP Atlas**, but neither has a data file/row in the catalog — a self-inconsistency worth fixing regardless of anything else below.

---

## 1. Games & interactive environments

Existing catalog coverage: Chess Puzzles (Epoch), Mystery Game Puzzles (Epoch), Balrog (NetHack), ARC-AGI-3.

| Benchmark | What it measures | Why distinct | Source |
| --- | --- | --- | --- |
| **Kaggle Game Arena** (Google DeepMind + Kaggle) | Live head-to-head leaderboard: frontier models play full adversarial Chess, Werewolf, and Poker against each other | Full adversarial gameplay across 3 named games with public rankings, vs. Epoch's single-position best-move (Chess Puzzles) or secret single-game (Mystery Game Puzzles) | [Kaggle](https://www.kaggle.com/game-arena) · [Google blog](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/kaggle-game-arena-updates/) |
| **PokéAgent Challenge** (NeurIPS 2025 competition → living benchmark) | Two tracks: competitive Pokémon battling (partial-observability opponent modeling) + RPG speedrunning (long-horizon agent orchestration) | Nothing in catalog covers Pokémon-style long-horizon RPG play | [pokeagent.github.io](https://pokeagent.github.io/) · [arXiv:2603.15563](https://arxiv.org/abs/2603.15563) |
| **TextArena** | 57+ competitive text-game environments (negotiation, deception, theory-of-mind), live public TrueSkill leaderboard, models play humans and each other | Broader and live-ranked vs. Balrog's fixed NetHack focus | [arXiv:2504.11442](https://arxiv.org/abs/2504.11442) · [textarena.ai](https://www.textarena.ai/) |
| **lmgame-Bench** (ICLR 2026) | Modular Gym-style harness across 6 popular video games, isolates perception/memory/reasoning, designed to resist contamination | Different design goal than Balrog | [arXiv:2505.15146](https://arxiv.org/abs/2505.15146) · [GitHub](https://github.com/lmgame-org/GamingAgent) |
| **VideoGameBench** | VLM benchmark on real Game Boy (via PyBoy) and MS-DOS games — live perception+control on actual retro binaries | Real game binaries, not a text abstraction | [GitHub](https://github.com/alexzhang13/videogamebench) |
| **Werewolf Arena** | Bidding-based turn-taking social-deduction framework for LLM deception/persuasion | Predates and is distinct from Kaggle Game Arena's Werewolf mode | [arXiv:2407.13943](https://arxiv.org/abs/2407.13943) |
| **DSGBench** | Multi-game "diverse strategic game" suite bundling several strategy games under one harness | — | [arXiv:2503.06047](https://arxiv.org/pdf/2503.06047) |
| **GameBench** | General strategic-reasoning eval across multiple novel/unseen games, chosen to avoid training-data contamination | — | [arXiv:2406.06613](https://arxiv.org/pdf/2406.06613) |

Lower-confidence / niche (single-paper, no real public leaderboard): PTCG-Bench (Pokémon TCG), Poker Arena (arXiv:2606.13815), PillagerBench (competitive multi-agent Minecraft), MC-Bench/MineBench (Minecraft build-quality, arguably out of scope), Game Reasoning Arena (arXiv:2508.03368), Triadic Werewolf/WOLF/Multicultural Spyfall (narrow theory-of-mind variants).

Not found: a formalized benchmark version of the "Claude/Gemini Plays Pokémon" livestreams distinct from PokéAgent Challenge, nor a maintained StarCraft II LLM leaderboard — these appear to be one-off stunts/papers, not catalogued benchmarks.

---

## 2. Web / computer-use / tool-use agents

Existing catalog coverage: GAIA, WebArena, AgentBench, tau-bench, OSWorld, AndroidWorld, BrowseComp, Vending-Bench, GDPval, TheAgentCompany, Terminal Bench, Cybench, ExploitBench, APEX Agents, DeepResearch Bench, Webdev Arena.

**Confirmed self-inconsistency in the current README** — both of these are cited with scores in the "most popular benchmarks" section but have no data file:

- **τ²-Bench (Telecom)** — Sierra's dual-control (agent + simulated user, both can act on shared environment) successor to tau-bench; 2,285 compositional tasks. Distinct from the already-catalogued single-control `tau-bench`. [GitHub](https://github.com/sierra-research/tau2-bench) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/tau2-bench)
- **MCP-Atlas** (Scale AI) — 1,000 tasks across 36 real MCP servers / 220 tools, tests tool discovery + multi-server workflows via claim-level scoring. Distinct from GAIA/AgentBench (MCP-protocol-specific). [arXiv:2602.00933](https://arxiv.org/abs/2602.00933) · [Scale leaderboard](https://labs.scale.com/leaderboard/mcp_atlas)

Other gaps, ranked:

| Benchmark | What it measures | Why distinct | Source |
| --- | --- | --- | --- |
| **Berkeley Function-Calling Leaderboard (BFCL, v1–v4)** | Standard tool/function-calling eval, executable + AST-based; v4 adds agentic eval | Nothing in catalog directly tests function-calling | [gorilla.cs.berkeley.edu](https://gorilla.cs.berkeley.edu/leaderboard.html) |
| **MultiChallenge** (Scale AI) | Multi-turn conversation: instruction retention, inference memory, versioned editing, self-coherence | Cited by Gemini 3 Pro/GPT-5.1 releases | [scale.com/research/multichallenge](https://scale.com/research/multichallenge) |
| **AppWorld** (ACL'24 Best Resource Paper) | 750 tasks, 9 simulated apps / 457 APIs, interactive-coding-agent benchmark | More complex environment than AgentBench | [GitHub](https://github.com/StonyBrookNLP/appworld) |
| **Online-Mind2Web** | Live re-evaluation of 300 tasks on 136 real high-traffic sites; found agents underperform 2024 baselines ("illusion of progress") | Distinct from static WebArena | [arXiv:2504.01382](https://arxiv.org/abs/2504.01382) |
| **VisualWebArena** | 910 tasks requiring visual/spatial page understanding | Extends WebArena (already catalogued) with a vision requirement | — |
| **Mind2Web / Mind2Web 2** | Foundational human-web-trace corpus + long-horizon agent-as-judge successor | — | — |
| **WebVoyager** | Live-web benchmark across 15 real sites | Useful contrast point — its ~90% scores collapse under Online-Mind2Web's harder live setting | — |
| **SPA-Bench** (ICLR'25 Spotlight) | Smartphone-agent benchmark, 340 tasks / 66 apps, English+Chinese, cross-app tasks | More comprehensive second mobile-agent entry vs. AndroidWorld | — |

Lower priority: ToolBench and API-Bank (2023-era, largely superseded by BFCL in citation frequency). No independent evidence found of a distinct "Nexus Function Calling" leaderboard beyond BFCL derivatives.

---

## 3. Safety, alignment, red-teaming, catastrophic risk

**Currently a total blank in the catalog.** Cybench/ExploitBench are offensive-security capability evals, not safety/alignment evals; TruthfulQA is about misconceptions, not safety.

**Catastrophic risk (bio/chem/cyber uplift)**

| Benchmark | What it measures | Source |
| --- | --- | --- |
| **WMDP** (Weapons of Mass Destruction Proxy) | 3,668 MCQ proxy for hazardous bio/cyber/chem knowledge; built by CAIS + UC Berkeley/MIT as both a hazard eval and an unlearning benchmark; directly cited in frontier bio-risk eval sections | [arXiv:2403.03218](https://arxiv.org/abs/2403.03218) · [CAIS](https://safe.ai/blog/wmdp-benchmark) |
| **Bio/cyber "uplift" trials** | Not one fixed benchmark — OpenAI and Anthropic both run bespoke red-team uplift studies referenced in every recent system card; SecureBio tracks these across labs | [SecureBio tracker](https://securebio.org/benchmarks/models/) · [Epoch AI critique](https://epoch.ai/gradient-updates/do-the-biorisk-evaluations-of-ai-labs-actually-measure-the-risk-of-developing-bioweapons) |
| **UK AISI Inspect Evals / Inspect Cyber** | Open-source eval framework + canonical eval packages (cyber, bio, autonomy, agentic CTF) UK AISI runs against frontier models pre-release — increasingly the toolchain labs coordinate through | [AISI blog](https://www.aisi.gov.uk/blog/inspect-cyber) · [inspect.cyber.aisi.org.uk](https://inspect.cyber.aisi.org.uk/) |

**Red-teaming / jailbreak / harm**

| Benchmark | What it measures | Source |
| --- | --- | --- |
| **HarmBench** | Standardized red-teaming benchmark, 400 harmful behaviors × 7 categories, Attack Success Rate metric, 18-method attack panel | [arXiv:2509.19100](https://arxiv.org/pdf/2509.19100) |
| **JailbreakBench** | Maintained leaderboard + JBB-Behaviors dataset (100 behaviors), tracks ASR for attacks and defenses over time | [jailbreakbench.github.io](https://jailbreakbench.github.io/) · [GitHub](https://github.com/JailbreakBench/jailbreakbench) |
| **AgentHarm** (ICLR 2025) | Extends harm evaluation to tool-using agents: 110 unique / 330 augmented multi-step agentic harm behaviors across 11 categories, 104 tools | [ICLR paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/c493d23af93118975cdbc32cbe7323f5-Paper-Conference.pdf) |
| StrongREJECT, AIR-Bench, SafetyBench, Do-Not-Answer | Real but second-tier — found only in aggregator roundups this pass, not independently verified with primary sources | lower priority |

**Honesty / scheming / deception**

| Benchmark | What it measures | Source |
| --- | --- | --- |
| **MASK** (Center for AI Safety + Scale AI) | Disentangles honesty from factual accuracy — tests whether models contradict their own stated beliefs under pressure to lie; frontier models score 20–60% lie rate despite high TruthfulQA scores (notable contrast to catalog's existing TruthfulQA entry) | [arXiv:2503.03750](https://arxiv.org/pdf/2503.03750) · [GitHub](https://github.com/centerforaisafety/mask) |
| **Apollo Research scheming/deception evals** | Not a single fixed public benchmark — active published research line (in-context scheming, alignment faking, oversight-gaming), increasingly referenced in frontier system cards | [MATS program page](https://www.matsprogram.org/stream/apollo) |

**Bias/toxicity** (established, but pre-2023 vintage, rarely cited in current frontier releases)

- **BBQ** — hand-built QA bias benchmark across protected-class social groups; folded into HELM Safety.
- **ToxiGen** — 274K machine-generated toxic/benign statements re: 13 minority groups.
- **RealToxicityPrompts** — naturally-occurring prompts probing toxic completion tendencies.

**Broad safety leaderboards**

| Benchmark | What it measures | Source |
| --- | --- | --- |
| **MLCommons AILuminate** | First cross-industry (OpenAI/Anthropic/Google et al. participated in the working group) standardized chat-safety benchmark, 12 hazard categories, 24K+ prompts, public graded leaderboard — the closest thing to an industry-consensus safety leaderboard | [MLCommons](https://mlcommons.org/ailuminate/) · [arXiv:2503.05731](https://arxiv.org/abs/2503.05731) · [GitHub](https://github.com/mlcommons/ailuminate) |
| **Stanford HELM Safety** | Aggregates BBQ + others into a 6-risk-category composite (violence, fraud, discrimination, sexual content, harassment, deception) | not independently re-verified with a primary URL this pass |

**Citation relevance:** WMDP-style uplift evals and UK AISI Inspect evaluations are the ones actually named in OpenAI/Anthropic/Google system cards. AILuminate is the closest to a cross-lab standardized public leaderboard. HarmBench/JailbreakBench/AgentHarm/MASK are academic-standard but not consistently cited in lab release posts — still worth a dedicated "safety/alignment" catalog section given the current zero coverage.

---

## 4. Instruction-following, long-context, coding/data, embeddings

**Instruction-following** — currently zero coverage; nothing in the catalog tests literal constraint-compliance.

| Benchmark | What it measures | Source |
| --- | --- | --- |
| **IFEval** | ~500 prompts with verifiable, auto-checkable constraints (word counts, keyword inclusion, format rules); part of HF Open LLM Leaderboard v2 | [google/IFEval](https://huggingface.co/datasets/google/IFEval) · [arXiv:2311.07911](https://arxiv.org/abs/2311.07911) |
| **IFBench** | Harder, contamination-resistant IFEval successor; tracked live on Artificial Analysis | [Artificial Analysis](https://artificialanalysis.ai/evaluations/ifbench) |
| **FollowBench** | Multi-level constraint-following (Content/Situation/Style/Format/Example), incrementally stacks constraints to find the failure point | [GitHub](https://github.com/YJiangcm/FollowBench) · [ACL 2024](https://aclanthology.org/2024.acl-long.257/) |
| **InfoBench** | 72-domain instruction decomposition into boolean sub-questions for LLM-judge scoring | — |

**Long-context** — currently zero coverage.

| Benchmark | What it measures | Source |
| --- | --- | --- |
| **RULER** (NVIDIA) | 13 synthetic tasks (multi-needle retrieval, variable tracing, multi-hop QA) up to 128K+ tokens; built to expose the gap between claimed and effective context length | [GitHub](https://github.com/NVIDIA/RULER) |
| **LongBench v2** | 503 MC questions, 8K–2M words, real-world multitask long-context reasoning (not synthetic retrieval) | — |
| **Needle-in-a-Haystack (NIAH-2)** | Canonical single/multi-needle retrieval smoke test; by 2026 considered a baseline sanity check rather than discriminating on its own | — |
| **InfiniteBench**, **BABILong** | Additional synthetic long-context suites, actively maintained as a cluster alongside LongBench v2/NIAH | — |
| **MRCR v2** (Multi-Round Context Retrieval) | Anthropic-aligned long-context eval, worth a look if pursuing this cluster further | — |

**Text-to-SQL / data-science coding**

| Benchmark | What it measures | Source |
| --- | --- | --- |
| **Spider 2.0** | 632 real enterprise text-to-SQL workflows (BigQuery/Snowflake/DuckDB/Postgres); active leaderboard. **Caveat:** a 2026 VLDB/CIDR paper found a 66.1% annotation-error rate in the Spider2-Snow subset — flag as data-quality caveat if added | [GitHub](https://github.com/xlang-ai/Spider2) |
| **BIRD-SQL** | 12,751 question/SQL pairs, 95 databases, 37 domains; standard cross-domain text-to-SQL benchmark, usually reported alongside Spider | — |
| **DS-1000** | 1,000 realistic data-science coding problems (NumPy/Pandas/SciPy/sklearn/PyTorch/TF/Matplotlib) from StackOverflow, deliberately perturbed to resist memorization | [ds1000-code-gen.github.io](https://ds1000-code-gen.github.io/) · [arXiv:2211.11501](https://arxiv.org/abs/2211.11501) |

**Additional coding benchmarks**

| Benchmark | What it measures | Source |
| --- | --- | --- |
| **BigCodeBench** | Diverse function-calls + complex multi-step instructions, harder/broader than HumanEval; active leaderboard | [GitHub](https://github.com/bigcode-project/bigcodebench) |
| **EvalPlus** | Rigor upgrade to HumanEval/MBPP via massively expanded auto-generated test cases — check for overlap with the MBPP+ variant already in `mbpp.csv` before adding | [Leaderboard](https://evalplus.github.io/leaderboard.html) |
| ClassEval, RepoBench, Multi-SWE-bench, CodeElo | Referenced in surrounding literature but not independently verified with a live leaderboard this pass | lower priority |

**Embeddings/retrieval** (out-of-category — a different capability axis, embedding models rather than generative LLMs; recommend a new top-level section if included at all)

- **MTEB** — 8 task types, 58 datasets, 112 languages, the standard embedding-model benchmark; active HF leaderboard + "MTEB Arena." [arXiv:2210.07316](https://arxiv.org/abs/2210.07316)
- BEIR — not independently re-verified this pass (largely superseded/absorbed by MTEB's retrieval tasks).

---

## 5. Domain-professional & organizational leaderboards

**Domain-professional** — currently zero coverage (no medicine/law/finance).

| Benchmark | Domain | What it measures | Source | Lab-cited? |
| --- | --- | --- | --- | --- |
| **HealthBench** | Medical | 5,000 realistic clinician-conversation scenarios, 48,562 physician-written rubric criteria; OpenAI's own eval | [OpenAI](https://openai.com/index/introducing-gpt-5/) | Yes — OpenAI GPT-5/system cards |
| **MedXpertQA** | Medical | 4,460 expert-level questions across 17 specialties, text + multimodal; built because MedQA saturated | [arXiv:2501.18362](https://arxiv.org/pdf/2501.18362) · [GitHub](https://github.com/TsinghuaC3I/MedXpertQA) | Increasingly, as MedQA saturates |
| **MedQA** | Medical | USMLE-style multiple-choice; now widely regarded as saturated | [llm-stats](https://llm-stats.com/benchmarks/medxpertqa) | Historically yes, now retired-ish |
| **LegalBench** | Legal | 162 crowd-built legal-reasoning tasks (issue-spotting, rule-recall, rule-application), live leaderboard | [arXiv:2308.11462](https://arxiv.org/abs/2308.11462) · [Vals AI leaderboard](https://www.vals.ai/benchmarks/legal_bench) | Cited via Vals AI's independent tracking |
| **CaseHOLD** | Legal | 53,000+ MC questions identifying legal holdings from real US case law | part of LegalBench suite | Academic, not lab-cited directly |
| **FinBen** | Finance | Holistic financial-LLM benchmark, 8-axis taxonomy (NeurIPS 2024 D&B track) | [arXiv:2402.12659](https://arxiv.org/pdf/2402.12659) · [GitHub](https://github.com/The-FinAI/FinBen) | Not directly by frontier labs |
| **FinQA** | Finance | Numerical reasoning over financial reports/tables | folded into FinBen | No |
| **Vals Index / Vals AI leaderboards** | Legal/finance/tax/coding | Independent third-party leaderboard combining Finance Agent v2, CorpFin v2, SWE-bench, Terminal-Bench 2.1 | [Vals AI](https://www.vals.ai/product) | Aggregator, tracks frontier models |

**Organizational/leaderboard-level gaps**

| Org / suite | What's notable | Source |
| --- | --- | --- |
| **Stanford HELM** (CRFM) | Open framework spanning 16 scenarios × 7 axes (accuracy, robustness, fairness, bias, toxicity, efficiency, calibration); wraps MMLU-Pro/GPQA/IFEval so mostly not new data, but has unique satellite suites not in this catalog: **MedHELM** (clinical), **VHELM** (vision), **HEIM** (text-to-image), **AIR-Bench** (safety) | [GitHub](https://github.com/stanford-crfm/helm) · [HELM Lite](https://crfm.stanford.edu/helm/lite/latest/) · [MedHELM](https://crfm.stanford.edu/helm/medhelm/latest/) |
| **Scale AI SEAL Leaderboards** | Private, expert-curated, pairwise-graded evals across coding/instruction-following/math/multilingual — can't be gamed since datasets stay unpublished; includes **PRBench** (Professional Reasoning Bench, incl. legal). A genuinely distinct provenance category (private-eval) absent from this catalog entirely | [Scale blog](https://scale.com/blog/leaderboard) · [PRBench-Legal](https://labs.scale.com/leaderboard/prbench-legal) |
| **AI2 (Allen Institute)** | **AstaBench** (ICLR 2026 oral) — grounded scientific-research-agent benchmark, 4 categories (lit search, code, data analysis, end-to-end discovery), closest thing to a "real AI-scientist" eval outside Sakana's. Also runs **IFBench**. | [AstaBench](https://allenai.org/blog/astabench-update-spring-2026) |
| **Multilingual** | **Global-MMLU** (Cohere/EleutherAI-backed, 42 languages, human+machine translated; Gemini 3.1 Pro cited at 93.2%), **Belebele** (Meta, 122-language reading comprehension on FLORES-200 passages), **FLORES-200** (low-resource MT eval, used in Gemini's own technical report) — a real, lab-cited hole: catalog has zero multilingual coverage | [Cohere](https://cohere.com/research/globalmmlu) · [Gemini technical report](https://arxiv.org/pdf/2312.11805) |

---

## Bottom-line priority list

If adding a prioritized subset (real public leaderboard or frontier-lab citation, not just an academic proposal):

1. **τ²-Bench (Telecom)** and **MCP-Atlas** — fixes an existing self-inconsistency in the README
2. **IFEval** / **IFBench** — instruction-following, currently zero coverage
3. **WMDP**, **MLCommons AILuminate**, **HarmBench**, **AgentHarm**, **MASK** — safety/alignment, currently zero coverage
4. **RULER**, **LongBench v2** — long-context, currently zero coverage
5. **Global-MMLU**, **Belebele** — multilingual, currently zero coverage
6. **HealthBench**, **LegalBench** (via Vals AI), **FinBen** — domain-professional, currently zero coverage
7. **BFCL** — function-calling, currently zero coverage
8. **Kaggle Game Arena**, **PokéAgent Challenge**, **TextArena** — games, rounds out existing category
9. **Spider 2.0** / **BIRD-SQL**, **BigCodeBench** — coding/data, rounds out existing category
10. **Scale AI SEAL** — worth a mention in the aggregators section as a distinct private-eval provenance category, alongside Epoch/Artificial Analysis/LMArena
