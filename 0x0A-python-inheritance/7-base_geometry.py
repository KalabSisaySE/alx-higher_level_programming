#!/usr/bin/python3
"""defines a class `BaseGeometry`."""


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
