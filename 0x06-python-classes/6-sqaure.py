#!/usr/bin/python3
""" Create a class called square """
class Square:
    """ define function __init__ """
    def __init__(self, size=0, position=(0,0)):
        self.__size = size
        self.__position = position
    """ getter """
    @property
    def position(self):
        return self.__position
    @property
    def size(self):
        return self.__size
    """ setter """
    @position.setter
    def position(self, value):
        if len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
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
    def my_print(self):
        if (self.__size == 0):
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                 print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(["#" for z in range(self.__size)]))
    
my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")