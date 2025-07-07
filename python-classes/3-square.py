#!/usr/bin/python3
"""
Module: square

This module defines a Square class that models a square with a given size.
It includes size validation and a method to compute the square's area.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The length of a side of the square. Must be a non-negative integer.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2
