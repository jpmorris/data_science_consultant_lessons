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
  infrequently. Its job: merge worker branches into `main` after the user has
  reviewed (or asks it to review), resolve conflicts if they arise, push to
  `origin` when asked, and answer occasional cross-cutting questions. It does
  **not** do content or visual work itself.
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
`quarto preview` server when you can — it sidesteps port/process management
entirely. If you do need live preview, use your assigned preview port.

## Git workflow

1. Work in your own worktree, on your own branch. Never touch `main` directly.
2. Commit as you go, with real commit messages. Don't wait until "done" to
   make your first commit.
3. When you've finished a meaningful chunk of work (not necessarily the whole
   task — smaller, more frequent handoffs are easier to merge than one big
   one at the end), tell the user it's ready. Don't merge it yourself.
4. The user will either review it with you, or ask the orchestrator to
   review/merge it. Either way, merging into `main` is the orchestrator's job.
5. If you're picking up new work after a merge, pull/rebase your worktree
   against the latest `main` first, so you're not building on stale state.

## Verification standard

Render, then check actual computed state (`getComputedStyle`,
`getBoundingClientRect`, relevant attributes) via Playwright/CDP — not just
"the screenshot looks fine." This deck's history has several cases where a
mid-transition frame looked correct but the settled end-state was wrong.
Screenshot the *settled* state, not just a moment mid-animation, before
calling something done.
