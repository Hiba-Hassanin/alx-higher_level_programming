#!/usr/bin/python3
import sys
import importlib.util

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
        sys.exit(1)

    print(f"{a} {operator_symbol} {b} = {result}")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    spec = importlib.util.spec_from_file_location('calculator_1', './calculator_1.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    add = module.add
    sub = module.sub
    mul = module.mul
    div = module.div

    perform_operation(a, operator, b)
