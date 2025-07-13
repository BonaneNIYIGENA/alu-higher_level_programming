#!/usr/bin/python3
"""Defines a Rectangle class with area comparison capability."""
class Rectangle:
    """Rectangle with width, height, instance count, and custom print symbol."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    # -------------------- width property --------------------
    @property
    def width(self):
        """Width getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # -------------------- height property -------------------
    @property
    def height(self):
        """Height getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # -------------------- instance methods ------------------
    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter, or 0 if width or height is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    # -------------------- dunder methods --------------------
    def __str__(self):
        """Return a string of the rectangle using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        sym = str(self.print_symbol)
        return "\n".join(sym * self.__width for _ in range(self.__height))

    def __repr__(self):
        """Return a recreatable string representation."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message and update instance count when deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    # -------------------- static method ---------------------
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the greater (or equal) area.

        Args:
            rect_1: first Rectangle instance.
            rect_2: second Rectangle instance.

        Raises:
            TypeError: if rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
