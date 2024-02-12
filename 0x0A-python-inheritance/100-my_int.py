#!/usr/bin/python3
"""MyInt inherits from int with inverted == and != operators"""


class MyInt(int):
    """Class representing a rebel MyInt."""

    def __eq__(self, other):
        """Invert the == operator."""

        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the != operator."""

        return super().__eq__(other)
