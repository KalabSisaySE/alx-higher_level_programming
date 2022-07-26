#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if type(a_dictionary) == dict:
        key_list = list(sorted(a_dictionary.keys()))
        for i in key_list:
            print(i + ":", a_dictionary.get(i))
