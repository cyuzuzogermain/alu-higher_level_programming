#!/usr/bin/python3

"""
A function to read files and print them to
stdout
"""


def read_file(filename=""):
    """
    The function block
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
