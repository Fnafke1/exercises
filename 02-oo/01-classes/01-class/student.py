class Wall:
    def __init__(self):
        self.__armor = 10
        self.__height = 5

    @property
    def armor(self):
        return self.__armor

    @property
    def height(self):
        return self.__height
