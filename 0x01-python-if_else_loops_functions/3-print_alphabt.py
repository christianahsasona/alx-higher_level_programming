#!/usr/bin/python
for char in range(26):
    if char != 4 and char != 16:
        print("{:s}".format(char(char + ord("a"))), end="")
