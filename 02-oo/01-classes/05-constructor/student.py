class Wall:
    def __init__(self, depth, height, width):
        self.__depth = depth
        self.__height = height
        self.__width = width
        self.volume = width * height * depth

        @property
        def depth(self):
            return self.__depth

        @property
        def height(self):
            return self.__height

        @property
        def width(self):
            return self.__width
