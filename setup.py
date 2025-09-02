from setuptools import setup, find_packages

def read_version():
    with open("VERSION", "r") as f:
        return f.read().strip()

setup(
    name="detect_dates",
    version=read_version(),
    description="Detects, extracts, and normalizes complex and non-standard Arabic/English date patterns from text. Supports Hijri, Gregorian, and Shamsi calendars. This repository is currently under active testing and development.",
    author="m.lotfi",
    packages=find_packages(),
    install_requires=[
        "regex>=2021.8.3",
        "numpy>=1.21.0",
        "pandas>=1.3.0",
    ],
)
