#!/usr/bin/python3
"""Sorting list"""
class MyList(list):
    """Mylist child of list"""
    def print_sorted(self):
        """
        print_sorted - prints the list in ascending sort
        """
        print(sorted(self))
