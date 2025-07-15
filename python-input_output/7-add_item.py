#!/usr/bin/python3

import sys
import json
import os

""" a function """

def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    filename = "add_item.json"

    """ main program """
    # Load existing list if file exists, else start with an empty list
    if os.path.exists(filename):
        data = load_from_json_file(filename)
    else:
        data = []

    # Add command-line arguments (excluding the script name) to the list
    data.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(data, filename)
