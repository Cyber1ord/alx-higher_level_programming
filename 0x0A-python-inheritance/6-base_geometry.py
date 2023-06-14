#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
