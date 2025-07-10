#!/usr/bin/python3

"""
A class that inherits from list
"""


class MyList(List):
    def __init__(self, List):
        super().__init__(self, List)
        self.list = List
    def print_sorted(self):
        print self.list.sort()
