#!/usr/bin/python3
"""a program that print all leap years from 1900 to 2100
a year is a leap year if is divisible by 4 
AND it is not divisible by 100 OR it is divisible by 400"""

# Loop through years from 1900 to 2100
for year in range(1900, 2101):
    # Check leap year conditions
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        print(year, end=" ")
