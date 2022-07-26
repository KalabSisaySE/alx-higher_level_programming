#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = list()
    for x in a_dictionary:
        if a_dictionary[x] == value:
            key_list.append(x)
    if len(key_list) > 0:
        for i in key_list:
            del a_dictionary[i]
    return a_dictionary
