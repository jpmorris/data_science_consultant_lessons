#!/usr/bin/env python3
"""Search Hacker News (via the free, unauthenticated Algolia HN Search API)
for stories/comments matching a query, sorted by points.

Usage:
    uv run search_hn.py "claude code" --tags story --months 6 --num 20
    uv run search_hn.py "MCP agents" --tags story,comment --output results.md
"""

import argparse
import datetime as dt
import json
import sys

import requests

HN_SEARCH_URL = "https://hn.algolia.com/api/v1/search"


def search(query: str, tags: str, months: int, num: int) -> list[dict]:
    params = {
        "query": query,
        "tags": tags,
        "hitsPerPage": num,
    }
    if months:
        cutoff = int((dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=30 * months)).timestamp())
        params["numericFilters"] = f"created_at_i>{cutoff}"

    resp = requests.get(HN_SEARCH_URL, params=params, timeout=15)
    resp.raise_for_status()
    hits = resp.json().get("hits", [])
    # Algolia's default search endpoint sorts by relevance; re-sort by points desc.
    hits.sort(key=lambda h: h.get("points") or 0, reverse=True)
    return hits


def format_hit(h: dict) -> str:
    title = h.get("title") or h.get("story_title") or "(comment)"
    points = h.get("points", 0)
    num_comments = h.get("num_comments", 0)
    date = h.get("created_at", "")[:10]
    hn_id = h.get("objectID")
    hn_url = f"https://news.ycombinator.com/item?id={hn_id}"
    ext_url = h.get("url") or ""
    return (
        f"- **{title}**  \n"
        f"  {points} pts | {num_comments} comments | {date}  \n"
        f"  HN: {hn_url}"
        + (f"  \n  Link: {ext_url}" if ext_url else "")
    )


def main() -> None:
    ap = argparse.ArgumentParser(description="Search Hacker News via Algolia (free, no auth).")
    ap.add_argument("query", help="Search query")
    ap.add_argument("--tags", default="story", help="Comma-separated: story, comment, ask_hn, show_hn, poll")
    ap.add_argument("--months", type=int, default=0, help="Only results from the last N months (0 = no limit)")
    ap.add_argument("--num", type=int, default=20, help="Max results")
    ap.add_argument("--output", help="Write results as markdown to this file instead of stdout")
    ap.add_argument("--json", action="store_true", help="Print raw JSON instead of formatted markdown")
    args = ap.parse_args()

    hits = search(args.query, args.tags, args.months, args.num)

    if args.json:
        print(json.dumps(hits, indent=2))
        return

    lines = [f"# HN search: \"{args.query}\" (tags={args.tags})\n"]
    if not hits:
        lines.append("_No results._")
    for h in hits:
        lines.append(format_hit(h))
    output = "\n\n".join(lines)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output + "\n")
        print(f"Wrote {len(hits)} results to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
