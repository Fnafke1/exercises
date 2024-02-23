class LengthConverter:
    def __init__(self):
        self.meter = 0
        self.feet = 0
        self.inch = 0

    @property
    def meter(self):
        return self.__meter

    @meter.setter
    def meter(self, value):
        self.__meter = value
        self.__feet = self.__meter * 3.28084
        self.__inch = self.__meter * 39.3701

    @property
    def feet(self):
        return self.__feet

    @feet.setter
    def feet(self, value):
        self.__feet = value
        self.__meter = self.__feet / 3.28084
        self.__inch = self.__meter * 39.3701

    @property
    def inch(self):
        return self.__inch

    @inch.setter
    def inch(self, value):
        self.__inch = value
        self.__meter = self.__inch / 39.3701
        self.__feet = self.__meter * 3.28084


converter = LengthConverter()
converter.meter = 100
print(converter.feet)
print(converter.inch)
print(converter.meter)
converter.feet = 5
print(converter.inch)
