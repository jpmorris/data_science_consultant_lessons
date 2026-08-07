# Content mining for "Grounded AI" Part 4

Small CLI scripts to search for "cool things people are doing with agents" /
practitioner opinions, feeding the anecdotes/examples for Part 4 ("What You
Should Know"). Each one prints a scannable markdown list (or `--json` for raw
data) that you skim and hand-pick from — nothing here auto-writes into
`content-draft.md`.

## Setup

```bash
cd content-mining
uv sync
```

## Hacker News — free, no auth, no setup

```bash
uv run search_hn.py "claude code" --tags story --months 6 --num 20
uv run search_hn.py "MCP agents" --tags story,comment --output hn-mcp.md
```

## Bluesky — free, no auth, no setup

```bash
uv run search_bluesky.py "claude code agent" --num 25
uv run search_bluesky.py "AI agent demo" --sort latest --output bsky-agents.md
```

## YouTube — free quota, needs a one-time API key

1. Google Cloud Console → new/existing project → enable "YouTube Data API v3" → Credentials → create an API key.
2. `export YOUTUBE_API_KEY=your_key_here`
3. Free tier: 10,000 quota units/day, a search costs 100 units (~100 searches/day). No paid tier exists — if you need more, there's a free quota-increase request form with no guaranteed review timeline.

```bash
uv run search_youtube.py "claude code agent demo" --num 10
uv run search_youtube.py "MCP server tutorial" --transcripts --output yt-mcp.md
```

`--transcripts` uses the unofficial `youtube-transcript-api` package (separate
from the Data API, no quota cost) to pull the video's public transcript —
useful for skimming a talk/demo without watching the whole thing. Doesn't
work on age-restricted videos; occasionally rate-limited on cloud-server IPs.

## Reddit (via Arctic Shift) — free, no auth, no approval, works today

Reddit's own OAuth app-creation flow is currently broken/unreliable for many
people (see r/redditdev — widespread reports of the "create app" button
silently doing nothing after CAPTCHA). **Use this instead** — Arctic Shift is
a free, third-party archive of Reddit posts/comments with a public search API,
no API key, no OAuth, no approval process at all.

```bash
uv run search_arctic_shift.py "claude code" --subreddit LocalLLaMA,ClaudeAI --months 6 --num 20
uv run search_arctic_shift.py "MCP server" --subreddit LocalLLaMA --type both --output as-mcp.md
```

Caveats:
- Requires a subreddit (or author) scope for search — no global full-text
  search across all of Reddit. Fine for us since we already know our target
  subreddits.
- Data is archived/historical, not guaranteed to include the very latest
  posts in real time.
- Rate-limited (self-throttles with waits on 429/422 "slow down" responses) —
  be patient with multi-subreddit queries, they run sequentially with a
  short delay between each to be polite to a free public service.
- Comma-separated `--subreddit` values are queried one at a time internally,
  not as a single combined filter (unverified whether the API even supports
  that syntax, so this is the safer approach).

## Reddit (official API) — built, but needs your approval to clear first

Reddit's free tier requires pre-approval even for personal/non-commercial use
(Nov 2025 "Responsible Builder Policy") — this script is ready, just untested
until your app registration clears.

Once approved:

1. reddit.com/prefs/apps → create a "script" type app.
2. Set the three env vars (no username/password needed — this runs read-only,
   app-only):

```bash
export REDDIT_CLIENT_ID=your_id
export REDDIT_CLIENT_SECRET=your_secret
export REDDIT_USER_AGENT="grounded-ai-talk-research/0.1 by u/yourusername"
```

```bash
uv run search_reddit.py "claude code" --subreddits LocalLLaMA,ClaudeAI --num 20
uv run search_reddit.py "MCP server" --time all --sort top --output reddit-mcp.md
```
