#!/usr/bin/env python

"""
Implement an algorithm to delete a node in the middle of a singly
linked list, given only access to that node.

EXAMPLE
Input: the node c from the linked list a->b->c->d->e
Result: nothing is returned, but the new linked list looks like a->b->d->e

- naive. copy data from next node, then delete the next node.
"""


import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'linked-lists'))

from singly_linked_list import Node



def deletemiddle(l, p):
    n = p.next
    p.data = n.data
    p.next = n.next
    del n



def deletemiddle():
    l = List([1, 2, 3])
    deletemiddle(l, l[1])
    assert l.list() == [1, 3]
