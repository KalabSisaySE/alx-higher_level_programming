#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file."""
import os
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    filename = "add_item.json"

    if not os.path.exists(filename):
        save_to_json_file([], filename)

    arg_list = []

    for i in range(len(argv)):
        arg_list.append(argv[i])
    if len(arg_list) > 0:
        arg_list.remove("./7-add_item.py")

    if type(load_from_json_file(filename)) == list:
        file_list = load_from_json_file(filename)
        file_list.extend(arg_list)
        save_to_json_file(file_list, filename)
    else:
        save_to_json_file(arg_list, filename)
