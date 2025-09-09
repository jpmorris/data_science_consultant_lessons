import requests
import boto3
import json
from datetime import datetime, timedelta
import os

# CONFIGURATION
S3_BUCKET = 'your-s3-bucket-name'
S3_PREFIX = 'press_releases_json/'  # Folder in S3 for JSON files
START_DATE = datetime(2016, 1, 1)
END_DATE = datetime.now()
API_URL = 'https://www.justice.gov/api/v1/press_releases.json'
AWS_REGION = 'us-east-1'  # Change if needed

# Initialize S3 client
s3 = boto3.client('s3', region_name=AWS_REGION)

def fetch_press_releases_for_date(date_str):
    all_results = []
    page = 0
    while True:
        params = {
            'date': date_str,
            'page': page
        }
        resp = requests.get(API_URL, params=params)
        if resp.status_code != 200:
            print(f"Failed for {date_str} page {page}: {resp.status_code}")
            break
        data = resp.json()
        results = data.get('results', [])
        if not results:
            break
        all_results.extend(results)
        if not data.get('next_page'):
            break
        page += 1
    return all_results

def main():
    current_date = START_DATE
    while current_date <= END_DATE:
        date_str = current_date.strftime('%Y-%m-%d')
        print(f"Fetching {date_str}")
        results = fetch_press_releases_for_date(date_str)
        if results:
            json_bytes = json.dumps(results).encode('utf-8')
            s3_key = f"{S3_PREFIX}{date_str}.json"
            s3.put_object(Bucket=S3_BUCKET, Key=s3_key, Body=json_bytes)
            print(f"Uploaded {s3_key} ({len(results)} records)")
        current_date += timedelta(days=1)

if __name__ == "__main__":
    main()
