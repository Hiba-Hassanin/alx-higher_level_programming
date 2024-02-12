#!/usr/bin/python3
"""
Module containing the Base class
"""

class Base:
    """
    Base class for managing id attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class

        Args:
            id (int): The id value for the instance

        Attributes:
            id (int): The public instance attribute for the id value
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

if __name__ == "__main__":
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
