#!/usr/bin/python3
"""Module base"""
import json


class Base:
    """Defines a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Method that assigns public instance id attribute

        Args:
            id(int): Integer value to manage id

        Return:
            Always nothing

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
