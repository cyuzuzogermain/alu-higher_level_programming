#!/usr/bin/python3

"""
A fundtion that wrtires a string to a
text file and returns the number of chars
written
"""


def write_file(filename="", text=""):
    """
    Function block
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
