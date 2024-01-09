#!/usr/bin/python3
import sys

def print_arguments(arguments):
    num_arguments = len(arguments) - 1

    if num_arguments > 1:
        print(f"{num_arguments} arguments:")
    elif num_arguments == 0:
        print(f"{num_arguments} arguments.")
    else:
        print(f"{num_arguments} argument:")

    for i, argument in enumerate(arguments):
        if i == 0:
            continue
        print(f"{i}: {argument}")

if __name__ == "__main__":
    arguments = sys.argv
    print_arguments(arguments)
