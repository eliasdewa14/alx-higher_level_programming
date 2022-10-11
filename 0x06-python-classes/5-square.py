#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""


    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square"""

        self.__size = size

    @property
    def size(self):
        """Get/set the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError('size must be an integer')
        if (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value


    def area(self):
        """Return the current area of the square"""

        return (self.__size ** 2)


    def my_print(self):
        """Print the square with # character"""
        if (self.size != 0):
            for i in range(self.size):
                print("#" * self.size)
        else:
            print()
