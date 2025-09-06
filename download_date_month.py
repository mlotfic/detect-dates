# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 22:01:45 2025

@author: m
"""

import requests
import csv
import time
from datetime import datetime, timedelta
import json
import os

def fetch_hijri_month_data(month, year):
    """Fetch data from Aladhan API for a given Hijri month and year"""
    url = f"https://api.aladhan.com/v1/hToGCalendar/{month}/{year}?calendarMethod=HJCoSA"
    
    try:
        response = requests.get(url, headers={'accept': 'application/json'})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {month}/{year}: {e}")
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

def check_cached_month_response(month, year):
    """Check if response file exists for a given month/year and load it"""
    debug_dir = "debug_responses_month"
    debug_file = os.path.join(debug_dir, f"month_response_{month}_{year}.json")
    
    if os.path.exists(debug_file):
        try:
            with open(debug_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading cached file {debug_file}: {e}")
            return None
    return None

def process_month_data(api_data, month=None, year=None):
    """Extract required fields from API response for all days in the month"""
    if not api_data or api_data.get('code') != 200:
        return None
    
    # Save response as JSON file for debugging if needed
    if month and year:
        debug_dir = "debug_responses_month"
        os.makedirs(debug_dir, exist_ok=True)
        debug_file = os.path.join(debug_dir, f"month_response_{month}_{year}.json")
        with open(debug_file, 'w', encoding='utf-8') as f:
            json.dump(api_data, f, indent=2, ensure_ascii=False)
    
    data = api_data.get('data', [])
    processed_month_data = []
    
    # Process each day in the month
    for day_data in data:
        gregorian = day_data.get('gregorian', {})
        hijri = day_data.get('hijri', {})
        
        # Extract relevant information for each day
        processed_day = {
            'gregorian_date': safe_get(day_data, 'gregorian.date'),
            'gregorian_day': safe_get(day_data, 'gregorian.day'),
            'gregorian_month_number': safe_get(day_data, 'gregorian.month.number'),
            'gregorian_month_en': safe_get(day_data, 'gregorian.month.en'),
            'gregorian_year': safe_get(day_data, 'gregorian.year'),
            'gregorian_weekday_en': safe_get(day_data, 'gregorian.weekday.en'),
            'hijri_date': safe_get(day_data, 'hijri.date'),
            'hijri_day': safe_get(day_data, 'hijri.day'),
            'hijri_month_number': safe_get(day_data, 'hijri.month.number'),
            'hijri_month_en': safe_get(day_data, 'hijri.month.en'),
            'hijri_month_ar': safe_get(day_data, 'hijri.month.ar'),
            'hijri_year': safe_get(day_data, 'hijri.year'),
            'hijri_weekday_en': safe_get(day_data, 'hijri.weekday.en'),
            'hijri_weekday_ar': safe_get(day_data, 'hijri.weekday.ar'),
            'hijri_designation': safe_get(day_data, 'hijri.designation.abbreviated'),
            'holidays': safe_get(day_data, 'hijri.holidays', [])
        }
        
        processed_month_data.append(processed_day)
    
    return processed_month_data

def generate_hijri_month_range(start_year, end_year):
    """Generate all Hijri months between start and end year"""
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):  # Hijri months 1-12
            yield month, year


def main():
    # Define Hijri year range
    start_hijri_year = 1182  # Year 1 AH (622 CE)
    end_hijri_year = 1500  # Current approximate Hijri year (2025 CE)
    
    # For testing, you might want to use a smaller range
    # start_hijri_year = 1445
    # end_hijri_year = 1446
    
    print(f"Fetching Hijri calendar data from year {start_hijri_year} to {end_hijri_year}")
    total_months = (end_hijri_year - start_hijri_year + 1) * 12
    print(f"Total months to process: {total_months}")
    
    processed_months = 0
    processed_days = 0
    error_count = 0
    cached_count = 0
    
    # Process each month
    for month, year in generate_hijri_month_range(start_hijri_year, end_hijri_year):
        print(f"Processing Hijri {month}/{year}...", end=' ')
        
        # First, check if we have a cached response
        api_response = check_cached_month_response(month, year)
        
        if api_response:
            print("(cached)", end=' ')
            cached_count += 1
        else:
            # Fetch data from API if not cached
            api_response = fetch_hijri_month_data(month, year)
            
            if api_response:
                # Rate limiting - be respectful to the API (only for new requests)
                time.sleep(0.1)  # 100ms delay between requests
            
        if api_response:
            # Process the month data
            processed_month_data = process_month_data(api_response, month, year)
            
            if processed_month_data:
                processed_months += 1
                processed_days += len(processed_month_data)
                print(f"✓ ({len(processed_month_data)} days)")
            else:
                error_count += 1
                print("✗ (processing failed)")
        else:
            error_count += 1
            print("✗ (API error)")

if __name__ == "__main__":
    main()