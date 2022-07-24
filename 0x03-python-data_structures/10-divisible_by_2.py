#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_list = []
    for i in my_list:
        if i % 2 == 0:
            value = True
        else:
            value = False
        bool_list.append(value)
    return bool_list
