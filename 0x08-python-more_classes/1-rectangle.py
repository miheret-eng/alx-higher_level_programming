#!/usr/bin/python3
"""
A rectangle with width and height.
"""


class Rectangle:
    """
    Rectangle functions and data
    """

    def __init__(self, height=0, width=0):
        """ Instantiation
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """ Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

        @property
        def width(self):
            """Getter for width
            """
            return self.__width

        @width.setter
        def width(self, value):
            """ Setter for width
            """
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
