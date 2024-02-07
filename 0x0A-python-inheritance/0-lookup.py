#!/usr/bin/python3
"""This module provides a function to return the list of available attributes and methods of an object."""

def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Parameters:
        obj: Any object whose attributes and methods are to be looked up.

    Returns:
        list: A list containing the names of attributes and methods.
    """
    return dir(obj)

