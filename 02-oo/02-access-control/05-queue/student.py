class Queue:
    def __init__(self):
        self.customers = []

    def add(self, item):
        self.customers.append(item)

    def next(self):
        next_person = self.customers[0]
        self.customers.remove(self.customers[0])
        return next_person

    def is_empty(self):
        return len(self.customers) == 0
