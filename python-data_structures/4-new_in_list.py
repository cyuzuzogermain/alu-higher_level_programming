#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        new_list[idx] = element
        print(my_list)
        print(new_list)
