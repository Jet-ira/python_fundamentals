#!/usr/bin/python
"""Write a function that checks if two sets have any common items and returns True or False."""

def have_common_items(set1, set2):
    return not set1.isdisjoint(set2)

a = {1, 2, 3}
b = {3, 4, 5}
c = {6, 7}

print(have_common_items(a, b))  
print(have_common_items(a, c))  
