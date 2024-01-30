#!/usr/bin/python3

def magic_string(iterations=[0]):
    iterations[0] += 1
    return "BestSchool" + ", BestSchool" * (iterations[0] - 1) + "\n"
