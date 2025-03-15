#!/usr/bin/python3
"""a program taht print from 1 to 50 if a number is divisible by 3 print fizz
if a number divisible by 5 print buzz if divisible by both 3 and 5 print buzz"""
for num in range(1, 50):
    if num % 3 == 0 and num % 5 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    elif num % 3 == 0:
        print("fizzbuzz")
    else:
        print(num)