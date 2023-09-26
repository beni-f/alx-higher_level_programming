#!/usr/bin/python3
""" Create a class called square """
class Square:
    """ define function __init__ """
    def __init__(self, size=0):
        self.__size = size
    """ getter """
    @property
    def size(self):
        return self.__size
    """ setter """
    @size.setter
    def size(self, value):
        if type(value) is not int:
            """ raise error """
            raise TypeError("size must be an integer")
        elif value < 0:
            """ raise error """
            raise ValueError("size must be >= 0")
        else:
            """ set size to value """
            self.__size = value
    def area(self):
        """ return the area """
        return self.__size ** 2
