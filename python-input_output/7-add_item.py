#!/usr/bin/python3
"""
Adds all arguments to a Python list, and then save them to a file
"""


from sys import argv
""" modules """
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

"""
a function
"""
file = "add_item.json"

try:
    """ function """
    arg_list = load_from_json_file(f)
except FileNotFoundError:
    """ function """
    arg_list = list()

for arg in argv[1:]:
    """ function """
    arg_list.append(arg)

save_to_json_file(arg_list, f)
