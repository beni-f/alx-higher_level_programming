#!/usr/bin/python3
"""
   checks if the object is an instance of a class that inherited (directly or indirectly) from the specified class 
"""
def inherits_from(obj, a_class):
    """
        inherits_from - returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class
        False otherwise
    """
    if isinstance(obj, a_class) and obj != object:
        return True
    else:
        return False
