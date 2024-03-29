#!/usr/bin/python3
"""Class Square inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class representing a square."""

    def __init__(self, size):
        """Initialize square with size."""

        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """String representation of Square."""

        return "[Square] {}/{}".format(self.__size, self.__size)
