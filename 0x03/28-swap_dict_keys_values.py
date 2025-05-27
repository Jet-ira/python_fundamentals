#!/usr/bin/python
"""Write a function that swaps keys and values in a dictionary.
{"a": 1, "b": 2} → {1: "a", 2: "b"}"""

def swap_keys_values(d):
    return {value: key for key, value in d.items()}

original_dict = {"a": 1, "b": 2}
swapped_dict = swap_keys_values(original_dict)
print(swapped_dict)
