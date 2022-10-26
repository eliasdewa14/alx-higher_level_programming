#!/usr/bin/python3
"""Define MyInt class inherits from int"""


class MyInt(int):
    """Invert the operators == and !=
    """

    def __eq__(self, value):
        """change equal (==) operator with not equal to (!=)
        """
        return self.real != value

    def __ne__(self, value):
        """change not equal to (!=) operator with equal (==)
        """
        return self.real == value
