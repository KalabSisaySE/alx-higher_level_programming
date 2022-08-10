#!/usr/bin/python3
"""12-pascal_tirangle Module."""


def pascal_triangle(n):
    """returns a list of lists representing the pascal's tirangle of size `n`.

    Args:
        n (int): size of the triangle.

    Returns:
        list: returns a list of list of integers.
    """
    my_list = []
    if n <= 0:
        return []
    full_list = []
    for i in range(n):
        if i == 0:
            li = [1]
        elif i == 1:
            li = [1, 1]
        elif i >= 2:
            li = [1]
            i = 0
            last_list = full_list[len(full_list) - 1]
            for elm in range(len(last_list) - 1):
                li.append(last_list[i] + last_list[i + 1])
                i += 1
            li.append(1)
        full_list.append(li)
    return full_list
