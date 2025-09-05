from dataclasses import dataclass
from typing import Optional, Union, Dict, List, Tuple
from enum import Enum

from parsed import ParsedDate  # Assuming ParsedDate is defined in parsed module
from detect_dates.calendar_variants.date_mapping import DateMapping  # Assuming DateMapping is defined here

from detect_dates.keywords.constants import (
    Language,
    Calendar,
    OutputFormat,
    PRECISION_LEVELS,
    CALENDAR_ALIASES,
    SUPPORTED_LANGUAGES,
    SUPPORTED_CALENDARS,
    SUPPORTED_CALENDARS_COLUMNS,
    WEEKDAY_COLUMN,
    DEFAULT_LANGUAGE,
    DEFAULT_CALENDAR,
    RelationType,
    ComplexityLevel,
)


@dataclass
class DateEntity:
    raw_start: ParsedDate  
    raw_start_alt: Optional[ParsedDate] = None  
    raw_end: Optional[ParsedDate] = None
    raw_end_alt: Optional[ParsedDate] = None
    
    calendar_input_count: int = 1
    complicity: Optional[str] = None  # "component", "simple_unknown", "simple", "composite", "seasonal", "complex"
    relation: Optional[str] = None  # "simple", "simple-range", "simple-financial", "complex-range", "complex-financial"
    text: Optional[str] = None
    
    def __post_init__(self):
        """Initialize derived date components after main initialization."""
        self.start_hijri: Optional[ParsedDate] = None
        self.end_hijri: Optional[ParsedDate] = None
        self.start_gregorian: Optional[ParsedDate] = None
        self.end_gregorian: Optional[ParsedDate] = None
        
        # Automatically determine relationships and complexity
        self._analyze_entity()
    
    def _analyze_entity(self):
        """Analyze the entity to determine complexity and relationships."""
        # Determine complexity based on calendar_input_count
        if self.calendar_input_count == 1:
            if self._is_complete_date(self.raw_start):
                self.complicity = ComplexityLevel.SIMPLE.value
                self.relation = "simple"
            else:
                self.complicity = ComplexityLevel.COMPONENT.value
                self.relation = "simple"
        
        elif self.calendar_input_count == 2:
            self.complicity = ComplexityLevel.COMPOSITE.value
            self.relation = self._determine_dual_relationship()
        
        elif self.calendar_input_count == 4:
            self.complicity = ComplexityLevel.COMPLEX.value
            self.relation = self._determine_complex_relationship()
    
    def _is_complete_date(self, date_comp: ParsedDate) -> bool:
        """Check if a DateComponent represents a complete date."""
        return (date_comp.day is not None and 
                date_comp.month is not None and 
                date_comp.year is not None)
    
    def _determine_dual_relationship(self) -> str:
        """Determine relationship between raw_start and raw_start_alt."""
        if not self.raw_start_alt:
            return "simple"
        
        start_cal = self.raw_start.calendar
        alt_cal = self.raw_start_alt.calendar
        
        # Case 1: Same calendar system
        if start_cal == alt_cal:
            if start_cal == 'hijri':
                # Check for financial year pattern
                if self._is_financial_year_pattern(self.raw_start, self.raw_start_alt):
                    return "simple-financial"
                # Check for range pattern
                elif self._is_range_pattern(self.raw_start, self.raw_start_alt):
                    return "simple-range"
            return "simple-range"  # Default for same calendar
        
        # Case 2: Different calendar systems (hijri-gregorian conversion)
        elif ((start_cal == 'hijri' and alt_cal == 'gregorian') or 
              (start_cal == 'gregorian' and alt_cal == 'hijri')):
            return "alternative_form"
        
        # Case 3: Other combinations
        else:
            if self._dates_qualify_for_comparison(self.raw_start, self.raw_start_alt):
                return "simple-range"
            return "incomparable"
    
    def _determine_complex_relationship(self) -> str:
        """Determine relationship for 4-date entities."""
        if not all([self.raw_start_alt, self.raw_end, self.raw_end_alt]):
            return "complex-range"
        
        # Analyze start pair
        start_relation = self._get_pair_relationship(self.raw_start, self.raw_start_alt)
        
        # Analyze end pair  
        end_relation = self._get_pair_relationship(self.raw_end, self.raw_end_alt)
        
        # Combine relationships
        if start_relation == "alternative_form" and end_relation == "alternative_form":
            return "complex-alternative"
        elif "financial" in start_relation or "financial" in end_relation:
            return "complex-financial"
        else:
            return "complex-range"
    
    def _get_pair_relationship(self, date1: ParsedDate, date2: ParsedDate) -> str:
        """Get relationship between a pair of dates."""
        if not date1 or not date2:
            return "unknown"
        
        cal1, cal2 = date1.calendar, date2.calendar
        
        if cal1 == cal2:
            if cal1 == 'hijri' and self._is_financial_year_pattern(date1, date2):
                return "financial"
            return "range"
        elif ((cal1 == 'hijri' and cal2 == 'gregorian') or 
              (cal1 == 'gregorian' and cal2 == 'hijri')):
            return "alternative_form"
        else:
            return "unknown"
    
    def _is_financial_year_pattern(self, date1: ParsedDate, date2: ParsedDate) -> bool:
        """Check if two dates represent a financial year pattern."""
        if not (date1.year and date2.year and date1.month and date2.month):
            return False
        
        try:
            year1, year2 = int(date1.year), int(date2.year)
            month1, month2 = int(date1.month), int(date2.month)
            
            # Financial year typically spans across calendar years
            # Common patterns: different years with specific month transitions
            if abs(year2 - year1) == 1:
                # Check for common financial year transitions
                if (month1 in [1, 4, 7, 10] and month2 in [3, 6, 9, 12]) or \
                   (month1 in [3, 6, 9, 12] and month2 in [1, 4, 7, 10]):
                    return True
            
            return False
        except (ValueError, TypeError):
            return False
    
    def _is_range_pattern(self, date1: ParsedDate, date2: ParsedDate) -> bool:
        """Check if two dates represent a date range."""
        if not self._dates_qualify_for_comparison(date1, date2):
            return False
        
        # If they have different months or years, likely a range
        return (date1.month != date2.month or date1.year != date2.year)
    
    def _dates_qualify_for_comparison(self, date1: ParsedDate, date2: ParsedDate) -> bool:
        """Check if two dates can be meaningfully compared."""
        if not date1 or not date2:
            return False
        
        # Both need at least year information
        if not (date1.year and date2.year):
            return False
        
        # Same calendar system preferred for comparison
        if date1.calendar and date2.calendar and date1.calendar != date2.calendar:
            # Only allow hijri-gregorian comparisons
            valid_pairs = {('hijri', 'gregorian'), ('gregorian', 'hijri')}
            return (date1.calendar, date2.calendar) in valid_pairs
        
        return True
    
    def get_relationship_analysis(self) -> Dict[str, any]:
        """Get comprehensive analysis of the date entity relationships."""
        analysis = {
            'complexity': self.complicity,
            'relation': self.relation,
            'calendar_count': self.calendar_input_count,
            'relationships': {}
        }
        
        if self.calendar_input_count >= 2 and self.raw_start_alt:
            analysis['relationships']['start_pair'] = {
                'calendars': (self.raw_start.calendar, self.raw_start_alt.calendar),
                'type': self._get_pair_relationship(self.raw_start, self.raw_start_alt),
                'comparable': self._dates_qualify_for_comparison(self.raw_start, self.raw_start_alt)
            }
        
        if self.calendar_input_count == 4 and self.raw_end and self.raw_end_alt:
            analysis['relationships']['end_pair'] = {
                'calendars': (self.raw_end.calendar, self.raw_end_alt.calendar),
                'type': self._get_pair_relationship(self.raw_end, self.raw_end_alt),
                'comparable': self._dates_qualify_for_comparison(self.raw_end, self.raw_end_alt)
            }
        
        return analysis
    
    def format_human_readable(self, format_template: Optional[str] = None, 
                            include_alternatives: bool = True,
                            separator: str = " - ") -> str:
        """
        Format the DateEntity in a human-readable format.
        
        Parameters
        ----------
        format_template : str, optional
            Custom format template. If None, uses intelligent defaults based on complexity
        include_alternatives : bool, default True
            Whether to include alternative calendar representations
        separator : str, default " - "
            Separator for date ranges and alternatives
        
        Returns
        -------
        str
            Human-readable formatted string
        """
        if not format_template:
            format_template = self._get_default_format_template()
        
        parts = []
        
        # Format main start date
        if self.raw_start:
            start_formatted = self._format_date_component(self.raw_start, format_template)
            parts.append(start_formatted)
        
        # Add alternative start if requested and available
        if include_alternatives and self.raw_start_alt:
            alt_formatted = self._format_date_component(self.raw_start_alt, format_template)
            if self.relation == "alternative_form":
                parts[-1] += f" ({alt_formatted})"
            else:
                parts.append(alt_formatted)
        
        # Add end dates for ranges
        if self.raw_end:
            end_formatted = self._format_date_component(self.raw_end, format_template)
            if self.calendar_input_count >= 2:
                # This is a range
                range_str = separator.join(parts) + separator + end_formatted
                parts = [range_str]
            else:
                parts.append(end_formatted)
        
        # Add alternative end if available
        if include_alternatives and self.raw_end_alt:
            end_alt_formatted = self._format_date_component(self.raw_end_alt, format_template)
            if self.relation == "complex-alternative":
                parts[-1] += f" ({end_alt_formatted})"
            else:
                parts.append(end_alt_formatted)
        
        return separator.join(parts)
    
    def _get_default_format_template(self) -> str:
        """Get appropriate default format based on complexity and available information."""
        if self.complicity == ComplexityLevel.COMPONENT.value:
            # For incomplete dates, show what we have
            if self.raw_start.year and not (self.raw_start.month or self.raw_start.day):
                return "%Y"
            elif self.raw_start.month and self.raw_start.year and not self.raw_start.day:
                return "%B %Y"
            else:
                return "%B %e, %Y"
        
        elif self.relation == "alternative_form":
            # Show calendar system for alternatives
            return "%B %e, %Y %S"
        
        elif "financial" in str(self.relation):
            # Financial years often need fiscal year context
            return "%B %Y"
        
        else:
            # Standard format for most cases
            return "%B %e, %Y"
    
    def _format_date_component(self, date_comp: ParsedDate, format_template: str) -> str:
        """Format a single DateComponent using the template."""
        # This assumes ParsedDate has a strftime method similar to your example
        # If not, you'll need to implement the formatting logic here
        if hasattr(date_comp, 'strftime'):
            return date_comp.strftime(format_template)
        else:
            # Fallback manual formatting
            return self._manual_format(date_comp, format_template)
    
    def _manual_format(self, date_comp: ParsedDate, format_template: str) -> str:
        """Manual formatting when strftime is not available on ParsedDate."""
        result = format_template
        
        # Basic replacements - you can expand this based on your needs
        if date_comp.day:
            result = result.replace('%e', str(date_comp.day))
            result = result.replace('%d', f"{int(date_comp.day):02d}")
        else:
            result = result.replace('%e', '?')
            result = result.replace('%d', '??')
        
        if date_comp.month:
            if isinstance(date_comp.month, str) and not date_comp.month.isdigit():
                result = result.replace('%B', str(date_comp.month))
                result = result.replace('%b', str(date_comp.month)[:3])
            else:
                month_names = ['', 'January', 'February', 'March', 'April', 'May', 'June',
                             'July', 'August', 'September', 'October', 'November', 'December']
                try:
                    month_num = int(date_comp.month)
                    if 1 <= month_num <= 12:
                        result = result.replace('%B', month_names[month_num])
                        result = result.replace('%b', month_names[month_num][:3])
                        result = result.replace('%m', f"{month_num:02d}")
                    else:
                        result = result.replace('%B', '???')
                        result = result.replace('%b', '???')
                        result = result.replace('%m', '??')
                except (ValueError, TypeError):
                    result = result.replace('%B', '???')
                    result = result.replace('%b', '???')
                    result = result.replace('%m', '??')
        else:
            result = result.replace('%B', '???')
            result = result.replace('%b', '???')
            result = result.replace('%m', '??')
        
        if date_comp.year:
            result = result.replace('%Y', str(date_comp.year))
        else:
            result = result.replace('%Y', '????')
        
        if date_comp.calendar:
            result = result.replace('%S', f"({date_comp.calendar})")
        else:
            result = result.replace('%S', '')
        
        return result
    
    def get_suggested_relationships(self) -> List[str]:
        """Get list of possible relationships based on current data."""
        suggestions = []
        
        if self.calendar_input_count == 2:
            if self.raw_start.calendar == self.raw_start_alt.calendar == 'hijri':
                suggestions.extend(['financial_year', 'range', 'seasonal'])
            elif {self.raw_start.calendar, self.raw_start_alt.calendar} == {'hijri', 'gregorian'}:
                suggestions.append('alternative_form')
            else:
                suggestions.extend(['range', 'seasonal'])
        
        elif self.calendar_input_count == 4:
            suggestions.extend(['complex_range', 'complex_financial', 'complex_alternative'])
        
        return suggestions
    
    def __str__(self) -> str:
        """String representation of the DateEntity."""
        return self.format_human_readable()
    
    def __repr__(self) -> str:
        """Detailed representation for debugging."""
        return (f"DateEntity(calendar_count={self.calendar_input_count}, "
                f"complexity='{self.complicity}', relation='{self.relation}', "
                f"text='{self.text}')")
        
# Initialize with mapper
mapper = DateMapping()
entity = DateEntity.create_with_mapper(
    raw_start=ParsedDate(day=15, month=3, year=2024, calendar='gregorian'),
    raw_start_alt=ParsedDate(day=8, month=9, year=1445, calendar='hijri'),  # This will be validated/corrected
    mapper=mapper
)

# Get validation status
status = entity.get_validation_status()
print(status)
# {'start_valid': True, 'start_alt_valid': False, 'corrections_made': ['corrected_start_alt']}

# Manual correction trigger
corrections = entity.correct_relationships(force_correction=True)
print(corrections['corrections_made'])  # ['corrected_start_alt']

# Automatically adds weekdays, alternative calendars, and validation
entity.enrich_with_mapper_data()

# Find patterns in months
ramadan_fridays = entity.find_date_patterns_in_month('hijri', 9, 1445, 'Friday')

# Basic usage with validation
mapper = DateMapping()

# Case 1: Alternative calendar validation
entity1 = DateEntity.create_with_mapper(
    raw_start=ParsedDate(day=1, month=1, year=2024, calendar='gregorian'),
    raw_start_alt=ParsedDate(day=19, month=6, year=1445, calendar='hijri'),  # Will verify this matches
    mapper=mapper
)

# Case 2: Financial year detection  
entity2 = DateEntity.create_with_mapper(
    raw_start=ParsedDate(month=1, year=1445, calendar='hijri'),
    raw_start_alt=ParsedDate(month=12, year=1445, calendar='hijri'),
    mapper=mapper
)

# Case 3: Complex range validation
entity3 = DateEntity.create_with_mapper(
    raw_start=ParsedDate(day=1, month=3, year=2024, calendar='gregorian'),
    raw_start_alt=ParsedDate(day=20, month=8, year=1445, calendar='hijri'),
    raw_end=ParsedDate(day=31, month=3, year=2024, calendar='gregorian'), 
    raw_end_alt=ParsedDate(day=19, month=9, year=1445, calendar='hijri'),
    mapper=mapper
)

# Check results
print(f"Relationship: {entity1.relation}")  # "alternative_form" (validated)
print(f"Validation: {entity1.get_validation_status()}")
print(f"Formatted: {entity1.format_human_readable()}")





def get_suggested_relationships(self) -> List[str]:
        """Get list of possible relationships based on current data and mapper validation."""
        suggestions = []
        
        if self.calendar_input_count == 2:
            if self.raw_start.calendar == self.raw_start_alt.calendar == 'hijri':
                suggestions.extend(['financial_year', 'range', 'seasonal'])
            elif {self.raw_start.calendar, self.raw_start_alt.calendar} == {'hijri', 'gregorian'}:
                suggestions.append('alternative_form')
            else:
                suggestions.extend(['range', 'seasonal'])
        
        elif self.calendar_input_count == 4:
            suggestions.extend(['complex_range', 'complex_financial', 'complex_alternative'])
        
        # Add mapper-based suggestions
        if self.mapper and hasattr(self, '_validation_results'):
            validation = self._validation_results
            if validation.get('relationship_verified'):
                current_relation = self.relation
                if current_relation not in suggestions:
                    suggestions.insert(0, current_relation)  # Put verified relation first
        
        return suggestions
    
    @classmethod
    def create_with_mapper(cls, raw_start: ParsedDate, 
                          mapper: 'DateMapping',
                          raw_start_alt: Optional[ParsedDate] = None,
                          raw_end: Optional[ParsedDate] = None,
                          raw_end_alt: Optional[ParsedDate] = None,
                          text: Optional[str] = None) -> 'DateEntity':
        """
        Create a DateEntity with mapper integration and automatic validation.
        
        Parameters
        ----------
        raw_start : ParsedDate
            Primary start date
        mapper : DateMapping
            DateMapping instance for validation and corrections
        raw_start_alt : ParsedDate, optional
            Alternative representation of start date
        raw_end : ParsedDate, optional  
            End date for ranges
        raw_end_alt : ParsedDate, optional
            Alternative representation of end date
        text : str, optional
            Original text representation
            
        Returns
        -------
        DateEntity
            Fully validated and corrected DateEntity instance
        """
        # Count non-None date components
        calendar_count = sum(1 for comp in [raw_start, raw_start_alt, raw_end, raw_end_alt] 
                           if comp is not None)
        
        entity = cls(
            raw_start=raw_start,
            raw_start_alt=raw_start_alt,
            raw_end=raw_end, 
            raw_end_alt=raw_end_alt,
            calendar_input_count=calendar_count,
            text=text,
            mapper=mapper
        )
        
        # Enrich with additional mapper data
        entity.enrich_with_mapper_data()
        
        return entityfrom dataclasses import dataclass



