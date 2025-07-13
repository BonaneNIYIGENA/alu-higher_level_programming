#!/usr/bin/python3
"""
This module defines the MyList class, which inherits from list
and adds a method to print the list sorted.
"""


class MyList(list):
    """
    Represents a list with an additional method to print a sorted version.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending order without modifying
        the original list.
        """
        print(sorted(self))
