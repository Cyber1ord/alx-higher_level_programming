#!/usr/bin/python3
for alhabet in range(97, 123):
    if ("{:alhabet}".format(alhabet) not in ('q', 'e')):
        print("{:alhabet}".format(alhabet), end="")
