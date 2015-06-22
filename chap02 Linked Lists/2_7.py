#!/usr/bin/env python

"""
Implement a function to check if a linked list is a palindrome.

Q: singly? doubly?

- reverse. create a second list l2, for every node the l1, insert it
in the head of l2.  Then compare l1 and l2. (Actually we just did is
actually make the list to be a doubly linked list.)
- reverse the first half by using a stack. If the size of list is not
known, fast/slow runner could be used to push half part into stack.
"""


import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'linked-lists'))

from singly_linked_list import Node, List


def ispalindrome(l):
    rev = List()
    n = l.head.next
    while n != l.tail:
        rev.insert(0, n.data)
        n = n.next

    n1 = l.head.next
    n2 = rev.head.next
    while n1 != l.tail:
        if n1.data != n2.data:
            return False

    return True

def test_ispalindrome():
    l = List([1, 2, 3, 2, 1])
    assert ispalindrome(l) == True
    l = List([1, 2, 3])
    assert ispalindrome(l) == False
