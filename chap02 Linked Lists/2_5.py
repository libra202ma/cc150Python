#!/usr/bin/env python

"""
You have two numbers represented by a linked list, where each node
contains a single digit. The digits are stored in reverse order, such
that the 1's digit is at the head of the list. Write a function that
adds the two numbers and returns the sum as a linked list.

EXAMPLE
Input: (7->1->6) + (5->9->2). That is, 617 + 295
Output: 2->1->9. That is, 912.

- naive.

FOLLOWUP
Suppose the digits are stored in forward order. Repeat the above problem.

EXAMPLE
Input: (6->1->7) + (2->9->5). That is, 617 + 295.
Output: 9->1->2. That is, 912.

- reverse the list before adding.
"""


def add(l1, l2):
    res = []
    i = 0
    carry = 0
    for i in range(min(len(l1), len(l2))):
        imres = l1[i] + l2[i] + carry
        carry = imres / 10
        imres = imres % 10
        res.append(imres)
    return res + l1[i+1:] + l2[i+2:]


def test_add():
    l1 = [7, 1, 6]
    l2 = [5, 9, 2]
    assert add(l1, l2) == [2, 1, 9]



def addreverse(l1, l2):
    l1.reverse()
    l2.reverse()
    res = add(l1, l2)
    res.reverse()
    return res

def test_addreverse():
    l1 = [6, 1, 7]
    l2 = [2, 9, 5]
    assert addreverse(l1, l2) == [9, 1, 2]
