#!/usr/bin/python3
"""
the `101-lazy_matrix_mul` module.
defines one function `lazy_matrix_mul`.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """mutliples two matrices `m_a` and `m_b`.

    Args:
        m_a (list): the first matrix.
        m_b (list): the second matrix.

    Returns:
        List: the product of `m_a` and `m_b`.
    """
    return numpy.matmul(m_a, m_b)
