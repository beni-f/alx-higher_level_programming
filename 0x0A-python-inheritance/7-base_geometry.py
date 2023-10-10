#!/usr/bin/python3
"""Raises and exception"""
class BaseGeometry:
    """raise exception with a message"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """checks value and type errors"""
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
        self.name = name
        self.value = value
