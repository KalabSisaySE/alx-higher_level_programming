#!/usr/bin/python3
"""define a class `Rectangle` that inherits
from imported class `BaseGeometry`."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """intializes Rectangle object after integer validation."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
