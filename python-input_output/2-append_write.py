#!/usr/bin/python3

"""
A function the appends text to
the end of a UTF-8 encoded file
"""


def append_write(filename="", text=""):
    """
    The function block
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
