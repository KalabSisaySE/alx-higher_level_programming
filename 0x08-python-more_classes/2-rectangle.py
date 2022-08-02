#!/usr/bin/python3
"""Defines a class `Rectangle`."""


class Rectangle:
    """creates a rectangle a width and height."""

    def __init__(self, width=0, height=0):
        """sets the `width` and `height` of the rectangle.

        Args:
            width(int, optional): width of the rectangle.
            height(int, optional): height of the rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """int: width of the rectangle.

        Args:
            value(int): width of the rectangle.

        Raises:
            TypeError: if `value` is not an integer.
            ValueError: if `value` is lessthan zero.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """int: height of the rectangle.

        Args:
            value(int): height of the rectangle.

        Raises:
            TypeError: if `value` is not an integer.
            ValueError: if `value` is lessthan zero.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """calclates the area of the rectangle.

        Returns:
            int: area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """calclates the perimeter of the rectangle.

        Returns:
            int: perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
