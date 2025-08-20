#!/usr/bin/env python3
"""
Script to download press releases from the Justice Department API and upload to S3.
Downloads data from 2016-01-01 to current date, paginating through all results.
"""

import json
import time
import boto3
from datetime import datetime, timedelta
import requests
from typing import List, Dict, Any
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class JusticeAPIDownloader:
    def __init__(self, aws_profile: str = 'SingleRegionAdminUser-545891282152'):
        """Initialize the downloader with AWS credentials."""
        self.base_url = "https://www.justice.gov/api/v1/press_releases.json"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        # Initialize S3 client
        self.s3_client = boto3.Session(profile_name=aws_profile).client('s3')
        
        # Rate limiting
        self.requests_per_second = 8  # Stay under the 10 req/sec limit
        self.min_delay = 1.0 / self.requests_per_second
        
    def date_to_timestamp(self, date_obj: datetime) -> int:
        """Convert datetime to Unix timestamp."""
        return int(date_obj.timestamp())
    
    def timestamp_to_date(self, timestamp: int) -> str:
        """Convert Unix timestamp to date string."""
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    
    def get_press_releases_for_date(self, date_obj: datetime) -> List[Dict[str, Any]]:
        """Get all press releases for a specific date."""
        timestamp = self.date_to_timestamp(date_obj)
        all_releases = []
        page = 0
        pagesize = 50  # Maximum allowed by API
        
        while True:
            try:
                # Build URL with parameters
                params = {
                    'parameters[date]': timestamp,
                    'pagesize': pagesize,
                    'page': page,
                    'sort': 'date',
                    'direction': 'ASC'
                }
                
                logger.info(f"Fetching page {page} for date {date_obj.strftime('%Y-%m-%d')}")
                
                response = self.session.get(self.base_url, params=params)
                response.raise_for_status()
                
                data = response.json()
                
                # Check if we have results
                if not data.get('results'):
                    logger.info(f"No results for date {date_obj.strftime('%Y-%m-%d')}")
                    break
                
                # Add results to our collection
                releases = data['results']
                all_releases.extend(releases)
                
                # Check if we've reached the end
                metadata = data.get('metadata', {})
                resultset = metadata.get('resultset', {})
                total_count = int(resultset.get('count', 0))
                current_page = int(resultset.get('page', 0))
                
                logger.info(f"Page {page}: Got {len(releases)} releases, total count: {total_count}")
                
                # If we've processed all results, break
                if len(all_releases) >= total_count:
                    break
                
                page += 1
                
                # Rate limiting
                time.sleep(self.min_delay)
                
            except requests.exceptions.RequestException as e:
                logger.error(f"Error fetching page {page} for date {date_obj.strftime('%Y-%m-%d')}: {e}")
                break
            except json.JSONDecodeError as e:
                logger.error(f"Error parsing JSON for page {page}: {e}")
                break
            except Exception as e:
                logger.error(f"Unexpected error for page {page}: {e}")
                break
        
        return all_releases
    
    def download_all_press_releases(self, start_date: str = "2016-01-01") -> None:
        """Download all press releases from start_date to current date."""
        start_dt = datetime.strptime(start_date, "%Y-%m-%d")
        end_dt = datetime.now()
        
        current_dt = start_dt
        
        while current_dt <= end_dt:
            date_str = current_dt.strftime('%Y-%m-%d')
            logger.info(f"Processing date: {date_str}")
            
            # Get all releases for this date
            releases = self.get_press_releases_for_date(current_dt)
            
            if releases:
                # Upload to S3
                self.upload_to_s3(releases, date_str)
                logger.info(f"Uploaded {len(releases)} releases for {date_str}")
            else:
                logger.info(f"No releases found for {date_str}")
            
            # Move to next date
            current_dt += timedelta(days=1)
            
            # Small delay between dates to be respectful
            time.sleep(0.5)
    
    def upload_to_s3(self, releases: List[Dict[str, Any]], date_str: str) -> None:
        """Upload press releases to S3 bucket."""
        bucket_name = "justice-press-releases"  # You can change this
        key = f"raw_data/{date_str}/press_releases.json"
        
        try:
            # Convert to JSON string
            json_data = json.dumps(releases, indent=2, ensure_ascii=False)
            
            # Upload to S3
            self.s3_client.put_object(
                Bucket=bucket_name,
                Key=key,
                Body=json_data.encode('utf-8'),
                ContentType='application/json'
            )
            
            logger.info(f"Successfully uploaded to s3://{bucket_name}/{key}")
            
        except Exception as e:
            logger.error(f"Error uploading to S3 for {date_str}: {e}")
            # Try to create bucket if it doesn't exist
            try:
                self.s3_client.create_bucket(Bucket=bucket_name)
                logger.info(f"Created bucket: {bucket_name}")
                # Retry upload
                self.upload_to_s3(releases, date_str)
            except Exception as create_error:
                logger.error(f"Could not create bucket: {create_error}")

def main():
    """Main function to run the downloader."""
    try:
        downloader = JusticeAPIDownloader()
        downloader.download_all_press_releases()
        logger.info("Download completed successfully!")
    except Exception as e:
        logger.error(f"Download failed: {e}")
        raise

if __name__ == "__main__":
    main()
