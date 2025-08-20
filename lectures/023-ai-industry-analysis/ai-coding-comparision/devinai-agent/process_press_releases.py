#!/usr/bin/env python3
"""
Script to read JSON files from S3, create pandas dataframe, and save as CSV to S3.
"""

import boto3
import pandas as pd
import json
import logging
from typing import List, Dict, Any
from botocore.exceptions import ClientError, NoCredentialsError
from io import StringIO

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PressReleaseProcessor:
    def __init__(self, aws_profile: str = 'SingleRegionAdminUser-545891282152', 
                 bucket_name: str = None):
        self.aws_profile = aws_profile
        self.bucket_name = bucket_name
        self.s3_client = None
        
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
    
    def list_json_files(self, prefix: str = 'press_releases_json/') -> List[str]:
        """List all JSON files in the S3 bucket with given prefix"""
        try:
            response = self.s3_client.list_objects_v2(
                Bucket=self.bucket_name,
                Prefix=prefix
            )
            
            files = []
            if 'Contents' in response:
                for obj in response['Contents']:
                    if obj['Key'].endswith('.json'):
                        files.append(obj['Key'])
            
            logger.info(f"Found {len(files)} JSON files in s3://{self.bucket_name}/{prefix}")
            return files
            
        except ClientError as e:
            logger.error(f"Failed to list S3 objects: {e}")
            raise
    
    def read_json_from_s3(self, s3_key: str) -> List[Dict[str, Any]]:
        """Read JSON data from S3"""
        try:
            response = self.s3_client.get_object(Bucket=self.bucket_name, Key=s3_key)
            content = response['Body'].read().decode('utf-8')
            data = json.loads(content)
            
            logger.info(f"Read {len(data)} records from s3://{self.bucket_name}/{s3_key}")
            return data
            
        except ClientError as e:
            logger.error(f"Failed to read {s3_key} from S3: {e}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON from {s3_key}: {e}")
            raise
    
    def load_all_data(self, prefix: str = 'press_releases_json/') -> List[Dict[str, Any]]:
        """Load all JSON files from S3 and combine into single list"""
        json_files = self.list_json_files(prefix)
        
        if not json_files:
            logger.warning("No JSON files found in S3")
            return []
        
        all_data = []
        
        for i, s3_key in enumerate(json_files, 1):
            try:
                logger.info(f"Processing file {i}/{len(json_files)}: {s3_key}")
                data = self.read_json_from_s3(s3_key)
                all_data.extend(data)
                
                if i % 50 == 0:
                    logger.info(f"Progress: {i}/{len(json_files)} files processed, {len(all_data)} total records")
                
            except Exception as e:
                logger.error(f"Failed to process {s3_key}: {e}")
                continue
        
        logger.info(f"Loaded {len(all_data)} total press release records from {len(json_files)} files")
        return all_data
    
    def create_dataframe(self, data: List[Dict[str, Any]]) -> pd.DataFrame:
        """Convert list of dictionaries to pandas DataFrame"""
        if not data:
            logger.warning("No data to convert to DataFrame")
            return pd.DataFrame()
        
        logger.info("Converting data to pandas DataFrame...")
        
        df = pd.DataFrame(data)
        
        logger.info(f"Created DataFrame with {len(df)} rows and {len(df.columns)} columns")
        logger.info(f"Columns: {list(df.columns)}")
        
        date_columns = ['date', 'created', 'updated', 'published']
        for col in date_columns:
            if col in df.columns:
                try:
                    df[col] = pd.to_datetime(df[col], errors='coerce')
                    logger.info(f"Converted column '{col}' to datetime")
                except Exception as e:
                    logger.warning(f"Failed to convert column '{col}' to datetime: {e}")
        
        if 'date' in df.columns:
            df = df.sort_values('date')
            logger.info("Sorted DataFrame by date")
        
        return df
    
    def save_csv_to_s3(self, df: pd.DataFrame, s3_key: str) -> bool:
        """Save DataFrame as CSV to S3"""
        if df.empty:
            logger.warning("DataFrame is empty, nothing to save")
            return False
        
        try:
            csv_buffer = StringIO()
            df.to_csv(csv_buffer, index=False, encoding='utf-8')
            csv_content = csv_buffer.getvalue()
            
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=s3_key,
                Body=csv_content.encode('utf-8'),
                ContentType='text/csv'
            )
            
            logger.info(f"Successfully saved CSV with {len(df)} rows to s3://{self.bucket_name}/{s3_key}")
            return True
            
        except ClientError as e:
            logger.error(f"Failed to save CSV to S3: {e}")
            return False
        except Exception as e:
            logger.error(f"Error creating CSV: {e}")
            return False
    
    def process_all_data(self, bucket_name: str = None, 
                        input_prefix: str = 'press_releases_json/',
                        output_key: str = 'press_releases_csv/all_press_releases.csv'):
        """Main processing function: load JSON files, create DataFrame, save as CSV"""
        if bucket_name:
            self.bucket_name = bucket_name
        
        if not self.bucket_name:
            raise ValueError("S3 bucket name must be specified")
        
        logger.info("Starting press release data processing...")
        
        all_data = self.load_all_data(input_prefix)
        
        if not all_data:
            logger.error("No data loaded, cannot proceed")
            return False
        
        df = self.create_dataframe(all_data)
        
        if df.empty:
            logger.error("Failed to create DataFrame, cannot proceed")
            return False
        
        logger.info("DataFrame Statistics:")
        logger.info(f"  Total records: {len(df)}")
        if 'date' in df.columns:
            logger.info(f"  Date range: {df['date'].min()} to {df['date'].max()}")
        
        logger.info("Sample of data:")
        logger.info(df.head().to_string())
        
        success = self.save_csv_to_s3(df, output_key)
        
        if success:
            logger.info("Processing completed successfully!")
        else:
            logger.error("Processing failed during CSV save")
        
        return success


def main():
    """Main function to run the processor"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Process Justice.gov press releases from S3 JSON to CSV')
    parser.add_argument('--bucket', required=True,
                       help='S3 bucket name containing the JSON files')
    parser.add_argument('--input-prefix', default='press_releases_json/',
                       help='S3 prefix for input JSON files')
    parser.add_argument('--output-key', default='press_releases_csv/all_press_releases.csv',
                       help='S3 key for output CSV file')
    parser.add_argument('--profile', default='SingleRegionAdminUser-545891282152',
                       help='AWS profile name')
    
    args = parser.parse_args()
    
    try:
        processor = PressReleaseProcessor(aws_profile=args.profile, bucket_name=args.bucket)
        success = processor.process_all_data(
            bucket_name=args.bucket,
            input_prefix=args.input_prefix,
            output_key=args.output_key
        )
        
        return 0 if success else 1
        
    except Exception as e:
        logger.error(f"Script failed: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
