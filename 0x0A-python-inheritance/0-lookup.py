#!/usr/bin/python3
"""
lookup - returns the list of available attributes and methods of an object
@obj: object
Return: list object
"""
def lookup(obj):
    """ returns all properties and methods of the specified object"""
    return dir(obj)
