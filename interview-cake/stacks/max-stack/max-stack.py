'''
You want to be able to access the largest element in a stack. ↴

(A stack stores items in a last in, first out queue.)

You've already implemented this Stack class:

  class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push new item to stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]

Use your Stack class to implement a new class MaxStack with a method get_max()
that returns the largest element in the stack. get_max() should not
remove the item.

(get_max() should be O(1).)

Your stacks will contain only integers.

'''


class Stack:
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push new item to stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]


class MaxStack(Stack):
    def __init__(self):
        super().__init__()
        self.max_items = Stack()

    def push(self, item):
        super().push(item)

        if self.get_max() is None or item >= self.get_max():
            self.max_items.push(item)

    def pop(self):
        item = super().pop()

        if item is not None and item == self.get_max():
            self.max_items.pop()

        return item

    def get_max(self):
        if not self.items:
            return None
        return self.max_items.peek()


ms = MaxStack()

ms.push(1)
print(ms.get_max(), 'expected', 1)

ms.push(2)
print(ms.get_max(), 'expected', 2)

ms.push(1)
print(ms.get_max(), 'expected', 2)

ms.push(4)
print(ms.get_max(), 'expected', 4)

ms.pop()
print(ms.get_max(), 'expected', 2)

ms.pop()
print(ms.get_max(), 'expected', 2)

ms.pop()
print(ms.get_max(), 'expected', 1)
