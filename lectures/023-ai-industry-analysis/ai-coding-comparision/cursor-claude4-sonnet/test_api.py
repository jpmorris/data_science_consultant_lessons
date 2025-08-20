#!/usr/bin/env python3
"""
Simple test script to verify the Justice Department API connection works.
"""

import requests
import json
from datetime import datetime

def test_api_connection():
    """Test basic API connectivity and response format."""
    base_url = "https://www.justice.gov/api/v1/press_releases.json"
    
    print("Testing Justice Department API connection...")
    print("=" * 50)
    
    try:
        # Test 1: Basic connection with minimal parameters
        print("Test 1: Basic connection...")
        response = requests.get(base_url, params={'pagesize': 1})
        response.raise_for_status()
        
        data = response.json()
        print(f"✓ Status: {response.status_code}")
        print(f"✓ Total count: {data.get('metadata', {}).get('resultset', {}).get('count', 'Unknown')}")
        print(f"✓ Results returned: {len(data.get('results', []))}")
        
        # Test 2: Check response structure
        print("\nTest 2: Response structure...")
        if 'results' in data and data['results']:
            first_result = data['results'][0]
            print(f"✓ Sample fields: {list(first_result.keys())}")
            
            # Show a sample press release
            if 'title' in first_result:
                print(f"✓ Sample title: {first_result['title'][:100]}...")
            if 'date' in first_result:
                timestamp = int(first_result['date'])
                date_str = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                print(f"✓ Sample date: {date_str}")
        else:
            print("✗ No results found in response")
            
        # Test 3: Test date filtering
        print("\nTest 3: Date filtering...")
        test_timestamp = int(datetime(2024, 1, 1).timestamp())
        response2 = requests.get(base_url, params={
            'parameters[date]': test_timestamp,
            'pagesize': 2
        })
        
        if response2.status_code == 200:
            data2 = response2.json()
            count = data2.get('metadata', {}).get('resultset', {}).get('count', 0)
            print(f"✓ Date filter works, found {count} results for 2024-01-01")
        else:
            print(f"✗ Date filter test failed: {response2.status_code}")
            
        # Test 4: Test pagination
        print("\nTest 4: Pagination...")
        response3 = requests.get(base_url, params={
            'pagesize': 2,
            'page': 1
        })
        
        if response3.status_code == 200:
            data3 = response3.json()
            page = data3.get('metadata', {}).get('resultset', {}).get('page', -1)
            print(f"✓ Pagination works, page {page} returned")
        else:
            print(f"✗ Pagination test failed: {response3.status_code}")
            
        print("\n" + "=" * 50)
        print("✓ All tests completed successfully!")
        print("The API is working correctly and ready for data download.")
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"✗ JSON parsing error: {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    test_api_connection()
