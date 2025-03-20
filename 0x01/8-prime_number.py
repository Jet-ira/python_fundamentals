#!/usr/bin/python3
"""a program that print all prime number between 1 to 50
use a nested loop to check if each number has factor"""

# Loop through numbers from 1 to 50

for num in range(1, 51):
    if num > 1:  # 1 is not a prime number
        is_prime = True
        
        # Check if num has any factors other than 1 and itself
        for i in range(2, num):
            if num % i == 0:  # If divisible, it's not prime
                is_prime = False
                break  # Exit loop early
        
        # If no factors found, it's prime
        if is_prime:
            print(num, end=" ")
