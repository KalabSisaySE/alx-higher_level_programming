#!/usr/bin/python3
"""
the 100-matrix_mul module.

defines one function `matrix_mul`.
"""


def matrix_mul(m_a, m_b):
    """multiplies two matrices, `m_a` and `m_b`.

    Args:
        m_a (list): the first matrix.
        m_b (list): the second matrix.

    Raises:
        TypeError: if `m_a`  or `m_b` is not a list.
            if `m_a` or `m_b` is not a list of lists.
            if one of those list of lists is not an integer or float.
            if `m_a` or `m_b` is not a rectangle (same size rows).
        ValueError: if `m_a` or `m_b` is empty.
            if `m_a` and `m_b` can't be multiplied.
    """
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    else:
        if m_a == [] or m_a == [[]]:
            raise ValueError("m_a can't be empty")

        for li in m_a:
            if type(li) is not list:
                raise TypeError('m_a must be a list of lists')
            err1 = 'm_a should contain only integers or floats'
            for elm in li:
                if type(elm) is not float and type(elm) is not int:
                    raise TypeError(err1)

        ma_rows = [len(row) for row in m_a]
        if len(ma_rows) != ma_rows.count(ma_rows[0]):
            raise TypeError('each row of m_a must be of the same size')

    if type(m_b) is not list:
        raise TypeError('m_b must be a list')
    else:
        if m_b == [] or m_b == [[]]:
            raise ValueError("m_b can't be empty")

        for li in m_b:
            if type(li) is not list:
                raise TypeError('m_b must be a list of lists')
            err2 = 'm_b should contain only integers or floats'
            for elm in li:
                if type(elm) is not float and type(elm) is not int:
                    raise TypeError(err2)

        mb_rows = [len(row) for row in m_b]
        if len(mb_rows) != mb_rows.count(mb_rows[0]):
            raise TypeError('each row of m_b must be of the same size')

    # inorder to multiply m_a with m_b
    # number of column of m_a should equal the number of rows of m_b

    if len(m_b) != len(m_a[0]):
        raise ValueError("m_a and m_b can't be multiplied")
    else:
        # transpose m_b
        mb_tsp = [[row[i] for row in m_b] for i in range(len(m_b[0]))]

        new_matrix = []
        row = []

        for row_a in m_a:
            for row_b in mb_tsp:
                i = 0
                res = 0
                while i < len(row_a):
                    res += row_a[i] * row_b[i]
                    i += 1
                row.append(res)
            new_matrix.append(row)
            row = []

        return new_matrix
