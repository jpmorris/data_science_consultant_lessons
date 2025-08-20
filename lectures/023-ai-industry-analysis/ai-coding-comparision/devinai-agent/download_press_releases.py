#!/usr/bin/env python3
"""
Script to download Justice.gov press releases from 2016-01-01 to current date
and upload to S3 bucket.
"""

import requests
import json
import boto3
import time
from datetime import datetime, timedelta
from typing import List, Dict, Any
import logging
from botocore.exceptions import ClientError, NoCredentialsError

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class JusticeGovDownloader:
    def __init__(self, aws_profile: str = 'SingleRegionAdminUser-545891282152', 
                 bucket_name: str = None):
        self.base_url = "http://www.justice.gov"
        self.endpoint = "/api/v1/press_releases.json"
        self.aws_profile = aws_profile
        self.bucket_name = bucket_name
        self.session = requests.Session()
        self.s3_client = None
        
        self.request_delay = 0.1  # 100ms between requests
        
        self._setup_aws()
    
    def _setup_aws(self):
        """Initialize AWS S3 client with specified profile"""
        try:
            session = boto3.Session(profile_name=self.aws_profile)
            self.s3_client = session.client('s3')
            
            self.s3_client.list_buckets()
            logger.info(f"Successfully authenticated with AWS profile: {self.aws_profile}")
            
        except NoCredentialsError:
            logger.error(f"No AWS credentials found for profile: {self.aws_profile}")
            logger.error("Please configure AWS credentials using 'aws configure --profile {}'".format(self.aws_profile))
            raise
        except ClientError as e:
            logger.error(f"AWS authentication failed: {e}")
            raise
    
    def _date_to_timestamp(self, date_str: str) -> int:
        """Convert date string (YYYY-MM-DD) to Unix timestamp"""
        dt = datetime.strptime(date_str, '%Y-%m-%d')
        return int(dt.timestamp())
    
    def _get_date_range(self, start_date: str, end_date: str = None) -> List[str]:
        """Generate list of dates between start_date and end_date"""
        if end_date is None:
            end_date = datetime.now().strftime('%Y-%m-%d')
        
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        
        dates = []
        current = start
        while current <= end:
            dates.append(current.strftime('%Y-%m-%d'))
            current += timedelta(days=1)
        
        return dates
    
    def _fetch_page(self, date_str: str, page: int = 0, pagesize: int = 50) -> Dict[str, Any]:
        """Fetch a single page of press releases for a given date"""
        timestamp = self._date_to_timestamp(date_str)
        
        params = {
            'parameters[date]': timestamp,
            'page': page,
            'pagesize': pagesize
        }
        
        url = f"{self.base_url}{self.endpoint}"
        
        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            
            time.sleep(self.request_delay)
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch page {page} for date {date_str}: {e}")
            raise
    
    def download_date_data(self, date_str: str) -> List[Dict[str, Any]]:
        """Download all press releases for a specific date"""
        logger.info(f"Downloading data for {date_str}")
        
        all_results = []
        page = 0
        
        while True:
            try:
                data = self._fetch_page(date_str, page)
                
                results = data.get('results', [])
                if not results:
                    break
                
                all_results.extend(results)
                
                total_count = data.get('count', 0)
                current_count = len(all_results)
                
                logger.info(f"Date {date_str}, page {page}: got {len(results)} results, total so far: {current_count}")
                
                if current_count >= total_count:
                    break
                
                page += 1
                
            except Exception as e:
                logger.error(f"Error downloading page {page} for date {date_str}: {e}")
                break
        
        logger.info(f"Downloaded {len(all_results)} press releases for {date_str}")
        return all_results
    
    def upload_to_s3(self, data: List[Dict[str, Any]], date_str: str) -> bool:
        """Upload JSON data to S3 bucket"""
        if not self.bucket_name:
            logger.error("No S3 bucket name specified")
            return False
        
        if not data:
            logger.info(f"No data to upload for {date_str}")
            return True
        
        s3_key = f"press_releases_json/{date_str}.json"
        
        try:
            json_data = json.dumps(data, indent=2, ensure_ascii=False)
            
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=s3_key,
                Body=json_data.encode('utf-8'),
                ContentType='application/json'
            )
            
            logger.info(f"Successfully uploaded {len(data)} records to s3://{self.bucket_name}/{s3_key}")
            return True
            
        except ClientError as e:
            logger.error(f"Failed to upload to S3: {e}")
            return False
    
    def download_all_data(self, start_date: str = '2016-01-01', 
                         end_date: str = None, bucket_name: str = None):
        """Download all press releases from start_date to end_date and upload to S3"""
        if bucket_name:
            self.bucket_name = bucket_name
        
        if not self.bucket_name:
            raise ValueError("S3 bucket name must be specified")
        
        dates = self._get_date_range(start_date, end_date)
        logger.info(f"Processing {len(dates)} dates from {start_date} to {dates[-1]}")
        
        successful_uploads = 0
        failed_uploads = 0
        
        for i, date_str in enumerate(dates, 1):
            try:
                logger.info(f"Processing date {i}/{len(dates)}: {date_str}")
                
                data = self.download_date_data(date_str)
                
                if self.upload_to_s3(data, date_str):
                    successful_uploads += 1
                else:
                    failed_uploads += 1
                
                if i % 10 == 0:
                    logger.info(f"Progress: {i}/{len(dates)} dates processed")
                
            except Exception as e:
                logger.error(f"Failed to process date {date_str}: {e}")
                failed_uploads += 1
                continue
        
        logger.info(f"Download complete! Successful: {successful_uploads}, Failed: {failed_uploads}")


def main():
    """Main function to run the downloader"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Download Justice.gov press releases to S3')
    parser.add_argument('--start-date', default='2016-01-01', 
                       help='Start date (YYYY-MM-DD), default: 2016-01-01')
    parser.add_argument('--end-date', default=None,
                       help='End date (YYYY-MM-DD), default: current date')
    parser.add_argument('--bucket', required=True,
                       help='S3 bucket name to upload data to')
    parser.add_argument('--profile', default='SingleRegionAdminUser-545891282152',
                       help='AWS profile name')
    
    args = parser.parse_args()
    
    try:
        downloader = JusticeGovDownloader(aws_profile=args.profile, bucket_name=args.bucket)
        downloader.download_all_data(
            start_date=args.start_date,
            end_date=args.end_date,
            bucket_name=args.bucket
        )
        
    except Exception as e:
        logger.error(f"Script failed: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
