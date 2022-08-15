#!/usr/bin/python3
"""
0-add_integer Module.

defines one function `add_integer`.
"""


def add_integer(a, b=98):
    """adds to integers and returns the result.

    Args:
        a (int) = the first integer to be added.
        b (int, optional) = the second integer to be added.

    Raises:
        TypeError: if `a` and `b` are neither integer nor floats.

    Returns:
        int: the sum of the two integers.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
