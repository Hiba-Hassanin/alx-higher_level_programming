#!/usr/bin/python3
"""
This module contains the text_indentation function.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be processed.

    Returns:
        None

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> text_indentation("Hello. How are you? Fine, thanks.")
        Hello.$
        $
        How are you?$
        $
        Fine, thanks.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        print(char, end="")
        if char in ('.', '?', ':'):
            print("\n")
