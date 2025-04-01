#!/usr/bin/python3
"""a function that Takes a string as input
Counts and returns the number of vowels (a, e, i, o, u) in the string"""

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

result = count_vowels("abacbecdio")
print(result)