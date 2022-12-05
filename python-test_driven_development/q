#!/usr/bin/python3
""" Write a function that prints a square with the charcter # """


def print_square(size):
    """ Raising exceptions """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end='')
            print()
