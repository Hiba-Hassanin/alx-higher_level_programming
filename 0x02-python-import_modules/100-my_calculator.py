#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    argv.pop(0)
    argvlength = len(argv)

    if argvlength == 3:
        a = int(argv[0])
        operator = argv[1]
        b = int(argv[2])

        operators = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div
        }

        if operator in operators:
            result = operators[operator](a, b)
            print(f"{a} {operator} {b} = {result}")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
