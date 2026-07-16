"""
===========================================================================
Project     : Autonomous AI Agent Platform
Module      : helpers.py

Description:
    Common helper functions used throughout the application.

Purpose:
    This module provides reusable utility functions that eliminate
    duplicate code and improve consistency across the project.

Responsibilities:
    - Generate unique identifiers
    - Generate timestamps
    - Convert Python objects to JSON
    - Print formatted JSON

Author      : Lokesh Kumar
Version     : v1.0.0
===========================================================================
"""

# ==========================================================================
# Standard Library Imports
# ==========================================================================

# Import the JSON module for serialization.
import json

# Import UUID utilities for generating unique identifiers.
import uuid

# Import date and time utilities.
from datetime import datetime


# ==========================================================================
# Helper Functions
# ==========================================================================

def generate_unique_id() -> str:
    """
    Generate a universally unique identifier.

    Returns
    -------
    str
        UUID represented as a string.
    """

    # Generate and return a UUID.
    return str(uuid.uuid4())


def get_current_timestamp() -> str:
    """
    Return the current timestamp.

    Returns
    -------
    str
        Current date and time in ISO-8601 format.
    """

    # Return the current timestamp.
    return datetime.now().isoformat()


def to_json(data: object) -> str:
    """
    Convert a Python object into formatted JSON.

    Parameters
    ----------
    data : object
        Object to serialize.

    Returns
    -------
    str
        Formatted JSON string.
    """

    # Convert the object into formatted JSON.
    return json.dumps(
        data,
        indent=4,
        default=str,
    )


def print_json(data: object) -> None:
    """
    Print formatted JSON.

    Parameters
    ----------
    data : object
        Object to print.
    """

    # Print the formatted JSON.
    print(to_json(data))


# ==========================================================================
# End of File
# ==========================================================================