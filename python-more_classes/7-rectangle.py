#!/usr/bin/python3
"""
Module: rectangle

Defines a Rectangle class that tracks instance
count, supports flexible
symbol printing, and includes geometric calculations.
"""


class Rectangle:
    """
    Represents a rectangle with width and height.

    Class Attributes:
        number_of_instances (int): Tracks number of active
        Rectangle instances.
        print_symbol: Symbol used for string representation.
        Default is '#'.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): Width of the rectangle (default 0).
            height (int): Height of the rectangle (default 0).
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
            value (int): Width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
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
            value (int): Height value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: Area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: Perimeter or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string visualizing the rectangle
        using `print_symbol`.

        Returns:
            str: Rectangle made of `print_symbol`, or
            empty string if zero size.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = str(self.print_symbol)
        lines = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """
        Returns a string that can recreate the Rectangle with eval().

        Returns:
            str: A string in the format Rectangle(width, height)
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Called when a Rectangle instance is deleted.

        Prints a message and decrements the instance count.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
