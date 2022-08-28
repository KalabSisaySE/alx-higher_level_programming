#!/usr/bin/python3
"""square.py Module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a square inherits from rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """instantiates a Square object

        Args:
            size (int): size of the square.
            x (int): x position of the square.
            y (int): y position of the square.
            id (int): unique id of the object.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id,
                                             self.x,
                                             self.y,
                                             self.width)

    @property
    def size(self):
        """getter and setter method for the size param."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates attributes of the object."""
        if args and len(args) > 0:
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        "returns the dictionary representation of the object"
        return {"id": self.id,
                "size": self.width,
                "x": self.x, "y": self.y}
