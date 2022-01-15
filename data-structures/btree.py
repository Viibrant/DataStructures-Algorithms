class BTree:
    def __init__(self, d=None):
        self.l = None
        self.d = d
        self.r = None

    def insert(self, n, side="l"):
        if side == "l":
            if not self.l:
                self.l = BTree(n)
            else:
                self.l.insert(n, side="l")
        elif side == "r":
            if not self.r:
                self.r = BTree(n)
            else:
                self.r.insert(n, side="r")

    def search(self, n) -> bool:
        if n == self.d:
            return True
        if self.l:
            self.l.search(n)
        if self.r:
            self.r.search(n)
        return False

    def output(self):
        if self.l:
            self.l.output()
        print(self.d)
        if self.r:
            self.r.output()


tree = BTree()
nums = [2, 3, 4, 5]

# random chance of left or right
import random

for n in nums:
    if random.randint(1, 2) == 1:
        tree.insert(n, side="l")
    else:
        tree.insert(n, side="r")

tree.output()
print(tree.search(5))
