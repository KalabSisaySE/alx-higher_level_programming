#!/usr/bin/python3
"""9-student Module."""
import json


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dictionary representation of the class instance.

        Returns:
            dict: representation of the instance.
        """
        return json.loads(json.dumps(self.__dict__))
