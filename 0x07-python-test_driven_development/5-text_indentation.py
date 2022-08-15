#!/usr/bin/python3
"""Module to print a formatted text.
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of \
        these characters: ., ? and :.

    Args:
        text(str): the tezt to be printed.

    Raises:
        TypeError: if `text` is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i <= len(text) - 1:
        print(text[i], end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            next_char = text[i + 1]
            print()
            print()
            if next_char == " ":
                i = i + 1
        i = i + 1
