import json
import time
from datetime import datetime, timedelta
from pathlib import Path

import boto3
import requests

# Constants
START_DATE = datetime(2016, 1, 1)
END_DATE = datetime.now()
BASE_URL = "https://www.justice.gov/api/v1/press_releases.json"
PAGE_SIZE = 50
AWS_PROFILE = "SingleRegionAdminUser-545891282152"
BUCKET_NAME = "jmorris-test-ai-explore"
EXPORT_FOLDER = "press_releases_json-copilot"

# Set AWS profile
session = boto3.Session(profile_name=AWS_PROFILE)
s3 = session.client("s3")

# Create local temp folder
Path(EXPORT_FOLDER).mkdir(exist_ok=True)

all_data = []
current_date = START_DATE

while current_date <= END_DATE:
    timestamp = int(time.mktime(current_date.timetuple()))
    page = 0
    while True:
        params = {"parameters[date]": timestamp, "pagesize": PAGE_SIZE, "page": page}
        response = requests.get(BASE_URL, params=params)
        if response.status_code != 200:
            break
        data = response.json()
        results = data.get("results", [])
        if not results:
            break
        all_data.extend(results)
        page += 1
        time.sleep(0.1)  # Respect rate limit
    current_date += timedelta(days=1)

# Save to local JSON file
json_filename = f"{EXPORT_FOLDER}/press_releases_{START_DATE.date()}_to_{END_DATE.date()}.json"
with open(json_filename, "w") as f:
    json.dump(all_data, f)

# Upload to S3
s3.upload_file(json_filename, BUCKET_NAME, f"{EXPORT_FOLDER}/{Path(json_filename).name}")
print(f"Uploaded to S3: {json_filename}")
