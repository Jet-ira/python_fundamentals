#!/usr/bin/python3
"""a programm that ask a user password the password must be at least 8 characters long
contain at least one digit contain at least one upper case
use a loop to keep asking for a password untill all conditions are met"""

def is_valid_password(password):
    """check if the passwords meets the required codition."""
    if len(password) < 8:
        print("password must be at least 8 characters long.")
        return False
    if not any(char.isdigit() for char in password):
        print("password must contain at least one digit.")
        return False
    if not any(char.isupper() for char in password):
        return False
    return True


# loop untill a valid password is entered
while True:
    password = input("Enter a strong password: ")
    if is_valid_password(password):
        print("password accepted!")
        "break" # Exist loop when password is valid