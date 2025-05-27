#!/usr/bin/python
"""a file that delet  a dictionary in python"""
laptop = {
    "brand": "Accer",
    "model": "aspire 5750",
    "price": "100000",
    "year": "2023",
    "color": "ash",
    "seize": "14.8"
}
print(laptop)

del laptop["price"]
#laptop.clear()

print(laptop)