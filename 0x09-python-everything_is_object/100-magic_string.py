#!/usr/bin/python3
def magic_string():
    return ", ".join(["BestSchool"] * magic_string.call_count)

magic_string.call_count = 0
