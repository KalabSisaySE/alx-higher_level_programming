#!/usr/bin/python3
"""defines a class MyList."""


class MyList(list):
    """inherits from list."""

    def print_sorted(self):
        """prints the sorted list."""
        new_list = self.copy()
        new_list.sort()
        print(new_list)
