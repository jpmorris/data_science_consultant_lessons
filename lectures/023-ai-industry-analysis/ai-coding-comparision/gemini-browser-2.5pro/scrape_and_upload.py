import json
from datetime import date, datetime, timedelta

import boto3
import requests


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def upload_to_s3(data, bucket, object_name, profile_name):
    """Upload a file to an S3 bucket"""
    session = boto3.Session(profile_name=profile_name)
    s3_client = session.client("s3")
    try:
        s3_client.put_object(Bucket=bucket, Key=object_name, Body=json.dumps(data))
        print(f"Successfully uploaded {object_name} to {bucket}")
    except Exception as e:
        print(f"Error uploading {object_name}: {e}")
        return False
    return True


def main():
    # Configuration
    base_url = "https://www.justice.gov/api/v1/press_releases.json"
    start_date = date(2016, 1, 1)
    end_date = date.today()
    bucket_name = "jmorris-test-ai-explore"  # <-- Replace with your bucket name
    folder_name = "press_releases_json-gemini"
    aws_profile = "SingleRegionAdminUser-545891282152"

    for single_date in daterange(start_date, end_date):
        print(f"Processing date: {single_date.strftime('%Y-%m-%d')}")
        all_data = []
        page = 0
        while True:
            # Convert date to timestamp
            timestamp = int(
                datetime.combine(single_date, datetime.min.time()).timestamp()
            )

            # API request with date and pagination
            params = {"parameters[date]": timestamp, "page": page}
            response = requests.get(base_url, params=params)

            if response.status_code == 200:
                data = response.json()
                if not data["results"]:
                    break  # No more results for this date
                all_data.extend(data["results"])
                page += 1
            else:
                print(
                    f"Error fetching data for {single_date.strftime('%Y-%m-%d')}, page {page}: {response.status_code}"
                )
                break

        if all_data:
            object_name = f"{folder_name}/{single_date.strftime('%Y-%m-%d')}.json"
            upload_to_s3(all_data, bucket_name, object_name, aws_profile)


if __name__ == "__main__":
    main()
