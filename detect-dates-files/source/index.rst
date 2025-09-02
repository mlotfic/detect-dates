Arabic Date Module
=================

A comprehensive Python package for detecting, parsing, and converting dates across 
Arabic, Persian, and Western calendar systems.

.. image:: https://img.shields.io/pypi/v/ar-date-module.svg
   :target: https://pypi.org/project/ar-date-module/
   :alt: PyPI version

.. image:: https://img.shields.io/github/license/mlotfi/ar-date-module.svg
   :target: https://github.com/mlotfi/ar-date-module/blob/main/LICENSE
   :alt: License

Features
--------

- Multi-calendar date detection and parsing
- Natural language processing for Arabic dates
- Calendar conversion utilities
- Extensive regex pattern library
- Cross-calendar reference handling

Documentation
------------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   user-guide/installation
   user-guide/quickstart
   user-guide/examples
   user-guide/configuration

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api/calendar_variants
   api/normalizers
   api/regex_patterns
   api/utils

.. toctree::
   :maxdepth: 1
   :caption: Development

   contributing
   changelog
   license

Quick Example
------------

.. code-block:: python

    from ar_date_module import DateDetector, CalendarConverter

    # Create a detector instance
    detector = DateDetector()

    # Detect dates in text
    text = "تم النشر يوم الجمعة 15 محرم 1445 هـ الموافق 4 أغسطس 2023 م"
    dates = detector.detect(text)

    # Convert between calendars
    converter = CalendarConverter()
    gregorian_date = converter.hijri_to_gregorian(1445, 1, 15)

Installation
-----------

.. code-block:: bash

    pip install ar-date-module

Indices and Tables
-----------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`