class Stack(object):
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def length(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return not self.items
