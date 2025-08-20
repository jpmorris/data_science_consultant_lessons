#!/usr/bin/env python3
"""
Aggregate daily DOJ press releases JSON files from S3 into a single Pandas DataFrame and write CSV back to S3.

Behavior:
- Reads all JSON files under a given input prefix in an S3 bucket. Each file is a list[dict] (one day's results).
- Concatenates into a DataFrame; normalizes nested fields minimally (keeps dict/list as JSON strings unless normalized).
- Writes a CSV to a target prefix and filename in the same bucket.

Usage:
  python aggregate_doj_press_releases.py --bucket <bucket> --in-prefix raw/doj/press_releases --out-prefix curated/doj --out-key press_releases.csv

Notes:
- Uses boto3 S3 list_objects_v2 pagination. Assumes files end with .json.
- If you have many files, consider running where you have good bandwidth to S3.
"""

from __future__ import annotations

import argparse
import io
import json
import os
import sys
from typing import Any, Dict, List

import boto3
import pandas as pd
from botocore.exceptions import BotoCoreError, ClientError


def parse_args():
    p = argparse.ArgumentParser(
        description="Aggregate DOJ press releases JSONs from S3 and write CSV"
    )
    p.add_argument(
        "--bucket",
        default=os.getenv("DOJ_S3_BUCKET"),
        help="S3 bucket name (or DOJ_S3_BUCKET)",
    )
    p.add_argument(
        "--in-prefix",
        default=os.getenv("DOJ_IN_PREFIX", "raw/doj/press_releases"),
        help="Input S3 prefix containing daily JSONs",
    )
    p.add_argument(
        "--out-prefix",
        default=os.getenv("DOJ_OUT_PREFIX", "curated/doj"),
        help="Output S3 prefix for the CSV",
    )
    p.add_argument(
        "--out-key",
        default=os.getenv("DOJ_OUT_KEY", "press_releases.csv"),
        help="Output CSV key name under out-prefix",
    )
    p.add_argument(
        "--max-keys",
        type=int,
        default=int(os.getenv("DOJ_MAX_KEYS", "1000")),
        help="Max keys per page for S3 listing",
    )
    p.add_argument(
        "--limit",
        type=int,
        default=int(os.getenv("DOJ_LIMIT", "0")),
        help="If >0, limit number of files for testing",
    )
    args = p.parse_args()

    if not args.bucket:
        print("ERROR: --bucket is required", file=sys.stderr)
        sys.exit(2)
    return args


def list_json_keys(s3_client, bucket: str, prefix: str, max_keys: int, limit: int = 0) -> List[str]:
    keys: List[str] = []
    continuation_token = None
    while True:
        kwargs = {"Bucket": bucket, "Prefix": prefix, "MaxKeys": max_keys}
        if continuation_token:
            kwargs["ContinuationToken"] = continuation_token
        resp = s3_client.list_objects_v2(**kwargs)
        contents = resp.get("Contents", [])
        for obj in contents:
            key = obj["Key"]
            if key.lower().endswith(".json"):
                keys.append(key)
                if limit and len(keys) >= limit:
                    return keys
        if resp.get("IsTruncated"):
            continuation_token = resp.get("NextContinuationToken")
        else:
            break
    return keys


def read_json_list(s3_client, bucket: str, key: str) -> List[Dict[str, Any]]:
    try:
        obj = s3_client.get_object(Bucket=bucket, Key=key)
        data = obj["Body"].read()
        return json.loads(data)
    except (BotoCoreError, ClientError, json.JSONDecodeError) as e:
        print(f"WARN: failed to read/parse {key}: {e}")
        return []


def coerce_for_csv(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    # Convert list/dict fields to JSON strings to avoid DataFrame exploding
    out: List[Dict[str, Any]] = []
    for rec in records:
        new_rec = {}
        for k, v in rec.items():
            if isinstance(v, (dict, list)):
                try:
                    new_rec[k] = json.dumps(v, ensure_ascii=False)
                except Exception:
                    new_rec[k] = str(v)
            else:
                new_rec[k] = v
        out.append(new_rec)
    return out


def main() -> int:
    args = parse_args()
    session = boto3.Session(profile_name="SingleRegionAdminUser-545891282152")
    s3 = session.client("s3")

    in_prefix = args.in_prefix.strip("/")
    out_prefix = args.out_prefix.strip("/")
    out_key = f"{out_prefix}/{args.out_key}"

    print(f"Listing JSONs in s3://{args.bucket}/{in_prefix} ...")
    keys = list_json_keys(s3, args.bucket, in_prefix, max_keys=args.max_keys, limit=args.limit)
    if not keys:
        print("No JSON files found to aggregate.")
        return 1
    print(f"Found {len(keys)} files.")

    all_records: List[Dict[str, Any]] = []
    for i, key in enumerate(keys, 1):
        records = read_json_list(s3, args.bucket, key)
        if records:
            all_records.extend(records)
        if i % 100 == 0:
            print(f"Read {i}/{len(keys)} files, records so far: {len(all_records)}")

    if not all_records:
        print("No records after reading files.")
        return 1

    print(f"Building DataFrame with {len(all_records)} records ...")
    coerced = coerce_for_csv(all_records)
    df = pd.DataFrame(coerced)

    # Optional: ensure some consistent column order if present
    preferred = [
        "uuid",
        "date",
        "title",
        "url",
        "created",
        "changed",
        "component",
        "topic",
        "teaser",
        "body",
        "attachment",
        "image",
        "number",
    ]
    cols = [c for c in preferred if c in df.columns] + [c for c in df.columns if c not in preferred]
    df = df[cols]

    print(f"Writing CSV to s3://{args.bucket}/{out_key} ...")
    csv_buf = io.StringIO()
    df.to_csv(csv_buf, index=False)
    data = csv_buf.getvalue().encode("utf-8")

    try:
        s3.put_object(
            Bucket=args.bucket,
            Key=out_key,
            Body=data,
            ContentType="text/csv; charset=utf-8",
        )
    except (BotoCoreError, ClientError) as e:
        print(f"ERROR: failed to write CSV: {e}")
        return 1

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
