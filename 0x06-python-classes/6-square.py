#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """sets the size of the square and calculates area."""

    def __init__(self, size=0, position=(0, 0)):
        """sets the size of the square.

        Args:
            size(int, optional): size of the square.
        """
        self.__size = size
        self.__position = position

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
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        cond_1 = type(value) == tuple
        cond_2 = len(value) == 2
        cond_3 = type(value[0]) == int and type(value[1]) == int
        cond_4 = value[0] >= 0 and value[1] >= 0
        if cond_1 and cond_2 and cond_3 and cond_4:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """calculates the area of the square.

        Returns:
            int: area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for a in range(self.__position[0]):
                    print(" ", end="")
                for b in range(self.__size):
                    print("#", end="")
                print()
