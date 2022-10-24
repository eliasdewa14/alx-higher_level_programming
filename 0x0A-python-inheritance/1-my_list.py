#!/usr/bin/python3
"""Define a class MyList that inherits from list"""


class MyList(list):
    """Represents a MyList class"""

    def print_sorted(self):
        """Print the sorted list"""

        print(sorted(self))
