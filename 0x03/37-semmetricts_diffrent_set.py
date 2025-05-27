#!/usr/bin/python
"""Write a function that returns the symmetric difference of two sets.
Explain what symmetric difference means in your docstring or comment."""

def symmetric_difference(set1, set2):
    """
    Returns the symmetric difference of two sets.

    The symmetric difference is the set of elements that are in either of the two sets,
    but not in both. In other words, it excludes the common elements.

    Example:
        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        Result = {1, 2, 4, 5}
    """
    return set1 ^ set2

a = {1, 2, 3}
b = {3, 4, 5}
print(symmetric_difference(a, b))
