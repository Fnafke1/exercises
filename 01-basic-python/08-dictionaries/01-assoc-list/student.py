from typing import Any


class AssocList:
    def __init__(self):
        self.__items = []

    def __setitem__(self, key, value):