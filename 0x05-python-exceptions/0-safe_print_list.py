#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    size = 0
    for i in my_list:
        size += 1
    index = 0 
    while index < x:
        try:
            print(my_list[index], end="")
            index += 1
        except IndexError:
            break
    print()
    return index
