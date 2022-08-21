#!/usr/bin/python3
"""
the `10-square` module.
defines a class `Square`.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents a square based on the `Rectangle` class."""

    def __init__(self, size):
        """instantiates a square object.

        Args:
            size (int): size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculates the area of the square.

        Returns:
            int: area of the square.
        """
        return super().area()
