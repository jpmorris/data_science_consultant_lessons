# Team Coordination — Grounded AI Talk Deck

Read this first, regardless of which agent you are. Find your role below.
For deck-specific technical knowledge (theme, conventions, the reveal.js
auto-animate findings), see `AGENT-BRIEFING.md` in this same directory — this
doc is about *how the team operates*, that one is about *the deck itself*.

## The team

| Role | Worktree name | Branch | Works in `main`? |
|---|---|---|---|
| Orchestrator | — (works in the canonical checkout, not a worktree) | `main` | Yes, exclusively |
| Content | `content` | `content` | No — own worktree |
| Visual 1 | `visual-1` | `visual-1` | No — own worktree |
| Visual 2 | `visual-2` | `visual-2` | No — own worktree |

**Naming rule**: worktrees and branches are named by *role*, never by the task
currently being worked on. `visual-1` might work on axis rotation today and an
unrelated diagram next week — the name doesn't change. Don't create a
worktree called `rotation` or similar.

## Roles

- **Orchestrator** — the canonical checkout, on `main`. Talks to the user
  infrequently, and operates with the same standing trust/autonomy a single
  agent would: it does **not** wait to be told "go ahead and merge." When a
  worker reports a piece of work done, the orchestrator merges it
  proactively — its own sanity check (clean render, no warnings, no obvious
  breakage) *is* the review, the same way a single agent's self-verification
  already is. Git history is the safety net; if a merge turns out to be
  wrong, back it out and fix it, don't add a pre-merge approval gate. The
  orchestrator resolves conflicts if they arise, pushes to `origin`
  proactively too (not just when asked), and surfaces to the user only when
  something needs a real decision — a conflict it can't resolve confidently,
  a broken render, an ambiguous change. It does **not** do content or visual
  work itself.
- **Content** — researches and writes talk content: bullet text, speaker
  notes, citations, accuracy-checking. Primarily edits `grounded-ai-talk-slides.qmd`.
- **Visual 1 / Visual 2** — general-purpose visual/UI work: diagrams
  (`images/*.svg`), layout, CSS (`custom.scss`), animation. Each works on
  whatever slide(s) they're currently assigned via their own session's
  kickoff prompt — that assignment is session-specific, not part of this doc.

## Ports (reserve these for the lifetime of your session, not per-task)

| Agent | CDP port | Quarto preview port |
|---|---|---|
| Orchestrator | 9400 (if it ever needs one) | 7900 |
| Content | 9401 | 7901 |
| Visual 1 | 9402 | 7902 |
| Visual 2 | 9403 | 7903 |

Launch your own headless Chrome for verification, don't reuse the user's own
`quarto-follow` window (that's on CDP `9224` / preview `7899` — don't touch
those):
```bash
/opt/google/chrome/chrome --headless=new --remote-debugging-port=<your CDP port> \
  --user-data-dir=/tmp/<role>-profile --no-first-run --window-size=1920,1080
```
Prefer one-shot `quarto render` + screenshot over running your own live
`quarto preview` server for your *own* verification — it sidesteps
port/process management entirely.

**The preview port exists for the user's benefit, separately from your own
verification loop.** The user watches each worktree's progress live — one
browser tab per worktree, pointed at that worktree's preview port — the same
way they'd watch a single agent work, but with one tab per agent instead of
one shared view. If it's not already running, start `quarto preview --port
<your assigned port> --no-browser` once early in your session and leave it
running; you don't need to manage it further.

## Git workflow

1. Work in your own worktree, on your own branch. Never touch `main` directly.
2. Commit as you go, with real commit messages. Don't wait until "done" to
   make your first commit.
3. When you've finished a meaningful chunk of work (not necessarily the whole
   task — smaller, more frequent handoffs are easier to merge than one big
   one at the end), tell the user it's ready. Don't merge it yourself — not
   because you need approval, but because it's mechanically awkward: `main`
   is checked out in the orchestrator's directory, not yours, and git won't
   let you check out a branch that's already checked out elsewhere.
4. Merging into `main` is the orchestrator's job, and it does so
   proactively — it doesn't wait to be told "go ahead." Once you've said
   your work is ready, expect it to land without needing to ask again.
5. Rebase against the latest `main` at two points: as soon as you're told
   your own last piece of work was merged (so you keep building on top of
   your own now-canonical history, not a stale copy of it), and before
   starting any new chunk of work generally (so you also pick up whatever
   the *other* agents have landed in the meantime). Don't bother rebasing
   mid-task just to stay live-synced — it's not needed for genuinely
   disjoint work and just adds churn.

## Verification standard

Render, then check actual computed state (`getComputedStyle`,
`getBoundingClientRect`, relevant attributes) via Playwright/CDP — not just
"the screenshot looks fine." This deck's history has several cases where a
mid-transition frame looked correct but the settled end-state was wrong.
Screenshot the *settled* state, not just a moment mid-animation, before
calling something done.
