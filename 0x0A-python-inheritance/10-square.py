#!/usr/bin/python3
"""Define a Square class that inherits from Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square class"""

    def __init__(self, size):
        """Initialization of a square

        Args:
            size: size of a square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
