#!/usr/bin/python3

def read_file(filename=""):
    """ The function reads a text file and then prints it to stdout """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")

if __name__ == "__main__":
    read_file()
