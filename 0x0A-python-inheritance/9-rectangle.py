#!/usr/bin/python3
"""define a class `Rectangle` that inherits
from imported class `BaseGeometry`."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
