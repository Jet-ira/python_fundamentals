#!/usr/bin/python3
"""a programm that takes a number input from the user
determine if the number is positive, negative, or zero
using comparison operator addition to check if the number is a floating point or integer  
print the corresponding"""
# Get input from the user
num = input("Enter a number: ")

# Try to convert input to a float
try:
    num = float(num)
    
    # Determine if the number is positive, negative, or zero
    if num > 0:
        sign = "Positive"
    elif num < 0:
        sign = "Negative"
    else:
        sign = "Zero"

    # Check if the number is an integer or a floating point
    if num == int(num):  # If float value equals its integer version, it's an integer
        num_type = "Integer"
    else:
        num_type = "Floating Point"

    # Print the result
    print(f"The number is {sign} and is of type {num_type}.")

except ValueError:
    print("Invalid input! Please enter a valid number.")