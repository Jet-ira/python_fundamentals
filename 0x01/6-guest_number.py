#!/usr/bin/py
"""a program that generates a random number 1 ans 20
ask the user to guess the number
if the guest is correct print congratulation you guessed it and exit
if the guess is too high print too high try again
if the guess is too low print too low try again
keep asking untill the correct number is guessed"""
import random
# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

# Loop until the user guesses correctly
while 1:
    try:
        guess = int(input("Guess a number between 1 and 20: "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations, you guessed it!")
            break  # Exit the loop when guessed correctly
    except ValueError:
        print("Invalid input! Please enter a valid number.")
