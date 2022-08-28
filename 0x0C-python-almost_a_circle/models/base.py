#!/usr/bin/python3
"""base.py Module."""
import json
import os
import csv
import turtle


class Base:
    """the base class for all the rest of the classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """intializes a base object.

        Args:
            id (int): sets the id to the object if provided
            otherwise it is set automatically
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of `list_dictionaries`.

        Args:
            list_dictionaries (list): list of dictionaries.

        Returns:
            str: JSON string representation.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of `list_objs`.

        Args:
            list_objs (list): list of instances who inherits of `Base`.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write(Base.to_json_string([]))
            else:
                obj_dict_list = []
                for obj in list_objs:
                    obj_dict_list.append(obj.to_dictionary())
                f.write(Base.to_json_string(obj_dict_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of JSON string representation.

        Args:
            json_string (str): string representing a list of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes set based on `dictionary`.

        Args:
            **dictionary (dict): used to set the instance's attributes.
        """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances."""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            dict_list = Base.from_json_string(f.read())
            li = []
            for di in dict_list:
                li.append(cls.create(**di))
            return li

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves list of instances to a csv file.

        Args:
            list_objs (list): list of instances.
        """
        filename = cls.__name__ + ".csv"

        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter='|', quotechar=' ')
            csv_writer.writerow(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"

        with open(filename, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter='|', quotechar=' ')
            obj_list = []
            for li in csv_reader:
                for di in li:
                    obj_list.append(di)
            return obj_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """"""
