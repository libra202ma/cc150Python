#!/usr/bin/env python

"""
Implement an algorithm to find the k-th to last element of a
singly linked list.

Q: size known?

- naive, find the n-k element from start.

not known

- use two pointers, p1 and p2. p1 is placed at the head, p2 is placed
k steps away from p1. move p1 and p2 in the same pace. when p2 heat
the end, p1 is k-th element to the end.
"""


import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'linked-lists'))

from singly_linked_list import Node, List


def k2last(l, k):
    j = l.head.next
    cnt = 0
    while cnt <= k:
        if j == l.tail:
            return None
        j = j.next
        cnt += 1
    # now j points at k-th node
    i = l.head.next
    while j != l.tail:
        j = j.next
        i = i.next

    return i


def test_k2last():
    l = List([1, 2, 3, 4, 5])
    assert k2last(l, 1).data == 4
    assert k2last(l, 0).data == 5
