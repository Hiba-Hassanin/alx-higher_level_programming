#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    sys.argv.pop(0)

    argvlength = len(sys.argv)
    # The length of sys.argv gives the number of command-line arguments.

    if (argvlength == 0):
        # If there are no arguments, print "0 arguments.".
        print("0 arguments.")
    elif (argvlength == 1):
        # If there is only one argument, print "1 argument:" and the argument itself.
        print("1 argument:")
        print("{:d}: {}".format(len(sys.argv), sys.argv[0]))
    else:
        # If there are multiple arguments, print "{:d} arguments:" and loop through the arguments.
        print("{:d} arguments:".format(argvlength))
        number = 1
        for argument in sys.argv:
            # Loop through the arguments and print each argument with its position.
            print("{:d}: {}".format(number, argument))
            number += 1
