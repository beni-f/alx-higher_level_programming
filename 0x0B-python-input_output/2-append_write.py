#!/usr/bin/python3
"""
2-append_write.py
"""
def append_write(filename="", text=""):
    """
    append_write - appends a string to the end of a text file (UTF8),
                and returns the number of characters written:
    Args:
        filename: name of the file
        text: text to be written
    Return: number of bytes written.
    """
    with open(filename, 'a',  encoding="UTF-8") as f:
        return f.write(text)
