#!/usr/bin/python3
"""
10-square.py
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Represents a square.
    Inherits from Rectangle.
    """
    def __init__(self, size):
        """
        init - Initializes a Square.
        Args:
            size: size of the square
        """
        self.integer_validator("Size", size)
        super().__init__(size, size)
        self.__size = size
    def area(self):
        """
        area - returns area of a square
        """
        return self.__size ** 2
