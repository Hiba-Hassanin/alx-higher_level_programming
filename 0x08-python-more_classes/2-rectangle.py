#!/usr/bin/python3
"""
Defines a class Rectangle with private instance attributes width and height,
and public instance methods for area and perimeter calculation.
"""


class Rectangle:
    """
    Defines a rectangle with private instance attributes width and height,
    and public instance methods for area and perimeter calculation.
    """

    def __init__(self, width=0, height=0):
        """The Rectangle instance."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """The width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width with error checking."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height with error checking."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
