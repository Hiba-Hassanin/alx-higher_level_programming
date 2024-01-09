#!/usr/bin/python3
import sys

def print_arguments(arguments):
    num_arguments = len(arguments) - 1

    if num_arguments == 0:
        print("Number of argument(s): 0.")
        return

    print("Number of argument(s):", num_arguments)
    print("Arguments:")

    for i in range(1, len(arguments)):
        print(f"{i}: {arguments[i]}")

if __name__ == "__main__":
    arguments = sys.argv
    print_arguments(arguments)
