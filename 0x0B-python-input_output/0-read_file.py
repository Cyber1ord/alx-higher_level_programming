#!/usr/bin/python3
"""A text file-reading function."""


def read_file(filename=""):
    """Print a UTF8 text content file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
