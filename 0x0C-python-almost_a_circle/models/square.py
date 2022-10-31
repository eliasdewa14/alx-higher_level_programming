#!/usr/bin/python3
""" Define a Rectangle class inherits from Base class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A Square class representation

    Args:
        Rectangle (class): A parent class for Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialization of a square class

        Args:
            size (int): Size of the square
            x (int): The x coordinate of square. Defaults to 0.
            y (int): The y coordinate of square. Defaults to 0.
            id (int): The id of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter method for size

        Returns:
            int: width of a rectangle
        """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter method for size

        Args:
            value (int): value to be set
        """
        self.__width = value
        self.__height = value

    def __str__(self):
        """ a public str method

        Returns:
            str: a format string representation of a square instance
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args,  **kwargs):
        """ a public method with assigned an argument to attributes
        """
        if len(args):
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        elif len(kwargs):
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
    
    def to_dictionary(self):
        """ a public method

        Returns:
            dict: the dictionary representation of a square
        """
        return {'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y}
