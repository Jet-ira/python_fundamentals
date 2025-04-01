#!/usr/bin/python3
"""a function named factoria n that takes an intiger n as input 
use recoursion to compute and return the factoria of n
result factoria 5 print result # 120"""
def factorial(n):
    """Recursively calculates the factorial of a given number n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)