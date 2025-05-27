#!/usr/bin/python
"""Write a function that takes a list of items and returns a
 dictionary with the count of each item.   Example: 
["apple", "banana", "apple"] → {"apple": 2, "banana": 1}."""

def count_items(items):
    count_dict = {}
    for item in items:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

fruits = ["apple", "banana", "apple"]
result = count_items(fruits)
print(result)
