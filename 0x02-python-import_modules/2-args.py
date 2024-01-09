#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args = sys.argv[1:]
    num_arguments = len(args)

    print("{} {}{}{}".format(num_arguments, "argument" if num_arguments == 1 else "arguments", ":" if num_arguments > 0 else ".", "\n" if num_arguments > 0 else ""))

    for i, argument in enumerate(args, start=1):
        print("{}: {}".format(i, argument))
