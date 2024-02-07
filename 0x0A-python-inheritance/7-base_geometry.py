#!/usr/bin/python3
"""Class BaseGeometry with public instance: area and integer_validator"""


class BaseGeometry:
    """Empty class representing base geometry."""

    def area(self):
        """Calculate the area."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value."""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
