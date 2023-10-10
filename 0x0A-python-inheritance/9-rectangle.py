#!/usr/bin/python3
"""
9-rectangle.py
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
        Class Rectangle inherited from BaseGeometry
    """
    def __init__(self, width, height):
        """
            inherits method from the base class
            args:
                width - width of the rectangle
                height - height of the rectangle
        """
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height
    def area(self):
        """area- returns area"""
        return self.__width * self.__height
    def __str__(self):
        """str - returns class description"""
        return str("[{}] {}/{}".format("Rectangle", self.__width, self.__height))
