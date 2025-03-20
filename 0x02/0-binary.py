#!/usr/bin/python3
"""a program that convert number to binary"""
def binary(decimal):
    rem = []
    while decimal > 0:
        rem.insert(0, str(decimal % 2))
        decimal //= 2
    return "".join(rem)


print(binary(8))