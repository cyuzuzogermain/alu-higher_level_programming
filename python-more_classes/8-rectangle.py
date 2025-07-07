#!/usr/bin/python3
"""
Module: rectangle

Defines a Rectangle class that supports instance
tracking, flexible symbol
representation, and comparison of rectangles based on area.
"""


class Rectangle:
    """
    Represents a rectangle with width and height.

    Class Attributes:
        number_of_instances (int): Tracks number of active instances.
        print_symbol: Symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): Rectangle width (default is 0).
            height (int): Rectangle height (default is 0).
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
            TypeError: If not an integer.
            ValueError: If less than 0.
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
            TypeError: If not an integer.
            ValueError: If less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle.

        Returns:
            int: width * height
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.

        Returns:
            int: 2 * (width + height), or 0 if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle
        using print_symbol.

        Returns:
            str: Rectangle represented by print_symbol, or
            empty string if 0 size.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = str(self.print_symbol)
        lines = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """
        Returns a string that can recreate this instance using eval().

        Returns:
            str: Rectangle(width, height)
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Called when a Rectangle instance is deleted.

        Prints a message and decrements the instance counter.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the one with the bigger area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: The rectangle with the greater or equal area.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
