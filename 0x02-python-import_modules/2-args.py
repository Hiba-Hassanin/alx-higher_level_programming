#!/usr/bin/python3
import sys

def print_arguments(arguments):
    num_arguments = len(arguments) - 1

    if num_arguments > 1:
        print("{:d} arguments:".format(num_arguments))
    elif num_arguments == 0:
        print("{:d} arguments.".format(num_arguments))
    else:
        print("{:d} argument:".format(num_arguments))

    for i, argument in enumerate(arguments):
        if i == 0:
            continue
        print("{:d}: {}".format(i, argument))

if __name__ == "__main__":
    arguments = sys.argv
    print_arguments(arguments)
