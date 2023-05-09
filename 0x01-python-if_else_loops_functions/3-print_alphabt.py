#!/usr/bin/python3
for c in range(97, 123):
    if ("{:c}".format(c) not in ('q', 'e')):
        print("{:c}".format(c), end="")
