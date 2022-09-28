#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        matrix_element = []
        for j in i:
            matrix_element.append(j**2)
        new_matrix.append(matrix_element)
    return new_matrix
