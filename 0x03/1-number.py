#!/usr/bin/python3
"""a program that count 1 to 20 and skip multiple of 5"""
for num in range(1, 20):
    if num % 5 == 0:
        continue
    else:
        print(num)
