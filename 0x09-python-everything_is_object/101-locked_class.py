#!/usr/bin/python3
""" Defines a locked class. """

class LockedClass:
    """ 
    Prevents the user from creating new instance a
    attributes except if the new instance attribute is
    called first_name
    """

    __slots__ = ["first_name"]
