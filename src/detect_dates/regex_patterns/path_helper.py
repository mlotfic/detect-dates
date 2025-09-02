#!/usr/bin/env python3
"""
Created on Thu Jul 24 20:01:16 2025

@author: m.lotfi

@description:

"""

# my_package/path_helper.py
import sys
import os
from pathlib import Path

# This module helps manage the Python path for importing modules in a package structure.
# ===================================================================================
# Function to add the parent of the last 'modules' folder to sys.path
def add_modules_to_sys_path(start_path: Path = None):
    """
    Add the parent of the last 'modules' folder in the current path tree to sys.path
    """
    if start_path is None:
        start_path = Path(__file__).resolve()

    # Go up through all parents and record all 'modules' matches
    modules_paths = [p for p in start_path.parents if p.name == 'modules']

    if not modules_paths:
        raise FileNotFoundError("'modules' folder not found in any parent directories")

    # Get the LAST (closest to root) match and its parent
    target_path = modules_paths[-1].parent

    if str(target_path) not in sys.path:
        sys.path.insert(0, str(target_path))  # Insert at the beginning to prioritize
        print(f"[sys.path] Added: {target_path}")
    else:
        print(f"[sys.path] Already exists: {target_path}")

    return target_path

#
# ===================================================================================
# Function to set up the package path
def setup_package_path():
    """Add package root to Python path for imports"""
    package_root = Path(__file__).parent.absolute()
    if str(package_root) not in sys.path:
        sys.path.insert(0, str(package_root))
    return package_root

# Call this at module level
# PACKAGE_ROOT = setup_package_path()

# This module helps manage the Python path for importing modules in a package structure.
# ===================================================================================
# Function to add the parent of the last 'data' folder to sys.path
def add_data_to_sys_path(start_path: Path = None):
    """
    Add the parent of the last 'data' folder in the current path tree to sys.path
    """
    if start_path is None:
        start_path = Path(__file__).resolve()

    # Go up through all parents and record all 'data' matches
    modules_paths = [p for p in start_path.parents if p.name == 'data']

    if not modules_paths:
        raise FileNotFoundError("'data' folder not found in any parent directories")

    # Get the LAST (closest to root) match and its parent
    target_path = modules_paths[-1].parent

    if str(target_path) not in sys.path:
        sys.path.insert(0, str(target_path))  # Insert at the beginning to prioritize
        print(f"[sys.path] Added: {target_path}")
    else:
        print(f"[sys.path] Already exists: {target_path}")

    return target_path

# Import path helper to ensure modules directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    print("This module is not intended to be run directly. Import it in your code.")
    # This is necessary for importing other modules in the package structure
    from path_helper import add_modules_to_sys_path
    # Ensure the modules directory is in sys.path for imports
    add_modules_to_sys_path()
    # Optionally, add data directory to sys.path
    add_data_to_sys_path()