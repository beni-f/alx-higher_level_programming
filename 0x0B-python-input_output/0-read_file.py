#!/usr/bin/python3
"""
0-read_file.py
"""
def read_file(filename=""):
    """
        filename - the name of the file to be read
    """
    with open(filename, 'r') as f:
        """
            Opens and reads the file
        """
        f.read()
