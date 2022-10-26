#!/usr/bin/python3
"""Define a function that adds a new attribute to an object if possible
"""


def add_attribute(obj, name, value):
    """adding a new attribute to an object

    Args:
        obj (any): the object to add
        name (str): name of attribute
        value (any): value of attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
