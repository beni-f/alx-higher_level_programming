#!/usr/bin/python3
""" Create a class called square """
class Square:
    """ define function __init__ """
    def __init__(self, size=0):
        self.__size = size
    def size(self):
        """ returns size """
        return self.__size
    def size(self, value):
        if type(value) != int:
            """ raise an error"""
            raise TypeError("size must be an integer")
        elif value < 0:
            """ raise an error """
            raise ValueError("size must be >= 0")
        else:
            """ set value to the private size member """
            self.__size = value
        
    def area(self):
        """ Return area of a Square """
        return self.__size ** 2
    