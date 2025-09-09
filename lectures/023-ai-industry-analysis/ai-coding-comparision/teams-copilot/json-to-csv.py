import json
from pathlib import Path

import boto3
import pandas as pd

AWS_PROFILE = "SingleRegionAdminUser-545891282152"
BUCKET_NAME = "jmorris-test-ai-explore"
IMPORT_FOLDER = "press_releases_json-copilot"
EXPORT_CSV_FOLDER = "press_releases_csv-copilot"

# Set AWS profile
session = boto3.Session(profile_name=AWS_PROFILE)
s3 = session.client("s3")

# List objects in the import folder
objects = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=IMPORT_FOLDER)

dataframes = []
for obj in objects.get("Contents", []):
    key = obj["Key"]
    if key.endswith(".json"):
        response = s3.get_object(Bucket=BUCKET_NAME, Key=key)
        content = response["Body"].read()
        json_data = json.loads(content)
        df = pd.DataFrame(json_data)
        dataframes.append(df)

# Concatenate all dataframes
final_df = pd.concat(dataframes, ignore_index=True)

# Save to CSV locally
Path(EXPORT_CSV_FOLDER).mkdir(exist_ok=True)
csv_filename = f"{EXPORT_CSV_FOLDER}/press_releases_combined.csv"
final_df.to_csv(csv_filename, index=False)

# Upload CSV to S3
s3.upload_file(csv_filename, BUCKET_NAME, f"{EXPORT_CSV_FOLDER}/{Path(csv_filename).name}")
print(f"Uploaded CSV to S3: {csv_filename}")
