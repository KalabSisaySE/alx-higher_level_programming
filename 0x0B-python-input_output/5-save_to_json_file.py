#!/usr/bin/python3
import json
"""defines a function."""


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (obj): python object to be serialized.
        filename (str): name of the file to save to.
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
