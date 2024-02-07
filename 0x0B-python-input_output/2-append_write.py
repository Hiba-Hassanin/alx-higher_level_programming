#!/usr/bin/python3

def append_write(filename="", text=""):
    """Appends a string to a text file and returns the number of characters added."""
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        return len(text)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: ./2-append_write.py filename text", file=sys.stderr)
        sys.exit(1)
    print(append_write(sys.argv[1], sys.argv[2]))
