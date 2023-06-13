#!/usr/bin/python3
"""A file appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
        char_no: numbers of character appended
    Returns:
        char_no.
    """
    with open(filename, "a", encoding="utf-8") as f:
        char_no = f.write(text)
        return char_no
