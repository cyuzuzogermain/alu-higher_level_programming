#!/usr/bin/python3
"""Module that creates a Python object from a JSON file."""

import json


def load_from_json_file(filename):
    """
    Load and return a Python object from a file containing JSON data.

    Args:
        filename: The name of the JSON file to read from.

    Returns:
        A Python object (e.g., dict, list) reconstructed from the JSON file content.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
