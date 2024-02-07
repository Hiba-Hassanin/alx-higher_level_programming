#!/usr/bin/python3
"""Function to return dictionary description with simple data structure
for JSON serialization of an object.
"""


def class_to_json(obj):
    """Return dictionary description with simple data for JSON."""

    return obj.__dict__
