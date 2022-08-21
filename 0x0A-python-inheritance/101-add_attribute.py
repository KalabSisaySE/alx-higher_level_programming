#!/usr/bin/python3
"""
the `101-add_attribute` module.
defines a function `add_attribute`.
"""


def add_attribute(obj, name, value):
    """adds attribute to `cls`.

    Args:
        obj (obj): the object to add the attribute to.
        name (str): name of the attribute.
        value (any): the value of the attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
