#!/usr/bin/python3
"""a program that ask the user of any food of their choice and store it on the list"""
fooditems = []

for _ in range(1, 10):
    food = input("Enter any food item: ")
    fooditems.append(food)

print(fooditems)
