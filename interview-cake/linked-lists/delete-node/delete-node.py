"""
Delete a node from a singly-linked list, ↴ given only a variable
pointing to that node.


The input could, for example, be the variable b below:

  class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next  = None

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

delete_node(b)

"""
from typing import Any, Union

from dataclasses import dataclass, field

def print_list(node):
    while node:
        print(node.value)

        if node.next:
            print('|')

        node = node.next


@dataclass
class LinkedListNode:
    value: str
    next: Any = None


def delete_node(node):
    if not node.next:
        raise RuntimeError('cannot delete last node')

    node.value = node.next.value
    node.next = node.next.next


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

delete_node(b)

print_list(a)
