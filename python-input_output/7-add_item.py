#!/usr/bin/python3
import sys      # For accessing command-line arguments
import json     # For JSON file handling
import os       # For checking if the file exists

def save_to_json_file(my_obj, filename):
    """
    Save a Python object to a file in JSON format.

    Args:
        my_obj: The Python object to serialize (e.g., list, dict).
        filename: The name of the file where the JSON data will be saved.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """
    Load a Python object from a file containing JSON data.

    Args:
        filename: The name of the file to read from.

    Returns:
        A Python object (usually a list or dict) reconstructed from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    # The name of the file where the list will be saved
    filename = "add_item.json"

    # Step 1: Load existing data from the file if it exists, else start with an empty list
    if os.path.exists(filename):
        data = load_from_json_file(filename)
    else:
        data = []

    # Step 2: Append all command-line arguments (excluding the script name itself)
    data.extend(sys.argv[1:])

    # Step 3: Save the updated list back to the file
    save_to_json_file(data, filename)
