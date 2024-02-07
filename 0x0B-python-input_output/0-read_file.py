#!/usr/bin/python3

def read_file(filename=""):
    """
    Read and print the content of a text file to stdout.

    Args:
        filename (str): The name of the text file to read.

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')

if __name__ == "__main__":
    read_file()
