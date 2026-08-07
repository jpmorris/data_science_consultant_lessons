#!/usr/bin/env python3
"""Search Reddit (via PRAW, in read-only app-only mode) for posts matching a
query, sorted by relevance/top/etc.

Requires a Reddit "script" app registered at reddit.com/prefs/apps (only
possible once your Responsible Builder Policy approval clears) and its
client_id/client_secret set as environment variables. No username/password
needed — this runs in PRAW's read-only, app-only mode, which is enough for
searching public posts.

Usage:
    export REDDIT_CLIENT_ID=your_id
    export REDDIT_CLIENT_SECRET=your_secret
    export REDDIT_USER_AGENT="grounded-ai-talk-research/0.1 by u/yourusername"

    uv run search_reddit.py "claude code" --subreddits LocalLLaMA,ClaudeAI --num 20
    uv run search_reddit.py "MCP server" --time all --sort top --output reddit-mcp.md
"""

import argparse
import json
import os
import sys


def get_client():
    import praw

    client_id = os.environ.get("REDDIT_CLIENT_ID")
    client_secret = os.environ.get("REDDIT_CLIENT_SECRET")
    user_agent = os.environ.get("REDDIT_USER_AGENT")
    if not (client_id and client_secret and user_agent):
        print(
            "Set REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, and REDDIT_USER_AGENT first "
            "(reddit.com/prefs/apps, once your app is approved).",
            file=sys.stderr,
        )
        sys.exit(1)

    return praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
    )  # no username/password -> read-only, app-only mode


def search(reddit, query: str, subreddits: str | None, num: int, sort: str, time_filter: str) -> list[dict]:
    target = reddit.subreddit(subreddits.replace(",", "+")) if subreddits else reddit.subreddit("all")
    results = []
    for submission in target.search(query, sort=sort, time_filter=time_filter, limit=num):
        results.append(
            {
                "title": submission.title,
                "subreddit": str(submission.subreddit),
                "score": submission.score,
                "num_comments": submission.num_comments,
                "created": submission.created_utc,
                "url": f"https://reddit.com{submission.permalink}",
                "link": submission.url,
                "selftext": submission.selftext[:500] if submission.selftext else "",
            }
        )
    return results


def format_result(r: dict) -> str:
    import datetime as dt

    date = dt.datetime.fromtimestamp(r["created"], tz=dt.timezone.utc).strftime("%Y-%m-%d")
    lines = [
        f"- **{r['title']}** — r/{r['subreddit']}  \n"
        f"  {r['score']} pts | {r['num_comments']} comments | {date}  \n"
        f"  {r['url']}"
    ]
    if r["selftext"]:
        lines.append(f"  {r['selftext']}{'...' if len(r['selftext']) == 500 else ''}")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description="Search Reddit via PRAW (read-only, app-only mode).")
    ap.add_argument("query", help="Search query")
    ap.add_argument("--subreddits", help="Comma-separated subreddits to restrict to (default: all of Reddit)")
    ap.add_argument("--num", type=int, default=20, help="Max results")
    ap.add_argument("--sort", choices=["relevance", "hot", "top", "new", "comments"], default="relevance")
    ap.add_argument("--time", dest="time_filter", choices=["all", "year", "month", "week", "day"], default="year")
    ap.add_argument("--output", help="Write results as markdown to this file instead of stdout")
    ap.add_argument("--json", action="store_true", help="Print raw JSON instead of formatted markdown")
    args = ap.parse_args()

    reddit = get_client()
    results = search(reddit, args.query, args.subreddits, args.num, args.sort, args.time_filter)

    if args.json:
        print(json.dumps(results, indent=2))
        return

    scope = f"r/{args.subreddits}" if args.subreddits else "all of Reddit"
    lines = [f"# Reddit search: \"{args.query}\" in {scope} (sort={args.sort}, time={args.time_filter})\n"]
    if not results:
        lines.append("_No results._")
    for r in results:
        lines.append(format_result(r))
    output = "\n\n".join(lines)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output + "\n")
        print(f"Wrote {len(results)} results to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
