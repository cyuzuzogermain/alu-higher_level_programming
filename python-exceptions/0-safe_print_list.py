#!/usr/bin/python3


def safe_print_list(my_list, x):
    counter = x
    while counter > 0:
        try:
            for i in my_list:
                print (i, end="")
        except:
            print ("Error")
