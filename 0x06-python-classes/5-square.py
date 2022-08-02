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
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculates the area of the square.

        Returns:
            int: area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """prints the square using `#` symbol."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
