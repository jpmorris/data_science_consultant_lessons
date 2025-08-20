# DOJ Press Releases Downloader and Aggregator

This repo contains two small Python scripts to download DOJ press releases via the public API and
aggregate them from S3.

## Scripts

1. download_doj_press_releases.py

- Iterates dates from 2016-01-01 to today (default) and pages through DOJ
  `/api/v1/press_releases.json` using parameters[date]=<noon UTC epoch>.
- Writes one JSON file per day to S3 containing a list of press release objects.

2. aggregate_doj_press_releases.py

- Reads all daily JSONs from an input S3 prefix and builds a Pandas DataFrame.
- Writes a single CSV to an output S3 prefix.

## Setup

Install Python deps (prefer a venv):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Configure AWS credentials via environment, shared credentials, or IAM role.

## Usage

Download daily JSONs to S3:

```bash
python download_doj_press_releases.py --bucket <your-bucket> \
  --prefix raw/doj/press_releases \
  --start 2016-01-01 \
  --end $(date -u +%F)
```

Aggregate from S3 and write CSV:

```bash
python aggregate_doj_press_releases.py --bucket <your-bucket> \
  --in-prefix raw/doj/press_releases \
  --out-prefix curated/doj \
  --out-key press_releases.csv
```

## Notes

- DOJ API max pagesize is 50. The scripts respect that and default to ~5 requests/sec.
- Daily files are stored at `s3://<bucket>/raw/doj/press_releases/YYYY/MM/DD.json` by default.
- Aggregator coerces nested fields to JSON strings to keep a simple flat CSV.
