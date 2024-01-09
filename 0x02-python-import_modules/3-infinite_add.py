#!/usr/bin/python3
import sys

def add_arguments(arguments):
    result = 0

    for argument in arguments:
        result += int(argument)

    print(result)

if __name__ == "__main__":
    arguments = sys.argv[1:]
    add_arguments(arguments)
