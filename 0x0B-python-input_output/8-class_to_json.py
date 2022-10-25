#!/usr/bin/python3
"""function that returns the dictionary description with JSON"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""

    return obj.__dict__
