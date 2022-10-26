#!/usr/bin/python3
"""Defines the function"""


def inherits_from(obj, a_class):
    """Check the object is an instance of a class that inherited from class

    Arg:
        obj: The object
        a_class: The object class to check
    Return:
        True if the object is an instance of a class; otherwise False
    """
    return (isinstance(obj, a_class) and type(obj) != a_class)
