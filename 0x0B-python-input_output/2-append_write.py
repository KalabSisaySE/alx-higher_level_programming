#!/usr/bin/python3
"""defines a function."""


def append_write(filename="", text=""):
    """appends a string to the end of a text file.

    Args:
        filename (str): name of the text file.
        text (str): the string to be appended to the file.

    Returns:
        int: number of characthers written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
