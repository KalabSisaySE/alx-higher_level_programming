#!/usr/bin/python3
"""defines a function."""


def write_file(filename="", text=""):
    """writes a text to a file.

    Args:
        filename (str): name of the file to write to.
        text (str): the text to be written to the file.

    Returns:
        int: number of characthers written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
