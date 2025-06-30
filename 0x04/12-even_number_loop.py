#!/usr/bin/python
"""Create a program that uses a for loop to print 
all even numbers between 1 and 50. Use the range() function.
Include a conditional to check for even numbers using the modulo operator.
Print each number on a new line."""

# Print even numbers between 1 and 50 using a for loop
print("Even numbers from 1 to 50:")

for number in range(1, 51):
    if number % 2 == 0:  # Check if the number is even
        print(number)
