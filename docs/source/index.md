# Arabic Date Module

A comprehensive Python package for detecting, parsing, and converting dates across Arabic, Persian, and Western calendar systems.

## Overview

This package provides robust tools for working with dates in multilingual texts, supporting:

- Hijri (Islamic) calendar
- Gregorian (Western) calendar 
- julian (Persian) calendar

## Key Features

- **Intelligent Date Detection**
  - Natural language date parsing
  - Multi-calendar format support
  - Complex date pattern recognition
  - Cross-calendar references handling

- **Calendar Conversion**
  - Bidirectional conversion between calendars
  - Accurate astronomical calculations
  - Historical date support
  - Era handling (AH, AD, SH)

- **Text Processing**
  - Arabic text normalization
  - Date expression extraction
  - Contextual disambiguation
  - Multiple dialect support

- **Pattern Matching**
  - Sophisticated regex patterns
  - Named month recognition
  - Weekday integration
  - Mixed format handling

## Documentation Structure

```{toctree}
:maxdepth: 2
:caption: Contents

user_guide/installation
user_guide/quickstart
user_guide/examples
api/calendar_variants
api/normalizers
api/regex_patterns
api/utils
```

## Quick Example

```python
from ar_date_module import DateDetector, CalendarConverter

# Create a detector instance
detector = DateDetector()

# Detect dates in text
text = "تم النشر يوم الجمعة 15 محرم 1445 هـ الموافق 4 أغسطس 2023 م"
dates = detector.detect(text)

# Convert between calendars
converter = CalendarConverter()
gregorian_date = converter.hijri_to_gregorian(1445, 1, 15)
```

## Installation

```bash
pip install ar-date-module
```

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](contributing.md) for details on how to submit pull requests, report issues, and contribute to the project.

## License

This project is licensed under the MIT License - see the [LICENSE](license.md) file for details.

## Authors

- **Mohammad Lotfi** - *Initial work* - [GitHub](https://github.com/mlotfi)

## Acknowledgments

- Arabic language processing community
- Open source calendar conversion libraries
- Documentation contributors