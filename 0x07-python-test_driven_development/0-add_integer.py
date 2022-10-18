#!/usr/bin/python3
"""Add two integer numbers"""


def add_integer(a, b=98):
    """Add two integers number

    Args:
        a: first integer
        b: second integer
    Return:
        The sum of a and b
    """
    if type(a) not in [int, float] or a is None:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float] or b is None:
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
