#!/usr/bin/python3
"""Defines a class Square with size validation, getter, and setter."""


class Square:
    """Represents a square with size control and area computation."""

    def __init__(self, size=0):
        """Initialize the square with optional size."""
        self.size = size  # use the setter for validation

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value: The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current square area."""
        return self.__size ** 2
