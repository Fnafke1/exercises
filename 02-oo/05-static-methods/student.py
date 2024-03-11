class Duration:
    def __init__(self, *, seconds, minutes, hours):
        self.__seconds = seconds
        self.__minutes = minutes
        self.__hours = hours

    @property
    def seconds(self):
        return self.__seconds

    @property
    def minutes(self):
        return self.__minutes

    @property
    def hours(self):
        return self.__hours

    @staticmethod
    def from_seconds(amount):
        return Duration(seconds=amount, minutes=amount/60, hours=amount/3600)

    @staticmethod
    def from_minutes(amount):
        return Duration(seconds=amount*60, minutes=amount, hours=amount/60)

    @staticmethod
    def from_hours(amount):
        return Duration(seconds=amount*3600, minutes=amount*60, hours=amount)
