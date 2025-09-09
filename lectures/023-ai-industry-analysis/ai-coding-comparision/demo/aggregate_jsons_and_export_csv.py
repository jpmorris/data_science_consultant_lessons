import boto3
import pandas as pd
import json
import os
from io import BytesIO

# CONFIGURATION
S3_BUCKET = 'your-s3-bucket-name'
S3_PREFIX = 'press_releases_json/'  # Folder in S3 for JSON files
S3_CSV_PREFIX = 'press_releases_csv/'  # Folder in S3 for CSV files
AWS_REGION = 'us-east-1'  # Change if needed

# Initialize S3 client
s3 = boto3.client('s3', region_name=AWS_REGION)

def list_json_files():
    paginator = s3.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=S3_BUCKET, Prefix=S3_PREFIX)
    files = []
    for page in pages:
        for obj in page.get('Contents', []):
            if obj['Key'].endswith('.json'):
                files.append(obj['Key'])
    return files

def read_json_from_s3(key):
    obj = s3.get_object(Bucket=S3_BUCKET, Key=key)
    return json.loads(obj['Body'].read())

def main():
    files = list_json_files()
    all_records = []
    for key in files:
        print(f"Reading {key}")
        records = read_json_from_s3(key)
        all_records.extend(records)
    df = pd.DataFrame(all_records)
    csv_buffer = BytesIO()
    df.to_csv(csv_buffer, index=False)
    csv_key = f"{S3_CSV_PREFIX}press_releases_all.csv"
    s3.put_object(Bucket=S3_BUCKET, Key=csv_key, Body=csv_buffer.getvalue())
    print(f"Uploaded CSV to {csv_key}")

if __name__ == "__main__":
    main()
