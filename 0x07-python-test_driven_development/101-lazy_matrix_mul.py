#!/usr/bin/python3
"""Matrix multiplication using NumPy"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    try:
        result = np.dot(m_a, m_b)
        return result.tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
