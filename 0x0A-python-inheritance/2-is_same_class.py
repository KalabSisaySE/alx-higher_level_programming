#!/usr/bin/python3
"""defines a function is_same_class."""


def is_same_class(obj, a_class):
    """returns true if `obj` is exactly an instance of `a_class`"""
    if a_class.__name__ == "object":
        return
    return type(obj) == a_class
