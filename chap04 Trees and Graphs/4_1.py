"""
Implement a function to check if a binary tree is balanced. For
the purpose of this question, a balanced tree is defined to be a tree
such that the heights of the two subtrees of any node never differ by
more than one.

- search. Depth-first Search to find depth of tree. Compare the
counting results of the two branches. Quickly return the result if
found one subtree is unbalanced.
"""


class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def countdepth(self):
        leftdepth = 0
        rightdepth = 0
        if self.left:
            leftdepth = self.left.countdepth()
            if leftdepth == -1:
                return -1
        if self.right:
            rightdepth = self.right.countdepth()
            if rightdepth == -1:
                return -1

        if abs(leftdepth - rightdepth) <= 1:
            return max(leftdepth, rightdepth) + 1
        else:
            return -1

    def isbalanced(self):
        if self.countdepth() == -1:
            return False
        else:
            return True


def test_countdepth():
    t = Tree(8)
    t.left = Tree(3)
    assert t.countdepth() == 2
    t.right = Tree(4)
    assert t.countdepth() == 2
    t.left.left = Tree(1)
    t.left.right = Tree(2)
    assert t.countdepth() == 3
    t.right.right = Tree(5)
    assert t.countdepth() == 3

def test_isbalanced():
    t = Tree(8)
    t.left = Tree(3)
    t.right = Tree(4)
    t.left.left = Tree(1)
    t.left.right = Tree(2)
    t.right.right = Tree(5)
    assert t.isbalanced() == True
    t.right.right.left = Tree(9)
    t.right.right.right = Tree(6)
    t.right.right.right.right = Tree(7)
    assert t.isbalanced() == False
