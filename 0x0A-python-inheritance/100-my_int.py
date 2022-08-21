#!/usr/bin/python3
"""
the `100-my_int` module.
defines a class `MyInt`
"""


class MyInt(int):
    """representes integers based on int data type."""

    def __init__(self, num):
        """instantiates MyInt object."""
        self.__num = num
        super().__init__()

    def __eq__(self, __x: object) -> bool:
        """defines the ==  comparison to MyInt."""
        return self.__num != __x

    def __ne__(self, __x: object) -> bool:
        """defines the != comparision to MyInt."""
        return self.__num == __x
