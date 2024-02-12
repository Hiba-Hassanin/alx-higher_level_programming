#!/usr/bin/python3
"""Class Rectangle inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""

        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle."""

        return self.__width * self.__height

    def __str__(self):
        """String representation of Rectangle."""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
