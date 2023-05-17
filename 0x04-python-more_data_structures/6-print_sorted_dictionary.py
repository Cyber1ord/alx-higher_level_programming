#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order_keys = sorted(a_dictionary.keys())
    for key in order_keys:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
