#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        length = 0
        first = None
    else:
        length = len(sentence)
        first = sentence[0]
    my_tuple = (length, first)
    return my_tuple
