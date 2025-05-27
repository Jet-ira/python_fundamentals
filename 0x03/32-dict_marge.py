#!/usr/bin/python
"""Write a function that merges two dictionaries. 
If a key exists in both, keep the value from the second dictionary."""

def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

dict_a = {"x": 1, "y": 2}
dict_b = {"y": 3, "z": 4}

result = merge_dictionaries(dict_a, dict_b)
print(result) 
