#!/usr/bin/python3
"""a programm that take an intiger input from the user
check if the number is even or odd using modulus operator
print the number is even if its visible by 2
otherwise print the number is odd"""
intiger = int(input("Enter intiger input from the the usre: "))
if intiger % 2 == 0:
    print("the number is even if its visible by 2")
else:
    print("the number is odd")