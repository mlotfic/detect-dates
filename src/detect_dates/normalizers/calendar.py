from typing import Dict, Any, List, Optional
import os

# Import path helper to ensure modules directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    # This is necessary for importing other modules in the package structure
    import sys
    from pathlib import Path
    def setup_src_path():
        current_file = Path(__file__).resolve()
        parts = current_file.parts
        for i, part in enumerate(parts):
            if part == 'src' and i + 2 < len(parts):
                src_second_path = str(Path(*parts[:i + 1]))
                if src_second_path not in sys.path:
                    sys.path.insert(0, src_second_path)
                    print(f"Added to sys.path: {src_second_path}")
                break
    print("INFO: Run Main File : adding file parent src to path ...")
    setup_src_path()

import os
import pandas as pd

from detect_dates.keywords.constants import (
    SUPPORTED_CALENDARS_COLUMNS,
    WEEKDAY_COLUMN,
    CALENDAR_ALIASES,
)

def normalize_calendar_name(calendar: Optional[str]) -> Optional[str]:
        """
        Normalize calendar name using aliases.

        Args:
            calendar: Calendar name to normalize

        Returns:
            str: Normalized calendar name

        Raises:
            ValueError: If calendar name is not recognized
        """
        if calendar is None:
            return None
        
        calendar = calendar.lower().strip()

        # Check aliases first
        if calendar in CALENDAR_ALIASES:
            return CALENDAR_ALIASES[calendar]

        # Check direct matches
        if calendar in SUPPORTED_CALENDARS_COLUMNS:
            return calendar

        # Generate helpful error message
        all_names = list(SUPPORTED_CALENDARS_COLUMNS.keys()) + list(CALENDAR_ALIASES.keys())
        raise ValueError(
            f"Unsupported calendar system: '{calendar}'. "
            f"Supported systems: {sorted(all_names)}"
        )
        
def get_calendar_info(self) -> Dict[str, Any]:
        """
        Get comprehensive information about the loaded calendar data.
        
        This method provides detailed statistics and metadata about the calendar
        mapping data, including data ranges, record counts, and sample entries.
        It's useful for debugging, data analysis, and system monitoring.
        
        Returns:
            Dict[str, Any]: Dictionary containing comprehensive data information::
            
                {
                    'data_loaded': bool,
                    'total_records': int,
                    'supported_calendars': List[str],
                    'calendar_aliases': Dict[str, str],
                    'date_ranges': Dict[str, Dict[str, int]],
                    'weekdays': List[str],
                    'csv_columns': List[str],
                    'sample_record': Dict[str, Any],
                    'file_path': str,
                    'data_quality': Dict[str, Any]
                }
                
        Example:
            Get system information::
            
                mapper = DateMapping()
                info = mapper.get_calendar_info()
                
                print(f"Data loaded: {info['data_loaded']}")
                print(f"Total records: {info['total_records']:,}")
                print(f"Gregorian range: {info['date_ranges']['gregorian']['min_year']}-{info['date_ranges']['gregorian']['max_year']}")
                
                # Show sample record
                sample = info['sample_record']
                print(f"Sample: {sample['gregorian']} = {sample['hijri']} (Hijri)")
        
        Note:
            This method always returns a dictionary, even if data loading failed.
            Check the 'data_loaded' key to determine if the data is available.
        """
        base_info = {
            'data_loaded': self.is_data_loaded(),
            'supported_calendars': self.get_supported_calendars(),
            'calendar_aliases': CALENDAR_ALIASES.copy(),
            'file_path': os.path.abspath(os.path.join(os.path.dirname(__file__), self.csv_path))
        }
        
        if not self.is_data_loaded():
            base_info.update({
                'error': 'Calendar data not loaded',
                'total_records': 0,
                'date_ranges': {},
                'weekdays': [],
                'csv_columns': [],
                'sample_record': {},
                'data_quality': {'status': 'data_not_loaded'}
            })
            return base_info
        
        # Get data statistics
        info = {
            **base_info,
            'total_records': len(self.df),
            'date_ranges': self.get_data_range(),
            'weekdays': sorted(self.df[WEEKDAY_COLUMN].unique().tolist()),
            'csv_columns': list(self.df.columns),
            'sample_record': {}
        }
        
        # Add a sample record for reference
        if not self.df.empty:
            sample_row = self.df.iloc[len(self.df)//2]  # Middle record for variety
            info['sample_record'] = {
                'gregorian': f"{sample_row['Gregorian Day']}/{sample_row['Gregorian Month']}/{sample_row['Gregorian Year']}",
                'hijri': f"{sample_row['Hijri Day']}/{sample_row['Hijri Month']}/{sample_row['Hijri Year']}",
                'julian': f"{sample_row['Solar Hijri Day']}/{sample_row['Solar Hijri Month']}/{sample_row['Solar Hijri Year']}",
                'weekday': sample_row[WEEKDAY_COLUMN]
            }
        
        # Add data quality information
        info['data_quality'] = self._get_data_quality_metrics()
        
        return info