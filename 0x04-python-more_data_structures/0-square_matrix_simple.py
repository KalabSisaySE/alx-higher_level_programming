#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_list = list()
    for row in matrix:
        my_list.append(list(map((lambda n: n ** 2), row)))
    return my_list
