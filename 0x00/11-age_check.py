#!/usr/bin/python
"""a programm that ask the user to enter their age 
if the age is greater than or equalto 18 
print you are eligible to vote
otherwise you are not eligible"""
age =int(input("Enter your age: "))
if age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")