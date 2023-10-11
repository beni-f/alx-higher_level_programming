#!/usr/bin/python3
"""
8-class_to_json.py
"""

def class_to_json(obj):
    """
    class_to_json - returns the dictionary description for JSON
    arg:
        obj - class object
    """
    return obj.__dict__
