"""
You have a singly-linked list ↴ and want to check if it contains a cycle.

A singly-linked list is built with nodes, where each node has:

node.next—the next node in the list.
node.value—the data held in the node.

For example, if our linked list stores
people in line at the movies, node.value might be the person's name.

For example:

  class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next  = None

A cycle occurs when a node's next points back to a previous node in the list.
The linked list is no longer linear with a beginning and end—instead,
it cycles through a loop of nodes.

Write a function contains_cycle() that takes the first node in a singly-linked
list and returns a boolean indicating whether the list contains a cycle.

"""


class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __hash__(self):
        return id(self)


def contains_cycle(node):
    seen = set()

    while node.next:
        seen.add(node)

        if node.next in seen:
            return True
        else:
            node = node.next

    return False


# no cycle
c = LinkedListNode('c')
b = LinkedListNode('b', c)
a = LinkedListNode('a', b)
print(contains_cycle(a))

# cycle
c = LinkedListNode('c')
b = LinkedListNode('b', c)
a = LinkedListNode('a', b)
c.next = a
print(contains_cycle(a))

# cycle
a = LinkedListNode('a')
a.next = a
print(contains_cycle(a))
