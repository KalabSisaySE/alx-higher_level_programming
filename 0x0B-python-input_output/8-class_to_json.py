#!/usr/bin/python3
"""defines a function."""


def class_to_json(obj):
    """returns dictionary description for JSON serialization of an object.

    Args:
        obj (obj): object to fetched.

    Return
        dict: dictionary decription.
    """
    return obj.__dict__
