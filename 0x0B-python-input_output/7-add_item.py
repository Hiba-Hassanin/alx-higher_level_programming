#!/usr/bin/python3


import sys
import json
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_item():
    """
    Adds all arguments to a Python list and saves them to a file.
    """

    filename = 'add_item.json'

    # Check if the file exists and load its contents if it does
    if exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []

    # Add command-line arguments to the list
    items.extend(sys.argv[1:])

    # Save the list as a JSON representation in the file
    save_to_json_file(items, filename)

if __name__ == '__main__':
    add_item()
