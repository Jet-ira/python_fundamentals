#!/usr/bin/python3
"""a program that allow a user to enter password with only 3 attempts is allowed
if the correct password secure123 is entered
print Access granted
if the wrong password is entered 3 times
print access denied"""

# Set the correct password
correct_password = "secure123"

# Allow up to 3 attempts
attempts = 3

while attempts > 0:
    # Ask the user to enter a password
    password = input("Enter your password: ")

    # Check if the password is correct
    if password == correct_password:
        print("Access Granted!")
        break  # Exit the loop if correct
    else:
        attempts -= 1  # Reduce attempts
        if attempts > 0:
            print(f"Incorrect password! You have {attempts} attempt(s) left.")
        else:
            print("Access Denied!")
