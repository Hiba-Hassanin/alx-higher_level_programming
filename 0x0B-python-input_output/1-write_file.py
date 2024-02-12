#!/usr/bin/python3
"""Function to write a string to a text file (UTF8)."""


def write_file(filename="", text=""):
    """Write a string to a text file and return the number of characters"""

    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
