"""
Write a program to sort a stack in ascending order (with biggest
items on top). You may use at most one additional stack to hold items,
but you may not copy the elements into any other data structures (such
as array). The stack supports the following operations: push, pop,
peek, and isEmpty.

- naive. Use s2 as cache. Pop a node A from s1, pop top of s2 back to
s1 until A < top of s2, then push A onto s2. Repeat until all nodes
are poped from s1 to s2. Now s2 is sorted in decending order (biggest
in head). Finally we pop all nodes from s2 back to s1.
"""

def sortstack(stk):
    buf = []
    while stk:
        data = stk.pop()
        while buf and data > buf[-1]:
            stk.append(buf.pop())
        buf.append(data)

    while buf:
        stk.append(buf.pop())


def test_sortstack():
    stk = [3, 1, 2]
    sortstack(stk)
    assert stk == [1, 2, 3]
    stk = [4, 5, 3, 1, 2]
    sortstack(stk)
    assert stk == [1, 2, 3, 4, 5]
