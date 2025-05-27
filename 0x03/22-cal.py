#!/usr/bin/python
"""a module that perform calculator operation"""
import sys

def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2


operator = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

args = sys.argv
if len(args) != 4:
    print("invalid operation")
    exit(1)

num1 = float(args[1])
op = args[2]
num2 = float(args[3])

for key, func in operator.items():
    if key == op:
        result = func(num1, num2)
        print(result)
        break