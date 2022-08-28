#!/usr/bin/python3
"""rectangle.py Module."""
from models.base import Base


class Rectangle(Base):
    """represents a Rectangle inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiates a Rectangle object.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
            x (int): x position of the rectangle.
            y (int): y position of the rectangle.
            id (int): unique id of the object.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter and setter method for the width param."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter and setter method for the height param."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter and setter method for the x param."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter and setter method for the y param."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates area of the rectangle.

        Returns:
            int: area of the object.
        """
        return self.__width * self.__height

    def display(self):
        """prints the rectangle with the `#` character."""
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """string representation of the object.

        Returns:
            str: describes the object's attributes
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__, self.id, self.__x,
            self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """updates the attributes of the object."""
        if args and len(args) > 0:
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}
