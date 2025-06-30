#!/usr/bin/python3


def safe_print_list_integers(my_list, x):
    count = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]))
            count += 1
    except (ValueError, TypeError):
        pass
