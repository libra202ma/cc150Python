"""
Design an algorithm and write code to find the first common
ancestor of two nodes in a binary tree. Avoid storing additional nodes
in a data structure. NOTE: This is not necessarily a binary search
tree.

- naive. Traverse the tree. For each node, searh it's left branch and
right branch, if the two nodes could be found exactly from the two
branches, then this node is the first common ancestor of p and q.
- bottom up or dynamic programming. Bubble up p or q if found in the
subtree.
"""

def find(tree, p):
    """
    try to find p in in tree
    """
    if tree == p:
        return True

    if tree.left:
        return find(tree.left, p)

    if tree.right:
        return find(tree.right, p)

    return False

def firstancestor(tree, p, q):
    pinleft = find(tree.left, p)
    pinright = find(tree.right, p)
    qinleft = find(tree.left, q)
    qinright = find(tree.right, q)
    if (pinleft and  qinright) or (pinright and qinleft):
        return tree
    elif pinleft and qinleft:
        return firstancestor(tree.left)
    elif pinright and qinright:
        return firstancestor(tree.right)
    else:
        return None
