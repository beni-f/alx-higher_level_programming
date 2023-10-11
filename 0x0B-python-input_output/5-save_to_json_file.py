#!/usr/bin/python3
"""
5-save_to_json_file.py
"""
import json
def save_to_json_file(my_obj, filename):
    """
        save_to_json_file - writes an Object to a text file,
                        using a JSON representation:
    Args:
        my_obj: object
        filename: name of the file
    Return:
    """
    with open(filename, 'w', encoding="UTF-8") as f:
        f.write(json.dumps(my_obj))
