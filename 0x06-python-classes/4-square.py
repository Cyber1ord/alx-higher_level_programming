#!/usr/bin/python3
"""Class Square defines a square"""



class Square:
    """this class define a square.

    """
    def __init__(self, size=0):
        """This method defines a square.

        Args:
            size (int): this define the size of the square

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ this method retrives size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """this methis sets the size of the square

        Args:
            size (int): this defines the size of the square.
                This size is validated with if/elif.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """int: Return ares of square"""
        return self.__size ** 2
