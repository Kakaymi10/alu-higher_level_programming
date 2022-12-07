#!/usr/bin/python3
"""
Module contains class Rectangle
Inherits from Base;
Inits superclass' id
Contains private width, height, x, y
"""
import base
Base = base.Base


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
