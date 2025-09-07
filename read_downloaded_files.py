# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 14:02:06 2025

@author: m
"""

import requests
import csv
import time
from datetime import datetime, timedelta
import json
import os

# Module-level constants
SUPPORTED_CALENDARS_COLUMNS = {
    'gregorian': ['Gregorian Day', 'Gregorian Month', 'Gregorian Year'],
    'hijri': ['Hijri Day', 'Hijri Month', 'Hijri Year'],
    'Jalali': ['Solar Hijri Day', 'Solar Hijri Month', 'Solar Hijri Year']
}

WEEKDAY_COLUMN = 'Week Day'


columns = [
    # Hijri
    "hijri.date",
    "hijri.format",
    "hijri.day",
    "hijri.month.number",
    "hijri.year",

    "hijri.weekday.ar",
    "hijri.weekday.en",
    "hijri.month.ar",
    "hijri.month.en",    
    "hijri.month.days",

    "hijri.designation.abbreviated",
    "hijri.designation.expanded",

    "hijri.holidays",
    "hijri.adjustedHolidays",
    "hijri.method",

    # Gregorian
    "gregorian.date",
    "gregorian.format",
    "gregorian.day",
    "gregorian.month.number",
    "gregorian.year",
    "gregorian.weekday.en",
    "gregorian.month.en",
    "gregorian.designation.abbreviated",
    "gregorian.designation.expanded",
    "gregorian.lunarSighting"
]

csv_columns = [
            "hijri.date", "hijri.format", "hijri.day", "hijri.month.number", "hijri.year",
            "hijri.weekday.ar", "hijri.weekday.en", "hijri.month.ar", "hijri.month.en",
            "hijri.month.days", "hijri.designation.abbreviated", "hijri.designation.expanded",
            "hijri.holidays", "hijri.adjustedHolidays", "hijri.method",
            "gregorian.date", "gregorian.format", "gregorian.day", "gregorian.month.number",
            "gregorian.year", "gregorian.weekday.en", "gregorian.month.en",
            "gregorian.designation.abbreviated", "gregorian.designation.expanded",
            "gregorian.lunarSighting"
        ]

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


def read_json_files_response():
    """Check if response file exists for a given month/year and load it"""
    json_dir = "debug_responses_month"
    # Loop through files in the directory
    for filename in os.listdir(json_dir):
        if filename.endswith(".json"):  # only process JSON
            file_path = os.path.join(json_dir, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    print(f"✅ Loaded {filename}:")
                    print(data)  # do your processing here
                except json.JSONDecodeError as e:
                    print(f"❌ Failed to parse {filename}: {e}")
    return None

