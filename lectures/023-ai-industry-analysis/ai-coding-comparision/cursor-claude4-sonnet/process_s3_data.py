#!/usr/bin/env python3
"""
Script to process JSON files from S3 bucket and convert them to a pandas dataframe.
Downloads all JSON files, combines them into a single dataframe, and saves as CSV to S3.
"""

import json
import boto3
import pandas as pd
from typing import List, Dict, Any
import logging
from io import StringIO
import tempfile
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class S3DataProcessor:
    def __init__(self, aws_profile: str = 'SingleRegionAdminUser-545891282152'):
        """Initialize the processor with AWS credentials."""
        self.s3_client = boto3.Session(profile_name=aws_profile).client('s3')
        self.bucket_name = "justice-press-releases"  # Same bucket as downloader
        
    def list_json_files(self, prefix: str = "raw_data/") -> List[str]:
        """List all JSON files in the S3 bucket with the given prefix."""
        try:
            paginator = self.s3_client.get_paginator('list_objects_v2')
            page_iterator = paginator.paginate(
                Bucket=self.bucket_name,
                Prefix=prefix
            )
            
            json_files = []
            for page in page_iterator:
                if 'Contents' in page:
                    for obj in page['Contents']:
                        if obj['Key'].endswith('.json'):
                            json_files.append(obj['Key'])
            
            logger.info(f"Found {len(json_files)} JSON files in S3")
            return json_files
            
        except Exception as e:
            logger.error(f"Error listing files in S3: {e}")
            return []
    
    def download_json_file(self, key: str) -> List[Dict[str, Any]]:
        """Download and parse a JSON file from S3."""
        try:
            response = self.s3_client.get_object(Bucket=self.bucket_name, Key=key)
            content = response['Body'].read().decode('utf-8')
            data = json.loads(content)
            
            if isinstance(data, list):
                return data
            else:
                logger.warning(f"Unexpected data format in {key}: {type(data)}")
                return []
                
        except Exception as e:
            logger.error(f"Error downloading {key}: {e}")
            return []
    
    def process_json_data(self, json_files: List[str]) -> pd.DataFrame:
        """Process all JSON files and combine them into a single dataframe."""
        all_data = []
        
        for i, key in enumerate(json_files):
            logger.info(f"Processing file {i+1}/{len(json_files)}: {key}")
            
            # Extract date from key for reference
            date_str = key.split('/')[1] if len(key.split('/')) > 1 else "unknown"
            
            # Download and parse JSON
            releases = self.download_json_file(key)
            
            if releases:
                # Add source date information
                for release in releases:
                    release['source_date'] = date_str
                    release['source_file'] = key
                
                all_data.extend(releases)
                logger.info(f"Added {len(releases)} records from {key}")
            else:
                logger.warning(f"No data found in {key}")
        
        if not all_data:
            logger.warning("No data found in any JSON files")
            return pd.DataFrame()
        
        # Convert to dataframe
        df = pd.DataFrame(all_data)
        
        # Clean up the dataframe
        df = self.clean_dataframe(df)
        
        logger.info(f"Created dataframe with {len(df)} rows and {len(df.columns)} columns")
        return df
    
    def clean_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean and normalize the dataframe."""
        # Convert timestamp fields to datetime
        timestamp_columns = ['date', 'created', 'changed']
        for col in timestamp_columns:
            if col in df.columns:
                try:
                    # Convert Unix timestamps to datetime
                    df[col] = pd.to_datetime(df[col], unit='s', errors='coerce')
                except:
                    # If not Unix timestamp, try parsing as string
                    df[col] = pd.to_datetime(df[col], errors='coerce')
        
        # Clean up HTML content in text fields
        text_columns = ['body', 'teaser', 'title']
        for col in text_columns:
            if col in df.columns:
                df[col] = df[col].astype(str).str.replace('<[^<]+?>', '', regex=True)
                df[col] = df[col].str.replace('&amp;', '&')
                df[col] = df[col].str.replace('&quot;', '"')
                df[col] = df[col].str.replace('&#39;', "'")
                df[col] = df[col].str.replace('&lt;', '<')
                df[col] = df[col].str.replace('&gt;', '>')
        
        # Handle component and topic fields (convert from list of dicts to strings)
        if 'component' in df.columns:
            df['component_names'] = df['component'].apply(
                lambda x: ', '.join([item.get('name', '') for item in x]) if isinstance(x, list) else str(x)
            )
        
        if 'topic' in df.columns:
            df['topic_names'] = df['topic'].apply(
                lambda x: ', '.join([item.get('name', '') for item in x]) if isinstance(x, list) else str(x)
            )
        
        # Remove columns with mostly empty values
        threshold = len(df) * 0.1  # Keep columns with at least 10% non-null values
        df = df.dropna(axis=1, thresh=threshold)
        
        return df
    
    def save_to_csv(self, df: pd.DataFrame, output_key: str = "processed_data/press_releases.csv") -> bool:
        """Save the dataframe as CSV to S3."""
        try:
            # Create a temporary file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as temp_file:
                # Save dataframe to CSV
                df.to_csv(temp_file.name, index=False, encoding='utf-8')
                temp_file_path = temp_file.name
            
            # Upload to S3
            with open(temp_file_path, 'rb') as file_obj:
                self.s3_client.upload_fileobj(
                    file_obj,
                    self.bucket_name,
                    output_key,
                    ExtraArgs={'ContentType': 'text/csv'}
                )
            
            # Clean up temporary file
            os.unlink(temp_file_path)
            
            logger.info(f"Successfully saved CSV to s3://{self.bucket_name}/{output_key}")
            return True
            
        except Exception as e:
            logger.error(f"Error saving CSV to S3: {e}")
            return False
    
    def process_all_data(self) -> pd.DataFrame:
        """Main method to process all data from S3."""
        logger.info("Starting data processing from S3...")
        
        # List all JSON files
        json_files = self.list_json_files()
        
        if not json_files:
            logger.error("No JSON files found in S3 bucket")
            return pd.DataFrame()
        
        # Process all JSON files
        df = self.process_json_data(json_files)
        
        if df.empty:
            logger.error("No data could be processed")
            return df
        
        # Save to CSV
        success = self.save_to_csv(df)
        
        if success:
            logger.info("Data processing completed successfully!")
        else:
            logger.error("Failed to save CSV to S3")
        
        return df

def main():
    """Main function to run the data processor."""
    try:
        processor = S3DataProcessor()
        df = processor.process_all_data()
        
        if not df.empty:
            logger.info(f"Final dataframe shape: {df.shape}")
            logger.info(f"Columns: {list(df.columns)}")
            logger.info(f"Sample data:\n{df.head()}")
        else:
            logger.warning("No data was processed")
            
    except Exception as e:
        logger.error(f"Data processing failed: {e}")
        raise

if __name__ == "__main__":
    main()
