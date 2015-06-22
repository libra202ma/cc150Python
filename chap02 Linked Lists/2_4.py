#!/usr/bin/env python

"""
Write code to partition a linked list around a value x, such that
all nodes less than x come before all nodes greater or equal to x.

Q: keep order of node occurring in the original list?

- naive. Create new list, append every node at end (> x) or start (< x).
- create two arrays, one for smaller, one for bigger. merge the list
  when complete.
"""


def partition(l, x):
    smaller = []
    larger = []
    for i in l:
        if i < x:
            smaller.append(i)
        else:
            larger.append(i)

    return smaller + larger


def test_partition():
    l = [7, 2]
    assert partition(l, 5) == [2, 7]
