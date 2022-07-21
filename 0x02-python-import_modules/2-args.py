#!/usr/bin/python3
from sys import argv
sign = "."
if len(argv) == 2:
    sign = ":"
    word = "argument"
else:
    sign = ":"
    word = "arguments"
if __name__ == "__main__":
    print("{} {}{}".format(len(argv) - 1, word, sign))
    if len(argv) > 1:
        i = 1
        while i < len(argv):
            print("{}: {}".format(i, argv[i]))
            i += 1
