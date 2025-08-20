#!/usr/bin/env python3
"""
Download DOJ press releases from /api/v1/press_releases.json day-by-day and upload daily JSONs to S3.

Behavior:
- Iterates dates from start (default 2016-01-01) to end (default today, inclusive).
- For each day, pages through results (pagesize up to 50) filtered by parameters[date]=<noon UTC epoch>.
- Concatenates results for the day into a list of dicts and uploads as JSON to S3 (one file per day).

Notes:
- DOJ API has a max pagesize of 50 and suggests <=10 req/sec. We default to ~5 req/sec.
- DOJ "date" appears to be noon UTC for the calendar date. We query with 12:00:00Z timestamps to match.

Usage:
  python download_doj_press_releases.py --bucket <bucket> [--prefix raw/doj/press_releases] [--start 2016-01-01] [--end YYYY-MM-DD]

AWS auth:
- Uses boto3 default auth (env vars, shared credentials, or instance profile).
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import time
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

import boto3
import requests
from botocore.exceptions import BotoCoreError, ClientError

API_URL = "https://www.justice.gov/api/v1/press_releases.json"
DEFAULT_PAGESIZE = 50
MAX_REQS_PER_SEC = 10


@dataclass
class Config:
    bucket: str
    prefix: str
    start_date: dt.date
    end_date: dt.date
    pagesize: int = DEFAULT_PAGESIZE
    pause_sec: float = 0.2  # 5 req/sec by default
    max_retries: int = 3
    write_empty: bool = True
    timeout: int = 30


def parse_args() -> Config:
    parser = argparse.ArgumentParser(description="Download DOJ press releases daily to S3")
    parser.add_argument(
        "--bucket",
        default=os.getenv("DOJ_S3_BUCKET"),
        required=False,
        help="S3 bucket name (or DOJ_S3_BUCKET env)",
    )
    parser.add_argument(
        "--prefix",
        default=os.getenv("DOJ_S3_PREFIX", "raw/doj/press_releases"),
        help="S3 key prefix to write daily JSONs",
    )
    parser.add_argument(
        "--start",
        default=os.getenv("DOJ_START_DATE", "2016-01-01"),
        help="Start date YYYY-MM-DD (inclusive)",
    )
    parser.add_argument(
        "--end",
        default=os.getenv("DOJ_END_DATE"),
        help="End date YYYY-MM-DD (inclusive); default=today",
    )
    parser.add_argument(
        "--pagesize",
        type=int,
        default=int(os.getenv("DOJ_PAGESIZE", str(DEFAULT_PAGESIZE))),
        help="Page size (max 50)",
    )
    parser.add_argument(
        "--pause-sec",
        type=float,
        default=float(os.getenv("DOJ_PAUSE_SEC", "0.2")),
        help="Pause between requests seconds (rate limit)",
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=int(os.getenv("DOJ_MAX_RETRIES", "3")),
        help="Max retries per request",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=int(os.getenv("DOJ_TIMEOUT", "30")),
        help="HTTP timeout seconds",
    )
    parser.add_argument(
        "--no-write-empty",
        action="store_true",
        help="If set, skip writing days with no results",
    )
    args = parser.parse_args()

    if not args.bucket:
        print("ERROR: --bucket is required or set DOJ_S3_BUCKET", file=sys.stderr)
        sys.exit(2)

    try:
        start_date = dt.date.fromisoformat(args.start)
    except Exception:
        print(f"ERROR: invalid --start {args.start}", file=sys.stderr)
        sys.exit(2)

    if args.end:
        try:
            end_date = dt.date.fromisoformat(args.end)
        except Exception:
            print(f"ERROR: invalid --end {args.end}", file=sys.stderr)
            sys.exit(2)
    else:
        end_date = dt.datetime.now(dt.timezone.utc).date()

    if start_date > end_date:
        print("ERROR: start date after end date", file=sys.stderr)
        sys.exit(2)

    pagesize = min(max(args.pagesize, 1), 50)

    return Config(
        bucket=args.bucket,
        prefix=args.prefix.strip("/"),
        start_date=start_date,
        end_date=end_date,
        pagesize=pagesize,
        pause_sec=max(args.pause_sec, 0.0),
        max_retries=max(args.max_retries, 0),
        write_empty=not args.no_write_empty,
        timeout=max(args.timeout, 5),
    )


def noon_utc_epoch(d: dt.date) -> int:
    return int(dt.datetime(d.year, d.month, d.day, 12, 0, 0, tzinfo=dt.timezone.utc).timestamp())


def s3_key_for_date(prefix: str, d: dt.date) -> str:
    return f"{prefix}/{d.strftime('%Y/%m/%d')}.json"


def request_with_retries(
    session: requests.Session,
    url: str,
    params: Dict[str, Any],
    timeout: int,
    max_retries: int,
    pause_sec: float,
) -> Optional[Dict[str, Any]]:
    last_exc: Optional[Exception] = None
    for attempt in range(max_retries + 1):
        try:
            resp = session.get(url, params=params, timeout=timeout)
            if resp.status_code >= 500:
                raise requests.HTTPError(f"HTTP {resp.status_code}")
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            last_exc = e
            # small backoff
            time.sleep(pause_sec * (attempt + 1))
    print(f"WARN: failed after retries for params={params}: {last_exc}")
    return None


def fetch_day(
    session: requests.Session,
    d: dt.date,
    pagesize: int,
    timeout: int,
    max_retries: int,
    pause_sec: float,
) -> List[Dict[str, Any]]:
    results: List[Dict[str, Any]] = []
    date_epoch = noon_utc_epoch(d)
    page = 0
    while True:
        params = {
            "pagesize": pagesize,
            "page": page,
            "parameters[date]": date_epoch,
        }
        data = request_with_retries(session, API_URL, params, timeout, max_retries, pause_sec)
        time.sleep(pause_sec)
        if not data:
            # Treat a failed page as no more results for this day to avoid infinite loops
            break
        page_results = data.get("results") or []
        if not page_results:
            break
        # Ensure each result has a uuid; skip malformed
        for item in page_results:
            if isinstance(item, dict) and item.get("uuid"):
                results.append(item)
        page += 1
    return results


def upload_json_to_s3(s3_client, bucket: str, key: str, obj: Any) -> None:
    body = json.dumps(obj, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    s3_client.put_object(
        Bucket=bucket, Key=key, Body=body, ContentType="application/json; charset=utf-8"
    )


def main() -> int:
    cfg = parse_args()
    session = boto3.Session(profile_name="SingleRegionAdminUser-545891282152")
    s3 = session.client("s3")
    session = requests.Session()

    total_days = (cfg.end_date - cfg.start_date).days + 1
    print(
        f"Downloading DOJ press releases {cfg.start_date} -> {cfg.end_date} ({total_days} days) to s3://{cfg.bucket}/{cfg.prefix}"
    )

    processed = 0
    total_items = 0
    for i in range(total_days):
        d = cfg.start_date + dt.timedelta(days=i)
        key = s3_key_for_date(cfg.prefix, d)
        try:
            day_results = fetch_day(
                session, d, cfg.pagesize, cfg.timeout, cfg.max_retries, cfg.pause_sec
            )
        except Exception as e:
            print(f"ERROR: fetch failed for {d}: {e}")
            day_results = []
        if not day_results and not cfg.write_empty:
            print(f"{d} -> 0 items (skipped write)")
        else:
            try:
                upload_json_to_s3(s3, cfg.bucket, key, day_results)
                print(f"{d} -> {len(day_results)} items -> s3://{cfg.bucket}/{key}")
                total_items += len(day_results)
            except (BotoCoreError, ClientError) as e:
                print(f"ERROR: S3 upload failed for {d} to {key}: {e}")
        processed += 1
    print(f"Done. Days processed: {processed}. Total items: {total_items}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
