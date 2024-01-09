#!/usr/bin/python3
import sys

def print_arguments(arguments):
    num_arguments = len(arguments) - 1

    if num_arguments == 0:
        print("0 arguments.")
    else:
        if num_arguments == 1:
            print("1 argument:")
        else:
            print(f"{num_arguments} arguments:")

        for i in range(1, len(arguments)):
            print(f"{i}: {arguments[i]}")

if __name__ == "__main__":
    arguments = sys.argv
    print_arguments(arguments)
