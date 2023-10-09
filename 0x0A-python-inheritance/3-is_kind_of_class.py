#!/usr/bin/python3
"""Checks if the object is an instance of a class that inherited from the specific class
"""
def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class - returns True the object is an instance of a class that inherited from the specific class
    False otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
