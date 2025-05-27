#!/usr/bin/python
"""Write a function that removes a key from a dictionary 
if it exists and returns the updated dictionary.
Parameters: dictionary and key to remove."""

def remove_key(d, key):
    if key in d:
        del d[key]
    return d

my_dict = {"a": 1, "b": 2, "c": 3}
updated_dict = remove_key(my_dict, "b")
print(updated_dict)
