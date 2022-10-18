#!/usr/bin/python3
"""Defines a matrix multiplies 2 matrices by using the module NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """a matrix multiplies 2 matrices.

    Args:
        m_a: The list of first matrix.
        m_b: The list of second matrix.
    """

    return (np.matmul(m_a, m_b))
