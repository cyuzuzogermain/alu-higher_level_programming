#!/usr/bin/python3
"""
Module that returns the dictionary description
of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Return the dictionary representation of a simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        A dictionary containing all serializable
        attributes of the object.
    """
    return obj.__dict__
