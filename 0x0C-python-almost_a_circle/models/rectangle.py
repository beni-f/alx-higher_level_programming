#!/usr/bin/python3

from base import Base
class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init - initialization
        Args:
            width - width object
            height - height object
            x - x object
            y - y object
            id - id object inherited
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
    @property
    def getWidth(self):
        """Width getter"""
        return self.__width
    
    def setWidth(self, value):
        """Width setter"""
        self.__width = value

    @property
    def getHeight(self):
        """Height getter"""
        return self.__height
    
    def setWidth(self, value):
        """Height setter"""
        self.__height = value

    @property
    def getx(self):
        """x getter"""
        return self.__x
    
    def setx(self, value):
        """x setter"""
        self.__x = value

    @property
    def gety(self):
        """y getter"""
        return self.__y
    
    def sety(self, value):
        """y setter"""
        self.__y = value
