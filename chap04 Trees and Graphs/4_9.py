"""
You are given a binary tree in which each node contains a
value. Design an algorithm to print all paths which sum to a given
value. The path does not need to start or end at the root or a leaf.

- Traversal the whole tree. For each node, we pass the path that goes
from root to this node, then we check if we could add this paths to
num using a for loop which starts from this node and going up until
hit root. If sum to the given value, just print the path. Using this
approach, we reduce the tree traversing overhead.
"""


def sumto(tree, value, path=[]):
    path.append(tree.data)
    sum = 0
    for i in range(len(path)):
        cur = -1 * (i + 1)
        sum += path[cur]
        if sum == value:
            print path[cur:]

    if tree.left:
        sumto(tree.left, value, path)
    if tree.right:
        sumto(tree.right, value, path)
