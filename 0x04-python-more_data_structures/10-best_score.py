#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) == dict:
        list_value = list(a_dictionary.values())
        if len(list_value) > 0:
            biggest = list_value[0]
            for x in a_dictionary:
                if a_dictionary[x] > biggest:
                    biggest = a_dictionary[x]
                    scorer = x
            return scorer
        else:
            return None
    else:
        return None
