#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
from os.path import exists
from typing import List
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

if __name__ == "__main__":
    arguments = sys.argv[1:]
    if exists('add_item.json'):
        items_list = load_from_json_file('add_item.json')
    else:
        items_list = []

    items_list.extend(arguments)
    save_to_json_file(items_list, 'add_item.json')

