#!/usr/bin/env python3
"""Search archived Reddit posts/comments via Arctic Shift (arctic-shift.photon-reddit.com)
— a free, unauthenticated third-party Reddit archive. No API key, no OAuth app,
no CAPTCHA, no Responsible Builder Policy approval needed.

Caveat: search requires a subreddit (or author) scope — there's no global
full-text search across all of Reddit without one. Fine for our use case
since we already have target subreddits in mind.

Data is archived/historical, not guaranteed to include the very latest posts
in real time.

Usage:
    uv run search_arctic_shift.py "MCP server" --subreddit LocalLLaMA,ClaudeAI --num 20
    uv run search_arctic_shift.py "claude code agent" --subreddit LocalLLaMA --months 6 --output as-results.md
"""

import argparse
import datetime as dt
import json
import sys
import time

import requests

BASE_URL = "https://arctic-shift.photon-reddit.com/api"


def _get(path: str, params: dict) -> list[dict]:
    url = f"{BASE_URL}/{path}"
    for attempt in range(6):
        resp = requests.get(url, params=params, timeout=20)
        if resp.status_code == 429:
            reset = resp.headers.get("X-RateLimit-Reset", "5")
            wait = float(reset) if reset.replace(".", "", 1).isdigit() else 5
            print(f"Rate limited (429), waiting {wait:.0f}s...", file=sys.stderr)
            time.sleep(wait)
            continue
        # The API also soft-throttles with a 422 + {"error": "Timeout. Maybe
        # slow down a bit"} instead of a proper 429 - back off and retry too.
        if resp.status_code == 422:
            try:
                body = resp.json()
            except ValueError:
                body = {}
            if "slow down" in str(body.get("error", "")).lower():
                wait = 3 * (attempt + 1)
                print(f"Server asked us to slow down, waiting {wait}s...", file=sys.stderr)
                time.sleep(wait)
                continue
        resp.raise_for_status()
        return resp.json().get("data", [])
    raise RuntimeError("Gave up after repeated throttling responses")


def _date_params(months: int) -> dict:
    if not months:
        return {}
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=30 * months)
    return {"after": cutoff.strftime("%Y-%m-%d")}


def _subreddit_list(subreddits: str | None) -> list[str | None]:
    # Comma-joined multi-subreddit filtering isn't confirmed to work on this
    # API - query each subreddit separately (safer, known-good) rather than
    # relying on unverified syntax. [None] means "no subreddit filter."
    if not subreddits:
        return [None]
    return [s.strip() for s in subreddits.split(",") if s.strip()]


def search_posts(query: str, subreddits: str | None, num: int, months: int, sort: str) -> list[dict]:
    results = []
    subs = _subreddit_list(subreddits)
    for i, sub in enumerate(subs):
        if i > 0:
            time.sleep(2)  # be polite to a free, unauthenticated service
        params = {"query": query, "limit": min(num, 100), "sort": sort, **_date_params(months)}
        if sub:
            params["subreddit"] = sub
        results.extend(_get("posts/search", params))
    return results


def search_comments(query: str, subreddits: str | None, num: int, months: int, sort: str) -> list[dict]:
    results = []
    subs = _subreddit_list(subreddits)
    for i, sub in enumerate(subs):
        if i > 0:
            time.sleep(2)
        params = {"body": query, "limit": min(num, 100), "sort": sort, **_date_params(months)}
        if sub:
            params["subreddit"] = sub
        results.extend(_get("comments/search", params))
    return results


def format_post(p: dict) -> str:
    date = dt.datetime.fromtimestamp(p.get("created_utc", 0), tz=dt.timezone.utc).strftime("%Y-%m-%d")
    body = (p.get("selftext") or "")[:300].replace("\n", " ")
    return (
        f"- **{p.get('title', '(no title)')}** — r/{p.get('subreddit', '?')}  \n"
        f"  {p.get('score', 0)} pts | {p.get('num_comments', 0)} comments | {date}  \n"
        f"  https://reddit.com{p.get('permalink', '')}"
        + (f"  \n  {body}{'...' if len(body) == 300 else ''}" if body else "")
    )


def format_comment(c: dict) -> str:
    date = dt.datetime.fromtimestamp(c.get("created_utc", 0), tz=dt.timezone.utc).strftime("%Y-%m-%d")
    body = (c.get("body") or "").replace("\n", " ")[:300]
    return (
        f"- r/{c.get('subreddit', '?')} — {c.get('score', 0)} pts — {date}  \n"
        f"  {body}{'...' if len(body) == 300 else ''}  \n"
        f"  https://reddit.com{c.get('permalink', '')}"
    )


def main() -> None:
    ap = argparse.ArgumentParser(description="Search Reddit via Arctic Shift (free, no auth, no approval).")
    ap.add_argument("query", help="Search query (searches title+body for posts, body for comments)")
    ap.add_argument("--subreddit", help="Comma-separated subreddits to restrict to (recommended)")
    ap.add_argument("--type", choices=["posts", "comments", "both"], default="posts")
    ap.add_argument("--num", type=int, default=25, help="Max results per type (up to 100)")
    ap.add_argument("--months", type=int, default=0, help="Only results from the last N months (0 = no limit)")
    ap.add_argument("--sort", choices=["asc", "desc"], default="desc")
    ap.add_argument("--output", help="Write results as markdown to this file instead of stdout")
    ap.add_argument("--json", action="store_true", help="Print raw JSON instead of formatted markdown")
    args = ap.parse_args()

    posts, comments = [], []
    if args.type in ("posts", "both"):
        posts = search_posts(args.query, args.subreddit, args.num, args.months, args.sort)
    if args.type in ("comments", "both"):
        comments = search_comments(args.query, args.subreddit, args.num, args.months, args.sort)

    if args.json:
        print(json.dumps({"posts": posts, "comments": comments}, indent=2))
        return

    scope = f"r/{args.subreddit}" if args.subreddit else "all of Reddit (slower, less reliable)"
    lines = [f"# Arctic Shift search: \"{args.query}\" in {scope}\n"]
    if posts:
        lines.append("## Posts\n")
        lines.extend(format_post(p) for p in posts)
    if comments:
        lines.append("\n## Comments\n")
        lines.extend(format_comment(c) for c in comments)
    if not posts and not comments:
        lines.append("_No results._")
    output = "\n\n".join(lines)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output + "\n")
        print(f"Wrote {len(posts)} posts, {len(comments)} comments to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
