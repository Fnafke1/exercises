class CircularBuffer:
    def __init__(self, items):
        self.items = items
        self.list = []

    def add(self, item):
        if len(self.list) < self.items:
            self.list.append(item)
            return
        del self.list[0]
        self.list.append(item)

    def __len__(self):
        return len(self.list)

    def __getitem__(self, indx):
        return self.list[indx]
