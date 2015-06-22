"""
You have two very large binary tree: T1, with millions of nodes,
and T2, with hundreds of nodes. Create an algorithm to decide if T2 is
a subtree of T1.

A tree T2 is a subtree of T1 if there exists a node n in T1 such that
the subtree of n is identical to T2. That is, if you cut off the tree
at node n, the two trees would be identical.

- naive. First use BFS to search for root of T2 in T1. If found, use
BFS to compare the two trees.
"""

def commonroot(T1, T2):
    """
    try to find a node in T1 equals to root of T2
    """
    if T1.data == T2.data:
        return T1

    if T1.left:
        return commonroot(T1.left, T2)

    if T2.right:
        return commonroot(T1.right, T2)

    return None

def comparetree(T1, T2):
    """
    compare two trees
    """
    if T1.left and not T2.left:
        return False
    if T1.right and not T2.right:
        return False

    ret =  T1.data == T2.data
    if T1.left:
        ret &= comparetree(T1.left, T2.left)
    if T1.right:
        ret &= comparetree(T1.right, T2.right)

    return ret


def issubtree(T1, T2):
    """
    check if T2 is subtree of T1
    """
    subtree = commonroot(T1, T2)
    if subtree:
        return comparetree(subtree, T2)
    else:
        return False
