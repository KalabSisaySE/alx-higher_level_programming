#!/usr/bin/python3
"""Defines a class MagicClass that genertes the given bytecode."""
import math


class MagicClass:
    """ calculates the circumference and area of a circle."""

    def __init__(self, radius=0):
        """sets the `radius` of the square.

        Args:
            radius(int, optional): the radius of the square
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ calculates the area of the circle.

        Returns:
            int: the area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ calculates the cicumference of the circle.

        Returns:
            int: the cicumference of the circle.
        """
        return 2 * math.pi * self.__radius
