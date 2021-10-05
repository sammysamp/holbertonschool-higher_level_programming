#!/usr/bin/python3
"""In this module we define a class for a square object"""


def eval_value(str_value, value):
    """Checks if the given value is a positive integer or raises an exception
    Args:
    value (int): The value must be a positive integer
    Returns:
    int: the checked integer
    """
    if type(value) is not int:
        raise TypeError(str_value + " must be an integer")
    elif value < 0:
        raise ValueError(str_value + " must be >= 0")
    else:
        return value


class Rectangle:
    """A class which defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes an object for a rectangle class.
        Args:
            width (int): The width of the rectangle. Can be 0 if width is not
                specified.
            height (int): The height of the rectangle. Can be 0 if height is
                not specified.
        """
        self.__width = eval_value("width", width)
        self.__height = eval_value("height", height)

    @property
    def width(self):
        """obj:`int`: returns o changes the value of the attribute`width`"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = eval_value("width", value)

    @property
    def height(self):
        """obj:`int`: returns o changes the value of the attribute`height`"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = eval_value("height", value)
