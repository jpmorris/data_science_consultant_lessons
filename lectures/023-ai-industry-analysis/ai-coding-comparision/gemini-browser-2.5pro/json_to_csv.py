import json
from io import StringIO

import boto3
import pandas as pd


def main():
    # Configuration
    bucket_name = "jmorris-test-ai-explore"  # <-- Replace with your bucket name
    source_folder = "press_releases_json-gemini/"
    destination_folder = "press_releases_csv-gemini/"
    aws_profile = "SingleRegionAdminUser-545891282152"

    session = boto3.Session(profile_name=aws_profile)
    s3_client = session.client("s3")

    # Get a list of all JSON files in the source folder
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=source_folder)
    files = [item["Key"] for item in response.get("Contents", [])]

    all_data = []
    for file in files:
        print(f"Processing file: {file}")
        obj = s3_client.get_object(Bucket=bucket_name, Key=file)
        data = json.loads(obj["Body"].read().decode("utf-8"))
        all_data.extend(data)

    if all_data:
        # Create a pandas DataFrame
        df = pd.DataFrame(all_data)

        # Save the DataFrame as a CSV in memory
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)

        # Upload the CSV to the destination folder
        csv_object_name = f"{destination_folder}all_press_releases.csv"
        s3_client.put_object(
            Bucket=bucket_name, Key=csv_object_name, Body=csv_buffer.getvalue()
        )
        print(f"Successfully uploaded {csv_object_name} to {bucket_name}")


if __name__ == "__main__":
    main()
