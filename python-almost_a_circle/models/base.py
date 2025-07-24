#!/usr/bin/python3
"""
Base module: contains the Base class which will be the foundation
for all other classes in this project.
"""

class Base:
    """The Base class to manage `id` attribute for all future classes."""

    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """
        Initialize the base instance.

        Args:
            id (int, optional): The id to assign. If None, auto-increment is used.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

