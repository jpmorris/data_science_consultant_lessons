I now have comprehensive data. Let me compile the full, organized report.

---

## Comprehensive Audit: Notable AI Benchmarks/Evals Missing from Your Catalog

Below are **70+ candidates** organized by category. Each is verified as NOT present in your 111-item catalog (including cross-checking for renamed/variant forms). I've filtered for significance — prioritizing those actively used to evaluate frontier LLMs as of 2024–2026.

---

## 🔬 SCIENCE & DOMAIN KNOWLEDGE

### 1. **MedQA / MedQA-USMLE**
- **Description:** Multiple-choice questions from US medical licensing exams (USMLE) testing clinical reasoning and medical knowledge.
- **Source:** Ke et al. (2021); widely used by OpenAI, Google for GPT-4/Gemini medical evaluations
- **URL:** https://github.com/jind11/MedQA
- **Year:** 2021; heavily used 2023–2026

### 2. **MedMCQA**
- **Description:** Multiple-choice QA from Indian medical entrance exams (AIIMS/NEET-PG), 194k questions across 21 subjects.
- **Source:** Pali et al., arXiv:2203.14371
- **URL:** https://medmcqa.github.io/
- **Year:** 2022

### 3. **PubMedQA**
- **Description:** Biomedical research question answering requiring yes/no/maybe answers from PubMed abstracts.
- **Source:** Jin et al., EMNLP 2019; widely used in medical LLM evals
- **URL:** https://pubmedqa.github.io/
- **Year:** 2019

### 4. **SciEval**
- **Description:** Multi-level LLM evaluation across chemistry, physics, and biology using Bloom's taxonomy (knowledge → research); includes dynamic questions to combat contamination. ~18,000 questions.
- **Source:** OpenDFM / AAAI 2024; arXiv:2308.13149
- **URL:** https://github.com/OpenDFM/SciEval
- **Year:** 2023/2024

### 5. **ChemBench**
- **Description:** Automated framework for benchmarking LLM chemical knowledge and reasoning; leading LLMs now sometimes outperform expert chemists on specific tasks.
- **Source:** LamaLab (Nature Chemistry 2025); arXiv ~2024
- **URL:** https://lamalab-org.github.io/chembench/
- **Year:** 2024

### 6. **OlympiadBench**
- **Description:** Bilingual (Chinese/English) math and science olympiad problems at competition level, used to test frontier reasoning.
- **Source:** He et al., ACL 2024; arXiv:2402.14008
- **URL:** https://github.com/OpenBMB/OlympiadBench
- **Year:** 2024

---

## 📐 MATH (ADDITIONAL NOTABLE ONES)

### 7. **MathArena**
- **Description:** Real-time, contamination-free evaluation platform using freshly released competition math (AIME, HMMT, USAMO, Putnam, IMO) — tests models only on problems released after their training cutoff. Includes both final-answer and full proof grading.
- **Source:** ETH Zurich / INSAIT; matharena.ai
- **URL:** https://matharena.ai/
- **Year:** 2024–ongoing

### 8. **MuSR (Multistep Soft Reasoning)**
- **Description:** Algorithmically-generated tasks (murder mysteries, object placements, team allocations) requiring multi-step reasoning over 1000+ word contexts. Part of HuggingFace Open LLM Leaderboard v2.
- **Source:** Sprague et al., arXiv:2310.16049; HuggingFace (2024)
- **URL:** https://arxiv.org/abs/2310.16049
- **Year:** 2023/2024

---

## 💻 CODING (ADDITIONAL NOTABLE ONES)

### 9. **EvalPlus / HumanEval+**
- **Description:** Rigorous extension of HumanEval and MBPP with 80× more test cases per problem to catch subtle code bugs; also includes EvalPerf for code efficiency.
- **Source:** Liu et al., NeurIPS 2023; evalplus.github.io
- **URL:** https://evalplus.github.io/
- **Year:** 2023

### 10. **APPS (Automated Programming Progress Standard)**
- **Description:** 10,000 Python programming problems at introductory through competition level with test-case-based evaluation; one of the first large competitive coding benchmarks for LLMs.
- **Source:** Hendrycks et al., NeurIPS 2021
- **URL:** https://github.com/hendrycks/apps
- **Year:** 2021

### 11. **CodeContests**
- **Description:** Competitive programming dataset from Codeforces, AtCoder, CodeChef with hard problems; used in AlphaCode evaluations. Strict test case validation.
- **Source:** DeepMind / Li et al., Science 2022
- **URL:** https://github.com/google-deepmind/code_contests
- **Year:** 2022

### 12. **CodeElo**
- **Description:** LLM competitive programming benchmark using real Codeforces problems; generates human-comparable Elo ratings by submitting to the actual platform judge.
- **Source:** Quan et al., arXiv:2501.01257 (2025)
- **URL:** https://arxiv.org/abs/2501.01257
- **Year:** 2025

---

## 🌐 WEB / BROWSER / GUI AGENT BENCHMARKS

### 13. **Mind2Web**
- **Description:** First large-scale dataset for generalist web agents on real websites across 137 websites and 2,000+ tasks; evaluates element identification and action prediction on live web pages.
- **Source:** Deng et al., NeurIPS 2023 (Ohio State)
- **URL:** https://osu-nlp-group.github.io/Mind2Web/
- **Year:** 2023

### 14. **WebVoyager**
- **Description:** End-to-end multimodal web agent benchmark; 643 real-world tasks across 15 websites (Amazon, GitHub, Google Maps, ESPN, etc.) with GPT-4V + human judge evaluation.
- **Source:** He et al., ACL 2024; arXiv:2401.13919
- **URL:** https://arxiv.org/abs/2401.13919
- **Year:** 2024

### 15. **WorkArena / WorkArena++**
- **Description:** Enterprise web-agent benchmark using ServiceNow platform; 33 tasks (v1) or 682 compositional tasks (v2/++) representing realistic knowledge-worker workflows.
- **Source:** ServiceNow Research / Drouin et al., ICML 2024; arXiv:2403.07718
- **URL:** https://github.com/ServiceNow/WorkArena
- **Year:** 2024

### 16. **AssistGUI**
- **Description:** Desktop GUI automation benchmark (Windows); 100 tasks in productivity software (After Effects, MS Word) requiring mouse/keyboard control via screenshots; CVPR 2024.
- **Source:** Gao et al., CVPR 2024
- **URL:** https://showlab.github.io/assistgui/
- **Year:** 2024

### 17. **MiniWoB++**
- **Description:** Mini World of Bits: web interaction benchmark with 100+ tasks in simulated browser environments; foundational agentic web-use evaluation.
- **Source:** Shi et al., OpenAI / Stanford 2017; Liu et al. 2018 (++)
- **URL:** https://miniwob.farama.org/
- **Year:** 2017/2018 (foundational; still widely cited)

### 18. **BrowserArena**
- **Description:** LLM-agent browser benchmark testing real-world web navigation across a wide range of live tasks; addresses contamination by using dynamically generated tasks.
- **Source:** arXiv:2510.02418 (2025)
- **URL:** https://arxiv.org/abs/2510.02418
- **Year:** 2025

---

## 🎮 GAME-PLAYING BENCHMARKS

### 19. **lmgame-Bench**
- **Description:** Unified LLM/VLM evaluation across 6 real video games (Super Mario Bros., Sokoban, Tetris, 2048, Candy Crush, Ace Attorney); modularizes perception, memory, and reasoning.
- **Source:** ICLR 2026; arXiv:2505.15146
- **URL:** https://github.com/lmgame-org/GamingAgent
- **Year:** 2025

### 20. **GAMEBoT**
- **Description:** Evaluates LLM reasoning using modular sub-problems from 8 competitive games (deduction, planning, head-to-head); 17 LLMs benchmarked with chain-of-thought.
- **Source:** ACL 2025 (Anthology: 2025.acl-long.378)
- **URL:** https://aclanthology.org/2025.acl-long.378/
- **Year:** 2025

### 21. **Werewolf Arena / Werewolf Benchmark**
- **Description:** Social deduction game benchmark using Werewolf/Mafia; evaluates LLMs on deception, persuasion, theory of mind, and coalition reasoning. Google Research (2024) + follow-up 2025 work.
- **Source:** Google Research; arXiv:2407.13943 (2024)
- **URL:** https://arxiv.org/abs/2407.13943
- **Year:** 2024

### 22. **LLM-Hanabi**
- **Description:** Cooperative card game benchmark testing theory-of-mind and collaborative rationale inference among multiple LLM agents in the Hanabi card game. EMNLP 2025.
- **Source:** HKUST-KnowComp; arXiv:2510.04980 / EMNLP 2025
- **URL:** https://arxiv.org/abs/2510.04980
- **Year:** 2025

### 23. **GameBench**
- **Description:** Strategic reasoning benchmark across 9 social/strategy games (Codenames, Coup, Sea Battle, SpyFall, etc.), testing multi-agent strategic thinking.
- **Source:** Costarelli et al., arXiv:2406.06975 (2024)
- **URL:** https://arxiv.org/abs/2406.06975
- **Year:** 2024

---

## 🤖 TOOL USE & FUNCTION CALLING

### 24. **Berkeley Function Calling Leaderboard (BFCL)**
- **Description:** Leading benchmark for LLM function/API calling; tests single-turn, multi-turn, parallel, nested calls across Python, Java, JavaScript, SQL, REST. Versioned (V1–V4), ICML 2025.
- **Source:** UC Berkeley Sky Computing Lab (Gorilla Project)
- **URL:** https://gorilla.cs.berkeley.edu/leaderboard.html
- **Year:** 2024 (V1), updated through 2025

### 25. **ToolBench / ToolEval**
- **Description:** Large-scale instruction-following benchmark for real-world tool use with 16,000+ real APIs; pairs with ToolLLaMA fine-tuned model; ICLR 2024 Spotlight.
- **Source:** OpenBMB / Qin et al., ICLR 2024
- **URL:** https://github.com/OpenBMB/ToolBench
- **Year:** 2023/2024

---

## 📏 INSTRUCTION FOLLOWING & GENERAL CAPABILITIES

### 26. **IFEval (Instruction Following Eval)**
- **Description:** Tests strict instruction-following ability (e.g., "write in JSON", "use exactly 500 words"); one of 6 core benchmarks in HuggingFace Open LLM Leaderboard v2.
- **Source:** Zhou et al., arXiv:2311.07911; Google Brain / HuggingFace 2024
- **URL:** https://arxiv.org/abs/2311.07911
- **Year:** 2023/2024

### 27. **MT-Bench**
- **Description:** Multi-turn conversational benchmark across 8 domains (writing, math, coding, roleplay, etc.) judged by GPT-4 on a 1–10 scale; foundational "LLM-as-judge" framework.
- **Source:** Zheng et al., NeurIPS 2023 (LMSYS / Berkeley)
- **URL:** https://arxiv.org/abs/2306.05685
- **Year:** 2023

### 28. **AlpacaEval / AlpacaEval 2.0**
- **Description:** Win-rate-based evaluation of instruction-following LLMs against reference model (GPT-4); uses LLM-as-judge; AlpacaEval 2.0 uses length-controlled win rate to reduce verbosity bias.
- **Source:** Dubois et al., Stanford / arXiv:2404.04475
- **URL:** https://tatsu-lab.github.io/alpaca_eval/
- **Year:** 2023/2024

### 29. **WildBench**
- **Description:** Evaluation on challenging, diverse "in the wild" real user queries; uses LLM-as-judge; designed to be harder than MT-Bench with less contamination.
- **Source:** Lin et al., arXiv:2406.04770 (AI2 / 2024)
- **URL:** https://arxiv.org/abs/2406.04770
- **Year:** 2024

### 30. **MMLU-ProX**
- **Description:** Multilingual extension of MMLU-Pro across 13–29 languages using expert-post-edited machine translation; enables direct cross-lingual LLM capability comparison.
- **Source:** arXiv:2503.10497 (2025)
- **URL:** https://arxiv.org/abs/2503.10497
- **Year:** 2025

---

## 🌍 MULTILINGUAL

### 31. **MGSM (Multilingual Grade School Math)**
- **Description:** Multilingual extension of GSM8K into 10 languages including low-resource; evaluates cross-lingual mathematical chain-of-thought reasoning.
- **Source:** Shi et al., ICLR 2023
- **URL:** https://huggingface.co/datasets/juletxara/mgsm
- **Year:** 2023

### 32. **FLORES-200**
- **Description:** Translation quality benchmark for 200 languages using professional-translated parallel sentences; widely used to evaluate multilingual LLM fluency and comprehension.
- **Source:** Meta AI / NLLB Team, arXiv:2207.04672
- **URL:** https://github.com/facebookresearch/flores
- **Year:** 2022

### 33. **IndicGenBench / IndicMMLU**
- **Description:** Benchmarks for Indian languages (22 officially recognized) covering generative tasks and MMLU-style QA; evaluates frontier models on underrepresented Indic scripts.
- **Source:** Google Research India; arXiv:2404.16816 (2024)
- **URL:** https://arxiv.org/abs/2404.16816
- **Year:** 2024

---

## 📸 MULTIMODAL (IMAGE / VISION-LANGUAGE)

### 34. **HEIM (Holistic Evaluation of Text-to-Image Models)**
- **Description:** 12-dimensional evaluation of text-to-image models (alignment, quality, aesthetics, bias, toxicity, fairness, robustness, etc.) across 29 models. Part of Stanford HELM.
- **Source:** Stanford CRFM
- **URL:** https://crfm.stanford.edu/helm/heim/latest/
- **Year:** 2023/2024

### 35. **GenAI-Bench**
- **Description:** 1,600+ compositional text-to-image/video prompts rated by 80k+ humans; introduces VQAScore metric; tests compositional understanding beyond simple generation quality.
- **Source:** TIGER-AI Lab; arXiv:2406.13743 / CVPR 2024
- **URL:** https://arxiv.org/abs/2406.13743
- **Year:** 2024

### 36. **RealWorldQA**
- **Description:** Evaluates real-world spatial understanding from photographs; tests whether VLMs understand physical scenes, distances, and spatial relationships.
- **Source:** xAI (Grok team), 2024
- **URL:** https://huggingface.co/datasets/xai-org/RealWorldQA
- **Year:** 2024

### 37. **MME (Multimodal LLM Evaluation)**
- **Description:** Comprehensive benchmark for multimodal LLMs testing perception (object recognition, OCR, scene recognition) and cognition (commonsense, arithmetic, text translation) with yes/no format.
- **Source:** Fu et al., arXiv:2306.13394 (2023)
- **URL:** https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models/tree/Evaluation
- **Year:** 2023

### 38. **Seed-Bench**
- **Description:** 19,000 multiple-choice questions for multimodal LLMs across 12 evaluation dimensions including image/video understanding; uses human annotation for ground-truth.
- **Source:** ByteDance; arXiv:2307.16125
- **URL:** https://github.com/AILab-CVC/SEED-Bench
- **Year:** 2023

---

## 🔊 AUDIO / SPEECH

### 39. **AudioBench**
- **Description:** Universal benchmark for audio LLMs across 8 task categories (ASR, speech QA, instruction following, audio captioning, emotion/accent/gender recognition) with 26 datasets.
- **Source:** Wang et al., NAACL 2025; arXiv:2406.16020
- **URL:** https://github.com/AudioLLMs/AudioBench
- **Year:** 2024

### 40. **AIR-Bench (Audio Instruct)**
- **Description:** Evaluation of audio LLMs on open-ended, instruction-following audio tasks across speech, sound, music, and mixed audio; dynamic, foundation-model-judged scoring.
- **Source:** Yang et al., ACL 2024
- **URL:** https://github.com/OFA-Sys/AIR-Bench
- **Year:** 2024

---

## 📜 LONG-CONTEXT

### 41. **RULER**
- **Description:** Comprehensive long-context benchmark going far beyond NIAH; includes multi-needle retrieval, multi-hop tracing, aggregation tasks, QA with distractors. Shows "effective context window" is much shorter than claimed.
- **Source:** NVIDIA; arXiv:2404.06654
- **URL:** https://github.com/NVIDIA/RULER
- **Year:** 2024

### 42. **LongBench / LongBench-v2**
- **Description:** Bilingual long-context benchmark (Chinese/English) across 21 tasks; v2 features tasks up to 1M tokens and harder multi-document reasoning and synthesis.
- **Source:** Bai et al. (Tsinghua); arXiv:2308.14508 (v1), v2 2024
- **URL:** https://github.com/THUDM/LongBench
- **Year:** 2023/2024

### 43. **SCROLLS**
- **Description:** Suite of long-document tasks (summarization, QA, NLI) across government reports, TV transcripts, scientific papers, legal contracts; forces true long-context integration.
- **Source:** Shaham et al., EMNLP 2022
- **URL:** https://huggingface.co/datasets/tau/scrolls
- **Year:** 2022

---

## 🧠 REASONING & PLANNING

### 44. **StrategyQA**
- **Description:** Binary yes/no questions requiring multi-hop world knowledge synthesis (e.g., "Was the Eiffel Tower taller than the Leaning Tower of Pisa when it was built?"); tests implicit reasoning chains.
- **Source:** Geva et al., TACL 2021
- **URL:** https://github.com/eladsegal/strategyqa
- **Year:** 2021

### 45. **PlanBench**
- **Description:** Classical planning benchmark (PDDL-based); domains include Blocksworld and Logistics; tests plan validity, cost optimization, replanning; even new "reasoning models" (o1) still struggle.
- **Source:** Valmeekam et al., NeurIPS 2023; arXiv:2206.10498
- **URL:** https://github.com/harshakokel/PlanBench
- **Year:** 2022/2023

### 46. **CLUTRR**
- **Description:** Multi-hop relational reasoning from family-relation narrative stories; tests explicit compositional inference chains.
- **Source:** Sinha et al., EMNLP 2019
- **URL:** https://github.com/facebookresearch/clutrr
- **Year:** 2019

### 47. **ToMBench**
- **Description:** Theory-of-Mind benchmark: 8 task types, 31 social cognition abilities (false beliefs, deception, faux-pas, perspective-tracking); MCQ format for automated, contamination-resistant eval. ACL 2024.
- **Source:** Chen et al., ACL 2024; arXiv:2402.15052
- **URL:** https://github.com/zhchen18/ToMBench
- **Year:** 2024

---

## 🏛️ HOLISTIC / META-EVALUATION FRAMEWORKS

### 48. **HELM (Holistic Evaluation of Language Models)**
- **Description:** Stanford's comprehensive evaluation framework covering 40+ scenarios and 7+ metrics (accuracy, robustness, calibration, efficiency, fairness, bias, toxicity); widely used as a multi-dimensional baseline.
- **Source:** Liang et al., Stanford CRFM; TMLR 2023
- **URL:** https://crfm.stanford.edu/helm/latest/
- **Year:** 2022/2023

### 49. **HELM-Lite / MedHELM**
- **Description:** Lightweight version of HELM for rapid evaluation (HELM-Lite); domain-specific extensions for medicine (MedHELM) and finance.
- **Source:** Stanford CRFM
- **URL:** https://crfm.stanford.edu/helm/lite/latest/
- **Year:** 2024

### 50. **Open LLM Leaderboard v2 (HuggingFace)**
- **Description:** HuggingFace's updated community leaderboard using 6 harder benchmarks (IFEval, BBH, MATH-Hard, MuSR, GPQA, MMLU-Pro); replaced the saturated v1.
- **Source:** HuggingFace / EleutherAI (2024)
- **URL:** https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard
- **Year:** 2024

---

## 🏢 ENTERPRISE / BUSINESS / PROFESSIONAL

### 51. **LegalBench**
- **Description:** 162 collaboratively built legal reasoning tasks (IRAC framework: issue spotting, rule application, legal argument); contributed by lawyers and professors. Nearly saturated at frontier (88%+) by 2026.
- **Source:** Guha et al., NeurIPS 2023; arXiv:2308.11462
- **URL:** https://hazyresearch.stanford.edu/legalbench/
- **Year:** 2023

### 52. **FinanceBench**
- **Description:** 10,000+ financial QA questions from real US public-company filings; tests document-grounded financial reasoning; even GPT-4-Turbo misses 81%+ without retrieval.
- **Source:** Islam et al. (Patronus AI); arXiv:2311.11944
- **URL:** https://github.com/patronus-ai/financebench
- **Year:** 2023

### 53. **Vals Index**
- **Description:** GDP-weighted composite benchmark across finance, legal, tax, and coding agentic tasks; designed as an enterprise AI performance index by Vals.AI.
- **Source:** Vals AI
- **URL:** https://www.vals.ai/benchmarks/vals_index
- **Year:** 2024

### 54. **Scale SEAL Leaderboards**
- **Description:** Expert-curated, contamination-resistant private benchmarks from Scale AI covering coding, math, instruction following, and multilingual tasks; used by enterprise buyers to compare models.
- **Source:** Scale AI
- **URL:** https://scale.com/leaderboard
- **Year:** 2023/2024

---

## 🦺 SAFETY, HALLUCINATION & ALIGNMENT

### 55. **HarmBench**
- **Description:** Standardized automated red-teaming benchmark; tests model refusal rates across harmful content, privacy violations, and misinformation using 7 attack methods and 200+ behaviors.
- **Source:** Mazeika et al., ICML 2024; arXiv:2402.04249
- **URL:** https://www.harmbench.org/
- **Year:** 2024

### 56. **HaluEval / HaluEval 2.0**
- **Description:** Hallucination evaluation benchmark across QA, dialogue, and summarization; quantifies hallucination frequency and trigger types; HaluEval 2.0 extends to biomedicine, finance, science.
- **Source:** Li et al., EMNLP 2023; arXiv:2305.11747
- **URL:** https://github.com/RUCAIBox/HaluEval
- **Year:** 2023/2024

### 57. **FActScore**
- **Description:** Fine-grained atomic factuality evaluation for free-form text generation; decomposes responses into atomic facts and checks each against a knowledge source.
- **Source:** Min et al., EMNLP 2023; arXiv:2305.14251
- **URL:** https://github.com/shmsw25/FActScore
- **Year:** 2023

### 58. **JailbreakBench**
- **Description:** Open benchmark for evaluating LLM robustness against jailbreak attacks; tracks attack success rates and refusal rates across standardized adversarial prompts.
- **Source:** Chao et al., arXiv:2404.01318 (2024)
- **URL:** https://jailbreakbench.github.io/
- **Year:** 2024

### 59. **Vectara Hallucination Leaderboard**
- **Description:** Leaderboard ranking LLMs by hallucination/faithfulness rate in RAG/summarization settings; uses FaithJudge (LLM-as-judge). Updated regularly.
- **Source:** Vectara
- **URL:** https://github.com/vectara/hallucination-leaderboard
- **Year:** 2023/ongoing

### 60. **AIR-Bench 2024 (AI Safety)**
- **Description:** Comprehensive safety benchmark across 4 risk categories and 8 hazard types; evaluates compliance with emerging AI safety standards (CAIS, OpenAI, EU AI Act).
- **Source:** Zeng et al., arXiv:2407.17436 (2024)
- **URL:** https://arxiv.org/abs/2407.17436
- **Year:** 2024

### 61. **ToxiGen**
- **Description:** Implicit hate speech and toxicity detection benchmark using adversarially generated text targeting 13 minority groups; tests models' ability to detect non-obvious harmful content.
- **Source:** Hartvigsen et al., ACL 2022
- **URL:** https://github.com/microsoft/ToxiGen
- **Year:** 2022

### 62. **BBQ (Bias Benchmark for QA)**
- **Description:** 58,000+ ambiguous trinary-choice QA questions across 9 social categories (race, age, gender, religion, etc.); tests whether LLMs rely on stereotypical shortcuts.
- **Source:** Parrish et al., ACL 2022
- **URL:** https://github.com/nyu-mll/bbq
- **Year:** 2022

---

## 🤝 MULTI-AGENT COLLABORATION

### 63. **MultiAgentBench**
- **Description:** Evaluates LLMs in cooperative (research writing, Minecraft building, coding) and competitive (negotiation, Werewolf) multi-agent scenarios with milestone-based KPIs. ACL 2025.
- **Source:** Chen et al., ACL 2025; MARBLE GitHub
- **URL:** https://github.com/ulab-uiuc/MARBLE
- **Year:** 2025

---

## 🦾 EMBODIED / ROBOTICS

### 64. **EmbodiedBench**
- **Description:** Comprehensive benchmark for multimodal LLMs as embodied agents; 4 simulation environments including EB-ALFRED (manipulation), EB-Habitat (navigation); ICML 2025 Oral. Even GPT-4o achieves only ~29% on low-level manipulation.
- **Source:** arXiv:2502.09560; ICML 2025
- **URL:** https://embodiedbench.github.io/
- **Year:** 2025

### 65. **VirtualHome / ALFRED**
- **Description:** Household task execution benchmarks for LLM-driven agents; ALFRED involves vision-language multi-step navigation and manipulation; VirtualHome uses symbolic program-execution in simulated rooms.
- **Source:** Shridhar et al. (ALFRED, CVPR 2020); Puig et al. (VirtualHome, CVPR 2018)
- **Year:** 2018/2020 (foundational; still used in 2024–2026 extensions)

---

## 🔭 RESEARCH & SCIENTIFIC PROCESS

### 66. **ScienceAgentBench**
- **Description:** 102 real-world data-driven scientific discovery tasks across chemistry, biology, economics, and more; tests agents' ability to execute end-to-end scientific workflows including code writing and experiment design.
- **Source:** Chen et al., arXiv:2410.05080 (2024)
- **URL:** https://arxiv.org/abs/2410.05080
- **Year:** 2024

### 67. **SWE-Lancer**
- **Description:** Real freelance software engineering tasks from Upwork ($1M in total task value); tests whether LLMs can complete work that professionals were paid to do.
- **Source:** OpenAI; arXiv:2502.12115 (2025)
- **URL:** https://arxiv.org/abs/2502.12115
- **Year:** 2025

---

## 📖 READING COMPREHENSION / LONG-DOCUMENT NLP

### 68. **SCROLLS (Standardized CompaRison Over Long Language Sequences)**
- **Description:** Multi-task long-document benchmark with 7 datasets (QASPER, QUALITY, GovReport, SummScreenFD, NarrativeQA, QMSum, ContractNLI); requires true long-context synthesis.
- **Source:** Shaham et al., EMNLP 2022
- **URL:** https://huggingface.co/datasets/tau/scrolls
- **Year:** 2022

### 69. **NarrativeQA**
- **Description:** Reading comprehension over full books and movie scripts; requires synthesis across very long texts; foundational long-document QA benchmark.
- **Source:** Kočiský et al., TACL 2018 (DeepMind)
- **URL:** https://github.com/google-deepmind/narrativeqa
- **Year:** 2018

### 70. **HotpotQA**
- **Description:** Multi-hop reasoning QA requiring information synthesis from multiple Wikipedia paragraphs; tests "follow the chain" reasoning ability. Very widely used.
- **Source:** Yang et al., EMNLP 2018
- **URL:** https://hotpotqa.github.io/
- **Year:** 2018

---

## 🔢 ADDITIONAL NOTABLE BENCHMARKS

### 71. **DROP (Discrete Reasoning Over Paragraphs)**
- **Description:** Reading comprehension requiring numerical reasoning, counting, sorting over passages; 96,000 questions from Wikipedia.
- **Source:** Dua et al., NAACL 2019
- **URL:** https://allenai.org/data/drop
- **Year:** 2019

### 72. **MathEval**
- **Description:** Aggregates 19 math datasets from elementary to competition level; cross-lingual (includes Gaokao); uses dynamic refresh to prevent contamination; LLM-based answer extraction.
- **Source:** Hou et al., Springer (2025); ICLR 2025 draft
- **URL:** https://arxiv.org/abs/2408.07107
- **Year:** 2024/2025

### 73. **PhysicsQA / SciPhyBench**
- **Description:** Physics olympiad and graduate-level physics question benchmarks testing models at the frontier of physical reasoning.
- **Source:** Various 2024 papers; see arXiv:2404.12456
- **Year:** 2024

### 74. **MINT-Bench**
- **Description:** Multi-turn interactive tool use benchmark; evaluates LLMs solving tasks by using tools over multiple rounds with feedback.
- **Source:** Wang et al., arXiv:2309.10691 (ICLR 2024)
- **URL:** https://arxiv.org/abs/2309.10691
- **Year:** 2023/2024

### 75. **DocFinQA**
- **Description:** Long-document financial reasoning QA requiring multi-hop reasoning over 10-K filings; harder than FinanceBench due to full document context requirements.
- **Source:** Reddy et al., ACL 2024
- **URL:** https://arxiv.org/abs/2401.06915
- **Year:** 2024

---

## 📊 SUMMARY TABLE

| # | Benchmark | Category | Year | Notable For |
|---|-----------|----------|------|-------------|
| 1 | MedQA/USMLE | Medical | 2021 | Clinical reasoning; GPT-4 benchmark |
| 2 | MedMCQA | Medical | 2022 | Indian medical exams |
| 3 | PubMedQA | Medical | 2019 | Biomedical QA |
| 4 | SciEval | Science | 2024 | Multi-level, dynamic science eval |
| 5 | ChemBench | Chemistry | 2024 | LLMs vs expert chemists |
| 6 | OlympiadBench | Math/Science | 2024 | Bilingual olympiad problems |
| 7 | MathArena | Math | 2024 | Live, contamination-free competitions |
| 8 | MuSR | Reasoning | 2024 | Multi-step soft reasoning |
| 9 | EvalPlus/HumanEval+ | Coding | 2023 | Rigorous code testing (80× more tests) |
| 10 | APPS | Coding | 2021 | Competitive programming pioneer |
| 11 | CodeContests | Coding | 2022 | DeepMind / Codeforces hard problems |
| 12 | CodeElo | Coding | 2025 | LLM Elo on real Codeforces |
| 13 | Mind2Web | Web Agent | 2023 | Generalist web agent eval |
| 14 | WebVoyager | Web Agent | 2024 | Multimodal real-web tasks |
| 15 | WorkArena/++ | Web Agent | 2024 | Enterprise ServiceNow workflows |
| 16 | AssistGUI | GUI Agent | 2024 | Windows desktop automation |
| 17 | MiniWoB++ | Web Agent | 2018 | Foundational browser task eval |
| 18 | BrowserArena | Web Agent | 2025 | Dynamic live web navigation |
| 19 | lmgame-Bench | Games | 2025 | 6 video games, modular eval |
| 20 | GAMEBoT | Games | 2025 | 8 competitive games, chain-of-thought |
| 21 | Werewolf Arena | Games | 2024 | Social deduction, deception |
| 22 | LLM-Hanabi | Games | 2025 | Cooperative ToM in Hanabi |
| 23 | GameBench | Games | 2024 | 9 strategy/social games |
| 24 | BFCL | Tool Use | 2024 | Function calling gold standard |
| 25 | ToolBench/ToolEval | Tool Use | 2024 | Real-world API tool use |
| 26 | IFEval | Instructions | 2024 | Strict instruction following |
| 27 | MT-Bench | Instructions | 2023 | Multi-turn LLM-as-judge |
| 28 | AlpacaEval 2.0 | Instructions | 2024 | Length-controlled win rate |
| 29 | WildBench | Instructions | 2024 | Hard real-user queries |
| 30 | MMLU-ProX | Multilingual | 2025 | 29-language MMLU-Pro |
| 31 | MGSM | Multilingual | 2023 | Multilingual math reasoning |
| 32 | FLORES-200 | Multilingual | 2022 | 200-language translation/fluency |
| 33 | IndicGenBench | Multilingual | 2024 | 22 Indian languages |
| 34 | HEIM | Multimodal | 2024 | Text-to-image holistic eval |
| 35 | GenAI-Bench | Multimodal | 2024 | Compositional T2I eval |
| 36 | RealWorldQA | Multimodal | 2024 | Spatial understanding from photos |
| 37 | MME | Multimodal | 2023 | Perception + cognition VLM eval |
| 38 | Seed-Bench | Multimodal | 2023 | 19k image/video MC questions |
| 39 | AudioBench | Audio | 2024 | Universal audio LLM evaluation |
| 40 | AIR-Bench (Audio) | Audio | 2024 | Open-ended audio instruction |
| 41 | RULER | Long-Context | 2024 | Multi-task long-context eval |
| 42 | LongBench/v2 | Long-Context | 2023/2024 | Bilingual, up to 1M tokens |
| 43 | SCROLLS | Long-Context | 2022 | 7-dataset long-document suite |
| 44 | StrategyQA | Reasoning | 2021 | Multi-hop implicit reasoning |
| 45 | PlanBench | Planning | 2022 | PDDL classical planning |
| 46 | CLUTRR | Reasoning | 2019 | Multi-hop relational reasoning |
| 47 | ToMBench | Social | 2024 | Theory of Mind, 31 abilities |
| 48 | HELM | Meta-Eval | 2022 | Holistic multi-metric framework |
| 49 | HELM-Lite/MedHELM | Meta-Eval | 2024 | Domain-specific HELM variants |
| 50 | Open LLM Leaderboard v2 | Meta-Eval | 2024 | HuggingFace community leaderboard |
| 51 | LegalBench | Enterprise | 2023 | 162 legal reasoning tasks |
| 52 | FinanceBench | Enterprise | 2023 | Financial document QA |
| 53 | Vals Index | Enterprise | 2024 | GDP-weighted professional tasks |
| 54 | Scale SEAL | Enterprise | 2024 | Expert-curated private evals |
| 55 | HarmBench | Safety | 2024 | Automated red-teaming |
| 56 | HaluEval / 2.0 | Safety | 2023/2024 | Hallucination taxonomy |
| 57 | FActScore | Safety | 2023 | Atomic factuality evaluation |
| 58 | JailbreakBench | Safety | 2024 | Jailbreak robustness |
| 59 | Vectara Hallucination LB | Safety | 2023 | RAG faithfulness leaderboard |
| 60 | AIR-Bench 2024 | Safety | 2024 | AI risk compliance evaluation |
| 61 | ToxiGen | Safety | 2022 | Implicit hate speech detection |
| 62 | BBQ | Fairness | 2022 | Bias across 9 social categories |
| 63 | MultiAgentBench | Multi-Agent | 2025 | Cooperation + competition KPIs |
| 64 | EmbodiedBench | Robotics | 2025 | ICML Oral; embodied manipulation |
| 65 | ALFRED/VirtualHome | Robotics | 2018/2020 | Household task execution |
| 66 | ScienceAgentBench | Research | 2024 | Scientific discovery workflow |
| 67 | SWE-Lancer | Coding | 2025 | $1M real freelance tasks |
| 68 | NarrativeQA | Reading | 2018 | Books/films QA (DeepMind) |
| 69 | HotpotQA | Reasoning | 2018 | Multi-hop Wikipedia QA |
| 70 | DROP | Reasoning | 2019 | Discrete numeric reasoning |
| 71 | MathEval | Math | 2025 | 19-dataset math aggregation |
| 72 | MINT-Bench | Tool Use | 2024 | Multi-turn interactive tool use |
| 73 | FinanceBench DocFinQA | Finance | 2024 | Long-doc financial reasoning |

---

## Gaps & Notes

1. **BALROG is already in your list** — but its sub-environments (NetHack, BabyAI, Crafter, TextWorld individually) are notable precursors that are not.
2. **Video-MME is already in your list** — AudioBench is the natural audio-side complement and is missing.
3. **Some "historical foundational" benchmarks** (CLUTRR, StrategyQA, HotpotQA, DROP, NarrativeQA) are not widely reported on new model cards anymore but are still referenced in research papers and HELM.
4. **SWE-Lancer** is very new (early 2025) and may not yet have wide leaderboard adoption; include cautiously.
5. **MathArena** is the most urgent missing entry for the math category — it is the primary live evaluation platform replacing static competition benchmarks.
6. **BFCL** is arguably the single most-cited missing benchmark for LLM tool-use capability, referenced in virtually every function-calling agent paper.
7. **WorkArena** is missing despite being a direct peer to WebArena for enterprise web agent eval.
8. **Vals Index / Scale SEAL** are the primary industry-facing composite evaluation indexes actively used by enterprise buyers and frequently referenced in model announcements.