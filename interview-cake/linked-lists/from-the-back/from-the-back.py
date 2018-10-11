"""
You have a linked list ↴ and want to find the kkth to last node.

Write a function kth_to_last_node() that takes an integer kk and the head_node
of a singly-linked list, and returns the kkth to last node in the list.

For example:

  class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None


a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

# Returns the node with value "Devil's Food" (the 2nd to last node)
kth_to_last_node(2, a)

"""
from typing import Any

from dataclasses import dataclass


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


def linked_to_list(node):
    """Convert a linked list to a regular list."""
    list_ = []

    while node:
        list_.append(node)
        node = node.next

    return list_


def kth_to_last_node(position, head):
    return linked_to_list(head)[-position]


a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

print(kth_to_last_node(2, a), "Devil's Food")  # Expected to be "Devil's Food"
