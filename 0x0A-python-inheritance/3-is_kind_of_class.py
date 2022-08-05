#!/usr/bin/python3
"""defines the function is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """returns true if `obj` is an instance of `a_class`
    or instance of a class that `a_class` inherited from."""
    return isinstance(obj, a_class)
