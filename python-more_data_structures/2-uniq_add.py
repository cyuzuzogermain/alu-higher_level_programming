#!/usr/bin/python3


def uniq_add(my_list=[]):
    unique_items = []
    total = 0
    for num in my_list:
        if num not in unique_items:
            unique_items.append(num)
            total += num
    return total
