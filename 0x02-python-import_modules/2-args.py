#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    num_arguments = len(argv) - 1
    arguments = argv[1:]

    print("{} {}{}.".format(num_arguments, "argument" if num_arguments == 1 else "arguments", ":" if num_arguments > 0 else "."))

    for i, argument in enumerate(arguments, start=1):
        print("{}: {}".format(i, argument))
