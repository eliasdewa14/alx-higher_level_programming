#!/usr/bin/python3
"""Defines the function"""


def is_same_class(obj, a_class):
    """Check the object is exactly an instance of the specified class

    Arg:
        obj: The object
        a_class: The class to check
    Return:
        True if the object is exactly an instance of the specified class; otherwise False
    """
    return isinstance(type(obj), a_class)
