#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            filtered_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_dict[attr] = getattr(self, attr)
            return filtered_dict
