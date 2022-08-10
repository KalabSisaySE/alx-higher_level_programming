#!/usr/bin/python3
"""0-read_file Module."""


def read_file(filename=""):
    """reads a file.

    Args:
        filename (str): name of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
