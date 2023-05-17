#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for no_c in my_string:
        if no_c != "c" and no_c != "C":
            new_string += no_c
    return new_string
