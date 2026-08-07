#!/usr/bin/env python3
"""Search Bluesky (via the free, unauthenticated public AT Protocol API)
for posts matching a query, sorted by like count.

No account or API key needed for search itself.

Usage:
    uv run search_bluesky.py "claude code agent" --num 25
    uv run search_bluesky.py "MCP server" --output results.md
"""

import argparse
import json
import sys

import requests

BLUESKY_SEARCH_URL = "https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts"


def search(query: str, num: int, sort: str) -> list[dict]:
    params = {"q": query, "limit": min(num, 100), "sort": sort}
    resp = requests.get(BLUESKY_SEARCH_URL, params=params, timeout=15)
    resp.raise_for_status()
    return resp.json().get("posts", [])


def format_post(p: dict) -> str:
    author = p.get("author", {})
    handle = author.get("handle", "unknown")
    display_name = author.get("displayName", handle)
    record = p.get("record", {})
    text = (record.get("text") or "").replace("\n", " ").strip()
    likes = p.get("likeCount", 0)
    reposts = p.get("repostCount", 0)
    created = (record.get("createdAt") or "")[:10]
    # uri looks like at://did:plc:xxxx/app.bsky.feed.post/yyyy
    uri = p.get("uri", "")
    post_id = uri.split("/")[-1] if uri else ""
    web_url = f"https://bsky.app/profile/{handle}/post/{post_id}" if post_id else ""
    return (
        f"- **{display_name}** (@{handle}) — {likes} likes, {reposts} reposts, {created}  \n"
        f"  {text}  \n"
        f"  {web_url}"
    )


def main() -> None:
    ap = argparse.ArgumentParser(description="Search Bluesky via the public AT Protocol API (free, no auth).")
    ap.add_argument("query", help="Search query")
    ap.add_argument("--num", type=int, default=25, help="Max results (up to 100)")
    ap.add_argument("--sort", choices=["top", "latest"], default="top", help="Sort order")
    ap.add_argument("--output", help="Write results as markdown to this file instead of stdout")
    ap.add_argument("--json", action="store_true", help="Print raw JSON instead of formatted markdown")
    args = ap.parse_args()

    posts = search(args.query, args.num, args.sort)

    if args.json:
        print(json.dumps(posts, indent=2))
        return

    lines = [f"# Bluesky search: \"{args.query}\" (sort={args.sort})\n"]
    if not posts:
        lines.append("_No results._")
    for p in posts:
        lines.append(format_post(p))
    output = "\n\n".join(lines)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output + "\n")
        print(f"Wrote {len(posts)} results to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
