#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """sets the size of a square."""
    def __init__(self, size=0):
        """sets the size of the square.

        Args:
            size(int, optional): size of the square.
        """
        self.__size = size
