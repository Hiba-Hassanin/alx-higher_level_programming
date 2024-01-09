#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

def perform_operation(a, operator, b):
    if operator == '+':
        result = add(a, b)
        operator_symbol = '+'
    elif operator == '-':
        result = sub(a, b)
        operator_symbol = '-'
    elif operator == '*':
        result = mul(a, b)
        operator_symbol = '*'
    elif operator == '/':
        result = div(a, b)
        operator_symbol = '/'
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print(f"{a} {operator_symbol} {b} = {result}")

if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    perform_operation(a, operator, b)
