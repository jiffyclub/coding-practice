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


def linked_list_len(node):
    count = 0

    while node:
        count += 1
        node = node.next

    return count


def kth_to_last_node2(position, head):
    list_len = linked_list_len(head)
    ordinal_position = list_len - position

    if ordinal_position < 0:
        raise ValueError(f'position {position} not in list')

    index = 0
    node = head

    while node:
        if index == ordinal_position:
            return node

        index += 1
        node = node.next
    else:
        raise RuntimeError('position {position} not found')


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
print(kth_to_last_node2(2, a), "Devil's Food")  # Expected to be "Devil's Food"
