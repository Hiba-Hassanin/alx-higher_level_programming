#!/usr/bin/python3
"""Class Student that defines a student."""


class Student:
    """Class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize student with first name, last name, and age."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance."""

        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Replace all attributes based on JSON dictionary."""

        for key, value in json.items():
            setattr(self, key, value)
