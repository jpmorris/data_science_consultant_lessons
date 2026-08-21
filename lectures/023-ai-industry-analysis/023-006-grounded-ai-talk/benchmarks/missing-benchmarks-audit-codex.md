# Missing AI benchmarks: web audit

Audit date: 2026-08-17

## Executive finding

The catalog is broad for headline language-model capability benchmarks, but it is not yet comprehensive. Its largest substantive gaps are **browser/computer-use agents**, **tool/API agents**, **games and embodied agents**, **scientific agents**, and whole model-quality domains such as **safety, multilinguality, long context, audio, medicine, and law**.

This audit treats a benchmark as a strong addition when it has a primary paper or official repository, a reproducible task set or evaluation harness, and results for multiple systems. It distinguishes benchmarks from frameworks, datasets without a comparative evaluation, and one-off demonstrations. Names were checked case-insensitively against the files under `benchmarks/`; benchmark components mentioned only in prose (for example, Mind2Web as an AgentBench environment) still count as missing standalone series.

## Priority 1: clear omissions that fit the existing catalog

These have direct relevance to frontier-model progress and generally have public evaluation code, reported multi-model results, or a leaderboard.

| Benchmark | What it adds beyond the current catalog | Primary source | Collection recommendation |
| --- | --- | --- | --- |
| WorkArena / WorkArena++ | Enterprise browser work in ServiceNow; WorkArena++ adds 682 compositional planning tasks rather than WebArena's consumer/community sites | [Official repository](https://github.com/ServiceNow/WorkArena), [paper](https://arxiv.org/abs/2403.07718) | Add separate L1 and ++ series; do not merge their success rates |
| VisualWebArena | 910 visually grounded tasks on realistic sites; materially different from text/DOM-centric WebArena | [Paper](https://arxiv.org/abs/2401.13649), [official project](https://jykoh.com/vwa) | Add task-success series |
| Online-Mind2Web | Live-web successor to the static 2,000-task Mind2Web dataset; maintained as sites change | [Official repository](https://github.com/OSU-NLP-Group/Online-Mind2Web) | Prefer the online benchmark over static element-selection scores for frontier trend tracking |
| WebVoyager | End-to-end interaction on live popular websites using visual and textual observations | [Paper](https://arxiv.org/abs/2401.13919), [official repository](https://github.com/MinorJerry/WebVoyager) | Add, but record evaluator type: human vs LLM-judge results are not interchangeable |
| WebBench | Large live-web READ/WRITE benchmark spanning hundreds of sites; includes authentication, downloads, and state-changing actions | [Official repository](https://github.com/Halluminate/WebBench) | Split READ and WRITE if both have enough comparable results |
| AssistantBench | Long, realistic live-web research/assistant tasks requiring planning, retrieval, and synthesis | [Paper](https://aclanthology.org/2024.emnlp-main.1113/), [official data](https://huggingface.co/datasets/AssistantBench/AssistantBench) | Add overall accuracy/reward; note live-web drift |
| Windows Agent Arena | Windows-specific multimodal desktop control across real applications, complementary to cross-platform OSWorld | [Official Microsoft repository](https://github.com/microsoft/WindowsAgentArena) | Add normal and hard modes separately |
| AppWorld | 750 executable tasks across simulated everyday apps, evaluated from resulting application state rather than an LLM judge | [Official site and leaderboard](https://appworld.dev/), [paper](https://aclanthology.org/2024.acl-long.850/) | High priority; add task-goal completion and scenario-goal completion as distinct units |
| AppWorld-UL | User-in-the-loop version testing clarification, confirmation, and infeasible requests | [Official site](https://appworld.dev/appworld-ul/) | Add separately from autonomous AppWorld |
| Berkeley Function Calling Leaderboard (BFCL) | Function/tool calling, including multi-turn, live APIs, hallucination, memory, and agentic web search | [Official UC Berkeley leaderboard](https://gorilla.cs.berkeley.edu/leaderboard) | Add versioned series; BFCL v1-v4 scores are not one continuous metric |
| AstaBench | Scientific-agent literature search, synthesis, and research tasks with trace/cost reporting | [Official Allen Institute for AI site](https://allenai.org/asta/bench) | High priority for the catalog's AI-scientist theme |
| AIRS-Bench | End-to-end AI research-science work by agents, with an official multi-agent leaderboard | [Official Meta repository](https://github.com/facebookresearch/airs-bench) | Add alongside RE-Bench, PaperBench, and MLE-bench; do not treat as an alias |
| LMGame-Bench | Standardized visual game-playing by bare VLMs and scaffolded computer-use gaming agents | [Official repository and leaderboard](https://github.com/lmgame-org/GamingAgent) | Strong game addition; keep bare-model and agentic scores separate |
| ORAK | Diverse video-game benchmark designed specifically for LLM agents, with configurable games, observations, and agent modules | [Paper](https://arxiv.org/abs/2506.03610), [official repository](https://github.com/krafton-ai/ORAK) | Add normalized aggregate plus per-game results if available |
| GAMA-Bench | Multi-agent strategic/social/economic games (auction, bargaining, battle, and others) | [Official repository and leaderboard](https://github.com/CUHK-ARISE/GAMABench) | Add; this covers strategic interaction absent from BALROG |
| GAMEBoT | Direct competition across games to expose planning/reasoning behavior | [Official repository](https://github.com/Visual-AI/GAMEBoT) | Add if the published leaderboard contains enough stable model/date points |
| GameDevBench | 333 agentic game-development tasks combining codebase work with shaders, sprites, animation, and visual scene validation | [Official repository and leaderboard](https://github.com/waynchi/gamedevbench) | Add under multimodal software engineering, not game playing |
| Roblox Open Game Eval | Executable game-development and debugging tasks with a maintained multi-model leaderboard | [Official Roblox repository](https://github.com/Roblox/open-game-eval) | Add; retain eval-set version and pass@k in every row |

## Priority 2: important coverage gaps

These benchmark families are essentially absent from the catalog. Before claiming “comprehensive,” at least a representative subset should be added.

| Family | Representative benchmarks to investigate | Why it matters |
| --- | --- | --- |
| Agent safety and robustness | [AgentDojo](https://github.com/ethz-spylab/agentdojo), [AgentHarm](https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/agentharm), [SafeAgentBench](https://github.com/shengyin1224/SafeAgentBench), [HarmBench](https://github.com/centerforaisafety/HarmBench) | Current catalog measures offensive cyber capability but almost no refusal, prompt-injection resistance, unsafe tool use, or hazardous embodied behavior |
| Enterprise agents | [CRMArena / CRMArena-Pro](https://github.com/SalesforceAIResearch/CRMArena) | Adds professional CRM work, business-process knowledge, confidentiality, and multi-turn interactions |
| Tool-use suites | ToolBench, API-Bank, ToolTalk, APIBench | `tau-bench` covers policy-aware customer service, but not broad API selection/calling; BFCL should be the first addition |
| Embodied/robotics | ALFWorld, ScienceWorld, VirtualHome, Habitat/BEHAVIOR, RoboCasa, EMMOE | The catalog has computer-use but almost no physical-world planning or manipulation. AgentBench contains ALFWorld, but that does not replace its standalone series |
| Multi-agent/social reasoning | AgentVerse-style suites, SOTOPIA, Diplomacy/Hanabi benchmarks | Current game coverage is mostly single-agent; coordination, negotiation, deception, and theory of mind are different capabilities |
| Long context and memory | LongBench, LongBench v2, RULER, InfiniteBench, LoCoMo, BABILong | FictionLiveBench alone does not cover retrieval, multi-hop reasoning, long-session memory, or effective context length |
| Multilingual and cultural | Global-MMLU, INCLUDE, Belebele, MGSM, MMLU-redux multilingual variants | The present list is overwhelmingly English and can misstate global capability progress |
| Safety, bias, and truthfulness | SafetyBench, BBQ, BOLD, RealToxicityPrompts, XSTest, StrongREJECT | TruthfulQA is not a general safety or fairness evaluation |
| Medicine and biology | MedQA, PubMedQA, MultiMedQA, HealthBench, LAB-Bench | GPQA/HLE science questions do not measure clinical reasoning, biomedical research, or safety in health advice |
| Law and finance | LegalBench, LawBench, FinanceBench | AGIEval exam items are not a substitute for professional-domain workflows and document reasoning |
| Audio and speech | AudioBench, MMAU, SpeechBench, VoiceBench | The multimodal section is almost entirely vision/video |
| Search/research agents | SearchBench, FreshQA, FRAMES, BrowseComp variants | BrowseComp and DeepResearch Bench are a good start, but research quality, citation correctness, and freshness need separate measures |
| Cyber defense and secure coding | CyberSecEval, InterCode-CTF, SecCodePLT/secure-code benchmarks | CyBench and ExploitBench emphasize offensive success; they do not measure secure generation or defensive work |

## Priority 3: classic game/RL benchmarks — include only if scope expands

The catalog currently reads as a benchmark history of frontier foundation models and agents, not all artificial intelligence. Under that scope it is reasonable to omit classic reinforcement-learning testbeds. If “AI benchmarks” is meant literally, however, these are major omissions:

- **Arcade Learning Environment (Atari 2600)** — the canonical deep-RL game suite.
- **Procgen** — 16 procedurally generated games explicitly measuring generalization to unseen levels; see the [official release](https://openai.com/index/procgen-benchmark/).
- **NetHack Learning Environment** — long-horizon exploration and planning in NetHack; BALROG uses NetHack but does not capture the historical RL leaderboard.
- **MineRL / MineDojo / Minecraft Universe** — open-ended Minecraft learning and generalist-agent evaluation.
- **Crafter** — survival, exploration, and technology-tree progress with compact, interpretable achievement metrics.
- **General Video Game AI (GVGAI), Obstacle Tower, DeepMind Lab, DMLab-30, Habitat, BabyAI, TextWorld, Jericho, and ScienceWorld**.

Recommendation: add a catalog-level `scope` statement. If the aim is *frontier foundation-model capability*, include newer LLM/VLM game benchmarks (LMGame-Bench, ORAK, GAMA-Bench) and leave classic RL suites in a separate historical appendix. Mixing Atari scores with LLM benchmark trends would not support the catalog's plateau/saturation question without a separate methodology.

## Things that should not be counted as missing standalone benchmarks

- **BrowserGym** and **AgentLab** are evaluation environments/frameworks that unify WebArena, WorkArena, VisualWebArena, AssistantBench, MiniWoB, and other suites. Add their constituent benchmarks, not a “BrowserGym score.” See the [BrowserGym paper](https://arxiv.org/abs/2412.05467) and [AgentLab repository](https://github.com/ServiceNow/AgentLab).
- **Inspect** is an evaluation framework/catalog, not a benchmark. Its [official site](https://inspect.aisi.org.uk/) is nevertheless a useful discovery source with implementations of hundreds of evals.
- **METR Hawk** is infrastructure; METR Time Horizon and RE-Bench are the benchmark outputs and are already present.
- A paper that only evaluates an agent on WebArena/OSWorld does not create a new benchmark.

## Recommended next collection pass

Start with a compact, high-value batch rather than importing dozens of low-signal datasets:

1. Browser/computer: WorkArena++, VisualWebArena, Online-Mind2Web, WebVoyager, Windows Agent Arena.
2. Tool/work: AppWorld, BFCL, CRMArena-Pro.
3. Games: LMGame-Bench, ORAK, GAMA-Bench.
4. Research: AstaBench and AIRS-Bench.
5. Safety: AgentDojo and AgentHarm.
6. Add one representative each for long context, multilingual, medicine, and audio after deciding whether the catalog is intended to cover model quality broadly or primarily frontier autonomy.

For every live or agentic benchmark, store not only `date, model, score` but also the **benchmark version/snapshot, agent scaffold, step/token/time budget, observation mode, evaluator type, number of trials, and cost**. Those variables now change results enough that model-only trend lines can be misleading.

## Bottom line

The catalog is comprehensive for the benchmark families it already emphasizes, but the claim should currently be “111 benchmark series focused on general reasoning, coding, frontier autonomy, and vision,” not “all AI benchmarks.” The browser and game gaps are real. A first expansion of roughly **15–20 series** from Priority 1 would materially improve coverage without turning the project into an uncurated benchmark directory.
