#!/usr/bin/python3
"""a calculator"""
add = __import__('2-add').add
mul = __import__('3-mul').mul
div = __import__('4-div').div
sub = __import__('13-sub').sub 

if __name__ == '__main__':
    num1 = int(input("Enter the first number"))
    num2 = int(input("Enter the second name"))
    op = input("Enter operation")

if op == "+":
    print(add(num1, num2))
elif op == "/":
    print(div(num1, num2))
elif op == "*":
    print(mul(num1, num2))
elif op == "-":
    print(sub(num1, num2))
else:
    print("invalid operator")