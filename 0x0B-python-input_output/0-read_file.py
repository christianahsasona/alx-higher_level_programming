#!/usr/bin/python3
"""Defines a function that reads a text file"""


def read_file(filename=""):
    """ This function prints utf8 contents to stdout.
    Args:
    Filename (str): The name of the file to read from """
    with open(filename, encoding="uf-8") as f:
        print(f.read(), end="")
