#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for.
        new_string (str): The line of text to insert.

    """

    new_content = []
    with open(filename, 'r') as file:
        for line in file:
            new_content.append(line)
            if search_string in line:
                new_content.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(new_content)

# Test the function
if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "\"C is fun!\\n\"")
