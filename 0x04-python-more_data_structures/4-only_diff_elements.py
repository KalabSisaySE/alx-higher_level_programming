#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    my_list = list(set_1)
    my_list.extend(set_2)
    new_set = set()
    for i in my_list:
        if my_list.count(i) == 1:
            new_set.add(i)
    return new_set
