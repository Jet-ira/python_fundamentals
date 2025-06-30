#!/usr/bin/python
"""Create a module called stats.py with two functions
average(lst) that returns the average of numbers in a list.
maximum(lst) that returns the highest number in a list.
Then, in this file, import your module and use it on a sample list of integers."""

# stats.py

def average(lst):
    """Returns the average of numbers in the list."""
    if not lst:
        return 0
    return sum(lst) / len(lst)

def maximum(lst):
    """Returns the highest number in the list."""
    if not lst:
        return None
    return max(lst)
