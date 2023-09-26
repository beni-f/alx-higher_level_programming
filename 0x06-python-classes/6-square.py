#!/usr/bin/python3
""" Create a class called square """
class Square:
    """ define function __init__ """
    def __init__(self, size=0, position=(0,0)):
        self.__size = size
        self.__position = position

    
    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size
    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): size of a side of the square
        Returns:
            None
        """
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
    """ print square """
    def my_print(self):
        if (self.__size == 0):
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                 print("_".join([" " for k in range(self.__position[0])]), end="")
            print("_".join(["#" for z in range(self.__size)]))

    @property
    def position(self):
        """getter of __position
        Returns:
            The position of the square in 2D space
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position
        Args:
            value (tuple): position of the square in 2D space
        Returns:
            None
        """
        if len(self.__position) != 2:
            """ raise error """
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value