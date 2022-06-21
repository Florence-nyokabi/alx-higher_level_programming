#!/usr/bin/python3
"""Square class"""


class Square:
    """__(int): size of a side"""
    def __init__(self, size):
        """initializes a square

        Args:
            size(int):size of a side

        Return: None
        """
         if type(size) is not int:
             raise TypeError("size must be an integer")
         else if:
             if size < 0:
                 raise ValueError("size must be >= 0")
             else:
                 self.__size = size

