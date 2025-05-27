#!/usr/bin/python3
"""upack a tuble containing three values name, age, city
and print a formatted sentence using those value"""
personal_Data = ("Elim", 15, "Califonia")
# unpack the tuple
name, age, city = personal_Data
# formatted sentence
print(f"My name is {name}, i'm {age} years old, from the city of {city}.")