#!/usr/bin/python3
class MagicString:
    n = 0

    @classmethod
    def magic_string(cls):
        cls.n += 1
        return "BestSchool, " * (cls.n - 1) + "BestSchool"
