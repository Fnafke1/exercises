class Money:
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency

    @property
    def amount(self):
        return self.__amount

    @property
    def currency(self):
        return self.__currency

    def __add__(self, other):
        if self.__currency == other.__currency:
            return Money(self.__amount + other.__amount, self.__currency)
        raise RuntimeError("Mismatched currencies")

    def __sub__(self, other):
        if self.__currency == other.__currency:
            return Money(self.__amount - other.__amount, self.__currency)
        raise RuntimeError("Mismatched currencies")

    def __mul__(self, inte):
        return Money(self.__amount * inte, self.__currency)
