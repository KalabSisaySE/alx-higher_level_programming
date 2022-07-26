#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    size = 0
    for i in my_list:
        size += 1
    index = 0
    nums_of_print = 0
    while index < x:
        try:
            print("{:d}".format(my_list[index]), end="")
            index += 1
            nums_of_print += 1
        except (TypeError, ValueError):
            index += 1
    print()
    return nums_of_print
