#!/usr/bin/python3
"""
    Checks if the object is exactly an instance of the specified class
"""
def is_same_class(obj, a_class):
    """
        is_same_class: returns True if the object matches instance of specified class
    """
    if (isinstance(obj, a_class) and (a_class != object)):
        return True
    else:
        return False
