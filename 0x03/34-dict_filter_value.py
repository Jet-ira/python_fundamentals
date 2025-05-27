#!/usr/bin/python
"""Write a function that returns a new dictionary only containing 
items where the value is greater than a given number."""

def filter_by_value(d, threshold):
    return {k: v for k, v in d.items() if v > threshold}

data = {"a": 5, "b": 10, "c": 3}
result = filter_by_value(data, 4)
print(result)
