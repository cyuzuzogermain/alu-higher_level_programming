#!/usr/bin/python3
"""
Module: rectangle

Defines a Rectangle class with full functionality, including area/perimeter
methods, string representation, instance tracking, comparison, and a factory
method to create square rectangles.
"""


class Rectangle:
    """
    Represents a rectangle with width and height.

    Class Attributes:
        number_of_instances (int): Tracks the number of instances.
        print_symbol (any): Symbol used for string representation.
        Defaults to '#'.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): Width of the rectangle. Default is 0.
            height (int): Height of the rectangle. Default is 0.
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
            value (int): The new width.

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
            value (int): The new height.

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
        Calculate and return the area of the rectangle.

        Returns:
            int: width * height
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            int: 2 * (width + height), or 0 if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the rectangle using `print_symbol`.

        Returns:
            str: Multiline string using `print_symbol`,
            or empty string if 0 area
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = str(self.print_symbol)
        lines = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """
        Return a string that can recreate the Rectangle instance.

        Returns:
            str: "Rectangle(width, height)"
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Called when the instance is deleted.

        Prints a message and decrements the instance counter.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the rectangle with the bigger area.

        Args:
            rect_1 (Rectangle): First rectangle.
            rect_2 (Rectangle): Second rectangle.

        Returns:
            Rectangle: The bigger rectangle (or rect_1 if equal).

        Raises:
            TypeError: If either argument is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a new Rectangle instance with width == height == size.

        Args:
            size (int): The size of the square sides.

        Returns:
            Rectangle: A new Rectangle instance (square).
        """
        return cls(size, size)
