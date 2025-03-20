#!/usr/bin/python3
"""a function that create a copy of a string removing the character at the position n"""
def remove_char_at(str, n):
    new_str = ""
    for num in range(len(str)):
        if num != n:
            new_str += str[num]
    return new_str

print(remove_char_at("python is awsome", 11))