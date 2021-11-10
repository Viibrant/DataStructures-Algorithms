class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        item = self.items[0]
        self.items = self.items[1:]
        return item

    def peek(self):
        return self.items[0]

    def length(self):
        return len(self.items)
