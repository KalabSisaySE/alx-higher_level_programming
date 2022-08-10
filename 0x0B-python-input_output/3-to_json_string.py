#!/usr/bin/python3
"""defines a function."""
import json


def to_json_string(my_obj):
    """converts a python object to a JSON.

    Args:
        my_obj (obj): python object to be converted.

    Returns:
        str: JSON representation of an object.
    """
    return json.dumps(my_obj)
