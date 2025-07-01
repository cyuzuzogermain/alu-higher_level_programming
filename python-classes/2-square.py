#!/usr/bin/python3


"""
Module: square

This module defines the Square class with a private size attribute.
"""


class Square:
        """
        Represents a square.

        Attributes:
        __size (any): The size of the square (no type/value checks).
        """

        def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
        size: The size of the square (no validation).   
        """
        self.__size = size
        """
        Initializing a try that check if the size is a number and also
        greater or equal to 0
        """
        try:
            if isinstance(self.__size, int) and self.__size > 0:
                continue
        """
        throwing explained exceptions to the user in case the above conditions 
        return errors
        """
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
