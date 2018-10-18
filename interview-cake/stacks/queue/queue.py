"""
Implement a queue ↴ with 2 stacks. ↴ Your queue should have an enqueue and a
dequeue method and it should be "first in first out" (FIFO).

(A stack stores items in a last in, first out queue.)

Optimize for the time cost of mm calls on your queue. These can be any mix of
enqueue and dequeue calls.

Assume you already have a stack implementation and it gives O(1)O(1) time
push and pop.

"""

from collections import deque


class Stack:
    def __init__(self):
        self.items = deque()

    def __len__(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


class Queue:
    def __init__(self):
        self.dequeue_stack = Stack()
        self.enqueue_stack = Stack()

    def enqueue(self, item):
        # need to transfer items from the dequeue stack to
        # the enqueue stack (reversing them in the process)
        while self.dequeue_stack:
            self.enqueue_stack.push(self.dequeue_stack.pop())

        self.enqueue_stack.push(item)

    def dequeue(self):
        if not self.dequeue_stack and not self.enqueue_stack:
            # no items in the queue
            raise RuntimeError('Queue is empty')

        # need to transfer items from the enqueue stack to
        # the dequeue stack (reversing them in the process)
        while self.enqueue_stack:
            self.dequeue_stack.push(self.enqueue_stack.pop())

        return self.dequeue_stack.pop()


Q = Queue()

Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)

print(Q.dequeue(), 'expected', 1)
print(Q.dequeue(), 'expected', 2)
print(Q.dequeue(), 'expected', 3)

Q.enqueue(1)

print(Q.dequeue(), 'expected', 1)

Q.enqueue(2)
Q.enqueue(3)

print(Q.dequeue(), 'expected', 2)
print(Q.dequeue(), 'expected', 3)
