#!/usr/bin/python3
"""Module to print a square based on a given size.
"""


def print_square(size):
    """prints a square with `#` characther based on the given size.

    Args:
        size(int): the size of the square

    Raises:
        TypeError: if size is not an integer.
            if size is float and lessthan zero.
        ValueError: if size is less than zero
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
