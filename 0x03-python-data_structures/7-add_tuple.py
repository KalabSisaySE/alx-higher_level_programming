#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    def add_sec_elm(my_tuple=()):
        if len(my_tuple) < 2:
            if len(my_tuple) == 1: 
                new_tuple = (my_tuple[0], 0)
                return new_tuple
            elif len(my_tuple) == 0: 
                new_tuple = (0, 0)
                return new_tuple
        else:
            return my_tuple
    new_tuple_a = add_sec_elm(tuple_a)
    new_tuple_b = add_sec_elm(tuple_b)
    add_tuple = (new_tuple_a[0] + new_tuple_b[0]), (new_tuple_a[1] + new_tuple_b[1])
    return add_tuple
