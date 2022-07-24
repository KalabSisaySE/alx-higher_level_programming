#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        num = 0
        for j in i:
            if num == 2:
                print("{:d}".format(j), end="")
            else:
                print("{:d} ".format(j), end="")
                num += 1
        print()
