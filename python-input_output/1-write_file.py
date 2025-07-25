#!/usr/bin/python3
"""Module that defines a function to write a string to a text file (UTF8)."""


def write_file(filename="", text=""):
    """Writes a string to a text file.
    Returns the number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
