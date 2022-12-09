#!/usr/bin/python3
"""Module contains class Rectangle
Inherits from Base;
Inits superclass' id
Contains private width, height"""
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Width of this rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        """Beg of task3 validte attributes"""
        if type(value) is not (int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        """End of task3"""
        self.__width = value

    @property
    def height(self):
        '''Height of this rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        """Beg of task3 validte attributes"""
        if type(value) is not (int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        """End of task 3"""
        self.__height = value

    @property
    def x(self):
        '''x of this rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
         """Beg of task3 validte attributes"""
         if type(value) is not (int):
             raise TypeError("x must be an integer")
         if value < 0:
             raise ValueError("x must be >= 0")
         """End of task 3"""
         self.__x = value

    @property
    def y(self):
        '''y of this rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
         """Beg of task3 validte attributes"""
         if type(value) is not (int):
             raise TypeError("y must be an integer")
         if value < 0:
             raise ValueError("y must be >= 0")
         """End of task 3"""
         self.__y = value

    """task 4 Area first"""
    def area(self):
        """returning the area of the rectangle"""
        return self.width * self.height

    """task 5"""
    def display(self):
        """return #"""
        print("\n" * self.__y +
              "\n".join(" " * self.__x + "#" * self.__width
                        for i in range(self.__height)))

    def __str__(self):
        """Prints [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[" + self.__class__.__name__ + " " + "(" + str(self.id) + ") " + str(self.__x) + "/" + str(self.__y) + "-" + str(self.__width) + "/" + str(self.__height)
