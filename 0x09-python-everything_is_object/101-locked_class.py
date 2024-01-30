#!/usr/bin/python3

class LockedClass:
    """Prevents dynamically creating new instance attributes, except first_name."""
    __slots__ = ['first_name']
