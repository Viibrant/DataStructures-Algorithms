class CircularQueue:
    def __init__(self, size):
        self.index = 0
        self.items = [i for i in range(size)]

    def enqueue(self, item):
        if self.length() == self.index:
            raise RuntimeError("SizeError: Queue is full")
        self.items[self.index] = item
        self.index += 1

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def length(self):
        return len(self.items)


x = CircularQueue(2)
x.enqueue(4)
x.enqueue(5)
print(x.items)
