#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """sets the size of the square and calculates area."""

    def __init__(self, size=0):
        """sets the size of the square.

        Args:
            size(int, optional): size of the square.
        """
        self.size = size

    @property
    def size(self):
        """int: size of the square.

        Raises:
            TypeError: if `value` is not an integer.
            ValueError: if `value` is lessthan zero.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int or type(value) != float:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculates the area of the square.

        Returns:
            int: area of the square.
        """
        return self.__size ** 2
