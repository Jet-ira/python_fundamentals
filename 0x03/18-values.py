#!/usr/bin/python
"""a file that displays all the values of a dictionary in python"""
cars = {
    "model1": "Toyota",
    "name": "Hummer",
    "year": "2023",
    "price": 30000000,
    "mileage": 150000,
    "engine": "hummer",
}
print(cars.values())

print(cars.items())

for key, value in cars.items():
    print(f"{key}: {value}")