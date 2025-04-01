#!/usr/bin/3
"""a function named remove_duplicates(lst) that
Takes a list as input
Returns a new list with all duplicates removed"""
def remove_duplicates(lst):
    return list(set(lst))

result = remove_duplicates([1, 2, 2, 3, 5, 3, 4, 4, 5])
print(result)