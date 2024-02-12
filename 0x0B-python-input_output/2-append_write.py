#!/usr/bin/python3
"""Function to append a string to the end of a text file (UTF8)."""


def append_write(filename="", text=""):
    """Append string to end of a text file and return number of characters"""

    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
