#!/usr/bin/python
"""Write a program that keeps asking the user to enter numbers until they enter 0.
Use a while loop. Add all numbers entered (excluding the zero).
Print the total sum after the loop ends."""

total = 0  # Initialize the sum

print("Enter numbers to add. Enter 0 to stop.")

while True:
    try:
        number = float(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if number == 0:
        break  # Exit the loop if the user enters 0

    total += number  # Add the number to the total

print(f"\nTotal sum of entered numbers (excluding 0): {total}")
