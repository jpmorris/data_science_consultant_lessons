# Mining VibeMathed: Lean/harness vs. think-hard-no-external-verify across 437 AI math results

**Source**: [vibemathed.com](https://vibemathed.com) — a community-curated tracker of math problems
first solved with AI in the loop. CC BY 4.0. Pulled via their own JSON export
(`/api/dataset`, `vibemathed-raw-599.json` in this folder), snapshotted
2026-08-19. 599 problems tracked total; **this pass covers the 437 marked
`resolution: resolved`** (fully proved or disproved), setting aside the 93
partial, 57 candidate, 9 variant, and 3 retracted entries for a later pass.

Companion files in this folder:
- `resolved-437-enriched.json` / `.csv` — one row per resolved problem, VibeMathed's
  own structured fields plus everything derived below (lean status, harness/think-hard
  keyword hits, verification route, and — for the 24 hand-reviewed problems — a manual
  verdict + one-paragraph rationale).
- `vibemathed-raw-599.json` — the untouched full export, in case a later pass needs
  the partial/candidate/variant/retracted problems too.
- `build_enrichment.py` — the script that produced the enriched file (rerunnable if
  VibeMathed's dataset updates).

## Why this exists

Started from a question about one row on the "AI and the Knowledge Frontier" slide
(the Dinitz–Garg–Goemans counterexample): was that brute-forceable? That led into a
bigger question this doc tries to answer with real data instead of anecdotes: **across
everything AI has resolved in research-level math, how much of it is "harness did a
huge search, then Lean or a human checked the output" versus a case where the model's
own single pass of reasoning produced something a human then read and confirmed by
hand** — the closer analogue to "here's my theory, go check it," with the model doing
comparatively little of the checking itself?

That single question turns out to have three real axes hiding inside it, not one:

1. **Discovery process** — did finding the result involve a search/retry/multi-agent
   harness, or a small number of passes (ideally one)?
2. **Result shape** — is the result a *construction* (a counterexample or witness —
   cheap and mechanical to check once you have it, regardless of how it was found) or
   an *argument* (a conceptual proof, where the hard part **is** the checking, because
   there's no simple external oracle to run it against)?
3. **Verification rigor** — once found, was the result checked by a Lean kernel, by a
   named outside expert, by the paper's own authors only, or not checked by anyone
   independent at all?

VibeMathed's own schema already separates axes 2 and 3 cleanly
(`resolutionMethod`: construction / argument / computation, and `verification`:
unreviewed → site-confirmed / lean-checked → lean-verified / expert-verified). Axis 1
— the one this document adds — isn't a structured field there; it has to be mined from
free-text `aiRole` / `resultNote` descriptions, and about 12% of resolved entries don't
have that text at all.

## Headline numbers (437 resolved problems)

- **Verification tier**: 281 unreviewed (64%) · 97 Lean-verified or Lean-checked (22%)
  · 49 site-confirmed (11%) · 10 expert-verified with no Lean (2%) · zero contested in
  this resolved subset (the 2 site-wide "contested" entries both fall outside the
  437 resolved). Confirms the intuition going in: **Lean is the exception, not the
  norm** — most "resolved" entries here rest on the paper's own authors' say-so, not
  machine or third-party checking.
- **Resolution method**: 250 arguments (57%) vs. 171 constructions (39%) vs. 16 pure
  computations (4%). Somewhat more proofs than counterexamples/witnesses overall.
- **Discovery-process auto-tag** (keyword-based, see Methodology below): 140 problems
  (32%) show explicit harness/search/multi-agent language; 7 (1.6%) show explicit
  one-shot/single-prompt language, plus 1 mixed and 1 with no text at all; 288 (66%)
  show neither keyword set — no process detail either way, not "no harness happened,"
  just **not disclosed in the text we have**.
- **Which branch of math is this actually concentrated in?** Combinatorics (112,
  26%) and Number theory (78, 18%) together are 43% of everything resolved — more
  than the next four fields combined. Logic & foundations is nearly empty (2). Number
  theory has the *highest* Lean-verified share of any field (38/78, ~49% — driven
  heavily by the Erdős-problems ecosystem and Harmonic's Aristotle prover); Combinatorics,
  despite having the most total results, has a much lower Lean share (15/112, ~13%).
- **Who's behind it**: OpenAI-attributed models are behind 217 of the 334 resolved
  problems with a named lab (65%); Anthropic 24, Google DeepMind 11, Harmonic 11 (mostly
  as the Lean-proving half of a pipeline, not the discovery half); 103 entries don't
  name a maker at all.

Full crosstabs (field × Lean status, field × auto-tag, maker counts, decade-posed
distribution) are in the appendix at the bottom.

## Methodology

**Discovery-process auto-tag.** For each resolved problem, concatenated `aiRole` +
`resultNote` + `verificationNote` + `claimIssueNote` and scanned for two keyword sets:

- *harness signal*: search, agent(s)/subagent(s), pipeline, harness, orchestrat-,
  iteration(s), autonomous, pruning, tool-use, repeat-/sampling, candidates, filtered,
  "generated and discarded", brute, enumerat-
- *think-hard signal*: one-shot, zero-shot, single/one prompt, "bare problem statement
  ... no historical context", immediately, first try, "without search"

A problem tagged **harness-signal** hit only the first set, **think-hard-signal** only
the second, **mixed-signal** both, **no-signal** neither (most common outcome — the
text just doesn't say), **insufficient-text** had no `aiRole`/`resultNote` at all (1
resolved problem).

This is a blunt instrument — "search" can mean the *math topic* (e.g. a search-theory
paper) rather than a description of the AI's process, so keyword hits were not trusted
on their own. **25 problems were selected for a full manual read** — every
`expert-read`/`expert-checked-construction` verification-route problem (10, VibeMathed's
own closest structural match to "checked by a human, not a machine"), every explicit
think-hard/mixed-signal keyword hit (8), and every `significance ≥ 40` problem that
didn't already fall in those buckets (8, with one overlap) — and each was read and given
a hand-written verdict + rationale, not just a keyword tag. Those 25 are in the
"Hand-reviewed cases" section below; the other 412 carry only the automated tag and
should be read with that caveat.

**What didn't work**: trying to extract explicit trial/attempt counts by regex
(`\d+ attempts`, `\d+ trials`, etc.) across all 437 texts. It found effectively
nothing usable beyond what was already known from outside reporting (e.g. the DGG
"4 prompts, 58 words" fact came from X/news coverage, not from VibeMathed's own
description of that problem). **VibeMathed's own write-ups almost never quantify how
many attempts something took** — that's a real, general finding, not a gap in this
analysis: the "how many trials" question you can't answer from this dataset alone for
the vast majority of entries, only for the handful where outside reporting filled it in.

## Hand-reviewed cases: the two axes in practice

### Group A — the target case: single-pass argument, checked only by a human, no Lean

These are the closest matches to "here's my theory, an expert read it and confirmed
it" — a *proof* (not a self-checking construction), produced from one prompt or a
short exchange, with no search/harness language anywhere in the description, and
verified by a named human rather than a machine:

| Problem | Field | Model | Verification | Note |
|---|---|---|---|---|
| [Middle Stair of Parallel Chip-Firing](https://vibemathed.com/problem/chip-firing-middle-stair) | Combinatorics | GPT-5.6 Sol | expert-verified | Paper states plainly the LLM found the Section 3 proof; authors verified, took responsibility. Cleanest case in the set. |
| [Simplicity of the Hodge Bundle](https://vibemathed.com/problem/hodge-bundle-simplicity) | Algebra (alg. geometry) | Aletheia (Gemini Deep Think) | expert-verified | "A single prompt asking for a proof; the author verified." |
| [Fill's Spectral Gap Equality](https://vibemathed.com/problem/fill-spectral-gap-equality) | Probability | ChatGPT 5.4 Pro | unreviewed (authors-verified) | "Produced ... in a one-shot manner and subsequently verified for correctness by the authors." |
| [Facial Distance Patterns in Planar Graphs](https://vibemathed.com/problem/facial-distance-patterns-planar) | Algorithms | GPT-5.6 Sol | unreviewed (authors-verified) | Single prompt; authors' own words: "surprising (not to say embarrassing) that this open problem has such a simple proof." Paper section literally titled "The ChatGPT Proof." |
| [Perfectly Complete Quantum Key Agreement from OWFs](https://vibemathed.com/problem/perfectly-complete-quantum-key-agreement-owf) | Quantum info | GPT-5.6 Sol Ultra | unreviewed (authors-verified) | "Discovered the proof in a one-shot conversation." |
| [Integral Local Invariant Cycles in Degree One](https://vibemathed.com/problem/integral-invariant-cycles-degree-one) | Algebra | QED (GPT-5.5) | expert-verified | Matches the pattern but the write-up is one line — low confidence from thin detail alone. |

Two more are close variants worth naming separately because the "one-shot" story has a wrinkle:

- **[Gamow liquid-drop minimizer conjecture](https://vibemathed.com/problem/gamow-liquid-drop-minimizer-conjecture)** (Analysis, ChatGPT 5.6 Pro): "a series of chats," not literally one prompt, and the proof strategy stayed close to the model's output — but authors reworked it and explicitly state the final paper contains no AI-written text. More dialogue than one-shot, but still no search/harness language.
- **[FullRSB Jamming Identity](https://vibemathed.com/problem/fullrsb-jamming-identity)** (Math. physics, Claude Sonnet 4.6/Opus 4.7): Claude "quickly proposed the essentially correct idea" from a single ask — but the first formal write-up had real errors the human authors (Parisi and Zamponi) had to fix before verifying. Worth being honest that this isn't a flawless one-shot; it's "mostly right, needed real human correction," which is a meaningfully different and probably more common shape than the clean cases above.

### Group B — the same pattern for a *construction* instead of an argument

The user's own point going in: a counterexample is always cheaply externally
checkable once you have it, so "one-shot, no harness" is a fair thing to notice
here even though the check itself is trivial — it's the *finding*, not the
*checking*, that would be remarkable:

| Problem | Field | Model | Verification | Note |
|---|---|---|---|---|
| [Huneke–Wiegand Conjecture](https://vibemathed.com/problem/son-pham) | Algebra | GPT-5.6-Pro | expert-verified | "Came up with the counterexample on [one] shot." Verified by the conjecture's own author. |
| [The Mihail–Vazirani Conjecture](https://vibemathed.com/problem/mihail-vazirani-conjecture) | Combinatorics | GPT-5.6 Sol | unreviewed (author-verified) | "Generated ... in a one-shot manner," construction not proof. Reused the same prompt template as the Cycle Double Cover harness run below — same template, opposite discovery mode, worth noting. |

**A genuine best-of-both case**: [Erdős Problem #1196](https://vibemathed.com/problem/erdos-1196-primitive-sets)
(already on the deck's slide) is one-shot *and* subsequently Lean-verified — not an
either/or. Liam Price fed GPT-5.4 Pro the bare problem statement with no historical
context; the model found the key move (reweighting via the von Mangoldt function) in
one pass, and the result was later formalized in Lean. Rare combination in this set.

### Group C — a real third category: iterative, human-guided, but not a harness

Not every non-one-shot result is a multi-agent search. Three cases show a human
steering a multi-turn conversation — closer to how a person actually works with a
capable collaborator than either "one shot" or "autonomous harness":

- **[Banach's isometric conjecture](https://vibemathed.com/problem/banach-s-isometric-conjecture)** (Analysis): "extensive interactions" over a problem the authors had already reduced themselves.
- **[White's Conjecture on Matroids](https://vibemathed.com/problem/white-s-conjecture-on-matroids)** (Combinatorics): the author directed the model rank by rank — checked 5, 6, then 7 through 10 — until a counterexample fell out. Directed, incremental human search using the model as the executor, not an autonomous multi-agent process.
- **[KLS Conjecture for Quadratic Forms](https://vibemathed.com/problem/kls-quadratic-forms)** (Geometry & topology): "developed in collaboration with" the model, checked by the author — collaborative framing, no explicit one-shot or harness language either way.

### Group D — clear harnesses (the contrast group)

These confirm the auto-tag correctly, and one detail is worth flagging: **the same
prompt template gets reused across unrelated problems**, sometimes run as a full
autonomous harness and sometimes as a single pass — the discovery *mode* is a choice
made per-run, not an inherent property of "AI on this problem":

- **[Cycle Double Cover Conjecture](https://vibemathed.com/problem/cycle-double-cover-conjecture)** (Combinatorics, GPT-5.6 Sol Ultra): 64 parallel subagents, under an hour, Lean formalization added afterward. This is the template later reused as a *one-shot* for Mihail–Vazirani (Group B) and as a *harness* for Crouzeix's conjecture below.
- **[Crouzeix's Conjecture](https://vibemathed.com/problem/crouzeix-s-conjecture)** (Analysis): 16-hour autonomous GPT-5.6 Sol run, branching subagent strategies, adversarial audit, no human intervention once started — reused the Cycle Double Cover prompt.
- **[Lamplighter Return Probability](https://vibemathed.com/problem/lamplighter-return-probability)** / **[Lamplighter Total Variation](https://vibemathed.com/problem/lamplighter-total-variation)** (Probability): QED multi-agent system, "multiple rounds of decomposition and refinement" — companion results, same day.
- **[Schiffer's Conjecture](https://vibemathed.com/problem/schiffer-conjecture)** / **[Sendov's Conjecture](https://vibemathed.com/problem/sendov-s-conjecture)** (Analysis): coding harnesses for numerics/drafting plus a separate Lean 4 formalization — the harness-then-Lean pipeline shape. Schiffer's incidentally also refutes the 1929 Pompeiu problem via the same construction.

### Group E — cautionary cases, worth knowing about even though they're not "results"

- **[Petersen Coloring Conjecture](https://vibemathed.com/problem/petersen-coloring-conjecture)**: the paper's entire AI-usage disclosure is boilerplate — "used extensively in discovery, computational search, verification, and preparation" — with no model name, version, or division of labor. Genuinely can't classify discovery mode from this. Worth keeping as a case study in *unhelpful* AI-usage disclosure. Also not even the first disproof of this conjecture — a different 68-vertex counterexample by a different author surfaced 16 days earlier.
- **[Sum-Product Conjecture over the Reals](https://vibemathed.com/problem/sum-product-conjecture-reals)**: the authors are explicit that the final proof and all main ideas are "almost entirely human-generated" — the model's only contribution was one simplifying lemma. If VibeMathed's `aiContribution` field reads this as more AI-driven than that, the authors' own account is the more careful source.
- **[Erdős's Planar Unit Distance Conjecture](https://vibemathed.com/problem/erdos-planar-unit-distance)**: thin disclosure ("model-assisted construction," version not named), and very likely **the same underlying event** as the OpenAI unit-distance disproof already on the deck's Knowledge Frontier slide (OVERSOLD row, May 2026) — cross-reference rather than double-count if this comes up again.

## Appendix: full crosstabs (437 resolved)

**Field × Lean status**

| Field group | Lean-verified | Lean-checked | Lean mentioned, untiered | No Lean mention |
|---|---|---|---|---|
| Combinatorics | 15 | 5 | 9 | 83 |
| Number theory | 38 | 4 | 8 | 28 |
| Analysis | 8 | 1 | 4 | 37 |
| Geometry & topology | 2 | 1 | 2 | 39 |
| Algebra | 12 | 1 | 2 | 28 |
| Probability & statistics | 3 | 0 | 1 | 30 |
| Theoretical computer science | 1 | 0 | 2 | 19 |
| Algorithms & optimization | 1 | 1 | 2 | 16 |
| Quantum information & computing | 1 | 0 | 1 | 13 |
| Mathematical physics | 0 | 1 | 0 | 7 |
| Differential equations | 1 | 0 | 1 | 7 |
| Logic & foundations | 1 | 0 | 0 | 1 |

**Field × discovery-process auto-tag**

| Field group | harness-signal | think-hard-signal | mixed | no-signal |
|---|---|---|---|---|
| Combinatorics | 44 | 1 | 0 | 67 |
| Number theory | 15 | 1 | 0 | 62 |
| Analysis | 21 | 1 | 0 | 28 |
| Geometry & topology | 18 | 0 | 0 | 26 |
| Algebra | 20 | 0 | 1 | 22 |
| Probability & statistics | 6 | 1 | 0 | 26 |
| Theoretical computer science | 2 | 0 | 0 | 20 |
| Algorithms & optimization | 5 | 2 | 0 | 13 |
| Quantum information & computing | 3 | 1 | 0 | 11 |
| Mathematical physics | 3 | 0 | 0 | 5 |
| Differential equations | 2 | 0 | 0 | 7 |
| Logic & foundations | 1 | 0 | 0 | 1 |

**Problem posed, by decade** (123 have no recorded year): 1920s–1 · 1930s–4 · 1940s–1 ·
1950s–7 · 1960s–15 · 1970s–34 · 1980s–44 · 1990s–51 · 2000s–35 · 2010s–53 · 2020s–69.
The 2020s bucket includes problems posed only shortly before AI resolved them —
worth separating "decades-old open problem" claims from "posed a year or two ago"
claims if this becomes a talking point; that split isn't broken out yet.

**Significance**: min 3, median 15, max 65 (only 1 of 437 scores ≥ 60; VibeMathed
calibrates 100 = Riemann Hypothesis, so nothing in this resolved set is close to that
tier — expected, since a truly top-tier open problem being *fully* resolved would be
enormous news well beyond this tracker).

## Open threads for next time

- Extend this same pass to the 93 "partial" + 57 "candidate" resolutions — likely
  where a lot of the highest-significance, most-contested activity actually lives
  (candidate = "publicly checkable, review pending," which is exactly the pending/
  contested territory the deck's slide already tracks for a handful of cases).
  Track the "how much of the reasoning is even visible in the chain-of-thought"
  question — whether hidden-reasoning-token research can say anything about specific
  high-profile cases here, not just in the abstract.
- The 289 "no-signal" resolved problems were deliberately *not* hand-read this pass
  (median description length ~225 characters — real content, just not read yet). If a
  specific field or lab's problems become the next area of interest, those are the
  ones with the most unclaimed signal left in them.
