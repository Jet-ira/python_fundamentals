#!/usr/bin/python3
"""a program that perform the function of a calculator"""

num1 = eval(input("Enter any number of your choice"))
num2 = eval(input("Enter any number of your chopice"))

op = input("Enter operator")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("invalid operator")