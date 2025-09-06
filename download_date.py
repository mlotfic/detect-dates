# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 18:57:17 2025

@author: m
"""

import requests
import csv
import time
from datetime import datetime, timedelta
import json
import os

def fetch_hijri_data(date_str):
    """Fetch data from Aladhan API for a given date"""
    url = f"https://api.aladhan.com/v1/gToH/{date_str}?calendarMethod=HJCoSA"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {date_str}: {e}")
        return None

def safe_get(data, path, default=""):
    """Safely get nested dictionary values"""
    try:
        keys = path.split('.')
        result = data
        for key in keys:
            result = result[key]
        return result if result is not None else default
    except (KeyError, TypeError):
        return default

def process_date_data(api_data, gregorian_date=None):
    """Extract required fields from API response"""
    if not api_data or api_data.get('code') != 200:
        return None
    
    # Save response as JSON file for debugging if needed
    if gregorian_date:
        debug_dir = "debug_responses"
        os.makedirs(debug_dir, exist_ok=True)
        debug_file = os.path.join(debug_dir, f"response_{gregorian_date.replace('-', '_')}.json")
        with open(debug_file, 'w', encoding='utf-8') as f:
            json.dump(api_data, f, indent=2, ensure_ascii=False)
    
    data = api_data.get('data', {})
    hijri = data.get('hijri', {})
    
    # Extract relevant information
    processed_data = {
        'gregorian_date': gregorian_date,
        'hijri_date': safe_get(data, 'hijri.date'),
        'hijri_day': safe_get(data, 'hijri.day'),
        'hijri_month_number': safe_get(data, 'hijri.month.number'),
        'hijri_month_en': safe_get(data, 'hijri.month.en'),
        'hijri_month_ar': safe_get(data, 'hijri.month.ar'),
        'hijri_year': safe_get(data, 'hijri.year'),
        'hijri_weekday_en': safe_get(data, 'hijri.weekday.en'),
        'hijri_weekday_ar': safe_get(data, 'hijri.weekday.ar'),
        'hijri_designation': safe_get(data, 'hijri.designation.abbreviated'),
        'holidays': safe_get(data, 'hijri.holidays', [])
    }
    
    return processed_data

def generate_date_range(start_date, end_date):
    """Generate all dates between start and end date"""
    current = start_date
    while current <= end_date:
        yield current.strftime("%d-%m-%Y")
        current += timedelta(days=1)

def save_to_csv(data_list, filename="hijri_calendar_data.csv"):
    """Save processed data to CSV file"""
    if not data_list:
        print("No data to save")
        return
    
    fieldnames = [
        'gregorian_date', 'hijri_date', 'hijri_day', 'hijri_month_number',
        'hijri_month_en', 'hijri_month_ar', 'hijri_year', 'hijri_weekday_en',
        'hijri_weekday_ar', 'hijri_designation', 'holidays'
    ]
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data_list:
            # Convert holidays list to string for CSV
            if isinstance(row.get('holidays'), list):
                row['holidays'] = '; '.join(row['holidays'])
            writer.writerow(row)
    
    print(f"Data saved to {filename}")

def main():
    # Define date range
    start_date = datetime(622, 7, 19)  # 19-07-622 (First day of Hijri calendar)
    end_date = datetime.now()          # Today
    
    # For testing, you might want to use a smaller range
    # start_date = datetime(2024, 1, 1)
    # end_date = datetime(2024, 1, 31)
    
    print(f"Fetching Hijri data from {start_date.strftime('%d-%m-%Y')} to {end_date.strftime('%d-%m-%Y')}")
    print(f"Total days to process: {(end_date - start_date).days + 1}")
    
    all_data = []
    processed_count = 0
    error_count = 0
    cached_count = 0
    
    # Process each date
    for date_str in generate_date_range(start_date, end_date):
        print(f"Processing {date_str}...", end=' ')
        
        # Fetch data from API
        api_response = fetch_hijri_data(date_str)
        
        if api_response:
            # Process the data
            processed_data = process_date_data(api_response, date_str)
            
            if processed_data:
                all_data.append(processed_data)
                processed_count += 1
                print("✓")
            else:
                error_count += 1
                print("✗ (processing failed)")
        else:
            error_count += 1
            print("✗ (API error)")
        
        # Rate limiting - be respectful to the API
        time.sleep(0.1)  # 100ms delay between requests
        
        # Optional: Save progress periodically
        if processed_count > 0 and processed_count % 100 == 0:
            print(f"\nProgress: {processed_count} records processed, {cached_count} from cache, {error_count} errors")
            # Save intermediate results
            save_to_csv(all_data, f"hijri_data_partial_{processed_count}.csv")
    
    print(f"\nCompleted! Processed {processed_count} records ({cached_count} from cache) with {error_count} errors")
    
    # Save final results
    if all_data:
        save_to_csv(all_data, "hijri_calendar_complete.csv")
        
        # Save as JSON as well
        with open("hijri_calendar_complete.json", 'w', encoding='utf-8') as f:
            json.dump(all_data, f, indent=2, ensure_ascii=False)
        print("Data also saved as JSON file")
    
    print("\nSample of processed data:")
    for i, record in enumerate(all_data[:3]):  # Show first 3 records
        print(f"Record {i+1}: {record}")

if __name__ == "__main__":
    main()