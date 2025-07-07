#!/usr/bin/python3
"""
Module: square

This module defines a class Square that represents a geometric square.
It includes input validation to ensure the size attribute is a non-negative integer.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The length of one side of the square. Must be a non-negative integer.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square's side. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
