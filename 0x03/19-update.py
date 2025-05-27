#!/usr/bin/python
"""a file that update  a dictionary in python"""
cars = {
    "model1": "Toyota",
    "name": "Hummer",
    "year": "2023",
    "price": 30000000,
    "mileage": 150000,
    "engine": "hummer",
}
cars.update({"model1": "Buggati", "name": "BMW", "year": 2024})

print(cars)