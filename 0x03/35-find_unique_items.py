#!/usr/bin/python
"""Write a function that takes two lists and returns 
a set of items that appear in only one list."""

def unique_items(list1, list2):
    return set(list1) ^ set(list2)

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
result = unique_items(a, b)
print(result)
