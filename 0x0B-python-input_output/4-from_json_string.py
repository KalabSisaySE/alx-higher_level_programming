#!/usr/bin/python3
"""defines a function."""
import json


def from_json_string(my_str):
    """returns an object represented by a JSON string.

    Args:
        my_str (str): JSON string representation of an object.

    Returns:
        object: python data structure object.
    """
    return json.loads(my_str)
