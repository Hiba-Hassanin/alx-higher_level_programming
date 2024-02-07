#!/usr/bin/python3
"""
Class MyList inherits from list.
"""

class MyList(list):
    """
    A class that inherits from list and provides additional functionality.
    """

    def print_sorted(self):
        """
        Print the list sorted in ascending order.
        """
        print(sorted(self))
