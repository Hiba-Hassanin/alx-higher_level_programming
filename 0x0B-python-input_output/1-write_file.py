#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Write a string to a text file and return the number of characters written.

    Args:
        filename (str): The name of the text file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)

if __name__ == "__main__":
    write_file()
