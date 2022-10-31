#!/usr/bin/python3
""" Define a Rectangle class inherits from Base class
"""
from models.base import Base


class Rectangle(Base):
    """ A Rectangle class representation

    Args:
        Base (class): A parent class for Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of a rectangle class

        Args:
            width (int): width of a rectangle
            height (int): height of a rectangle
            x (int): the x coordinate. Defaults to 0.
            y (int): the y coordinate. Defaults to 0.
            id (int): id value. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter function for width

        Returns:
            int: width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter function for width

        Args:
            value (int): value to be set

        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')

        self.__width = value

    @property
    def height(self):
        """ Getter function for height

        Returns:
            int: height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter function for height

        Args:
            value (int): value to be set

        Raises:
            TypeError: height must be an integer
            ValueError: height must be > 0
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @property
    def x(self):
        """ Getter function for x

        Returns:
            int: x coordinate of rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter function for x

        Args:
            value (int): value to be set

        Raises:
            TypeError: x must be an integer
            ValueError: x must be >= 0
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @property
    def y(self):
        """ Getter function for y

        Returns:
            int: y coordinate of rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter function for y

        Args:
            value (int): value to be set

        Raises:
            TypeError: y must be an integer
            ValueError: y must be >= 0
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')

        self.__y = value

    def area(self):
        """ public area method

        Returns:
            int: return the area of the rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """ a public display method

        Print:
            the Rectangle instance with the character #
        """
        for y in range(self.__y):
            print("")
        for h in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ a public str method

        Returns:
            str: a format string representation of a rectangle instance
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.x,
                                                                 self.y,
                                                                 self.width,
                                                                 self.height)

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
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        elif len(kwargs):
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ a public method

        Returns:
            dict: the dictionary representation of a Rectangle
        """
        return {'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width}
