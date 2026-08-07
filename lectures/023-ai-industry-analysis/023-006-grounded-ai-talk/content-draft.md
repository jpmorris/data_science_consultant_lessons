# preamble

- Know your audience: this talk should be geared towards the different roles at
  this organization hopefully somthing useful to all

72 unique attendees (Data Community + Data Engineering Cap + individually cc'd,
deduped), cross-referenced against the company LinkedIn role dataset:

| Category                                    | Count | %   |
| ------------------------------------------- | ----- | --- |
| Data Engineering                            | 15    | 21% |
| Data Analytics / BI / Viz                   | 14    | 19% |
| Consulting Leadership / Engagement Mgmt     | 8     | 11% |
| Data Science / AI-ML                        | 6     | 8%  |
| Project/Program Mgmt / Change Mgmt          | 2     | 3%  |
| Software Engineering / Dev                  | 2     | 3%  |
| DevOps / Cloud / Infra                      | 2     | 3%  |
| Business Analysis / Product                 | 1     | 1%  |
| Recruiting / HR                             | 1     | 1%  |
| Scrum Master / Agile Coach                  | 1     | 1%  |
| Unknown (Excella employee, no title listed) | 1     | 1%  |
| Unmatched (no LinkedIn record found)        | 19    | 26% |

Technical-practitioner vs. people-management/BA split:

|                             | Count | % of all 72 | % of the 52 classifiable |
| --------------------------- | ----- | ----------- | ------------------------ |
| Technical practitioner      | 39    | 54%         | 75%                      |
| People mgmt / BA / delivery | 13    | 18%         | 25%                      |
| Unclear (no data)           | 20    | 28%         | —                        |

- What you see in this talk is one person's opinion
  - There may be errors and prediction is hard especially about the future
  - Nothing I say here should be construed as policy or recommendations from
    Excella.
- Make sure you always have backups of all your important data and manage risk
  appropriately
- AI was used to create this talk

## if you take away anything from this talk slide

- AI progress, job/task replacement, the future depends at some point the
  ability to find a fast, cheap, trustworthy way to check an answer
- fill in others

# Part 1: The Magic

## ingredients for genai

- These GenAI Tools seem magical what makes the magic happen?
- Ingredients
  - Vector Embeddings/latent space: a mathematical method to create extremelpy
    dense representations spaces
  - A statistical model with:
    1. incredible degrees of freedom (Kimi K3 has 2.8 Trillion)
    1. The ability to attend to all words in context
    - This is the Transformer
      - Nothing has replaced Transformers as dominant model
        - Show alternatives/variations to transfomers (mamba, rwkv etc)
        - Describe these high performing versions
    - How else are the models different? MoE, Normalization discuss differences
      among the models
  - Lots of data to train these trillions of parameters
    - Data needs to be informationally dense and have a statistically robust
      relation between atomic features such as images and language
  - Lots of compute
  - A informationally dense, context-sensitive language of a certain sort

- It's currently next-token prediction all the way down
  - Show examples for
    - zero-shot example
    - CoT example
    - Agent/tool example
      - Define 'harness'

- Introduce entropy floor
  - How specs, requirements, text lower the floor (the oracle?)

## What is astounding about LLMs?

- Everyone knew:
  - words, and their meaning, correlate with each other (Firth)
  - langauge is highly predictable from context (Shannon)
    - Humans are able to complete text based on context, so maybe the bots could
      too
  - RNN/LSTMs Neural Networks predating Transformers could encode lots of
    knowledge in weights to generating convincing text
  - Words encode for meaning - embeddings

| Milestone                                                                            | Date      | What it showed                                                                                                                 | Surprise / why                                                                                                                                                           | Category                                |
| ------------------------------------------------------------------------------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------- |
| Chomsky's Universal Grammar (Syntactic Structures / Aspects of the Theory of Syntax) | 1957/1965 | Human language competence requires innate grammatical structure, not learnable from data alone                                 | Contested, not resolved — LLM success is claimed by some (Hinton, Piantadosi) as evidence against innateness; Chomsky/Grodzinsky reject this as engineering, not science | Live debate, not settled                |
| AlexNet                                                                              | 2012      | Deep nets crush hand-crafted computer vision features                                                                          | Huge — the starting gun for the whole modern deep learning wave (vision, not language, but the shockwave hit everything)                                                 | Paradigm shift                          |
| Word2Vec (Mikolov et al.)                                                            | 2013      | Meaning has clean linear structure (king − man + woman ≈ queen)                                                                | High — "you can do math with meaning" was genuinely unanticipated                                                                                                        | Anomaly → contributed to paradigm shift |
| Attention Is All You Need (Vaswani et al.)                                           | 2017      | You can drop recurrence entirely; attention alone is enough, and it parallelizes                                               | Real, clean anomaly against the field's assumption that recurrence was necessary — true significance mostly retrospective                                                | Anomaly → enabling                      |
| GPT-2 ("Language Models are Unsupervised Multitask Learners")                        | 2019      | Zero-shot multitask competence with zero fine-tuning — reading comprehension, translation, summarization, QA just from prompts | High — violated BERT's (and OpenAI's own GPT-1's) immediately-preceding assumption that fine-tuning was necessary                                                        | Anomaly, arguably paradigm shift        |
| GPT-3 ("Language Models are Few-Shot Learners")                                      | 2020      | Few-shot in-context learning — new tasks from a handful of prompt examples, zero weight updates                                | High — nothing in the training objective predicted this                                                                                                                  | Paradigm shift                          |

- What we still dont know
- (some) Linguists vs (some) Computer Scientists -- when we see an LLM solve
  problems it's never seen before (grad physics, math olypiad, problems not in
  the training data) is it just close enough to it's training data that it can
  express that regularity with simple next-word prediction because language is
  that exact (low entropy) in these cases OR is it encoding knowledge and
  understanding at some level that it's no longer relying on language and
  next-token exclusvely. Inside these networks is there encoded rationality in
  the weights or is there only encoded next-token that only looks like
  rationality.

## How do these models get better

- are LLMs like Moore's law (50 years of gains) or are they like compression,
  statisical sampling, symbolic AI, quick gains followed by a plateau

- Remind the audience of different trends on top of METR performance show
  different trend possibilities

- Current trends and benchmarks
  - Review of the all the benchmarks out there
- What is the theoretical ceiling of preformance
  - Define entropy
  - How context lowers entropy floor
  - How task-size (better word?) changes the entropy floor
- Will this ever stop?
- Well, how do they get better?
  - Pretraining
  - Inference time/CoT
  - Fine-Tuning
  - RLHF
  - Engineering
- Is improvement purely a data and compute problem
  - How much of the methods above are data vs non-data improvements
  - with infinite data and compute how good can these models get

- Context window trends

## AI and the knowledge frontier

- Closely related to the reasoning debate is the degree to which GenAI can
  discover new knowledge.
  - There is existing human knowledge and at least 3 types of discoveries
    - A discovery missed in plain sight that is more interpolation of current
      data
    - A discovering at the edge of the knowledge frontier that is a slight
      improvment beyond what we already know
    - A major paradigm shifting discovery (Einstein and special relativity)
  - AI can hammer at the frontier almost classical-search style (but with LLM
    flexibility and powerful human regularity) by trying many times on a problem
    against an oracle to find smething new.
  - AI can also zero-shot (or few-shot) an answer that seems closer to how
    humans might

# Part 2: The Future

- quote about prediction is difficult especially about the future

## Short term

- Synthetic benchmarks will continue to improve in the near term
- Harness-based, oracle verification produces many small-deal (and some bigger
  deal) discoveries over years until low-hanging discoveries are exhausted
  - Math and LEAN
    - Review all the AI-assisted discoveries (Jacobian, groups, mention Erdos
      here and any caveats around this being a retrevial problem)
  - Protein folding - Protein databank
  - Computer science
    - Some Matrix discovery
  - Cybersecurity
    - Hacking and vulnerability discovery will happen for the near term until
      existing software can be patched and systems hardened
    - Review of recent sandbox escapes and how novel these escapes are (are the
      Go-move creative, or just doing the thing humans dont have the motivation
      to--using highly technical knoweldge and trying stuff over and over
      thousands of time). Does this all comes down to code is cheap now? It's
      not the ideas, it's the code and attempts are cheap. But begs the question
      of why we didn't see this with gpt-3,4,5, maybe no one tried?
- Will the future be like Moore's law or like other computer-based scaling
  misses
- Tech companies will make AI a first-classs citizen everywhere that we will see
  6 months - 1 year prior (some of the examples I will show)
- Delivery will happen, real cool tools will come, but will lag what you would
  expect from the benchmarks or what we see in coding
- 'normies' that don't code may appreciate some (or lots) of these benefits but
  will not find it as groundbreaking as the coders where the oracle exists
- Without a serious breakthrough plateau should happen at some point
  - There's no existing scaling explanation in any scaling law that wouldn't
    plateau
  - Either a major breakthrough or an unforeseen emergent phenomenon would have
    to happen for continual scaling
  - This may be a point that risks job loss (most likely confined to software
    and some tech), or other dangerous outcomes
  -

## Long-term craziness

- We will all be working for years for some of us close to 40 years and living
  for longer
  - Lots can happen in 40 years. That far out, all bets are off
- ASI
  - Most likely would come from RSI
  - Read papers on RSI
  - Two RSI defeaters
    - Can never even get to AI+1
    - AI+1... AI+N steps are not all assured and one is too difficult
  - Two canaries something big may happen:
    - Real-world problems are being zero-shotted and major advancements
    - RSI starts producing major advances (not small asymptotic improvements of
      increasing parameters, changing architecture, but major discoveries

# Part 3: Your Job

## Excella Roles

Federal-consulting context matters here (Section 508, ATO/FedRAMP, COR
relationships, formal reporting cadences) — distinct from purely commercial
consulting.

**Vulnerability legend** (my personal call, not a benchmark score):

- **Replacement** — AI can already do most of the task's mechanics with a human
  mainly spot-checking, or will very soon.
- **Augmentation** — AI meaningfully speeds up/improves the task, but human
  judgment, accountability, or context stays essential to doing it well.
- **Influence** — AI doesn't do the task directly; it changes how/why/whether
  the task happens, usually because the task is fundamentally relational,
  political, or accountability-bound.

### BA/EM

| Task                                                       | Vulnerability | Why                                                                                                               |
| ---------------------------------------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------- |
| Formal status reporting (PM)                               | Replacement   | Agents pulling from Jira/ADO and drafting the required report is close to fully automatable today                 |
| EVM reporting (PM)                                         | Replacement   | Formulaic, standardized government calculation — one of the most mechanical tasks on this list                    |
| Formal requirements docs — SRS-style (BA)                  | Replacement   | Drafting structured documentation from notes is one of the most directly automatable knowledge-work tasks         |
| Scope management against the SOW (EM)                      | Augmentation  | AI can flag scope-creep in documents fast; judgment/political handling stays human                                |
| Financial management — budget/utilization/margin (EM)      | Augmentation  | Spreadsheet-style tracking/forecasting is very automatable; sign-off/negotiation stays human                      |
| Business development (EM)                                  | Augmentation  | AI drafts proposals and mines RFPs fast; winning trust and bid/no-bid judgment stays human                        |
| Schedule management (PM)                                   | Augmentation  | Agents already track dependencies/flag slippage well; tradeoff judgment stays human                               |
| Resource allocation (PM)                                   | Augmentation  | Real optimization problem AI is good at proposing options for; final call factors in politics                     |
| Risk/issue tracking (PM)                                   | Augmentation  | Mechanical flagging is close to automatable now; mitigation strategy stays human                                  |
| Budget/cost tracking (PM)                                  | Augmentation  | Same reasoning as EM's financial management                                                                       |
| Stakeholder analysis (Change Mgmt)                         | Augmentation  | AI can map stakeholders from org data; nuance on influence/sentiment benefits from a human read                   |
| Change impact assessments (Change Mgmt)                    | Augmentation  | AI can draft cross-system impact analysis from documentation, genuine accelerant                                  |
| Communication planning (Change Mgmt)                       | Augmentation  | Strong drafting use case; calibration to org culture/politics benefits from a human pass                          |
| Training plan development (Change Mgmt)                    | Augmentation  | Drafting training materials is very automatable now                                                               |
| ADKAR/Prosci readiness assessments (Change Mgmt)           | Augmentation  | Structured framework-based survey synthesis is AI-friendly                                                        |
| Requirements gathering (BA)                                | Augmentation  | AI helps draft questions/synthesize notes; interview/workshop facilitation and trust-building is human            |
| Process mapping — current vs. future state (BA)            | Augmentation  | AI can draft process diagrams from descriptions; validating against real org nuance needs a human                 |
| Backlog grooming support (BA)                              | Augmentation  | AI drafting/refining user stories and acceptance criteria is a solid, current use case                            |
| UAT planning (BA)                                          | Augmentation  | Generating test cases from requirements is a strong existing AI use case                                          |
| Client satisfaction / relationship management (EM)         | Influence     | Trust and reading political dynamics is human; AI preps talking points, doesn't do the relationship               |
| Staffing decisions (EM)                                    | Influence     | Interpersonal fit and career politics dominate; AI mostly changes what skills are needed, not the decision itself |
| Managing COR relationship / contract vehicle dynamics (EM) | Influence     | Deeply relational and procurement-specific; AI is background prep at most                                         |
| Governance — steering committees, gate reviews (PM)        | Influence     | Building consensus among senior stakeholders in a room is relational                                              |
| Training delivery (Change Mgmt)                            | Influence     | In-person facilitation and trust still matter, though AI tutoring is closing this gap                             |
| Resistance management (Change Mgmt)                        | Influence     | Fundamentally emotional/political navigation, not something AI does directly                                      |
| Change champion networks (Change Mgmt)                     | Influence     | Building human networks of trust/influence isn't automatable                                                      |
| Facilitating between business and technical teams (BA)     | Influence     | Translation work requiring trust from both sides; deeply relational                                               |

### Scrummaster

| Task                                       | Vulnerability | Why                                                                                                       |
| ------------------------------------------ | ------------- | --------------------------------------------------------------------------------------------------------- |
| Track/report sprint metrics                | Replacement   | Mechanical data-pull-and-summarize, essentially automatable already                                       |
| Manage the board — ticket hygiene          | Replacement   | Very mechanical; agents already do this via ticket-system APIs                                            |
| Status reporting to COR                    | Replacement   | Same as PM's formal status reporting — mechanical compliance reporting                                    |
| Jira + personal-agent preplanning workflow | Augmentation  | Speculative/emerging — this is itself a coming shift in how planning gets prepped, not a settled task yet |
| Facilitate ceremonies                      | Augmentation  | Async "standup bot" summarization already exists; live room facilitation for bigger decisions stays human |
| Scrum-of-Scrums coordination               | Augmentation  | Cross-team status synthesis is AI-friendly; negotiating cross-team priorities stays human                 |
| Remove blockers/impediments                | Influence     | Requires organizational authority/relationships; AI helps find who's blocking, not resolve it             |
| Coach team on Agile practices              | Influence     | Coaching/mentorship is relational                                                                         |
| Conflict resolution                        | Influence     | Deeply emotional/human, not meaningfully automatable                                                      |

### Software Developer

| Task                                              | Vulnerability | Why                                                                                                                                                               |
| ------------------------------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Unit/integration testing                          | Replacement   | AI is very good at generating test cases/boilerplate already — one of the more automatable dev tasks                                                              |
| Documentation of code/APIs                        | Replacement   | One of the cleanest, most automatable software tasks that exists today                                                                                            |
| STIG/security scans before deployment             | Replacement   | Already tooling-driven; AI mainly improves the remediation-suggestion layer on top                                                                                |
| Writing/maintaining application code              | Augmentation  | Trending toward Replacement for narrow, well-specified tasks; system-level judgment/architecture stays human for now — the fastest-moving row in this whole table |
| Code review                                       | Augmentation  | AI does a strong automated first pass (style/bugs/security); architectural/business-context judgment is still valuable, though the balance is shifting fast       |
| Translating requirements into features            | Augmentation  | AI drafts implementation from a well-specified story; interpreting ambiguous/political requirements needs a human                                                 |
| Debugging/troubleshooting production issues       | Augmentation  | AI helps with log analysis/hypothesis generation; accountability under pressure during a live incident stays human                                                |
| Technical design/architecture discussions         | Augmentation  | AI drafts design docs/tradeoff analyses well; final judgment and stakeholder buy-in stays human                                                                   |
| Git workflow / PR review gates                    | Augmentation  | Automated CI gating already exists; AI improves the quality of automated feedback further                                                                         |
| Participating in sprint ceremonies                | Influence     | Team-dynamics contribution, not a target for automation itself                                                                                                    |
| Pair programming / knowledge transfer for handoff | Influence     | Mentorship-heavy and relational, though AI-generated docs help the underlying artifact                                                                            |

### Devops Engineer

| Task                                                            | Vulnerability | Why                                                                                                                                                                               |
| --------------------------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Secrets/config management                                       | Replacement   | Fairly mechanical and rule-based, a good current automation target                                                                                                                |
| CI/CD pipeline design and maintenance                           | Augmentation  | AI-assisted config generation speeds this up; overall system design judgment stays human, though increasingly agent-assisted end to end                                           |
| Infrastructure as Code                                          | Augmentation  | AI is quite good at generating Terraform/Ansible from a description; review before a production apply stays a human gate given the blast radius of mistakes                       |
| Cloud provisioning/management                                   | Augmentation  | Same reasoning as IaC                                                                                                                                                             |
| Containerization/orchestration                                  | Augmentation  | Config generation is heavily assisted; operational judgment during incidents stays human                                                                                          |
| Monitoring/observability setup                                  | Augmentation  | AI helps design dashboards/alerts; alert tuning and on-call response judgment stays human                                                                                         |
| ATO docs / FedRAMP / RMF continuous monitoring / STIG hardening | Augmentation  | Drafting SSPs/control narratives from system data is a strong current use case; final ISSO/AO sign-off is a regulatory requirement to stay human, not just a practical limitation |
| Incident response/on-call                                       | Augmentation  | High-stakes and judgment-heavy; human accountability essential during live incidents even with strong AI assist                                                                   |
| Cost optimization                                               | Augmentation  | Recommendation engines already exist for the analysis; implementation decisions are often still human-gated due to risk                                                           |

### UI/UX

| Task                                                   | Vulnerability | Why                                                                                                                                                                        |
| ------------------------------------------------------ | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Wireframing/prototyping                                | Augmentation  | AI already generates serviceable first-draft UIs from a prompt; refining to product/brand quality stays human for now                                                      |
| Personas, journey maps, user flows                     | Augmentation  | AI synthesizes research data into draft personas quickly; validation against real research still matters                                                                   |
| Section 508 accessibility compliance                   | Augmentation  | Automated accessibility scanners already exist and AI improves remediation suggestions — one of the stronger near-term automation opportunities here since it's rule-based |
| Design systems/component libraries                     | Augmentation  | AI helps generate/maintain component docs and code; design coherence judgment stays human                                                                                  |
| Front-end implementation (dev-hybrid)                  | Augmentation  | Same reasoning as Software Developer's coding tasks — trending toward Replacement for well-specified components                                                            |
| Design QA against implemented UI                       | Augmentation  | Visual diffing against a spec is a genuinely strong current automatable use case                                                                                           |
| User research — interviews, surveys, usability testing | Influence     | Reading real humans and subtle contextual cues is core human skill; AI-moderated research is an emerging but not dominant trend yet                                        |
| Stakeholder presentations, feedback gathering          | Influence     | Relational/persuasion-based; AI preps materials, doesn't build the human trust                                                                                             |
| Usability testing sessions with real users             | Influence     | Same as user research above — human interaction is the core skill                                                                                                          |

### Data Scientist

| Task                                               | Vulnerability | Why                                                                                                                                                                                       |
| -------------------------------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data exploration/cleaning (EDA)                    | Augmentation  | One of the most commoditized/automatable parts of data science already; mature AI-assisted EDA tools                                                                                      |
| Model development                                  | Augmentation  | Strong AI assist for boilerplate/architecture selection; problem-framing and methodology validity for a specific federal program stays human, especially given defensibility requirements |
| Feature engineering, model evaluation              | Augmentation  | Same reasoning as model development                                                                                                                                                       |
| Ad hoc analysis requests                           | Augmentation  | Agents doing quick, well-specified data pulls/analysis is already quite mature                                                                                                            |
| Documentation/methodology write-up for audit trail | Augmentation  | Drafting from analysis is very automatable; final accountability on methodology validity is human, especially for audit-defensible work                                                   |
| Maintaining production models (MLOps)              | Augmentation  | Monitoring itself is increasingly automated; operational judgment during drift/retraining decisions stays human                                                                           |
| Communicating findings to stakeholders             | Influence     | Translating technical findings for non-technical government stakeholders needs trust/credibility; AI drafts the slides, not the defense of findings under scrutiny                        |
| Collaborating with data engineers                  | Influence     | Team collaboration dynamic, not really a target for automation itself                                                                                                                     |

# Part 4: What you Should Know

## Slash Commands

## MCP

## `remote-control` in claude

## Swarms

## The more access you give agents the more powerful they are

- BUT KEEP BACKUPS
- RESTRICT AGENTS (restricted AWS accounts, AI files that restrict `rm -rf /`,
  prompt you for elevation or decryption)
- Access to email
  - can keep it read only or have it send
  - Use Case: Compose chair email

## AI Agents are multimodal

- Paste images directly into terminal
- Speech-To-Text tools

## AI Agents like deterministic oracles with immedate feedback

- One Agent to create tests another for Code but not one for the same
- Use Case:
  - AI is great with Configuratin
    - Ansible
    - Linux config files
    - Neovim

## AI Agents like robust interfaces (REST-like or programmatic APIs)

- CLI vs Browser automation
  - Also android automation
- Use Case: Sending physical mail via API
- AWS, GCP, Azure
  - Use Case: GCP TTS to create any audiobook from ebook
- Use Case: JIRA CLI
- Use Case: Interface to your email

# Summary

## Hopefully you took away from this talk

- Copy of intro summary
- AI progress, job/task replacement, the future depends at some point the
  ability to find a fast, cheap, trustworthy way to check an answer
- Final message: some work went into this presentation, you cant just tell AI
  "make a good presentation on AI' so maybe there's room for the human after
  all.
  - Try different version of othis talk where the AI makes it from scratch
    recast for full automation of labor: 2164 → 2116 without so much
    hand-holding and see what hte results are
