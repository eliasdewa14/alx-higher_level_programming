#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Define a Rectangle class that inherits from BaseGeometry class"""


class Rectangle(BaseGeometry):
    """Represent a rectangle class"""

    def __init__(self, width, height):
        """Initialization of a rectangle

        Args:
            width: width of a rectangle
            height: height of a rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of a rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
