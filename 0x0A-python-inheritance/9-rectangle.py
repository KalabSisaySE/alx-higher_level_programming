#!/usr/bin/python3
"""define a class `Rectangle` that inherits
from imported class `BaseGeometry`."""


class BaseGeometry:
    """represents base geometry."""

    def area(self):
        """ not implemented.
        Raises:
            Exception: `area() is not implemented`.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if `value` is an integer.

        Args:
            name (str): name of the instance.
            value (int): the number to be validated.

        Raises:
            TypeError: if `value` is not an integer.
            ValueError: if `value` is less or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """represent a Rectangle based on BaseGeometry."""

    def __init__(self, width, height):
        """intializes Rectangle object after integer validation."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area of the rectangle."""
        return self.__height * self.__width

    def __str__(self):
        """returns a string representation of Rectangle object."""
        return "[{}] {}/{}".format(
            type(self).__name__,
            self.__width,
            self.__height)
