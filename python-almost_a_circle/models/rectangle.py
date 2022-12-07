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
    Inherited Attributes:
        id
    Class Attributes:
        __width          __height
        __x              __y
    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
        update(self, *args, **kwargs)
        width(self)      width(self, value)
        height(self)     height(self, value)
        x(self)          x(self, value)
        y(self)          y(self, value)
        area(self)       display(self)
        __str__          to_dictionary(self)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self .y = y
