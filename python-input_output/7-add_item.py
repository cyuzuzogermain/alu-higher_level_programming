#!/usr/bin/python3


import sys
import json
import os


def save_to_json_file(my_obj, filename):
    """
    Write a Python object to a file in JSON format.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """
    Load and return a Python object from a file containing JSON data.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    filename = "add_item.json"

    # Load existing items if file exists, otherwise use empty list
    if os.path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []

    # Add command-line arguments (excluding the script name) to the list
    items.extend(sys.argv[1:])

    # Save updated list back to the file
    save_to_json_file(items, filename)
