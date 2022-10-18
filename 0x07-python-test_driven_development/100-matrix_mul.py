#!/usr/bin/python3
"""Multiplies two matrices."""


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices

    Args:
        m_a: matrix list
        m_b: matrix list
    Return:
        a matrix
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for i in m_a:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")

    a_row_len = []
    for i in m_a:
        a_row_len.append(len(i))
    if not all(i == a_row_len[0] for i in a_row_len):
        raise TypeError("each row of m_a must be of the same size")
    b_row_len = []
    for i in m_b:
        b_row_len.append(len(i))
    if not all(i == b_row_len[0] for i in b_row_len):
        raise TypeError("each row of m_b must be of the same size")

    a_col = 0
    for i in m_a[0]:
        a_col += 1
    b_row = 0
    for i in m_b:
        b_row += 1

    if a_col != b_row:
        raise ValueError("m_a and m_b can't be multiplied")

    res = [[0 for i in range(len(m_b[0]))] for j in range(len(m_a[0]))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                res[i][j] += m_a[i][k] * m_b[k][j]

    return res
