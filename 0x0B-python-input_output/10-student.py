#!/usr/bin/python3
"""10-student module."""
import json


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary representation of the class instance.

        Args:
            attrs (list): used to filter the dictionary.

        Returns:
            dict: representation of the instance.
        """
        is_valid = False
        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    is_valid = False
                    break
            is_valid = True
        if is_valid:
            new_dict = self.__dict__.copy()
            for key in self.__dict__:
                if attrs.count(key) == 0:
                    new_dict.pop(key)
            return new_dict
        else:
            return self.__dict__
