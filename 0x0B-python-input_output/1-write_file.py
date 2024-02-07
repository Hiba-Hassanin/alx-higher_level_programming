#!/usr/bin/python3

import sys

def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written."""
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
        return len(text)

if len(sys.argv) != 3:
    print("Usage: ./1-write_file.py filename text", file=sys.stderr)
    sys.exit(1)

print(write_file(sys.argv[1], sys.argv[2]))
