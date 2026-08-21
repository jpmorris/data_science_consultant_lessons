import json, re, collections

SCRATCH = "/tmp/claude-1000/-mnt-bebop-jmorris-code-data-science-consultant-lessons-lectures-032-ai-agents/017fd929-0d0a-47c8-89f5-927b895a899d/scratchpad"
d = json.load(open(f"{SCRATCH}/vibemathed.json"))
resolved = [p for p in d["problems"] if p.get("resolution") == "resolved"]

HARNESS_KW = [
    "search", "agent", "subagent", "pipeline", "harness", "orchestrat",
    "iteration", "iterated", "autonomous", "pruning", "pruned", "tool use",
    "tool-use", "repeat", "sampling", "candidates", "filtered", "filter",
    "generated and discarded", "many attempt", "brute", "enumerat",
]
THINK_HARD_KW = [
    "one-shot", "one shot", "zero-shot", "single prompt", "one prompt",
    "bare problem statement", "no historical context", "immediately",
    "first try", "straight away", "without search", "no search",
]
LEAN_WORD = re.compile(r"\blean\b", re.IGNORECASE)
TRIAL_NUM = re.compile(
    r"(\d[\d,]*)\s*(?:attempts?|trials?|iterations?|prompts?|tries|generations?|candidates?|hours?|days?|tokens?|sub-?agents?)",
    re.IGNORECASE,
)

def text_of(p):
    return " ".join(filter(None, [p.get("aiRole", ""), p.get("resultNote", ""),
                                    p.get("verificationNote", ""), p.get("claimIssueNote", "")]))

def lean_status(p):
    v = p.get("verification")
    if v in ("lean-verified", "lean-checked"):
        return "tiered-" + v
    t = text_of(p)
    if LEAN_WORD.search(t):
        return "mentioned-not-tiered"
    return "no-mention"

def kw_hits(text, kws):
    tl = text.lower()
    return sorted({k for k in kws if k in tl})

def trial_mentions(text):
    return sorted(set(m.group(0) for m in TRIAL_NUM.finditer(text)))

rows = []
for p in resolved:
    text = text_of(p)
    harness_hits = kw_hits(text, HARNESS_KW)
    th_hits = kw_hits(text, THINK_HARD_KW)
    lean = lean_status(p)
    trials = trial_mentions(text)
    has_text = bool(text.strip())

    # verification_route: how the *result* itself was checked
    v, rm = p.get("verification"), p.get("resolutionMethod")
    if v in ("lean-verified", "lean-checked"):
        vroute = "lean"
    elif v == "expert-verified":
        vroute = "expert-read" if rm == "argument" else "expert-checked-construction"
    elif v == "site-confirmed":
        vroute = "site-reproduced"
    elif v == "contested":
        vroute = "contested"
    else:  # unreviewed
        vroute = "unreviewed-argument" if rm == "argument" else "unreviewed-construction/computation"

    # coarse auto-tag for discovery process
    if not has_text:
        auto_tag = "insufficient-text"
    elif harness_hits and not th_hits:
        auto_tag = "harness-signal"
    elif th_hits and not harness_hits:
        auto_tag = "think-hard-signal"
    elif harness_hits and th_hits:
        auto_tag = "mixed-signal"
    else:
        auto_tag = "no-signal"  # neither keyword set hit - needs a human read

    sig = p.get("significance") or 0
    needs_review = (
        auto_tag in ("think-hard-signal", "mixed-signal", "no-signal")
        or sig >= 40
        or vroute == "expert-read"
        or (rm == "construction" and v in ("expert-verified", "unreviewed") and len(trials) <= 1)
    )

    rows.append({
        "slug": p["slug"], "name": p["name"], "field": p.get("field"),
        "fieldGroup": p.get("fieldGroup"), "yearPosed": p.get("yearPosed"),
        "solveDate": p.get("solveDate"), "model": p.get("model"),
        "modelMaker": p.get("modelMaker"), "aiContribution": p.get("aiContribution"),
        "resolutionMethod": rm, "verification": v, "significance": sig,
        "solveType": p.get("solveType"), "publication": p.get("publication"),
        "lean_status": lean, "harness_keyword_hits": harness_hits,
        "think_hard_keyword_hits": th_hits, "trial_mentions": trials,
        "verification_route": vroute, "auto_tag": auto_tag,
        "needs_manual_review": needs_review,
        "aiRole": p.get("aiRole"), "resultNote": p.get("resultNote"),
        "verificationNote": p.get("verificationNote"),
        "sourceUrl": p.get("sourceUrl"),
        "manual_verdict": None, "manual_rationale": None,
    })

with open(f"{SCRATCH}/vibemath/resolved_enriched.json", "w") as f:
    json.dump(rows, f, indent=1)

c_auto = collections.Counter(r["auto_tag"] for r in rows)
c_lean = collections.Counter(r["lean_status"] for r in rows)
c_vroute = collections.Counter(r["verification_route"] for r in rows)
n_review = sum(r["needs_manual_review"] for r in rows)

print("auto_tag distribution:", dict(c_auto))
print("lean_status distribution:", dict(c_lean))
print("verification_route distribution:", dict(c_vroute))
print("needs_manual_review:", n_review, "/", len(rows))
