"""
Given a sorted (increasing order) array with unique integer
elements, write an algorithm to create a binary search tree with
minimal height.

- start from middle of the array, kind like the reverse process of
binary search. The middle of the array would be the root, the middle
of left half would be left leaf, the middle of the right half would be
right leaf. Repeat the process until all nodes are added.
"""


class Tree():
    def __init__(self, array):
        """
        init a binary search tree from sorted array
        """
        if not array:
            return None

        mid = len(array) / 2
        self.data = array[mid]
        self.left = Tree(array[0:mid])
        self.right = Tree(array[mid + 1:])


def test_init():
    a = [1, 2, 3]
    t = Tree(a)
    assert t.data == 2
    assert t.left.data == 1
    assert t.right.data == 3

    a = [1, 2, 3, 4]
    t = Tree(a)
    assert t.data == 3
    assert t.left.data == 2
    assert t.left.left.data == 1
    assert t.right.data == 4
