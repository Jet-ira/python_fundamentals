#!/usr/bin/python3
"""a function named reverse_list(lst) that
Takes a list as input
Returns the list reversed, but without using the .reverse() method"""

def reverse_list(lst):

    return lst[-1]
result = reverse_list([1, 2, 3, 4, 5])

print(result)