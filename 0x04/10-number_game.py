#!/usr/bin/python
"""Write a game where the program generates a random number between 1 and 20 (hint: use random module).
Ask the user to guess the number. If the guess is too high or too low, let them know.
Allow up to 5 attempts and print "Game Over" if they fail.
Use loops, conditionals, and the random module."""

import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

# Allow up to 5 attempts
max_attempts = 5
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 20.")

while attempts < max_attempts:
    try:
        guess = int(input(f"\nAttempt {attempts + 1}: Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    attempts += 1

    if guess == secret_number:
        print("🎉 Congratulations, you guessed it!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

# If user doesn't guess in 5 tries
if guess != secret_number:
    print("\nGame Over! The correct number was:", secret_number)
