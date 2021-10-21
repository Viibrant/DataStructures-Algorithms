from mystack import Stack
from myqueue import Queue

# Implement an algorithm to reverse a Queue,
# e.g.
# Queue(1, 2, 3, 4, 5) --> Queue(5, 4, 3, 2, 1)


def reverse_queue(queue: Queue) -> Queue:
    size = queue.length() - 1
    stack = Stack()

    for _ in range(size):
        stack.push(queue.dequeue())

    for _ in range(size):
        queue.enqueue(stack.pop())

    return queue


a = Queue()
for i in range(5):
    a.enqueue(i + 1)

print(a.items)

print(reverse_queue(a).items)
