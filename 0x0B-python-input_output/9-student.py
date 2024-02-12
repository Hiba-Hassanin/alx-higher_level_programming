#!/usr/bin/python3
"""Class Student that defines a student."""


class Student:
    """Class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize student with first name,last name,and age."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve dictionary representation of a Student instance."""

        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
