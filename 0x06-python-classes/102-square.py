#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """sets the size of the square and calculates area."""

    def __init__(self, size=0):
        """sets the size of the square.

        Args:
            size(int, optional): size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """get/set the size of the square.

        Raises:
            TypeError: if `value` is not an integer.
            ValueError: if `value` is lessthan zero.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculates the area of the square.

        Returns:
            int: area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
