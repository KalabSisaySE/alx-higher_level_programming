#!/usr/bin/python3
i = 1
value = 122
while i <= 26:
    if i % 2 != 0:
        print(chr(value), end="")
    else:
        print(chr(value - 32), end="")
    value -= 1
    i += 1
