queue = __import__("3-queue")

# Implement a stack using a queue


class Stack:
    def __init__(self):
        self.items = queue.Queue()

    def pop(self):
        original = self.items
        subset = queue.Queue()
        for _ in range(self.length() - 1):
            subset.enqueue(self.items.dequeue())

        subset = subset.peek()
        self.items = original
        return subset

    def push(self, item):
        self.items.enqueue(item)

    def length(self):
        return self.items.length()


x = Stack()

for i in range(4):
    x.push(i)


print(x.items.items)
print(x.pop())
print(x.items.items)
