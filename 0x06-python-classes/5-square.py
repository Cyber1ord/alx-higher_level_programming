#!/usr/bin/python3
""" Class square"""


class Square:
    """ Class Square that define a square"""
    def __init__(self, size=0):
        self._size = 0
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self._size = value

    def area(self):
        return self._size ** 2

    def my_print(self):
        """Prints in STDOUT the square with character #"""
        if self._size != 0:
            for _ in range(self._size):
                print('#' * self._size)
        else:
            print()
