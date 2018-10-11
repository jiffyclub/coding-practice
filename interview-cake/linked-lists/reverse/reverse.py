"""
Hooray! It's opposite day. Linked lists go the opposite way today.

Write a function for reversing a linked list. ↴ Do it in place. ↴

Your function will have one input: the head of the list.

Your function should return the new head of the list.

Here's a sample linked list node class:

  class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None

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


def reverse(head):
    current_node = head.next
    prev_node = head
    head.next = None

    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    return prev_node


c = LinkedListNode('c')
b = LinkedListNode('b', c)
a = LinkedListNode('a', b)
print_list(a)
print_list(reverse(a))

print()

d = LinkedListNode('d')
print_list(d)
print_list(reverse(d))
