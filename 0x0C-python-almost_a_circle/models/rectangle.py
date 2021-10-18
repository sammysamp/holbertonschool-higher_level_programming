#!/usr/bin/python3
"""class rectangle"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize method"""
        self.__width = width
        self.__height = height
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        self.__width = new_width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        if type(new_x) is not int:
            raise TypeError("x must be and integer")
        if new_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        if type(new_y) is not int:
            raise TypeError("y must be and integer")
        if new_y < 0:
            raise ValueError("y must be >= 0")

        self.__y = new_y

    def area(self):
        """area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """that prints in stdout the Rectangle"""
        for y in range(0, self.y):
            print()
        for j in range(0, self.height):
            for x in range(0, self.x):
                print(" ", end="")
            for i in range(0, self.width):
                print("#", end="")
            print()

    def __str__(self):
        """overriding the __str__ method"""
        return ("[rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ public method def update that assigns an
        argument to each attribute
        -**kwargs must be skipped if *args exists and is not empty
        -Each key in this dictionary represents an attribute to the instance
        """
        args_list = ["id", "width", "height", "x", "y"]
        if args and args[0] is not None:
            if len(args) > len(args_list):
                max_len = len(args_list)
            else:
                max_len = len(args)
            for i in range(max_len):
                setattr(self, args_list[i], args[i])
        elif kwargs is not None:
            for key in kwargs:
                if hasattr(self, key) is True:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        return ({'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width})
