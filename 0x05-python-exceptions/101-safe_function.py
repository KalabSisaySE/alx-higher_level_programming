#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = None
    try:
        return fct(*args)
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return result
