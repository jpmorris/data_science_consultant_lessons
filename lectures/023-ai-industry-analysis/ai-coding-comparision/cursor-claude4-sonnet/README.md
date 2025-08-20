# Justice Department Press Releases Data Pipeline

This repository contains two Python scripts for downloading press releases from the Justice
Department API and processing them into a structured format.

## Overview

1. **`download_press_releases.py`** - Downloads press releases from the Justice Department API and
   uploads them to S3
2. **`process_s3_data.py`** - Processes the JSON files from S3 and converts them to a pandas
   dataframe, then saves as CSV

## Prerequisites

- Python 3.7+
- AWS CLI configured with profile `SingleRegionAdminUser-545891282152`
- Access to S3 bucket (will be created automatically if it doesn't exist)

## Installation

1. Install the required Python packages:

```bash
pip install -r requirements.txt
```

2. Ensure your AWS credentials are properly configured in `~/.aws/config`:

```ini
[profile SingleRegionAdminUser-545891282152]
region = us-east-1
output = json
```

## Usage

### Step 1: Download Press Releases

Run the download script to fetch all press releases from 2016-01-01 to the current date:

```bash
python download_press_releases.py
```

This script will:

- Step through each date from 2016-01-01 to today
- For each date, paginate through all available press releases
- Download JSON payloads and concatenate them
- Upload each day's data to S3 in the `raw_data/YYYY-MM-DD/` folder structure
- Respect API rate limits (stays under 10 requests per second)

**Note**: This process may take several hours depending on the amount of data and your internet
connection.

### Step 2: Process Data

After the download is complete, run the processing script to convert all JSON files to a single CSV:

```bash
python process_s3_data.py
```

This script will:

- Download all JSON files from the S3 bucket
- Combine them into a single pandas dataframe
- Clean and normalize the data (remove HTML tags, convert timestamps, etc.)
- Save the final dataframe as a CSV file in the `processed_data/` folder in S3

## Data Structure

### Raw JSON Structure

Each press release contains fields such as:

- `title`: Press release title
- `body`: Full text content (HTML formatted)
- `date`: Publication date (Unix timestamp)
- `created`: Creation date
- `changed`: Last modified date
- `component`: Department/division information
- `topic`: Topic tags
- `url`: Link to the full press release
- `uuid`: Unique identifier

### Processed CSV Structure

The final CSV will contain:

- All original fields (cleaned of HTML)
- `source_date`: The date folder the data came from
- `source_file`: The S3 key of the source file
- `component_names`: Comma-separated component names
- `topic_names`: Comma-separated topic names
- Timestamps converted to readable datetime format

## S3 Bucket Structure

```
justice-press-releases/
├── raw_data/
│   ├── 2016-01-01/
│   │   └── press_releases.json
│   ├── 2016-01-02/
│   │   └── press_releases.json
│   └── ...
└── processed_data/
    └── press_releases.csv
```

## Configuration

### Customizing the Download

You can modify the following parameters in `download_press_releases.py`:

- **Start date**: Change the `start_date` parameter in the `download_all_press_releases()` call
- **S3 bucket name**: Modify the `bucket_name` variable in the `JusticeAPIDownloader` class
- **Rate limiting**: Adjust the `requests_per_second` variable (default: 8 to stay under API limit)

### Customizing the Processing

You can modify the following in `process_s3_data.py`:

- **S3 bucket name**: Change the `bucket_name` variable
- **Output path**: Modify the `output_key` parameter in `save_to_csv()`
- **Data cleaning**: Customize the `clean_dataframe()` method for your specific needs

## Error Handling

Both scripts include comprehensive error handling:

- API request failures are logged and the script continues
- S3 upload/download errors are logged with retry logic
- Rate limiting prevents API throttling
- Progress logging shows current status

## Monitoring

The scripts provide detailed logging output. Monitor the console for:

- Download progress by date
- Number of press releases found per date
- S3 upload status
- Data processing progress
- Any errors or warnings

## Troubleshooting

### Common Issues

1. **AWS Profile Not Found**: Ensure your AWS profile is correctly configured
2. **S3 Permission Errors**: Verify your AWS user has S3 read/write permissions
3. **API Rate Limiting**: The script automatically handles this, but if you see errors, reduce the
   `requests_per_second` value
4. **Memory Issues**: For very large datasets, consider processing data in chunks

### Logs

All operations are logged with timestamps. Check the console output for detailed information about
any failures.

## Performance Notes

- The download script processes approximately 8 requests per second to respect API limits
- Each date is processed sequentially to avoid overwhelming the API
- S3 uploads happen immediately after each date's data is downloaded
- The processing script downloads all JSON files from S3, so ensure you have sufficient bandwidth

## License

This project is provided as-is for educational and research purposes.
