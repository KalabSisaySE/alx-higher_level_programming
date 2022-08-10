#!/usr/bin/python3
import json
"""defines a function."""


def load_from_json_file(filename):
    """creates an Object from a JSON file.

    Args:
        filename (str): name of the file to load from.

    Returns:
        Object
    """
    with open(filename, "r") as f:
        return json.loads(f.read())
