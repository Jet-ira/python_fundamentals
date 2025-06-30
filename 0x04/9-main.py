#!/usr/bin/python

# main.py

average = __import__("9-stats").average
maximum = __import__("9-stats").maximum
# Import the custom module

numbers = [8, 22, 17, 35, 42]

# Use the functions from stats.py
avg = average(numbers)
max_val = maximum(numbers)

# Print the results
print(f"Numbers: {numbers}")
print(f"Average: {avg}")
print(f"Maximum: {max_val}")
