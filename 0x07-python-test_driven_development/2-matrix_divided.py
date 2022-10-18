#!/usr/bin/python3
"""Divides all elements of a matrix by div"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div

    Args:
        matrix: the matrix of number
        div: the divisor
    Return:
        a new matrix
    """
    if type(matrix) is not list:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    list_size = 0
    for i in matrix:
        if type(i) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError(
                    'matrix must be a matrix (list of lists) of integers/floats')
        if list_size == 0:
            list_size = len(i)
        elif list_size != len(i):
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = []
    new_list = []
    for i in matrix:
        for j in i:
            new_list.append(round(j/div, 2))
        new_matrix.append(new_list)
        new_list = []

    return new_matrix
