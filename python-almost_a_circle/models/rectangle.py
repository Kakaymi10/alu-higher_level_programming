#!/usr/bin/python3
"""
Module contains class Rectangle
Inherits from Base;
Inits superclass' id
Contains private width, height, x, y
"""
from base import Base


class Rectangle(Base):
    """
    defines class Rectangle; inherits from class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self .y = y

    @property
    def width(self):
        """getter width"""
        return self.__width

    @property
    def height(self):
        """getter height"""
        return self.__height

    @property
    def x(self):
        """getter x"""
        return self.__x

    @property
    def y(self):
        """getter y"""
        return self.__y

    @width.setter
    def width(self, value):
        """setter width"""
        self.__width = value
    
    @height.setter
    def height(self,value):
        """setter height"""
        self.__height = value

    @x.setter
    def x(self, value):
        """setter x"""
        self.__x = value

    @y.setter
    def y(self, value):
        """setter y"""
        self.__y = value
