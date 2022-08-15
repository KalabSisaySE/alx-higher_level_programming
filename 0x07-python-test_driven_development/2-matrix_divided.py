#!/usr/bin/python3
"""Module to divde each element of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """divdes all the elements of a given matrix by the div.

    Args:
        matrix(list): the given matrix two dimensional list.
        div(int): the divisor integer.

    Raises:
        TypeError: if `matrix` is not a list of list of integers or floats.
            if each row of the `matrix` is not of the same size.
            if `div` is not an integer or a float.
        ZeroDivisionError: if `div` is zero.

    Returns:
        list: a new matrix.
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) \
            of integers/floats")
    else:
        for i in matrix:
            if type(i) is not list:
                raise TypeError("matrix must be a matrix (list of lists) \
                     of integers/floats")
            for j in i:
                if type(j) is not int and type(j) is not float:
                    raise TypeError("matrix must be a matrix (list of lists) \
                         of integers/floats")
    list_of_row = [len(row) for row in matrix]
    number_of_occurence = list_of_row.count(list_of_row[0])
    for i in matrix:
        if len(list_of_row) != number_of_occurence:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for i in matrix:
        new_matrix.append([round((j / div), 2) for j in i])
    return new_matrix
