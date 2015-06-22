#!/usr/bin/env python

"""
Given a circular linked list, implement an algorithm which returns
the node at the beginning of the loop.

DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next
pointer points to an earlier node, so as to make a loop in the linked
list.

EXAMPLE
Input: A->B->C->D->E->C [the same C as earlier]
Output: C

- naive. Make an hash to store visited nodes, scan every node, if node
  is already in the hash, return it, otherwise append to the array.

Slow/Fast Runner

Slow runner runs at 1 speed, while fast runner at 2 speed. If there is
a loop, they will surly collide. (interesting!)

Suppose the loop start at k-th node, then the collision spot will be k
distance to the start of loop.

Now set another slow runner at the head, move the two slow runner at
speed of 1, then they will collide at start of loop. (WOW)

The slow/fast runner can also be used to find middle of a list.
"""


import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'linked-lists'))

from singly_linked_list import Node, List


def findloop(l):
    i = l.head.next
    j = l.head.next
    while True:
        i = i.next
        i = i.next
        j = j.next
        if i == j:
            break
    # now i, j collide at k-th to start of loop

    i = l.head.next
    while True:
        i = i.next
        j = j.next
        if i == j:
            return i


def test_findloop():
    l = List([0, 1, 2, 3, 4, 5])
    l[5].next = l[2]
    assert findloop(l) == l[2]
