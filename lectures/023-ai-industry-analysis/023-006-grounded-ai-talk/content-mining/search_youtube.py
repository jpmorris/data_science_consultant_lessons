#!/usr/bin/env python3
"""Search YouTube (via the free YouTube Data API v3) for videos matching a
query, and optionally pull transcripts for the results.

Requires a free Google Cloud API key with "YouTube Data API v3" enabled, set
as the YOUTUBE_API_KEY environment variable. Free quota is 10,000 units/day;
a search call costs 100 units (~100 searches/day), video-detail lookups cost
1 unit each.

Transcript fetching uses the unofficial `youtube-transcript-api` package
(no API key/quota cost) — this is a separate mechanism from the Data API,
since the official API doesn't expose transcripts for third-party videos.

Usage:
    export YOUTUBE_API_KEY=your_key_here
    uv run search_youtube.py "claude code agent demo" --num 10
    uv run search_youtube.py "MCP server tutorial" --transcripts --output results.md
"""

import argparse
import json
import os
import sys

import requests

SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
VIDEOS_URL = "https://www.googleapis.com/youtube/v3/videos"


def search(api_key: str, query: str, num: int, order: str) -> list[dict]:
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": min(num, 50),
        "order": order,  # relevance | viewCount | date
        "key": api_key,
    }
    resp = requests.get(SEARCH_URL, params=params, timeout=15)
    resp.raise_for_status()
    items = resp.json().get("items", [])
    video_ids = [it["id"]["videoId"] for it in items]
    stats = _get_stats(api_key, video_ids) if video_ids else {}

    results = []
    for it in items:
        vid = it["id"]["videoId"]
        snippet = it["snippet"]
        results.append(
            {
                "id": vid,
                "title": snippet.get("title"),
                "channel": snippet.get("channelTitle"),
                "published": snippet.get("publishedAt", "")[:10],
                "url": f"https://www.youtube.com/watch?v={vid}",
                "views": stats.get(vid, {}).get("viewCount"),
                "likes": stats.get(vid, {}).get("likeCount"),
            }
        )
    return results


def _get_stats(api_key: str, video_ids: list[str]) -> dict:
    params = {"part": "statistics", "id": ",".join(video_ids), "key": api_key}
    resp = requests.get(VIDEOS_URL, params=params, timeout=15)
    resp.raise_for_status()
    out = {}
    for it in resp.json().get("items", []):
        out[it["id"]] = it.get("statistics", {})
    return out


def fetch_transcript(video_id: str) -> str | None:
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        print("youtube-transcript-api not installed — run `uv sync`", file=sys.stderr)
        return None
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)
        return " ".join(snippet.text for snippet in transcript)
    except Exception as e:  # noqa: BLE001 - just report and move on for a research script
        print(f"  (transcript unavailable for {video_id}: {e})", file=sys.stderr)
        return None


def format_result(r: dict, transcript: str | None) -> str:
    views = f"{int(r['views']):,} views" if r.get("views") else "views unknown"
    likes = f"{int(r['likes']):,} likes" if r.get("likes") else ""
    stats = " | ".join(x for x in [views, likes] if x)
    lines = [
        f"- **{r['title']}** — {r['channel']}  \n"
        f"  {stats} | {r['published']}  \n"
        f"  {r['url']}"
    ]
    if transcript:
        snippet = transcript[:500] + ("..." if len(transcript) > 500 else "")
        lines.append(f"  Transcript (first 500 chars): {snippet}")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description="Search YouTube via the Data API v3 (free quota, self-serve key).")
    ap.add_argument("query", help="Search query")
    ap.add_argument("--num", type=int, default=10, help="Max results (up to 50)")
    ap.add_argument("--order", choices=["relevance", "viewCount", "date"], default="relevance")
    ap.add_argument("--transcripts", action="store_true", help="Also fetch transcripts (slow, one extra call each)")
    ap.add_argument("--output", help="Write results as markdown to this file instead of stdout")
    ap.add_argument("--json", action="store_true", help="Print raw JSON instead of formatted markdown")
    args = ap.parse_args()

    api_key = os.environ.get("YOUTUBE_API_KEY")
    if not api_key:
        print("Set YOUTUBE_API_KEY first (Google Cloud Console > enable YouTube Data API v3 > create API key).", file=sys.stderr)
        sys.exit(1)

    results = search(api_key, args.query, args.num, args.order)

    transcripts = {}
    if args.transcripts:
        for r in results:
            transcripts[r["id"]] = fetch_transcript(r["id"])

    if args.json:
        for r in results:
            r["transcript"] = transcripts.get(r["id"])
        print(json.dumps(results, indent=2))
        return

    lines = [f"# YouTube search: \"{args.query}\" (order={args.order})\n"]
    if not results:
        lines.append("_No results._")
    for r in results:
        lines.append(format_result(r, transcripts.get(r["id"])))
    output = "\n\n".join(lines)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output + "\n")
        print(f"Wrote {len(results)} results to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
