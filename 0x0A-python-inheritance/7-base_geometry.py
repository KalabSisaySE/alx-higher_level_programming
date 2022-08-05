#!/usr/bin/python3
"""defines a class `BaseGeometry`."""


class BaseGeometry:
    """
    Attributes:
        area
    """

    def area(self):
        """
        Raises:
            Exception: `area() is not implemented`.
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """validates if `value` is an integer.
        
        Raises:
            TypeError: if `value` is not an integer.
            ValueError: if `value` is less or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must greater than 0".format(name))
