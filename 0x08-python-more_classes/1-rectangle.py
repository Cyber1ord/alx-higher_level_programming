#!/usr/bin/python3
"""Defines a class rectangle"""


class Rectangle:
    """Represents a recatnagle"""

    def __init__(self, width=0, height=0):
        """Method that initializes a rectangle
        Args:
            width(int): the width of the rectangle
            height(int): the height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """private instance attribute taht return the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Methis that define width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Methos that retrun the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method for height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
