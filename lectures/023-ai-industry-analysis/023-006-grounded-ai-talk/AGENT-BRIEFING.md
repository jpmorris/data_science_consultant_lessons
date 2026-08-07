# Project Briefing — Grounded AI Talk Deck

Read this before starting work in this repo. It captures decisions and hard-won
technical findings from earlier work on this deck, so you don't re-derive or
contradict them.

## What this is

A Quarto revealjs presentation, `grounded-ai-talk-slides.qmd`, rendered with
`uv run quarto render grounded-ai-talk-slides.qmd`. Uses a Jupyter kernel
(`ds-ai-industry-slides`) for any executable code chunks. Self-contained HTML
output, 1920x1080, dark theme.

## Design system (already decided — don't re-litigate)

- **Base theme**: `moon` (built-in Quarto/revealjs theme, Solarized Dark),
  layered with `custom.scss`: `theme: [moon, custom.scss]`
- **Background**: lightened one step from moon's default via
  `$body-bg: #073642` (Solarized `base02` instead of `base03`) — dark theme,
  intentionally not pitch black
- **Fonts**: **Inter** (body) + **Inter Display** (headings), self-hosted —
  `fonts/*.ttf` + `fonts.css` (`@font-face` rules) + `custom.scss` (`$font-family-sans-serif`,
  `$presentation-heading-font`). Declared in YAML via `resources:`.
  - **Do not use `fonts/Sohne-Buch.otf`** if you see it in the fonts directory —
    it's an unlicensed/pirated file from an earlier exploration, explicitly
    rejected. Inter is the legitimate replacement (SIL OFL licensed, free).
- **Color palette** (Solarized accents, used consistently across diagrams):
  cyan `#2aa198`, amber `#b58900`, blue `#268bd2`, violet `#6c71c4`,
  green `#859900`, cream `#eee8d5`, grey `#93a1a1`, panel bg `#0d4a55`
- **Slide treatments**: `.heading-accent` (amber underline, default for
  content slides) applied to all regular slides; `.divider-slide` +
  `data-background-gradient` for Part-divider slides; `.stat-slide` for the
  single "thesis" callout slide. All defined in `custom.scss`.

## Structural conventions

- **Diagrams are standalone `.svg` files in `images/`**, pulled into slides
  via `{{< include images/foo.svg >}}` inside a `` ```{=html} `` raw block —
  **not** via markdown `![]()` image syntax. This matters: `![]()` renders as
  an opaque `<img>`, which hides the SVG's internal elements from JS/CSS
  entirely. `{{< include >}}` splices the raw SVG into the page DOM
  (verified byte-identical to inline embedding), which is required for any
  per-element interactivity/animation.
- **Two-column diagram+text layout**: use the `.diagram-split-row` /
  `.diagram-split-visual` / `.diagram-split-text` classes (defined in
  `custom.scss`), **not** Quarto's native `:::: {.columns}` syntax. Quarto's
  `.columns` has a confirmed bug: it breaks (`display: flex` → stuck at
  `display: initial`) when the same column structure repeats across adjacent
  `auto-animate="true"` slides. Root-caused and fixed this way; don't revert.
- **Multi-stage auto-animate sequences** get explicit heading IDs and a
  comment tag for human referenceability:
  ```markdown
  <!-- STAGE 3/8 (llm-stage-3-latent-space): latent space: axes skew, 5 axes total -->
  ## The Ingredients of an LLM {#llm-stage-3-latent-space auto-animate="true" .heading-accent}
  ```
  Keep this pattern for any new multi-stage sequence — it's how the user
  refers to specific slides when giving feedback.
- reveal.js's core CSS sets `ul`/`ol` to `display: inline-block`, which makes
  short bullet lists look like a narrow left column. Already fixed globally
  in `custom.scss` (`display: block` override). Don't re-break it.
- A markdown formatter (Neovim/prettier, configured outside this repo) was
  previously corrupting `::: {.notes}` fenced divs by joining the fence
  marker onto adjacent text. Already fixed at the editor-config level — if
  you see `:::` warnings on render, check for fence markers glued to content
  lines and give them their own line.

## Critical technical finding: reveal.js auto-animate cannot rotate elements

This took a long, rigorous investigation to nail down — don't rediscover it
the hard way.

**What auto-animate does NOT support, confirmed via direct pixel/DOM testing
(not guessing):**
- Raw SVG geometry attribute changes (`x1/y1/x2/y2`, `cx/cy/r`,
  `x/y/width/height`) between matched (`data-id`) elements do not interpolate
  — they pop instantly to the final value with no animation. (Settle position
  is *correct*, just not animated — safe to use if you don't need motion.)
- **`transform` (rotate, translate, or any value) on a matched element does
  not work at all** — not just rotation. Confirmed on both SVG and plain
  HTML elements, whether the value changes between slides or stays identical,
  whether set via CSS `style` or the SVG `transform` attribute. The element
  ends up rendered as if untransformed (or, for lines/text, visually
  collapsed/misplaced).
- Root cause: reveal.js uses the CSS `transform` property internally to
  express whatever position/size delta *it* computes for a matched element.
  Authoring your own `transform` value conflicts with that mechanism. Reveal
  injects `[data-auto-animate="running"] [data-auto-animate-target] { transform: none }`
  as part of its own animation setup, and this can get permanently stuck
  (the section never clears `data-auto-animate="running"`), leaving the
  element's transform nulled forever.
- This matches reveal.js's own docs (revealjs.com/auto-animate/): every
  official example only changes plain CSS box properties (`height`, `color`,
  `margin-top`, `background`). Rotation is never demonstrated and isn't in
  their documented supported-property list (position, size, `color`,
  `background-color`, `font-size`, `line-height`, `padding`, `margin`).

**What DOES work:**
- Position changes via normal CSS layout or explicit `left`/`top` (no
  rotation) — genuinely interpolates and settles correctly.
- New elements simply fading in/out (give them a *different* `data-id` per
  stage rather than trying to force a broken interpolation) — this is the
  pattern used throughout the existing 8-stage "Ingredients of an LLM"
  sequence for anything that needed to visually "move": elements that
  change get unmatched (unique id per stage) so they cross-fade cleanly
  instead of collapsing.

**Open problem, if you're picking up the rotation work:** the technically
sound path is JS-created (not statically-declared) SVG elements + a plain
CSS `transition: transform` + a JS listener on `Reveal.on('slidechanged'
| 'fragmentshown', ...)`, entirely bypassing auto-animate's `data-id`
matching. Confirmed: freshly `document.createElementNS`'d SVG elements DO
correctly interpolate `transform` this way. Unconfirmed/unexplained: the
exact same technique failed on an SVG element that was part of the page's
*static* initial HTML (not JS-created) — even after ruling out timing,
stylesheet-vs-inline-style, and `transform-origin` as causes. If you hit
this, the known-working fallback is to build the shape via JS from scratch
rather than starting from static markup.

## Verification workflow

Render, then screenshot via a **headless**, CDP-connected Chrome instance —
not the user's own visible browser/window. Launch your own:
```bash
/opt/google/chrome/chrome --headless=new --remote-debugging-port=<YOUR_PORT> \
  --user-data-dir=/tmp/<unique-profile-name> --no-first-run --window-size=1920,1080
```
Then drive it via Playwright's `connect_over_cdp`. Verify actual state, not
just visual impression — check `getComputedStyle(...).transform`,
`getBoundingClientRect()`, and `data-auto-animate` attributes directly via
`page.evaluate`, not just "does the screenshot look okay," since several
bugs in this deck's history looked fine mid-transition but were wrong at
settle time.

**Port note**: the user's own Neovim `quarto-follow` tool (separate repo,
`~/dotfiles`) defaults to CDP port `9224` and quarto preview port `7899`.
Use different ports for your own testing so you don't collide with it or
with other concurrent agents. Prefer one-shot `quarto render` + screenshot
over running your own live `quarto preview` server, to avoid port
management entirely when you don't need live-reload.

## Content status

The "Ingredients of an LLM" 8-stage sequence (`llm-stage-1-language` through
`llm-stage-8-inference`) is built and content-complete, citations in speaker
notes (Epoch AI, Stanford HAI AI Index, Nemotron-CC/FineWeb papers,
Anthropic's "Toy Models of Superposition"). Rest of the deck (Parts 2-4,
Summary) is built; Part 4 has several sections marked
`<!-- DRAFT: verify/expand before presenting -->` (Slash Commands, MCP,
Remote Control, Swarms) still needing real content/verification.
