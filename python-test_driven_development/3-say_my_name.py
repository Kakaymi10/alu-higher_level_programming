#!/usr/bin/python3
"""Write a fuction that prints  My name '1sr name' '2nd name'"""


def say_my_name(first_name, last_name=""):
    """Raising exception if param is not string"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is " + first_name + " " + last_name)
