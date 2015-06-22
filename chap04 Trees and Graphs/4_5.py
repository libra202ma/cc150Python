"""
Implement a function to check if a binary tree is binary search
tree.

- Search. Modified, in-order DFS and keep track of a global variable
last_visited. Check if left branch is binary search tree, if false,
return false. Check if current data is less or equal to global min, if
yes, retrun false. Update the last_visited. Check if the right branch
is balanced. (???)

NOTE: check only left.data <= current.data < right.data is not
sufficient. The requirement is that ALL left data <= current data <
ALL right data.

- DFS. Use a range (min, max). When branch left, the max gets updated
using current data. When branch right, the min updated using current
data. Then the (min, max) passed to the recursion of left or right
check. If the current data does not satisfy the passed range, return
false.
"""

def isBST(t, min=float('-inf'), max=float('inf')):
    if not min <= t.data < max:
        return False

    if t.left:
        isBST(t.left, min, t.data)
    if t.right:
        isBST(t.right, t.data, max)
