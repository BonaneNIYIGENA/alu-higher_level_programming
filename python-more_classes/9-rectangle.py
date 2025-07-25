#!/usr/bin/python3
"""Defines a Rectangle class with extra utility methods."""
# Two blank lines above class required by PEP 8.


class Rectangle:
    """Represents a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a rectangle instance."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    # -------------------- deletion --------------------
    def __del__(self):
        """Print message and update instance count when deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    # -------------------- width property --------------
    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # -------------------- height property -------------
    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # -------------------- instance methods ------------
    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    # -------------------- string representations ------
    def __str__(self):
        """Return a printable string using print_symbol."""
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)
        line = symbol * self.width
        return "\n".join(line for _ in range(self.height))

    def __repr__(self):
        """Return a recreatable string representation."""
        return "Rectangle({}, {})".format(self.width, self.height)

    # -------------------- comparison utility ----------
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the greater (or equal) area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    # -------------------- square class‑method ---------
    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size."""
        return cls(size, size)
