#!/usr/bin/python
"""Write a function called is_multiple(a, b) that returns True if a is 
a multiple of b, otherwise False. Use the modulo operator %.
Use logical operators to check if both a is a multiple of b and b is a multiple of a.
Test your function with different values and print the results."""

def is_multiple(a, b):
    """
    Returns True if a is a multiple of b or b is a multiple of a.
    Returns False otherwise.
    """
    if a == 0 or b == 0:
        return False  # Avoid division by zero

    return a % b == 0 or b % a == 0


# Test the function with different values
test_cases = [
    (10, 2),
    (2, 10),
    (15, 5),
    (7, 3),
    (0, 5),
    (5, 0),
    (6, 6)
]

print("Testing is_multiple(a, b):")
for a, b in test_cases:
    result = is_multiple(a, b)
    print(f"is_multiple({a}, {b}) => {result}")
