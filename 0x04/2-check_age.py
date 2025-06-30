#!/usr/bin/python
"""Write a program that prompts the user to enter their age and 
checks if they are eligible to vote (age >= 18).
Print "You can vote!" if true, otherwise print "Sorry, you're
 not eligible to vote yet."""

age = int(input("Enter you age"))
if age >= 18:
    print("you are eligable to vote")

else:
    print("not eligible to vote")


