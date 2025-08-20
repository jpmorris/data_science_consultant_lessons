# Justice.gov Press Releases Data Pipeline

This repository contains two Python scripts for downloading and processing Justice Department press releases data.

## Scripts

### 1. download_press_releases.py
Downloads press releases from the Justice.gov API and uploads to S3.

**Usage:**
```bash
python3 download_press_releases.py --bucket your-bucket-name --start-date 2016-01-01
```

**Options:**
- `--bucket`: S3 bucket name (required)
- `--start-date`: Start date (YYYY-MM-DD), default: 2016-01-01
- `--end-date`: End date (YYYY-MM-DD), default: current date
- `--profile`: AWS profile name, default: SingleRegionAdminUser-545891282152

### 2. process_press_releases.py
Reads JSON files from S3, creates pandas DataFrame, and saves as CSV.

**Usage:**
```bash
python3 process_press_releases.py --bucket your-bucket-name
```

**Options:**
- `--bucket`: S3 bucket name (required)
- `--input-prefix`: S3 prefix for JSON files, default: press_releases_json/
- `--output-key`: S3 key for CSV output, default: press_releases_csv/all_press_releases.csv
- `--profile`: AWS profile name, default: SingleRegionAdminUser-545891282152

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure AWS credentials for the profile 'SingleRegionAdminUser-545891282152'

## Data Structure

The scripts will create the following S3 structure:
```
your-bucket/
├── press_releases_json/
│   ├── 2016-01-01.json
│   ├── 2016-01-02.json
│   └── ...
└── press_releases_csv/
    └── all_press_releases.csv
```

## API Information

- Base URL: http://www.justice.gov
- Endpoint: /api/v1/press_releases.json
- Rate limit: 10 requests per second
- Pagination: 50 results per page maximum
