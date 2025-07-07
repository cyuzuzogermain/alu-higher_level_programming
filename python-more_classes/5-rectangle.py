#!/usr/bin/python3
"""
Module: rectangle

Defines a Rectangle class with width and height, including methods
to compute area and perimeter, provide printable representations,
and handle deletion with a message.
"""


class Rectangle:
    """
    Represents a rectangle with width and height.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): Width of the rectangle (default is 0).
            height (int): Height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width with validation.

        Args:
            value (int): The new width.

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
        """Getter for the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height with validation.

        Args:
            value (int): The new height.

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
            int: Area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: Perimeter (2 * (width + height)), or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a printable string representation of the rectangle using '#'.

        Returns:
            str: Multiline string of '#' characters or empty string if
            any dimension is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        lines = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """
        Returns a string that can recreate the rectangle instance with eval().

        Returns:
            str: A string like 'Rectangle(width, height)'.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Called when the instance is about to be destroyed.

        Prints a message indicating the rectangle is being deleted.
        """
        print("Bye rectangle...")

