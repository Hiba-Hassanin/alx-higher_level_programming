#!/usr/bin/python3

from add_0 import add

a, b = 1, 2
result = add(a, b)

output = "{a:d} + {b:d} = {result:d}"
print(output.format(a=a, b=b, result=result))
