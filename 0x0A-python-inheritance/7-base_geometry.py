#!/usr/bin/python3
"""Raises and exception"""
class BaseGeometry:
    """raise exception with a message"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
         """
        Args:
            name: The name of the parameter.
            value: The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        