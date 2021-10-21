from mystack import Stack

# Implement a queue using a stack


class Queue:
    def __init__(self):
        self.items = Stack()

    def enqueue(self, item):
        self.items.push(item)

    def dequeue(self):
        subset = Stack()
        for _ in range(self.length(), 1, -1):
            subset.push(self.items.pop())

        new = subset
        head = self.items.pop()

        for _ in range(new.length()):
            self.items.push(new.pop())

        return head

    def length(self):
        return self.items.length()
