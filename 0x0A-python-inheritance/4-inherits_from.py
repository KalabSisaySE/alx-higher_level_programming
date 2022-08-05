#!/usr/bin/python3
"""defines the function `inherits_from`."""


def inherits_from(obj, a_class):
    """returns true if  if the `obj` is an instance of a
    class that inherited (directly or indirectly) from `a_class`."""
    return issubclass(type(obj), a_class) and type(obj) != a_class
