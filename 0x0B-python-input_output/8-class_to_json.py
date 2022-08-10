#!/usr/bin/python3
"""defines a function."""
import json


def class_to_json(obj):
    """returns dictionary description for JSON serialization of an object.

    Args:
        obj (obj): object to fetched.

    Return
        dict: dictionary decription.
    """
    return json.loads(json.dumps(obj.__dict__))
