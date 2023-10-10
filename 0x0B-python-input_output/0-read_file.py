#!/usr/bin/python3
"""Defines a function that reads a text file"""


def read_file(filename=""):
    """ This function prints utf8 contents to stdout. """
    with open("tests\my_file_0.txt", r, encoding="uf-8") as f:
        for f in lines:
            print(f.read())
    f.close()
