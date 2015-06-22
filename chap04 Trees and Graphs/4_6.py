"""
Write an algorithm to find the 'next' node (i.e., in-order
successor) of a given node in a binary search tree. You may assume
that each node has a link to its parent.

- If node n has right subtree, the n's next in-order node is leftmost
  node of the right subtree. If node n does not have right subtree, we
  have to go up until we found a node who is the left subtree of its
  parent, this parent is n's in-order next node. (WOW)
"""


def next(n):
    if n.right:
        # find leftmost of right subtree
        n = n.right
        while n.left:
            n = n.left
        return n

    while n:
        if n == n.parent.left:
            return n.parent
        else:
            n = n.parent

    return None
