#!/usr/bin/python
"""Create a program that asks the user for a score between 0 and 100.
Using conditionals, print the corresponding grade based on the following:"""


# Ask the user for a score between 0 and 100
score = int(input("Enter your score (0–100): "))

# Check and print the corresponding grade
if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score <= 89:
    print("Grade: B")
elif 70 <= score <= 79:
    print("Grade: C")
elif 60 <= score <= 69:
    print("Grade: D")
elif 0 <= score <= 59:
    print("Grade: F")
else:
    print("Invalid score! Please enter a number between 0 and 100.")

