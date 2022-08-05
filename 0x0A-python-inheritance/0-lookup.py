#!/usr/bin/python3
"""defines a function lookup."""


def lookup(obj):
    """returns a list of attributes and methods of an object.

    Args:
        obj(object): the object to be looked up.

    Returns:
        list: list of attributes and methods of the `obj`.
    """
    return dir(obj)
