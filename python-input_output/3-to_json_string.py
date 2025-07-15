#!/usr/bin/python3
"""
Module that returns the JSON representation of an object (string).
"""


import json

def to_json_string(my_obj):
    """
    Convert a Python object to a JSON-formatted string.

    Args:
        my_obj: The Python object to serialize (e.g., dict, list, int, str).

    Returns:
        A string containing the JSON representation of `my_obj`.
    """
    return json.dumps(my_obj)
