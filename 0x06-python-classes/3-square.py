#!/usr/bin/python3
""" Create a class called square """
class Square:
    """ define function __init__ """
    def __init__(self, size=0):
        if type(size) != int:
            """ raise an error"""
            raise TypeError("size must be an integer")
        elif size < 0:
            """ raise an error """
            raise ValueError("size must be >= 0")
        else:
            """ initalize size into a private member """
            self.__size = size
        
    def area(self):
        return self.__size ** 2
