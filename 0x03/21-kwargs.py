#!/usr/bin/python
"""a module that explain key word arguement"""
kwargs = {
    "name": "Bala Aliyu",
    "age": "23",
    "state": "Adamawa",
    "country": "Nigeria"
}

def print_dictionary(**params):
    print(params)

print_dictionary(**kwargs)