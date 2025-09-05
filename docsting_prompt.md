You are a Python documentation and refactoring assistant.  
Your task is to improve the attached Python file with the following rules:

1. Keep the original logic intact (do not change how functions/classes work).  
2. Add or fix **docstrings** in **NumPy style**, compatible with Sphinx autodoc.  
   - Include a short summary, parameters, returns, raises, and examples if useful.  
3. Add **inline comments** where the code is not self-explanatory.  
4. Make the style **human-readable, clear, and simple** (no over-engineering).  
5. Do not add boilerplate or unused imports.  
6. Preserve my project vibe: practical, production-oriented, with minimal noise.  

Return the full improved file.

------------------------

You are a Python documentation and refactoring assistant. Your task is to improve the attached Python file with the following rules:

1. Keep the original logic intact (do not change how functions/classes work).  
2. Add or fix **docstrings** in **NumPy style**, compatible with Sphinx autodoc.  
   - Include a short summary, parameters, returns, raises, and examples if useful.  
3. Add **inline comments** where the code is not self-explanatory.  
4. Make the style **human-readable, clear, and simple** (no over-engineering).  
5. Do not add boilerplate or unused imports.  
6. Preserve my project vibe: practical, production-oriented, with minimal noise.  
7. **Add a `Usage` section at the very top of the file** (a quickstart guide with copy-pastable code).  
8. Keep examples inside docstrings of classes and methods where appropriate.  

Return the full improved file.




You are a Python code expert, your role is understand description given and generate human like code and simple and clear, knowing my vibe and style so far from our conversation 
- you have Calendar Date Mapping Module A comprehensive module for converting dates between different calendar systems including Gregorian, Hijri (Islamic), and Solar Hijri (Persian) calendars.

Performance:
    * First load reads and validates the entire CSV file
    * Subsequent operations use in-memory pandas DataFrame
    * Date lookups are optimized using boolean indexing
    * Data validation ensures integrity of conversions

This module provides functionality to:
* Convert dates between calendar systems with high accuracy
* Get weekday information for specific dates across different calendars
* Retrieve all dates within a specific month and year
* Access alternative calendar representations for any given date
* Validate dates across different calendar systems
example usage 
```py
"""
    Main function demonstrating usage of the DateMapping class.
    
    This function provides comprehensive examples of how to use the DateMapping 
    class for various calendar conversion operations, serving as both documentation
    and a test suite for the module's functionality.
    """
    print("Calendar Date Mapping Module")
    print("=" * 50)
    print("Comprehensive calendar conversion and date mapping functionality")
    print()
    
    try:
        # Initialize the DateMapping instance
        print("1. Initializing DateMapping...")
        mapper = DateMapping()
        
        if not mapper.is_data_loaded():
            print("❌ Failed to load calendar data. Please check the CSV file path.")

        else:
            print("✓ DateMapping initialized successfully")
            print()
            
            # Display calendar information
            print("2. Calendar Data Information:")
            info = mapper.get_calendar_info()
            print(f"   📊 Total records: {info['total_records']:,}")
            print(f"   📅 Supported calendars: {', '.join(info['SUPPORTED_CALENDARS_COLUMNS'])}")
            print(f"   🌍 Available weekdays: {', '.join(info['weekdays'])}")
            
            if info['sample_record']:
                sample = info['sample_record']
                print(f"   📝 Sample record:")
                print(f"      Gregorian: {sample['gregorian']}")
                print(f"      Hijri: {sample['hijri']}")
                print(f"      Solar Hijri: {sample['julian']}")
                print(f"      Weekday: {sample['weekday']}")
            print()
            
            # Display data ranges
            print("3. Available Date Ranges:")
            ranges = mapper.get_data_range()
            for calendar, range_info in ranges.items():
                print(f"   {calendar.title()}: {range_info['min_year']} - {range_info['max_year']} "
                      f"({range_info['total_years']:,} years)")
            print()
            
            # Example 1: Get weekday for specific dates
            print("4. Weekday Lookup Examples:")
            test_dates = [
                ('gregorian', 1, 1, 2024, 'New Year 2024'),
                ('hijri', 1, 1, 1445, 'Islamic New Year 1445'),
                ('julian', 1, 1, 1403, 'Persian New Year 1403')
            ]
            
            for calendar, day, month, year, description in test_dates:
                weekday = mapper.get_weekday_by_date(calendar, day, month, year)
                if weekday:
                    print(f"   📅 {description} ({calendar} {day}/{month}/{year}): {weekday}")
                else:
                    print(f"   ❓ {description}: Date not found in mapping data")
            print()
            
            # Example 2: Calendar system conversions
            print("5. Calendar System Conversion Examples:")
            conversion_examples = [
                ('gregorian', 1, 1, 2024, 'January 1, 2024 (Gregorian)'),
                ('hijri', 1, 1, 1445, 'Muharram 1, 1445 (Hijri)'),
                ('julian', 1, 1, 1403, 'Farvardin 1, 1403 (Solar Hijri)')
            ]
            
            for calendar, day, month, year, description in conversion_examples:
                alternatives = mapper.get_date_alternative_calendar(calendar, day, month, year)
                if alternatives:
                    print(f"   🔄 {description} converts to:")
                    for cal_name, cal_date in alternatives.items():
                        if cal_name != 'weekday' and cal_name != calendar:
                            print(f"      {cal_name.title()}: {cal_date['day']}/{cal_date['month']}/{cal_date['year']}")
                    print(f"      Weekday: {alternatives['weekday']}")
                    print()
            
            # Example 3: Month analysis
            print("6. Month Analysis Example:")
            month_info = mapper.get_month_info('gregorian', 2, 2024)  # February 2024
            if 'error' not in month_info:
                print(f"   📅 February 2024 Analysis:")
                print(f"      Days in month: {month_info['day_count']}")
                print(f"      First day: {month_info['first_day']} ({month_info['first_weekday']})")
                print(f"      Last day: {month_info['last_day']} ({month_info['last_weekday']})")
                print(f"      Weekday distribution: {month_info['weekday_distribution']}")
            print()
            
            # Example 4: Find specific weekdays
            print("7. Weekday Search Example:")
            # Find first Monday of March 2024
            first_monday = mapper.find_date_by_weekday('gregorian', 'Monday', 3, 2024, 1)
            if first_monday:
                greg_date = first_monday['gregorian']
                print(f"   🔍 First Monday of March 2024: {greg_date['day']}/{greg_date['month']}/{greg_date['year']}")
            
            # Find last Friday of December 2023
            last_friday = mapper.find_date_by_weekday('gregorian', 'Friday', 12, 2023, -1)
            if last_friday:
                greg_date = last_friday['gregorian']
                print(f"   🔍 Last Friday of December 2023: {greg_date['day']}/{greg_date['month']}/{greg_date['year']}")
            print()
            
            # Example 5: Date validation
            print("8. Date Validation Examples:")
            validation_tests = [
                ('gregorian', 29, 2, 2024, 'Feb 29, 2024 (leap year)'),
                ('gregorian', 29, 2, 2023, 'Feb 29, 2023 (non-leap year)'),
                ('hijri', 30, 12, 1445, 'Dhu al-Hijjah 30, 1445'),
                ('julian', 31, 12, 1403, 'Esfand 31, 1403 (invalid - max 29/30)')
            ]
            
            for calendar, day, month, year, description in validation_tests:
                is_valid = mapper.validate_date(calendar, day, month, year)
                status = "✅ Valid" if is_valid else "❌ Invalid"
                print(f"   {status}: {description}")
            print()
            
            # Example 6: Performance demonstration
            print("9. Performance Test:")
            import time
            
            start_time = time.time()
            for i in range(100):
                mapper.get_weekday_by_date('gregorian', 15, 3, 2024)
            end_time = time.time()
            
            print(f"   ⚡ 100 weekday lookups completed in {(end_time - start_time)*1000:.2f}ms")
            print(f"   📈 Average lookup time: {(end_time - start_time)*10:.2f}ms per lookup")
            
    except Exception as e:
        print(f"❌ Error during demonstration: {str(e)}")
        logger.exception("Error in main demonstration")
    
    print()
    print("=" * 50)
    print("Demonstration completed. Import this module to use DateMapping in your code.")
```

- you have a custom date dataclass 
```py
@dataclass
class DateComponents:
    """
    Basic date components container for structured date representation.

    A lightweight container class that holds the fundamental components of a date,
    including day, month, year, century, era, and calendar system. Useful for
    passing date information between functions without normalization overhead.

    Parameters
    ----------
    weekday : str, optional
        Day of the week (e.g., 'Monday', 'Tuesday')
    day : int or str, optional
        Day of the month (1-31), accepts both numeric and string formats
    month : int or str, optional
        Month of the year (1-12 or month name like 'January')
    year : int or str, optional
        Year (positive for CE/AD, negative for BCE/BC)
    century : int or str, optional
        Century (e.g., 21 for 21st century)
    era : str, optional
        Era designation ('CE', 'BCE', 'AH')
    calendar : str, optional
        Calendar system ('gregorian', 'hijri', 'julian')

    Examples
    --------
    >>> components = DateComponents(day=15, month=3, year=2023, century=21, era="CE", calendar="gregorian")
    >>> simple_components = DateComponents(year=2023)
    >>> print(components.day)
    15
    """
    weekday: Optional[str] = None
    day: Optional[Union[int, str]] = None
    month: Optional[Union[int, str]] = None
    year: Optional[Union[int, str]] = None
    century: Optional[Union[int, str]] = None
    era: Optional[str] = None
    calendar: Optional[str] = None
```

- i want to continue the following 
```py
@dataclass
class DateEntity:
    raw_start: DateComponents  
    raw_start_alt: Optional[DateComponents] = None  
    raw_end: Optional[DateComponents] = None
    raw_end_alt: Optional[DateComponents] = None
    
    calendar_input_count: int = 1
    complicity : Optional[str] = None  # "component"1, "simple_unknown" 1, "simple" 1, "composite" 2, "seasonal"2,4, "complex"4.
    relation: Optional[str] = None  # "simple", "simple-range" 2, "simple-financial"2, "complex-range"4, "complex-financial"4
    text: Optional[str] = None
    
    
    def __post_init__(self):
        start_hijri: Optional[DateComponents] = None
        end_hijri: Optional[DateComponents] = None
        start_gregorian: Optional[DateComponents] = None
        end_gregorian: Optional[DateComponents] = None
```

generate a methods to prove the relationship and find it
if calendar_input_count = 2:
- get the relation between `raw_start` and `raw_start_alt`
   - case  hijri , hijri - relationship could be - `financial year`, `range` 
   - case  hijri , gregorian or gregorian, hijri - relationship could be - `alternative form`
   - else
   - check if date qualify to be compared 

if calendar_input_count = 4:
- get the relation between `raw_start` and `raw_start_alt` and `raw_end` and `raw_end_alt`
   - find relationship between each two classes then using the above
   could be - `financial year`, `range` , `alternative form`, else
   - case  hijri , gregorian or gregorian, hijri - relationship could be - `alternative form`
   - suggest relationships

generate method to format custom human readable format knowning i have function to format DataComponents class
```py
def strftime(self, format_string: str) -> str:
        """
        Format the parsed date using strftime-like format codes with extensions.
        
        Supports standard strftime codes plus custom extensions for partial dates
        and calendar-specific information. Missing components are displayed with
        question marks to indicate incomplete data.

        Parameters
        ----------
        format_string : str
            Format string with % codes for date components

        Returns
        -------
        str
            Formatted date string with missing components shown as ? marks

        Notes
        -----
        Standard strftime codes supported:
        - %d: Day with zero padding (01-31) or ?? if None
        - %e: Day without padding (1-31) or ? if None  
        - %m: Month as number with padding (01-12) or ?? if None
        - %n: Month as number without padding (1-12) or ? if None
        - %b: Abbreviated month name (Jan, Feb, ...) or ??? if None
        - %B: Full month name (January, February, ...) or ??? if None
        - %y: Year without century (00-99) or ?? if None
        - %Y: Year with century (e.g. 2023, 1066) or ???? if None
        - %C: Century number or ?? if None
        - %A: Full weekday name (Monday, ...) or ??? if None
        - %a: Abbreviated weekday name (Mon, ...) or ??? if None

        Custom extensions:
        - %E: Era (BCE, CE, AD, BC) or empty if None
        - %S: Calendar system or empty if None  
        - %P: Precision level or empty if None
        - %%: Literal % character

        Examples
        --------
        >>> date = ParsedDate(raw=DateComponents(day="15", month="3", year="2023", era="CE"),
        ...                   standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> date.strftime("%Y-%m-%d")
        '2023-03-15'
        >>> date.strftime("%B %e, %Y %E")
        'March 15, 2023 CE'
        >>> partial = ParsedDate(raw=DateComponents(month="March", year="2023"),
        ...                      standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> partial.strftime("%B %Y")
        'March 2023'
        >>> partial.strftime("%Y-%m-%d")
        '2023-03-??'
        """
        result = format_string
        
        # Day formatting
        if self.day is not None:
            result = result.replace('%d', f"{self.day:02d}")
            result = result.replace('%e', str(self.day))
        else:
            result = result.replace('%d', '??')
            result = result.replace('%e', '?')
        
        # Month formatting
        if self.month_num is not None:
            result = result.replace('%m', f"{self.month_num:02d}")
            result = result.replace('%n', str(self.month_num))
            
            # Use existing month name from standard components if available
            if self.month:
                # Full month name
                result = result.replace('%B', str(self.month))
                # Abbreviated month name (first 3 characters)
                abbr_month = str(self.month)[:3] if len(str(self.month)) >= 3 else str(self.month)
                result = result.replace('%b', abbr_month)
            else:
                result = result.replace('%B', '???')
                result = result.replace('%b', '???')
        else:
            result = result.replace('%m', '??')
            result = result.replace('%n', '?')
            result = result.replace('%B', '???')
            result = result.replace('%b', '???')
        
        # Year formatting
        if self.year is not None:
            result = result.replace('%Y', str(self.year))
            result = result.replace('%y', f"{abs(self.year) % 100:02d}")
            # Century calculation
            if self.century is not None:
                result = result.replace('%C', str(self.century))
            else:
                # Calculate century from year
                century_num = (abs(self.year) // 100) + 1
                result = result.replace('%C', str(century_num))
        else:
            result = result.replace('%Y', '????')
            result = result.replace('%y', '??')
            result = result.replace('%C', '??')
        
        # Weekday formatting
        if self.weekday is not None:
            weekday_str = str(self.weekday)
            result = result.replace('%A', weekday_str)
            # Abbreviated weekday (first 3 characters)
            abbr_weekday = weekday_str[:3] if len(weekday_str) >= 3 else weekday_str
            result = result.replace('%a', abbr_weekday)
        else:
            result = result.replace('%A', '???')
            result = result.replace('%a', '???')
        
        # Custom extension formatting
        result = result.replace('%E', self.era or '')
        result = result.replace('%S', self.calendar or '')
        result = result.replace('%P', self.precision or '')
        
        # Handle literal % character (must be done last)
        result = result.replace('%%', '%')
        
        return result

    def _to_datetime(self):
        """
        Convert to Python datetime object if possible.
        
        Attempts to create a Python datetime object from the parsed date components.
        Only works for complete Gregorian calendar dates with all required components
        (day, month, year). Other calendar systems and partial dates cannot be converted.

        Returns
        -------
        datetime or None
            Python datetime object if conversion is possible, None otherwise

        Notes
        -----
        Conversion requirements:
        - Must be a complete date (day, month, year all present)
        - Must use Gregorian calendar system
        - Date components must represent a valid calendar date
        - Negative years (BCE) are not supported by Python datetime

        Examples
        --------
        >>> from datetime import datetime
        >>> complete_date = ParsedDate(raw=DateComponents(day="15", month="3", year="2023", 
        ...                                              era="CE", calendar="gregorian"),
        ...                           standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> dt = complete_date._to_datetime()
        >>> isinstance(dt, datetime)
        True
        >>> dt.year
        2023

        >>> partial_date = ParsedDate(raw=DateComponents(month="March", year="2023"),
        ...                          standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> partial_date._to_datetime() is None
        True

        >>> hijri_date = ParsedDate(raw=DateComponents(day="15", month="3", year="1445", 
        ...                                           era="AH", calendar="hijri"),
        ...                        standard=DateComponents(), numeric=DateComponents(), meta=DateMeta())
        >>> hijri_date._to_datetime() is None
        True
        """
        # Import datetime here to avoid circular imports
        from datetime import datetime
        
        # Check if we have a complete Gregorian date
        if not self.is_complete_date:
            return None
            
        if self.calendar != 'gregorian':
            return None
            
        # Check for required components
        if self.day is None or self.month_num is None or self.year is None:
            return None
            
        # Python datetime doesn't support negative years (BCE dates)
        if self.year <= 0:
            return None
        
        try:
            # Attempt to create datetime object with validation
            return datetime(
                year=int(self.year),
                month=int(self.month_num), 
                day=int(self.day)
            )
        except (ValueError, TypeError, OverflowError):
            # Handle invalid dates (e.g., Feb 30, invalid ranges)
            return None
```

✅ **Pros of Using JavaScript and Promises in Shiny Apps**: 

1. **Improved Performance**: Offloads tasks to the client, reducing server load. 

2. **Enhanced User Experience**: Ensures non-blocking and responsive UI. 

3. **Access to Advanced Features**: Integrates modern web libraries like D3.js and Plotly.js. 

4. **Error Handling**: Promises provide structured ways to catch and handle errors. 

5. **Cross-Browser Compatibility**: JavaScript ensures your app works across major browsers. 

❌ **Cons to Consider**: 

1. **Steeper Learning Curve**: Requires familiarity with JavaScript and its integration with Shiny. 

2. **Debugging Complexity**: Errors across R and JavaScript may be harder to trace. 

3. **Increased Maintenance**: Mixing R and JavaScript can make your codebase harder to maintain. 

4. **Dependency on External APIs**: API availability or downtime can affect app functionality. 

5. **Browser Limitations**: Some users may experience issues due to older browsers or disabled JavaScript. * * 



* **🔗 Helpful Resources to Get Started:** 

* Promises in JavaScript (MDN) * Using JavaScript in Shiny (Shiny Official Documentation) 

* Shiny and Promises (RStudio Blog) Are you already using JavaScript with Shiny? 

🔗 #RStats #Shiny #JavaScript #WebDevelopment #Promises”