#!/usr/bin/python3
"""Defines a class `Rectangle`."""


class Rectangle:
    """creates a rectangle a width and height."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """sets the `width` and `height` of the rectangle.

        Args:
            width(int, optional): width of the rectangle.
            height(int, optional): height of the rectangle.
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

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
        """calculates the area of the rectangle.

        Returns:
            int: area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """calculates the perimeter of the rectangle.

        Returns:
            int: perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """string representation of the rectangle with the `#` characther.

        Returns:
            str: a rectangle made with the `#` characther.
        """
        rectangle = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    rectangle += str(self.print_symbol)
                if i + 1 != self.__height:
                    rectangle += "\n"
        return rectangle

    def __repr__(self):
        """returns a string that reproduces the object.

        Returns:
            str: a string that reproduces the object.
        """
        rep = "Rectangle({}, {})".format(self.__width, self.__height)
        return rep

    def __del__(self):
        """deletes the object."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compare the area two rectangles.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.

        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.

        Returns:
            Rectangle: the rectangle with the bigger area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size):
        """creates a new instance of the `Rectangle` class.

        Args:
            size(int): the size of the new Rectangle.

        Returns:
            Rectangle: new instance of a `Rectangle` with
            width and height equal to `size`.
        """
        return cls(size, size)
