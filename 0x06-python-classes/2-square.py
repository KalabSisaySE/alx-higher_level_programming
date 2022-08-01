#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """sets the size of the square."""
    def __init__(self, size=0):
        """checks for type and value before setting the `size`.

        Args:
            size(int, optional): size of the square.

        Raises:
            TypeError: if `size` is not an integer.
            ValueError: if `size` is lessthan zero.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
