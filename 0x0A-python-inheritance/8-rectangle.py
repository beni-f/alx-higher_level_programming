#!/usr/bin/python3
"""
8-rectangle.py
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
