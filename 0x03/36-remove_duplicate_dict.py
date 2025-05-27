#!/usr/bin/python
"""Write a function that removes dictionary items 
with duplicate values, keeping only the first occurrence."""

def remove_duplicates_by_value(d):
    seen_values = set()
    result = {}
    for key, value in d.items():
        if value not in seen_values:
            result[key] = value
            seen_values.add(value)
    return result

data = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
cleaned = remove_duplicates_by_value(data)
print(cleaned)
