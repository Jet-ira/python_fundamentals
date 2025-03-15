#!/usr/bin/python3
"""a program that ask the user to enter their user name and password
if the user name is admin and the password is 12345"
print login successful"
"otherwise invalid credentials"""
username =input("Enter user name ")
password =input("Enter password")
if username == "admin" and password == "12345":
    print("Successsful")
else:
    print("invalid credentials")