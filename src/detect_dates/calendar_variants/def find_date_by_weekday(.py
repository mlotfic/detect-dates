def find_date_by_weekday(
        self, calendar: Optional[str], weekday: str, month: int, year: int, 
        occurrence: int = 1) -> Optional[Dict[str, Any]]:
        """
        Find a specific occurrence of a weekday in a given month/year.
        
        Parameters
        ----------
        calendar : str
            Calendar system
        weekday : str
            Target weekday ('Monday', 'Tuesday', etc.)
        month : int
            Month number (1-12)
        year : int
            Year
        occurrence : int, default 1
            Which occurrence (1=first, 2=second, -1=last, etc.)
            
        Returns
        -------
        Optional[Dict[str, Any]]
            Date information if found, None otherwise
            
        Examples
        --------
        >>> mapper = DateMapping(DateDataLoader())
        >>> # Find first Monday of March 2024
        >>> first_monday = mapper.find_date_by_weekday('gregorian', 'Monday', 3, 2024, 1)
        >>> # Find last Friday of December 2023
        >>> last_friday = mapper.find_date_by_weekday('gregorian', 'Friday', 12, 2023, -1)
        """
        if not self._is_data_loaded() or self.df is None:
            return None
        
        calendar = normalize_calendar_from_era(calendar)
        if calendar not in SUPPORTED_CALENDARS_COLUMNS:
            return None
        
        # Get column names for this calendar
        day_col, month_col, year_col = SUPPORTED_CALENDARS_COLUMNS[calendar]
        
        # Filter data for the specific month and year, and the target weekday
        filter_mask = (
            (self.df[month_col] == month) & 
            (self.df[year_col] == year) & 
            (self.df[WEEKDAY_COLUMN] == weekday)
        )
        matching_dates = self.df[filter_mask].sort_values(day_col)
        
        if matching_dates.empty:
            return None
        
        # Handle occurrence selection
        try:
            if occurrence > 0:
                # Positive: count from beginning
                selected_row = matching_dates.iloc[occurrence - 1]
            else:
                # Negative: count from end
                selected_row = matching_dates.iloc[occurrence]
            
            # Return the calendar variants for the found date
            day = int(selected_row[day_col])
            return self.get_calendar_variants(calendar, day, month, year)
            
        except IndexError:
            return None
        
@dataclass
class DateMapping:
    """
    A class for mapping and converting dates between different calendar systems.

    This class provides comprehensive methods to convert dates between Gregorian,
    Hijri (Islamic), and Solar Hijri (Persian) calendar systems. It uses a
    pre-calculated CSV mapping file containing astronomical conversions to ensure
    accuracy across different historical periods.

    The class is designed with performance in mind, using pandas for efficient
    data operations and caching mechanisms to avoid repeated file I/O.

    Attributes
    ----------
    df : Optional[pd.DataFrame]
        DataFrame containing the calendar mapping data.
        This is loaded automatically during initialization.
    csv_path : str
        Path to the CSV file containing mapping data.
    _data_loaded : bool
        Internal flag indicating successful data loading.
    _date_ranges : Dict[str, Dict[str, int]]
        Cached date ranges for each calendar.

    Examples
    --------
    Initialize and perform basic operations:

    >>> # Standard initialization (uses default CSV path)
    >>> mapper = DateMapping()
    >>> # Custom CSV path
    >>> mapper = DateMapping(csv_path="custom/path/to/calendar_data.csv")
    >>> # Check if data loaded successfully
    >>> if mapper.is_data_loaded():
    ...     weekday = mapper.get_weekday_by_date('gregorian', 15, 3, 2024)

    Notes
    -----
    The CSV file should be located at the specified path relative to this
    module's location. If the file is not found, the class will raise a
    FileNotFoundError with helpful guidance.
    """
    
    _data_loaded: bool = False
    _date_ranges: Optional[Dict[str, Dict[str, int]]] = None

    def __post_init__(self, csv_path=None) -> None:
        """
        Initialize the DateMapping instance by loading the calendar data.

        This method is automatically called after object creation to:

        * Load and validate the mapping data from the CSV file
        * Perform data integrity checks
        * Cache frequently used information
        * Set up error handling for missing or corrupt data

        The initialization is fail-safe: if data loading fails, the object
        is still created but with limited functionality.

        Parameters
        ----------
        csv_path : str, optional
            Path to the CSV file containing calendar mappings.
            If None, uses default path from DateDataLoader.

        Raises
        ------
        FileNotFoundError
            If the calendar mapping CSV file cannot be found
        ValueError
            If the CSV file has incorrect structure or missing columns
        RuntimeError
            If there are issues with data processing
        """
        try:
            loader = DateDataLoader()
            print(f"   Supported calendars: {loader.get_supported_calendars()}")
            
            self.df = loader.load_data()
            print(f"   Loaded {len(self.df):,} records (first call)")
            print(f"   Retrieved {len(self.df):,} records (cached)")

            self._data_loaded = True
            logger.info(f"Successfully loaded {len(self.df):,} calendar mapping records")
        except Exception as e:
            logger.error(f"Failed to initialize DateMapping: {str(e)}")
            self._data_loaded = False
            # Don't re-raise to allow graceful degradation        

    def is_data_loaded(self) -> bool:
        """
        Check if the calendar mapping data was loaded successfully.

        Returns
        -------
        bool
            True if data is loaded and ready for use, False otherwise

        Examples
        --------
        >>> mapper = DateMapping()
        >>> if mapper.is_data_loaded():
        ...     # Safe to use mapping functions
        ...     result = mapper.get_weekday_by_date('gregorian', 1, 1, 2024)
        ... else:
        ...     print("Calendar data not available")
        """
        return self._data_loaded and self.df is not None and not self.df.empty

    def _validate_date_ranges(self) -> None:
        """
        Validate that date ranges in the DataFrame are reasonable.

        This method checks the loaded data to ensure that day, month, and year
        values fall within expected ranges for each calendar system.

        Raises
        ------
        ValueError
            If date ranges are invalid or suspicious
        """
        for calendar_name, columns in SUPPORTED_CALENDARS_COLUMNS.items():
            day_col, month_col, year_col = columns

            # Check day ranges (1-31)
            day_min, day_max = self.df[day_col].min(), self.df[day_col].max()
            if not (1 <= day_min and day_max <= 31):
                raise ValueError(f"Invalid day range for {calendar_name}: {day_min}-{day_max}")

            # Check month ranges (1-12)
            month_min, month_max = self.df[month_col].min(), self.df[month_col].max()
            if not (1 <= month_min and month_max <= 12):
                raise ValueError(f"Invalid month range for {calendar_name}: {month_min}-{month_max}")

            # Check year ranges (reasonable historical range)
            year_min, year_max = self.df[year_col].min(), self.df[year_col].max()
            if calendar_name == 'gregorian':
                if year_min < -5000 or year_max > 10000:
                    logger.warning(f"Unusual Gregorian year range: {year_min}-{year_max}")
                    
def info(self) -> Dict[str, Any]:
        """
        Get comprehensive information about the calendar mapping system.
        
        This method provides detailed information about the loaded data,
        supported calendar systems, and basic statistics.
        
        Returns
        -------
        Dict[str, Any]
            Dictionary containing calendar system information:
            
            {
                'total_records': int,
                'supported_calendars': List[str],
                'weekdays': List[str],
                'date_ranges': Dict[str, Dict[str, int]],
                'sample_record': Dict[str, Any]
            }
            
        Examples
        --------
        >>> mapper = DateMapping(DateDataLoader())
        >>> info = mapper.info()
        >>> print(f"Total records: {info['total_records']:,}")
        >>> print(f"Supported calendars: {', '.join(info['supported_calendars'])}")
        """
        if not self._is_data_loaded() or self.df is None:
            return {'error': 'Data not loaded'}
        
        # Get sample record for demonstration
        sample_row = self.df.iloc[0]
        sample_record = {
            'gregorian': {
                'day': int(sample_row['Gregorian Day']),
                'month': int(sample_row['Gregorian Month']),
                'year': int(sample_row['Gregorian Year'])
            },
            'hijri': {
                'day': int(sample_row['Hijri Day']),
                'month': int(sample_row['Hijri Month']),
                'year': int(sample_row['Hijri Year'])
            },
            'Jalali': {
                'day': int(sample_row['Solar Hijri Day']),
                'month': int(sample_row['Solar Hijri Month']),
                'year': int(sample_row['Solar Hijri Year'])
            },
            'weekday': sample_row[WEEKDAY_COLUMN]
        }
        
        return {
            'total_records': len(self.df),
            'supported_calendars': list(SUPPORTED_CALENDARS_COLUMNS.keys()),
            'calendar_aliases': CALENDAR_ALIASES,
            'weekdays': sorted(self.df[WEEKDAY_COLUMN].unique()),
            'date_ranges': self.get_data_range(),
            'sample_record': sample_record,
            'data_quality': self._get_data_quality_metrics()
        }
def _get_data_quality_metrics(self) -> Dict[str, Any]:
        """
        Calculate data quality metrics for the loaded dataset.
        
        Returns
        -------
        Dict[str, Any]
            Data quality metrics including record count, date coverage, etc.
        """
        if not self._is_data_loaded() or self.df is None:
            return {'status': 'no_data'}
        
        metrics = {
            'status': 'good',
            'total_records': len(self.df),
            'unique_weekdays': len(self.df[WEEKDAY_COLUMN].unique()),
            'date_coverage': {}
        }
        
        # Check date coverage for each calendar
        for calendar_name, columns in SUPPORTED_CALENDARS_COLUMNS.items():
            year_col = columns[2]  # Year column is always third
            year_range = self.df[year_col].max() - self.df[year_col].min() + 1
            unique_years = len(self.df[year_col].unique())
            
            metrics['date_coverage'][calendar_name] = {
                'year_span': year_range,
                'unique_years': unique_years,
                'coverage_ratio': unique_years / year_range if year_range > 0 else 0
            }
        
        return metrics