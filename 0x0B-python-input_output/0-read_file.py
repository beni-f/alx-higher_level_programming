#!/usr/bin/python3
"""
0-read_file.py
"""
def read_file(filename=""):
    """
        filename - the name of the file to be read
    """
    with open(filename, 'r', encoding="UTF-8") as f:
        """
            Opens and reads the file
        """
        for line in f:
            print(line, end="")
