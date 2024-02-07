#!/usr/bin/python3

def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: ./0-read_file.py filename", file=sys.stderr)
        sys.exit(1)
    read_file(sys.argv[1])
