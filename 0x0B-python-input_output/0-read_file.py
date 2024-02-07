#!/usr/bin/python3

def read_file(filename=""):
    """ The function reads a text file and then prints it to stdout """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
