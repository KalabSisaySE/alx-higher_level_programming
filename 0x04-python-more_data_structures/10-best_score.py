#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) == dict:
        biggest = list(a_dictionary.values())[0]
        for x in a_dictionary:
            if a_dictionary[x] > biggest:
                biggest = a_dictionary[x]
        return x
    else:
        return None
