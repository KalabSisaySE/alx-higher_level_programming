#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    duplicates = list()
    for i in my_list:
        if my_list.count(i) == 1:
            result += i
        else:
            if duplicates.count(i) == 0:
                duplicates.append(i)
    for i in duplicates:
        result += i
    return result
