#!/usr/bin/python3

end = ""

for num in range(0, 90):
    if num % 10 > num / 10:
        end += "{:02d}, ".format(num) if num != 89 else "{:02d}".format(num)

print(end)
