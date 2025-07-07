#!/usr/bin/python3
"""
Module: rectangle

This module defines a Rectangle class that tracks
the number of instances,
allows for area and perimeter calculations, and provides
string representations.
"""


class Rectangle:
    """
    Represents a rectangle with width and height.

    Attributes:
        number_of_instances (int): Tracks the number
        of Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): Width of the rectangle. Defaults to 0.
            height (int): Height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width with validation.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height with validation.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: Area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: Perimeter (2 * (width + height)), or 0 if
            width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a user-friendly string representation
        using '#' characters.

        Returns:
            str: A multiline string of '#'s representing the rectangle,
                 or an empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        lines = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """
        Returns an official string representation of the rectangle
        that can recreate a new instance using eval().

        Returns:
            str: A string in the form Rectangle(width, height).
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Called when an instance is deleted.

        Prints a goodbye message and decrements the instance counter.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
