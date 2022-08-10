#!/usr/bin/python3
import json
"""defines a function."""


def to_json_string(my_obj):
    """converts a python object to a JSON.

    Args:
        my_obj (obj): python object to be converted.

    Returns:
        str: JSON representation of an object.
    """
    return json.dumps(my_obj)
