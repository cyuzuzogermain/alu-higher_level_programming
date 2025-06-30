#!/usr/bin/python3


def safe_print_integer(value):
    try:
        if isdigit(value):
            print("{:d}.format()", value)
            return True
    except IndexError:
        return False
