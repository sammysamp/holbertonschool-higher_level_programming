#!/usr/bin/python3
"""In this module we define a class for a rectangle object"""


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


def eval_rec(str_value, value):
    """Checks if the given object is an instance of the class Rectangle or
    raises an exception
    """
    if type(value) is not Rectangle:
        raise TypeError(str_value + " must be an instance of Rectangle")
    else:
        return value


class Rectangle:
    """A class which defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

    def __str__(self):
        """A printable representation of the class Rectangle"""
        if self.width != 0 and self.height != 0:
            symbol = str(self.print_symbol)
            lines = ((symbol * self.width) + "\n") * \
                (self.height - 1)
            last = (symbol * self.width)
            return lines + last
        return ""

    def __repr__(self):
        """A string representation of the class Rectangle ready to recreate
        a new object instance of this class"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """This method does something when the object is deleted"""
        print("Bye rectangle...")
        if Rectangle.number_of_instances != 0:
            Rectangle.number_of_instances -= 1

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

    def area(self):
        """Returns the current rectangle area.
        Args: None
        Returns:
            The area of a rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """Returns the current rectangle perimeter.
        Args: None
        Returns:
            The perimeter of a rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the area of two rectangles
        Args:
            rect_1: A rectangle whose area will be compared
            rect_2: Another rectangle whose area will be compared
        Returns:
            rect_1 if its area is bigger or equal than rect_2, or
            rect_2 otherwise
        """
        r1 = eval_rec("rect_1", rect_1)
        r2 = eval_rec("rect_2", rect_2)
        if r1.area() >= r2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        sq = Rectangle(size, size)
        return sq
