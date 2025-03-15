#!/usr/bin/python3
"""a program that takes a persons age as input
if the age is less than 13 print you are a child
if between 13 and 19 you are a teeneger 
otherwise print you are an adult"""
age =int(input("Enter your age "))
if age < 13:
    print("you are a child.")
elif 13 <= age <= 19:
    print("you are a teeneger. ")
else:
    print("you are an adult")