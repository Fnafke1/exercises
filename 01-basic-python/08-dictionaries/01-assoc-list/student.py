from typing import Any


class AssocList:
    def __init__(self):
        self.__items = []

    def __setitem__(self, key, value):
        for i in self.__items:
            for k, v in i.items():
                if k == key:
                    i[k] = value

        self.__items.append({key: value})
