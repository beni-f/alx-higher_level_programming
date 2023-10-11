#!/usr/bin/python3
"""
8-class_to_json.py
"""
import json
def class_to_json(obj):
    """
    class_to_json - returns the dictionary description for JSON
    arg:
        obj - class object
    """
    return json.dumps(obj.__dict__)
