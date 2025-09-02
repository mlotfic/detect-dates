from typing import Dict, Any
import os

# Module-level constants for supported calendar systems
# Based on actual CSV structure: Week Day,Hijri Day,Hijri Month,Hijri Year,Gregorian Day,Gregorian Month,Gregorian Year,Solar Hijri Day,Solar Hijri Month,Solar Hijri Year
SUPPORTED_CALENDARS = {
    'gregorian': ['Gregorian Day', 'Gregorian Month', 'Gregorian Year'],
    'hijri': ['Hijri Day', 'Hijri Month', 'Hijri Year'],
    'julian': ['Solar Hijri Day', 'Solar Hijri Month', 'Solar Hijri Year']  # Note: 'julian' maps to Solar Hijri
}

# Column name for weekday information in the CSV file
WEEKDAY_COLUMN = 'Week Day'

# Calendar system aliases for user convenience
CALENDAR_ALIASES = {
    'solar_hijri': 'julian',
    'persian': 'julian',
    'islamic': 'hijri',
    'greg': 'gregorian'
}

def normalize_calendar_name(self, calendar: str) -> str:
        """
        Normalize calendar name using aliases.

        Args:
            calendar: Calendar name to normalize

        Returns:
            str: Normalized calendar name

        Raises:
            ValueError: If calendar name is not recognized
        """
        calendar = calendar.lower().strip()

        # Check aliases first
        if calendar in CALENDAR_ALIASES:
            return CALENDAR_ALIASES[calendar]

        # Check direct matches
        if calendar in SUPPORTED_CALENDARS:
            return calendar

        # Generate helpful error message
        all_names = list(SUPPORTED_CALENDARS.keys()) + list(CALENDAR_ALIASES.keys())
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