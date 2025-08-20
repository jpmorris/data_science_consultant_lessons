#!/usr/bin/env python3
"""
Demonstration script showing how to use the Justice.gov press releases scripts
"""

import subprocess
import sys
import os

def demonstrate_usage():
    """Demonstrate how to use both scripts"""
    print("Justice.gov Press Releases Data Pipeline - Usage Demo")
    print("=" * 60)
    
    print("\n1. SETUP REQUIREMENTS:")
    print("   - Install dependencies: pip install -r requirements.txt")
    print("   - Configure AWS credentials for profile 'SingleRegionAdminUser-545891282152'")
    print("   - Have an S3 bucket ready")
    
    print("\n2. DOWNLOAD SCRIPT USAGE:")
    print("   Download all data from 2016-01-01 to current date:")
    print("   python3 download_press_releases.py --bucket YOUR_BUCKET_NAME")
    print()
    print("   Download specific date range:")
    print("   python3 download_press_releases.py --bucket YOUR_BUCKET_NAME --start-date 2022-01-01 --end-date 2022-12-31")
    print()
    print("   Test with small range (recommended first):")
    print("   python3 download_press_releases.py --bucket YOUR_BUCKET_NAME --start-date 2022-06-01 --end-date 2022-06-03")
    
    print("\n3. PROCESSING SCRIPT USAGE:")
    print("   Process all JSON files to CSV:")
    print("   python3 process_press_releases.py --bucket YOUR_BUCKET_NAME")
    print()
    print("   Custom input/output locations:")
    print("   python3 process_press_releases.py --bucket YOUR_BUCKET_NAME --input-prefix custom_json/ --output-key custom_csv/data.csv")
    
    print("\n4. EXPECTED S3 STRUCTURE AFTER RUNNING:")
    print("   YOUR_BUCKET_NAME/")
    print("   ├── press_releases_json/")
    print("   │   ├── 2016-01-01.json")
    print("   │   ├── 2016-01-02.json")
    print("   │   └── ... (one file per day)")
    print("   └── press_releases_csv/")
    print("       └── all_press_releases.csv")
    
    print("\n5. SCRIPT FEATURES:")
    print("   Download Script:")
    print("   - Handles API rate limiting (10 requests/second)")
    print("   - Processes pagination automatically")
    print("   - Robust error handling and logging")
    print("   - Uploads one JSON file per date to S3")
    print()
    print("   Processing Script:")
    print("   - Reads all JSON files from S3")
    print("   - Creates unified pandas DataFrame")
    print("   - Handles date conversion and sorting")
    print("   - Saves as CSV to different S3 location")
    
    print("\n6. MONITORING:")
    print("   Both scripts provide detailed logging output")
    print("   Progress updates every 10 dates (download) or 50 files (processing)")
    print("   Error handling with continuation on individual failures")

if __name__ == "__main__":
    demonstrate_usage()
