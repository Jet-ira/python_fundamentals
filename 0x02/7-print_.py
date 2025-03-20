#!/usr/bin/python
"""a function that print any character"""
def print_at(str, n):
    new_str = ""
    for num in range(len(str)):
        if num == n:
            new_str += str[num]
            break
    return new_str

print(print_at("python is awsome", 11))