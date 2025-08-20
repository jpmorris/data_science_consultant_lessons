#!/usr/bin/env python3
"""
Comprehensive test script to understand the Justice.gov API structure
"""

import requests
import json
from datetime import datetime, timedelta

def test_justice_api():
    """Test the Justice.gov API endpoint comprehensively"""
    base_url = 'http://www.justice.gov'
    endpoint = '/api/v1/press_releases.json'
    
    print("=== Test 1: General API call (no date filter) ===")
    params1 = {
        'page': 0,
        'pagesize': 3
    }
    
    try:
        response = requests.get(f'{base_url}{endpoint}', params=params1, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        print(f'Status Code: {response.status_code}')
        print(f'Total Count: {data.get("count", "N/A")}')
        print(f'Results in this page: {len(data.get("results", []))}')
        
        if data.get("results"):
            sample_result = data["results"][0]
            print(f'Sample result keys: {list(sample_result.keys())}')
            print(f'Sample result (first 800 chars):')
            print(json.dumps(sample_result, indent=2)[:800] + "...")
            
            if 'date' in sample_result:
                print(f'Date field value: {sample_result["date"]}')
        
        print(f'Response structure keys: {list(data.keys())}')
        
    except Exception as e:
        print(f'General API test failed: {e}')
        return False
    
    print("\n" + "="*60 + "\n")
    
    test_dates = ['2023-12-01', '2023-01-15', '2022-06-01']
    
    for test_date in test_dates:
        print(f"=== Test with date filter ({test_date}) ===")
        timestamp = int(datetime.strptime(test_date, '%Y-%m-%d').timestamp())
        
        params2 = {
            'parameters[date]': timestamp,
            'page': 0,
            'pagesize': 3
        }
        
        try:
            print(f"Testing with date: {test_date} (timestamp: {timestamp})")
            response = requests.get(f'{base_url}{endpoint}', params=params2, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            print(f'Status Code: {response.status_code}')
            print(f'Total Count: {data.get("count", "N/A")}')
            print(f'Results in this page: {len(data.get("results", []))}')
            
            if data.get("results"):
                print("Found results with date filter!")
                sample = data["results"][0]
                if 'date' in sample:
                    print(f'Sample date from result: {sample["date"]}')
            else:
                print("No results with date filter")
                
        except Exception as e:
            print(f'Date filtered API test failed: {e}')
        
        print("-" * 40)
    
    return True

if __name__ == "__main__":
    test_justice_api()
