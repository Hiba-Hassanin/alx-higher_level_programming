#!/usr/bin/python3
"""Function reads a text file (UTF8) and print it to stdout."""


def read_file(filename=""):
    """Read a text file (UTF8) and print it to stdout."""

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
