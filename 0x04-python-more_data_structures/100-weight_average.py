#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        result = 0
        deno = 0
        for tup in my_list:
            mul = 1
            deno += tup[len(tup) - 1]
            for i in tup:
                mul *= i
            result += mul
        return result / deno
    else:
        return 0
