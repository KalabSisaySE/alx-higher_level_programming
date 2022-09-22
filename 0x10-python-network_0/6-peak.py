#!/usr/bin/python3
"""defines the function `find_peak`"""


def find_peak(list_of_integers):
    """finds the peak from `list_of_integers`.

    Args:
        list_of_integers (List): the give unsorted list of integers

    Returns:
        Int: the peak from `list_of_integers`
    """
    if list_of_integers == []:
        return None

    s = len(list_of_integers)
    if s == 1:
        return list_of_integers[0]
    elif s == 2:
        return max(list_of_integers)

    m = int(s / 2)
    peak = list_of_integers[m]
    if peak > list_of_integers[m - 1] and peak > list_of_integers[m + 1]:
        return peak
    elif peak < list_of_integers[m - 1]:
        return find_peak(list_of_integers[:m])
    else:
        return find_peak(list_of_integers[m + 1:])